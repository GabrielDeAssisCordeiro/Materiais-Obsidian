---
tags:
  - devops
  - dev
aliases:
  - "Mocks"
  - "Fixtures"
  - "Stubs"
tipo: devops
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Sandbox de Dados]]"
  - "[[Criar Sandbox de Desenvolvimento Web e APIs]]"
---
# Dados de Teste e Mocks

| Técnica | Quando usar |
|---|---|
| Fixtures/factories | Dados determinísticos em testes |
| Faker | Dados fictícios realistas ([[Sandbox de Dados]]) |
| Mocks/stubs em código | Isolar unidades (`unittest.mock`) |
| Servidor de mock (WireMock, Mockoon, Prism a partir de OpenAPI) | Simular APIs externas |
| Contas sandbox de provedores | Testar integrações reais sem efeito real |

```python
from unittest.mock import patch

def test_cobranca_recusada():
    with patch("meuapp.pagamentos.cobrar", return_value={"status": "recusado"}):
        ...
```

> [!tip] Teste caminhos de falha: erro 500, *timeout*, resposta lenta, dados inválidos.

## Exercício

Escreva um teste com mock que simula *timeout* de uma API externa.

## Veja também

- [[Sandbox de Dados]]
- [[Testes de Integração com Containers]]
- [[Criar Sandbox de Desenvolvimento Web e APIs]]
- [[MOC - Dev e DevOps]]
