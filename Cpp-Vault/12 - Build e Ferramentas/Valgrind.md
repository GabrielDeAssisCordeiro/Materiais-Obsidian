---
titulo: "Valgrind"
tags: [cpp, ferramentas]
aliases: ["Valgrind", "memcheck", "helgrind", "callgrind", "massif", "KCachegrind"]
tipo: ferramenta
nivel: intermediario
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Sanitizers]]", "[[Vazamentos e Dangling Pointers]]", "[[Profiling e Benchmarking]]"]
---

# Valgrind

Máquina virtual que **interpreta** o binário e monitora memória, sem recompilar (apenas `-g` para boas mensagens). Roda **~10–50× mais lento**. Linux e macOS (suporte limitado e variável em Apple Silicon — verificar).

| Ferramenta | Função |
|---|---|
| **memcheck** (padrão) | Leitura/escrita inválida, uso de memória não inicializada, vazamentos, *double free* |
| **helgrind / drd** | Data races e problemas de lock |
| **callgrind** | Perfil de chamadas e instruções (visualizar com KCachegrind) |
| **cachegrind** | Simula caches e *branch predictor* |
| **massif** | Perfil de uso de heap ao longo do tempo |

```cpp
// g++ -std=c++20 -g -O0 -Wall -Wextra
// BUG PROPOSITAL: vazamento + leitura não inicializada. Compila; Valgrind aponta os problemas.
// Correção: usar std::unique_ptr / std::vector e inicializar variáveis.
#include <iostream>

int main() {
    int* p = new int[10];                  // nunca liberado: "definitely lost"
    int x;                                  // não inicializado
    if (x > 0) std::cout << "positivo\n";   // "Conditional jump depends on uninitialised value"
    p[0] = 1;
}
```

```bash
g++ -std=c++20 -g -O0 prog.cpp -o prog
valgrind --leak-check=full --show-leak-kinds=all --track-origins=yes ./prog
valgrind --tool=callgrind ./prog && callgrind_annotate callgrind.out.*
valgrind --tool=massif ./prog && ms_print massif.out.*
```

## Valgrind vs Sanitizers

| | Valgrind | ASan/UBSan |
|---|---|---|
| Recompilar? | Não | Sim |
| Velocidade | Muito mais lento | ~2× |
| Memória não inicializada | **Sim** | Só MSan (Clang) |
| Stack/global overflow | Limitado | **Sim** |
| Código de terceiros sem fontes | **Sim** | Não |

> [!tip] Quando usar
> Quando não é possível recompilar, para achar variáveis não inicializadas, ou para perfil com callgrind. No dia a dia, [[Sanitizers]] são mais rápidos.

## Veja também

- [[Sanitizers]]
- [[Vazamentos e Dangling Pointers]]
- [[Depuração com GDB LLDB e Visual Studio]]
- [[Profiling e Benchmarking]]

## Exercício

1. Rode o exemplo no Valgrind e interprete cada seção do relatório.
2. Use `massif` para ver o crescimento do heap de um `std::vector` com `push_back`.
