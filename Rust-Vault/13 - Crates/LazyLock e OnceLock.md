---
tags: [rust, crates, std]
aliases: ["LazyLock", "OnceLock", "once_cell", "lazy_static", "inicialização preguiçosa"]
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Constantes e statics]]", "[[Mutex e RwLock]]", "[[regex]]"]
---

# LazyLock e OnceLock

A biblioteca padrão traz inicialização **preguiçosa e thread-safe** que substitui os crates `once_cell` e `lazy_static` na maioria dos usos (`OnceLock`, `LazyLock` e `OnceCell`/`LazyCell` estáveis nas versões recentes).

```rust
use std::collections::HashMap;
use std::sync::{LazyLock, Mutex, OnceLock};

// LazyLock: inicializado na primeira vez que for acessado
static TABELA: LazyLock<HashMap<&'static str, u32>> = LazyLock::new(|| {
    println!("inicializando tabela...");
    HashMap::from([("um", 1), ("dois", 2), ("tres", 3)])
});

// LazyLock + Mutex: estado global mutável
static HISTORICO: LazyLock<Mutex<Vec<String>>> = LazyLock::new(|| Mutex::new(Vec::new()));

// OnceLock: valor definido uma única vez, possivelmente em runtime
static CONFIG: OnceLock<String> = OnceLock::new();

fn main() {
    println!("antes do primeiro acesso");
    println!("{:?}", TABELA.get("dois")); // aqui a closure roda
    println!("{:?}", TABELA.get("tres")); // não roda de novo

    HISTORICO.lock().unwrap().push("start".to_string());
    println!("{:?}", HISTORICO.lock().unwrap());

    CONFIG.set("producao".to_string()).unwrap();
    println!("{:?}", CONFIG.get());
    println!("{:?}", CONFIG.set("outra".to_string()).is_err()); // true: já definido
}
```

| Tipo | Quando usar |
|---|---|
| `LazyLock<T>` | valor global com inicializador conhecido de antemão |
| `OnceLock<T>` | valor global definido depois (ex.: lido da configuração) |
| `LazyCell` / `OnceCell` | mesma ideia, **sem** thread-safety (uma thread) |

> [!question] Verificar na documentação oficial
> Confirme a versão em que `LazyLock` foi estabilizado e se a sua toolchain o inclui; em toolchains antigas use `once_cell`.

## Veja também

- [[Constantes e statics]]
- [[Mutex e RwLock]]
- [[regex]]
