---
tags: [rust, basico, tipos]
aliases: ["array", "[T; N]"]
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Slices]]", "[[Tuplas]]", "[[Vec]]"]
---

# Arrays

Um **array** tem tamanho fixo conhecido em compilação e vive na pilha: tipo `[T; N]`.

```rust
fn main() {
    let a = [1, 2, 3, 4, 5];
    let b: [i32; 3] = [10, 20, 30];
    let zeros = [0u8; 4];          // [0, 0, 0, 0]

    println!("{} {} {:?}", a[0], b.len(), zeros);

    // Iteração
    for x in a {
        print!("{x} ");
    }
    println!();
}
```

> [!warning] Índice fora dos limites
> `a[10]` em array de 5 elementos causa **panic** em tempo de execução (ou erro de compilação quando o índice é constante e o compilador detecta). Não há acesso inseguro à memória. Use `a.get(10)` para obter `Option`.

```rust
fn main() {
    let a = [1, 2, 3];
    match a.get(10) {
        Some(v) => println!("achou {v}"),
        None => println!("índice inválido"),
    }
}
```

Para tamanho dinâmico use `Vec<T>`.

## Veja também

- [[Slices]]
- [[Tuplas]]
- [[Vec]]
