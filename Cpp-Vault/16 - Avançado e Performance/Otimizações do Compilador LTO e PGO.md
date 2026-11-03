---
titulo: "Otimizações do compilador: -O, LTO, PGO"
tags: [cpp, performance, otimizacao, inline, compilador]
aliases: ["Otimizações", "-O2", "-O3", "PGO", "Link-Time Optimization", "Profile-Guided Optimization", "inlining", "BOLT", "-march=native"]
tipo: conceito
nivel: avancado
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Flags Essenciais do Compilador]]", "[[Compiler Explorer]]", "[[Profiling e Benchmarking]]"]
---

# Otimizações do compilador: `-O`, LTO, PGO

## Níveis de otimização

| Flag | Efeito |
|---|---|
| `-O0` | Sem otimização (depuração) |
| `-Og` | Otimiza sem atrapalhar a depuração |
| `-O1` / `-O2` | Conjunto equilibrado; **`-O2`** é o padrão de produção na maioria dos projetos |
| `-O3` | Mais agressivo (vetorização, *unrolling*, inlining); nem sempre mais rápido |
| `-Os` / `-Oz` | Tamanho de código |
| `-Ofast` | `-O3` + `-ffast-math`: **quebra conformidade IEEE** (NaN, associatividade) |
| `-march=native` | Usa instruções da CPU atual; binário **não portátil** (ou `-march=x86-64-v3`) |

## Principais transformações

| Otimização | Exemplo |
|---|---|
| **Inlining** | Substitui chamada pelo corpo; habilita outras otimizações |
| Propagação/dobra de constantes | `constexpr`, `2 * 3` → `6` |
| Eliminação de código morto | Remove o que não afeta o resultado observável |
| *Loop unrolling*, **vetorização** (SIMD) | [[SIMD e Vetorização - Cpp]] |
| Elisão de cópias, **RVO** | [[Copy Elision e RVO]] |
| Devirtualização | Quando o tipo dinâmico é conhecido |
| Otimização de cauda | Recursão → laço |

> [!danger] Otimizador e UB
> O compilador **assume que não há UB**. Overflow de inteiro com sinal, acesso fora dos limites ou aliasing estrito violado podem fazer o programa "funcionar" em `-O0` e quebrar em `-O2` ([[Comportamento Indefinido e Não Especificado]]).

```cpp
// g++ -std=c++20 -O2 -Wall -Wextra
// Em -O2 o compilador pode transformar esta função em "return true;" porque overflow com sinal é UB.
#include <iostream>
#include <limits>

bool sempre_maior(int x) { return x + 1 > x; }

int main() {
    std::cout << sempre_maior(std::numeric_limits<int>::max()) << '\n';   // comportamento NÃO garantido (UB)
}
```

## LTO (*Link-Time Optimization*)

Normalmente cada `.cpp` é otimizado **isoladamente**. Com LTO, o otimizador vê o **programa inteiro** no link: inlining entre arquivos, remoção de código global morto, melhor devirtualização.

```bash
g++ -std=c++20 -O2 -flto -c a.cpp b.cpp && g++ -O2 -flto a.o b.o -o app      # GCC
clang++ -O2 -flto=thin a.cpp b.cpp -o app                                       # ThinLTO (mais escalável)
```

```cmake
include(CheckIPOSupported)
check_ipo_supported(RESULT ok)
if(ok) set_property(TARGET app PROPERTY INTERPROCEDURAL_OPTIMIZATION ON) endif()
```

## PGO (*Profile-Guided Optimization*)

O compilador usa **dados de execução reais** para decidir inlining, layout de código e ramos prováveis. Ganhos típicos: 5–30%.

```bash
# GCC
g++ -O2 -fprofile-generate prog.cpp -o prog_instr
./prog_instr < carga_tipica.txt                       # gera *.gcda
g++ -O2 -fprofile-use -fprofile-correction prog.cpp -o prog_pgo

# Clang
clang++ -O2 -fprofile-instr-generate prog.cpp -o prog_instr
LLVM_PROFILE_FILE=prog.profraw ./prog_instr
llvm-profdata merge -o prog.profdata prog.profraw
clang++ -O2 -fprofile-instr-use=prog.profdata prog.cpp -o prog_pgo
```

Ferramentas pós-link: **BOLT** (reorganiza o binário com perfil), **AutoFDO**.

## Dicas de código que ajudam o otimizador

- `const`, `constexpr`, `noexcept`, `[[likely]]`/`[[unlikely]]` (C++20) — use com medições.
- `std::unreachable()` (C++23) para caminhos impossíveis (UB se alcançado!).
- Evite aliasing: `__restrict` (extensão) em laços numéricos.
- Funções pequenas e visíveis (em header ou com LTO).

> [!tip] Processo
> 1. Compile em **Release** (`-O2`). 2. Meça ([[Profiling e Benchmarking]]). 3. Tente LTO. 4. Se valer, PGO. 5. Só depois, `-march`.

## Veja também

- [[Flags Essenciais do Compilador]]
- [[Compiler Explorer]]
- [[Profiling e Benchmarking]]
- [[Copy Elision e RVO]]
- [[Comportamento Indefinido e Não Especificado]]

## Exercício

1. Compile o mesmo benchmark com `-O0`, `-O2`, `-O3`, `-O2 -flto` e tabule os tempos.
2. Aplique PGO a um programa com ramos previsíveis e compare.
