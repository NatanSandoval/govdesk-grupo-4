# Plano de melhoria contínua do ProntoEstoque

Consolidação em 5 de novembro de 2026, após o período previsto para a Semana 9. O repositório consultado não continha uma avaliação registrada da Semana 9; esta análise usa a versão atual e não atribui avaliações ou resultados retroativos ao grupo.

## BSC e indicadores

| Perspectiva | Objetivo | Indicador e fonte | Meta proposta | Limitação atual |
| --- | --- | --- | --- | --- |
| Financeira | Reduzir perdas e falhas de suprimento | Valor de perdas por mês, a levantar em inventário e compras | Definir após obter linha de base | O protótipo não coleta custos, perdas ou inventário físico |
| Usuários | Dar visibilidade à reposição | Concluídas ÷ total de solicitações × 100 em /indicadores | Validar com PO no piloto | Percentual do banco local, sem prazo de atendimento ou pesquisa de satisfação |
| Processos internos | Identificar necessidade de reposição | Quantidade de produtos com saldo menor que o mínimo em /indicadores | Monitorar diariamente no piloto | Estoque crítico não mede disponibilidade real de fornecedor |
| Processos internos | Preservar consistência | Casos de saldo negativo e recebimento repetido nos testes | Zero ocorrências nos cenários automatizados | Evidência de teste não prova ausência de toda falha operacional |
| Aprendizado | Melhorar revisão e rastreabilidade | Checklist técnico e lições validadas por integrante | Cinco validações individuais antes do aceite | Validação individual pendente |

O painel também exibe total de produtos, total de solicitações e contagem por status. Na ausência de solicitações, 0% é convenção de exibição, não uma taxa observada. O alvo original de eliminar divergências do PETI permanece uma meta e não foi comprovado em operação.

## Não conformidades e tratamento

| ID | Achado | Tratamento | Responsável de referência | Estado |
| --- | --- | --- | --- | --- |
| NC1 | Domínio do exercício difere do PETI | Mapear chamados para reposições e registrar o processo | Isabella | adaptação implementada, revisão da PO pendente |
| NC2 | Faltava avanço de status no sistema de estoque | Criar ciclo Aberta, Em andamento, Concluída e histórico | Ruan | implementado e testado |
| NC3 | Faltava proteção contra recebimento duplicado | Status esperado e transação atômica com teste de reenvio | Ruan | implementado e testado |
| NC4 | Faltavam BPMN e documentos finais | Consolidar processo, encerramento e lições | Max | documentação preparada, validação do grupo pendente |
| NC5 | Ausência de login, perfis e CSRF | Implementar H8 antes de uso com dados reais | Guilherme | backlog futuro |
| NC6 | Sem medição de perdas e satisfação | Definir piloto e linha de base | Isabella | backlog futuro |

## Maturidade

Avaliação descritiva: há processo documentado e verificações automatizadas no protótipo, mas ainda não há processo medido em operação, controle de acesso ou ciclo comprovado de auditorias. Não foi aplicada avaliação formal COBIT ou CMMI e não se atribui certificação nem nota de maturidade.

## Roadmap e ciclo de revisão

| Horizonte relativo ao aceite | Melhoria | Dono de referência | Evidência para encerrar |
| --- | --- | --- | --- |
| Antes de dados reais | H8 autenticação, perfis, CSRF e revisão de privacidade | Guilherme | testes de acesso negado e permitido e validação da PO |
| Primeira semana do piloto | H12 backup e restauração ensaiados | Guilherme | restauração de uma cópia e conferência dos registros |
| Segunda semana do piloto | H13 cancelamento e recebimento parcial | Ruan | critérios aprovados e testes sem duplicação |
| Após um mês de piloto | H14 linha de base de perdas e atendimento | Isabella | indicadores com fonte, período e amostra |

O cronograma é proposto e depende do aceite. A cada revisão, comparar indicadores, abrir não conformidades, priorizar ações, executar testes e registrar a decisão da PO. Atualizar backlog e Kanban usando os mesmos IDs.
