---
tags: [rust, cargo]
aliases: ["semver", "Cargo.lock", "caret requirements"]
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Cargo.toml e dependências]]", "[[Comandos úteis do Cargo]]", "[[Publicar no crates.io]]"]
---

# Versionamento semântico

O ecossistema segue **SemVer**: `MAJOR.MINOR.PATCH`.

| Mudança | Quando |
|---|---|
| `PATCH` | correção de bug compatível |
| `MINOR` | funcionalidade nova compatível |
| `MAJOR` | quebra de compatibilidade |

Em versões `0.x`, a regra desloca: o `MINOR` funciona como "major" (`0.3 → 0.4` pode quebrar).

## Como o Cargo interpreta requisitos

| Escrito | Significa | Aceita |
|---|---|---|
| `"1.2.3"` ou `"^1.2.3"` | compatível com 1.2.3 | `>=1.2.3, <2.0.0` |
| `"0.3.5"` | | `>=0.3.5, <0.4.0` |
| `"~1.2.3"` | só patches | `>=1.2.3, <1.3.0` |
| `"1.*"` | qualquer 1.x | `>=1.0.0, <2.0.0` |
| `"=1.2.3"` | exatamente | só 1.2.3 |
| `">=1.2, <1.5"` | intervalo | |

## Cargo.lock

- Registra as **versões exatas** resolvidas, garantindo builds reproduzíveis.
- **Binários/aplicações:** versione o `Cargo.lock` no Git.
- **Bibliotecas:** historicamente não se versionava, mas hoje a recomendação oficial é versionar também (a decisão é do projeto).

```bash
cargo update                  # atualiza para as versões mais novas permitidas
cargo update -p serde         # só um crate
cargo update -p serde --precise 1.0.200   # fixa uma versão específica
```

> [!question] Verificar na documentação oficial
> Confirme a recomendação atual do Cargo Book sobre versionar o `Cargo.lock` em bibliotecas.

> [!tip] MSRV
> Defina `rust-version` no `Cargo.toml` e teste essa versão mínima na CI.

## Veja também

- [[Cargo.toml e dependências]]
- [[Comandos úteis do Cargo]]
- [[Publicar no crates.io]]
