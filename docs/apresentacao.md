# Apresentação final do GovDesk

Oito minutos de apresentação e dois de perguntas. Todos os cinco integrantes têm participação prevista. O enunciado traz uma tabela acumulada até dez minutos e também pede oito mais dois; este roteiro reserva explicitamente os dois minutos finais às perguntas.

[PowerPoint editável com notas dos apresentadores](apresentacao/govdesk-semana10.pptx). O slide de lições contém referências para ensaio; cada pessoa valida sua experiência antes de apresentar.

| Intervalo | Quem | Conteúdo e evidência |
| --- | --- | --- |
| 0:00 a 1:00 | Isabella | Problema de estoque, usuários, objetivo do PETI e adaptação de chamados para reposições |
| 1:00 a 2:30 | Guilherme | Demonstrar cadastro, erro com campo em branco e alerta de mínimo |
| 2:30 a 4:00 | Ruan | Abrir reposição, iniciar atendimento, confirmar recebimento e mostrar histórico e indicador |
| 4:00 a 5:15 | Natan | Conectar LGPD, RACI e BPMN TO-BE, ressaltando uso de dados fictícios e ausência de login |
| 5:15 a 6:15 | Max | Mostrar evidência dos 23 testes, checklist go/no-go e plano BSC, distinguindo metas de resultados |
| 6:15 a 7:30 | Todos, 15 segundos cada | Cada integrante comenta uma lição que validou pessoalmente |
| 7:30 a 8:00 | Isabella | Roadmap, riscos residuais e estado real do aceite |
| 8:00 a 10:00 | Todos | Perguntas do professor |

## Preparação e demonstração

Executar em um banco separado, com `GOVDESK_DATABASE` apontando para um arquivo de demonstração. Não apagar nem substituir o banco existente. Instalar dependências e abrir o app antes da apresentação. Registrar o hash do último commit demonstrado e manter a versão congelada.

1. Cadastrar Papel A4 demo, responsável Operador fictício, inicial 2, mínimo 5 e prioridade alta. Mostrar o aviso junto à descrição. O produto fica Abaixo do mínimo.
2. Na página de novo produto, tentar enviar nome composto só de espaços e responsável fictício. Mostrar a rejeição no servidor e os campos preservados. Não criar outro produto.
3. Abrir Solicitações de reposição, solicitar 8 unidades do produto e informar Solicitante fictício. Mostrar status Aberta e histórico.
4. Informar Técnico fictício e iniciar atendimento. O saldo ainda é 2.
5. Confirmar recebimento integral. Mostrar status Concluída, saldo 10 e uma entrada de 8 no histórico.
6. Abrir Indicadores. Com uma única solicitação concluída nesse banco, o percentual será 100%. Esclarecer que são dados de demonstração, não uma taxa de sucesso operacional.
7. Abrir RACI, BPMN e melhoria contínua. Mostrar backlog futuro e pendências de aceite e autoavaliação.

## Perguntas para ensaio

- Por que SQLite? Persistência simples para o protótipo, com transação para preservar status e estoque juntos.
- O que impede entrada duplicada? O status esperado é comparado ao atual dentro de uma transação e a solicitação concluída não pode avançar novamente.
- O que significa Concluída? Recebimento integral confirmado, com entrada efetiva no estoque.
- O sistema já pode usar dados reais? Ainda depende de autenticação, autorização, CSRF e definição dos controles de privacidade e operação.
- Quem decidiu adiar melhorias? A proposta está no backlog e precisa de decisão registrada pela PO, sem presumir uma aprovação já dada.
- A meta do PETI foi alcançada? O protótipo demonstra controle lógico de estoque. Não há dados de inventário físico que comprovem eliminação de divergências.
