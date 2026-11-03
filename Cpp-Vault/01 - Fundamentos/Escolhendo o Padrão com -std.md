---
titulo: "Escolhendo o padrão com -std"
tags: [cpp, fundamentos, std, padroes]
aliases: ["-std=c++20", "Escolher padrão C++", "__cplusplus", "Feature test macros"]
tipo: referencia
nivel: iniciante
padrao: C++11
criado: 2026-10-24
relacionados: ["[[História e Evolução dos Padrões]]", "[[Flags Essenciais do Compilador]]", "[[Suporte dos Compiladores aos Padrões]]"]
---

# Escolhendo o padrão com `-std`

## Flags por padrão

| Padrão | GCC / Clang | MSVC |
|---|---|---|
| C++11 | `-std=c++11` | (mínimo suportado é C++14) |
| C++14 | `-std=c++14` | `/std:c++14` (padrão do MSVC) |
| C++17 | `-std=c++17` | `/std:c++17` |
| C++20 | `-std=c++20` | `/std:c++20` |
| C++23 | `-std=c++23` (versões antigas: `-std=c++2b`) | `/std:c++latest` (ou flag específica em versões recentes) |
| C++26 | `-std=c++26` (versões antigas: `-std=c++2c`) | `/std:c++latest` |

Variante **`gnu++20`** etc.: o mesmo padrão **com extensões GNU**. Use `c++20` (sem `gnu`) para código portável.

> [!question] Verificar na documentação oficial
> A partir de qual versão cada compilador aceita `-std=c++23` e `-std=c++26` (em vez de `c++2b`/`c++2c`) e quais flags o MSVC usa para C++23/26 variam. Consulte a documentação do seu compilador.

## Padrão default de cada compilador

| Compilador | Default |
|---|---|
| GCC 11 a 15 | `gnu++17` |
| GCC 16 | `gnu++20` (mudança no 16.1) |
| Clang 16 em diante | `gnu++17` |
| MSVC | C++14 |

> [!warning] Nunca dependa do default
> Especifique `-std` explicitamente no build (por exemplo, `CMAKE_CXX_STANDARD`), para que o projeto compile igual em qualquer máquina.

## Qual padrão usar?

- **Projeto novo:** C++20 ou C++23, se seus compiladores-alvo suportam os recursos que você usa.
- **Código legado:** o mais novo que a base de código e as dependências permitirem; migre gradualmente.
- **Bibliotecas públicas:** mínimo comum entre seus consumidores (muitas bibliotecas exigem C++17).

## Detectando o padrão e recursos no código

`__cplusplus` informa o padrão; **macros de teste de recurso** (cabeçalho `<version>`) informam recursos específicos.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <version>   // macros __cpp_lib_* (C++20)

int main() {
    std::cout << "__cplusplus = " << __cplusplus << '\n';
    // 199711L C++98 | 201103L C++11 | 201402L C++14
    // 201703L C++17 | 202002L C++20 | 202302L C++23

#ifdef __cpp_concepts
    std::cout << "concepts: " << __cpp_concepts << '\n';
#else
    std::cout << "sem concepts\n";
#endif

#ifdef __cpp_lib_ranges
    std::cout << "ranges: " << __cpp_lib_ranges << '\n';
#else
    std::cout << "sem ranges\n";
#endif
}
```

> [!warning] MSVC e `__cplusplus`
> O MSVC só reporta o valor correto de `__cplusplus` com `/Zc:__cplusplus`. Alternativamente, use `_MSVC_LANG`.

## Veja também

- [[História e Evolução dos Padrões]]
- [[Flags Essenciais do Compilador]]
- [[Suporte dos Compiladores aos Padrões]]
- [[Cpp26 Visão Geral]]

## Exercício

1. Compile o programa com `-std=c++17` e com `-std=c++20` e compare as saídas.
2. Descubra o padrão default do seu compilador sem passar `-std`.
