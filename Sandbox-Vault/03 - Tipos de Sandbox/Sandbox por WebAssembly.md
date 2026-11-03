---
tags:
  - tipos
aliases: []
tipo: tipo-de-sandbox
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Criar Sandbox com WebAssembly e Wasmtime]]"
  - "[[Sandbox em Linguagem]]"
  - "[[Caso - Plugins e Extensões]]"
---
# Sandbox por WebAssembly

**WebAssembly (Wasm)** é um formato binário executado por uma máquina virtual com **memória linear isolada**. Por padrão, o módulo **não tem acesso** a arquivos, rede ou relógio; só ao que o hospedeiro oferece.

**WASI** define interfaces de sistema baseadas em **capacidades**: o hospedeiro entrega, por exemplo, apenas um diretório específico.

| Vantagem | Limitação |
|---|---|
| Inicialização muito rápida | Nem todo código/biblioteca compila para Wasm |
| Portável, multi-linguagem | Ecossistema WASI ainda evolui |
| Permissões explícitas | Bugs no *runtime* ainda são possíveis |

```bash
# Wasmtime: só o diretório ./dados é visível ao módulo
wasmtime run --dir ./dados app.wasm
```

## Veja também

- [[Criar Sandbox com WebAssembly e Wasmtime]]
- [[Sandbox em Linguagem]]
- [[Caso - Plugins e Extensões]]
- [[MOC - Tipos de Sandbox]]
