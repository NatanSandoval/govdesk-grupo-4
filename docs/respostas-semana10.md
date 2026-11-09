# Respostas da Semana 10 do ProntoEstoque

Conferência do PDF Semana10_Detalhamento_Exercicios em 5 de novembro de 2026. O ProntoEstoque é o nome atual do projeto iniciado como GovDesk. Os requisitos do PDF coincidem com os do documento Word usado na implementação. O domínio foi adaptado para gestão de estoques e solicitações de reposição, conforme a decisão do grupo.

O grupo confirmou nesta revisão que o aceite da PO ainda não foi registrado e que o link ainda não foi enviado ao professor.

## Resumo da entrega para o professor

O ProntoEstoque é uma aplicação Flask para gestão de estoques com persistência SQLite. Permite cadastrar produtos, validar campos e quantidades, registrar entradas e saídas, consultar saldos e identificar itens abaixo do mínimo. As solicitações de reposição passam pelos estados Aberta, Em andamento e Concluída. A conclusão confirma o recebimento integral e registra uma entrada única no estoque, junto com o histórico da atualização. O sistema também oferece indicadores, busca e filtros, além de interface responsiva e avisos de privacidade.

A governança está documentada em PETI, LGPD, RACI, backlog, WBS, BPMN TO-BE e plano de melhoria contínua. Foram preparados o termo de encerramento, seis lições aprendidas, procedimentos de sustentação, apresentação com fala para os cinco integrantes e formulários de autoavaliação. A versão atual possui 25 testes automatizados aprovados. O aceite formal, as validações individuais, o ensaio e o envio ao professor dependem do grupo.

## Checklist go no go respondido

Marcar um item significa que há evidência para o cenário descrito. Campos pendentes não devem ser marcados apenas porque o material foi preparado.

- [x] **O app inicia pelo botão Run sem erro.** O comando `python app.py` foi executado com sucesso localmente e `.replit` configura esse comando no botão Run. A execução do botão na plataforma escolhida ainda precisa ser conferida pelo grupo. Situação parcial.
- [x] **Fluxo completo de abertura, validação e avanço de status.** No domínio do projeto, o chamado é a solicitação de reposição. Cadastro, validação, Aberta, Em andamento, Concluída e entrada de recebimento foram testados.
- [x] **Aviso LGPD visível e nenhum dado pessoal real nos exemplos de demonstração verificados.** Os avisos foram vistos no navegador e os testes usaram identificações fictícias. Antes da apresentação, usar o banco de demonstração e revisar os registros que serão exibidos; a verificação não é uma certificação sobre todo dado inserido manualmente depois.
- [x] **RACI com um único A por atividade.** O verificador confere 14 atividades, cada uma com uma responsabilidade final.
- [x] **Backlog, WBS e Kanban coerentes.** Histórias técnicas entregues e tarefas de aceite, apresentação e envio têm estados separados. Os IDs do quadro constam em `kanban.md`.
- [x] **BPMN TO-BE com raias iguais aos papéis da RACI.** Product Owner / CIO, Dev Lead e QA / Auditoria. Arquivos editável e visual em `processo-estoque.bpmn` e `processo-estoque.svg`.
- [x] **Melhoria contínua atualizada após o período da Semana 9.** O documento consolida BSC, não conformidades, maturidade descritiva e roadmap. A atualização não presume uma avaliação histórica da Semana 9 que não estava registrada no repositório.
- [x] **Encerramento e lições aprendidas concluídos.** Os documentos estão redigidos, com seis lições e referência aos cinco integrantes. Faltam a validação pessoal das lições e o aceite formal da PO. Situação parcial.
- [x] **README explica como rodar e quem faz o quê.** Inclui instalação, execução, integrantes, papéis, documentos, limitações e backlog futuro.
- [x] **Link do repositório enviado.** O grupo confirmou que esse envio ainda não ocorreu. Link a enviar: https://github.com/NatanSandoval/govdesk-grupo-4.

