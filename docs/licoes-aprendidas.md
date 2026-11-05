# Lições aprendidas do GovDesk

As situações abaixo derivam da evolução técnica e dos registros disponíveis do repositório. Cada integrante tem uma lição de referência para discutir e validar. A indicação de nome não constitui depoimento pessoal nem comprovação de autoria individual.

| Número | Situação | Causa ou fator identificado | Ação recomendada | Responsável de referência |
| --- | --- | --- | --- | --- |
| 1 | O enunciado trabalhava chamados e o PETI definia estoque | Exemplos da disciplina e domínio escolhido eram diferentes | Registrar a correspondência de campos e validar a adaptação antes de implementar cada entrega | Isabella Jacques |
| 2 | A página da equipe tinha três nomes e papéis diferentes da documentação com cinco integrantes | Código e documentação mantinham cadastros separados | Conferir equipe e papéis em README, aplicação e RACI na revisão final | Guilherme Cimino |
| 3 | O protótipo inicial mantinha registros em memória | A primeira versão simplificava a persistência para ensino | Persistir em SQLite e executar teste de reinício e atualização de banco | Ruan Bauer |
| 4 | O aviso de privacidade estava no HTML e ficou oculto no navegador usado na Semana 6 | A presença no código não garantia a apresentação visual | Validar avisos na tela e sua associação acessível ao campo, além do teste de conteúdo | Natan Correa |
| 5 | O encerramento exige evidências de planejamento, processo e melhorias que ainda não estavam consolidadas | As entregas técnicas e a documentação eram verificadas separadamente | Usar uma matriz de go/no-go com links e registrar pendências sem declarar aprovações inexistentes | Max Iago |
| 6 | Um recebimento poderia ser duplicado por reenvio de uma página antiga | Requisições HTTP podem ser repetidas independentemente do clique original | Comparar o status esperado, usar transação e testar repetição e reversão de falha | Ruan Bauer |

## O que funcionou

Os critérios de aceite orientaram testes reproduzíveis. Bancos temporários permitiram verificar entradas, saídas, validações e persistência sem modificar os dados do protótipo local. Separar o estado de estoque do estado da solicitação evitou transformar um alerta de mínimo em um status manual incoerente.

## O que não funcionou

Os exemplos de chamados não podiam ser aplicados literalmente ao domínio de estoque. Verificar apenas o HTML não comprovou a visibilidade do aviso no navegador. O repositório disponível também não demonstrava uma revisão contínua de BPMN, melhoria e encerramento entre as semanas.

## O que mudaríamos

Incluir uma revisão conjunta do domínio, critérios e documentação no começo de cada sprint. Conferir migração e repetição de operações antes de ampliar o fluxo. Coletar métricas operacionais em um piloto, em vez de apresentar metas do PETI como resultados atingidos.

## Validação individual

Cada integrante deve confirmar ou corrigir a lição de referência e acrescentar sua experiência real, com evidência de contribuição. A autoavaliação individual continua em [autoavaliacao.md](autoavaliacao.md).
