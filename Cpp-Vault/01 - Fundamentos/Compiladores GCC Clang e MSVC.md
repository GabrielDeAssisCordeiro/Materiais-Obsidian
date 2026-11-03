---
titulo: "Compiladores: GCC, Clang e MSVC"
tags: [cpp, fundamentos, compiladores, gcc, clang, msvc]
aliases: ["GCC", "Clang", "MSVC", "Compiladores C++"]
tipo: ferramenta
nivel: iniciante
padrao: C++98
criado: 2026-10-24
relacionados: ["[[Suporte dos Compiladores aos Padrões]]", "[[Flags Essenciais do Compilador]]", "[[Pipeline de Compilação - Cpp]]"]
---

# Compiladores: GCC, Clang e MSVC

## Os três principais

| Compilador | Mantenedor | Sistemas | Driver | Biblioteca padrão |
|---|---|---|---|---|
| **GCC** (GNU Compiler Collection) | Projeto GNU | Linux, BSD, Windows (MinGW/MSYS2), macOS | `g++` | libstdc++ |
| **Clang** (LLVM) | Projeto LLVM | Linux, macOS, Windows, BSD | `clang++` | libc++ ou libstdc++ |
| **MSVC** | Microsoft | Windows | `cl.exe` | MS STL |

Outros: **Apple Clang** (Xcode), **Intel oneAPI DPC++/C++** (baseado em Clang), **NVIDIA nvcc** (CUDA), **clang-cl** (Clang com interface do MSVC).

## Versões de referência (consulta em 24/10/2026)

| Compilador | Versão recente identificada | Observações |
|---|---|---|
| GCC | **16.1** (30/04/2026) | Padrão default passou de `gnu++17` para `gnu++20`; reflexão C++26 com `-std=c++26 -freflection`; módulos ainda experimentais (`-fmodules`) |
| Clang | Verificar em releases.llvm.org | Reflexão C++26 apenas em forks experimentais (`-freflection-latest`) |
| MSVC | Build Tools 14.51 citado pela cppreference (04/2026) | Consulte a documentação "Microsoft C/C++ language conformance" |

> [!question] Verificar na documentação oficial
> Números de versão mudam com frequência. Confirme em gcc.gnu.org, releases.llvm.org e learn.microsoft.com antes de fixar uma versão em um projeto.

## Qual escolher?

- Para **aprender**: o que já vem no seu sistema (GCC no Linux, Clang no macOS, MSVC no Windows).
- Para **portabilidade**: compile com pelo menos dois compiladores (cada um aponta erros diferentes) — ideal em integração contínua (CI). Veja [[Suporte dos Compiladores aos Padrões]].
- Para **mensagens de erro**: Clang costuma ser considerado claro; GCC melhorou muito nas últimas versões.

## Biblioteca padrão e compilador são coisas diferentes

O compilador entende a **linguagem**; a **biblioteca padrão** (`std::vector`, `std::format`...) é implementada à parte. Um recurso pode estar disponível no compilador, mas ausente na biblioteca instalada. Por isso o suporte é descrito por **dois eixos**: núcleo da linguagem e biblioteca.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>

int main() {
    // Macros predefinidas que identificam o compilador
#if defined(__clang__)
    std::cout << "Clang " << __clang_major__ << '\n';
#elif defined(__GNUC__)
    std::cout << "GCC " << __GNUC__ << '.' << __GNUC_MINOR__ << '\n';
#elif defined(_MSC_VER)
    std::cout << "MSVC " << _MSC_VER << '\n';
#else
    std::cout << "Compilador desconhecido\n";
#endif
}
```

> [!warning] Clang também define `__GNUC__`
> Teste `__clang__` **antes** de `__GNUC__`, como no exemplo.

## Compiler Explorer

O site godbolt.org (Compiler Explorer) permite testar código em dezenas de compiladores e versões e ver o assembly gerado — útil para checar suporte de recursos sem instalar nada.

## Veja também

- [[Suporte dos Compiladores aos Padrões]]
- [[Flags Essenciais do Compilador]]
- [[Escolhendo o Padrão com -std]]
- [[Pipeline de Compilação - Cpp]]
- [[Instalação no Linux - Cpp]]

## Exercício

1. Compile o exemplo acima com `g++` e com `clang++` (se tiver os dois). Qual saída aparece em cada um?
2. Descubra qual biblioteca padrão seu `clang++` usa (`clang++ -dM -E -x c++ /dev/null | grep -i version` ou `-stdlib=`).
