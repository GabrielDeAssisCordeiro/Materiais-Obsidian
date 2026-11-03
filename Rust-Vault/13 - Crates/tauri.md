---
tags: [rust, crates]
aliases: ["tauri", "apps desktop", "webview"]
tipo: ferramenta
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Áreas de Aplicação]]", "[[serde e serde_json]]"]
---

# tauri

**Tauri** cria aplicativos desktop (e mobile) com **front-end web** (HTML/JS/TS e qualquer framework) e **back-end em Rust**, usando o webview do sistema (binários pequenos, sem embutir um navegador).

```text
meu-app/
├── src/              # front-end (React, Svelte, Vue, JS puro...)
└── src-tauri/
    ├── Cargo.toml
    ├── tauri.conf.json
    └── src/main.rs   # back-end Rust
```

```rust
// requer crate: tauri
// src-tauri/src/main.rs
#[tauri::command]
fn saudar(nome: &str) -> String {
    format!("Olá, {nome}! (vindo do Rust)")
}

fn main() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![saudar])
        .run(tauri::generate_context!())
        .expect("erro ao executar o app");
}
```

```bash
cargo install create-tauri-app --locked
cargo create-tauri-app
cargo tauri dev        # modo desenvolvimento
cargo tauri build      # empacota para a plataforma
```

No front-end, a chamada fica `invoke('saudar', { nome: 'Ana' })`.

> [!question] Verificar na documentação oficial
> Os comandos e a estrutura mudaram da versão 1 para a 2. Siga o guia atual em tauri.app.

> [!info] Segurança
> O Tauri usa um sistema de **permissões/capabilities** para limitar o que o front-end pode chamar do back-end.

## Veja também

- [[Áreas de Aplicação]]
- [[serde e serde_json]]
