---
titulo: "Exercícios de Erros, Strings e IO"
tags: [cpp, exercicios, erros, excecoes, strings, io]
aliases: ["Exercícios de erros e strings"]
tipo: exercicio
nivel: intermediario
padrao: C++20
criado: 2026-10-24
relacionados: ["[[MOC - Erros e Exceções]]", "[[MOC - Strings e IO]]", "[[MOC - Exercícios - Cpp]]"]
---

# Exercícios de Erros, Strings e IO

Teoria: [[Exceções try catch throw]], [[Segurança de Exceções]], [[optional]], [[string_view]], [[Formatação std format e std print]].

## 1. Converter texto em inteiro sem exceções

Escreva `std::optional<int> parse_int(std::string_view)` com `std::from_chars`; rejeite lixo no fim (`"12x"`).

> [!success] Gabarito

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <charconv>
#include <iostream>
#include <optional>
#include <string_view>

std::optional<int> parse_int(std::string_view s) {
    int v{};
    auto [fim, ec] = std::from_chars(s.data(), s.data() + s.size(), v);
    if (ec != std::errc{} || fim != s.data() + s.size()) return std::nullopt;
    return v;
}

int main() {
    for (auto t : {"42", "-7", "12x", ""}) {
        auto r = parse_int(t);
        std::cout << '"' << t << "\" -> " << (r ? std::to_string(*r) : "inválido") << '\n';
    }
}
```

## 2. Exceção própria

Crie `ErroDeSaldo` derivada de `std::runtime_error`, lançada por `sacar` quando o saldo é insuficiente; capture por referência `const`.

> [!success] Gabarito

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <stdexcept>

struct ErroDeSaldo : std::runtime_error {
    double faltam;
    ErroDeSaldo(double f) : std::runtime_error("saldo insuficiente"), faltam(f) {}
};

class Conta {
    double saldo_ = 100;
public:
    void sacar(double v) {
        if (v > saldo_) throw ErroDeSaldo(v - saldo_);
        saldo_ -= v;                           // só altera DEPOIS de validar (garantia forte)
    }
};

int main() {
    Conta c;
    try { c.sacar(150); }
    catch (const ErroDeSaldo& e) { std::cout << e.what() << ": faltam " << e.faltam << '\n'; }
}
```

## 3. `split` e `join`

Implemente `split(std::string_view, char)` e `join(vector<string>, string_view)`.

> [!success] Gabarito

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <string>
#include <string_view>
#include <vector>

std::vector<std::string> split(std::string_view s, char sep) {
    std::vector<std::string> r;
    std::size_t ini = 0;
    while (true) {
        auto pos = s.find(sep, ini);
        if (pos == std::string_view::npos) { r.emplace_back(s.substr(ini)); break; }
        r.emplace_back(s.substr(ini, pos - ini));
        ini = pos + 1;
    }
    return r;
}

std::string join(const std::vector<std::string>& v, std::string_view sep) {
    std::string r;
    for (std::size_t i = 0; i < v.size(); ++i) {
        if (i) r += sep;
        r += v[i];
    }
    return r;
}

int main() {
    auto partes = split("a,b,,c", ',');
    std::cout << partes.size() << ' ' << join(partes, "|") << '\n';   // 4 a|b||c
}
```

## 4. Tabela formatada

Imprima a tabela abaixo alinhada, com `std::format` (C++20): nome à esquerda (10 colunas) e preço à direita com 2 casas.

> [!success] Gabarito

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <format>
#include <iostream>

int main() {
    struct Item { const char* nome; double preco; };
    for (auto [nome, preco] : {Item{"Café", 7.5}, Item{"Pão", 1.25}})
        std::cout << std::format("{:<10}{:>8.2f}\n", nome, preco);
}
```

> [!warning] Largura e UTF-8
> O padrão calcula a largura em "colunas" estimadas por ponto de código, mas o **GCC 13** testado aqui contou *bytes* (`é` desalinhou a coluna: `Café` ocupa 5 bytes). Versões recentes corrigem isso; em código portável use fonte ASCII ou ajuste a largura manualmente ([[Unicode e Codificações]]).

## Veja também

- [[Exceções try catch throw]]
- [[Segurança de Exceções]]
- [[Streams e iostream]]
- [[MOC - Exercícios - Cpp]]

## Exercício

Reescreva o exercício 1 retornando `std::expected<int, std::errc>` (C++23) e compare com `optional` ([[Tratamento de Erros com expected]]).
