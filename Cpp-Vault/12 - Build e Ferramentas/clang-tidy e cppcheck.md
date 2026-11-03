---
titulo: "Análise estática: clang-tidy e cppcheck"
tags: [cpp, ferramentas]
aliases: ["clang-tidy", "cppcheck", "Análise estática", ".clang-tidy", "clangd"]
tipo: ferramenta
nivel: intermediario
padrao: C++11
criado: 2026-10-24
relacionados: ["[[clang-format]]", "[[Core Guidelines]]", "[[CMake Moderno e Presets]]"]
---

# Análise estática: clang-tidy e cppcheck

Analisam o **código-fonte** (sem executar) em busca de bugs, más práticas e oportunidades de modernização.

| Ferramenta | Característica |
|---|---|
| **clang-tidy** | Baseado no AST do Clang; checks por prefixo: `bugprone-`, `modernize-`, `performance-`, `readability-`, `cppcoreguidelines-`, `clang-analyzer-`, `misc-`; muitos têm **fix automático** |
| **cppcheck** | Independente de compilador; foco em poucos falsos positivos; boa para código legado; suporta regras MISRA (versão premium) |
| **Compilador** | `-Wall -Wextra -Wpedantic -Wconversion -Wshadow` (e `-fanalyzer` no GCC) |
| **clangd** | Servidor de linguagem; roda clang-tidy no editor |
| Comerciais | PVS-Studio, Coverity, SonarQube, Klocwork |

```yaml
# .clang-tidy
Checks: >
  -*,bugprone-*,performance-*,modernize-*,readability-*,cppcoreguidelines-*,
  -modernize-use-trailing-return-type,-readability-magic-numbers
WarningsAsErrors: 'bugprone-*'
HeaderFilterRegex: '^(include|src)/.*'
```

```cpp
// g++ -std=c++20 -Wall -Wextra
// Exemplo que o clang-tidy criticaria (compila normalmente):
//  - modernize-loop-convert, performance-for-range-copy, bugprone-narrowing-conversions
#include <iostream>
#include <string>
#include <vector>

int main() {
    std::vector<std::string> nomes{"Ana", "Bia"};
    for (std::string n : nomes)               // cópia desnecessária → use const std::string&
        std::cout << n << '\n';
    for (unsigned i = 0; i < nomes.size(); ++i)   // modernize-loop-convert → range-for
        std::cout << nomes[i] << '\n';
}
```

```bash
# Requer compile_commands.json (cmake -DCMAKE_EXPORT_COMPILE_COMMANDS=ON)
clang-tidy -p build src/*.cpp
clang-tidy -p build --fix --checks='modernize-*' src/main.cpp   # aplica correções automáticas (revise o diff!)
run-clang-tidy -p build -j4                                    # script paralelo
cppcheck --enable=warning,performance,portability --std=c++20 --project=build/compile_commands.json
```

```cmake
set(CMAKE_CXX_CLANG_TIDY clang-tidy -p ${CMAKE_BINARY_DIR})   # roda em cada compilação (mais lento)
```

> [!warning] Cuidados
> - Falsos positivos existem: desative checks específicos em vez de todo o linter, ou use `// NOLINT(check-name)` com justificativa.
> - `--fix` pode alterar semântica sutil: revise e compile/teste depois.
> - Comece com poucos checks e **aumente gradualmente** em código legado.

## Veja também

- [[clang-format]]
- [[Core Guidelines]]
- [[Sanitizers]]
- [[Flags Essenciais do Compilador]]
- [[CMake Moderno e Presets]]

## Exercício

1. Rode `clang-tidy` com `modernize-*` em um projeto antigo e aplique um fix; revise o diff.
2. Compare o que cppcheck e clang-tidy encontram no mesmo arquivo.
