---
tags: [rust, macros, crates]
aliases: ["syn", "quote", "proc-macro2", "TokenStream", "parse_macro_input"]
tipo: ferramenta
nivel: avancado
criado: 2026-10-24
relacionados: ["[[Macros procedurais]]", "[[macro_rules]]", "[[Enums]]"]
---

# syn e quote

Três crates formam a base para escrever macros procedurais:

| Crate | Papel |
|---|---|
| `proc-macro2` | `TokenStream` utilizável fora de macros (testável) |
| `syn` | **parser**: transforma tokens em árvore sintática (`DeriveInput`, `ItemFn`, `Expr`...) |
| `quote` | **gerador**: `quote! { ... }` produz tokens, com interpolação `#variavel` e repetição `#( ... )*` |

## Exemplo: listar os campos de uma struct

```rust
// requer crate: syn
use proc_macro::TokenStream;
use quote::quote;
use syn::{parse_macro_input, Data, DataStruct, DeriveInput, Fields};

#[proc_macro_derive(NomesDosCampos)]
pub fn nomes_dos_campos(entrada: TokenStream) -> TokenStream {
    let ast = parse_macro_input!(entrada as DeriveInput);
    let nome = &ast.ident;

    // Percorre a estrutura sintática: só aceita structs com campos nomeados
    let campos: Vec<String> = match &ast.data {
        Data::Struct(DataStruct { fields: Fields::Named(f), .. }) => f
            .named
            .iter()
            .map(|c| c.ident.as_ref().unwrap().to_string())
            .collect(),
        _ => {
            return syn::Error::new_spanned(&ast, "NomesDosCampos exige uma struct com campos nomeados")
                .to_compile_error()
                .into();
        }
    };

    // #( #campos ),* repete a interpolação separada por vírgulas
    quote! {
        impl #nome {
            pub fn nomes_dos_campos() -> &'static [&'static str] {
                &[ #( #campos ),* ]
            }
        }
    }
    .into()
}
```

```rust
// requer crate: syn
// Uso:
#[derive(NomesDosCampos)]
struct Usuario {
    id: u32,
    nome: String,
}

fn main() {
    println!("{:?}", Usuario::nomes_dos_campos()); // ["id", "nome"]
}
```

## Boas práticas

- Reporte erros com `syn::Error` (apontando para o trecho certo) em vez de `panic!`.
- Teste a expansão com `cargo expand` e o crate **`trybuild`** (casos que devem compilar e que devem falhar).
- Gere caminhos absolutos (`::std::...`) para evitar colisões com nomes do usuário.

> [!question] Verificar na documentação oficial
> Confirme as APIs atuais de `syn` 2.x em docs.rs/syn; os tipos e os *features* (`full`, `extra-traits`) afetam o que está disponível.

## Veja também

- [[Macros procedurais]]
- [[macro_rules]]
- [[Enums]]
