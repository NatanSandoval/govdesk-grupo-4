# PETI — Plano Estratégico de TI do Projeto

**Sistema de Gerenciamento de Estoques**

| Campo | Descrição |
| :--- | :--- |
| **Objetivo de Negócio** | Garantir a visibilidade e o controle em tempo real dos itens armazenados, eliminando a perda de produtos por extravio ou validade e reduzindo falhas de suprimento que impactam o atendimento e as operações da organização. |
| **Objetivo de TI** | Disponibilizar uma aplicação web centralizada e responsiva que permita o cadastro estruturado de produtos, controle automatizado de entradas e saídas, consulta dinâmica de saldos e emissão de alertas automáticos para itens com estoque abaixo do limite mínimo. |
| **Indicador de Sucesso** | Reduzir em 100% as divergências manuais de contagem de inventário e garantir que 100% dos itens críticos tenham seus níveis de saldo atualizados e visíveis para a equipe até o fim do ciclo de implementação. |
| **Prioridade da Semana** | Modelar o banco de dados SQL (tabelas de `produtos` e `movimentacoes`), integrar a conexão com o Flask e criar a interface visual com formulários para cadastro e listagem em tempo real. |

## Consolidação da Semana 10

O objetivo estratégico permanece o gerenciamento de estoques. O protótipo entrega cadastro, movimentações, saldos, alertas e solicitações de reposição com atendimento e recebimento integral. O painel mostra contagens e percentual de reposições concluídas no banco local. O indicador de sucesso acima é uma meta original: não há inventário físico ou medição operacional para afirmar que as divergências foram eliminadas.

A prioridade da entrega final é demonstrar o fluxo e consolidar governança, lições e sustentação. Antes de uso com dados reais, implementar controles de acesso, proteção dos formulários e política de privacidade validada. O BSC e as medições propostas estão em [melhoria-continua.md](melhoria-continua.md).
