---
tags: [rust, erros]
aliases: ["panic!", "unwrap", "expect", "erros irrecuperáveis", "RUST_BACKTRACE"]
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Operador de interrogação]]", "[[Option e Result]]", "[[Boas práticas de tratamento de erros]]"]
---

# Panic

Rust separa erros em duas categorias:

| Categoria | Mecanismo | Exemplo |
|---|---|---|
| **Recuperável** | `Result<T, E>` / `Option<T>` | arquivo não encontrado, entrada inválida |
| **Irrecuperável** (bug) | `panic!` | índice fora do limite, invariante violada |

```rust
fn main() {
    let v = vec![1, 2, 3];
    let r = std::panic::catch_unwind(|| {
        let v = vec![1, 2, 3];
        v[10] // panic: index out of bounds
    });
    println!("capturado: {}", r.is_err());
    println!("{:?}", v);
}
```

## Fontes comuns de panic

- `panic!("mensagem")`, `unreachable!()`, `todo!()`, `unimplemented!()`
- `option.unwrap()` / `result.unwrap()` / `expect("contexto")`
- indexação `v[i]` fora do limite, divisão inteira por zero
- `assert!`, `assert_eq!`, `RefCell::borrow_mut` em empréstimo ativo
- estouro aritmético em debug

```rust
// Boas mensagens com expect descrevem a invariante, não o erro
fn main() {
    let porta: u16 = "8080".parse().expect("PORTA padrão deve ser um número válido");
    println!("{porta}");
}
```

## Backtrace

```bash
RUST_BACKTRACE=1 cargo run      # mostra a pilha de chamadas
RUST_BACKTRACE=full cargo run   # versão completa
```

## Abortar em vez de desenrolar a pilha

```toml
[profile.release]
panic = "abort"   # binário menor; sem unwinding nem catch_unwind
```

> [!tip] Quando usar `panic!`
> Em bugs de programação, estados "impossíveis", testes e protótipos. Para falhas esperadas (rede, disco, entrada do usuário), devolva `Result`.

> [!warning] Bibliotecas
> Uma biblioteca não deve causar panic por causa de entrada do usuário; documente qualquer panic possível em `# Panics`.

## Veja também

- [[Operador de interrogação]]
- [[Option e Result]]
- [[Boas práticas de tratamento de erros]]
