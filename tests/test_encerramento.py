import sqlite3
import tempfile
import unittest
from pathlib import Path

from app import create_app, get_db


class EncerramentoTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.config = {'TESTING': True, 'DATABASE': str(Path(self.temp.name) / 'estoque.sqlite3')}
        self.app = create_app(self.config)
        self.client = self.app.test_client()
        self.client.post('/novo', data={'nome': 'Papel fictício', 'responsavel': 'Operador teste',
                                        'estoque_inicial': '2', 'estoque_minimo': '5'})

    def tearDown(self):
        self.temp.cleanup()

    def abrir(self, **alteracoes):
        dados = {'produto_id': '1', 'quantidade': '8', 'solicitante': 'Pessoa teste',
                 'prioridade': 'alta', 'descricao': 'Reposição fictícia'}
        dados.update(alteracoes)
        return self.client.post('/solicitacoes/nova', data=dados)

    def avancar(self, status='aberta', responsavel='Técnico teste'):
        return self.client.post('/solicitacoes/1/avancar', data={'status_atual': status, 'responsavel': responsavel})

    def registros(self, tabela):
        with self.app.app_context():
            return [dict(r) for r in get_db().execute('SELECT * FROM ' + tabela)]

    def test_paginas_vazias_e_aviso(self):
        for rota in ['/solicitacoes', '/solicitacoes/nova', '/indicadores']:
            self.assertEqual(self.client.get(rota).status_code, 200)
        self.assertIn('Nenhuma solicitação', self.client.get('/solicitacoes').get_data(as_text=True))
        html = self.client.get('/solicitacoes/nova').get_data(as_text=True)
        self.assertIn('Aviso de privacidade', html)
        self.assertIn('aria-describedby="orientacao-reposicao"', html)
        html = self.client.get('/indicadores').get_data(as_text=True)
        self.assertIn('0%', html)

    def test_fluxo_completo_e_recebimento_unico(self):
        resposta = self.abrir()
        self.assertEqual(resposta.status_code, 302)
        self.assertEqual(resposta.headers['Location'], '/solicitacoes/1')
        self.assertEqual(self.registros('solicitacoes')[0]['status'], 'aberta')
        self.assertEqual(len(self.registros('movimentacoes')), 1)
        self.assertEqual(self.avancar().status_code, 302)
        self.assertEqual(self.registros('solicitacoes')[0]['status'], 'em andamento')
        self.assertEqual(len(self.registros('movimentacoes')), 1)
        self.assertEqual(self.avancar('em andamento').status_code, 302)
        s = self.registros('solicitacoes')[0]
        self.assertEqual(s['status'], 'concluida')
        self.assertIsNotNone(s['movimentacao_id'])
        self.assertEqual(self.registros('movimentacoes')[-1]['quantidade'], 8)
        self.assertEqual(self.registros('movimentacoes')[-1]['tipo'], 'entrada')
        self.assertEqual(len(self.registros('historico_solicitacoes')), 3)
        self.assertIn('<td>10</td>', self.client.get('/').get_data(as_text=True))
        for estado in ['aberta', 'em andamento', 'concluida']:
            self.assertEqual(self.avancar(estado).status_code, 409)
        self.assertEqual(len(self.registros('movimentacoes')), 2)

    def test_campos_invalidos_nao_gravam(self):
        casos = [{'produto_id': ''}, {'produto_id': '999'}, {'produto_id': 'abc'},
                 {'quantidade': '0'}, {'quantidade': '-1'}, {'quantidade': '1.5'},
                 {'quantidade': '1000000001'}, {'quantidade': ''}, {'solicitante': '  '},
                 {'prioridade': 'urgente'}]
        for dados in casos:
            with self.subTest(dados=dados):
                html = self.abrir(**dados).get_data(as_text=True)
                self.assertIn('role="alert"', html)
                self.assertIn('Reposição fictícia', html)
                self.assertEqual(self.registros('solicitacoes'), [])
                self.assertEqual(self.registros('historico_solicitacoes'), [])

    def test_campos_ausentes_e_valores_padrao(self):
        self.assertEqual(self.client.post('/solicitacoes/nova', data={}).status_code, 200)
        resposta = self.client.post('/solicitacoes/nova', data={
            'produto_id': '1', 'quantidade': '1', 'solicitante': '  Pessoa teste  '})
        self.assertEqual(resposta.status_code, 302)
        s = self.registros('solicitacoes')[0]
        self.assertEqual(s['prioridade'], 'média')
        self.assertEqual(s['descricao'], '')
        self.assertEqual(s['solicitante'], 'Pessoa teste')

    def test_status_obsoleto_e_responsavel_obrigatorio(self):
        self.abrir()
        for status, pessoa in [('concluida', 'Pessoa'), ('aberta', '  '), ('', 'Pessoa')]:
            self.assertEqual(self.avancar(status, pessoa).status_code, 409)
        self.assertEqual(self.registros('solicitacoes')[0]['status'], 'aberta')
        self.avancar()
        self.assertEqual(self.avancar().status_code, 409)
        self.assertEqual(self.registros('solicitacoes')[0]['status'], 'em andamento')
        self.assertEqual(len(self.registros('movimentacoes')), 1)

    def test_inexistente_e_get_nao_alteram(self):
        self.assertEqual(self.client.get('/solicitacoes/999').status_code, 404)
        self.assertEqual(self.client.post('/solicitacoes/999/avancar').status_code, 404)
        self.abrir()
        self.assertEqual(self.client.get('/solicitacoes/1/avancar').status_code, 405)
        self.client.get('/solicitacoes/1')
        self.assertEqual(self.registros('solicitacoes')[0]['status'], 'aberta')

    def test_indicadores_com_dados_e_percentual(self):
        self.abrir()
        self.abrir()
        self.abrir()
        self.avancar()
        self.avancar('em andamento')
        html = self.client.get('/indicadores').get_data(as_text=True)
        self.assertIn('33.3%', html)
        self.assertIn('<td>Produtos abaixo do mínimo</td><td>0</td>', html)
        self.assertIn('<td>Aberta</td><td>2</td>', html)
        self.assertIn('<td>Concluída</td><td>1</td>', html)

    def test_persistencia_de_status_e_historico(self):
        self.abrir()
        self.avancar()
        outra = create_app(self.config).test_client()
        html = outra.get('/solicitacoes/1').get_data(as_text=True)
        self.assertIn('Em andamento', html)
        self.assertIn('Técnico teste', html)

    def test_falha_de_gravacao_reverte_recebimento_e_status(self):
        self.abrir()
        self.avancar()
        with self.app.app_context():
            get_db().executescript("CREATE TRIGGER falha_recebimento BEFORE INSERT ON historico_solicitacoes WHEN NEW.status = 'concluida' BEGIN SELECT RAISE(ABORT, 'falha simulada'); END;")
        with self.assertRaises(sqlite3.IntegrityError):
            self.avancar('em andamento')
        self.assertEqual(len(self.registros('movimentacoes')), 1)
        self.assertEqual(self.registros('solicitacoes')[0]['status'], 'em andamento')
        self.assertEqual(len(self.registros('historico_solicitacoes')), 2)

    def test_migracao_aditiva_preserva_estoque(self):
        # Simula banco anterior à Semana 10 mantendo os dados de produtos e movimentos.
        with self.app.app_context():
            get_db().executescript('DROP TABLE historico_solicitacoes; DROP TABLE solicitacoes;')
        outra_app = create_app(self.config)
        self.assertIn('Papel fictício', outra_app.test_client().get('/').get_data(as_text=True))
        self.assertEqual(len(self.registros('movimentacoes')), 1)
        self.assertEqual(self.registros('solicitacoes'), [])

    def test_html_escapado_e_sem_produto(self):
        self.abrir(descricao='<script>alert(1)</script>')
        html = self.client.get('/solicitacoes/1').get_data(as_text=True)
        self.assertIn('&lt;script&gt;', html)
        self.assertNotIn('<script>alert(1)</script>', html)
        vazia = create_app({'TESTING': True, 'DATABASE': str(Path(self.temp.name) / 'vazio.sqlite3')})
        html = vazia.test_client().get('/solicitacoes/nova').get_data(as_text=True)
        self.assertIn('Cadastre um produto', html)

    def test_filtros_de_estoque_combinados_e_busca(self):
        self.client.post('/novo', data={'nome': 'Caneta demonstrativa', 'responsavel': 'Equipe demo',
                                        'prioridade': 'alta', 'estoque_inicial': '10', 'estoque_minimo': '3'})
        for query in ['q=CANETA', 'q=Equipe', 'situacao=regular&prioridade=alta']:
            with self.subTest(query=query):
                html = self.client.get('/?' + query).get_data(as_text=True)
                self.assertIn('Caneta demonstrativa', html)
                self.assertNotIn('Papel fictício', html)
                self.assertIn('Exibindo 1 de 2 produtos', html)
        html = self.client.get('/?situacao=repor').get_data(as_text=True)
        self.assertIn('Papel fictício', html)
        self.assertNotIn('Caneta demonstrativa', html)

    def test_busca_sem_resultados_e_identidade(self):
        html = self.client.get('/?q=produto-inexistente').get_data(as_text=True)
        self.assertIn('Nenhum produto encontrado', html)
        self.assertIn('Exibindo 0 de 1 produtos', html)
        self.assertIn('ProntoEstoque', html)
        for asset in ['/static/app.css', '/static/app.js']:
            with self.client.get(asset) as resposta:
                self.assertEqual(resposta.status_code, 200)


if __name__ == '__main__':
    unittest.main()
