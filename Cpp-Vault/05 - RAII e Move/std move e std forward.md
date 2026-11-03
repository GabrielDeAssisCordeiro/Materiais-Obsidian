---
titulo: "std::move e std::forward"
tags: [cpp, move]
aliases: ["std::move", "std::forward", "Cast para rvalue", "std::exchange"]
tipo: conceito
nivel: intermediario
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Semântica de Movimento]]", "[[Referências Universais e Perfect Forwarding]]", "[[Lvalue e Rvalue]]"]
---

# `std::move` e `std::forward`

Ambos estão em `<utility>` e **são apenas casts** — nenhum deles move ou encaminha nada por si só.

## `std::move`

`std::move(x)` converte `x` em um **rvalue** (xvalue): "pode roubar de mim". Quem de fato move é o **construtor/atribuição de movimento** selecionado pela sobrecarga.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <string>
#include <utility>
#include <vector>

int main() {
    std::string s = "uma string bem longa para evitar a otimização de string pequena";
    std::vector<std::string> v;

    v.push_back(s);                  // cópia: s continua com o valor
    v.push_back(std::move(s));       // movimento: s fica "movido"
    std::cout << v[0].size() << ' ' << v[1].size() << '\n';

    // std::move em tipos triviais é só cópia
    int a = 5;
    int b = std::move(a);
    std::cout << a << b << '\n';     // 55
}
```

> [!warning] `std::move` em `const` copia
> `std::move(objeto_const)` produz `const T&&`, que **não** liga a `T&&`: cai no construtor de cópia. Sem erro, mas sem movimento.

> [!bug] `return std::move(local);` é um anti-padrão
> Impede a elisão (NRVO) e pode ser mais lento. Escreva `return local;` — o compilador já trata `local` como rvalue na devolução ([[Copy Elision e RVO]]).

## Quando usar `std::move`

| Situação | Exemplo |
|---|---|
| Passar objeto que **não será mais usado** | `lista.push_back(std::move(obj));` |
| Transferir posse de membros | `: nome_(std::move(nome))` (parâmetro por valor) |
| Mover **membros** em construtor/atribuição de movimento | `dados_(std::move(o.dados_))` |
| Trocar valores | `std::swap`, `std::exchange` |

## `std::exchange` (C++14)

`std::exchange(obj, novo)` devolve o valor antigo e atribui `novo` — ideal para construtores de movimento.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <utility>

int main() {
    int* p = new int(7);
    int* q = std::exchange(p, nullptr);     // q recebe o antigo; p vira nullptr
    std::cout << (p == nullptr) << *q << '\n';   // 17
    delete q;
}
```

## `std::forward`

`std::forward<T>(x)` **preserva a categoria de valor** original de um argumento em código genérico: se o chamador passou um rvalue, encaminha como rvalue; se passou lvalue, como lvalue. É a base do **perfect forwarding** ([[Referências Universais e Perfect Forwarding]]).

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <string>
#include <utility>

void alvo(const std::string&) { std::cout << "lvalue\n"; }
void alvo(std::string&&)      { std::cout << "rvalue\n"; }

template <typename T>
void encaminha_ruim(T&& x)  { alvo(x); }                     // x tem nome: SEMPRE lvalue
template <typename T>
void encaminha_bom(T&& x)   { alvo(std::forward<T>(x)); }    // preserva a categoria

int main() {
    std::string s = "a";
    encaminha_ruim(std::string("b"));   // lvalue (perdeu o rvalue)
    encaminha_bom(s);                   // lvalue
    encaminha_bom(std::string("c"));    // rvalue
}
```

## Comparação

| | `std::move(x)` | `std::forward<T>(x)` |
|---|---|---|
| Condicional? | Não: sempre rvalue | Sim: depende de `T` |
| Onde | Qualquer lugar | Apenas em templates com `T&&` |
| Intenção | "Pode roubar de mim" | "Repasse como recebeu" |

## Veja também

- [[Semântica de Movimento]]
- [[Referências Universais e Perfect Forwarding]]
- [[Copy Elision e RVO]]
- [[Lvalue e Rvalue]]

## Exercício

1. Escreva `template<class T> void adiciona(std::vector<T>& v, T&& x)` e observe o que acontece com `adiciona(v, s)` (lvalue). Por quê?
2. Reescreva o construtor de movimento de `Buffer` ([[Regra do 0, 3 e 5]]) usando `std::exchange`.
