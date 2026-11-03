---
tags: [rust, ownership, lifetimes, structs]
aliases: ["struct com referência", "struct<'a>"]
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Lifetimes]]", "[[Elisão de lifetimes]]", "[[Structs]]"]
---

# Lifetimes em structs

Uma struct que guarda **referências** precisa declarar o lifetime, garantindo que ela não sobreviva ao dado emprestado.

```rust
struct Trecho<'a> {
    parte: &'a str,
}

impl<'a> Trecho<'a> {
    fn tamanho(&self) -> usize {
        self.parte.len()
    }
}

fn main() {
    let romance = String::from("Chamem-me Ismael. Há alguns anos...");
    let primeira = romance.split('.').next().unwrap();
    let t = Trecho { parte: primeira };
    println!("{} ({} bytes)", t.parte, t.tamanho());
}
```

```rust
// ❌ NÃO COMPILA: a struct sobreviveria ao dado
struct Trecho<'a> {
    parte: &'a str,
}

fn main() {
    let t;
    {
        let texto = String::from("curto");
        t = Trecho { parte: &texto };
    } // texto é liberado aqui
    println!("{}", t.parte);
}
```

```text
error[E0597]: `texto` does not live long enough
```

> [!tip] Alternativa
> Se a complexidade dos lifetimes atrapalha, a struct pode **possuir** os dados (`String` em vez de `&str`) ao custo de uma alocação.

## Veja também

- [[Lifetimes]]
- [[Elisão de lifetimes]]
- [[Structs]]
