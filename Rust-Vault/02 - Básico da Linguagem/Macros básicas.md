---
tags: [rust, basico, macros]
aliases: ["println!", "format!", "vec!", "dbg!", "assert!"]
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Formatação com println]]", "[[Primeiro programa Hello World]]", "[[macro_rules]]"]
---

# Macros básicas

Macros terminam com `!` e são expandidas em tempo de compilação. As mais usadas:

| Macro | Função |
|---|---|
| `println!` / `print!` | Escrever em stdout |
| `eprintln!` / `eprint!` | Escrever em stderr |
| `format!` | Criar uma `String` formatada |
| `vec!` | Criar um `Vec` |
| `dbg!` | Imprimir expressão e valor (stderr) e devolver o valor |
| `assert!`, `assert_eq!` | Verificações (panic se falhar) |
| `panic!` | Abortar a thread com mensagem |
| `todo!`, `unimplemented!`, `unreachable!` | Marcadores de código |
| `matches!` | Testa se um valor casa com um padrão |

```rust
fn main() {
    let v = vec![1, 2, 3];
    let texto = format!("{v:?}");
    println!("{texto}");

    let x = dbg!(2 * 3) + 1; // imprime [src/main.rs:L:C] 2 * 3 = 6 em stderr
    assert_eq!(x, 7);

    println!("{}", matches!(Some(5), Some(n) if n > 3));
}
```

> [!tip] `dbg!` x `println!`
> `dbg!` mostra arquivo/linha e **toma posse** do valor, devolvendo-o; para tipos sem `Copy`, passe uma referência: `dbg!(&valor)`.

## Veja também

- [[Formatação com println]]
- [[Primeiro programa Hello World]]
- [[macro_rules]]
