# Checklist LGPD do Projeto 

## Protótipo da Semana 6

O protótipo acadêmico coleta nome e descrição do produto, identificação do responsável, prioridade de reposição, mínimo, tipo e quantidade de movimentação e data e hora UTC. A identificação do responsável aparece na lista de produtos e no histórico. Use apenas identificações fictícias; os formulários orientam a não informar CPF nem dados pessoais sensíveis.

Os registros permanecem no arquivo SQLite local `instance/govdesk.sqlite3` após reiniciar. O arquivo não é versionado no Git. O protótipo ainda não tem autenticação, restrição por perfil nem rotina de retenção e exclusão; esses controles devem ser definidos antes de uso com dados reais. Não há coleta de CPF ou e-mail pelo formulário atual, nem tabela de logs de acesso. Os dados e prazos da seção seguinte representam o planejamento original do sistema e precisam de validação pela organização antes de sua implantação.

## Dados Coletados 
| Dado | Finalidade | Base Legal | Quem Acessa | Retenção |
|------|-----------|------------|-------------|----------|
| Nome completo do operador | Identificar o usuário responsável pelas movimentações de produtos e contagens de estoque | Execução de contrato | Equipe de TI, Gerência de Estoque e RH | Durante o vínculo empregatício + 5 anos |
| CPF / Matrícula | Autenticação no sistema e controle de acessos por perfil | Execução de contrato | Equipe de TI e Administradores do Sistema | Durante o vínculo empregatício + 5 anos |
| E-mail corporativo | Envio de alertas de estoque crítico, relatórios e recuperação de senha | Legítimo interesse | Equipe de TI e o próprio usuário | Enquanto o cadastro estiver ativo |
| Nome e e-mail do representante do fornecedor | Comunicação para pedidos de compra e reposição de produtos | Execução de contrato | Setor de Compras e Almoxarifado | Durante a relação comercial + 5 anos |
| Log de acesso (IP e Horário) | Rastreabilidade de ações e segurança do sistema | Cumprimento de obrigação legal | Equipe de TI e Segurança da Informação | 6 meses |

## Dados Sensíveis Identificados 
No módulo de registro de ocorrências de avaria ou divergência de estoque, existe um campo de texto livre em "Observações do Item". Existe o risco de o operador digitar justificativas contendo dados de saúde (ex.: "caixa caiu porque fulano passou mal") ou opiniões pessoais. 
* *Risco:* Inserção não intencional de dados de saúde ou comentários inadequados sobre funcionários.
* *Como reduzir:* Treinamento com os operadores para não inserir dados pessoais em campos do sistema e substituição da caixa de texto livre por seleções pré-definidas (ex.: "Avaria por transporte", "Item quebrado", "Divergência de contagem").

## Direitos do Titular 
O titular (operador ou representante de fornecedor) poderá exercer seus direitos enviando um e-mail para o Encarregado de Dados (DPO) da empresa. 
* *Acesso e Correção:* O usuário solicita a visualização ou correção dos seus dados ao DPO, que repassa a demanda para a equipe de TI atualizar o cadastro no módulo de usuários em até 5 dias úteis.
* *Exclusão/Anonimização:* Em caso de desligamento ou término de contrato, os logs de movimentação de estoque são mantidos por obrigações legais, mas o cadastro do titular é inativado e seus dados de contato direto são removidos após o prazo legal de retenção.
