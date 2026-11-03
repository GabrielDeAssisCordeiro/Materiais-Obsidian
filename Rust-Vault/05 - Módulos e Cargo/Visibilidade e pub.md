---
tags: [rust, modulos]
aliases: ["pub", "pub(crate)", "pub(super)"]
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Módulos e mod]]", "[[use e caminhos]]", "[[Structs]]"]
---

# Visibilidade e pub

Regra geral: um item é visível no **módulo onde está** e nos seus **descendentes**; para os demais, só com `pub`.

| Modificador | Visível em |
|---|---|
| (nenhum) | módulo atual e filhos |
| `pub` | qualquer lugar que alcance o módulo |
| `pub(crate)` | todo o crate |
| `pub(super)` | módulo pai |
| `pub(in caminho)` | módulo ancestral indicado |

```rust
mod a {
    pub(crate) fn publica_no_crate() {
        println!("visível no crate todo");
    }

    pub mod b {
        pub(super) fn so_para_a() {
            println!("só o módulo a vê");
        }
        pub(in crate::a) fn tambem_para_a() {
            println!("restrita a crate::a");
        }
    }

    pub fn chama() {
        b::so_para_a();
        b::tambem_para_a();
    }
}

fn main() {
    a::publica_no_crate();
    a::chama();
}
```

```rust
// ❌ NÃO COMPILA: função privada
mod a {
    fn privada() {}
}

fn main() {
    a::privada();
}
```

```text
error[E0603]: function `privada` is private
```

> [!warning] `pub` em struct não abre os campos
> `pub struct S { x: i32 }` deixa `x` privado. Cada campo precisa de `pub`. Para enums, as variantes são públicas se o enum é público.

> [!tip] API mínima
> Exponha o mínimo necessário. Itens privados podem mudar sem quebrar quem usa a biblioteca.

## Veja também

- [[Módulos e mod]]
- [[use e caminhos]]
- [[Structs]]
