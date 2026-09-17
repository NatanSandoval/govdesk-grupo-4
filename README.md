# GovDesk — Gerenciamento de Estoques

Projeto desenvolvido para a disciplina de Gestão e Governança de Tecnologia da Informação. O GovDesk tem como escopo o gerenciamento de estoques em ambiente governamental/corporativo, conforme o [Plano Estratégico de TI](docs/PETI.md).

O sistema planejado contempla cadastro de produtos, registro de entradas e saídas, consulta de saldos e alertas de estoque mínimo, para reduzir perdas e falhas de suprimento.

**Estado atual:** a aplicação Flask ainda contém o protótipo inicial de chamados. As funcionalidades de estoque descritas no PETI são o escopo a implementar; esta entrega organiza a documentação e as responsabilidades.

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

Alterações relevantes de escopo devem ser registradas usando o template e submetidas à pessoa responsável pela aprovação na matriz RACI antes da implementação.

## Gestão e Organização (Kanban)

O acompanhamento das tarefas e entregas das semanas é feito através do quadro Trello do grupo:

* **Board do Trello:** [Acessar Trello do GovDesk - Grupo 4](https://trello.com/invite/b/6a98ddf57454667a93f97381/ATTId824acd5765d91a1e7acdfe7deb366a3782109BD/govdesk-grupo-4)

## Como Executar o Projeto Localmente

1. Clone o repositório:

   ```bash
   git clone https://github.com/NatanSandoval/govdesk-grupo-4.git
   cd govdesk-grupo-4
   ```

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. Execute a aplicação Flask:

   ```bash
   python app.py
   ```

4. Acesse http://localhost:8080 (ou o endereço e porta informados no terminal).
