---
titulo: "Instalação no macOS - Cpp"
tags: [cpp, fundamentos, instalacao, macos]
aliases: ["Instalar C++ no macOS", "Setup macOS"]
tipo: procedimento
nivel: iniciante
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Instalação no Linux - Cpp]]", "[[Instalação no Windows]]", "[[IDEs e Editores]]"]
---

# Instalação no macOS - Cpp

## Ferramentas de linha de comando (Apple Clang)

```bash
xcode-select --install
```

Isso instala o **Apple Clang** e a biblioteca **libc++**. Atenção: no macOS, o comando `g++` costuma ser **apenas um atalho para o Clang**.

```bash
g++ --version        # mostra "Apple clang version ..." no macOS
```

## Homebrew: GCC, LLVM, CMake e Ninja

Instale o Homebrew (brew.sh) e então:

```bash
brew install cmake ninja llvm gcc gdb
```

| Pacote | O que fornece |
|---|---|
| `llvm` | Clang/LLVM oficial (mais novo que o da Apple), `clang-tidy`, `clang-format` |
| `gcc` | GCC de verdade, com binários numerados como `g++-NN` |
| `cmake`, `ninja` | Sistema de build |
| `gdb` | Em Macs recentes, o **LLDB** (já incluído) costuma ser a escolha |

> [!warning] Caminho do compilador
> O `llvm` do Homebrew não substitui o Clang da Apple automaticamente. Use o caminho completo (`$(brew --prefix llvm)/bin/clang++`) ou ajuste o `PATH`.

> [!question] Verificar na documentação oficial
> Detalhes de pacotes (por exemplo, disponibilidade do `gdb` em Apple Silicon) mudam; consulte a documentação do Homebrew.

## Compilando

```bash
clang++ -std=c++20 -Wall -Wextra ola.cpp -o ola && ./ola
```

## Depuração

Use o **LLDB** (`lldb ./ola`) ou o Xcode. Os sanitizers (ASan, UBSan) funcionam bem no Apple Clang.

## Veja também

- [[Instalação no Linux - Cpp]]
- [[Instalação no Windows]]
- [[IDEs e Editores]]
- [[Compiladores GCC Clang e MSVC]]

## Exercício

1. Rode `g++ --version` e `clang++ --version`. Eles são o mesmo programa no seu Mac?
2. Instale o `llvm` pelo Homebrew e compare as versões do Clang.
