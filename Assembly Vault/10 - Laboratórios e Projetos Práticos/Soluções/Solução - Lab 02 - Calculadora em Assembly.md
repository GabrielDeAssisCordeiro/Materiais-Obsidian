---
titulo: "Solução - Lab 02 - Calculadora em Assembly"
aliases:
tipo: solucao
tags:
  - assembly
  - lab
  - solucao
  - nasm
  - parsing
nivel: iniciante
arquitetura:
  - x64
criado: 2026-10-21
---

# Solução - Lab 02 - Calculadora em Assembly

> [!warning] Tente primeiro!
> Primeiro o [[Lab 02 - Calculadora em Assembly]]. Depois compare.

Voltar: [[Lab 02 - Calculadora em Assembly]] · Módulo: [[10 - Laboratórios e Projetos Práticos]]

> [!success] Testada
> Montada e executada com a entrada do enunciado (incluindo pipe, divisão por zero e erro de sintaxe). As saídas foram exatamente as listadas na seção 5 do lab.

## 1. Código completo comentado

```nasm
; Lab 02 - Calculadora: lê "A op B" da stdin e imprime o resultado
default rel
global _start

section .data
prompt   db "calc> "
prompt_n equ $ - prompt
e_div    db "erro: divisao por zero", 10
e_div_n  equ $ - e_div
e_syn    db "erro: sintaxe (use: A op B, op em + - * /)", 10
e_syn_n  equ $ - e_syn

section .bss
inbuf resb 128
outbuf resb 32

section .text
write:                      ; rsi, rdx
    mov eax, 1
    mov edi, 1
    syscall
    ret

; parse_int: RSI = ptr -> RAX = valor (com sinal), RSI avança; CF=1 se nenhum dígito
parse_int:
.sp: cmp byte [rsi], ' '
    jne .sg
    inc rsi
    jmp .sp
.sg: xor r8d, r8d           ; r8 = negativo?
    cmp byte [rsi], '-'
    jne .dg
    mov r8d, 1
    inc rsi
.dg: xor eax, eax
    xor ecx, ecx            ; nº de dígitos
.lp: movzx edx, byte [rsi]
    sub edx, '0'
    cmp edx, 9
    ja  .end
    imul rax, rax, 10
    add rax, rdx
    inc rsi
    inc ecx
    jmp .lp
.end:
    test r8d, r8d
    jz .ok
    neg rax
.ok:
    test ecx, ecx
    jz .fail
    clc
    ret
.fail:
    stc
    ret

; print_i64: RAX
print_i64:
    mov r9, rax
    lea rsi, [outbuf + 31]
    mov byte [rsi], 10
    test rax, rax
    jns .pos
    neg rax
.pos:
    mov rcx, 10
.d: xor edx, edx
    div rcx
    add dl, '0'
    dec rsi
    mov [rsi], dl
    test rax, rax
    jnz .d
    test r9, r9
    jns .w
    dec rsi
    mov byte [rsi], '-'
.w: lea rdx, [outbuf + 32]
    sub rdx, rsi
    jmp write

; read_line: lê byte a byte até '\n' (ou EOF). Devolve RAX = bytes lidos (0 = EOF puro)
; (1 syscall por byte: simples e correto também com stdin em pipe; ver análise de desempenho)
read_line:
    xor r10d, r10d
.r: xor eax, eax
    xor edi, edi
    lea rsi, [inbuf + r10]
    mov edx, 1
    syscall
    test rax, rax
    jle .eof
    cmp byte [inbuf + r10], 10
    je  .nl
    inc r10d
    cmp r10d, 126
    jb  .r
.nl: mov byte [inbuf + r10], 0
    lea eax, [r10 + 1]      ; conta o '\n' (linha vazia devolve 1, não EOF)
    ret
.eof:
    mov byte [inbuf + r10], 0
    mov eax, r10d           ; 0 se nada foi lido
    ret

_start:
.loop:
    lea rsi, [prompt]
    mov edx, prompt_n
    call write
    call read_line          ; RAX = nº de bytes (0 = EOF)
    test rax, rax
    jle .exit
    lea rsi, [inbuf]
    call parse_int
    jc  .syn
    mov r12, rax            ; A
.skip: cmp byte [rsi], ' '
    jne .op
    inc rsi
    jmp .skip
.op: movzx ebx, byte [rsi]
    inc rsi
    call parse_int
    jc  .syn
    mov r13, rax            ; B
    cmp bl, '+'
    je .add
    cmp bl, '-'
    je .sub
    cmp bl, '*'
    je .mul
    cmp bl, '/'
    je .div
.syn:
    lea rsi, [e_syn]
    mov edx, e_syn_n
    call write
    jmp .loop
.add: lea rax, [r12 + r13]
    jmp .out
.sub: mov rax, r12
    sub rax, r13
    jmp .out
.mul: mov rax, r12
    imul rax, r13
    jmp .out
.div: test r13, r13
    jz .dz
    mov rax, r12
    cqo
    idiv r13
.out:
    call print_i64
    jmp .loop
.dz:
    lea rsi, [e_div]
    mov edx, e_div_n
    call write
    jmp .loop
.exit:
    mov eax, 60
    xor edi, edi
    syscall

section .note.GNU-stack noalloc noexec nowrite progbits
```

