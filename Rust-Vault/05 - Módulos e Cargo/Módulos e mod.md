---
tags: [rust, modulos]
aliases: ["mod", "módulo inline", "módulo em arquivo"]
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Visibilidade e pub]]", "[[use e caminhos]]", "[[Packages, crates e módulos]]"]
---

# Módulos e mod

`mod` declara um módulo. Itens dentro dele são **privados por padrão**.

```rust
mod jardim {
    pub mod legumes {
        #[derive(Debug)]
        pub struct Cenoura {
            pub tamanho: u32,
            segredo: u8, // campo privado ao módulo legumes
        }

        impl Cenoura {
            pub fn nova(tamanho: u32) -> Self {
                Self { tamanho, segredo: 7 }
            }
            pub fn segredo(&self) -> u8 {
                self.segredo
            }
        }
    }

    pub fn planta() {
        println!("plantando");
        colhe(); // funções privadas são visíveis dentro do mesmo módulo
    }

    fn colhe() {
        println!("colhendo");
    }
}

use jardim::legumes::Cenoura;

fn main() {
    jardim::planta();
    let c = Cenoura::nova(3);
    println!("{:?} {}", c, c.segredo());
}
```

## Módulos em arquivos

Declarar `mod nome;` faz o compilador procurar o código em um arquivo.

```text
src/
├── main.rs          # contém: mod rede;
├── rede.rs          # módulo rede (ou rede/mod.rs, estilo antigo)
└── rede/
    └── http.rs      # submódulo: em rede.rs declare `pub mod http;`
```

```rust
// trecho: src/main.rs
mod rede; // carrega src/rede.rs

fn main() {
    rede::conecta();
}
```

> [!tip] Estilo atual
> Prefira `rede.rs` + pasta `rede/` para submódulos; o estilo `rede/mod.rs` continua válido, mas é o antigo.

## Veja também

- [[Visibilidade e pub]]
- [[use e caminhos]]
- [[Packages, crates e módulos]]
