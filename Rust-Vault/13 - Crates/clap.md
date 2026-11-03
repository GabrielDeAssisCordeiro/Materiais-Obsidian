---
tags: [rust, crates, cli]
aliases: ["clap", "argumentos de linha de comando", "Parser", "Subcommand"]
tipo: ferramenta
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[derive]]", "[[Escolhendo e avaliando crates]]", "[[CLI com Rust]]"]
---

# clap

**clap** analisa argumentos de linha de comando e gera `--help` automaticamente. A forma mais usada é a API **derive**.

```toml
[dependencies]
clap = { version = "4", features = ["derive"] }
```

```rust
// requer crate: clap
use clap::{Parser, Subcommand};

/// Gerenciador de tarefas de exemplo
#[derive(Parser, Debug)]
#[command(name = "tarefas", version, about)]
struct Cli {
    /// Arquivo de dados
    #[arg(short, long, default_value = "tarefas.json")]
    arquivo: String,

    /// Mais detalhes na saída (-v, -vv)
    #[arg(short, long, action = clap::ArgAction::Count)]
    verbose: u8,

    #[command(subcommand)]
    comando: Comando,
}

#[derive(Subcommand, Debug)]
enum Comando {
    /// Adiciona uma tarefa
    Add { titulo: String },
    /// Lista as tarefas
    List {
        #[arg(long)]
        apenas_abertas: bool,
    },
}

fn main() {
    let cli = Cli::parse(); // sai com mensagem de erro/ajuda se os argumentos forem inválidos
    match cli.comando {
        Comando::Add { titulo } => println!("adicionando {titulo} em {}", cli.arquivo),
        Comando::List { apenas_abertas } => println!("listando (abertas: {apenas_abertas})"),
    }
}
```

```bash
cargo run -- add "estudar Rust"
cargo run -- --help
cargo run -- list --apenas-abertas
```

> [!tip] Comentários `///` viram texto de ajuda
> Cada comentário de documentação em campos e variantes é usado como descrição no `--help`.

> [!question] Verificar na documentação oficial
> As APIs de crates externos mudam entre versões maiores. Confirme versão e exemplos em docs.rs/clap antes de copiar para um projeto.

## Veja também

- [[derive]]
- [[Escolhendo e avaliando crates]]
- [[CLI com Rust]]
