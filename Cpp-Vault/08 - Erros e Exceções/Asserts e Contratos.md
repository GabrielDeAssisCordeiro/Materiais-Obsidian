---
titulo: "Asserts e contratos"
tags: [cpp, erros, static_assert, contratos, cpp26]
aliases: ["assert", "Contratos", "contract_assert", "NDEBUG", "Pré-condições", "Pós-condições"]
tipo: conceito
nivel: intermediario
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Tratamento de Erros com expected]]", "[[Cpp26 Visão Geral]]", "[[Comportamento Indefinido e Não Especificado]]"]
---

# Asserts e contratos

Nem todo erro merece exceção. **Bugs de programação** (pré-condições violadas pelo próprio código) devem ser detectados e **interromper** o programa o mais cedo possível, não "tratados".

## `assert` (tempo de execução)

`assert(cond)` (`<cassert>`) aborta com mensagem se `cond` for falsa — **desativado** se `NDEBUG` estiver definido (builds de *release*).

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <cassert>
#include <iostream>
#include <vector>

double media(const std::vector<double>& v) {
    assert(!v.empty() && "media() exige vetor não vazio");   // pré-condição; a string dá contexto
    double s = 0;
    for (double x : v) s += x;
    return s / v.size();
}

int main() {
    std::cout << media({1, 2, 3}) << '\n';                    // 2
    // media({});                                             // aborta em debug
}
```

> [!warning] `assert` some em release
> **Nunca** coloque efeitos colaterais dentro (`assert(f())` não chama `f` com `NDEBUG`). E **não use** `assert` para validar **entrada externa** (usuário, arquivo, rede): isso é erro **esperado** — trate-o.

## `static_assert` (tempo de compilação)

Verifica condições **constantes** durante a compilação; falha impede o build (veja [[static_assert e Type Traits]]).

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <cstdint>
#include <type_traits>

struct Cabecalho { std::uint32_t id; std::uint16_t tamanho; std::uint16_t flags; };

static_assert(sizeof(Cabecalho) == 8, "Cabecalho deve ter 8 bytes");
static_assert(std::is_trivially_copyable_v<Cabecalho>);
static_assert(sizeof(void*) == 8, "esperado 64 bits");

int main() {}
```

## Contratos (C++26)

> [!info] Introdução
> **C++26** (P2900): pré-condições (`pre`), pós-condições (`post`) e asserções (`contract_assert`) como **parte da linguagem**. GCC 16.1 tem implementação (flags/semânticas a confirmar).
> [!question] Verificar na documentação oficial
> Sintaxe final, semânticas de avaliação (*ignore*, *observe*, *enforce*, *quick_enforce*) e flags do compilador. Os blocos abaixo estão como não verificados.

```cpp
// [nv] g++-16 -std=c++26 -fcontracts   (confirmar flags no manual do GCC 16)
#include <vector>

double media(const std::vector<double>& v)
    pre(!v.empty())                       // pré-condição: responsabilidade do chamador
    post(r : r == r)                      // pós-condição ilustrativa: 'r' nomeia o valor retornado (não é NaN)
{
    double s = 0;
    for (double x : v) s += x;
    contract_assert(v.size() > 0);        // asserção no corpo
    return s / v.size();
}
```

Vantagens sobre `assert`: fazem parte da **interface** (visíveis ao chamador e a ferramentas), têm **semântica configurável** por build e podem ser verificadas por análise estática.

## Quando usar cada mecanismo

| Situação | Mecanismo |
|---|---|
| Condição constante que **deve** valer (tamanho, traits) | `static_assert` |
| Pré/pós-condição que indica **bug** | `assert` / contratos |
| Entrada **inválida do usuário** | `expected`, `optional`, exceção |
| Falha de recurso (rede, disco) | Exceção / `expected` / `error_code` |
| Estado impossível | `std::unreachable()` (C++23) — **UB** se alcançado; use com cuidado |

> [!danger] `std::unreachable()` e `[[assume(cond)]]` (C++23)
> Prometem ao compilador que o ponto não é alcançado / a condição é verdadeira. Se a promessa falhar: **comportamento indefinido**. Use apenas com certeza e proteja com `assert` em debug.

## Boas práticas

- Defina uma macro própria (`MEU_ASSERT`) para controlar mensagem, *log* e política (abortar, lançar em testes).
- Mantenha **assertivas ativas em CI** (builds de teste sem `NDEBUG`).
- Combine com **sanitizers** e a biblioteca padrão em modo *hardened*.

## Veja também

- [[static_assert e Type Traits]]
- [[Tratamento de Erros com expected]]
- [[Cpp26 Visão Geral]]
- [[Comportamento Indefinido e Não Especificado]]
- [[Boas Práticas e Custo das Exceções]]

## Exercício

1. Escreva uma função `fatia(span, i, n)` com `assert` para todas as pré-condições e uma versão que lança `std::out_of_range`; discuta quando cada uma é apropriada.
2. Adicione `static_assert` para garantir que `sizeof(Pacote)` é 16 em todas as plataformas suportadas.
