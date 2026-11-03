---
titulo: "Cheat sheet: CMake"
tags: [cpp, referencia, cheat-sheet, cmake, build]
aliases: ["Cheat sheet CMake", "Resumo CMake", "Comandos CMake"]
tipo: referencia
nivel: intermediario
padrao: C++20
criado: 2026-10-24
relacionados: ["[[CMake Moderno e Presets]]", "[[Estrutura de Projetos]]", "[[vcpkg e Conan]]"]
---

# Cheat sheet: CMake

## Linha de comando

```bash
cmake -S . -B build -G Ninja -DCMAKE_BUILD_TYPE=Release   # configurar (source, build dir)
cmake --build build -j                                      # compilar (-j: paralelo)
cmake --build build --target app --config Debug             # alvo e configuração (multi-config)
ctest --test-dir build --output-on-failure -j4              # testes
cmake --install build --prefix /opt/app                     # instalar
cmake --preset release && cmake --build --preset release    # presets
cmake -L build                                              # listar variáveis do cache
cmake -DVAR=valor build                                     # alterar variável
cmake --fresh -S . -B build                                 # reconfigurar do zero (3.24+)
```

## `CMakeLists.txt` completo e comentado

```cmake
cmake_minimum_required(VERSION 3.20)
project(meuapp VERSION 1.2.3 LANGUAGES CXX)

# --- Padrão e opções globais do projeto
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)                       # -std=c++20, não gnu++20
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
option(MEUAPP_TESTS "Compilar testes" ON)

# --- Alvos
add_library(core STATIC src/core.cpp)               # STATIC | SHARED | OBJECT | INTERFACE
add_library(meuapp::core ALIAS core)
target_include_directories(core
    PUBLIC  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
            $<INSTALL_INTERFACE:include>
    PRIVATE src)
target_compile_features(core PUBLIC cxx_std_20)
target_compile_options(core PRIVATE
    $<$<CXX_COMPILER_ID:GNU,Clang,AppleClang>:-Wall -Wextra -Wpedantic>
    $<$<CXX_COMPILER_ID:MSVC>:/W4 /permissive->)
target_compile_definitions(core PUBLIC MEUAPP_VERSION="${PROJECT_VERSION}")

add_executable(app src/main.cpp)
target_link_libraries(app PRIVATE meuapp::core)

# --- Dependências
find_package(Threads REQUIRED)
find_package(fmt CONFIG REQUIRED)                   # via vcpkg/Conan/sistema
target_link_libraries(core PUBLIC fmt::fmt PRIVATE Threads::Threads)

include(FetchContent)                               # baixa no configure
FetchContent_Declare(json URL https://github.com/nlohmann/json/releases/download/v3.11.3/json.tar.xz)
FetchContent_MakeAvailable(json)

# --- Testes
if(MEUAPP_TESTS)
  enable_testing()
  add_subdirectory(tests)
endif()

# --- Instalação
install(TARGETS app core EXPORT meuappTargets)
install(DIRECTORY include/ DESTINATION include)
```

## Palavras-chave de visibilidade

| | Aplica ao próprio alvo | Propaga a quem o liga |
|---|---|---|
| `PRIVATE` | ✅ | ❌ |
| `PUBLIC` | ✅ | ✅ |
| `INTERFACE` | ❌ | ✅ |

## Variáveis e *generator expressions* úteis

| Item | Significado |
|---|---|
| `CMAKE_SOURCE_DIR`, `CMAKE_CURRENT_SOURCE_DIR` | Raiz do projeto / do diretório atual |
| `CMAKE_BINARY_DIR`, `PROJECT_BINARY_DIR` | Diretório de build |
| `CMAKE_BUILD_TYPE` | `Debug`, `Release`, `RelWithDebInfo`, `MinSizeRel` |
| `CMAKE_CXX_COMPILER_ID` | `GNU`, `Clang`, `AppleClang`, `MSVC` |
| `$<CONFIG:Debug>` | Condição por configuração |
| `$<TARGET_FILE:app>` | Caminho do binário |
| `$<BOOL:...>`, `$<IF:cond,a,b>` | Lógica em geração |

> [!warning] Más práticas comuns
> `file(GLOB)` para fontes; `include_directories`/`link_libraries` globais; `-std=` escrito à mão; definir `CMAKE_CXX_FLAGS` no `CMakeLists`; build dentro da pasta de fontes.

> [!question] Verificar na documentação oficial
> Comandos e *policies* evoluem entre versões (CMake 4.x removeu compatibilidades antigas). Consulte cmake.org/cmake/help/latest.

## Veja também

- [[CMake Moderno e Presets]]
- [[Estrutura de Projetos]]
- [[vcpkg e Conan]]
- [[Ninja e Make]]
- [[MOC - Referência - Cpp]]

## Exercício

1. Crie um projeto com biblioteca, executável e teste usando apenas comandos `target_*`.
2. Adicione `option(ENABLE_ASAN ...)` que ativa sanitizers.
