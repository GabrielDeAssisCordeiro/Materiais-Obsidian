---
tags: [rust, cargo, desempenho]
aliases: ["perfil dev", "perfil release"]
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Cargo.toml e dependências]]", "[[Zero-cost abstractions]]", "[[Cargo básico]]"]
---

# Debug vs release

O Cargo compila com **perfis** (*profiles*). Os dois principais:

| | `dev` (`cargo build`) | `release` (`cargo build --release`) |
|---|---|---|
| `opt-level` | 0 (sem otimização) | 3 |
| Tempo de compilação | rápido | lento |
| Execução | lenta | rápida |
| Verificação de overflow | **ligada** (panic) | desligada (dá a volta) |
| `debug-assertions` | ligadas | desligadas |
| Símbolos de depuração | sim | não |
| Saída | `target/debug/` | `target/release/` |

```toml
[profile.dev]
opt-level = 1               # um pouco de otimização para tornar o dev menos lento

[profile.dev.package."*"]
opt-level = 3               # otimiza só as dependências

[profile.release]
opt-level = 3
lto = "fat"                 # otimização entre crates (link time optimization)
codegen-units = 1           # menos paralelismo, mais otimização
panic = "abort"             # binário menor
strip = true                # remove símbolos
debug = false

# Perfil customizado herdando de release
[profile.profiling]
inherits = "release"
debug = true                # mantém símbolos para flamegraph/perf
```

| Opção | Efeito |
|---|---|
| `opt-level` | `0`–`3`, `"s"` (tamanho), `"z"` (tamanho mínimo) |
| `lto` | `false`, `"thin"`, `"fat"` |
| `codegen-units` | menos unidades → melhor otimização, compilação mais lenta |
| `panic` | `"unwind"` (padrão) ou `"abort"` |
| `strip` | remove símbolos/depuração do binário |

> [!warning] Meça sempre em release
> Comparações de desempenho em `debug` são enganosas, principalmente com iteradores e genéricos.

> [!tip] Binário menor
> `opt-level = "z"`, `lto = true`, `codegen-units = 1`, `panic = "abort"` e `strip = true`.

## Veja também

- [[Cargo.toml e dependências]]
- [[Zero-cost abstractions]]
- [[Cargo básico]]
