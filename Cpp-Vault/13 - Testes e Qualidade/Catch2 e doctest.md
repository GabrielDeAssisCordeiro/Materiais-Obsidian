---
titulo: "Catch2 e doctest"
tags: [cpp, testes, framework]
aliases: ["Catch2", "doctest", "TEST_CASE", "SECTION", "REQUIRE", "CHECK", "BDD"]
tipo: biblioteca
nivel: iniciante
padrao: C++14
criado: 2026-10-24
relacionados: ["[[GoogleTest]]", "[[Fundamentos de Testes Unitários]]", "[[Google Benchmark]]"]
---

# Catch2 e doctest

Alternativas modernas ao [[GoogleTest]], sem *fixtures* como classes: usam `TEST_CASE` e `SECTION`.

| | **Catch2 v3** | **doctest** |
|---|---|---|
| Distribuição | Biblioteca compilada (v3); *amalgamated header* removido do padrão | **Header-only** leve |
| Expressões | `REQUIRE(a == b)` decompõe a expressão e mostra os dois lados | Igual (`CHECK`, `REQUIRE`) |
| Fixtures | `SECTION` aninhadas (cada seção reexecuta o setup) | `SUBCASE` |
| Extras | Matchers, geradores (`GENERATE`), benchmarks embutidos, BDD (`SCENARIO/GIVEN/WHEN/THEN`) | Muito rápido de compilar; `DOCTEST_CONFIG_*` |
| Padrão mínimo | C++14 (v3) | C++11 |

## Catch2

```cpp
// [nv] g++ -std=c++20 -Wall -Wextra -lCatch2Main -lCatch2   (requer Catch2 v3; indisponível no ambiente de teste do vault)
#include <catch2/catch_test_macros.hpp>
#include <catch2/generators/catch_generators.hpp>
#include <vector>

TEST_CASE("vector se comporta", "[vector]") {
    std::vector<int> v{1, 2, 3};                       // setup reexecutado para cada SECTION

    SECTION("push_back aumenta o tamanho") {
        v.push_back(4);
        REQUIRE(v.size() == 4);
    }
    SECTION("clear zera") {
        v.clear();
        REQUIRE(v.empty());
    }
}

TEST_CASE("quadrados") {
    auto n = GENERATE(1, 2, 3, 4);
    REQUIRE(n * n >= n);
}

SCENARIO("pilha vazia") {
    GIVEN("uma pilha vazia") {
        std::vector<int> pilha;
        WHEN("empilhamos 1") {
            pilha.push_back(1);
            THEN("o tamanho é 1") { REQUIRE(pilha.size() == 1); }
        }
    }
}
```

## doctest

```cpp
// [nv] g++ -std=c++20 -Wall -Wextra   (requer doctest.h; indisponível no ambiente de teste do vault)
#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>

int fatorial(int n) { return n <= 1 ? 1 : n * fatorial(n - 1); }

TEST_CASE("fatorial") {
    CHECK(fatorial(0) == 1);
    CHECK(fatorial(5) == 120);
    SUBCASE("negativos") { CHECK(fatorial(-3) == 1); }
}
```

```cmake
find_package(Catch2 3 REQUIRED)
add_executable(testes testes.cpp)
target_link_libraries(testes PRIVATE Catch2::Catch2WithMain)

include(CTest)
include(Catch)
catch_discover_tests(testes)
```

> [!tip] Como escolher
> **GoogleTest**: projetos grandes, integração com gMock e ecossistema Google. **Catch2**: sintaxe expressiva e BDD. **doctest**: compilação rápida e testes no mesmo arquivo do código.

## Veja também

- [[GoogleTest]]
- [[Fundamentos de Testes Unitários]]
- [[Google Benchmark]]
- [[CMake Moderno e Presets]]

## Exercício

1. Reescreva em Catch2 os testes de uma classe feita antes com GoogleTest.
2. Use `GENERATE` para testar `eh_primo` em 10 valores.
