# Operação e sustentação do GovDesk

## Iniciar e verificar

Instalar Python 3.10 ou superior, executar `python -m pip install -r requirements.txt` e iniciar com `python app.py`. O botão Run de um projeto Python no Replit utiliza `.replit`. Conferir a lista, cadastrar um produto fictício, abrir uma reposição, iniciar atendimento e confirmar recebimento. O saldo só aumenta na conclusão da reposição.

O banco padrão fica em `instance/govdesk.sqlite3`. `GOVDESK_DATABASE` permite outro arquivo persistente, com diretório gravável pelo processo. Não armazenar o banco em diretório temporário quando for necessário manter dados. No serviço de hospedagem, confirmar a existência de volume persistente. Não versionar o banco ou credenciais.

## Responsabilidades de referência

| Atividade | Responsável final | Execução e apoio |
| --- | --- | --- |
| Priorizar mudança e aceitar entrega | Isabella Jacques | Consulta a Dev e QA |
| Diagnosticar inicialização, banco e restauração | Guilherme Cimino | Ruan Bauer |
| Manter fluxo de solicitação e recebimento | Ruan Bauer | Guilherme Cimino |
| Validar saldos, status e regressões | Natan Correa | Max Iago |
| Conferir documentos e evidências de encerramento | Max Iago | Natan Correa |

Essas referências seguem [raci.md](raci.md). Contatos e disponibilidade devem ser acordados pelo grupo no aceite, sem presumir compromisso de suporte já assumido.

## Backup e recuperação

1. Parar a aplicação para evitar escrita durante a cópia.
2. Copiar o arquivo do banco para uma pasta de backup protegida, identificando data e versão do código. Cópias com dados pessoais exigem os mesmos controles de acesso do original.
3. Para conferir a recuperação, copiar o backup para um novo arquivo de teste, configurar `GOVDESK_DATABASE` para esse arquivo e iniciar a mesma versão do código.
4. Conferir produtos, saldos, solicitações e históricos antes de substituir qualquer arquivo operacional. Preservar uma cópia do original.
5. Executar os testes com bancos temporários. Nunca apagar o banco ativo como solução de uma falha de inicialização.

## Tratamento de incidentes

Registrar versão, horário UTC, rota, mensagem de erro e cenário com dados fictícios. Evitar copiar descrições, nomes, credenciais ou o banco em comentários públicos. Dev investiga, QA reproduz e testa a correção e a PO aprova mudança de escopo. Em caso de conflito 409 no avanço de status, recarregar a solicitação e conferir o histórico antes de repetir.

## Níveis de serviço propostos

Para um futuro piloto, propor triagem em até um dia útil e plano de resposta em até dois dias úteis para falhas que bloqueiem o fluxo. São propostas para negociação com a PO, não SLA contratado. Não há disponibilidade 24 horas nem canal institucional de suporte configurado nesta entrega.
