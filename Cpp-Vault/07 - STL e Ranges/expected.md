---
titulo: "std::expected"
tags: [cpp, stl, expected, erros, cpp23, vocabulary-types]
aliases: ["std::expected", "expected", "Resultado ou erro", "unexpected", "Result type"]
tipo: conceito
nivel: intermediario
padrao: C++23
criado: 2026-10-24
relacionados: ["[[optional]]", "[[Tratamento de Erros com expected]]", "[[Exceções try catch throw]]"]
---

# `std::expected`

> [!info] Introdução
> **C++23** (`<expected>`). Suporte: GCC 12+, Clang 16+ (libc++), MSVC 2022 17.3+. Equivalente ao `Result<T, E>` de Rust e ao `Either` funcional.
> [!question] Verificar na documentação oficial
> Confirme as operações monádicas (`and_then`, `transform`, `or_else`, `transform_error`) no seu compilador; elas vieram com o C++23 completo (GCC 13+).

`std::expected<T, E>` guarda **ou** um valor esperado `T` **ou** um erro `E` — **por valor**, sem exceções.

```cpp
// g++ -std=c++23 -Wall -Wextra
#include <charconv>
#include <expected>
#include <iostream>
#include <string>
#include <string_view>
#include <system_error>

enum class ErroParse { vazio, invalido, fora_do_intervalo };

std::expected<int, ErroParse> parse_int(std::string_view s) {
    if (s.empty()) return std::unexpected(ErroParse::vazio);
    int valor{};
    auto [fim, ec] = std::from_chars(s.data(), s.data() + s.size(), valor);
    if (ec == std::errc::result_out_of_range) return std::unexpected(ErroParse::fora_do_intervalo);
    if (ec != std::errc{} || fim != s.data() + s.size()) return std::unexpected(ErroParse::invalido);
    return valor;
}

int main() {
    for (std::string_view txt : {"123", "", "12x", "99999999999"}) {
        auto r = parse_int(txt);
        if (r) std::cout << "ok: " << *r << '\n';
        else   std::cout << "erro " << static_cast<int>(r.error()) << '\n';
    }

    std::cout << parse_int("7").value_or(-1) << parse_int("x").value_or(-1) << '\n';   // 7-1
}
```

## Operações principais

| Operação | Significado |
|---|---|
| `if (r)` / `r.has_value()` | Tem valor? |
| `*r`, `r.value()` | Valor (`value()` lança `bad_expected_access` se erro) |
| `r.error()` | Erro (UB se tiver valor) |
| `r.value_or(x)` | Valor ou padrão |
| `std::unexpected(e)` | Constrói o estado de erro |
| `r.and_then(f)` | Encadeia `f` (que retorna `expected`) se houver valor |
| `r.transform(f)` | Mapeia o valor |
| `r.or_else(f)` | Trata o erro (pode recuperar) |
| `r.transform_error(f)` | Mapeia o tipo do erro |

## Encadeamento sem `if` aninhados

```cpp
// [nv] g++ -std=c++23 -Wall -Wextra   (operações monádicas exigem GCC 13+/libstdc++ 13+)
#include <expected>
#include <iostream>
#include <string>

std::expected<int, std::string> dobra(int x) {
    if (x > 100) return std::unexpected("grande demais");
    return x * 2;
}
std::expected<int, std::string> menos_um(int x) {
    if (x == 0) return std::unexpected("zero");
    return x - 1;
}

int main() {
    auto r = dobra(10).and_then(menos_um).transform([](int v) { return v * 10; });
    std::cout << r.value_or(-1) << '\n';                 // 190

    auto e = dobra(500).and_then(menos_um);
    std::cout << e.error() << '\n';                      // grande demais (curto-circuito)
}
```

## `expected` vs `optional` vs exceções

| | `optional<T>` | `expected<T, E>` | Exceções |
|---|---|---|---|
| Informa **motivo**? | Não | **Sim** | Sim |
| Custo no caminho feliz | Mínimo | Mínimo | Mínimo (zero-cost model) |
| Custo no erro | Mínimo | Mínimo | **Alto** (desenrolamento) |
| Obriga o chamador a tratar | Não (mas visível no tipo) | Não (visível no tipo; `[[nodiscard]]` ajuda) | Propaga automaticamente |
| Bom para | Ausência esperada | Falhas **esperadas e frequentes** (parsing, E/S, validação) | Falhas **excepcionais** |

> [!tip] Marque funções com `[[nodiscard]]`
> Ignorar um `expected` perde o erro. Declare `[[nodiscard]] std::expected<...> f();` ou o tipo como `[[nodiscard]]`.

> [!warning] `.error()` sem checar é UB
> Chame `error()` somente quando `!r`. Em dúvida, use `value()`/`and_then`.

Veja o uso em estratégia de erros em [[Tratamento de Erros com expected]].

## Veja também

- [[optional]]
- [[Tratamento de Erros com expected]]
- [[Exceções try catch throw]]
- [[Códigos de Erro e error_code]]
- [[variant]]

## Exercício

1. Escreva `std::expected<Config, std::string> carrega(const std::string& caminho)` que valida cada campo e retorna o primeiro erro.
2. Converta uma função que lança `std::invalid_argument` para retornar `expected` e compare o código do chamador.
