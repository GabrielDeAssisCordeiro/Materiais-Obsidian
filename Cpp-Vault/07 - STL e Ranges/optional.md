---
titulo: "std::optional"
tags: [cpp, stl, vocabulary-types, cpp17]
aliases: ["std::optional", "optional", "Valor opcional", "nullopt"]
tipo: conceito
nivel: intermediario
padrao: C++17
criado: 2026-10-24
relacionados: ["[[variant]]", "[[expected]]", "[[Tratamento de Erros com expected]]"]
---

# `std::optional`

> [!info] Introdução
> **C++17** (`<optional>`). As operações monádicas `and_then`, `transform`, `or_else` chegaram no **C++23**.

`std::optional<T>` representa **"um `T` ou nada"**, **por valor** (sem heap e sem ponteiro nulo). Substitui "valores mágicos" (`-1`, `""`) e `T*` para ausência.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <optional>
#include <string>
#include <vector>

std::optional<int> acha_indice(const std::vector<std::string>& v, const std::string& alvo) {
    for (std::size_t i = 0; i < v.size(); ++i)
        if (v[i] == alvo) return static_cast<int>(i);        // converte implicitamente para optional
    return std::nullopt;                                      // "nada"
}

std::optional<double> raiz(double x) {
    if (x < 0) return {};                                     // também vazio
    return x / 2;                                             // exemplo simplificado
}

int main() {
    std::vector<std::string> nomes{"Ana", "Bia", "Caio"};

    if (auto i = acha_indice(nomes, "Bia")) std::cout << "achou em " << *i << '\n';   // operator bool, operator*
    else std::cout << "não achou\n";

    auto r = acha_indice(nomes, "Zé");
    std::cout << r.has_value() << ' ' << r.value_or(-1) << '\n';   // 0 -1

    // value() lança std::bad_optional_access se vazio
    try { std::cout << r.value(); } catch (const std::bad_optional_access&) { std::cout << "vazio!\n"; }

    std::optional<std::string> s;                             // vazio
    s = "olá";
    s.emplace("construído no lugar");
    s.reset();                                                // volta a vazio

    std::cout << raiz(-1).has_value() << raiz(8).value() << '\n';   // 04
}
```

## Quando usar

| Situação | Use |
|---|---|
| Retorno que **pode não existir** (busca, parsing) sem ser erro | `std::optional<T>` |
| Parâmetro opcional **por valor** | `std::optional<T>` (para tipos pequenos) |
| Membro opcional | `std::optional<T>` |
| Ausência com **motivo** (erro) | [[expected]] (C++23) ou exceções |
| Posse/polimorfismo/ponteiros | `unique_ptr`, `T*` |

## Custo

`sizeof(optional<T>)` ≈ `sizeof(T)` + 1 flag (com *padding*). Sem alocação dinâmica.

> [!danger] Desreferenciar `optional` vazio é UB
> ```cpp
> std::optional<int> o;
> int x = *o;          // COMPORTAMENTO INDEFINIDO (operator* não verifica)
> int y = o.value();   // seguro: lança bad_optional_access
> ```
> Teste antes (`if (o)`) ou use `value_or`.

> [!warning] `optional<bool>` e `optional<T&>`
> `if (opt)` testa **presença**, não o valor `bool`. `optional<T&>` não é permitido (C++26 adiciona suporte a referências); use `std::reference_wrapper<T>` ou `T*`.

## Operações monádicas (C++23)

```cpp
// [nv] g++ -std=c++23 -Wall -Wextra
#include <iostream>
#include <optional>
#include <string>

std::optional<int> parse(const std::string& s) {
    try { return std::stoi(s); } catch (...) { return std::nullopt; }
}

int main() {
    auto resultado = parse("21")
        .transform([](int x) { return x * 2; })           // aplica se houver valor: optional<int>
        .and_then([](int x) -> std::optional<int> { return x > 10 ? std::optional{x} : std::nullopt; })
        .or_else([] { return std::optional<int>{0}; });    // valor alternativo se vazio
    std::cout << *resultado << '\n';                       // 42
}
```

## Veja também

- [[variant]]
- [[expected]]
- [[Tratamento de Erros com expected]]
- [[Ponteiros]]

## Exercício

1. Escreva `std::optional<int> para_int(std::string_view)` com `std::from_chars` e use-a para somar uma lista de strings numéricas ignorando as inválidas.
2. Por que `optional<T>` é preferível a retornar `T*` apontando para um membro estático?
