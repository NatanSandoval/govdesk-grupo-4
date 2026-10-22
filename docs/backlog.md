# Backlog do GovDesk

A Sprint 1 adapta o exercício da Semana 6 ao gerenciamento de estoques definido no [PETI](PETI.md), conforme orientação do grupo nesta entrega. O cadastro de chamado foi convertido em cadastro de produto: título corresponde a nome do produto, solicitante a responsável e prioridade a prioridade de reposição. A descrição mantém o aviso de privacidade. Entradas e saídas, saldos e alertas completam o fluxo de estoque. Os dados ficam em SQLite, em vez da lista em memória do gabarito.

Os responsáveis abaixo são referências para revisão e continuidade, conforme os papéis da [RACI](raci.md). A implementação assistida não comprova trabalho ou aprovação individual desses integrantes. A PO responde pela aprovação final da priorização e do escopo.

| ID | Épico | História | Critério de aceite | Prioridade | Responsável | Sprint |
| --- | --- | --- | --- | --- | --- | --- |
| H1 | Cadastro de produtos | Como operador, quero cadastrar produtos, para organizar os itens armazenados. | GET /novo retorna 200; POST válido grava nome, descrição, responsável, prioridade e mínimo, registra entrada inicial se positiva e redireciona para a lista. | alta | Guilherme Cimino | 1 |
| H2 | Cadastro de produtos | Como operador, quero corrigir campos inválidos, para cadastrar produtos sem perder o que digitei. | Nome e responsável ausentes, vazios ou só com espaços são rejeitados; prioridades adulteradas e quantidades negativas, fracionárias ou acima de 1 bilhão são rejeitadas sem gravação parcial; campos válidos são preservados. | alta | Ruan Bauer | 1 |
| H3 | Privacidade e rastreabilidade | Como operador, quero ver avisos de privacidade, para evitar dados sensíveis nos registros. | Descrição tem aviso associado ao campo; formulário de movimentação orienta identificação fictícia; valores HTML são escapados na exibição. | alta | Natan Correa | 1 |
| H4 | Movimentações de estoque | Como operador, quero registrar entradas e saídas, para manter o saldo atualizado. | Entrada soma e saída subtrai quantidade inteira positiva; saída maior que o saldo e tipo inválido são rejeitados; histórico registra responsável e data UTC; dados permanecem após reiniciar. | alta | Ruan Bauer | 1 |
| H5 | Consulta e reposição | Como gestor, quero consultar saldos e alertas de mínimo, para planejar a reposição. | Página inicial lista produto, responsável, prioridade, saldo e mínimo; destaca Abaixo do mínimo apenas quando saldo é menor que o mínimo; apresenta estado vazio e acesso à movimentação. | alta | Guilherme Cimino | 1 |
| H6 | Gestão e qualidade | Como auditor, quero planejamento e testes versionados e Kanban atualizado, para rastrear a entrega. | Backlog com ao menos seis histórias e dois épicos; WBS com até três níveis e tarefas de até uma hora; testes reproduzíveis e roteiro manual; cards H1 a H6 nas colunas A fazer, Fazendo e Pronto conforme evidências. | alta | Max Iago | 1 |
| H7 | Governança do projeto | Como PO, quero avaliar a adaptação e as prioridades, para alinhar a entrega ao PETI. | Revisar docs/semana6.md, backlog e WBS; registrar a decisão da PO, inclusive histórias adiadas, sem presumir aprovação em nome dela. | média | Isabella Jacques | 2 |
| H8 | Controle de acesso | Como gestor, quero limitar alterações a operadores autorizados, para proteger os registros de estoque. | Autenticação, autorização de escrita, proteção CSRF e testes de acesso implementados antes de uso com dados reais. | alta | Guilherme Cimino | 2 |

## Priorização

H1 a H6 formam a entrega técnica da Semana 6. H7 e H8 ficam para a Sprint 2: a revisão da PO depende de manifestação dela, e o controle de acesso será uma evolução antes de uso operacional. Essa sequência é uma proposta para revisão da PO, não um registro de decisão pessoal já tomada por ela. Mudanças seguem o [template de solicitação](template-mudanca.md).

Conclusão técnica exige critério de aceite verificado e evidência no repositório. Commits e revisões de cada integrante são contribuições pessoais e não devem ser simulados.
