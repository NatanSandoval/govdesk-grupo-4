import os
import sqlite3
from pathlib import Path

from flask import Flask, abort, g, redirect, render_template, request, url_for

PRIORIDADES = ["baixa", "média", "alta"]
STATUS_REPOSICAO = {"aberta": "Aberta", "em andamento": "Em andamento", "concluida": "Concluída"}
MAX_QUANTIDADE = 1_000_000_000

equipe = [
    {"nome": "Isabella Jacques", "papel": "Product Owner / CIO"},
    {"nome": "Guilherme Cimino", "papel": "Dev Lead"},
    {"nome": "Ruan Bauer", "papel": "Dev Lead"},
    {"nome": "Natan Correa", "papel": "QA / Auditoria"},
    {"nome": "Max Iago", "papel": "QA / Auditoria"},
]


def get_db():
    if "db" not in g:
        from flask import current_app
        g.db = sqlite3.connect(current_app.config["DATABASE"])
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA foreign_keys = ON")
    return g.db


def quantidade_inteira(valor, minimo=0):
    try:
        numero = int(valor)
    except (TypeError, ValueError):
        raise ValueError("Informe quantidades inteiras válidas.") from None
    if not minimo <= numero <= MAX_QUANTIDADE:
        raise ValueError(f"A quantidade deve estar entre {minimo} e {MAX_QUANTIDADE}.")
    return numero


