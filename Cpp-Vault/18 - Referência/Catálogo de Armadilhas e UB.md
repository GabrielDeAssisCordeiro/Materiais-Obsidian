---
titulo: "Catálogo de armadilhas e comportamento indefinido"
tags: [cpp, referencia, ub, seguranca]
aliases: ["Catálogo de UB", "Armadilhas de UB", "Lista de comportamento indefinido", "Undefined behavior catalog"]
tipo: referencia
nivel: avancado
padrao: C++20
criado: 2026-10-24
relacionados: ["[[Comportamento Indefinido e Não Especificado]]", "[[Sanitizers]]", "[[Segurança e Hardening]]"]
---

# Catálogo de armadilhas e comportamento indefinido

> [!danger] O que é UB
> Se o programa executa uma operação com **comportamento indefinido**, o padrão não impõe **nenhum** requisito: pode "funcionar", travar, corromper dados ou ser explorado por atacantes. O compilador **assume que UB nunca ocorre** e otimiza com base nisso ([[Otimizações do Compilador LTO e PGO]]). Para a teoria: [[Comportamento Indefinido e Não Especificado]].

| # | Armadilha | Exemplo | Como detectar / evitar |
|---|---|---|---|
| 1 | **Overflow de inteiro com sinal** | `INT_MAX + 1` | `-fsanitize=undefined`; use tipos maiores/`__builtin_*_overflow`; sem sinal faz *wrap* (definido) |
| 2 | **Acesso fora dos limites** | `v[v.size()]`, `a[10]` em `int a[10]` | ASan, `at()`, hardening (`_GLIBCXX_ASSERTIONS`), `std::span` |
| 3 | **Use-after-free / dangling** | `delete p; *p`; referência a local; `string_view` de temporário | ASan, `unique_ptr`, cuidado com views |
| 4 | **Double free / `delete` errado** | `delete` duas vezes; `delete` em vez de `delete[]` | ASan; smart pointers |
| 5 | **Desreferenciar `nullptr`** | `*p` com `p == nullptr` | `-fsanitize=null`, checagens, referências |
| 6 | **Leitura de variável não inicializada** | `int x; use(x);` | `-Wall`, MSan/Valgrind; inicialize sempre |
| 7 | **Data race** | duas threads, uma escreve | TSan, mutex/atomic ([[Data Races e Deadlocks]]) |
| 8 | **Violar strict aliasing** | `*(int*)&float_var` | `std::bit_cast`, `memcpy`; `-fno-strict-aliasing` só como mitigação |
| 9 | **Desalinhamento** | converter `char*` para `int*` desalinhado | `memcpy`, `alignas`, UBSan |
| 10 | **Shift inválido** | `1 << 32` (int de 32 bits), shift negativo | UBSan; use `1u << n` com `n < width` |
| 11 | **Divisão por zero (inteiros)** | `x / 0` | Teste o divisor |
| 12 | **Fim de função não-`void` sem `return`** | `int f() { if (c) return 1; }` | `-Wreturn-type` |
| 13 | **Invalidação de iteradores** | `for (auto x : v) v.push_back(x);` | [[Complexidade e Invalidação de Iteradores]] |
| 14 | **Modificar objeto `const`** | `const_cast` e escrever em objeto realmente const | Evite `const_cast` |
| 15 | **Violação da ODR** | Duas definições diferentes da mesma classe em TUs distintas | Sem diagnóstico; headers consistentes ([[Declaração vs Definição e ODR]]) |
| 16 | **Ordem de avaliação / efeitos colaterais** | `i = i++ + ++i;` (C++17 define algumas ordens, não todas) | Uma modificação por expressão |
| 17 | **`unsigned` em laços decrescentes** | `for (size_t i = n-1; i >= 0; --i)` | Não é UB, mas laço infinito / acesso fora |
| 18 | **Destruir objeto por ponteiro base sem destrutor virtual** | `delete base_ptr` | `virtual ~Base()` ([[Polimorfismo e Funções Virtuais]]) |
| 19 | **Chamar virtual em construtor/destrutor** | Chama a versão da classe atual, não da derivada | Não faça |
| 20 | **`memcpy` de tipos não trivialmente copiáveis** | `memcpy(&string_a, &string_b, ...)` | Copie com `=` |
| 21 | **Exceção saindo de `noexcept`** | `terminate` | Capture ou remova `noexcept` |
| 22 | **Uso de objeto movido** | usar `s` após `std::move(s)` (estado válido, **valor não especificado**) | Reatribua antes de reutilizar |
| 23 | **Tempo de vida de temporário em range-for** | `for (x : f().g())` onde `f()` retorna temporário | Guarde `auto&& t = f();` (corrigido em parte pelo C++23) |
| 24 | **Strings: `std::string(nullptr)`** | construir de `nullptr` | Verifique o ponteiro |

## Exemplo: o otimizador "prova" que o UB não ocorre

```cpp
// g++ -std=c++20 -O2 -Wall -Wextra
#include <iostream>

int tamanho_da_busca(int* p, int n) {
    int primeiro = *p;                      // desreferencia p...
    if (p == nullptr) return -1;            // ...então o compilador pode REMOVER este teste (p "não pode" ser nulo)
    return n + primeiro;
}

int main() {
    int x = 5;
    std::cout << tamanho_da_busca(&x, 10) << '\n';   // 15 (uso válido)
}
```

## Exemplo: versão segura de aliasing e de overflow

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <bit>
#include <cstdint>
#include <iostream>
#include <limits>

int main() {
    float f = 1.5f;
    // ERRO (UB): std::uint32_t bits = *reinterpret_cast<std::uint32_t*>(&f);   // viola strict aliasing
    auto bits = std::bit_cast<std::uint32_t>(f);                                 // correto (C++20)
    std::cout << std::hex << bits << std::dec << '\n';                           // 3fc00000

    int a = std::numeric_limits<int>::max();
    // ERRO (UB): a + 1;                                                          // overflow com sinal
    long long grande = static_cast<long long>(a) + 1;                            // alargue o tipo antes
    std::cout << grande << '\n';
}
```

## Ferramentas por tipo de UB

| Ferramenta | Detecta |
|---|---|
| ASan | 2, 3, 4, 5 (parcial) |
| UBSan | 1, 5, 9, 10, 11, 12 |
| MSan / Valgrind | 6 |
| TSan | 7 |
| `-Wall -Wextra -Wconversion -Wshadow` | 6, 12, vários descuidos |
| clang-tidy / cppcheck | Padrões perigosos ([[clang-tidy e cppcheck]]) |
| Fuzzing | Todos os acima em entradas inesperadas ([[Fuzzing]]) |

> [!tip] Estratégia
> Habilite sanitizers nos testes, compile com `-Werror` em CI e adote tipos que tornam o erro impossível (`span`, `optional`, `unique_ptr`, `std::variant`). No C++26, parte das leituras não inicializadas deixa de ser UB (*erroneous behavior*): veja [[Cpp26 Visão Geral]].

## Veja também

- [[Comportamento Indefinido e Não Especificado]]
- [[Sanitizers]]
- [[Segurança e Hardening]]
- [[Erros Comuns de Iniciantes - Cpp]]
- [[MOC - Referência - Cpp]]

## Exercício

1. Para 5 linhas da tabela, escreva um programa mínimo que reproduza o problema e mostre o relatório do sanitizer correspondente.
2. Explique por que o teste `p == nullptr` do primeiro exemplo pode ser removido com `-O2`.
