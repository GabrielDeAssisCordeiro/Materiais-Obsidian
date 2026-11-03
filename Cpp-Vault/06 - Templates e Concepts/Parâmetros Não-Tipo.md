---
titulo: "Parâmetros de template não-tipo"
tags: [cpp, templates]
aliases: ["Parâmetros de template não-tipo", "NTTP", "Non-type template parameters", "template<int N>"]
tipo: conceito
nivel: intermediario
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Templates de Classe]]", "[[Arrays e std array]]", "[[constexpr consteval constinit]]"]
---

# Parâmetros de template não-tipo

Além de **tipos**, templates aceitam **valores constantes de compilação** como parâmetros.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <array>
#include <cstddef>
#include <iostream>

template <typename T, std::size_t N>
class VetorFixo {                                   // semelhante a std::array
public:
    constexpr std::size_t tamanho() const { return N; }
    T& operator[](std::size_t i) { return dados_[i]; }
    const T& operator[](std::size_t i) const { return dados_[i]; }
private:
    T dados_[N]{};
};

template <int N>
struct Fatorial { static constexpr long valor = N * Fatorial<N - 1>::valor; };
template <>
struct Fatorial<0> { static constexpr long valor = 1; };

int main() {
    VetorFixo<int, 4> v;
    v[0] = 5;
    std::cout << v.tamanho() << v[0] << '\n';              // 45

    static_assert(Fatorial<5>::valor == 120);
    std::array<int, Fatorial<3>::valor> a{};               // tamanho 6
    std::cout << a.size() << '\n';
}
```

## O que pode ser parâmetro não-tipo

| Categoria | Padrão | Exemplo |
|---|---|---|
| Inteiros, `enum`, `bool`, `char` | C++98 | `template <int N>` |
| Ponteiros e referências a objetos com ligação | C++98 | `template <int* P>` |
| `std::nullptr_t` | C++11 | |
| `auto` (tipo deduzido) | **C++17** | `template <auto V>` |
| Tipos de classe "estruturais" (literais, membros públicos) | **C++20** | `template <Texto T>` |
| `double` e outros ponto flutuante | **C++20** | `template <double D>` |

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <algorithm>
#include <cstddef>
#include <iostream>
#include <string_view>

template <auto V>                                   // C++17: o tipo de V é deduzido
struct Constante { static constexpr auto valor = V; };

template <std::size_t N>
struct TextoFixo {                                  // tipo estrutural (C++20): pode ser NTTP
    constexpr TextoFixo(const char (&s)[N]) { std::copy_n(s, N, dados); }
    char dados[N];
};

template <TextoFixo T>
struct Etiqueta {
    static constexpr std::string_view nome() { return T.dados; }
};

int main() {
    std::cout << Constante<42>::valor << Constante<'x'>::valor << Constante<true>::valor << '\n';
    std::cout << Etiqueta<"ola">::nome() << '\n';   // string literal como parâmetro de template (C++20)
}
```

## Valores padrão e deduzidos

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <cstddef>
#include <iostream>

template <typename T, std::size_t N>
constexpr std::size_t tam(const T (&)[N]) { return N; }          // N deduzido do tipo do array

template <typename T = int, int Base = 10>                        // padrões
struct Config { T v = Base; };

int main() {
    int a[7];
    std::cout << tam(a) << Config<>{}.v << Config<double, 3>{}.v << '\n';   // 7103
}
```

## Quando usar

- Tamanhos e dimensões conhecidos em compilação (`std::array<T, N>`, `std::bitset<N>`, matrizes `Matriz<T, L, C>`).
- Configuração por **política** (`template <bool Thread_safe>`).
- Metaprogramação com valores.

> [!bug] Exemplo inválido proposital
> ```cpp
> int n = 5;
> std::array<int, n> a;     // erro: n não é constante de compilação
> ```
> **Correção:** `constexpr int n = 5;`.

## Veja também

- [[Templates de Classe]]
- [[Arrays e std array]]
- [[constexpr consteval constinit]]
- [[Metaprogramação em Compilação]]

## Exercício

1. Implemente `Matriz<T, L, C>` com `operator*` entre `Matriz<T, L, M>` e `Matriz<T, M, C>`; verifique que dimensões incompatíveis não compilam.
2. O que muda ao trocar `template <int N>` por `template <auto N>`?