def create_app(test_config=None):
    app = Flask(__name__)
    app.config["DATABASE"] = os.environ.get("GOVDESK_DATABASE", str(Path(app.instance_path) / "govdesk.sqlite3"))
    if test_config:
        app.config.update(test_config)
    Path(app.config["DATABASE"]).parent.mkdir(parents=True, exist_ok=True)

    @app.teardown_appcontext
    def close_db(exception=None):
        db = g.pop("db", None)
        if db is not None:
            db.close()

    with app.app_context():
        get_db().executescript("""
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                descricao TEXT NOT NULL DEFAULT '',
                responsavel TEXT NOT NULL,
                prioridade TEXT NOT NULL CHECK (prioridade IN ('baixa', 'média', 'alta')),
                estoque_minimo INTEGER NOT NULL CHECK (estoque_minimo >= 0)
            );
            CREATE TABLE IF NOT EXISTS movimentacoes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                produto_id INTEGER NOT NULL REFERENCES produtos(id),
                tipo TEXT NOT NULL CHECK (tipo IN ('entrada', 'saida')),
                quantidade INTEGER NOT NULL CHECK (quantidade > 0),
                responsavel TEXT NOT NULL,
                criado_em TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            );
            CREATE TABLE IF NOT EXISTS solicitacoes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                produto_id INTEGER NOT NULL REFERENCES produtos(id),
                quantidade INTEGER NOT NULL CHECK (quantidade > 0),
                descricao TEXT NOT NULL DEFAULT '',
                solicitante TEXT NOT NULL,
                prioridade TEXT NOT NULL CHECK (prioridade IN ('baixa', 'média', 'alta')),
                status TEXT NOT NULL DEFAULT 'aberta' CHECK (status IN ('aberta', 'em andamento', 'concluida')),
                criado_em TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                atualizado_em TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                movimentacao_id INTEGER UNIQUE REFERENCES movimentacoes(id)
            );
            CREATE TABLE IF NOT EXISTS historico_solicitacoes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                solicitacao_id INTEGER NOT NULL REFERENCES solicitacoes(id),
                status TEXT NOT NULL,
                responsavel TEXT NOT NULL,
                criado_em TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            );
        """)

    @app.route("/")
    def index():
        produtos = get_db().execute("""
            SELECT p.*, COALESCE(SUM(CASE WHEN m.tipo = 'entrada'
                THEN m.quantidade ELSE -m.quantidade END), 0) AS saldo
            FROM produtos p LEFT JOIN movimentacoes m ON m.produto_id = p.id
            GROUP BY p.id ORDER BY p.id
        """).fetchall()
        total = len(produtos)
        unidades = sum(p["saldo"] for p in produtos)
        abaixo_minimo = sum(p["saldo"] < p["estoque_minimo"] for p in produtos)
        pendentes = get_db().execute("SELECT COUNT(*) FROM solicitacoes WHERE status != 'concluida'").fetchone()[0]
        busca = request.args.get("q", "").strip().casefold()
        situacao = request.args.get("situacao", "")
        prioridade = request.args.get("prioridade", "")
        produtos = [p for p in produtos
                    if (not busca or busca in p["nome"].casefold() or busca in p["responsavel"].casefold())
                    and (situacao != "repor" or p["saldo"] < p["estoque_minimo"])
                    and (situacao != "regular" or p["saldo"] >= p["estoque_minimo"])
                    and (prioridade not in PRIORIDADES or p["prioridade"] == prioridade)]
        return render_template("index.html", produtos=produtos, total=total,
                               unidades=unidades, abaixo_minimo=abaixo_minimo, pendentes=pendentes)

    @app.route("/novo", methods=["GET", "POST"])
    def novo():
        erro = None
        if request.method == "POST":
            nome = request.form.get("nome", "").strip()
            descricao = request.form.get("descricao", "").strip()
            responsavel = request.form.get("responsavel", "").strip()
            prioridade = request.form.get("prioridade", "média")
            try:
                if not nome or not responsavel:
                    raise ValueError("Preencha o nome do produto e o responsável.")
                if prioridade not in PRIORIDADES:
                    raise ValueError("Prioridade inválida.")
                inicial = quantidade_inteira(request.form.get("estoque_inicial", "0"))
                minimo = quantidade_inteira(request.form.get("estoque_minimo", "0"))
                db = get_db()
                with db:
                    cursor = db.execute(
                        "INSERT INTO produtos (nome, descricao, responsavel, prioridade, estoque_minimo) VALUES (?, ?, ?, ?, ?)",
                        (nome, descricao, responsavel, prioridade, minimo))
                    if inicial:
                        db.execute("INSERT INTO movimentacoes (produto_id, tipo, quantidade, responsavel) VALUES (?, 'entrada', ?, ?)",
                                   (cursor.lastrowid, inicial, responsavel))
                return redirect(url_for("index"))
            except ValueError as exc:
                erro = str(exc)
        return render_template("novo.html", erro=erro, prioridades=PRIORIDADES, dados=request.form)

    @app.route("/produtos/<int:produto_id>/movimentar", methods=["GET", "POST"])
    def movimentar(produto_id):
        db = get_db()
        produto = db.execute("SELECT * FROM produtos WHERE id = ?", (produto_id,)).fetchone()
        if produto is None:
            abort(404)
        erro = None
        if request.method == "POST":
            try:
                tipo = request.form.get("tipo", "")
                responsavel = request.form.get("responsavel", "").strip()
                if tipo not in ("entrada", "saida"):
                    raise ValueError("Tipo de movimentação inválido.")
                if not responsavel:
                    raise ValueError("Informe o responsável pela movimentação.")
                quantidade = quantidade_inteira(request.form.get("quantidade"), minimo=1)
                # Validação de saldo e escrita ficam na mesma transação.
                with db:
                    db.execute("BEGIN IMMEDIATE")
                    saldo = db.execute("SELECT COALESCE(SUM(CASE WHEN tipo = 'entrada' THEN quantidade ELSE -quantidade END), 0) FROM movimentacoes WHERE produto_id = ?",
                                       (produto_id,)).fetchone()[0]
                    if tipo == "saida" and quantidade > saldo:
                        raise ValueError("Saldo insuficiente para essa saída.")
                    db.execute("INSERT INTO movimentacoes (produto_id, tipo, quantidade, responsavel) VALUES (?, ?, ?, ?)",
                               (produto_id, tipo, quantidade, responsavel))
                return redirect(url_for("index"))
            except ValueError as exc:
                erro = str(exc)
        historico = db.execute("SELECT * FROM movimentacoes WHERE produto_id = ? ORDER BY id DESC", (produto_id,)).fetchall()
        saldo = sum(m["quantidade"] if m["tipo"] == "entrada" else -m["quantidade"] for m in historico)
        return render_template("movimentar.html", produto=produto, historico=historico,
                               saldo=saldo, erro=erro, dados=request.form)

    @app.route("/sobre")
    def sobre():
        return render_template("sobre.html", equipe=equipe)

    @app.route("/solicitacoes")
    def solicitacoes():
        registros = get_db().execute("""
            SELECT s.*, p.nome AS produto FROM solicitacoes s
            JOIN produtos p ON p.id = s.produto_id ORDER BY s.id DESC
        """).fetchall()
        return render_template("solicitacoes.html", solicitacoes=registros, status_labels=STATUS_REPOSICAO)

    @app.route("/solicitacoes/nova", methods=["GET", "POST"])
    def nova_solicitacao():
        db = get_db()
        erro = None
        if request.method == "POST":
            try:
                produto_id = quantidade_inteira(request.form.get("produto_id"), minimo=1)
                quantidade = quantidade_inteira(request.form.get("quantidade"), minimo=1)
                solicitante = request.form.get("solicitante", "").strip()
                prioridade = request.form.get("prioridade", "média")
                descricao = request.form.get("descricao", "").strip()
                if not solicitante:
                    raise ValueError("Informe o solicitante.")
                if prioridade not in PRIORIDADES:
                    raise ValueError("Prioridade inválida.")
                if db.execute("SELECT id FROM produtos WHERE id = ?", (produto_id,)).fetchone() is None:
                    raise ValueError("Selecione um produto cadastrado.")
                with db:
                    cursor = db.execute("INSERT INTO solicitacoes (produto_id, quantidade, descricao, solicitante, prioridade) VALUES (?, ?, ?, ?, ?)",
                                        (produto_id, quantidade, descricao, solicitante, prioridade))
                    db.execute("INSERT INTO historico_solicitacoes (solicitacao_id, status, responsavel) VALUES (?, 'aberta', ?)",
                               (cursor.lastrowid, solicitante))
                return redirect(url_for("detalhe_solicitacao", solicitacao_id=cursor.lastrowid))
            except ValueError as exc:
                erro = str(exc)
        produtos = db.execute("SELECT id, nome FROM produtos ORDER BY nome, id").fetchall()
        return render_template("nova_solicitacao.html", produtos=produtos, erro=erro,
                               dados=request.form, prioridades=PRIORIDADES)

    @app.route("/solicitacoes/<int:solicitacao_id>")
    def detalhe_solicitacao(solicitacao_id):
        registro = get_db().execute("SELECT s.*, p.nome AS produto FROM solicitacoes s JOIN produtos p ON p.id = s.produto_id WHERE s.id = ?",
                                    (solicitacao_id,)).fetchone()
        if registro is None:
            abort(404)
        historico = get_db().execute("SELECT * FROM historico_solicitacoes WHERE solicitacao_id = ? ORDER BY id", (solicitacao_id,)).fetchall()
        return render_template("detalhe_solicitacao.html", solicitacao=registro,
                               historico=historico, status_labels=STATUS_REPOSICAO)

    @app.route("/solicitacoes/<int:solicitacao_id>/avancar", methods=["POST"])
    def avancar_solicitacao(solicitacao_id):
        db = get_db()
        responsavel = request.form.get("responsavel", "").strip()
        esperado = request.form.get("status_atual", "")
        try:
            with db:
                db.execute("BEGIN IMMEDIATE")
                registro = db.execute("SELECT * FROM solicitacoes WHERE id = ?", (solicitacao_id,)).fetchone()
                if registro is None:
                    abort(404)
                if not responsavel:
                    raise ValueError("Informe o responsável pela atualização.")
                if registro["status"] != esperado or registro["status"] == "concluida":
                    raise ValueError("Esta solicitação já foi atualizada. Recarregue a página antes de continuar.")
                proximo = "em andamento" if registro["status"] == "aberta" else "concluida"
                movimentacao_id = None
                if proximo == "concluida":
                    cursor = db.execute("INSERT INTO movimentacoes (produto_id, tipo, quantidade, responsavel) VALUES (?, 'entrada', ?, ?)",
                                        (registro["produto_id"], registro["quantidade"], responsavel))
                    movimentacao_id = cursor.lastrowid
                db.execute("UPDATE solicitacoes SET status = ?, atualizado_em = CURRENT_TIMESTAMP, movimentacao_id = ? WHERE id = ?",
                           (proximo, movimentacao_id, solicitacao_id))
                db.execute("INSERT INTO historico_solicitacoes (solicitacao_id, status, responsavel) VALUES (?, ?, ?)",
                           (solicitacao_id, proximo, responsavel))
            return redirect(url_for("detalhe_solicitacao", solicitacao_id=solicitacao_id))
        except ValueError as exc:
            return render_template("erro_solicitacao.html", erro=str(exc), solicitacao_id=solicitacao_id), 409

    @app.route("/indicadores")
    def indicadores():
        db = get_db()
        total_produtos = db.execute("SELECT COUNT(*) FROM produtos").fetchone()[0]
        abaixo_minimo = db.execute("""
            SELECT COUNT(*) FROM (
                SELECT p.id, p.estoque_minimo, COALESCE(SUM(CASE WHEN m.tipo = 'entrada'
                    THEN m.quantidade ELSE -m.quantidade END), 0) AS saldo
                FROM produtos p LEFT JOIN movimentacoes m ON m.produto_id = p.id
                GROUP BY p.id HAVING saldo < p.estoque_minimo
            )
        """).fetchone()[0]
        contagens = {r["status"]: r["total"] for r in db.execute("SELECT status, COUNT(*) AS total FROM solicitacoes GROUP BY status")}
        total = sum(contagens.values())
        concluidas = contagens.get("concluida", 0)
        return render_template("indicadores.html", total_produtos=total_produtos,
                               abaixo_minimo=abaixo_minimo, contagens=contagens,
                               total=total, concluidas=concluidas,
                               percentual=round(100 * concluidas / total, 1) if total else 0,
                               status_labels=STATUS_REPOSICAO)

    return app


if __name__ == "__main__":
    porta = int(os.environ.get("PORT", 8080))
    create_app().run(host="0.0.0.0", port=porta)
