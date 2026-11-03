---
titulo: "MOC — Build e Ferramentas"
tags: [cpp, moc, build, ferramentas]
aliases: ["MOC Build e Ferramentas", "Build e Ferramentas"]
tipo: moc
nivel: intermediario
padrao: C++20
criado: 2026-10-24
relacionados: ["[[Home - Cpp]]", "[[MOC - Módulos e Organização]]", "[[MOC - Testes e Qualidade - Cpp]]"]
---

# MOC — Build e Ferramentas

```mermaid
flowchart LR
    SRC[Código] --> CM[CMake / Meson / Bazel]
    CM --> NJ[Ninja / Make]
    NJ --> CC[ccache]
    DEP[vcpkg / Conan] --> CM
    NJ --> BIN[Binário]
    BIN --> DBG[GDB / LLDB]
    BIN --> SAN[Sanitizers / Valgrind]
    SRC --> LINT[clang-tidy / cppcheck / clang-format]
    CM --> CROSS[Cross-compilation]
```

## Sistemas de build e dependências

- [[CMake Moderno e Presets]]
- [[Ninja e Make]]
- [[Meson e Bazel]]
- [[vcpkg e Conan]]
- [[ccache]]
- [[Cross-compilation]]

## Depuração e análise

- [[Depuração com GDB LLDB e Visual Studio]]
- [[Sanitizers]]
- [[Valgrind]]
- [[clang-tidy e cppcheck]]
- [[clang-format]]
- [[Compiler Explorer]]

## Ordem sugerida

[[Ninja e Make]] → [[CMake Moderno e Presets]] → [[vcpkg e Conan]] → [[Depuração com GDB LLDB e Visual Studio]] → [[Sanitizers]] → [[Valgrind]] → [[clang-format]] → [[clang-tidy e cppcheck]] → [[ccache]] → [[Compiler Explorer]] → [[Cross-compilation]] → [[Meson e Bazel]]

## Veja também

- [[Home - Cpp]]
- [[MOC - Módulos e Organização]]
- [[MOC - Testes e Qualidade - Cpp]]
- [[Flags Essenciais do Compilador]]
