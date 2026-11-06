# WBS do ProntoEstoque

A raiz é o nível 1, os pacotes são o nível 2 e cada folha é o nível 3. Cada folha tem um executor de referência e cabe em aproximadamente uma hora ou menos. As estimativas não representam horas efetivamente trabalhadas.

```text
ProntoEstoque — MVP
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

## Extensão da WBS para encerramento

Os pacotes abaixo continuam sob a mesma raiz ProntoEstoque — MVP. A raiz é o nível 1, os pacotes 6 a 8 são o nível 2 e as folhas são o nível 3. As estimativas são propostas e não registros de trabalho individual.

```text
ProntoEstoque — MVP
  6 Solicitações e indicadores
    6.1 Criar tabelas e formulário de reposição [H9; Ruan; 1 h]
    6.2 Implementar avanço e histórico [H9; Ruan; 1 h]
    6.3 Vincular recebimento único e transação [H9; Ruan; 1 h]
    6.4 Implementar painel e fórmulas [H10; Guilherme; 1 h]
    6.5 Verificar migração, reenvio e reversão de falha [H9; Natan; 1 h]
  7 Documentação e apresentação
    7.1 Consolidar RACI e BPMN TO-BE [H11; Max; 1 h]
    7.2 Consolidar BSC, não conformidades e roadmap [H11; Max; 1 h]
    7.3 Preparar termo e procedimentos de sustentação [H11; Guilherme; 1 h]
    7.4 Revisar lições com cada integrante [H11; todos; 1 h]
    7.5 Preparar roteiro e apresentação [H11; Isabella; 1 h]
    7.6 Executar go/no-go e conferir Kanban [H11; Natan; 1 h]
  8 Aceite e entrega pelo grupo
    8.1 Registrar aceite e ressalvas da PO [H7; Isabella; 30 min]
    8.2 Preencher autoavaliações individualmente [H11; todos; 30 min]
    8.3 Conferir commits, enviar link e congelar versão [H11; Natan; 30 min]
    8.4 Ensaiar oito minutos e perguntas [H11; todos; 30 min]
```

Na revisão do PDF, as folhas 7.6, 8.1, 7.4, 8.4 e 8.2 correspondem, respectivamente, aos cards S10-01 a S10-05. A folha 8.3 foi desdobrada nos cards S10-06 (conferir contribuições) e S10-07 (envio e congelamento), mantendo a estimativa total proposta de 30 minutos. Links e estados em [kanban.md](kanban.md). Preparar documentos não conclui essas ações do grupo.
