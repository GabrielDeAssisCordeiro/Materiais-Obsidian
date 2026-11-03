---
titulo: "clang-format"
tags: [cpp, ferramentas, formatacao]
aliases: ["clang-format", ".clang-format", "Formatação de código", "Estilo de código", "git-clang-format"]
tipo: ferramenta
nivel: iniciante
padrao: C++11
criado: 2026-10-24
relacionados: ["[[clang-tidy e cppcheck]]", "[[CI e CD para Cpp]]", "[[Convenções - Cpp]]"]
---

# clang-format

Formata automaticamente o código segundo um estilo configurável, encerrando discussões de estilo em revisões de código.

```yaml
# .clang-format
BasedOnStyle: Google          # LLVM, Google, Chromium, Mozilla, WebKit, Microsoft, GNU
IndentWidth: 4
ColumnLimit: 100
AccessModifierOffset: -4
PointerAlignment: Left
IncludeBlocks: Regroup
SortIncludes: CaseSensitive
AllowShortFunctionsOnASingleLine: Inline
```

```bash
clang-format --dump-config -style=Google > .clang-format    # ponto de partida
clang-format -i src/*.cpp include/**/*.hpp                   # formatar no lugar
clang-format --dry-run --Werror src/main.cpp                 # verificar (para CI): falha se mudar algo
git clang-format HEAD~1                                      # só as linhas alteradas
```

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>

// clang-format off
int matriz[3][3] = { {1, 0, 0},
                     {0, 1, 0},
                     {0, 0, 1} };      // trecho que mantemos manualmente alinhado
// clang-format on

int main() { std::cout << matriz[1][1] << '\n'; }
```

> [!tip] Integração
> - **Editor**: formatar ao salvar (VS Code, CLion, Vim, Visual Studio).
> - **pre-commit**: hook que roda `clang-format` nos arquivos modificados.
> - **CI**: bloqueia PR não formatado ([[CI e CD para Cpp]]).
> - Formate o repositório **uma vez** em um commit separado e registre-o em `.git-blame-ignore-revs`.

> [!info] Alternativas
> `uncrustify`, `astyle`. Para organização de includes, **include-what-you-use** (IWYU) complementa.

## Veja também

- [[clang-tidy e cppcheck]]
- [[CI e CD para Cpp]]
- [[Core Guidelines]]
- [[Convenções - Cpp]]

## Exercício

1. Escolha um estilo, formate um projeto e configure o hook de pre-commit.
2. Use `// clang-format off/on` para proteger uma tabela alinhada.