As ações restantes foram abertas no Trello como S10-01 a S10-07, todas em A fazer. Os links, responsáveis de referência e correspondência com a WBS estão em [kanban.md](kanban.md). H7 coordena o encerramento e H11 registra os materiais preparados.

## Correspondência dos oito entregáveis

| Entregável do PDF | Resposta e evidência | O que falta |
| --- | --- | --- |
| 1 Sistema funcionando | Aplicação de estoque e reposições com validação, aviso, status e indicadores; 25 testes e conferência no navegador | Conferir Run na plataforma de apresentação |
| 2 docs completo e coerente | PETI.md, lgpd.md, raci.md, template-mudanca.md, backlog.md, wbs.md, processo-chamados.md e melhoria-continua.md | Revisão final do grupo após esta publicação |
| 3 Encerramento | encerramento.md com escopo, resultados, pendências, riscos e sustentação | Decisão, data e registro do aceite pela PO |
| 4 Lições aprendidas | licoes-aprendidas.md com seis situações, causas, ações e responsáveis de referência | Cada integrante valida sua lição e experiência |
| 5 README final | Marca ProntoEstoque, execução, papéis, documentos e continuidade | Nenhuma lacuna técnica identificada nesta conferência |
| 6 Apresentação | PowerPoint editável e roteiro 8 minutos mais 2 de perguntas, com fala para todos | Ensaio e apresentação pelo grupo |
| 7 Commits e link | Histórico real do Git e repositório publicado | Conferir contribuição dos cinco integrantes e enviar link ao professor |

## Respostas para o termo de encerramento

**Escopo planejado:** desenvolver uma aplicação de gestão de estoques com cadastro de produtos, entradas e saídas, consulta de saldos, alertas de mínimo e governança documentada.

**Escopo entregue:** cadastro com validação e aviso de privacidade, movimentações persistidas em SQLite, alertas de mínimo, solicitações de reposição com avanço de status e histórico, recebimento integral com proteção contra duplicação, painel de indicadores, busca e filtros. A interface usa a identidade ProntoEstoque e se adapta ao celular.

**Resultados e indicadores:** 25 testes automatizados aprovados; persistência e migração de dados verificadas; transação atômica entre status, histórico e recebimento; contagens de produtos, alertas e solicitações por status. O percentual de conclusão é concluídas dividido pelo total, multiplicado por 100. Não houve medição operacional de redução de perdas ou divergências físicas.

**Pendências e riscos:** autenticação, autorização e CSRF; rotina automática de backup e restauração ensaiada; recebimento parcial e cancelamento; linha de base de indicadores operacionais; aceite formal e ações individuais. Até implementar os controles necessários, usar dados fictícios no ambiente acadêmico.

**Sustentação:** Isabella Jacques é a referência para propriedade do sistema e aprovação de mudanças; Guilherme Cimino e Ruan Bauer para suporte técnico; Natan Correa e Max Iago para verificação e auditoria. As referências seguem a RACI e precisam ser confirmadas pelo grupo no handover.

**Aceite:** Product Owner Isabella Jacques. Decisão e data pendentes de registro pela própria PO. Preparar o termo não equivale a aprová-lo.

## Respostas sobre as lições aprendidas

**O que funcionou:** usar critérios de aceite e testes reproduzíveis, persistir os dados em SQLite e separar a situação de estoque do status de atendimento da reposição.

**O que não funcionou:** aplicar literalmente o exemplo de chamados a um projeto de estoque; manter equipe e papéis divergentes entre código e documentos; conferir o aviso de privacidade apenas no HTML; deixar a consolidação da governança para o fim.

**O que mudaríamos:** revisar domínio e critérios antes de cada sprint; verificar formulários no navegador; conferir RACI, BPMN e backlog em conjunto; testar migração, repetição de operações e restauração; coletar indicadores reais durante um piloto.

**Uma lição de referência por integrante:** Isabella, alinhar escopo e PETI; Guilherme, revisar papéis em código e documentação; Ruan, testar persistência e repetição de operações; Natan, conferir a visibilidade dos avisos na tela; Max, consolidar evidências de entrega. Cada pessoa deve validar essa referência antes de apresentá-la como experiência própria.
