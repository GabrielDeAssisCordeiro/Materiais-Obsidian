---
titulo: "Cheat Sheet de Instruções (x86-64, sintaxe NASM/Intel)"
aliases:
  - Cheat Sheet x86-64
  - Instruções x86-64
tipo: cheatsheet
tags:
  - assembly
  - cheatsheet
  - x64
  - nasm
  - instrucoes
nivel: todos
arquitetura:
  - x64
criado: 2026-10-21
---

# Cheat Sheet de Instruções (x86-64, sintaxe NASM/Intel)

> [!abstract] Resumo
> Consulta rápida das instruções mais usadas, flags, condições de salto, formas de endereçamento e syscalls Linux. Para detalhes, veja o **Intel SDM, Volume 2** ou *felixcloutier.com/x86*. Voltar: [[11 - Recursos e Referências]] · [[00 - Índice]]

Tags: #assembly #cheatsheet #x64

> [!note] Convenção
> Em sintaxe Intel o **destino vem primeiro**: `mov dst, src`. `r` = registrador, `m` = memória, `i` = imediato. Uma instrução aceita **no máximo um** operando de memória (exceto as de string).

---

## 1. Registradores

| 64 | 32 | 16 | 8 baixo | Uso típico |
|----|----|----|---------|------------|
| `rax` | `eax` | `ax` | `al` | retorno, `mul`/`div` |
| `rbx` | `ebx` | `bx` | `bl` | *callee-saved* |
| `rcx` | `ecx` | `cx` | `cl` | contador, 4º arg (SysV), 1º arg (MS) |
| `rdx` | `edx` | `dx` | `dl` | `mul`/`div`, 3º arg (SysV) |
| `rsi` | `esi` | `si` | `sil` | 2º arg (SysV) |
| `rdi` | `edi` | `di` | `dil` | 1º arg (SysV) |
| `rbp` | `ebp` | `bp` | `bpl` | *frame pointer* |
| `rsp` | `esp` | `sp` | `spl` | topo da pilha |
| `r8`-`r15` | `r8d`-`r15d` | `r8w`-`r15w` | `r8b`-`r15b` | gerais |

> [!warning] Regras de escrita parcial
> Escrever em **32 bits** (`mov eax, 1`) **zera** a metade alta de `rax`. Escrever em **8 ou 16 bits** **preserva** o resto (e cria dependência falsa). Registradores vetoriais: `xmm0-15` (128 bits), `ymm0-15` (256), `zmm0-31` (512).

## 2. Flags

| Flag | Nome | Ligada quando |
|------|------|---------------|
| **CF** | Carry | vai-um / empréstimo (sem sinal estourou) |
| **ZF** | Zero | resultado é zero |
| **SF** | Sign | resultado negativo (bit mais alto = 1) |
| **OF** | Overflow | estouro **com sinal** |
| **PF** | Parity | paridade do byte baixo (poucas vezes útil) |
| **DF** | Direction | sentido das instruções de string (`cld`/`std`) |

## 3. Movimento de dados

| Instrução | Efeito | Observação |
|-----------|--------|------------|
| `mov d, s` | `d = s` | não mexe nas flags; memória ← memória **não existe** |
| `movzx d, s` | estende com zeros | `movzx eax, byte [rsi]` |
| `movsx d, s` / `movsxd rax, ecx` | estende com sinal | |
| `lea d, [ea]` | `d = endereço efetivo` | **não acessa memória**; aritmética grátis; não altera flags |
| `xchg a, b` | troca | com memória é **atômica** (implica `lock`) |
| `push s` / `pop d` | pilha | `rsp -= 8` / `rsp += 8` |
| `cmovcc d, s` | `mov` condicional | sem salto; só registrador/memória de origem |
| `setcc r8` | 0 ou 1 conforme a condição | `sete al` |
| `bswap r` | inverte a ordem dos bytes | *endianness* |
| `cdq` / `cqo` | estende o sinal de `eax`→`edx:eax` / `rax`→`rdx:rax` | antes de `idiv` |
| `cdqe` | `eax` → `rax` com sinal | |

## 4. Aritmética

| Instrução | Efeito |
|-----------|--------|
| `add d, s` / `sub d, s` | soma / subtração |
| `adc d, s` / `sbb d, s` | com carry (precisão múltipla) |
| `inc d` / `dec d` | ±1 (**não altera CF**) |
| `neg d` | `d = -d` |
| `cmp a, b` | `a - b`, só flags |
| `mul r/m` | sem sinal: `rdx:rax = rax * r/m` |
| `imul r/m` | com sinal, forma de 1 operando (igual a `mul`) |
| `imul d, s` / `imul d, s, imm` | com sinal, resultado truncado |
| `div r/m` | sem sinal: `rax = rdx:rax / r/m`, `rdx = resto` |
| `idiv r/m` | com sinal (faça `cqo` antes) |

