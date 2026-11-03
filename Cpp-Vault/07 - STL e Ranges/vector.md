---
titulo: "std::vector"
tags: [cpp, stl, vector, conteineres, sequenciais]
aliases: ["std::vector", "vector", "Array dinâmico", "capacity e reserve", "emplace_back"]
tipo: conceito
nivel: iniciante
padrao: C++98
criado: 2026-10-24
relacionados: ["[[Complexidade e Invalidação de Iteradores]]", "[[deque]]", "[[Escolhendo um Contêiner]]"]
---

# `std::vector`

Array **dinâmico e contíguo**: o contêiner padrão do C++. Elementos ficam lado a lado na memória (ótima localidade de cache), com crescimento automático.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

int main() {
    std::vector<int> v;                       // vazio
    std::vector<int> a(5);                    // 5 zeros
    std::vector<int> b(3, 7);                 // {7, 7, 7}
    std::vector<int> c{1, 2, 3, 4};           // lista de inicialização

    v.reserve(100);                           // reserva capacidade (sem criar elementos)
    for (int i = 0; i < 5; ++i) v.push_back(i * i);     // 0 1 4 9 16
    v.emplace_back(25);                       // constrói no lugar

    std::cout << v.size() << ' ' << v.capacity() << '\n';       // 6 100
    std::cout << v[2] << ' ' << v.at(3) << ' ' << v.front() << ' ' << v.back() << '\n';

    v.insert(v.begin() + 1, 99);              // O(n): desloca os seguintes
    v.erase(v.begin());                       // remove o primeiro: O(n)
    v.pop_back();                             // O(1)

    // Idioma erase-remove (pré-C++20) / std::erase_if (C++20)
    std::erase_if(v, [](int x) { return x % 2 == 0; });          // remove pares

    for (int x : v) std::cout << x << ' ';
    std::cout << '\n';

    int* p = v.data();                        // ponteiro para o buffer contíguo (interop com C)
    (void)p;
    v.shrink_to_fit();                        // pedido (não vinculante) de reduzir a capacidade
    v.clear();                                // size = 0; capacity inalterada
}
```

## `size` vs `capacity`

- **`size()`**: número de elementos.
- **`capacity()`**: elementos que cabem **sem realocar**.
- Ao estourar a capacidade, aloca um buffer maior (crescimento **geométrico**, tipicamente ×1,5 ou ×2), **move/copia** os elementos e libera o antigo → `push_back` é **O(1) amortizado**.

> [!tip] `reserve` evita realocações
> Se souber o tamanho aproximado, chame `v.reserve(n)` antes de inserir: elimina cópias/movimentos e **preserva iteradores**.

## Complexidade

| Operação | Custo |
|---|---|
| `v[i]`, `at(i)`, `front`, `back` | O(1) |
| `push_back`, `emplace_back` | O(1) amortizado |
| `pop_back` | O(1) |
| `insert/erase` no meio ou início | O(n) |
| Busca linear | O(n) |
| Busca binária (ordenado) | O(log n) |

## Invalidação

> [!danger] Referências e iteradores podem invalidar
> ```cpp
> std::vector<int> v{1, 2, 3};
> int& r = v[0];
> v.push_back(4);        // pode realocar: 'r' agora é pendente
> r = 10;                // UB possível
> ```
> Veja [[Complexidade e Invalidação de Iteradores]]. Regra: `push_back`/`insert` fora de `reserve` invalida tudo se realocar; `erase` invalida do ponto em diante.

## `operator[]` vs `at()`

| | `v[i]` | `v.at(i)` |
|---|---|---|
| Verifica limites | **Não** (UB se fora) | **Sim** (`std::out_of_range`) |
| Custo | Mínimo | Pequeno |

> [!warning] Acesso fora do intervalo
> `v[v.size()]` é UB. Em *builds* de desenvolvimento ative as verificações da biblioteca: `-D_GLIBCXX_ASSERTIONS` (libstdc++) ou os modos *hardened* de libc++/MS STL.

## `std::vector<bool>` é especial

É uma especialização que **empacota bits** e retorna um *proxy* em `operator[]`, não `bool&`. Evite em código genérico; prefira `std::vector<char>`, `std::deque<bool>` ou `std::bitset`.

## Matrizes e vetores de vetores

`std::vector<std::vector<int>>` não é contíguo entre linhas. Para matrizes densas use um `std::vector<int>` único com `i * colunas + j` (ou `std::mdspan` no C++23).

## Veja também

- [[Complexidade e Invalidação de Iteradores]]
- [[deque]]
- [[Escolhendo um Contêiner]]
- [[span]]
- [[Arrays e std array]]

## Exercício

1. Insira 1 milhão de inteiros com e sem `reserve` e conte quantas vezes `capacity()` muda.
2. Remova todos os elementos duplicados de um vetor ordenado (dica: `std::unique` + `erase`).
