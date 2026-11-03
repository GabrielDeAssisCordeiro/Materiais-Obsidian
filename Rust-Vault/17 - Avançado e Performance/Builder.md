---
tags: [rust, avancado, padroes, api]
aliases: ["builder pattern", "construtor fluente"]
tipo: padrao
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Typestate]]", "[[Default]]", "[[Structs]]", "[[Erros customizados]]"]
---

# Builder

O **builder** constrói objetos com muitos parâmetros opcionais por encadeamento de métodos, já que Rust não tem argumentos nomeados nem opcionais.

```rust
#[derive(Debug)]
struct Servidor {
    host: String,
    porta: u16,
    threads: usize,
    tls: bool,
}

#[derive(Default)]
struct ServidorBuilder {
    host: Option<String>,
    porta: Option<u16>,
    threads: Option<usize>,
    tls: bool,
}

impl ServidorBuilder {
    fn novo() -> Self {
        Self::default()
    }

    fn host(mut self, h: &str) -> Self {
        self.host = Some(h.to_string());
        self
    }

    fn porta(mut self, p: u16) -> Self {
        self.porta = Some(p);
        self
    }

    fn threads(mut self, n: usize) -> Self {
        self.threads = Some(n);
        self
    }

    fn tls(mut self, ativo: bool) -> Self {
        self.tls = ativo;
        self
    }

    // `build` valida e devolve Result
    fn build(self) -> Result<Servidor, String> {
        let host = self.host.ok_or("host é obrigatório")?;
        Ok(Servidor {
            host,
            porta: self.porta.unwrap_or(8080),
            threads: self.threads.unwrap_or(4),
            tls: self.tls,
        })
    }
}

fn main() {
    let s = ServidorBuilder::novo()
        .host("localhost")
        .porta(3000)
        .tls(true)
        .build();
    println!("{s:?}");

    let erro = ServidorBuilder::novo().porta(1).build();
    println!("{erro:?}"); // Err("host é obrigatório")
}
```

| Variante | Quando |
|---|---|
| Builder por valor (`self -> Self`) | construção única, como acima |
| Builder por referência (`&mut self -> &mut Self`) | reutilizar o builder; padrão da `std::process::Command` |
| Builder com [[Typestate]] | campos obrigatórios verificados em compilação |
| `..Default::default()` | structs simples: veja [[Default]] |

> [!tip] Na biblioteca padrão
> `std::process::Command`, `std::thread::Builder` e `std::fs::OpenOptions` são builders. Crates como `bon` e `derive_builder` geram o código para você.

## Veja também

- [[Typestate]]
- [[Default]]
- [[Structs]]
- [[Erros customizados]]
