---
tags: [rust, performance, cargo]
aliases: ["codegen-units", "opt-level", "panic abort", "strip", "target-cpu"]
tipo: referencia
nivel: avancado
criado: 2026-10-24
relacionados: ["[[Debug vs release]]", "[[Cargo.toml e dependências]]", "[[Perfilamento]]", "[[WebAssembly]]", "[[Otimização de desempenho]]"]
---

# Release profile LTO e codegen

O perfil `release` do Cargo tem muitos botões que trocam **velocidade de execução**, **tamanho do binário** e **tempo de compilação**.

```toml
[profile.release]
opt-level = 3          # 0..3 (velocidade), "s"/"z" (tamanho)
lto = "fat"            # otimização entre crates (false | "thin" | "fat")
codegen-units = 1      # menos paralelismo na compilação, melhor otimização
panic = "abort"        # sem unwinding: binário menor e um pouco mais rápido
strip = true           # remove símbolos do binário final
debug = false          # true para perfilar

# Perfil personalizado herdando de release
[profile.profiling]
inherits = "release"
debug = true
strip = false
```

| Opção | Efeito | Custo |
|---|---|---|
| `lto = "thin"` | boa otimização entre crates | pouco tempo extra |
| `lto = "fat"` | máxima otimização | compilação lenta |
| `codegen-units = 1` | melhor *inlining* | compilação mais lenta |
| `panic = "abort"` | menos código | não permite `catch_unwind` nem testes com panics capturados |
| `opt-level = "z"` | menor binário | mais lento |
| `strip = true` | binário menor | sem símbolos para depurar |

## Outras ferramentas

```bash
# Otimizar para a CPU local (não portátil!)
RUSTFLAGS="-C target-cpu=native" cargo build --release

# Otimização guiada por perfil (PGO), via cargo-pgo
cargo install cargo-pgo
cargo pgo build

# Ver o que mais pesa no binário
cargo install cargo-bloat
cargo bloat --release -n 10
```

> [!warning] `target-cpu=native`
> O binário pode não executar em máquinas mais antigas. Para distribuição, use um nível alvo conservador (por exemplo, `x86-64-v3`) ou detecção em tempo de execução (veja [[SIMD e vetorização]]).

> [!question] Verificar na documentação oficial
> Confirme valores aceitos e padrões em doc.rust-lang.org/cargo/reference/profiles.html.

## Veja também

- [[Debug vs release]]
- [[Cargo.toml e dependências]]
- [[Perfilamento]]
- [[WebAssembly]]
- [[Otimização de desempenho]]
