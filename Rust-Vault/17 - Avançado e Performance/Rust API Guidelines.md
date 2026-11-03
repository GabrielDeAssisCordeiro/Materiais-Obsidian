---
tags: [rust, avancado, boas-praticas, api]
aliases: ["API Guidelines", "design de API", "convenções de nomes", "C-CONV"]
tipo: referencia
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Builder]]", "[[Newtype]]", "[[Boas práticas de tratamento de erros]]", "[[cargo doc]]", "[[Traits padrão]]", "[[Versionamento semântico]]"]
---

# Rust API Guidelines

As **Rust API Guidelines** (rust-lang.github.io/api-guidelines) são o checklist oficial para criar bibliotecas idiomáticas.

## Convenções de nomes

| Prefixo | Significado | Custo | Exemplo |
|---|---|---|---|
| `as_` | visão emprestada → emprestada | barato | `str::as_bytes` |
| `to_` | conversão (pode alocar) | variável | `str::to_uppercase` |
| `into_` | consome `self` | variável | `Vec::into_boxed_slice` |
| `is_` / `has_` | booleano | barato | `Vec::is_empty` |
| `iter` / `iter_mut` / `into_iter` | os três tipos de iteração | — | `Vec::iter` |
| `with_` | construtor com opção | — | `Vec::with_capacity` |

## Checklist

- [ ] Implemente as traits comuns: `Debug`, `Clone`, `PartialEq`, `Eq`, `Hash`, `Default`, `Display` quando fizer sentido (veja [[Traits padrão]] e [[derive]]).
- [ ] Prefira **conversões** com `From`/`Into`/`TryFrom`/`AsRef`: [[From e Into]].
- [ ] Argumentos genéricos mínimos: aceite `impl AsRef<str>` ou `&str`, retorne tipos concretos.
- [ ] Erros: tipos de erro dedicados que implementam `std::error::Error` e `Send + Sync`: [[Erros customizados]].
- [ ] Documente tudo com exemplos em [[Doc tests]], incluindo seções `# Errors`, `# Panics` e `# Safety`.
- [ ] Use [[Newtype]] para evitar *stringly typed* APIs; [[Builder]] para configuração complexa.
- [ ] Ponha `#[non_exhaustive]` em enums/structs públicos que possam crescer.
- [ ] Mantenha campos privados e exponha métodos, preservando liberdade de evolução.
- [ ] Siga [[Versionamento semântico]] e mantenha um changelog.
- [ ] Ative `#![warn(missing_docs)]` e `cargo clippy`: [[Clippy]].

```rust
use std::path::Path;

/// Conta as linhas de um arquivo.
///
/// # Errors
///
/// Retorna erro de I/O se o arquivo não puder ser lido.
pub fn contar_linhas(caminho: impl AsRef<Path>) -> std::io::Result<usize> {
    let conteudo = std::fs::read_to_string(caminho)?;
    Ok(conteudo.lines().count())
}

#[derive(Debug, Clone, PartialEq, Eq, Hash, Default)]
#[non_exhaustive]
pub struct Opcoes {
    pub ignorar_vazias: bool,
}

fn main() {
    println!("{:?}", contar_linhas("/caminho/inexistente").is_err());
    println!("{:?}", Opcoes::default());
}
```

## Veja também

- [[Builder]]
- [[Newtype]]
- [[Boas práticas de tratamento de erros]]
- [[cargo doc]]
- [[Traits padrão]]
- [[Versionamento semântico]]
