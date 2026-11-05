# Verificação final da Semana 10

## Testes automatizados

Em 5 de novembro de 2026, `python -m unittest discover -s tests -v` executou **23 testes aprovados**: 12 em `test_app.py` e 11 em `test_encerramento.py`. A execução usa bancos SQLite temporários, independentes do banco existente. Flask 3.0.3 e Python 3.12 no ambiente verificado.

| Área | Casos verificados | Resultado |
| --- | --- | --- |
| Estoque anterior | Cadastro, prioridades, obrigatórios, espaços, quantidades inválidas, entrada, saída, saldo insuficiente, mínimo, persistência e escape HTML | 12 testes aprovados |
| Solicitações | Páginas vazias, formulário com aviso, criação, padrões e valores inválidos, preservação dos campos | aprovado |
| Avanço de status | Aberta, Em andamento, Concluída, responsável obrigatório, estado antigo, GET sem alteração e ID inexistente | aprovado |
| Recebimento | Uma entrada na conclusão, nenhuma entrada no início, bloqueio de reenvio concluído | aprovado |
| Atomicidade | Falha simulada no histórico reverte entrada e status da mesma transação | aprovado |
| Continuidade | Persistência de status e migração aditiva preservam estoque | aprovado |
| Indicadores | Contagens com dados, 33,3% com uma de três concluídas, ausência de divisão por zero e alerta eliminado após reposição | aprovado |

O verificador `python scripts/verificar_entrega.py` confere links locais dos documentos, presença dos entregáveis, um A por linha da RACI, três raias BPMN coerentes, referências do diagrama e lições para os cinco integrantes.

## Verificação pelo navegador

Conferido em banco de demonstração separado em 5 de novembro de 2026: cadastro com saldo 2 e mínimo 5; aviso de privacidade visível; criação de reposição de 8; avanço para Em andamento sem recebimento; confirmação para Concluída com histórico dos três estados; painel com uma concluída, nenhum produto abaixo do mínimo e percentual de 100% nesse cenário fictício. O cenário não representa melhoria operacional medida.

## Go no go do enunciado

| Critério | Evidência | Estado |
| --- | --- | --- |
| App inicia sem erro | `python app.py` e servidor local conferidos; `.replit` define Run | local aprovado; botão real no Replit a conferir pelo grupo |
| Fluxo completo com validação e status | /novo e /solicitacoes, testes e demonstração local | aprovado tecnicamente |
| Aviso e exemplos sem dados pessoais reais | Avisos visíveis, demonstração com pessoas fictícias | aprovado no cenário verificado |
| RACI com um A | raci.md e verificador | conferência automatizada |
| Backlog, WBS e Kanban | H9, H10 e H11 em Pronto; H7, H8 e H12 a H14 em A fazer, conforme kanban.md | atualizado em 5 de novembro de 2026 |
| BPMN com os papéis da RACI | processo-chamados.md, processo-estoque.bpmn e SVG | elaborado e conferido |
| Melhoria contínua após Semana 9 | BSC, não conformidades, maturidade descritiva e roadmap | consolidado sem presumir avaliação histórica ausente |
| Encerramento e lições | Termo preparado e seis lições com referência aos cinco integrantes | revisão e aceite pessoal pendentes |
| README final | Execução, equipe, documentos, limites e backlog futuro | atualizado |
| Apresentação | PowerPoint e roteiro de oito minutos mais dois de perguntas | preparado; ensaio e exposição pelo grupo |
| Autoavaliação individual | Cinco seções em autoavaliacao.md | preenchimento e envio individuais pendentes |
| Commits de todos e link enviado | Histórico real do Git e canal da disciplina | conferir contribuições pessoais e enviar pelo grupo |

**Decisão técnica:** protótipo e materiais preparados para demonstração acadêmica. **Decisão de encerramento formal:** pendente da PO e das ações individuais. **Uso operacional com dados reais:** fora desta versão, depende das melhorias e controles documentados.
