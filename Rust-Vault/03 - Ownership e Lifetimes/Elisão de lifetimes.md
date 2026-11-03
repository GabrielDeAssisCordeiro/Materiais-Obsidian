---
tags: [rust, ownership, lifetimes]
aliases: ["lifetime elision", "regras de elisão"]
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Lifetimes]]", "[[Lifetimes em structs]]"]
---

# Elisão de lifetimes

O compilador aplica **três regras de elisão** para preencher lifetimes automaticamente:

1. Cada parâmetro de referência recebe seu próprio lifetime.
2. Se há **exatamente um** lifetime de entrada, ele é atribuído a todos os de saída.
3. Se há `&self` ou `&mut self`, o lifetime de `self` é atribuído às saídas.

```rust
// Regra 2: um parâmetro => o retorno usa o mesmo lifetime
fn primeira_palavra(s: &str) -> &str {
    s.split_whitespace().next().unwrap_or("")
}
// Forma completa (equivalente): fn primeira_palavra<'a>(s: &'a str) -> &'a str

struct Texto {
    conteudo: String,
}

impl Texto {
    // Regra 3: o retorno usa o lifetime de &self
    fn inicio(&self) -> &str {
        &self.conteudo[..2]
    }
}

fn main() {
    println!("{}", primeira_palavra("oi mundo"));
    let t = Texto { conteudo: String::from("abcdef") };
    println!("{}", t.inicio());
}
```

Se as regras não resolvem (como em `maior(a, b)` com dois parâmetros), você precisa anotar manualmente.

> [!tip] Lifetime anônimo
> `'_` pede ao compilador para inferir: `impl Iterator<Item = &'_ str>` ou `fn f(x: &'_ str)`.

## Veja também

- [[Lifetimes]]
- [[Lifetimes em structs]]
