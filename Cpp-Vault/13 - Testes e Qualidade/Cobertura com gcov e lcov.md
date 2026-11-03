---
titulo: "Cobertura de código: gcov, lcov e llvm-cov"
tags: [cpp, testes]
aliases: ["Cobertura de código", "gcov", "lcov", "gcovr", "llvm-cov", "--coverage"]
tipo: ferramenta
nivel: intermediario
padrao: C++11
criado: 2026-10-24
relacionados: ["[[GoogleTest]]", "[[CI e CD para Cpp]]", "[[Fundamentos de Testes Unitários]]"]
---

# Cobertura de código: gcov, lcov e llvm-cov

**Cobertura** mede quanto do código foi executado pelos testes: linhas, ramos (*branches*), funções.

> [!warning] Cobertura alta ≠ testes bons
> 100% de linhas não garante que os resultados sejam **verificados**. Use como indicador para achar código não testado, não como meta absoluta.

```cpp
// g++ -std=c++20 -Wall -Wextra --coverage -O0
#include <iostream>

int classificar(int n) {
    if (n < 0) return -1;
    if (n == 0) return 0;
    return 1;                    // o teste abaixo só chama com n > 0 → ramos negativos ficam descobertos
}

int main() {
    std::cout << classificar(5) << '\n';
}
```

## GCC: gcov + lcov/gcovr

```bash
g++ -std=c++20 --coverage -O0 -g prog.cpp -o prog   # gera instrumentação (.gcno)
./prog                                              # gera dados de execução (.gcda)
gcov prog-prog.gcda                                 # relatório textual (.gcov) - o nome pode variar
lcov --capture --directory . --output-file cov.info
lcov --remove cov.info '/usr/*' '*/tests/*' --output-file cov.info
genhtml cov.info --output-directory cobertura_html  # abre cobertura_html/index.html

gcovr -r . --html-details -o cobertura.html --branches   # alternativa mais simples
```

## Clang: llvm-cov

```bash
clang++ -std=c++20 -fprofile-instr-generate -fcoverage-mapping -O0 prog.cpp -o prog
LLVM_PROFILE_FILE=prog.profraw ./prog
llvm-profdata merge -sparse prog.profraw -o prog.profdata
llvm-cov show ./prog -instr-profile=prog.profdata -format=html -output-dir=cov_html
llvm-cov report ./prog -instr-profile=prog.profdata
```

```cmake
option(ENABLE_COVERAGE "Cobertura" OFF)
if(ENABLE_COVERAGE)
  add_compile_options(--coverage -O0 -g)
  add_link_options(--coverage)
endif()
```

> [!tip] Boas práticas
> - Compile a cobertura com `-O0` para linhas confiáveis.
> - Exclua código de terceiros e testes do relatório.
> - Publique o relatório na CI (Codecov, Coveralls) e **falhe** se a cobertura *cair* em um PR, em vez de exigir um número mágico.
> - Cobertura de **ramos** é mais informativa que de linhas.

## Veja também

- [[GoogleTest]]
- [[CI e CD para Cpp]]
- [[Fundamentos de Testes Unitários]]
- [[Fuzzing]]

## Exercício

1. Gere o relatório HTML do exemplo, adicione testes e veja os ramos ficarem cobertos.
2. Configure um alvo CMake `coverage` que executa os testes e gera o HTML.
