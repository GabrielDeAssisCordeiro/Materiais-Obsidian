---
tags: [rust, traits]
aliases: ["regra órfã", "coerência"]
tipo: conceito
nivel: avancado
criado: 2026-10-24
relacionados: ["[[Traits]]", "[[Sobrecarga de operadores]]", "[[Structs tupla e unit]]"]
---

# Orphan rule

**Regra órfã (orphan rule):** só é permitido `impl Trait for Tipo` se **a trait** ou **o tipo** pertencer ao seu crate. Isso impede que dois crates implementem a mesma trait para o mesmo tipo de forma conflitante (coerência).

```rust
// ❌ NÃO COMPILA: Display e Vec são ambos de std
use std::fmt;

impl fmt::Display for Vec<i32> {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "vetor")
    }
}

fn main() {}
```

```text
error[E0117]: only traits defined in the current crate can be implemented for types defined outside of the crate
```

## Solução: padrão newtype

Embrulhe o tipo externo em uma struct tupla local.

```rust
use std::fmt;

struct Lista(Vec<i32>);

impl fmt::Display for Lista {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        let partes: Vec<String> = self.0.iter().map(|n| n.to_string()).collect();
        write!(f, "[{}]", partes.join(", "))
    }
}

fn main() {
    println!("{}", Lista(vec![1, 2, 3]));
}
```

| Caso | Permitido? |
|---|---|
| Trait local para tipo externo | Sim |
| Trait externa para tipo local | Sim |
| Trait externa para tipo externo | **Não** |

> [!info] Custo do newtype
> Em tempo de execução o newtype tem o mesmo layout do tipo interno: não há custo. Para expor os métodos do tipo interno, considere `Deref` (com cautela) ou delegue manualmente.

## Veja também

- [[Traits]]
- [[Sobrecarga de operadores]]
- [[Structs tupla e unit]]
