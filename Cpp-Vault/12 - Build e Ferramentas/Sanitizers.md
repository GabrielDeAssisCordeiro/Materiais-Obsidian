---
titulo: "Sanitizers"
tags: [cpp, ferramentas, sanitizers, tsan]
aliases: ["AddressSanitizer", "ASan", "UBSan", "MSan", "-fsanitize"]
tipo: ferramenta
nivel: intermediario
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Comportamento Indefinido e Não Especificado]]", "[[Vazamentos e Dangling Pointers]]", "[[Data Races e Deadlocks]]"]
---

# Sanitizers

Instrumentam o código em **tempo de compilação** para detectar bugs em **execução**, com mensagens precisas. Disponíveis em GCC, Clang e (ASan) MSVC.

| Sanitizer | Flag | Detecta |
|---|---|---|
| **AddressSanitizer** | `-fsanitize=address` | Estouro de heap/stack/global, *use-after-free*, *use-after-scope*, *double free*, vazamentos (LeakSanitizer) |
| **UndefinedBehaviorSanitizer** | `-fsanitize=undefined` | Overflow de inteiros com sinal, desvio por nulo, shifts inválidos, alinhamento, `bool` inválido... |
| **ThreadSanitizer** | `-fsanitize=thread` | Data races ([[Data Races e Deadlocks]]) |
| **MemorySanitizer** | `-fsanitize=memory` (Clang) | Leitura de memória **não inicializada** |

Combinações: ASan + UBSan funcionam juntos; **TSan e ASan não** (execute separado); MSan só com Clang e toda a pilha instrumentada.

```cpp
// g++ -std=c++20 -g -O1 -Wall -Wextra
// PROGRAMA COM BUG PROPOSITAL (heap-buffer-overflow). Compila; falha em execução com ASan.
// Correção: usar v.at(5) / verificar índice, ou iterar com range-for.
#include <iostream>
#include <vector>

int main() {
    std::vector<int> v(5, 1);
    std::cout << v[5] << '\n';             // índice 5 em vetor de tamanho 5: UB
}
```

```bash
g++ -std=c++20 -g -O1 -fsanitize=address,undefined -fno-omit-frame-pointer bug.cpp -o bug && ./bug
# ==ERROR: AddressSanitizer: heap-buffer-overflow on address ...
# READ of size 4 ...   #0 main bug.cpp:9

clang++ -std=c++20 -g -O1 -fsanitize=thread race.cpp -o race && ./race
```

```cmake
# CMake: habilite por opção/preset
option(ENABLE_SANITIZERS "ASan+UBSan" OFF)
if(ENABLE_SANITIZERS AND CMAKE_CXX_COMPILER_ID MATCHES "GNU|Clang")
  add_compile_options(-fsanitize=address,undefined -fno-omit-frame-pointer)
  add_link_options(-fsanitize=address,undefined)
endif()
```

> [!tip] Rotina de qualidade
> Rode **testes unitários com ASan+UBSan** em toda CI, e TSan em testes concorrentes. O custo (≈2× mais lento, ≈2–3× mais memória para ASan) é pequeno frente ao benefício.

> [!warning] Limitações
> - Sanitizers só acham bugs nos **caminhos executados**: combine com bons testes e [[Fuzzing]].
> - Não use em *builds* de produção finais sem avaliar o custo e a superfície de ataque.
> - Variáveis de ambiente úteis: `ASAN_OPTIONS=detect_leaks=1:halt_on_error=0`, `UBSAN_OPTIONS=print_stacktrace=1`.

## Veja também

- [[Valgrind]]
- [[Depuração com GDB LLDB e Visual Studio]]
- [[Comportamento Indefinido e Não Especificado]]
- [[Fuzzing]]
- [[Vazamentos e Dangling Pointers]]

## Exercício

1. Provoque use-after-free, stack overflow de array e overflow de inteiro com sinal; identifique o sanitizer que pega cada um.
2. Adicione um preset `asan` ao seu CMake e rode os testes com ele.
