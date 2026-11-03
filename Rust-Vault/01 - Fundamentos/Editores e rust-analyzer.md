---
tags: [rust, fundamentos, ferramentas]
aliases: ["rust-analyzer", "IDE para Rust"]
tipo: ferramenta
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Instalação com rustup]]", "[[Primeiro programa Hello World]]"]
---

# Editores e rust-analyzer

O **rust-analyzer** é o servidor de linguagem (LSP) oficial. Ele fornece autocompletar, ir para definição, *inlay hints* (tipos inferidos exibidos no código), refatorações e diagnósticos em tempo real.

## Opções de editor

| Editor | Como configurar |
|---|---|
| VS Code | Extensão "rust-analyzer" |
| RustRover (JetBrains) | IDE dedicada a Rust |
| Neovim / Helix / Emacs | Cliente LSP + rust-analyzer |
| Zed | Suporte nativo |

```bash
# Instala o rust-analyzer como componente do rustup
rustup component add rust-analyzer
```

> [!tip] Inlay hints
> Ative as dicas de tipo: elas ajudam muito a entender inferência de tipos e lifetimes enquanto você aprende.

> [!info] Formatar ao salvar
> Configure o editor para rodar o `rustfmt` ao salvar; veja [[Cargo básico]].

## Veja também

- [[Instalação com rustup]]
- [[Primeiro programa Hello World]]
