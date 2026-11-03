---
titulo: "Locale"
tags: [cpp, io]
aliases: ["std::locale", "locale", "Internacionalização", "imbue", "facet"]
tipo: conceito
nivel: avancado
padrao: C++98
criado: 2026-10-24
relacionados: ["[[Streams e iostream]]", "[[Unicode e Codificações]]", "[[Formatação std format e std print]]"]
---

# Locale

Um **locale** reúne regras culturais: separador decimal, agrupamento de milhares, formato de data/moeda, classificação de caracteres. Em C++ é `std::locale` (composto de *facets*); em C, `setlocale`.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <locale>
#include <sstream>

// Facet que usa vírgula decimal e ponto para milhares
struct PtBR : std::numpunct<char> {
    char do_decimal_point() const override { return ','; }
    char do_thousands_sep() const override { return '.'; }
    std::string do_grouping() const override { return "\3"; }
};

int main() {
    std::ostringstream os;
    os.imbue(std::locale(std::locale::classic(), new PtBR));   // a locale assume a posse do facet
    os << 1234567.89;
    std::cout << os.str() << '\n';                              // 1.234.567,89

    std::cout.imbue(std::locale::classic());                    // locale "C": neutro e previsível
    std::cout << 1234.5 << '\n';                                // 1234.5
}
```

> [!info] Locales do sistema
> `std::locale("pt_BR.UTF-8")` lança `std::runtime_error` se o locale não estiver instalado. `std::locale("")` usa o ambiente do usuário. Disponibilidade e nomes variam por plataforma.

## Quando importa

| Situação | Cuidado |
|---|---|
| Serializar números (JSON, CSV, protocolos) | Use o locale **clássico** (`"C"`) para não trocar `.` por `,` |
| `std::format` | Por padrão **independe** do locale; use `{:L}` para ativá-lo |
| `std::to_string`, `printf` | Dependem do locale **C** global (`setlocale`) |
| `std::from_chars`/`to_chars` | **Independentes** de locale, rápidas: ideais para protocolos |

> [!warning] Global é perigoso
> `std::locale::global(...)` e `setlocale` afetam todo o programa (e threads). Prefira `imbue` em streams específicas.

## Veja também

- [[Streams e iostream]]
- [[Unicode e Codificações]]
- [[Formatação std format e std print]]
- [[Serialização]]

## Exercício

1. Imprima um valor monetário com agrupamento brasileiro usando um facet próprio.
2. Mostre o bug causado por `setlocale(LC_ALL, "pt_BR.UTF-8")` ao gerar um arquivo CSV com `printf("%f")`.
