---
titulo: "SFINAE e enable_if"
tags: [cpp, templates, metaprogramacao]
aliases: ["SFINAE", "enable_if", "Substitution Failure Is Not An Error", "void_t", "Detection idiom"]
tipo: conceito
nivel: avancado
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Concepts e requires]]", "[[if constexpr]]", "[[static_assert e Type Traits]]"]
---

# SFINAE e `enable_if`

**SFINAE** = *Substitution Failure Is Not An Error*: se, ao **substituir** os argumentos de template na **assinatura** de um candidato, o resultado for inválido, esse candidato é **descartado silenciosamente** em vez de gerar erro de compilação.

> [!info] Contexto histórico
> Foi a técnica principal para restringir templates de C++11 a C++17. Em C++20, **concepts** ([[Concepts e requires]]) a substituem na grande maioria dos casos, com sintaxe e mensagens muito melhores. Aprenda SFINAE para **ler código existente**.

## Exemplo mínimo

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>

template <typename T>
auto tem_size(const T& x) -> decltype(x.size(), void()) {   // inválido se T não tem .size(): vira "não viável"
    std::cout << "tem size: " << x.size() << '\n';
}

void tem_size(...) { std::cout << "sem size\n"; }           // fallback (reticências: pior conversão)

#include <string>
int main() {
    tem_size(std::string("abc"));    // template viável: tem size: 3
    tem_size(42);                    // template descartado (SFINAE): sem size
}
```

## `std::enable_if`

`std::enable_if_t<cond, T>` é `T` se `cond` for verdadeira; caso contrário **não existe** (falha de substituição).

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <string>
#include <type_traits>

// Sobrecarga habilitada só para tipos integrais
template <typename T, std::enable_if_t<std::is_integral_v<T>, int> = 0>
std::string forma(T v) { return "int:" + std::to_string(v); }

// Sobrecarga habilitada só para ponto flutuante
template <typename T, std::enable_if_t<std::is_floating_point_v<T>, int> = 0>
std::string forma(T v) { return "fp:" + std::to_string(v); }

int main() {
    std::cout << forma(7) << ' ' << forma(2.5) << '\n';
    // forma("x");        // erro: nenhuma função viável (ambas descartadas)
}
```

O padrão `std::enable_if_t<cond, int> = 0` como **parâmetro não-tipo com valor padrão** é o mais usado: não polui a assinatura de retorno.

## `std::void_t` e o idioma de detecção

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <string>
#include <type_traits>
#include <vector>

template <typename, typename = void>
struct tem_push_back : std::false_type {};                 // caso geral

template <typename T>
struct tem_push_back<T, std::void_t<decltype(std::declval<T&>().push_back(std::declval<typename T::value_type>()))>>
    : std::true_type {};                                   // especialização válida só se a expressão compilar

int main() {
    std::cout << tem_push_back<std::vector<int>>::value << tem_push_back<int>::value << '\n';   // 10
    static_assert(tem_push_back<std::string>::value);
}
```

## A mesma ideia com C++20

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <concepts>
#include <iostream>
#include <vector>

template <typename T>
concept TemPushBack = requires(T c, typename T::value_type v) { c.push_back(v); };

template <TemPushBack C>
void adiciona(C& c, typename C::value_type v) { c.push_back(v); }

int main() {
    std::vector<int> v;
    adiciona(v, 5);
    std::cout << v.size() << '\n';
    static_assert(!TemPushBack<int>);
}
```

## Comparação

| | SFINAE | `if constexpr` | Concepts |
|---|---|---|---|
| Padrão | C++11 | C++17 | C++20 |
| Escolhe **sobrecarga** | Sim | Não | Sim |
| Escolhe **código** dentro de uma função | Difícil | **Sim** | Combina com `if constexpr` |
| Legibilidade | Baixa | Alta | Alta |
| Mensagem de erro | Ruim ("no matching function") | Boa | **Ótima** |

## Veja também

- [[Concepts e requires]]
- [[if constexpr]]
- [[static_assert e Type Traits]]
- [[Especialização de Templates]]

## Exercício

1. Reescreva as duas sobrecargas de `forma` usando concepts (`std::integral`, `std::floating_point`).
2. Por que o erro dentro do **corpo** de uma função template não aciona SFINAE (só a assinatura)?
