---
titulo: "range-v3 e Abseil"
tags: [cpp, bibliotecas, utilitarios]
aliases: ["range-v3", "Abseil", "absl", "flat_hash_map", "StrCat", "Swiss tables"]
tipo: biblioteca
nivel: intermediario
padrao: C++17
criado: 2026-10-24
relacionados: ["[[Ranges e Views]]", "[[Visão Geral das Bibliotecas]]", "[[unordered_map e unordered_set]]"]
---

# range-v3 e Abseil

## range-v3

Implementação de referência de ranges de Eric Niebler, que serviu de base ao `<ranges>` do C++20. Traz **mais views e ações** do que o padrão (ainda mais depois do C++23) e é útil em compiladores sem suporte completo.

```cpp
// [nv] g++ -std=c++17 -Wall -Wextra   (requer range-v3; indisponível no ambiente de teste do vault)
#include <iostream>
#include <range/v3/all.hpp>
#include <vector>

int main() {
    std::vector<int> v{1, 2, 3, 4, 5, 6};
    auto r = v | ranges::views::filter([](int x) { return x % 2 == 0; })
               | ranges::views::transform([](int x) { return x * x; });
    for (int x : r) std::cout << x << ' ';                          // 4 16 36

    std::vector<int> a{3, 1, 2};
    a |= ranges::actions::sort | ranges::actions::unique;           // ações: modificam o contêiner
    for (int x : ranges::views::zip(a, v) | ranges::views::keys) std::cout << x;
}
```

| range-v3 | Equivalente padrão |
|---|---|
| `views::filter/transform/take` | C++20 `std::views` ([[Ranges e Views]]) |
| `views::zip`, `enumerate`, `chunk`, `slide` | C++23 |
| `actions::sort`, `unique` (ações) | Não há equivalente direto |
| `ranges::to<std::vector>()` | C++23 `std::ranges::to` |

## Abseil (`absl`)

Biblioteca do Google (Apache 2.0) com os componentes comuns do código interno deles.

| Componente | Descrição |
|---|---|
| `absl::flat_hash_map/set` | Tabelas hash *Swiss table*, mais rápidas e compactas que `std::unordered_map` (sem estabilidade de ponteiros) |
| `absl::StrCat`, `StrFormat`, `StrSplit`, `StrJoin` | Utilitários de texto |
| `absl::Status`, `StatusOr<T>` | Tratamento de erros sem exceções (parecido com `std::expected`) |
| `absl::Span`, `string_view`, `optional` | Tipos de vocabulário (hoje já na STL) |
| `absl::Time`, `Duration` | Tempo e fuso horário |
| `absl::Mutex` | Mutex com anotações para análise de threads |
| `absl::Cleanup`, `CHECK`, `log` | Utilitários e logging |

```cpp
// [nv] g++ -std=c++20 -Wall -Wextra -labsl_strings -labsl_hash   (requer Abseil; indisponível no ambiente de teste do vault)
#include <absl/container/flat_hash_map.h>
#include <absl/strings/str_cat.h>
#include <absl/strings/str_split.h>
#include <iostream>
#include <string>
#include <vector>

int main() {
    absl::flat_hash_map<std::string, int> contagem;
    for (std::string_view p : absl::StrSplit("a b a c b a", ' ')) ++contagem[std::string(p)];
    std::cout << absl::StrCat("a=", contagem["a"], " b=", contagem["b"]) << '\n';   // a=3 b=2
}
```

> [!warning] Abseil e ABI
> Abseil **não garante estabilidade de ABI** entre versões; compile tudo junto (via vcpkg/Conan ou CMake) e evite misturar versões ([[ABI]]).

## Veja também

- [[Ranges e Views]]
- [[unordered_map e unordered_set]]
- [[Tratamento de Erros com expected]]
- [[Visão Geral das Bibliotecas]]

## Exercício

1. Compare o tempo de inserção em `std::unordered_map` e `absl::flat_hash_map` para 10⁶ chaves.
2. Reescreva um pipeline de range-v3 usando apenas `std::ranges` (C++23).
