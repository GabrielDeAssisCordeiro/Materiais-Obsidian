---
tags:
  - tipos
aliases:
  - "Dados sintéticos"
  - "Anonimização"
  - "Mascaramento"
tipo: tipo-de-sandbox
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Caso - Homologação e Staging]]"
  - "[[Caso - Testes de Software e QA]]"
---
# Sandbox de Dados

Isola **informação**, não código: ambientes de teste usam dados que não expõem pessoas reais.

| Técnica | Descrição | Risco residual |
|---|---|---|
| Dados sintéticos | Gerados artificialmente | Podem não refletir casos reais |
| Mascaramento | Substitui campos sensíveis | Reidentificação por combinação de campos |
| Pseudonimização | Troca identificadores por pseudônimos reversíveis | Continua sendo dado pessoal (LGPD) |
| Anonimização | Remove a possibilidade de identificação | Difícil de garantir |
| Subconjunto (*subsetting*) | Amostra reduzida | Herdar sensibilidade |

> [!warning] LGPD
> Dados pseudonimizados continuam sujeitos à LGPD. Prefira dados sintéticos em ambientes não produtivos.

```python
# Exemplo: gerar dados falsos com a biblioteca Faker
from faker import Faker
f = Faker("pt_BR")
print({"nome": f.name(), "email": f.email(), "cpf": f.cpf()})
```

## Exercício

Gere 10 clientes fictícios com Faker e carregue em um banco de teste.

## Veja também

- [[Caso - Homologação e Staging]]
- [[Caso - Testes de Software e QA]]
- [[Caso - Sandbox de APIs e Pagamentos]]
- [[MOC - Tipos de Sandbox]]
