---
titulo: "Estrutura de projetos"
tags: [cpp, organizacao, projeto, cmake]
aliases: ["Estrutura de projetos", "src include tests"]
tipo: conceito
nivel: intermediario
padrao: C++17
criado: 2026-10-24
relacionados: ["[[Headers vs Sources]]", "[[Bibliotecas Estáticas e Dinâmicas]]"]
---

# Estrutura de projetos

Não há layout oficial, mas há convenções amplamente usadas (inspiradas no *Pitchfork Layout*):

```text
meu_projeto/
├── CMakeLists.txt
├── CMakePresets.json
├── include/
│   └── meuproj/          # headers PÚBLICOS (namespace de diretório)
│       └── calculadora.hpp
├── src/                  # implementação e headers PRIVADOS
│   ├── calculadora.cpp
│   └── main.cpp
├── tests/
│   ├── CMakeLists.txt
│   └── calculadora_test.cpp
├── examples/
├── docs/
├── third_party/          # ou gerenciador: vcpkg.json / conanfile.txt
├── .clang-format
├── .clang-tidy
└── README.md
```

## Princípios

1. **Separe interface pública e privada**: só `include/meuproj/` é instalado; o que está em `src/` é detalhe.
2. **Prefixe includes com o nome do projeto** (`#include <meuproj/calculadora.hpp>`) para evitar colisão.
3. **Uma biblioteca + executável fino**: lógica em `libmeuproj`, `main.cpp` só chama. Facilita testes.
4. **Build fora da árvore** (`cmake -S . -B build`): o repositório fica limpo.
5. **Dependências declaradas** (vcpkg/Conan/FetchContent), não copiadas.
6. **Testes e ferramentas** (format, tidy, sanitizers) integrados desde o início.

```cmake
# CMakeLists.txt (raiz)
cmake_minimum_required(VERSION 3.20)
project(meuproj VERSION 1.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

add_library(meuproj src/calculadora.cpp)
target_include_directories(meuproj PUBLIC include)
target_compile_options(meuproj PRIVATE -Wall -Wextra)

add_executable(app src/main.cpp)
target_link_libraries(app PRIVATE meuproj)

enable_testing()
add_subdirectory(tests)
```

```bash
cmake -S . -B build -G Ninja -DCMAKE_BUILD_TYPE=Release
cmake --build build
ctest --test-dir build
```

> [!tip] Convenções de código
> Nomes de arquivos consistentes (`snake_case.hpp` ou `PascalCase.hpp`), um tipo principal por header, e `#pragma once` ou guards ([[Include Guards e pragma once]]).

> [!info] Mais detalhes
> Para CMake em profundidade (alvos, `PUBLIC/PRIVATE`, presets) veja a seção Build e Ferramentas.

## Veja também

- [[Headers vs Sources]]
- [[Bibliotecas Estáticas e Dinâmicas]]
- [[Módulos Cpp20]]
- [[Flags Essenciais do Compilador]]

## Exercício

1. Crie o esqueleto acima, compile com Ninja e rode `ctest` com um teste simples.
2. Adicione `.clang-format` e formate o projeto.
