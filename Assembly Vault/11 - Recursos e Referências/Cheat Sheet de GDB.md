---
titulo: "Cheat Sheet de GDB para Assembly"
aliases:
  - Depuração
tipo: cheatsheet
tags:
  - assembly
  - cheatsheet
  - depuracao
  - x64
nivel: todos
arquitetura:
  - x64
criado: 2026-10-21
---

# Cheat Sheet de GDB para Assembly

> [!abstract] Resumo
> Comandos do **GDB** mais úteis para depurar Assembly: iniciar, pontos de parada, execução passo a passo (por instrução), ver registradores, flags e memória, desmontar, e depurar sem símbolos. Também `strace`, `objdump` e uma sessão completa de exemplo. Voltar: [[11 - Recursos e Referências]] · [[00 - Índice]]

Tags: #assembly #cheatsheet #gdb #depuracao

---

## 1. Preparar o programa e abrir o GDB

```bash
nasm -f elf64 -g -F dwarf prog.asm -o prog.o     # -g -F dwarf: símbolos e linhas de código
ld prog.o -o prog
gdb ./prog                                       # abre o GDB
gdb -q ./prog                                    # sem o banner
gdb --args ./prog arg1 arg2                      # com argumentos
```

> [!tip] Configuração recomendada (`~/.gdbinit`)
> ```text
> set disassembly-flavor intel
> set pagination off
> set confirm off
> ```
> Sem a primeira linha, o GDB mostra a sintaxe **AT&T** (com `%` e operandos invertidos).

## 2. Executar

| Comando | Abrev. | Efeito |
|---------|:------:|--------|
| `run [args]` | `r` | inicia o programa |
| `starti` | | inicia e **para na primeira instrução** (antes de `_start`) |
| `start` | | para no `main` (só com libc/símbolo `main`) |
| `continue` | `c` | continua até o próximo ponto de parada |
| `stepi` | `si` | executa **uma instrução** (entra em `call`) |
| `nexti` | `ni` | uma instrução (**pula** `call`) |
| `step` / `next` | `s` / `n` | uma **linha** de código-fonte (pouco útil em Assembly puro) |
| `finish` | `fin` | executa até a função atual retornar |
| `until *ADDR` | | executa até o endereço |
| `kill` | `k` | termina o programa |
| `quit` | `q` | sai |

> [!tip] `si 5`, `ni 10`
> Aceitam uma contagem: `si 5` executa 5 instruções.

## 3. Pontos de parada

| Comando | Efeito |
|---------|--------|
| `break rotulo` / `b rotulo` | para no rótulo (função) |
| `break *0x401000` | para num **endereço** exato (útil sem símbolos) |
| `break arq.asm:42` | numa linha |
| `tbreak rotulo` | ponto de parada **temporário** (uma vez) |
| `break rotulo if $rax == 5` | **condicional** |
| `info breakpoints` | lista (`i b`) |
| `delete 2` / `delete` | remove o nº 2 / todos |
| `disable 2` / `enable 2` | desliga / liga |
| `watch var` | para quando `var` **muda** (*watchpoint* de escrita) |
| `watch *(long *)0x601000` | idem para um endereço |
| `rwatch` / `awatch` | leitura / leitura ou escrita |
| `catch syscall write` | para em uma **syscall** (`catch syscall` = todas) |
| `catch signal SIGSEGV` | para ao receber um sinal |

## 4. Registradores e flags

| Comando | Efeito |
|---------|--------|
| `info registers` / `i r` | todos os registradores gerais |
| `info registers rax rbx` | só esses |
| `info registers eflags` | flags: `[ ZF PF ]` etc. |
| `info all-registers` | inclui `xmm`/`ymm` |
| `p $rax` / `p/x $rax` | imprime (decimal / hexa) |
| `p/t $rax` / `p/c $al` / `p/d $eax` | binário / caractere / decimal com sinal |
| `p $xmm0` | vetor completo (com `v4_float`, `v2_double`, ...) |
| `p $xmm0.v4_float[0]` | um elemento |
| `p $eflags` | flags como texto |
| `set $rax = 10` | altera um registrador |
| `set $rip = rotulo` | **desvia a execução** |

> [!note] Subregistradores
> `$eax`, `$ax`, `$al` funcionam (`$eax` é o valor de 32 bits). O ponteiro de instrução é **`$rip`** (ou `$pc`) e a pilha **`$rsp`** (ou `$sp`).

## 5. Memória: o comando `x`

Formato: `x/NFU endereço`, com **N** = quantidade, **F** = formato, **U** = unidade.

| Formato (F) | Significado | Unidade (U) | Tamanho |
|:-----------:|-------------|:-----------:|:-------:|
| `x` | hexa | `b` | byte |
| `d` | decimal | `h` | 2 bytes (*halfword*) |
| `u` | decimal sem sinal | `w` | 4 bytes (*word*) |
| `o` | octal | `g` | 8 bytes (*giant*) |
| `t` | binário | | |
| `c` | caractere | | |
| `s` | **string** terminada em 0 | | |
| `i` | **instrução** | | |
| `f` | ponto flutuante | | |
| `a` | endereço | | |

