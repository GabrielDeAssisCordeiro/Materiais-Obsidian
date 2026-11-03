---
titulo: "Suporte dos compiladores aos padrões"
tags: [cpp, fundamentos, compiladores]
aliases: ["Compiler support", "Suporte a recursos C++", "Tabela de suporte"]
tipo: referencia
nivel: intermediario
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Compiladores GCC Clang e MSVC]]", "[[Escolhendo o Padrão com -std]]", "[[Cpp26 Visão Geral]]"]
---

# Suporte dos compiladores aos padrões

> [!question] Verificar na documentação oficial
> Esta tabela é **aproximada** e serve como mapa. A fonte de verdade é a página *C++ compiler support* da cppreference (`en.cppreference.com/w/cpp/compiler_support`) e as páginas de status de cada compilador (`gcc.gnu.org/projects/cxx-status.html`, `clang.llvm.org/cxx_status.html`, documentação de conformidade do MSVC). Atualizado pela última vez em 24/10/2026.

## Núcleo da linguagem

| Padrão | GCC | Clang | MSVC |
|---|---|---|---|
| C++11 | completo desde 4.8.1 | completo desde 3.3 | amplo desde VS 2015 |
| C++14 | completo desde 5 | completo desde 3.4 | VS 2015 Update 3 / 2017 |
| C++17 | amplo desde 7 | amplo desde 5 | amplo desde VS 2017 15.7+ |
| C++20 | amplo (≈ 10 a 11+) | amplo, com ressalvas históricas | amplo (VS 2019 16.11 / 2022) |
| C++23 | em grande parte (≈ 13 a 14+) | em grande parte (≈ 17 em diante) | em grande parte (VS 2022 17.x) |
| C++26 | parcial (GCC 16: reflexão, contratos, expansion statements) | parcial; reflexão só em forks | parcial |

## Recursos de destaque

| Recurso | Padrão | Observação de suporte |
|---|---|---|
| Concepts | C++20 | Amplamente suportado em GCC 10+, Clang 10+, MSVC 2019 16.3+ |
| Ranges | C++20 | Biblioteca completa depende da versão da libstdc++/libc++/MS STL (verificar) |
| Corrotinas | C++20 | GCC 10+ (`-fcoroutines`; default em `-std=c++20` a partir do GCC 11), Clang, MSVC 16.8+ |
| Módulos | C++20 | Suporte parcial e **experimental no GCC** (flag `-fmodules`); Clang e MSVC mais avançados; exigem suporte do sistema de build (CMake + Ninja) |
| `import std;` | C++23 | Requer toolchain recente e CMake; suporte desigual |
| `std::format` | C++20 | GCC 13+, MSVC 16.10+, libc++ (completo em versões mais novas) |
| `std::print` | C++23 | GCC 14+, MSVC 17.7+, libc++ 18+ |
| `std::expected` | C++23 | GCC 12+, MSVC 17.3+, libc++ 16+ |
| `std::flat_map` | C++23 | Versões recentes de cada biblioteca (verificar) |
| Reflexão | C++26 | GCC 16.1+ (`-freflection`); Clang em forks |

> [!tip] Como verificar sem instalar
> Use o Compiler Explorer (godbolt.org): escolha o compilador/versão, passe `-std=c++XX` e compile um trecho mínimo. Para testar recursos em tempo de compilação use as macros `__cpp_*` e `__cpp_lib_*` ([[Escolhendo o Padrão com -std]]).

## Estratégia prática

1. Defina o **padrão mínimo** do projeto e os compiladores-alvo.
2. Teste em CI com pelo menos GCC e Clang (e MSVC se for portável para Windows).
3. Para recursos recentes, proteja com macros de teste de recurso ou *fallbacks*.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <version>

int main() {
#if defined(__cpp_lib_format)
    std::cout << "std::format disponível (" << __cpp_lib_format << ")\n";
#else
    std::cout << "std::format indisponível nesta toolchain\n";
#endif
#if defined(__cpp_lib_expected)
    std::cout << "std::expected disponível\n";
#else
    std::cout << "std::expected indisponível\n";
#endif
}
```

## Veja também

- [[Compiladores GCC Clang e MSVC]]
- [[Escolhendo o Padrão com -std]]
- [[Cpp26 Visão Geral]]
- [[História e Evolução dos Padrões]]

## Exercício

1. Compile o exemplo com `g++` e `clang++`. As respostas são iguais? O que isso revela sobre biblioteca vs compilador?
2. No Compiler Explorer, descubra a primeira versão do GCC em que `#include <print>` compila com `-std=c++23`.
