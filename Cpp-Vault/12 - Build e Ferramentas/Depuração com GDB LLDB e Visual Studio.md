---
titulo: "Depuração: GDB, LLDB e Visual Studio"
tags: [cpp, ferramentas, depuracao, gdb, lldb]
aliases: ["LLDB", "Depurador", "Debugger", "breakpoint", "core dump", "Visual Studio Debugger"]
tipo: ferramenta
nivel: iniciante
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Sanitizers]]", "[[Valgrind]]", "[[Flags Essenciais do Compilador]]"]
---

# Depuração: GDB, LLDB e Visual Studio

Depurar = pausar o programa, inspecionar estado e avançar passo a passo. Compile com **símbolos de depuração** (`-g`) e, para depurar, com pouca ou nenhuma otimização (`-O0` ou `-Og`).

| Depurador | Plataforma | Observação |
|---|---|---|
| **GDB** | Linux (GNU) | Padrão com GCC; `gdb --tui`, *pretty printers* para STL |
| **LLDB** | macOS, Linux, Windows | Padrão com Clang/Xcode |
| **Visual Studio / VS Code** | Windows (VS), multi (VS Code) | Interface gráfica, depurador MSVC ou GDB/LLDB via DAP |
| **rr** | Linux | **Execução reversível** (grava e reexecuta) |

```cpp
// g++ -std=c++20 -g -O0 -Wall -Wextra
#include <iostream>
#include <vector>

int soma(const std::vector<int>& v) {
    int total = 0;
    for (std::size_t i = 0; i < v.size(); ++i) total += v[i];     // coloque um breakpoint aqui
    return total;
}

int main() {
    std::vector<int> dados{1, 2, 3, 4};
    std::cout << soma(dados) << '\n';
}
```

## Comandos essenciais

| Ação | GDB | LLDB |
|---|---|---|
| Executar | `run` (`r`) | `run` (`r`) |
| Breakpoint | `break arquivo.cpp:8` / `b soma` | `b arquivo.cpp:8` / `b soma` |
| Próxima linha (sem entrar) | `next` (`n`) | `next` (`n`) |
| Entrar na função | `step` (`s`) | `step` (`s`) |
| Continuar | `continue` (`c`) | `continue` (`c`) |
| Pilha de chamadas | `backtrace` (`bt`) | `bt` |
| Imprimir | `print v`, `p v.size()` | `p v`, `expr v.size()` |
| Variáveis locais | `info locals` | `frame variable` |
| Watchpoint | `watch total` | `watchpoint set variable total` |
| Breakpoint condicional | `b soma if i == 2` | `b soma -c 'i == 2'` |
| Sair | `quit` | `quit` |

```bash
g++ -std=c++20 -g -O0 prog.cpp -o prog
gdb ./prog
# (gdb) b soma
# (gdb) run
# (gdb) bt
# (gdb) p v
# (gdb) finish        # executa até retornar da função

# Analisar um core dump (programa que travou)
ulimit -c unlimited && ./prog     # gera "core"
gdb ./prog core
```

> [!tip] Técnicas úteis
> - **`bt`** ao travar mostra de onde veio o erro. `thread apply all bt` para programas multithread.
> - Em arquivos otimizados (`-O2 -g`), variáveis podem aparecer como `<optimized out>`: use `-Og` ao depurar.
> - Habilite `-D_GLIBCXX_DEBUG` (libstdc++) para verificar limites e iteradores do STL.
> - Combine com [[Sanitizers]] — eles apontam a causa; o depurador mostra o contexto.
> - `rr record ./prog` e `rr replay` permitem voltar no tempo (`reverse-continue`).

> [!info] Printf debugging
> Também é legítimo. Use `std::println`/`std::cerr` e, em código de produção, uma biblioteca de log ([[Visão Geral das Bibliotecas]]).

## Veja também

- [[Sanitizers]]
- [[Valgrind]]
- [[Flags Essenciais do Compilador]]
- [[Comportamento Indefinido e Não Especificado]]

## Exercício

1. Introduza um acesso fora do limite e use GDB para achar a linha exata.
2. Gere um core dump de um programa que acessa `nullptr` e analise com `bt`.
