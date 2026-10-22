import tempfile
import unittest
from pathlib import Path

from app import create_app, get_db


class EstoqueTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.config = {'TESTING': True, 'DATABASE': str(Path(self.temp.name) / 'teste.sqlite3')}
        self.app = create_app(self.config)
        self.client = self.app.test_client()

    def tearDown(self):
        self.temp.cleanup()

    def cadastrar(self, **alteracoes):
        dados = {'nome': '  Papel A4  ', 'descricao': '  Pacote fictício  ',
                 'responsavel': '  Operador fictício  ', 'prioridade': 'alta',
                 'estoque_inicial': '10', 'estoque_minimo': '5'}
        dados.update(alteracoes)
        return self.client.post('/novo', data=dados)

    def linhas(self, tabela):
        with self.app.app_context():
            return [dict(r) for r in get_db().execute('SELECT * FROM ' + tabela).fetchall()]

    def mover(self, **alteracoes):
        dados = {'tipo': 'saida', 'quantidade': '7', 'responsavel': 'Pessoa fictícia'}
        dados.update(alteracoes)
        return self.client.post('/produtos/1/movimentar', data=dados)

    def test_formulario_privacidade_e_prioridade_padrao(self):
        resposta = self.client.get('/novo')
        self.assertEqual(resposta.status_code, 200)
        html = resposta.get_data(as_text=True)
        for texto in ['name="nome"', 'name="descricao"', 'name="responsavel"',
                      'name="prioridade"', 'name="estoque_inicial"', 'name="estoque_minimo"',
                      'dados pessoais sensíveis', 'aria-describedby="orientacao-descricao"',
                      'value="média" selected']:
            self.assertIn(texto, html)

    def test_cadastro_persiste_produto_e_entrada_inicial(self):
        for prioridade in ['baixa', 'média', 'alta']:
            with self.subTest(prioridade=prioridade):
                resposta = self.cadastrar(prioridade=prioridade)
                self.assertEqual(resposta.status_code, 302)
                self.assertEqual(resposta.headers['Location'], '/')
                produto = self.linhas('produtos')[-1]
                self.assertEqual(produto['nome'], 'Papel A4')
                self.assertEqual(produto['descricao'], 'Pacote fictício')
                self.assertEqual(produto['responsavel'], 'Operador fictício')
                self.assertEqual(produto['prioridade'], prioridade)
                self.assertEqual(self.linhas('movimentacoes')[-1]['quantidade'], 10)
        produtos = self.linhas('produtos')
        self.assertEqual(len({p['id'] for p in produtos}), 3)
        html = self.client.get('/').get_data(as_text=True)
        self.assertIn('Papel A4', html)
        self.assertIn('Operador fictício', html)

    def test_obrigatorios_ausentes_vazios_e_espacos(self):
        for campo in ['nome', 'responsavel']:
            for valor in [None, '', '   ']:
                with self.subTest(campo=campo, valor=valor):
                    dados = {'nome': 'Papel', 'responsavel': 'Pessoa fictícia',
                             'descricao': 'Descrição preservada', 'prioridade': 'alta',
                             'estoque_inicial': '8', 'estoque_minimo': '2'}
                    if valor is None:
                        dados.pop(campo)
                    else:
                        dados[campo] = valor
                    html = self.client.post('/novo', data=dados).get_data(as_text=True)
                    for texto in ['Preencha o nome do produto e o responsável.',
                                  'Descrição preservada', 'value="alta" selected', 'value="8"', 'value="2"']:
                        self.assertIn(texto, html)
                    self.assertEqual(self.linhas('produtos'), [])
                    self.assertEqual(self.linhas('movimentacoes'), [])

    def test_prioridades_invalidas(self):
        for prioridade in ['urgente', '', 'ALTA']:
            resposta = self.cadastrar(prioridade=prioridade)
            self.assertIn('Prioridade inválida.', resposta.get_data(as_text=True))
        self.assertEqual(self.linhas('produtos'), [])

    def test_quantidades_invalidas_nao_criam_registros(self):
        for campo in ['estoque_inicial', 'estoque_minimo']:
            for valor in ['-1', '1.5', 'abc', '', '1000000001', '999999999999999999999999']:
                with self.subTest(campo=campo, valor=valor):
                    html = self.cadastrar(**{campo: valor}).get_data(as_text=True)
                    self.assertIn('role="alert"', html)
                    self.assertEqual(self.linhas('produtos'), [])
                    self.assertEqual(self.linhas('movimentacoes'), [])

    def test_cadastro_sem_opcionais_e_estoque_zero(self):
        resposta = self.client.post('/novo', data={'nome': 'Papel', 'responsavel': 'Pessoa fictícia'})
        self.assertEqual(resposta.status_code, 302)
        produto = self.linhas('produtos')[0]
        self.assertEqual(produto['descricao'], '')
        self.assertEqual(produto['prioridade'], 'média')
        self.assertEqual(produto['estoque_minimo'], 0)
        self.assertEqual(self.linhas('movimentacoes'), [])

    def test_entrada_saida_alerta_e_historico(self):
        self.cadastrar()
        self.assertEqual(self.mover().status_code, 302)
        html = self.client.get('/').get_data(as_text=True)
        self.assertIn('Abaixo do mínimo', html)
        self.assertIn('<td>3</td>', html)
        self.assertEqual(self.mover(tipo='entrada', quantidade='2').status_code, 302)
        html = self.client.get('/').get_data(as_text=True)
        self.assertNotIn('Abaixo do mínimo', html)
        self.assertIn('Regular', html)
        historico = self.client.get('/produtos/1/movimentar')
        self.assertEqual(historico.status_code, 200)
        self.assertIn('Pessoa fictícia', historico.get_data(as_text=True))
        self.assertEqual(len(self.linhas('movimentacoes')), 3)

    def test_saida_insuficiente_preserva_saldo_e_campos(self):
        self.cadastrar()
        resposta = self.mover(quantidade='11')
        html = resposta.get_data(as_text=True)
        for texto in ['Saldo insuficiente', 'value="11"', 'Pessoa fictícia', 'value="saida" selected']:
            self.assertIn(texto, html)
        self.assertEqual(len(self.linhas('movimentacoes')), 1)
        self.assertEqual(self.mover(quantidade='10').status_code, 302)
        self.assertIn('Saldo insuficiente', self.mover(quantidade='1').get_data(as_text=True))
        self.assertEqual(len(self.linhas('movimentacoes')), 2)

    def test_movimentacoes_invalidas(self):
        self.cadastrar()
        for alteracoes in [{'tipo': 'ajuste'}, {'responsavel': '  '},
                           {'quantidade': '0'}, {'quantidade': '-1'},
                           {'quantidade': '1.5'}, {'quantidade': 'abc'},
                           {'quantidade': '1000000001'}]:
            with self.subTest(alteracoes=alteracoes):
                self.assertIn('role="alert"', self.mover(**alteracoes).get_data(as_text=True))
                self.assertEqual(len(self.linhas('movimentacoes')), 1)
        for metodo in [self.client.get, self.client.post]:
            self.assertEqual(metodo('/produtos/999/movimentar').status_code, 404)

    def test_persistencia_ao_recriar_aplicacao(self):
        self.cadastrar()
        self.mover()
        outra_app = create_app(self.config)
        outro_client = outra_app.test_client()
        html = outro_client.get('/').get_data(as_text=True)
        self.assertIn('Papel A4', html)
        self.assertIn('<td>3</td>', html)
        self.assertIn('Abaixo do mínimo', html)

    def test_html_escapado_e_sql_parametrizado(self):
        nome = '<script>alert("teste")</script>'
        responsavel = "Pessoa fictícia'); DROP TABLE produtos; --"
        self.cadastrar(nome=nome, responsavel=responsavel)
        html = self.client.get('/').get_data(as_text=True)
        self.assertNotIn(nome, html)
        self.assertIn('&lt;script&gt;', html)
        self.assertEqual(self.linhas('produtos')[0]['responsavel'], responsavel)
        html = self.cadastrar(nome=nome, responsavel='').get_data(as_text=True)
        self.assertNotIn(nome, html)
        self.assertIn('&lt;script&gt;', html)

    def test_estado_vazio_e_equipe(self):
        inicio = self.client.get('/')
        self.assertEqual(inicio.status_code, 200)
        self.assertIn('Nenhum produto cadastrado', inicio.get_data(as_text=True))
        sobre = self.client.get('/sobre')
        self.assertEqual(sobre.status_code, 200)
        for nome in ['Isabella Jacques', 'Guilherme Cimino', 'Ruan Bauer', 'Natan Correa', 'Max Iago']:
            self.assertIn(nome, sobre.get_data(as_text=True))


if __name__ == '__main__':
    unittest.main()
