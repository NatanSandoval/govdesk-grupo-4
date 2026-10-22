# WBS do GovDesk

A raiz é o nível 1, os pacotes são o nível 2 e cada folha é o nível 3. Cada folha tem um executor de referência e cabe em aproximadamente uma hora ou menos. As estimativas não representam horas efetivamente trabalhadas.

```text
GovDesk — MVP
  1 Cadastro de produtos
    1.1 Criar tabela SQL de produtos e conexão Flask [H1; Guilherme; 1 h]
    1.2 Implementar formulário e gravação em /novo [H1; Guilherme; 1 h]
    1.3 Validar campos e preservar valores após erro [H2; Ruan; 1 h]
    1.4 Incluir aviso de privacidade e conferir escape HTML [H3; Natan; 30 min]
  2 Movimentações de estoque
    2.1 Criar tabela de movimentações e entrada inicial [H4; Ruan; 1 h]
    2.2 Implementar formulário de entrada e saída [H4; Ruan; 1 h]
    2.3 Validar saldo na mesma transação da saída [H4; Ruan; 1 h]
    2.4 Exibir histórico e verificar persistência [H4; Ruan; 1 h]
  3 Consulta e reposição
    3.1 Calcular saldos e exibir lista de produtos [H5; Guilherme; 1 h]
    3.2 Destacar mínimo e conferir navegação e estado vazio [H5; Guilherme; 30 min]
  4 Gestão e qualidade
    4.1 Elaborar backlog com responsáveis e critérios [H6; Max; 1 h]
    4.2 Elaborar WBS e registrar adaptação do exercício [H6; Max; 1 h]
    4.3 Executar testes automatizados e registrar resultados [H6; Max; 1 h]
    4.4 Executar roteiro manual com dados fictícios [H6; Natan; 30 min]
    4.5 Criar e atualizar cards da Sprint 1 no Trello [H6; Max; 1 h]
    4.6 Conferir contribuições e preparar envio ao professor [H6; Natan; 30 min]
  5 Evolução da Sprint 2
    5.1 Revisar adaptação e registrar decisão da PO [H7; Isabella; 1 h]
    5.2 Definir perfis e regras de acesso [H8; Guilherme; 1 h]
    5.3 Implementar autenticação de operadores [H8; Guilherme; 1 h]
    5.4 Restringir gravações e proteger formulários contra CSRF [H8; Guilherme; 1 h]
    5.5 Testar acessos permitidos e negados [H8; Natan; 1 h]
```

Os pacotes 1 a 4 organizam a Semana 6; o pacote 5 registra trabalho futuro. Os nomes representam os responsáveis de referência para revisão e continuidade, não comprovação de autoria da implementação assistida. A [RACI](raci.md) mantém um único A por atividade.
