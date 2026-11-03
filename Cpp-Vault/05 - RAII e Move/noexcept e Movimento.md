---
titulo: "noexcept e movimento"
tags: [cpp, move, vector, excecoes]
aliases: ["noexcept", "move_if_noexcept", "Operador noexcept", "Especificação noexcept"]
tipo: conceito
nivel: intermediario
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Semântica de Movimento]]", "[[Regra do 0, 3 e 5]]", "[[Funções - Cpp]]"]
---

# `noexcept` e movimento

`noexcept` declara que uma função **não lança exceções**. Se mesmo assim uma exceção escapar, o programa chama `std::terminate`.

## Sintaxe

```cpp
void f() noexcept;                  // não lança
void g() noexcept(true);            // equivalente
void h() noexcept(noexcept(T()));   // condicional: depende de uma expressão
bool b = noexcept(f());             // operador: true se f() não lança (avaliado em compilação)
```

## Por que importa para o movimento

Ao crescer, `std::vector` precisa mover elementos para o novo buffer. Para manter a **garantia forte de exceção**, usa `std::move_if_noexcept`: se o movimento **pode lançar** e o tipo é copiável, o vetor **copia** em vez de mover.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <vector>

struct Movel {
    Movel() = default;
    Movel(const Movel&)            { std::cout << "cópia\n"; }
    Movel(Movel&&) noexcept        { std::cout << "move\n"; }     // noexcept: vector usa movimento
};

struct MovelSemNoexcept {
    MovelSemNoexcept() = default;
    MovelSemNoexcept(const MovelSemNoexcept&)  { std::cout << "cópia\n"; }
    MovelSemNoexcept(MovelSemNoexcept&&)       { std::cout << "move\n"; }   // pode lançar: vector prefere cópia
};

int main() {
    std::cout << "-- com noexcept\n";
    std::vector<Movel> a(1);
    a.reserve(10);                       // realocação: usa move

    std::cout << "-- sem noexcept\n";
    std::vector<MovelSemNoexcept> b(1);
    b.reserve(10);                       // realocação: usa cópia (!)
}
```

> [!warning] Esquecer `noexcept` no movimento custa desempenho
> Seus tipos movíveis ficam sendo **copiados** em `std::vector`, `std::deque` (em algumas operações), `std::swap` genérico etc. Marque movimentos e `swap` como `noexcept` quando for verdade.

## O que deve ser `noexcept`

| Função | Deve ser `noexcept`? |
|---|---|
| Destrutor | **Já é** por padrão (não declare `noexcept(false)`) |
| Construtor/atribuição de movimento | **Sim**, sempre que possível |
| `swap` | **Sim** |
| Funções que podem falhar (E/S, alocação...) | Não |
| Funções "folha" triviais | Opcional; ajuda o otimizador |

> [!tip] Verificando em compilação
> `static_assert(std::is_nothrow_move_constructible_v<T>);` garante que o tipo será movido por contêineres.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <string>
#include <type_traits>
#include <vector>

static_assert(std::is_nothrow_move_constructible_v<std::string>);
static_assert(std::is_nothrow_move_constructible_v<std::vector<int>>);

int main() {}
```

## Custos e riscos

- `noexcept` **não** custa nada em tempo de execução (ao contrário das antigas `throw()`).
- Quebrar a promessa **termina** o programa: use com cuidado em funções que chamam código desconhecido.

> [!info] Mais sobre exceções
> Garantias de segurança de exceções e o custo das exceções estão na seção de tratamento de erros.

## Veja também

- [[Semântica de Movimento]]
- [[Regra do 0, 3 e 5]]
- [[std move e std forward]]
- [[Funções - Cpp]]

## Exercício

1. Remova o `noexcept` do construtor de movimento de `Buffer` ([[Regra do 0, 3 e 5]]) e observe se `std::vector<Buffer>` o utiliza ao crescer.
2. Por que destrutores são `noexcept` por padrão?
