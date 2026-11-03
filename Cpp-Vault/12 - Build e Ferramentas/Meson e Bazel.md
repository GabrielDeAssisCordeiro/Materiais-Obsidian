---
titulo: "Meson e Bazel (introdução)"
tags: [cpp, build]
aliases: ["Meson", "meson.build", "Bazel", "BUILD.bazel", "Alternativas ao CMake", "Buck2", "xmake"]
tipo: ferramenta
nivel: intermediario
padrao: C++17
criado: 2026-10-24
relacionados: ["[[CMake Moderno e Presets]]", "[[Ninja e Make]]", "[[vcpkg e Conan]]"]
---

# Meson e Bazel (introdução)

Alternativas ao CMake com filosofias diferentes.

| | **CMake** | **Meson** | **Bazel** |
|---|---|---|---|
| Linguagem de configuração | Própria (verbosa) | Python-like, declarativa | Starlark (subconjunto de Python) |
| Backend | Ninja, Make, MSBuild, Xcode | Ninja (e VS/Xcode) | Próprio (sandbox, cache remoto) |
| Ponto forte | Ecossistema enorme | Simplicidade e velocidade | **Builds hermeticos e escaláveis** (monorepos) |
| Dependências | `find_package`, FetchContent, vcpkg/Conan | `subprojects/`, WrapDB, pkg-config | `MODULE.bazel` (bzlmod), regras |
| Quem usa | A maioria do ecossistema | GNOME, Mesa, systemd | Google, TensorFlow, monorepos grandes |

## Meson

```meson
# meson.build
project('demo', 'cpp', version : '1.0', default_options : ['cpp_std=c++20', 'warning_level=3'])

core = static_library('core', 'src/core.cpp', include_directories : include_directories('include'))
exe  = executable('app', 'src/main.cpp', link_with : core)
test('smoke', exe)
```

```bash
meson setup build --buildtype=release
meson compile -C build
meson test -C build
```

## Bazel

```python
# BUILD.bazel
cc_library(
    name = "core",
    srcs = ["src/core.cpp"],
    hdrs = ["include/core.hpp"],
    includes = ["include"],
)

cc_binary(
    name = "app",
    srcs = ["src/main.cpp"],
    deps = [":core"],
)
```

```bash
bazel build //:app --cxxopt=-std=c++20
bazel test //...
bazel run //:app
```

> [!info] Quando considerar
> - **Meson**: projeto novo, equipe que quer menos boilerplate e bom suporte a *cross-compilation*.
> - **Bazel**: monorepo grande, múltiplas linguagens, necessidade de **builds reproduzíveis** e **cache remoto**. Curva de aprendizado maior.
> - **CMake**: o padrão quando se consome bibliotecas de terceiros.

> [!question] Verificar na documentação oficial
> Versões e sintaxe mudam (por exemplo, `WORKSPACE` foi substituído por `MODULE.bazel` no Bazel moderno). Consulte mesonbuild.com e bazel.build.

## Veja também

- [[CMake Moderno e Presets]]
- [[Ninja e Make]]
- [[vcpkg e Conan]]
- [[Cross-compilation]]

## Exercício

1. Porte o projeto do exercício do CMake para Meson e compare as linhas de configuração.
2. Descreva em um parágrafo por que *hermeticidade* importa em um monorepo.
