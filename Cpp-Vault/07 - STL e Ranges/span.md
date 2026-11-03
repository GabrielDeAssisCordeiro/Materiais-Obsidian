---
titulo: "std::span"
tags: [cpp, stl, views, cpp20]
aliases: ["std::span", "span", "Visão contígua", "Extent dinâmico", "as_bytes"]
tipo: conceito
nivel: intermediario
padrao: C++20
criado: 2026-10-24
relacionados: ["[[vector]]", "[[Arrays e std array]]", "[[string_view]]"]
---

# `std::span`

> [!info] Introdução
> **C++20** (`<span>`). Suporte: GCC 10+, Clang 7+ (libc++ 7+), MSVC 2019 16.6+.

`std::span<T>` é uma **visão não-possuidora** de uma sequência **contígua** de `T` (ponteiro + tamanho). Substitui o par `(T* p, size_t n)` e funciona com arrays C, `std::array`, `std::vector` etc.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <array>
#include <iostream>
#include <numeric>
#include <span>
#include <vector>

double media(std::span<const double> dados) {              // aceita qualquer contêiner contíguo
    if (dados.empty()) return 0;
    return std::accumulate(dados.begin(), dados.end(), 0.0) / dados.size();
}

void zera(std::span<int> v) { for (int& x : v) x = 0; }    // span mutável

int main() {
    std::vector<double> v{1, 2, 3, 4};
    std::array<double, 3> a{10, 20, 30};
    double c[] = {5, 5};

    std::cout << media(v) << ' ' << media(a) << ' ' << media(c) << '\n';   // 2.5 20 5

    std::vector<int> n{1, 2, 3, 4, 5};
    std::span<int> s{n};
    auto meio = s.subspan(1, 3);                            // {2, 3, 4}: sem cópia
    zera(meio);
    for (int x : n) std::cout << x << ' ';                  // 1 0 0 0 5
    std::cout << '\n';
    std::cout << s.first(2).size() << s.last(2).size() << '\n';   // 22
}
```

## Dois tipos de *extent*

| Declaração | Tamanho |
|---|---|
| `std::span<int>` | Dinâmico (guardado em tempo de execução) |
| `std::span<int, 4>` | Fixo, conhecido em compilação (não guarda tamanho) |

## Quando usar

- **Parâmetros de função** que só leem/escrevem uma sequência contígua: `span<const T>` (somente leitura) ou `span<T>`.
- Dividir buffers em partes (`first`, `last`, `subspan`) sem cópias.
- Substituir `T*, size_t` em APIs, ganhando segurança e expressividade.

> [!danger] `span` não possui os dados (dangling)
> ```cpp
> std::span<int> f() {
>     std::vector<int> v{1, 2, 3};
>     return v;              // span aponta para v, que morre ao sair: PENDENTE
> }
> ```
> Também invalida se o contêiner **realocar** (`push_back`). Trate `span` como um ponteiro: vida do dado é sua responsabilidade.

> [!warning] `operator[]` não verifica limites
> Acesso fora do intervalo é UB (a biblioteca *hardened* do C++26 verifica; `std::span::at` chegou no C++26).
> [!question] Verificar na documentação oficial
> Disponibilidade de `span::at` no seu compilador.

## `span<byte>` e bytes

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <cstddef>
#include <iostream>
#include <span>

int main() {
    int dados[] = {1, 2, 3};
    auto bytes = std::as_bytes(std::span{dados});          // visão somente leitura dos bytes
    std::cout << bytes.size() << '\n';                      // 12 (3 * sizeof(int) típico)
}
```

## Veja também

- [[vector]]
- [[Arrays e std array]]
- [[string_view]]
- [[Complexidade e Invalidação de Iteradores]]

## Exercício

1. Escreva `void ordena_metade(std::span<int> v)` que ordena apenas a primeira metade do intervalo recebido.
2. Por que `span<const T>` é preferível a `const std::vector<T>&` em APIs genéricas?
