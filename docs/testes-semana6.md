# Verificação da Semana 6

## Resultado automatizado

Em 22 de outubro de 2026, os 12 testes de `tests/test_app.py` passaram com Flask 3.0.3 e Python 3.12. Cada teste usa seu próprio banco SQLite temporário. Execução:

```bash
python -m unittest discover -s tests -v
```

| Verificação | Resultado |
| --- | --- |
| GET /novo, campos, aviso associado e prioridade média padrão | passou |
| Cadastro com baixa, média e alta, remoção de espaços, IDs e entrada inicial | passou |
| Nome e responsável ausentes, vazios e só com espaços; preservação de valores | passou |
| Prioridade adulterada, vazia e em caixa inesperada | passou |
| Quantidades negativas, fracionárias, vazias, não numéricas e acima do limite | passou |
| Cadastro sem descrição, prioridade e quantidades; saldo inicial zero | passou |
| Entrada, saída, histórico, alerta abaixo do mínimo e igualdade ao mínimo | passou |
| Saída acima do saldo e preservação dos campos; consumo até zero | passou |
| Movimentações inválidas e produto inexistente com resposta 404 | passou |
| Persistência do produto e saldo ao recriar a aplicação | passou |
| Escape HTML e entradas SQL tratadas como dados | passou |
| Lista vazia e página com os cinco integrantes | passou |

## Roteiro manual

Conferência pelo navegador realizada em 22 de outubro de 2026: produto demonstrativo com saldo inicial 10 e mínimo 5; saída 7 resultou em saldo 3 e alerta; saída 4 foi rejeitada, mantendo saldo e campos; entrada 2 resultou em saldo 5 e situação Regular. Avisos de privacidade foram conferidos visíveis nos dois formulários. Persistência após recriar a aplicação e demais entradas inválidas também foram verificadas pelos testes automatizados. A aprovação pessoal de QA e a revisão em tela estreita continuam sendo ações do grupo.

Reproduzir com o servidor local e dados fictícios. A aprovação pessoal de QA deve ser registrada pelo integrante que realizar sua revisão.

1. Abrir `/novo`; conferir nomes dos campos, leitura do aviso junto à descrição e navegação pelo teclado.
2. Cadastrar Papel A4, descrição Pacote fictício, responsável Operador fictício, prioridade alta, estoque inicial 10 e mínimo 5. Esperado: redirecionamento para `/`, produto com saldo 10 e situação Regular.
3. Tentar cadastrar sem nome ou responsável. Esperado: bloqueio do navegador. Enviar somente espaços para verificar também a validação no servidor: erro visível, dados preservados e nenhum novo produto.
4. Abrir Movimentar Papel A4 e registrar saída 7 com responsável fictício. Esperado: saldo 3, aviso Abaixo do mínimo e histórico com a saída e a entrada inicial.
5. Tentar saída 4. Esperado: Saldo insuficiente, valores preservados, saldo ainda 3 e nenhuma movimentação adicional.
6. Registrar entrada 2. Esperado: saldo 5, situação Regular e histórico atualizado.
7. Reiniciar a aplicação usando o mesmo banco. Esperado: produto e saldo 5 permanecem.
8. Em janela estreita, conferir formulário legível e rolagem horizontal da tabela.
