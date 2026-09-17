# Matriz RACI do Projeto

Esta matriz distribui as responsabilidades do GovDesk para o escopo de gerenciamento de estoques definido no PETI, preservando os papéis da equipe registrados no README.

- **R — Responsible:** executa a atividade.
- **A — Accountable:** responde pelo resultado e pela aprovação final da atividade.
- **C — Consulted:** é consultado antes da decisão ou conclusão.
- **I — Informed:** é informado sobre a decisão ou o resultado.
- **A/R:** a mesma pessoa executa e responde pelo resultado.

Cada atividade possui exatamente uma pessoa com A, inclusive quando combinado como A/R. Mais de uma pessoa pode executar a atividade, mas a responsabilidade final é individual.

| Atividade | Isabella Jacques (Product Owner / CIO) | Guilherme Cimino (Dev Lead) | Ruan Bauer (Dev Lead) | Natan Correa (QA / Auditoria) | Max Iago (QA / Auditoria) |
| --- | --- | --- | --- | --- | --- |
| Definir prioridades do backlog e regras de negócio de estoque | A/R | C | C | C | I |
| Modelar as tabelas de produtos e movimentações e integrar o banco SQL ao Flask | C | A/R | R | C | I |
| Implementar cadastro de produtos e registro de entradas e saídas | C | C | A/R | C | I |
| Implementar consulta de saldos e alertas de estoque mínimo | C | A/R | R | C | I |
| Testar movimentações, consistência dos saldos e alertas de estoque | I | C | C | A/R | R |
| Validar usabilidade, formulários e rotas da aplicação | C | C | C | R | A/R |
| Avaliar e aprovar solicitações de mudança de escopo | A/R | C | C | C | C |
| Documentar decisões e manter a rastreabilidade das entregas no GitHub | C | R | C | C | A/R |
| Atualizar o Kanban após verificar os critérios de conclusão da entrega | A | I | I | R | C |

## Aplicação da matriz

Guilherme e Ruan compartilham o papel de Dev Lead, mas têm responsabilidades finais distintas nas atividades acima. Natan e Max compartilham QA / Auditoria, também com um único A por atividade.

Mudanças relevantes de escopo devem usar o arquivo `template-mudanca.md`. Isabella Jacques, como Product Owner / CIO e A da aprovação de mudanças, decide após consultar Desenvolvimento e QA sobre impacto e risco. A aprovação de uma mudança não significa que sua implementação ou validação esteja concluída.