```text
(gdb) x/8xb &buf            # 8 bytes em hexa
(gdb) x/4xg $rsp            # 4 quadwords a partir do topo da pilha
(gdb) x/s msg               # string em msg
(gdb) x/5i $rip             # as próximas 5 instruções
(gdb) x/16xb $rsp-16        # inclui a red zone
(gdb) x/4fw &floats         # 4 floats
(gdb) x/2dw &ints           # 2 inteiros de 32 bits com sinal
```

| Outros | Efeito |
|--------|--------|
| `p var` / `p/x var` | valor de uma variável (rótulo de dados) |
| `p &var` | endereço |
| `p *(int *)0x601000` | interpreta um endereço como `int` |
| `p (char[8])var` | reinterpreta como bytes |
| `set var = 7` / `set {int}0x601000 = 7` | escreve em memória |
| `info symbol 0x401010` | nome do símbolo naquele endereço |
| `info line rotulo` | endereço de uma linha |

## 6. Desmontar e ver o contexto

| Comando | Efeito |
|---------|--------|
| `disassemble` / `disas` | desmonta a função atual |
| `disas /r` | com **bytes de código de máquina** |
| `disas /s` | misturado com o código-fonte |
| `disas rotulo` | desmonta um rótulo |
| `disas 0x401000,+32` | um intervalo (32 bytes) |
| `display/i $pc` | **mostra a próxima instrução a cada parada** |
| `display/x $rax` | mostra um valor a cada parada |
| `undisplay 1` | remove |
| `layout asm` / `layout regs` | **modo TUI**: painel de código e de registradores |
| `focus cmd` / `Ctrl+x a` | alterna a TUI; `Ctrl+l` redesenha |
| `info frame` / `bt` | quadro atual / pilha de chamadas |
| `info proc mappings` | mapa de memória do processo |
| `info files` | seções e ponto de entrada |

## 7. Receitas

### 7.1 Sessão típica

```text
$ gdb -q ./prog
(gdb) set disassembly-flavor intel
(gdb) starti
(gdb) layout regs
(gdb) display/i $pc
(gdb) break _start
(gdb) si 3
(gdb) x/4xg $rsp
(gdb) info registers eflags
(gdb) watch *(long *)&contador
(gdb) continue
```

### 7.2 Depurar sem símbolos (binário "stripped")

```text
(gdb) info files                 # acha o "Entry point: 0x401040"
(gdb) break *0x401040
(gdb) run
(gdb) x/20i $rip
```

### 7.3 Ver os argumentos de uma syscall

```text
(gdb) catch syscall write
(gdb) run
(gdb) p $rax          # número da syscall (1 = write)
(gdb) p $rdi          # fd
(gdb) x/s $rsi        # buffer
(gdb) p $rdx          # tamanho
(gdb) finish          # ou "si" e olhar $rax: valor de retorno
```

### 7.4 Achar um `SIGSEGV`

```text
(gdb) run
Program received signal SIGSEGV
(gdb) x/i $rip                  # instrução que falhou
(gdb) info registers            # qual registrador tinha o endereço ruim?
(gdb) bt                        # quem chamou
```

### 7.5 Pilha desalinhada antes de um `call`

```text
(gdb) break *ENDERECO_DO_CALL
(gdb) run
(gdb) p $rsp & 0xf              # deve ser 0 imediatamente ANTES do call
```

---

## 8. Outras ferramentas de apoio

| Ferramenta | Comando | Uso |
|------------|---------|-----|
| **strace** | `strace ./prog` | lista as syscalls, argumentos e retornos |
| | `strace -f -e trace=write,read ./prog` | só algumas; segue *forks* |
| | `strace -o saida.txt ./prog` | grava num arquivo |
| **ltrace** | `ltrace ./prog` | chamadas a funções de bibliotecas |
| **objdump** | `objdump -d -M intel prog` | desmonta em sintaxe Intel |
| | `objdump -d -M intel -S prog` | com o código-fonte |
| **readelf** | `readelf -h prog` / `-S` / `-l` | cabeçalho / seções / segmentos |
| **nm** | `nm prog` | símbolos |
| **hexdump / xxd** | `xxd prog \| head` | bytes brutos |
| **echo $?** | `echo $?` | **código de saída** do último programa |

> [!warning] Erros comuns
> 1. **Esquecer `-g -F dwarf`** ao montar e depois não ver linhas nem rótulos.
> 2. **`si` em um `call` a uma função da libc**: entra em código sem símbolos; use `ni` ou `finish`.
> 3. **Esquecer a sintaxe Intel** e interpretar `mov %rax, %rbx` de trás para frente.
> 4. **Tentar `watch` numa variável que ainda não existe** (antes de `run`).
> 5. **Depurar um binário PIE sem iniciá-lo:** os endereços só são finais depois do `run` (use `starti`).

**Voltar:** [[11 - Recursos e Referências]] · **Ver também:** [[Cheat Sheet de Instruções]] · [[Cheat Sheet de Calling Conventions]] · [[01 - Fundamentos de Arquitetura e Assembly]] · [[Glossário#Assembly (x86-64 e ARM)]]
