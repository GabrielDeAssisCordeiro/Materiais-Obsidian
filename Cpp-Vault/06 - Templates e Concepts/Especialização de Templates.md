---
titulo: "Especialização de templates"
tags: [cpp, templates]
aliases: ["Especialização total", "Especialização parcial", "Template specialization"]
tipo: conceito
nivel: avancado
padrao: C++98
criado: 2026-10-24
relacionados: ["[[Templates de Classe]]", "[[static_assert e Type Traits]]", "[[SFINAE e enable_if]]"]
---

# Especialização de templates

Permite fornecer uma implementação **diferente** para tipos específicos.

## Especialização total

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <string>

template <typename T>
struct Descricao {                                   // template primário
    static std::string nome() { return "tipo genérico"; }
};

template <>
struct Descricao<int> {                              // especialização total para int
    static std::string nome() { return "inteiro"; }
};

template <>
struct Descricao<std::string> {
    static std::string nome() { return "texto"; }
};

int main() {
    std::cout << Descricao<double>::nome() << ' ' << Descricao<int>::nome() << ' '
              << Descricao<std::string>::nome() << '\n';
}
```

## Especialização parcial (só para templates de classe e variável)

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <type_traits>
#include <vector>

template <typename T>
struct E_Ponteiro { static constexpr bool valor = false; };

template <typename T>
struct E_Ponteiro<T*> { static constexpr bool valor = true; };     // parcial: qualquer T*

template <typename T>
struct ElementoDe { using tipo = T; };

template <typename T>
struct ElementoDe<std::vector<T>> { using tipo = T; };             // parcial: vector<T> -> T

template <typename A, typename B> struct Par { static constexpr int n = 0; };
template <typename A> struct Par<A, A> { static constexpr int n = 1; };    // mesmo tipo

int main() {
    std::cout << E_Ponteiro<int>::valor << E_Ponteiro<int*>::valor << '\n';    // 01
    static_assert(std::is_same_v<ElementoDe<std::vector<double>>::tipo, double>);
    std::cout << Par<int, double>::n << Par<int, int>::n << '\n';              // 01
}
```
## Funções: use sobrecarga, não especialização parcial

Templates de **função** não têm especialização parcial. A especialização total de funções interage mal com a sobrecarga (a especialização **não participa** da escolha da sobrecarga). Prefira **sobrecarga** ou *tag dispatching*/`if constexpr`/concepts.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>

template <typename T> void f(T)  { std::cout << "genérico\n"; }
template <typename T> void f(T*) { std::cout << "ponteiro\n"; }   // outra sobrecarga (não especialização)

int main() {
    int x = 0;
    f(x);     // genérico
    f(&x);    // ponteiro
}
```

## Traits: o uso clássico

Uma **trait** é um template de classe especializado que informa propriedades de um tipo (usado em toda a biblioteca padrão: `std::is_integral`, `std::iterator_traits`, `std::char_traits`).

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>

template <typename T> struct Zero;                          // declarado, não definido: obriga a especializar
template <> struct Zero<int>    { static constexpr int valor = 0; };
template <> struct Zero<double> { static constexpr double valor = 0.0; };

template <typename T>
T inicial() { return Zero<T>::valor; }

int main() { std::cout << inicial<int>() << inicial<double>() << '\n'; }
```

> [!bug] Exemplo inválido proposital
> ```cpp
> inicial<char>();   // erro: implicit instantiation of undefined template 'Zero<char>'
> ```
> Esse erro é desejado: avisa que a trait não foi definida para `char`.

> [!warning] Declare a especialização antes do primeiro uso
> Usar `Descricao<int>` antes de a especialização ser visível é erro (instanciação do primário já ocorreu). Mantenha especializações no mesmo cabeçalho, logo após o primário.

## Alternativas modernas

| Necessidade | Em vez de especializar |
|---|---|
| Código diferente por categoria de tipo | `if constexpr` ([[if constexpr]]) |
| Habilitar/desabilitar sobrecargas | **Concepts** ([[Concepts e requires]]) |
| Constantes por tipo | [[Templates de Variável]] |

## Veja também

- [[Templates de Classe]]
- [[static_assert e Type Traits]]
- [[SFINAE e enable_if]]
- [[if constexpr]]
- [[Concepts e requires]]

## Exercício

1. Crie `NomeDoTipo<T>::valor()` com especializações para `int`, `double` e `std::string`.
2. Implemente `remove_pointer<T>` por especialização parcial e compare com `std::remove_pointer_t`.
