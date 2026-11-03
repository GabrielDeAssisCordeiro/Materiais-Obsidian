---
titulo: "Pré-processador e macros"
tags: [cpp, organizacao, preprocessador, macros]
aliases: ["Pré-processador", "#define", "#include", "#if", "__has_include"]
tipo: conceito
nivel: iniciante
padrao: C++98
criado: 2026-10-24
relacionados: ["[[Include Guards e pragma once]]", "[[Pipeline de Compilação - Cpp]]", "[[const e constexpr]]"]
---

# Pré-processador e macros

O pré-processador é a **primeira fase** da compilação ([[Pipeline de Compilação - Cpp]]): trabalha com **texto**, antes do compilador entender tipos. Diretivas começam com `#`.

| Diretiva | Função |
|---|---|
| `#include` | Copia o conteúdo de outro arquivo |
| `#define` / `#undef` | Define/remove macro |
| `#if`, `#ifdef`, `#ifndef`, `#elif`, `#else`, `#endif` | Compilação condicional |
| `#error`, `#warning` (C++23) | Mensagem na compilação |
| `#pragma` | Instruções específicas do compilador |
| `#embed` (C++26) | Incorpora bytes de arquivo |

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>

#define VERSAO 3
#define QUADRADO_RUIM(x) x * x                  // BUG: sem parênteses
#define QUADRADO(x) ((x) * (x))                 // melhor, ainda avalia x duas vezes

#if defined(__GNUC__) || defined(__clang__)
#define COMPILADOR "GCC/Clang"
#elif defined(_MSC_VER)
#define COMPILADOR "MSVC"
#else
#define COMPILADOR "outro"
#endif

#if __has_include(<optional>)
#include <optional>
#endif

int main() {
    std::cout << COMPILADOR << ' ' << VERSAO << ' ' << __cplusplus << '\n';   // 202002 com -std=c++20
    std::cout << QUADRADO_RUIM(1 + 2) << ' ' << QUADRADO(1 + 2) << '\n';       // 5 9
    std::cout << __FILE__ << ':' << __LINE__ << '\n';
}
```

> [!bug] Macros não respeitam escopo nem tipos
> `QUADRADO_RUIM(1 + 2)` vira `1 + 2 * 1 + 2` = 5. `QUADRADO(i++)` incrementa duas vezes. Macros também vazam entre headers e ignoram namespaces (`min`/`max` do `<windows.h>` quebram `std::max`).

## Alternativas em C++ moderno

| Em vez de | Use |
|---|---|
| `#define N 10` | `constexpr int N = 10;` ([[const e constexpr]]) |
| Macro de função | `inline`/`constexpr`/template ([[Templates de Função]]) |
| `#ifdef` por recurso | `if constexpr`, `__has_include`, [[Concepts e requires]] |
| `__FILE__`/`__LINE__` | `std::source_location` (C++20) |
| `assert` customizado | `static_assert`, contratos ([[Asserts e Contratos]]) |

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <source_location>

void log(const char* msg, std::source_location loc = std::source_location::current()) {
    std::cout << loc.file_name() << ':' << loc.line() << " [" << loc.function_name() << "] " << msg << '\n';
}

int main() { log("olá"); }
```

## Macros ainda úteis

- Include guards e `#pragma once`.
- Detecção de plataforma/compilador/recurso: `__cplusplus`, `_MSC_VER`, `__cpp_concepts` (macros de teste de recursos em `<version>`).
- Exportação de símbolos de bibliotecas (`EXPORT_API`).
- Stringificação `#x` e concatenação `a##b` (X-macros).

> [!tip] Convenções
> Macros em `MAIÚSCULAS_COM_PREFIXO_DO_PROJETO` para evitar colisões. Documente-as e use `#undef` para macros temporárias.

## Veja também

- [[Include Guards e pragma once]]
- [[Pipeline de Compilação - Cpp]]
- [[const e constexpr]]
- [[Flags Essenciais do Compilador]]

## Exercício

1. Escreva `MAX(a, b)` como macro, mostre o bug com efeitos colaterais e substitua por função `constexpr`.
2. Use `g++ -E` para ver o resultado do pré-processamento do exemplo.
