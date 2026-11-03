---
titulo: "Cheat Sheet de GDB - Cpp"
tags: [cpp, referencia, cheat-sheet, gdb, lldb, depuracao]
aliases: ["Cheat sheet GDB", "Comandos GDB", "Comandos LLDB", "Resumo GDB"]
tipo: referencia
nivel: iniciante
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Depuração com GDB LLDB e Visual Studio]]", "[[Sanitizers]]", "[[Valgrind]]"]
---

# Cheat Sheet de GDB - Cpp

Compile com `-g -O0` (ou `-Og`). Iniciar: `gdb ./prog` ou `gdb --args ./prog arg1 arg2`; `gdb -tui` para interface de texto.

## Execução

| Ação | GDB | LLDB |
|---|---|---|
| Rodar | `run` / `r` | `run` / `r` |
| Continuar | `continue` / `c` | `continue` / `c` |
| Próxima linha | `next` / `n` | `next` / `n` |
| Entrar na função | `step` / `s` | `step` / `s` |
| Instrução (assembly) | `nexti` / `stepi` | `ni` / `si` |
| Sair da função | `finish` | `finish` |
| Executar até linha | `until 42` | `thread until 42` |
| Reiniciar / matar | `start` (para em `main`) / `kill` | `process launch -s` / `kill` |

## Breakpoints

| Ação | GDB | LLDB |
|---|---|---|
| Em função | `break soma` | `b soma` |
| Em linha | `break arq.cpp:42` | `b arq.cpp:42` |
| Condicional | `break f if x > 3` | `b f -c 'x > 3'` |
| Temporário | `tbreak f` | `b -o true f` |
| Listar | `info breakpoints` | `breakpoint list` |
| Remover / desabilitar | `delete 1` / `disable 1` | `breakpoint delete 1` / `disable 1` |
| Watchpoint (variável muda) | `watch total` | `watchpoint set variable total` |
| Em exceção C++ | `catch throw` | `breakpoint set -E c++` |

## Inspeção

| Ação | GDB | LLDB |
|---|---|---|
| Imprimir | `print v`, `p *ptr`, `p arr@5` (array de 5) | `p v`, `p *ptr` |
| Formato | `p/x n` (hex), `p/t n` (bin) | `p/x n` |
| Locais / args | `info locals` / `info args` | `frame variable` |
| Pilha | `backtrace` / `bt` / `bt full` | `bt` |
| Mudar de quadro | `up`, `down`, `frame 2` | `up`, `down`, `frame select 2` |
| Tipo | `ptype T`, `whatis x` | `image lookup -t T` |
| Memória | `x/8xw &v` (8 words hex) | `memory read -c8 -fx &v` |
| Exibir sempre | `display x` | `display x` |
| Código fonte | `list`, `list 40,60` | `source list` |
| Registradores/asm | `info registers`, `disassemble` | `register read`, `disassemble` |
| Modificar | `set var x = 5` | `expr x = 5` |

## Threads, core dumps e outros

| Ação | GDB |
|---|---|
| Listar threads | `info threads` |
| Trocar | `thread 2` |
| Pilhas de todas | `thread apply all bt` |
| Core dump | `ulimit -c unlimited` → executar → `gdb ./prog core` |
| Anexar a processo | `gdb -p PID` |
| Pretty-printers STL | Habilitados automaticamente com libstdc++ (`info pretty-printer`) |
| Script/comandos | `gdb -batch -ex run -ex bt --args ./prog` |
| Reverso (rr) | `rr record ./prog` → `rr replay` → `reverse-next`, `reverse-continue` |

```bash
# Rotina típica
g++ -std=c++20 -g -O0 prog.cpp -o prog
gdb -q ./prog
(gdb) break main
(gdb) run
(gdb) next
(gdb) p v
(gdb) bt
(gdb) continue
```

> [!tip] `.gdbinit`
> Em `~/.gdbinit`: `set print pretty on`, `set pagination off`, `set history save on`, `set confirm off`.

## Veja também

- [[Depuração com GDB LLDB e Visual Studio]]
- [[Sanitizers]]
- [[Valgrind]]
- [[Tabela de Erros de Compilador e Linker]]
- [[MOC - Referência - Cpp]]

## Exercício

1. Depure um programa com um *segfault* e use `bt` e `p` para achar a causa.
2. Use `watch` para descobrir qual linha corrompe uma variável.
