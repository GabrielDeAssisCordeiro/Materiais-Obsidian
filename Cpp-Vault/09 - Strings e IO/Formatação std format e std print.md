---
titulo: "Formatação: std::format e std::print"
tags: [cpp, io, format, print, formatacao, cpp20, cpp23]
aliases: ["std::format", "std::print", "std::println", "std::formatter", "format_to", "Formatação de texto"]
tipo: conceito
nivel: intermediario
padrao: C++20
criado: 2026-10-24
relacionados: ["[[Streams e iostream]]", "[[Entrada e Saída Básica]]", "[[Unicode e Codificações]]"]
---

# Formatação: `std::format` e `std::print`

> [!info] Introdução
> - `std::format` / `format_to` / `formatted_size`: **C++20** (`<format>`). GCC 13+, MSVC 2019 16.10+, libc++ 17+ (completo em versões posteriores).
> - `std::print` / `println`: **C++23** (`<print>`). GCC 14+, MSVC 2022 17.7+, libc++ 18+.
> - `std::formatter` customizado, `std::format_string`: C++20; `std::runtime_format`: C++26.
> [!question] Verificar na documentação oficial
> Versões mínimas exatas na página *C++ compiler support* da cppreference. Os exemplos de `<print>` abaixo estão marcados como não verificados porque o ambiente de teste do vault usa GCC 13.

Substituem `printf` (inseguro) e `iostream` (verboso, estado pegajoso) por **strings de formato em estilo Python**, verificadas em **compilação**.

## Sintaxe de formato

`{[índice][:especificação]}` — a especificação segue `[[fill]align][sign][#][0][width][.precision][type]`.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <format>
#include <iostream>
#include <string>
#include <vector>

int main() {
    std::cout << std::format("{} tem {} anos\n", "Ana", 30);                 // posicional automático
    std::cout << std::format("{1} {0} {1}\n", "a", "b");                      // por índice: b a b
    std::cout << std::format("{:>8}|{:<8}|{:^8}|\n", "dir", "esq", "meio");   // alinhamentos
    std::cout << std::format("{:*^10}\n", "x");                               // preenchimento: ****x*****
    std::cout << std::format("{:.2f} {:8.3f} {:+d} {:05d}\n", 3.14159, 2.5, 7, 42);   // 3.14    2.500 +7 00042
    std::cout << std::format("{:#x} {:#b} {:o} {:X}\n", 255, 5, 8, 255);     // 0xff 0b101 10 FF
    std::cout << std::format("{:e} {:g}\n", 12345.678, 0.0001);
    std::cout << std::format("{:>{}}\n", "largura dinâmica", 20);            // largura vinda de argumento
    std::cout << std::format("{{literal}} {}\n", true);                        // chaves duplas escapam: {literal} true
}
```

> [!bug] Formato inválido não compila (de propósito)
> ```cpp
> // ERRO INTENCIONAL (não compila): "{:%}" não é especificação válida para string.
> // Correção: use uma especificação válida, p.ex. "{:>8}".
> std::string s = std::format("{:%}", "x");
> ```
> Como a string de formato é verificada **em compilação**, o erro aparece no build, não em execução.

## Mais exemplos

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <format>
#include <iostream>
#include <iterator>
#include <string>
#include <vector>

int main() {
    std::cout << std::format("{:>8}|{:<8}|{:^8}|\n", "dir", "esq", "meio");
    std::cout << std::format("{:.2f} {:+d} {:05d} {:#x}\n", 3.14159, 7, 42, 255);

    std::string buffer;
    std::format_to(std::back_inserter(buffer), "{}-{}", 1, 2);               // escreve num iterador de saída
    std::cout << buffer << ' ' << std::formatted_size("{:>10}", "oi") << '\n';   // 1-2 10

    std::vector<int> v{1, 2, 3};
    for (int x : v) std::cout << std::format("[{:3}]", x);                    // [  1][  2][  3]
    std::cout << '\n';
}
```

## `std::print` (C++23)

```cpp
// [nv] g++ -std=c++23 -Wall -Wextra   (requer GCC 14+; indisponível no ambiente de teste do vault)
#include <print>

int main() {
    std::println("Olá, {}!", "mundo");                  // com '\n' no final
    std::print("{} + {} = {}\n", 2, 3, 5);
    std::println(stderr, "erro: {}", 42);               // para outro FILE*
}
```

Vantagens: sem estado pegajoso, **bem mais rápido** que `iostream` em muitos casos, tratamento correto de Unicode em terminais que suportam e verificação em compilação.

## Formatando tipos próprios: `std::formatter`

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <format>
#include <iostream>

struct Ponto { int x, y; };

template <>
struct std::formatter<Ponto> {
    constexpr auto parse(std::format_parse_context& ctx) { return ctx.begin(); }   // sem opções próprias
    auto format(const Ponto& p, std::format_context& ctx) const {
        return std::format_to(ctx.out(), "({}, {})", p.x, p.y);
    }
};

int main() {
    std::cout << std::format("origem = {}\n", Ponto{0, 0});
}
```

## Comparação

| | `printf` | `iostream` | `std::format`/`print` |
|---|---|---|---|
| Segurança de tipos | **Não** | Sim | Sim |
| Erros de formato | Execução (UB) | — | **Compilação** |
| Tipos próprios | Não | `operator<<` | `std::formatter` |
| Estado persistente | Não | **Sim** (pegajoso) | Não |
| Ordem dos argumentos reordenável (i18n) | `%1$d` (POSIX) | Não | **Sim** (`{1}`) |

> [!warning] Formatos dinâmicos
> A string de formato deve ser **constante de compilação**. Para formatos vindos de dados (tradução, configuração), use `std::vformat` com `std::make_format_args` (ou `std::runtime_format` em C++26) e trate `std::format_error`.

## Veja também

- [[Streams e iostream]]
- [[Entrada e Saída Básica]]
- [[Unicode e Codificações]]
- [[Locale]]

## Exercício

1. Imprima uma tabela 5×3 alinhada com larguras dinâmicas usando `std::format`.
2. Implemente `std::formatter<Cor>` que suporte as especificações `{:hex}` e `{:rgb}`.
