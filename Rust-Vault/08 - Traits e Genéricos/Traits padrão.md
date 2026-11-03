---
tags: [rust, traits, std]
aliases: ["Debug", "Display", "PartialEq", "Eq", "PartialOrd", "Ord", "Hash"]
tipo: referencia
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[derive]]", "[[From e Into]]", "[[Deref e AsRef]]", "[[Sobrecarga de operadores]]", "[[Drop e RAII]]"]
---

# Traits padrão

| Trait | Função | `derive`? |
|---|---|---|
| `Debug` | formatar com `{:?}` (desenvolvedor) | sim |
| `Display` | formatar com `{}` (usuário) | **não** (manual) |
| `Clone` | duplicar com `.clone()` | sim |
| `Copy` | cópia bit a bit implícita | sim (exige `Clone`) |
| `PartialEq` / `Eq` | `==` / igualdade total | sim |
| `PartialOrd` / `Ord` | `<`, `>` / ordem total | sim |
| `Hash` | uso como chave de `HashMap` | sim |
| `Default` | valor padrão | sim |
| `From` / `Into` | conversões infalíveis | não |
| `TryFrom` / `TryInto` | conversões falíveis | não |
| `Iterator` / `IntoIterator` | iteração | não |
| `Deref` / `DerefMut` | comportamento de ponteiro | não |
| `Drop` | limpeza ao destruir | não |
| `AsRef` / `AsMut` | conversão barata de referência | não |
| `Send` / `Sync` | segurança entre threads | automáticas |

```rust
use std::collections::HashSet;
use std::fmt;

#[derive(Debug, Clone, PartialEq, Eq, Hash, PartialOrd, Ord, Default)]
struct Versao {
    maior: u32,
    menor: u32,
    patch: u32,
}

// Display é sempre manual
impl fmt::Display for Versao {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{}.{}.{}", self.maior, self.menor, self.patch)
    }
}

fn main() {
    let a = Versao { maior: 1, menor: 2, patch: 3 };
    let b = Versao { maior: 1, menor: 10, patch: 0 };

    println!("{a} < {b}? {}", a < b);        // compara campo a campo, na ordem
    println!("{:?}", a.clone().max(b.clone()));

    let mut set = HashSet::new();
    set.insert(a.clone());
    println!("{}", set.contains(&a));

    println!("{}", Versao::default());       // 0.0.0
}
```

> [!warning] `PartialEq` x `Eq`, `PartialOrd` x `Ord`
> `f64` implementa só as versões "Partial" porque `NaN != NaN`. Por isso `f64` não serve como chave de `HashMap` nem entra em `sort()`; veja [[Ordenação e busca]].

> [!info] Relação entre traits
> `Eq: PartialEq`, `Ord: Eq + PartialOrd`, `Copy: Clone`. Se você implementa `Hash` manualmente, ele deve ser consistente com `Eq`: valores iguais, hashes iguais.

## Veja também

- [[derive]]
- [[From e Into]]
- [[Deref e AsRef]]
- [[Sobrecarga de operadores]]
- [[Drop e RAII]]
