---
tags:
  - devops
  - dev
aliases:
  - "Feature toggles"
tipo: devops
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Ambientes de Staging e Promoção]]"
  - "[[Caso - CI e CD]]"
---
# Feature Flags

*Feature flags* ativam/desativam funcionalidades sem novo *deploy*, permitindo lançamento gradual e **desligamento de emergência** (*kill switch*).

```python
import os

def flag(nome: str, padrao: bool = False) -> bool:
    return os.getenv(f"FLAG_{nome.upper()}", str(padrao)).lower() in {"1", "true", "on"}

if flag("novo_checkout"):
    ...
```

| Cuidado | Motivo |
|---|---|
| Padrão **desligado** | Falha segura |
| Remover flags antigas | Dívida técnica |
| Testar combinações críticas | Comportamentos inesperados |
| Controle de acesso à ferramenta de flags | Alterar flag = alterar produção |

## Exercício

Liste as flags do seu projeto e marque as que já podem ser removidas.

## Veja também

- [[Ambientes de Staging e Promoção]]
- [[Runners Efêmeros e Pipelines Seguros]]
- [[MOC - Dev e DevOps]]
