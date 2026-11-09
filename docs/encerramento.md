# Termo de encerramento do ProntoEstoque

Versão de entrega acadêmica preparada em 5 de novembro de 2026. O encerramento formal depende do aceite da Product Owner registrado ao final deste termo.

## Escopo planejado e entregue

O PETI define gestão de estoques: cadastro de produtos, entradas e saídas, saldos e alertas de mínimo. A Semana 10 acrescenta o ciclo de atendimento solicitado pelo exercício, adaptado para solicitações de reposição.

| Planejado | Entrega verificável | Situação |
| --- | --- | --- |
| Cadastro com validação e privacidade | /novo com produto, responsável, prioridade, quantidades e aviso visível | implementado |
| Movimentações e saldos | Entradas e saídas em SQLite, bloqueio de saldo negativo, histórico UTC e alerta de mínimo | implementado |
| Abertura e avanço de status | /solicitacoes/nova e detalhe com Aberta, Em andamento e Concluída | implementado |
| Reposição recebida | Conclusão registra uma entrada integral, na mesma transação do status e histórico | implementado |
| Indicadores | /indicadores com produtos, itens abaixo do mínimo, solicitações por status e percentual concluído | implementado |
| Governança e transferência | PETI, LGPD, RACI, backlog, WBS, BPMN TO-BE, melhoria, lições, sustentação e roteiro | documentado |
| Aceite e apresentação | Campos de aceite, autoavaliações e apresentação preparados | execução e validação pelo grupo pendentes |

O protótipo cobre o fluxo acadêmico. Autenticação, perfis, CSRF, recebimento parcial, cancelamento e integração com compras não fazem parte desta versão. Os papéis da RACI organizam responsabilidades da equipe e não são permissões de acesso implementadas.

## Resultados e indicadores

- 25 testes automatizados aprovados em 5 de novembro de 2026: 12 de estoque e 13 da continuação e interface da Semana 10. Evidências em [testes](testes-semana10.md).
- Migração aditiva cria tabelas de solicitações e histórico, preservando produtos e movimentações existentes. Teste de atualização incluído.
- Reenvio de avanço com status desatualizado recebe 409. Recebimento, mudança de status e histórico são atômicos e têm teste de reversão de falha.
- Indicadores do painel são calculados no banco local. Não há medição operacional que comprove redução de perdas, satisfação ou eliminação de divergências físicas.

As fórmulas, metas propostas e limitações constam no [plano de melhoria](melhoria-continua.md).

## Pendências e riscos residuais

| Item | Impacto | Plano e responsável de referência |
| --- | --- | --- |
| Sem autenticação, autorização e CSRF | Escrita aberta no protótipo | Guilherme e Ruan: H8 antes de qualquer uso com dados reais |
| Recebimento somente integral, sem cancelamento | Fluxo não representa entregas parciais ou desistência | PO: priorizar H13 no backlog futuro |
| Banco local sem rotina automática de backup | Falha no dispositivo pode perder registros | Guilherme: copiar banco com aplicação parada e testar restauração conforme sustentacao.md |
| Dados pessoais em campos livres | Exposição indevida na lista ou no histórico | QA: manter exemplos fictícios e revisar formulários, retenção e acesso antes da implantação |
| Ausência de evidência operacional | Metas do PETI ainda não comprovadas | PO: definir linha de base, piloto e coleta de indicadores |
| Aceite, lições pessoais e autoavaliações | Encerramento acadêmico depende do grupo | Cada integrante valida sua seção; Isabella registra aceite; grupo envia o link ao professor |

## Sustentação

Dona de referência do sistema e aprovadora de mudanças: Isabella Jacques, Product Owner / CIO. Suporte técnico de referência: Guilherme Cimino e Ruan Bauer, Dev Lead. Verificação e auditoria de referência: Natan Correa e Max Iago, QA / Auditoria. Essas referências seguem a RACI e precisam ser confirmadas no handover. Procedimentos e níveis de serviço propostos em [sustentacao.md](sustentacao.md).

## Aceite

Product Owner: Isabella Jacques.

Decisão: **pendente de preenchimento pela PO**.

Data do aceite: ____________________.

Ressalvas e condições: ____________________.

Registro de aprovação pela própria PO, em commit, ata ou comentário rastreável: ____________________.

Em 5 de novembro de 2026, o grupo confirmou que o aceite ainda não foi registrado e o link ainda não foi enviado ao professor. Nenhuma assinatura ou aprovação é presumida pela preparação deste documento.

## Congelamento para apresentação

A versão a demonstrar deve ser o último commit publicado e identificado pelo grupo no início da apresentação. Após a publicação final, manter código e documentos congelados até o término da apresentação. Falhas encontradas durante esse período devem ser anotadas no backlog, sem alterar a versão demonstrada. O grupo comunica o identificador desse commit ao professor juntamente com o link do repositório.