> [!warning] Divisão
> `div`/`idiv` geram **`#DE` (SIGFPE)** com divisor zero **ou** quando o quociente não cabe no registrador. Zere `rdx` (`xor edx, edx`) antes de `div`; use `cqo` antes de `idiv`.

## 5. Lógica e bits

| Instrução | Efeito |
|-----------|--------|
| `and` / `or` / `xor` / `not` | operações bit a bit (`xor eax, eax` zera) |
| `test a, b` | `a & b`, só flags |
| `shl`/`sal` `d, n` | desloca à esquerda (×2ⁿ) |
| `shr d, n` | desloca à direita **lógico** (sem sinal) |
| `sar d, n` | desloca à direita **aritmético** (com sinal) |
| `rol` / `ror` | rotações |
| `bt r, i` / `bts` / `btr` / `btc` | testa/ liga / desliga / inverte um bit (resultado em CF) |
| `bsf` / `bsr` | índice do bit 1 menos / mais significativo |
| `tzcnt` / `lzcnt` | contagem de zeros à direita / à esquerda (BMI1 / ABM) |
| `popcnt d, s` | número de bits 1 |
| `andn`, `bextr`, `blsr`, `pext`, `pdep` | BMI1/BMI2 |

> [!tip] Deslocamento variável
> A quantidade de bits em `shl/shr/sar` vem do **imediato** ou de **`cl`** (e só de `cl`). BMI2 tem `shlx`/`shrx`/`sarx` com qualquer registrador, sem tocar nas flags.

## 6. Condições de salto (`jcc`, `cmovcc`, `setcc`)

| Condição | Aliases | Flags | Significado |
|----------|---------|-------|-------------|
| `e` | `z` | ZF=1 | igual / zero |
| `ne` | `nz` | ZF=0 | diferente |
| **Sem sinal** | | | |
| `a` | `nbe` | CF=0 e ZF=0 | acima (`>`) |
| `ae` | `nb`, `nc` | CF=0 | acima ou igual (`>=`) |
| `b` | `nae`, `c` | CF=1 | abaixo (`<`) |
| `be` | `na` | CF=1 ou ZF=1 | abaixo ou igual (`<=`) |
| **Com sinal** | | | |
| `g` | `nle` | ZF=0 e SF=OF | maior (`>`) |
| `ge` | `nl` | SF=OF | maior ou igual |
| `l` | `nge` | SF≠OF | menor (`<`) |
| `le` | `ng` | ZF=1 ou SF≠OF | menor ou igual |
| **Flags** | | | |
| `s` / `ns` | | SF=1 / SF=0 | negativo / não negativo |
| `o` / `no` | | OF=1 / OF=0 | com / sem estouro |
| `p` / `np` | | PF=1 / PF=0 | paridade (usada após `ucomisd` para detectar NaN) |

> [!warning] Sem sinal × com sinal
> Depois de `cmp a, b`: use **`ja/jb`** para números **sem sinal** (ponteiros, tamanhos) e **`jg/jl`** para **com sinal**. Trocar um pelo outro é um dos bugs mais comuns.

## 7. Fluxo de controle

| Instrução | Efeito |
|-----------|--------|
| `jmp alvo` | salto incondicional (relativo, ou `jmp rax`/`jmp [mem]` indireto) |
| `jcc alvo` | salto condicional (curto: ±127 bytes; longo: ±2 GiB) |
| `call alvo` | empilha o endereço de retorno e salta |
| `ret` / `ret n` | desempilha e retorna (`ret n` também libera `n` bytes) |
| `loop alvo` | `rcx--` e salta se `rcx != 0` (lenta; prefira `dec`+`jnz`) |
| `jrcxz alvo` | salta se `rcx == 0` |
| `syscall` | chamada de sistema (Linux x64) |
| `int3` | ponto de parada (0xCC) |
| `ud2` | instrução inválida (gera `#UD`) |
| `nop` | nada |

## 8. Strings

Usam `rsi` (origem), `rdi` (destino), `rcx` (contador) e `DF` (sentido; `cld` = para frente).

| Instrução | Efeito |
|-----------|--------|
| `movsb/w/d/q` | copia `[rsi]` → `[rdi]` e avança |
| `stosb/w/d/q` | grava `al/ax/eax/rax` em `[rdi]` e avança |
| `lodsb/w/d/q` | carrega `[rsi]` em `al/ax/eax/rax` e avança |
| `cmpsb/...` | compara `[rsi]` com `[rdi]` |
| `scasb/...` | compara `al/ax/eax/rax` com `[rdi]` |
| prefixos `rep` / `repe` / `repne` | repete até `rcx == 0` (ou enquanto igual / diferente) |

`rep movsb` e `rep stosb` são rápidos em CPUs com **ERMSB/FSRM** para blocos médios e grandes (módulo 09, seção 5.7); `repne scasb` é lenta e irregular.

## 9. Formas de endereçamento

