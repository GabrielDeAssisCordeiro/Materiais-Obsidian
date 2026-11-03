---
titulo: "vcpkg e Conan"
tags: [cpp, build, dependencias]
aliases: ["vcpkg", "Conan", "Gerenciador de pacotes", "vcpkg.json", "conanfile.txt"]
tipo: ferramenta
nivel: intermediario
padrao: C++17
criado: 2026-10-24
relacionados: ["[[CMake Moderno e Presets]]", "[[Bibliotecas Estáticas e Dinâmicas]]", "[[Visão Geral das Bibliotecas]]"]
---

# vcpkg e Conan

O C++ não tem gerenciador de pacotes oficial. Os dois mais usados:

| | **vcpkg** (Microsoft) | **Conan** (JFrog) |
|---|---|---|
| Modelo | Catálogo único (*ports*) compilados do código-fonte | Receitas + binários pré-compilados em remotos |
| Arquivo | `vcpkg.json` (manifest) | `conanfile.txt` / `conanfile.py` |
| Integração CMake | `CMAKE_TOOLCHAIN_FILE` | `conan_toolchain.cmake` + `CMakeDeps` |
| Pontos fortes | Simplicidade, versionamento por *baseline* | Flexibilidade, binários, repositórios privados |
| Escrito em | C++/CMake | Python |

## vcpkg (modo manifesto)

```json
{
  "name": "demo",
  "version": "1.0.0",
  "dependencies": ["fmt", "spdlog", { "name": "gtest", "host": false }],
  "builtin-baseline": "<hash-do-commit-do-vcpkg>"
}
```

```bash
git clone https://github.com/microsoft/vcpkg && ./vcpkg/bootstrap-vcpkg.sh
cmake -S . -B build -DCMAKE_TOOLCHAIN_FILE=$PWD/vcpkg/scripts/buildsystems/vcpkg.cmake
cmake --build build
```

```cmake
find_package(fmt CONFIG REQUIRED)
target_link_libraries(app PRIVATE fmt::fmt)
```

## Conan 2

```ini
# conanfile.txt
[requires]
fmt/11.0.2
spdlog/1.14.1

[generators]
CMakeDeps
CMakeToolchain

[layout]
cmake_layout
```

```bash
conan profile detect
conan install . --output-folder=build --build=missing
cmake -S . -B build -DCMAKE_TOOLCHAIN_FILE=build/conan_toolchain.cmake -DCMAKE_BUILD_TYPE=Release
cmake --build build
```

> [!tip] Reprodutibilidade
> Fixe versões: *baseline* no vcpkg, *lockfiles* no Conan (`conan lock create`). Registre a versão do compilador e da biblioteca padrão na CI.

> [!warning] Armadilhas
> - Misturar bibliotecas compiladas com **ABIs diferentes** (`libstdc++` vs `libc++`, Debug/Release do MSVC) — veja [[ABI]].
> - Alternativas leves: **FetchContent** (CMake), `git submodule`, **CPM.cmake**, Meson WrapDB.
> - Versões e *triplets* mudam com frequência: confira as docs oficiais.

## Veja também

- [[CMake Moderno e Presets]]
- [[Bibliotecas Estáticas e Dinâmicas]]
- [[ABI]]
- [[Visão Geral das Bibliotecas]]

## Exercício

1. Adicione `fmt` a um projeto via vcpkg e depois via Conan; compare os passos.
2. Gere um *lockfile* e explique o que ele garante.
