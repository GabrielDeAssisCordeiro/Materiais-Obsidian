---
titulo: "gMock e dublês de teste"
tags: [cpp, testes]
aliases: ["gMock", "GoogleMock", "Stub", "Spy", "Dublês de teste", "MOCK_METHOD"]
tipo: conceito
nivel: intermediario
padrao: C++14
criado: 2026-10-24
relacionados: ["[[GoogleTest]]", "[[Classes Abstratas e Interfaces]]", "[[Polimorfismo e Funções Virtuais]]"]
---

# gMock e dublês de teste

Para testar uma unidade **isolada** de suas dependências (banco, rede, relógio), substituímos essas dependências por **dublês**.

| Dublê | O que faz |
|---|---|
| **Dummy** | Preenche parâmetro; nunca usado |
| **Stub** | Retorna respostas fixas |
| **Fake** | Implementação simplificada funcional (banco em memória) |
| **Spy** | Grava chamadas para verificação posterior |
| **Mock** | Define **expectativas** de chamadas e as verifica |

## Primeiro: projete para substituição

O código precisa depender de uma **interface** ([[Classes Abstratas e Interfaces]]), injetada no construtor.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <memory>
#include <string>

struct Relogio { virtual ~Relogio() = default; virtual int hora() const = 0; };

class Saudacao {
public:
    explicit Saudacao(const Relogio& r) : relogio_{r} {}      // injeção de dependência
    std::string dizer() const {
        int h = relogio_.hora();
        return h < 12 ? "Bom dia" : (h < 18 ? "Boa tarde" : "Boa noite");
    }
private:
    const Relogio& relogio_;
};

struct RelogioFalso : Relogio {                                 // um "fake/stub" escrito à mão
    explicit RelogioFalso(int h) : h_{h} {}
    int hora() const override { return h_; }
    int h_;
};

int main() {
    std::cout << Saudacao{RelogioFalso{9}}.dizer() << ' ' << Saudacao{RelogioFalso{20}}.dizer() << '\n';
}
```

## Com gMock

```cpp
// [nv] g++ -std=c++20 -Wall -Wextra -lgmock -lgtest -lgtest_main -pthread   (requer GoogleTest/gMock; indisponível no ambiente de teste do vault)
#include <gmock/gmock.h>
#include <gtest/gtest.h>
#include <string>

struct Relogio { virtual ~Relogio() = default; virtual int hora() const = 0; };

class RelogioMock : public Relogio {
public:
    MOCK_METHOD(int, hora, (), (const, override));
};

std::string saudar(const Relogio& r) { return r.hora() < 12 ? "Bom dia" : "Boa noite"; }

using ::testing::Return;

TEST(Saudacao, Manha) {
    RelogioMock relogio;
    EXPECT_CALL(relogio, hora()).Times(1).WillOnce(Return(8));   // expectativa: 1 chamada retornando 8
    EXPECT_EQ(saudar(relogio), "Bom dia");
}
```

> [!warning] Mocks em excesso
> Testes cheios de mocks acoplam-se à **implementação** e quebram em refatorações. Prefira **fakes** e testes sobre o **comportamento** observável. Use mocks para fronteiras (rede, disco, tempo).

> [!tip] Sem virtuais?
> Se não quiser `virtual`, injete por **template** (`template <typename Relogio> class Saudacao`) ou `std::function` — [[std function e Functors]]. O custo do polimorfismo estático é zero ([[Templates de Classe]]).

## Veja também

- [[GoogleTest]]
- [[Classes Abstratas e Interfaces]]
- [[Polimorfismo e Funções Virtuais]]
- [[std function e Functors]]

## Exercício

1. Teste uma classe `Notificador` que depende de `EnviadorEmail` usando um mock.
2. Refatore o `Saudacao` para receber o relógio por template e compare.
