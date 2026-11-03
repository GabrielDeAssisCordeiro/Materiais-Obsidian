---
tags: [rust, ownership, borrow-checker]
aliases: ["Non-Lexical Lifetimes", "lifetimes não lexicais"]
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Regras do borrow checker]]", "[[Lifetimes]]"]
---

# NLL

Com **NLL** (*non-lexical lifetimes*), um empréstimo dura **até o último uso** da referência, e não até o fim do bloco `{ }`.

```rust
fn main() {
    let mut s = String::from("olá");

    let r1 = &s;
    let r2 = &s;
    println!("{r1} {r2}");
    // r1 e r2 não são mais usadas a partir daqui

    let r3 = &mut s; // OK: os empréstimos anteriores já terminaram
    r3.push('!');
    println!("{r3}");
}
```

Sem NLL (antes da edição 2018), esse código era rejeitado, pois `r1` e `r2` "viveriam" até o fim do escopo.

> [!info] Limitações
> O NLL ainda é conservador em alguns casos (por exemplo, certos retornos condicionais de referências). O projeto Polonius busca um verificador mais preciso.
> [!question] Verificar na documentação oficial
> Confirme o estado atual do Polonius na versão estável antes de citá-lo como disponível.

## Veja também

- [[Regras do borrow checker]]
- [[Lifetimes]]
