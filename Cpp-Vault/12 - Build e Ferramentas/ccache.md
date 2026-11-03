---
titulo: "ccache e redução do tempo de compilação"
tags: [cpp, build, cache, compilacao, desempenho]
aliases: ["ccache", "sccache", "Cache de compilação", "Precompiled headers", "Unity build", "Tempo de compilação"]
tipo: ferramenta
nivel: intermediario
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Ninja e Make]]", "[[CMake Moderno e Presets]]", "[[Headers vs Sources]]"]
---

# ccache e redução do tempo de compilação

**ccache** guarda o resultado de cada compilação indexado por um *hash* do código pré-processado + flags + versão do compilador. Se a mesma entrada reaparecer (outro *branch*, `make clean`, CI), devolve o `.o` instantaneamente.

```bash
sudo apt install ccache
ccache -s                       # estatísticas (hit rate)
ccache -M 20G                   # tamanho máximo do cache
ccache -C                       # limpar
```

```cmake
# Ative via launcher (CMake 3.4+)
find_program(CCACHE ccache)
if(CCACHE)
  set(CMAKE_CXX_COMPILER_LAUNCHER ${CCACHE})
endif()
```

```bash
# Alternativa por linha de comando
cmake -S . -B build -DCMAKE_CXX_COMPILER_LAUNCHER=ccache
```

| Alternativa | Observação |
|---|---|
| **sccache** | Mozilla; cache local ou remoto (S3/GCS), suporta MSVC e Rust |
| **Cache remoto do Bazel/BuildBuddy** | Em monorepos |
| **distcc / icecream** | Distribuem a compilação entre máquinas |

## Outras formas de compilar mais rápido

| Técnica | Efeito |
|---|---|
| Ninja + `-j` | Paralelismo máximo |
| **Forward declarations** ([[Forward Declarations]]) | Menos `#include` |
| **Precompiled headers** (`target_precompile_headers`) | Pré-compila headers estáveis (`<vector>`, `<string>`) |
| **Unity builds** (`UNITY_BUILD ON`) | Junta vários `.cpp` em um (cuidado com colisões de nomes) |
| **Módulos C++20** ([[Módulos Cpp20]]) | Evita reprocessar headers |
| Menos templates pesados em headers | Mova implementações para `.cpp` ou use `extern template` |
| Linker rápido (`lld`, `mold`) | Tempo de link menor |
| `-O0`/`-Og` em desenvolvimento | Compilação mais rápida |
| **Pimpl** | Isola mudanças de implementação |

```cmake
target_precompile_headers(core PRIVATE <vector> <string> <map>)
set_target_properties(core PROPERTIES UNITY_BUILD ON)
add_link_options(-fuse-ld=lld)      # ou -fuse-ld=mold
```

> [!tip] Meça antes
> `cmake --build build -- -d stats` (Ninja) ou `clang -ftime-trace` mostram onde o tempo vai (use o Perfetto/Chrome tracing para visualizar). **ClangBuildAnalyzer** agrega por header.

> [!warning] Armadilhas do ccache
> - Resultados dependem de caminhos absolutos e macros como `__DATE__`/`__TIME__` (inibem *hits*).
> - Para MSVC, o suporte tem limitações (prefira sccache ou configuração específica).

## Veja também

- [[Ninja e Make]]
- [[CMake Moderno e Presets]]
- [[Forward Declarations]]
- [[Módulos Cpp20]]

## Exercício

1. Meça o tempo de um build limpo com e sem ccache (segundo build).
2. Use `-ftime-trace` e descubra qual header mais custa em um projeto seu.
