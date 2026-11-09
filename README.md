# ProntoEstoque

Nome atual da aplicação desenvolvida como GovDesk na disciplina. O ProntoEstoque reúne catálogo, movimentações e reposições em uma interface responsiva, com identidade visual própria, busca e filtros de estoque. O nome do repositório e as referências históricas da disciplina permanecem identificados como GovDesk.

Projeto desenvolvido para a disciplina de Gestão e Governança de Tecnologia da Informação. O GovDesk tem como escopo o gerenciamento de estoques em ambiente governamental/corporativo, conforme o [Plano Estratégico de TI](docs/PETI.md).

O sistema planejado contempla cadastro de produtos, registro de entradas e saídas, consulta de saldos e alertas de estoque mínimo, para reduzir perdas e falhas de suprimento.

**Entrega final da Semana 10:** protótipo funcional de estoque com cadastro de produtos em `/novo`, validação, aviso de privacidade, entradas e saídas, histórico, saldos e alertas de mínimo. Solicitações de reposição avançam de Aberta para Em andamento e Concluída; confirmar o recebimento registra a entrada no estoque. O painel `/indicadores` mostra a posição do banco local. Os dados são persistidos em SQLite. Mantivemos a adaptação do exercício para o domínio de estoques escolhida pelo grupo na Semana 6.

O código e a documentação estão preparados para apresentação. O encerramento formal depende do aceite da PO, das validações pessoais e do envio ao professor, conforme o [termo de encerramento](docs/encerramento.md).

## Equipe do Projeto

| Nome | Papel | Responsabilidade Principal |
| :--- | :--- | :--- |
| **Isabella Jacques** | Product Owner / CIO | Prioriza as funcionalidades, regras de negócio e entregas de cada semana. |
| **Guilherme Cimino** e **Ruan Bauer** | Dev Lead | Organizam a arquitetura do código Flask, a estrutura de diretórios e a execução da aplicação. |
| **Natan Correa** e **Max Iago** | QA / Auditoria | Realizam testes de usabilidade, validação de rotas e mantêm o histórico de commits organizado no GitHub. |

A distribuição individual das responsabilidades está na [matriz RACI](docs/raci.md).

## Documentação e governança

- [Plano Estratégico de TI](docs/PETI.md)
- [Matriz RACI](docs/raci.md)
- [Template de solicitação de mudança](docs/template-mudanca.md)
- [Backlog da Sprint 1 e próximas entregas](docs/backlog.md)
- [WBS do MVP](docs/wbs.md)
- [Cards do Kanban](docs/kanban.md)
- [Testes e roteiro de validação](docs/testes-semana6.md)
- [Entrega e adaptação da Semana 6](docs/semana6.md)
- [Privacidade](docs/lgpd.md)
- [Processo TO-BE com BPMN editável](docs/processo-chamados.md)
- [Plano de melhoria contínua e BSC](docs/melhoria-continua.md)
- [Termo de encerramento e aceite pendente](docs/encerramento.md)
- [Lições aprendidas para validação dos integrantes](docs/licoes-aprendidas.md)
- [Operação, backup e sustentação](docs/sustentacao.md)
- [Testes e checklist final](docs/testes-semana10.md)
- [Roteiro da apresentação em oito minutos](docs/apresentacao.md)
- [PowerPoint editável da apresentação](docs/apresentacao/prontoestoque-semana10.pptx)
- [Autoavaliação individual para preenchimento](docs/autoavaliacao.md)
- [Respostas e checklist do PDF da Semana 10](docs/respostas-semana10.md)

Alterações relevantes de escopo devem ser registradas usando o template e submetidas à pessoa responsável pela aprovação na matriz RACI antes da implementação.

## Gestão e Organização (Kanban)

O acompanhamento das tarefas e entregas das semanas é feito através do quadro Trello do grupo:

* **Board do Trello:** [Acessar Trello do GovDesk - Grupo 4](https://trello.com/b/ztGAnpaq/govdesk-grupo-4)

## Como Executar o Projeto Localmente

1. Clone o repositório:

   ```bash
   git clone https://github.com/NatanSandoval/govdesk-grupo-4.git
   cd govdesk-grupo-4
   ```

2. Use Python 3.10 ou superior e instale as dependências:

   ```bash
   python -m pip install -r requirements.txt
   ```

3. Execute a aplicação Flask:

   ```bash
   python app.py
   ```

4. Acesse http://localhost:8080 (ou o endereço e porta informados no terminal).

No Replit, o arquivo `.replit` define `python app.py` para o botão Run. Instale primeiro as dependências de `requirements.txt`. A variável `PORT` permite alterar a porta, cujo padrão é 8080.

O banco `instance/govdesk.sqlite3` e as tabelas são criados automaticamente na primeira execução. O estoque começa vazio; use dados fictícios. Para escolher outro arquivo de banco, configure a variável `GOVDESK_DATABASE`. O saldo é calculado pelas entradas menos as saídas; saídas acima do disponível são bloqueadas. O mínimo é um limite de alerta e não impede consumo. A prioridade é de reposição e não um status de chamado.

## Executar os testes

No ambiente em que as dependências foram instaladas:

```bash
python -m unittest discover -s tests -v
```

Os testes usam bancos temporários e não alteram o estoque local. A aplicação também pode ser iniciada por `flask --app app run --port 8080`, que identifica a fábrica `create_app`.

## Limites do protótipo

A criação das tabelas de reposição é aditiva: o app não apaga produtos ou movimentações já existentes. O recebimento é integral; uma confirmação final grava status, entrada e histórico na mesma transação. Páginas com status desatualizado recebem 409 e devem ser recarregadas. Cada avanço exige responsável e mantém a data UTC.

Use apenas em ambiente acadêmico com dados fictícios: autenticação, autorização e proteção CSRF estão previstas em H8. O aviso de privacidade não substitui controles de acesso nem comprova conformidade jurídica. A tabela LGPD original descreve o sistema planejado; os dados efetivamente gravados pelo protótipo estão detalhados em `docs/lgpd.md`.

## Backlog futuro e encerramento

H7 é a revisão da PO. H8 cobre autenticação, autorização e CSRF. H12 trata backup ensaiado, H13 recebimentos parciais e cancelamento, e H14 linha de base de indicadores operacionais. Critérios e responsáveis em [backlog.md](docs/backlog.md). Essas melhorias não estão apresentadas como funcionalidades prontas.

O grupo deve validar as lições e a sustentação, preencher autoavaliações, registrar o aceite da PO, confirmar os commits individuais e enviar o link ao professor. Após o último commit da entrega, congelar alterações até terminar a apresentação. As falas dos cinco integrantes estão no roteiro.
