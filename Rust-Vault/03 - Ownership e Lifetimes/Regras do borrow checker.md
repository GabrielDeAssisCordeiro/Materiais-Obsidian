---
tags: [rust, ownership, borrow-checker]
aliases: ["borrow checker", "aliasing XOR mutabilidade"]
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Borrowing e referências]]", "[[NLL]]", "[[Erros comuns do borrow checker]]", "[[Lifetimes]]"]
---

# Regras do borrow checker

O *borrow checker* aplica uma ideia simples: **ou muitos leitores, ou um escritor** (*aliasing XOR mutability*).

1. Em um dado momento, vale **uma** das opções: várias `&T` **ou** uma única `&mut T`.
2. Toda referência deve ser **válida** (não pode viver mais que o dado).

```rust
// ❌ NÃO COMPILA: &mut enquanto existe &
fn main() {
    let mut v = vec![1, 2, 3];
    let primeiro = &v[0];  // empréstimo imutável
    v.push(4);             // precisa de &mut v
    println!("{primeiro}");
}
```

```text
error[E0502]: cannot borrow `v` as mutable because it is also borrowed as immutable
```

**Por quê?** `push` pode realocar o vetor, deixando `primeiro` apontando para memória liberada.

**Correção:** terminar de usar a referência antes de mutar.

```rust
fn main() {
    let mut v = vec![1, 2, 3];
    let primeiro = v[0]; // cópia do i32: não há empréstimo ativo
    v.push(4);
    println!("{primeiro} {v:?}");
}
```

```rust
// ❌ NÃO COMPILA: duas referências mutáveis
fn main() {
    let mut s = String::from("a");
    let r1 = &mut s;
    let r2 = &mut s;
    r1.push('b');
    r2.push('c');
}
```

```text
error[E0499]: cannot borrow `s` as mutable more than once at a time
```

> [!tip] Isso previne data races
> A mesma regra, aplicada entre threads, evita *data races* em tempo de compilação. Veja [[Concorrência sem medo]].

## Veja também

- [[Borrowing e referências]]
- [[NLL]]
- [[Erros comuns do borrow checker]]
- [[Lifetimes]]
