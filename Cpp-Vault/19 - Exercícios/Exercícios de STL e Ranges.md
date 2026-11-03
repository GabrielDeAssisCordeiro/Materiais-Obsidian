---
titulo: "Exercícios de STL e Ranges"
tags: [cpp, exercicios, stl, ranges]
aliases: ["Exercícios de STL"]
tipo: exercicio
nivel: intermediario
padrao: C++20
criado: 2026-10-24
relacionados: ["[[MOC - STL e Ranges]]", "[[MOC - Exercícios - Cpp]]"]
---

# Exercícios de STL e Ranges

Teoria: [[vector]], [[unordered_map e unordered_set]], [[Algoritmos da STL]], [[Ranges e Views]], [[Lambdas e Captura]].

## 1. Frequência de palavras

Dado um texto, conte a frequência de cada palavra e imprima do mais ao menos frequente (desempate alfabético).

> [!success] Gabarito

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>

int main() {
    std::istringstream in{"a casa a porta a casa o sol"};
    std::unordered_map<std::string, int> freq;
    for (std::string w; in >> w;) ++freq[w];

    std::vector<std::pair<std::string, int>> v(freq.begin(), freq.end());
    std::ranges::sort(v, [](const auto& a, const auto& b) {
        return a.second != b.second ? a.second > b.second : a.first < b.first;
    });
    for (const auto& [palavra, n] : v) std::cout << palavra << '=' << n << ' ';
    std::cout << '\n';   // a=3 casa=2 o=1 porta=1 sol=1
}
```

## 2. Remover elementos

Remova de um `std::vector<int>` todos os números pares, sem laço manual de `erase`.

> [!success] Gabarito

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <vector>

int main() {
    std::vector<int> v{1, 2, 3, 4, 5, 6};
    std::erase_if(v, [](int x) { return x % 2 == 0; });   // C++20
    for (int x : v) std::cout << x << ' ';                // 1 3 5
    std::cout << '\n';
}
```

## 3. Pipeline com ranges

Dos números de 1 a 20, pegue os ímpares, eleve ao quadrado e fique com os 5 primeiros.

> [!success] Gabarito

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <ranges>

int main() {
    namespace v = std::views;
    for (int x : v::iota(1, 21)
                 | v::filter([](int n) { return n % 2 == 1; })
                 | v::transform([](int n) { return n * n; })
                 | v::take(5))
        std::cout << x << ' ';                            // 1 9 25 49 81
    std::cout << '\n';
}
```

## 4. Ordenar por vários critérios

Ordene pessoas por idade decrescente e, em empate, por nome crescente, usando `std::tie`.

> [!success] Gabarito

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <algorithm>
#include <iostream>
#include <string>
#include <tuple>
#include <vector>

struct Pessoa { std::string nome; int idade; };

int main() {
    std::vector<Pessoa> v{{"Ana", 30}, {"Bruno", 25}, {"Caio", 30}};
    std::ranges::sort(v, [](const Pessoa& a, const Pessoa& b) {
        return std::tie(b.idade, a.nome) < std::tie(a.idade, b.nome);   // idade desc, nome asc
    });
    for (const auto& p : v) std::cout << p.nome << ' ';                  // Ana Caio Bruno
    std::cout << '\n';
}
```

## Veja também

- [[Algoritmos da STL]]
- [[Ranges e Views]]
- [[Escolhendo um Contêiner]]
- [[MOC - Exercícios - Cpp]]

## Exercício

Refaça o exercício 1 com `std::map` (ordenado) e compare a saída e a complexidade com a versão `unordered_map`.
