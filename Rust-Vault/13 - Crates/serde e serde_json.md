---
tags: [rust, crates, json]
aliases: ["serde", "serde_json", "Serialize", "Deserialize"]
tipo: ferramenta
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[derive]]", "[[Escolhendo e avaliando crates]]", "[[Erros customizados]]"]
---

# serde e serde_json

**serde** é o framework de (de)serialização: o mesmo `derive` funciona com JSON, TOML, YAML, bincode, MessagePack e mais.

```toml
[dependencies]
serde = { version = "1", features = ["derive"] }
serde_json = "1"
```

```rust
// requer crate: serde
use serde::{Deserialize, Serialize};

#[derive(Debug, Serialize, Deserialize)]
struct Usuario {
    id: u32,
    #[serde(rename = "nomeCompleto")]       // nome diferente no JSON
    nome: String,
    #[serde(default)]                       // usa Default se ausente
    ativo: bool,
    #[serde(skip_serializing_if = "Option::is_none")]
    email: Option<String>,
}

fn main() -> Result<(), serde_json::Error> {
    let u = Usuario { id: 1, nome: "Ana".into(), ativo: true, email: None };

    let json = serde_json::to_string(&u)?;          // struct -> String
    println!("{json}");                              // {"id":1,"nomeCompleto":"Ana","ativo":true}

    let de: Usuario = serde_json::from_str(r#"{"id":2,"nomeCompleto":"Bia"}"#)?;
    println!("{:?}", de);

    // JSON dinâmico
    let v: serde_json::Value = serde_json::from_str(r#"{"a": [1, 2, 3]}"#)?;
    println!("{}", v["a"][1]); // 2
    let v2 = serde_json::json!({ "x": 1, "lista": [true, null] });
    println!("{}", serde_json::to_string_pretty(&v2)?);
    Ok(())
}
```

| Atributo | Efeito |
|---|---|
| `#[serde(rename = "x")]` | renomeia campo/variante |
| `#[serde(rename_all = "camelCase")]` | converte todos os nomes |
| `#[serde(default)]` | valor padrão se faltar |
| `#[serde(skip)]` / `skip_serializing_if` | omite campo |
| `#[serde(flatten)]` | achata struct aninhada |
| `#[serde(tag = "tipo")]` | enum com tag interna |

> [!question] Verificar na documentação oficial
> As APIs de crates externos mudam entre versões maiores. Confirme versão e exemplos em docs.rs/serde antes de copiar para um projeto.

## Veja também

- [[derive]]
- [[Escolhendo e avaliando crates]]
- [[Erros customizados]]
