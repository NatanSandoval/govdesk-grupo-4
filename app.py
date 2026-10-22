import os
import sqlite3
from pathlib import Path

from flask import Flask, abort, g, redirect, render_template, request, url_for

PRIORIDADES = ["baixa", "média", "alta"]
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
        """)

    @app.route("/")
    def index():
        produtos = get_db().execute("""
            SELECT p.*, COALESCE(SUM(CASE WHEN m.tipo = 'entrada'
                THEN m.quantidade ELSE -m.quantidade END), 0) AS saldo
            FROM produtos p LEFT JOIN movimentacoes m ON m.produto_id = p.id
            GROUP BY p.id ORDER BY p.id
        """).fetchall()
        return render_template("index.html", produtos=produtos, total=len(produtos))

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

    return app


if __name__ == "__main__":
    porta = int(os.environ.get("PORT", 8080))
    create_app().run(host="0.0.0.0", port=porta)
