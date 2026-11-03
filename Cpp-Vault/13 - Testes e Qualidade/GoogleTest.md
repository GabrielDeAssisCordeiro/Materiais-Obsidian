---
titulo: "GoogleTest"
tags: [cpp, testes, framework]
aliases: ["GoogleTest", "gtest", "TEST", "TEST_F", "TEST_P", "EXPECT_EQ"]
tipo: biblioteca
nivel: iniciante
padrao: C++14
criado: 2026-10-24
relacionados: ["[[Fundamentos de Testes Unitários]]", "[[gMock e Dublês de Teste]]", "[[CMake Moderno e Presets]]"]
---

# GoogleTest

Framework de testes unitários do Google (inclui **GoogleMock**). Versões recentes exigem C++17 (confirmar a versão mínima atual no repositório).

| Macro | Função |
|---|---|
| `TEST(Suite, Nome)` | Teste simples |
| `TEST_F(Fixture, Nome)` | Teste com **fixture** (`SetUp`/`TearDown`) |
| `TEST_P` + `INSTANTIATE_TEST_SUITE_P` | Teste **parametrizado** |
| `EXPECT_*` | Falha **não fatal** (continua) |
| `ASSERT_*` | Falha **fatal** (aborta o teste) |
| `EXPECT_THROW`, `EXPECT_NEAR`, `EXPECT_DEATH` | Exceções, float, morte do processo |

```cpp
// [nv] g++ -std=c++20 -Wall -Wextra -lgtest -lgtest_main -pthread   (requer GoogleTest instalado; indisponível no ambiente de teste do vault)
#include <gtest/gtest.h>
#include <stdexcept>
#include <vector>

int dividir(int a, int b) {
    if (b == 0) throw std::invalid_argument{"divisão por zero"};
    return a / b;
}

TEST(Divisao, CasoNormal) {
    EXPECT_EQ(dividir(10, 2), 5);
    EXPECT_NE(dividir(10, 3), 4);
}

TEST(Divisao, PorZeroLancaExcecao) {
    EXPECT_THROW(dividir(1, 0), std::invalid_argument);
}

class PilhaTest : public ::testing::Test {
protected:
    void SetUp() override { v = {1, 2, 3}; }
    std::vector<int> v;
};

TEST_F(PilhaTest, TamanhoInicial) { ASSERT_EQ(v.size(), 3u); EXPECT_EQ(v.back(), 3); }

class ParesTest : public ::testing::TestWithParam<int> {};
TEST_P(ParesTest, EhPar) { EXPECT_EQ(GetParam() % 2, 0); }
INSTANTIATE_TEST_SUITE_P(Valores, ParesTest, ::testing::Values(2, 4, 100));
```

```cmake
include(FetchContent)
FetchContent_Declare(googletest URL https://github.com/google/googletest/archive/refs/tags/v1.15.2.zip)
FetchContent_MakeAvailable(googletest)

enable_testing()
add_executable(testes testes.cpp)
target_link_libraries(testes PRIVATE GTest::gtest_main)

include(GoogleTest)
gtest_discover_tests(testes)       # registra cada TEST como um teste do CTest
```

```bash
./testes --gtest_filter='Divisao.*' --gtest_repeat=10 --gtest_shuffle
```

> [!tip] Boas práticas
> - Prefira `EXPECT` (vê todos os erros); use `ASSERT` quando continuar não faz sentido.
> - `EXPECT_EQ(valor_obtido, valor_esperado)` (ordem consistente para boas mensagens).
> - Rode com `--gtest_shuffle` para detectar dependência de ordem.
> - Use [[Sanitizers]] ao executar a suíte.

> [!question] Verificar na documentação oficial
> Tags de versão e requisitos de padrão (`GIT_TAG`) mudam; confira em github.com/google/googletest.

## Veja também

- [[Fundamentos de Testes Unitários]]
- [[gMock e Dublês de Teste]]
- [[Catch2 e doctest]]
- [[Cobertura com gcov e lcov]]

## Exercício

1. Teste uma classe `Pilha` com fixture e testes parametrizados.
2. Gere um relatório XML (`--gtest_output=xml`) e consuma na CI.
