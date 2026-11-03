---
tags: [rust, option, result, erros]
aliases: ["unwrap_or", "ok_or", "combinadores"]
tipo: referencia
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Option e Result]]", "[[Closures]]", "[[Operador de interrogação]]"]
---

# Combinadores de Option e Result

Métodos que transformam `Option`/`Result` sem `match` explícito:

| Método | O que faz |
|---|---|
| `map(f)` | aplica `f` ao valor interno |
| `and_then(f)` | encadeia operação que também devolve `Option`/`Result` |
| `unwrap_or(v)` / `unwrap_or_else(f)` / `unwrap_or_default()` | valor padrão |
| `ok_or(e)` / `ok_or_else(f)` | `Option` → `Result` |
| `ok()` | `Result` → `Option` (descarta o erro) |
| `map_err(f)` | transforma o erro |
| `filter(p)` | `Some` só se o predicado valer |
| `is_some()`, `is_none()`, `is_ok()`, `is_err()` | testes |
| `take()` | tira o valor deixando `None` |

```rust
fn main() {
    let nome: Option<&str> = Some("  ana ");

    let tamanho = nome.map(|n| n.trim().len()).unwrap_or(0);
    println!("{tamanho}"); // 3

    // Encadeando
    let n: Option<i32> = "42".parse().ok();
    let r = n.and_then(|v| v.checked_mul(2)).filter(|v| *v > 50);
    println!("{:?}", r); // Some(84)

    // Option -> Result
    let r: Result<i32, String> = None.ok_or("faltou valor".to_string());
    println!("{:?}", r);

    // map_err
    let r2: Result<i32, String> = "abc".parse::<i32>().map_err(|e| e.to_string());
    println!("{:?}", r2);

    // take
    let mut slot = Some(5);
    let antigo = slot.take();
    println!("{:?} {:?}", antigo, slot); // Some(5) None
}
```

> [!tip] Quando usar `match` em vez de combinadores
> Quando a lógica fica difícil de ler em cadeia, um `match` claro vence uma sequência de `and_then`.

## Veja também

- [[Option e Result]]
- [[Closures]]
- [[Operador de interrogação]]
