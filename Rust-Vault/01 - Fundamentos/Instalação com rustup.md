---
tags: [rust, fundamentos, instalacao]
aliases: ["rustup", "Instalar Rust"]
tipo: procedimento
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Toolchains stable beta nightly]]", "[[Editores e rust-analyzer]]", "[[Primeiro programa Hello World]]"]
---

# Instalação com rustup

O **rustup** é o instalador e gerenciador de toolchains oficial. Ele instala `rustc`, `cargo`, `rustfmt`, `clippy` e permite alternar versões.

## Linux e macOS

```bash
# Instala o rustup (veja a página oficial rust-lang.org/tools/install)
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Carrega o cargo no PATH da sessão atual
. "$HOME/.cargo/env"

# Confirma a instalação
rustc --version
cargo --version
```

## Windows

Baixe o `rustup-init.exe` em rust-lang.org/tools/install. O Rust no Windows precisa das ferramentas de build do MSVC (Visual Studio Build Tools) ou do alvo GNU.

## Comandos úteis do rustup

```bash
rustup update                      # atualiza as toolchains instaladas
rustup show                        # mostra toolchain ativa e alvos
rustup component add clippy rustfmt  # adiciona componentes
rustup target add wasm32-unknown-unknown  # adiciona um alvo de compilação
rustup toolchain install nightly   # instala a nightly
rustup default stable              # define a toolchain padrão
rustup doc --book                  # abre o livro oficial offline
```

> [!tip] Documentação offline
> `rustup doc` abre a documentação local no navegador: livro, std, Rust by Example e mais.

## Exercício

Instale o Rust, rode `rustup show` e anote a versão do `rustc`.

## Veja também

- [[Toolchains stable beta nightly]]
- [[Editores e rust-analyzer]]
- [[Primeiro programa Hello World]]