```nasm
mov rax, [rbx]                 ; base
mov rax, [rbx + 8]             ; base + deslocamento
mov rax, [rbx + rcx*8]         ; base + índice*escala (escala 1, 2, 4 ou 8)
mov rax, [rbx + rcx*8 + 16]    ; completo
mov rax, [rel var]             ; relativo a RIP (use "default rel")
mov rax, [fs:0]                ; segmento (TLS)
lea rax, [rax + rax*4]         ; rax *= 5, sem tocar flags
```

## 10. SSE / AVX (essencial)

| Instrução | Efeito |
|-----------|--------|
| `movss` / `movsd` | escalar `float` / `double` |
| `movaps` / `movups` | 128 bits (alinhado / não alinhado) |
| `movdqa` / `movdqu` | inteiros 128 bits (alinhado / não alinhado) |
| `addss/sd/ps/pd`, `sub*`, `mul*`, `div*`, `sqrt*`, `min*`, `max*` | aritmética (sufixo `ss/sd` escalar, `ps/pd` empacotado) |
| `cvtsi2sd`, `cvttsd2si`, `cvtss2sd`, `cvtsd2ss` | conversões |
| `ucomisd a, b` | compara `double`, ajusta ZF, PF, CF |
| `pcmpeqb/w/d`, `pcmpgtb/w/d` | comparação → máscaras de 0xFF.. |
| `pmovmskb r32, xmm` | extrai o bit alto de cada byte |
| `pand`, `por`, `pxor`, `pandn` | lógica |
| `paddb/w/d/q`, `psubb/w/d/q` | soma/subtração empacotada de inteiros |
| `pshufb`, `pshufd`, `punpck*` | embaralhamento |
| `vaddps ymm0, ymm1, ymm2` | AVX: três operandos, 256 bits (não destrutivo) |
| `vfmadd231ps` | FMA: `a = b*c + a` com um só arredondamento |
| `vzeroupper` | **chame antes de voltar de código AVX** para código SSE |

## 11. Chamadas de sistema Linux

### 11.1 x86-64 (instrução `syscall`; número em `rax`; argumentos em `rdi, rsi, rdx, r10, r8, r9`; retorno em `rax`)

| Nº | Nome | Argumentos |
|---:|------|------------|
| 0 | `read` | `fd, buf, count` |
| 1 | `write` | `fd, buf, count` |
| 2 | `open` | `path, flags, mode` |
| 3 | `close` | `fd` |
| 5 | `fstat` | `fd, statbuf` |
| 8 | `lseek` | `fd, offset, whence` |
| 9 | `mmap` | `addr, len, prot, flags, fd, off` |
| 11 | `munmap` | `addr, len` |
| 12 | `brk` | `addr` |
| 39 | `getpid` | |
| 57 | `fork` | |
| 59 | `execve` | `path, argv, envp` |
| 60 | `exit` | `status` |
| 228 | `clock_gettime` | `clk, ts` |
| 231 | `exit_group` | `status` |
| 257 | `openat` | `dirfd, path, flags, mode` |

> [!warning] A instrução `syscall` destrói `rcx` e `r11`
> Use `r10` (não `rcx`) para o 4º argumento. Retorno entre **`-4095` e `-1`** é **`-errno`** (por exemplo `-2` = `ENOENT`, `-13` = `EACCES`).

### 11.2 Outras arquiteturas (resumo)

| Arquitetura | Instrução | Nº em | Args | Retorno | `write` | `exit` |
|-------------|-----------|-------|------|---------|:-------:|:------:|
| x86-64 | `syscall` | `rax` | `rdi rsi rdx r10 r8 r9` | `rax` | 1 | 60 |
| x86 (32 bits) | `int 0x80` | `eax` | `ebx ecx edx esi edi ebp` | `eax` | 4 | 1 |
| AArch64 | `svc #0` | `x8` | `x0`-`x5` | `x0` | 64 | 93 |
| AArch32 (EABI) | `svc #0` | `r7` | `r0`-`r5` | `r0` | 4 | 1 |

## 12. NASM × MASM em uma tabela

| Tema | NASM (Linux) | MASM (Windows) |
|------|--------------|----------------|
| Memória | `mov eax, [var]` | `mov eax, var` (nome já é memória) |
| Endereço | `mov rax, var` / `lea rax, [var]` | `lea rax, var` / `offset var` |
| Tamanho | `mov byte [x], 1` | `mov byte ptr x, 1` |
| Dados | `dd 5`, `resd 1` | `DWORD 5`, `?` |
| Seções | `section .text` | `.code` |
| Rótulo local | `.loop` | `@@` |
| Procedimento | rótulo + `ret` | `nome PROC ... ENDP` |

**Voltar:** [[11 - Recursos e Referências]] · **Ver também:** [[Cheat Sheet de Calling Conventions]] · [[Cheat Sheet de GDB]] · [[03 - Instruções Básicas e Controle de Fluxo]] · [[Glossário#Assembly (x86-64 e ARM)]]
