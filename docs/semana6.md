# Entrega da Semana 6 do GovDesk

A entrega aplica o planejamento e o protótipo funcional da Semana 6 ao gerenciamento de estoques do PETI, conforme orientação do grupo em 22 de outubro de 2026. O formulário `/novo` cadastra produtos, valida campos e mostra aviso de privacidade. Produtos e movimentações são persistidos em SQLite; a página inicial calcula saldos e alerta quando estão abaixo do mínimo.

## Correspondência com o exercício

| Item do enunciado | Adaptação entregue |
| --- | --- |
| Título do chamado | Nome do produto |
| Descrição do chamado | Descrição do produto com aviso de privacidade |
| Solicitante | Responsável pelo cadastro |
| Prioridade | Prioridade de reposição baixa, média ou alta |
| Lista de chamados | Lista de produtos com saldo, mínimo, responsável e prioridade |
| Status aberto | Situação de estoque calculada como Regular ou Abaixo do mínimo |
| Lista em memória | Tabelas SQLite de produtos e movimentações |
| Kanban do GitHub Projects | Trello indicado pelo grupo com A fazer, Fazendo e Pronto |

## Evidências

- [Backlog](backlog.md): oito histórias, seis na Sprint 1, com critérios de aceite, prioridades e responsáveis.
- [WBS](wbs.md): até três níveis, tarefas finais estimadas em no máximo uma hora.
- [Testes](testes-semana6.md): 12 testes automatizados aprovados e roteiro manual reproduzível.
- [RACI](raci.md), [PETI](PETI.md) e [privacidade](lgpd.md): contexto e responsabilidades.
- [Quadro do Trello](https://trello.com/b/ztGAnpaq/govdesk-grupo-4): cards por ID da história.
- [Índice dos cards](kanban.md): links diretos para H1 a H6.
- [Repositório para entrega](https://github.com/NatanSandoval/govdesk-grupo-4).

## Conclusão técnica e ações do grupo

O código e a documentação são uma implementação assistida. A indicação de responsáveis no planejamento não é prova de execução ou aprovação individual. Cada integrante precisa realizar sua revisão e registrar sua própria contribuição em commit, sem alteração artificial de autoria. O grupo também precisa enviar o link ao professor pelo canal da disciplina; esse envio não foi realizado por esta entrega.

H7, revisão da PO, e H8, controle de acesso, ficam propostas para a Sprint 2. A PO deve registrar sua decisão sobre prioridades e histórias adiadas, em vez de ser apresentada como autora de uma aprovação que ainda não registrou.