## 2. Explicação por blocos

| Trecho | O que faz | Detalhe de arquitetura |
|--------|-----------|------------------------|
| `read_line` | lê **1 byte** por `read` até `'\n'` ou 126 bytes | usa `R10` como índice (a `syscall` **não** destrói `R10`); termina a linha com `0` |
| `lea eax,[r10+1]` | devolve `bytes + 1` (o `'\n'` conta) | assim uma **linha vazia** retorna 1 e só o **EOF** retorna 0 |
| `parse_int` → `sub edx,'0'` / `cmp edx,9` / `ja` | teste de dígito com **uma** comparação sem sinal | valores abaixo de `'0'` viram números enormes (*wraparound*) |
| `imul rax,rax,10` / `add rax,rdx` | `acc = acc*10 + dígito` | `imul` de 3 operandos (latência ~3 ciclos) |
| `neg rax` | complemento de dois | `neg` também seta `CF` (por isso o `clc`/`stc` finais usam instruções próprias) |
| `stc` / `clc` | sinaliza erro/sucesso na **flag de carry** | convenção comum em Assembly: erro em `CF`, sem mexer em registradores |
| `mov ebx, byte` do operador, `cmp bl,'+'` ... | **cadeia de comparações** | 4 operadores: a cadeia é tão boa quanto uma tabela de saltos |
| `lea rax,[r12+r13]` | soma sem alterar flags e sem copiar | `lea` faz `r12 + r13` em uma instrução |
| `.mul: imul rax, r13` | multiplicação com sinal de 64 bits | o produto de 128 bits **não** é checado aqui (desafio: `jo`) |
| `.div: cqo` / `idiv r13` | `RDX:RAX ÷ r13` com sinal | `cqo` estende o sinal de `RAX` em `RDX`; **o resto fica em `RDX`** |
| `print_i64` | `neg` se negativo, converte, escreve `'-'` | guarda o sinal original em `R9` (o `div` destrói `RDX`) |

### Registradores preservados pela `syscall`
O kernel preserva todos os registradores **exceto `RAX` (resultado), `RCX` e `R11`**. Por isso `R12`/`R13` (operandos) e `R10` (índice) sobrevivem às chamadas de `read`/`write`.

## 3. Variações

**Resto (`%`):**
```nasm
.mod: test r13, r13
    jz  .dz
    mov rax, r12
    cqo
    idiv r13
    mov rax, rdx          ; o resto está em RDX
    jmp .out
```

**Detectar overflow na soma:**
```nasm
.add: mov rax, r12
    add rax, r13
    jo  .ovf              ; OF = 1 se o resultado com sinal não cabe em 64 bits
    jmp .out
```

**Caso especial `INT64_MIN / -1`:** `idiv` gera exceção `#DE` (`SIGFPE`) porque `+2⁶³` não cabe. Teste antes: se `r12 == 0x8000000000000000` e `r13 == -1`, trate como erro.

## 4. Análise de desempenho

| Item | Observação |
|------|------------|
| **Syscalls** | 9 por linha de 8 bytes (8 `read` + ...): o custo domina. Com bloco de entrada de 64 KiB, serão **≈ 1 `read` por 64 KiB** |
| **Cadeia de `cmp`** | 4 comparações: irrelevante. Com **dezenas** de comandos, use tabela de saltos (`jmp [tabela + rax*8]`, módulo [[03 - Instruções Básicas e Controle de Fluxo]]) |
| **`idiv` de 64 bits** | é a instrução mais lenta do programa (dezenas de ciclos); em CPUs recentes, `idiv r64` é bem mais rápida que em CPUs de 2015 |
| **Previsão de desvios** | o `cmp bl, ...` depende da entrada, mas para entrada interativa é imperceptível |

## 5. Erros comuns

> [!warning]
> 1. **`xor edx,edx` + `idiv`** com números negativos → resultado errado; use **`cqo`**.
> 2. **Um único `read`** assumindo "uma linha por chamada" → falha com *pipe*.
> 3. **Linha vazia tratada como EOF** (devolver 0 quando só havia `'\n'`).
> 4. **Não terminar o buffer com 0** → o *parser* lê lixo da linha anterior.
> 5. **Perder o sinal** em `print_i64` ao destruir `RAX` na divisão (guarde antes).

Anterior: [[Solução - Lab 01 - Hello World e Operações Básicas]] · Próximo: [[Lab 03 - Manipulação de Strings e Arrays]]
