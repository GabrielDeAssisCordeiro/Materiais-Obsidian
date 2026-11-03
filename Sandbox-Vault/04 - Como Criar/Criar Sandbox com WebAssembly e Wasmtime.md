---
tags:
  - como-criar
aliases: []
tipo: procedimento
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Sandbox por WebAssembly]]"
  - "[[Sandbox em Linguagem]]"
---
# Criar Sandbox com WebAssembly e Wasmtime

```bash
# Instalação (inspecione o script antes de executar, ou use o gerenciador de pacotes)
curl https://wasmtime.dev/install.sh -sSf -o install-wasmtime.sh
less install-wasmtime.sh && bash install-wasmtime.sh

# Compilar um programa Rust para WASI
rustup target add wasm32-wasip1
cargo build --release --target wasm32-wasip1
```

Executar com capacidades mínimas:

```bash
# Sem flags: o módulo não enxerga arquivos
wasmtime run target/wasm32-wasip1/release/app.wasm

# Libera somente o diretório ./dados
wasmtime run --dir ./dados target/wasm32-wasip1/release/app.wasm

# Variável de ambiente explícita
wasmtime run --env MODO=teste target/wasm32-wasip1/release/app.wasm
```

> [!question] Verificar na documentação oficial
> O alvo foi renomeado de `wasm32-wasi` para `wasm32-wasip1`. Limites de execução (combustível, tempo) variam por versão; veja `wasmtime run -W help`.

> [!tip] Capacidades, não permissões globais
> Cada diretório liberado é uma capacidade explícita. É o modelo oposto ao de um processo comum.

## Exercício

Escreva um programa que tenta abrir `/etc/passwd` e rode-o no Wasmtime com e sem `--dir`.

## Veja também

- [[Sandbox por WebAssembly]]
- [[Sandbox em Linguagem]]
- [[Caso - Plugins e Extensões]]
- [[MOC - Como Criar]]
