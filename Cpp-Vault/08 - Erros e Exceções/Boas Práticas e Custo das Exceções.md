---
titulo: "Boas práticas e custo das exceções"
tags: [cpp, erros, excecoes, boas-praticas, desempenho]
aliases: ["Custo das exceções", "Exceções são lentas?", "Zero-cost exceptions", "-fno-exceptions"]
tipo: guia
nivel: avancado
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Exceções try catch throw]]", "[[Segurança de Exceções]]", "[[Tratamento de Erros com expected]]"]
---

# Boas práticas e custo das exceções

## Como as exceções são implementadas

Os principais compiladores usam o modelo de **tabelas** (*zero-cost exceptions*, ABI Itanium; no MSVC x64 também por tabelas):

| Cenário | Custo |
|---|---|
| **Caminho feliz** (nada é lançado) | Praticamente **zero** em tempo; algum aumento do **binário** (tabelas de desenrolamento) |
| **`throw` + `catch`** | **Alto**: da ordem de **microssegundos** (centenas a milhares de vezes uma chamada comum) devido à busca de handlers e desenrolamento |
| Otimização | Código com `try` pode limitar algumas otimizações |

> [!info] Consequência prática
> Exceções são **excelentes** para falhas **raras**; péssimas como fluxo de controle para eventos **frequentes** (por exemplo, "linha inválida" em um arquivo de milhões de linhas). Nesses casos use [[Tratamento de Erros com expected|expected]] ou códigos de erro.

```cpp
// g++ -std=c++20 -O2 -Wall -Wextra
#include <chrono>
#include <iostream>
#include <stdexcept>

int com_excecao(int x) { if (x % 2) throw std::runtime_error("ímpar"); return x; }
int com_codigo(int x, bool& erro) { erro = x % 2; return erro ? 0 : x; }

int main() {
    using clock = std::chrono::steady_clock;
    constexpr int N = 200'000;
    long soma = 0;

    auto t0 = clock::now();
    for (int i = 0; i < N; ++i) {
        try { soma += com_excecao(i); } catch (const std::exception&) {}
    }
    auto t1 = clock::now();
    for (int i = 0; i < N; ++i) { bool e; soma += com_codigo(i, e); }
    auto t2 = clock::now();

    auto ms = [](auto a, auto b) { return std::chrono::duration_cast<std::chrono::milliseconds>(b - a).count(); };
    std::cout << "exceções: " << ms(t0, t1) << " ms | códigos: " << ms(t1, t2) << " ms | " << soma << '\n';
}
```

(Meça na sua máquina: com 50% de erros, a versão com exceções costuma ser ordens de grandeza mais lenta.)

## Quando usar exceções

| Use | Evite |
|---|---|
| Falha de **construtor** (sem valor de retorno possível) | Fluxo normal (fim de laço, "não encontrado" esperado) |
| Erros **inesperados** e difíceis de tratar localmente | Hot paths com erro frequente |
| Propagar por **várias camadas** sem poluir o código | Código que roda em ambientes sem suporte (`-fno-exceptions`) |
| Violação de invariantes **recuperável** | Tempo real *hard* (previsibilidade) |

## Regras de ouro

1. **RAII em tudo** — a base da segurança de exceções ([[Segurança de Exceções]]).
2. **Lance por valor, capture por `const&`.**
3. **Destrutores e `swap`**: `noexcept`.
4. **Capture onde puder tratar**, não "só por capturar": evite `catch (...) {}` que engole erros.
5. **Não use *exception specifications* dinâmicas** (`throw(int)`): removidas no C++17.
6. **Mensagens úteis**: o que falhou, com quais dados, onde (`std::source_location`, C++20).
7. **Defina uma política** por módulo (lança / não lança) e documente.
8. **`main` com rede de segurança**:

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <exception>
#include <iostream>
#include <stdexcept>

int executa();                                            // sua lógica

int main() try {
    return executa();
} catch (const std::exception& e) {
    std::cerr << "erro fatal: " << e.what() << '\n';
    return 1;
} catch (...) {
    std::cerr << "erro fatal desconhecido\n";
    return 2;
}

int executa() { throw std::runtime_error("exemplo"); }
```

## Exceções desativadas

Alguns projetos compilam com **`-fno-exceptions`** (jogos, embarcados, kernels, Chromium, LLVM). Efeitos:

- `throw` vira erro de compilação; a biblioteca padrão chama `std::abort`/`terminate` onde lançaria.
- Todos os erros precisam de códigos/`expected`.
- Bibliotecas que dependem de exceções (partes da STL, Boost) podem não funcionar.

> [!warning] RTTI e exceções
> `-fno-rtti` e `-fno-exceptions` reduzem o binário, mas restringem bibliotecas. Verifique a compatibilidade antes de adotar.

## Resumo de decisão

| Pergunta | Resposta |
|---|---|
| É bug do programador? | `assert`/contrato |
| Falha **esperada e frequente**? | `expected`/`error_code` |
| Falha **rara e excepcional**? | Exceção |
| Fora de controle (hardware, memória)? | Exceção/terminate, conforme o projeto |
| Interface com C? | Códigos de erro, nunca deixe exceções cruzarem a fronteira |

> [!danger] Exceção atravessando `extern "C"` ou *callbacks* de C
> Lançar exceções por funções C/`qsort`/`pthread` callbacks é **UB**. Capture na fronteira e converta em código de erro.

## Veja também

- [[Exceções try catch throw]]
- [[Segurança de Exceções]]
- [[Tratamento de Erros com expected]]
- [[Asserts e Contratos]]
- [[Hierarquia de Exceções]]

## Exercício

1. Repita o benchmark com 0,1%, 1% e 50% de falhas e trace a curva de tempo vs. taxa de erro.
2. Escreva as diretrizes de erro de um projeto fictício (qual mecanismo em cada camada) em uma página.
