---
titulo: "Compiler Explorer (Godbolt)"
tags: [cpp, ferramentas, assembly]
aliases: ["Compiler Explorer", "Godbolt", "godbolt.org", "Assembly", "Ver assembly"]
tipo: ferramenta
nivel: iniciante
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Suporte dos Compiladores aos Padrões]]", "[[Compiladores GCC Clang e MSVC]]", "[[Profiling e Benchmarking]]"]
---

# Compiler Explorer (Godbolt)

Site (godbolt.org) que compila código C++ em **dezenas de compiladores e versões** e mostra o **assembly** lado a lado, com destaque das linhas correspondentes.

## Para que serve

| Uso | Exemplo |
|---|---|
| Ver o efeito de otimizações | `-O0` vs `-O2` vs `-O3` |
| Testar recursos novos | Escolha GCC/Clang/MSVC trunk para C++23/26 ([[Suporte dos Compiladores aos Padrões]]) |
| Comparar compiladores | O mesmo código em GCC, Clang e MSVC |
| Entender abstrações | Custo zero de `std::span`, `std::array`, lambdas, `constexpr` |
| Compartilhar *bug reports* | Link curto reproduzível |
| Bibliotecas | Suporte a fmt, Boost, Eigen, Google Benchmark... (menu *Libraries*) |
| Ferramentas | Executar o programa, sanitizers, `llvm-mca`, *opt pipeline*, saída do pré-processador |

```cpp
// g++ -std=c++20 -O2 -Wall -Wextra
// Cole no Compiler Explorer com -O2: o compilador reduz tudo a uma constante.
#include <array>

constexpr int soma_quadrados(int n) {
    int s = 0;
    for (int i = 1; i <= n; ++i) s += i * i;
    return s;
}

int main() {
    constexpr int r = soma_quadrados(10);      // calculado em compilação
    static_assert(r == 385);
    std::array<int, 3> a{1, 2, 3};
    return r + a[0] - 386;                     // retorna 0
}
```

> [!tip] Dicas
> - Marque *Compile to binary* e *Execute the code* para ver a saída real.
> - Use `-O2 -march=native` (cuidado: depende da máquina do servidor) ou `-march=x86-64-v3` para ver SIMD.
> - Reduza o código ao mínimo (funções que **retornam** o valor) para evitar que o compilador elimine tudo como código morto.

> [!warning] Cuidado com microbenchmarks
> Olhar assembly não substitui **medir**; veja [[Profiling e Benchmarking]].

## Veja também

- [[Suporte dos Compiladores aos Padrões]]
- [[Compiladores GCC Clang e MSVC]]
- [[Profiling e Benchmarking]]
- [[Flags Essenciais do Compilador]]

## Exercício

1. Compare o assembly de um laço com `std::vector<int>` e com `std::array<int, 1000>` em `-O2`.
2. Descubra se o seu compilador favorito já suporta um recurso do C++26 usando a versão trunk.
