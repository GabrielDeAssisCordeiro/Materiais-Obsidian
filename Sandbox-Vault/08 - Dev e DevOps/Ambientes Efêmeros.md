---
tags:
  - devops
  - dev
aliases:
  - "Ephemeral environments"
tipo: devops
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Caso - CI e CD]]"
  - "[[Descarte Seguro]]"
  - "[[Preview Environments]]"
---
# Ambientes Efêmeros

Ambientes **criados sob demanda e destruídos automaticamente** após o uso (por job, por PR, por teste).

**Benefícios:** sem "deriva" de configuração, custo menor, menor janela de ataque, estado conhecido.

```mermaid
flowchart LR
    E[Evento: PR/teste] --> C[Cria ambiente via IaC]
    C --> U[Uso]
    U --> D[Destrói automaticamente]
```

Pilares: **infraestrutura como código**, **dados sintéticos**, **TTL** (tempo de vida máximo) e **limpeza automática**.

> [!warning] Ambientes esquecidos custam dinheiro e criam risco
> Defina TTL e alarme de ambientes órfãos.

## Exercício

Defina o TTL e o procedimento de limpeza para ambientes de PR em um projeto seu.

## Veja também

- [[Preview Environments]]
- [[Infraestrutura como Código]]
- [[Descarte Seguro]]
- [[MOC - Dev e DevOps]]
