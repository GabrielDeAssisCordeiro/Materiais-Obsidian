---
titulo: "Expressões regulares: std::regex e alternativas"
tags: [cpp, strings]
aliases: ["std::regex", "Expressões regulares", "RE2", "CTRE", "Boost.Regex"]
tipo: conceito
nivel: intermediario
padrao: C++11
criado: 2026-10-24
relacionados: ["[[std string em Profundidade]]", "[[Unicode e Codificações]]", "[[Bibliotecas Estáticas e Dinâmicas]]"]
---

# Expressões regulares: `std::regex` e alternativas

`<regex>` (C++11) oferece `std::regex`, `regex_match` (casa a string **inteira**), `regex_search` (procura em qualquer ponto), `regex_replace` e iteradores `sregex_iterator`. Sintaxe padrão: ECMAScript.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <regex>
#include <string>

int main() {
    std::regex email{R"(([\w.]+)@([\w.]+\.\w+))"};     // raw string evita escapar barras
    std::string texto = "contatos: ana@ex.com, bruno.s@site.org.";

    std::smatch m;
    std::string resto = texto;
    for (std::sregex_iterator it{texto.begin(), texto.end(), email}, fim; it != fim; ++it)
        std::cout << (*it)[1] << " em " << (*it)[2] << '\n';   // usuário e domínio

    std::cout << std::regex_match("2026-10-24", std::regex{R"(\d{4}-\d{2}-\d{2})"}) << '\n';   // 1
    std::cout << std::regex_replace("a  b   c", std::regex{R"(\s+)"}, " ") << '\n';           // a b c

    if (std::regex_search(resto, m, std::regex{R"((\d+)\.(\d+))"})) std::cout << "achou\n";
    else std::cout << "sem números decimais\n";
}
```

> [!warning] Problemas conhecidos de `std::regex`
> - **Lento**, geralmente ordens de grandeza abaixo de RE2/PCRE2/Hyperscan.
> - **Estouro de pilha** em entradas grandes (implementação recursiva na libstdc++).
> - Sem suporte adequado a Unicode (opera por `char`).
> - Compilar a regex a cada chamada é caro: construa **uma vez** e reutilize.
> - Padrões vindos do usuário podem causar **ReDoS** (retrocesso catastrófico).

## Alternativas

| Biblioteca | Característica |
|---|---|
| **RE2** (Google) | Tempo linear, sem backtracking exponencial: seguro para entrada não confiável |
| **PCRE2** | Sintaxe Perl completa, rápida (JIT) |
| **Boost.Regex** | Mais completa/rápida que `std::regex`; base do padrão |
| **CTRE** (Compile Time Regular Expressions) | Regex avaliada em **compilação**, muito rápida |
| **Hyperscan/Vectorscan** | Milhares de padrões simultâneos |
| Parsing manual / `string_view` | Para formatos simples, muitas vezes basta e é mais rápido |

> [!tip] Antes de usar regex
> Para validar/tokenizar formatos simples, `std::from_chars`, `find`, `split` com [[string_view]] ou um parser pequeno costumam ser mais claros e rápidos. Veja também `std::from_chars` em [[Streams e iostream]].

## Veja também

- [[std string em Profundidade]]
- [[string_view]]
- [[Unicode e Codificações]]
- [[Bibliotecas Estáticas e Dinâmicas]]

## Exercício

1. Extraia todas as URLs `http(s)://...` de um texto e imprima o domínio de cada uma.
2. Reimplemente o mesmo problema sem regex (apenas `find`/`string_view`) e compare legibilidade.
