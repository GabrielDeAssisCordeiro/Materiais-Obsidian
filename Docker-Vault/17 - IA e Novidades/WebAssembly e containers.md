---
tags:
  - docker
  - ia
  - novidades
aliases: []
tipo: conceito
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[containerd e runc]]"
  - "[[Padrão OCI]]"
  - "[[Build multiplataforma]]"
---

# WebAssembly e containers

**WebAssembly (Wasm)** é um formato binário portátil, seguro (sandbox) e de inicialização muito rápida. Com **WASI**, módulos Wasm rodam fora do navegador (servidores, edge).

## Wasm vs containers

| Característica | Container Linux | Wasm/WASI |
|---|---|---|
| Isolamento | Kernel compartilhado + namespaces | Sandbox da VM Wasm (capabilities explícitas) |
| Tamanho | MBs a GBs | KBs a poucos MBs |
| Inicialização | Segundos/milissegundos | **Microssegundos/milissegundos** |
| Portabilidade | Por arquitetura (multi-arch) | **Independente de arquitetura** |
| Maturidade/ecossistema | **Muito alta** | Em evolução (WASI 0.2/0.3) |

## Integração com o ecossistema de containers

- O **containerd** executa Wasm por meio de *shims* (projeto **runwasi**: Wasmtime, WasmEdge, Spin).
- Módulos Wasm podem ser empacotados como **artefatos OCI** e distribuídos em registries.
- No Kubernetes, selecione o runtime por `RuntimeClass`; frameworks como **Spin/SpinKube** facilitam.

```bash
# Conceito: executar um módulo Wasm empacotado como imagem (requer runtime e suporte habilitados)
docker run --rm \
  --runtime=io.containerd.wasmtime.v1 \
  --platform=wasi/wasm \
  IMAGEM-WASM
```

> [!question] Verificar na documentação oficial
> O suporte a Wasm no Docker Desktop/Engine é **experimental ou em evolução**; os nomes dos runtimes (`io.containerd.*`), a necessidade do containerd image store e as imagens de exemplo mudam. Consulte a documentação "Wasm workloads".

> [!info] Complemento, não substituto
> Wasm brilha em *edge*, *plugins*, funções e cargas curtas. Aplicações tradicionais com sistema de arquivos, bibliotecas nativas e longa duração seguem nos containers Linux.

## Exercício

Pesquise um exemplo de aplicação Spin/Wasm e descreva duas vantagens e duas limitações em comparação com um container tradicional para a mesma tarefa.

## Veja também

- [[containerd e runc]]
- [[Padrão OCI]]
- [[Build multiplataforma]]
- [[MOC - IA e Novidades]]
