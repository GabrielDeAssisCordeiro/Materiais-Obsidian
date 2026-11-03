---
tags: [rust, macros, metaprogramacao]
aliases: ["proc macros", "derive macro", "attribute macro", "function-like macro"]
tipo: conceito
nivel: avancado
criado: 2026-10-24
relacionados: ["[[macro_rules]]", "[[syn e quote]]", "[[Quando usar e evitar macros]]", "[[derive]]"]
---

# Macros procedurais

**Macros procedurais** são funções Rust que recebem um fluxo de *tokens* e devolvem outro, executadas em compilação. São mais poderosas (e mais trabalhosas) que `macro_rules!`.

## Três tipos

| Tipo | Declaração | Uso | Exemplos conhecidos |
|---|---|---|---|
| **Derive** | `#[proc_macro_derive(Nome)]` | `#[derive(Nome)]` | `Serialize`, `Error` (thiserror), `Parser` (clap) |
| **Atributo** | `#[proc_macro_attribute]` | `#[nome(args)] item` | `#[tokio::main]`, `#[get("/")]` (actix) |
| **Function-like** | `#[proc_macro]` | `nome!(...)` | `sqlx::query!`, `json!` |

## Regra importante

Macros procedurais precisam estar em um **crate separado** com `proc-macro = true`:

```toml
# Cargo.toml do crate de macros
[lib]
proc-macro = true

[dependencies]
syn = { version = "2", features = ["full"] }
quote = "1"
proc-macro2 = "1"
```

## Exemplo: derive

```rust
// requer crate: syn
use proc_macro::TokenStream;
use quote::quote;
use syn::{parse_macro_input, DeriveInput};

#[proc_macro_derive(OlaMacro)]
pub fn ola_derive(entrada: TokenStream) -> TokenStream {
    // 1. Faz o parsing da entrada em uma árvore sintática
    let ast = parse_macro_input!(entrada as DeriveInput);
    let nome = &ast.ident;

    // 2. Gera código com quote!; #nome interpola a variável
    let saida = quote! {
        impl OlaMacro for #nome {
            fn ola() {
                println!("Olá, sou {}!", stringify!(#nome));
            }
        }
    };

    // 3. Converte de volta para TokenStream
    saida.into()
}
```

```rust
// requer crate: syn
// Uso, em outro crate que depende do crate de macros:
trait OlaMacro {
    fn ola();
}

#[derive(OlaMacro)]
struct Panqueca;

fn main() {
    Panqueca::ola(); // "Olá, sou Panqueca!"
}
```

## Atributo e function-like (assinaturas)

```rust
// requer crate: syn
use proc_macro::TokenStream;

// #[rota(GET, "/")] fn index() {}
#[proc_macro_attribute]
pub fn rota(atributos: TokenStream, item: TokenStream) -> TokenStream {
    let _ = atributos; // args do atributo
    item               // aqui você reescreveria ou envolveria o item
}

// consulta!(SELECT ...)
#[proc_macro]
pub fn consulta(entrada: TokenStream) -> TokenStream {
    entrada
}
```

> [!warning] Edição 2024
> `gen` é palavra reservada na edição 2024; não use `gen` como nome de variável em código de macros (use `saida`).

> [!info] Custos
> Proc macros aumentam o tempo de compilação (compilam `syn`/`quote`), podem esconder complexidade e geram mensagens de erro difíceis. Use onde o ganho é grande (derives repetitivos, DSLs).

## Veja também

- [[macro_rules]]
- [[syn e quote]]
- [[Quando usar e evitar macros]]
- [[derive]]
