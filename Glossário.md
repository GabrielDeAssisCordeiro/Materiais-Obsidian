---
titulo: "Glossário"
aliases:
  - Glossário Técnico
  - Glossary
  - Termos
  - Vocabulário
  - Dicionário do Obsidian
tipo: glossario
nivel: todos
criado: 2026-10-24
tags:
  - glossario
  - referencia
---

# Glossário

> [!abstract] Glossário unificado
> Um único glossário para todos os vaults, com os termos agrupados por assunto e, dentro de cada assunto, por tópico e em ordem alfabética. Cada definição aponta para a nota que explica o conceito. Termos que existem em mais de um assunto (por exemplo, *Menor privilégio*, *Mock*, *Syscall*) aparecem em cada um, com a definição do contexto.

**Assuntos:** [[#Assembly (x86-64 e ARM)|Assembly]] · [[#Python|Python]] · [[#Rust|Rust]] · [[#C++|C++]] · [[#Sistemas Operacionais|Sistemas Operacionais]] · [[#Obsidian|Obsidian]] · [[#Docker|Docker]] · [[#Sandboxes e isolamento|Sandboxes e isolamento]] · [[#Segurança de IA (jailbreaking e prompt injection)|Segurança de IA]] · [[#Integração de Segurança|Integração]] · [[#Automação de Segurança|Automação]] · [[#Cibersegurança (Arsenal)|Cibersegurança]]

## Assembly (x86-64 e ARM)

Voltar ao índice: [[00 - Índice]].

### Arquitetura e CPU

| Termo | Definição |
|---|---|
| **AAPCS64 / AAPCS32** | convenção de chamada de procedimentos da Arm (64 e 32 bits) → [[Cheat Sheet de Calling Conventions]], [[08 - ARM e AArch64]] |
| **AArch64** | modo de 64 bits da arquitetura Arm (A64) → [[08 - ARM e AArch64]] |
| **Acumulador** | registrador (ou variável) que acumula um resultado; em SIMD, vários acumuladores quebram cadeias de dependência → [[09 - Otimização, SIMD e Performance]] |
| **ALU** | unidade lógica e aritmética → [[01 - Fundamentos de Arquitetura e Assembly]] |
| **Atômica (operação)** | indivisível para outras CPUs (`lock`, `xchg`, `ldadd`) → [[07 - Assembly Avançado (x86-x64)]], [[08 - ARM e AArch64]] |
| **Barramento** (*bus*) | caminho de dados/endereços/controle entre CPU, memória e periféricos → [[01 - Fundamentos de Arquitetura e Assembly]] |
| **Big-endian** | byte mais significativo no endereço mais baixo → [[02 - Registradores e Memória]] |
| **BMI** | *Bit Manipulation Instructions* (`andn`, `bextr`, `pext`, `pdep`, `tzcnt`) → [[Cheat Sheet de Instruções]] |
| **CISC / RISC** | *Complex / Reduced Instruction Set Computer* → [[01 - Fundamentos de Arquitetura e Assembly]], [[08 - ARM e AArch64]] |
| **Código de máquina** | os bytes que a CPU executa → [[01 - Fundamentos de Arquitetura e Assembly]] |
| **cpuid** | instrução que informa os recursos da CPU → [[07 - Assembly Avançado (x86-x64)]] |
| **DF** (*direction flag*) | sentido das instruções de string → [[Cheat Sheet de Instruções]] |
| **EFLAGS / RFLAGS** | registrador de flags → [[Cheat Sheet de Instruções]] |
| **Endereço efetivo** | endereço calculado por `base + índice*escala + deslocamento` → [[02 - Registradores e Memória]] |
| **Endianness** | ordem dos bytes de um valor em memória → [[02 - Registradores e Memória]] |
| **errno** | código de erro; syscalls devolvem `-errno` em `rax` → [[05 - Entrada-Saída e System Calls]] |
| **Exceção** | evento síncrono da CPU (`#DE`, `#GP`, `#PF`) → [[07 - Assembly Avançado (x86-x64)]] |
| **Fetch-decode-execute** | ciclo de busca, decodificação e execução → [[01 - Fundamentos de Arquitetura e Assembly]] |
| **Flags** | bits de estado (ZF, CF, SF, OF, PF, DF) → [[Cheat Sheet de Instruções]] |
| **Imediato** | valor constante codificado na instrução → [[02 - Registradores e Memória]] |
| **Interrupção** | evento assíncrono (dispositivo, temporizador) que desvia a CPU → [[07 - Assembly Avançado (x86-x64)]] |
| **ISA** | *Instruction Set Architecture*: o contrato entre software e processador → [[01 - Fundamentos de Arquitetura e Assembly]] |
| **LEA** | *load effective address*: calcula endereço sem acessar memória → [[Cheat Sheet de Instruções]] |
| **Little-endian** | byte menos significativo no menor endereço (x86, AArch64 típico) → [[02 - Registradores e Memória]] |
| **Load/store** | arquitetura em que só instruções de carga/escrita acessam memória (ARM) → [[08 - ARM e AArch64]] |
| **LR** | *link register* (`x30`/`r14`), guarda o endereço de retorno em ARM → [[08 - ARM e AArch64]] |
| **Mnemônico** | nome simbólico de uma instrução (`mov`, `add`) → [[01 - Fundamentos de Arquitetura e Assembly]] |
| **Modos de endereçamento** | formas de especificar um operando → [[02 - Registradores e Memória]] |
| **Opcode** | parte da instrução que indica a operação → [[01 - Fundamentos de Arquitetura e Assembly]] |
| **Overflow (OF)** | estouro de aritmética **com sinal** → [[03 - Instruções Básicas e Controle de Fluxo]] |
| **PC / RIP** | contador de programa: endereço da próxima instrução → [[01 - Fundamentos de Arquitetura e Assembly]] |
| **popcnt** | conta bits 1 → [[Cheat Sheet de Instruções]] |
| **Registrador** | memória interna da CPU, a mais rápida → [[02 - Registradores e Memória]] |
| **REP** | prefixo que repete instruções de string → [[Cheat Sheet de Instruções]] |
| **RIP-relative** | endereçamento relativo ao contador de programa → [[07 - Assembly Avançado (x86-x64)]] |
| **SIGSEGV / SIGFPE** | sinais de acesso inválido à memória / erro aritmético → [[Cheat Sheet de GDB]] |
| **Syscall** | pedido de serviço ao kernel → [[05 - Entrada-Saída e System Calls]] |
| **Thumb** | conjunto compacto de instruções (16/32 bits) da Arm → [[08 - ARM e AArch64]] |
| **Word / palavra** | unidade natural de dados (x86: 16 bits historicamente; ARM: 32 bits) → [[02 - Registradores e Memória]] |
| **Zeragem** (`xor r, r`) | idioma que zera um registrador sem dependência → [[09 - Otimização, SIMD e Performance]] |
| **Zero flag (ZF)** | ligada quando o resultado é zero → [[Cheat Sheet de Instruções]] |

### Sintaxe, montadores e depuração

| Termo | Definição |
|---|---|
| **AT&T (sintaxe)** | sintaxe do GAS: origem primeiro, `%reg`, `$imm` → [[01 - Fundamentos de Arquitetura e Assembly]] |
| **Breakpoint** | ponto de parada do depurador (`int3`, 0xCC) → [[Cheat Sheet de GDB]] |
| **CFI** (DWARF) | informações de quadro de chamada para desenrolar a pilha → [[07 - Assembly Avançado (x86-x64)]] |
| **Cross-compilation** | compilar para outra arquitetura → [[08 - ARM e AArch64]] |
| **DWARF** | formato de informações de depuração → [[Cheat Sheet de GDB]] |
| **GAS** | GNU Assembler (`as`) → [[01 - Fundamentos de Arquitetura e Assembly]] |
| **GDB** | depurador do projeto GNU → [[Cheat Sheet de GDB]] |
| **Intel (sintaxe)** | destino primeiro: `mov rax, rbx` → [[01 - Fundamentos de Arquitetura e Assembly]] |
| **Linker (ligador)** | junta objetos e resolve símbolos (`ld`) → [[05 - Entrada-Saída e System Calls]] |
| **llvm-mca** | simulador de pipeline → [[09 - Otimização, SIMD e Performance]] |
| **MASM** | *Microsoft Macro Assembler* → [[01 - Fundamentos de Arquitetura e Assembly]] |
| **NASM** | *Netwide Assembler* (sintaxe Intel) → [[00 - Índice]] |

### Programa na memória e formatos

| Termo | Definição |
|---|---|
| **Alinhamento** | exigência de que um endereço seja múltiplo de um tamanho (4, 8, 16, 32, 64) → [[02 - Registradores e Memória]] |
| **ASLR** | sorteio dos endereços de pilha, *heap* e bibliotecas a cada execução → [[07 - Assembly Avançado (x86-x64)]] |
| **BSS** | seção de dados **não inicializados** (zerados pelo carregador) → [[02 - Registradores e Memória]] |
| **ELF** | formato de executáveis, objetos e bibliotecas no Linux → [[05 - Entrada-Saída e System Calls]] |
| **GOT / PLT** | tabelas para endereços e chamadas dinâmicas em código independente de posição → [[07 - Assembly Avançado (x86-x64)]] |
| **Heap** | região para alocação dinâmica (`malloc`) → [[06 - Estruturas de Dados e Arrays]] |
| **Padding** | bytes de enchimento para alinhar campos ou quebrar conflitos de cache → [[06 - Estruturas de Dados e Arrays]] |
| **Página** | unidade de memória virtual (4 KiB) → [[09 - Otimização, SIMD e Performance]] |
| **PIC / PIE** | código / executável independente de posição → [[07 - Assembly Avançado (x86-x64)]] |
| **Seção** | parte do arquivo (`.text`, `.data`, `.rodata`, `.bss`) → [[02 - Registradores e Memória]] |
| **Stack / pilha** | região LIFO usada em chamadas e variáveis locais → [[04 - Procedimentos, Stack e Calling Conventions]] |
| **TLB** | cache de traduções de endereços virtuais → [[07 - Assembly Avançado (x86-x64)]] |
| **TLS** | *thread-local storage* (`fs:`/`gs:`) → [[07 - Assembly Avançado (x86-x64)]] |
| **Virtual (memória)** | espaço de endereços por processo mapeado a RAM → [[05 - Entrada-Saída e System Calls]] |

### Chamadas de procedimento e pilha

| Termo | Definição |
|---|---|
| **ABI** (*Application Binary Interface*) | contrato binário: convenção de chamada, layout de dados, formato de objetos, nomes de símbolos → [[04 - Procedimentos, Stack e Calling Conventions]] |
| **Callee-saved** | registradores que a **função chamada** precisa preservar → [[Cheat Sheet de Calling Conventions]] |
| **Caller-saved** | registradores que a **chamadora** deve salvar se precisar deles → [[Cheat Sheet de Calling Conventions]] |
| **cdecl / stdcall / fastcall** | convenções de chamada de 32 bits → [[Cheat Sheet de Calling Conventions]] |
| **Epílogo** | final de uma função (restaurar pilha e registradores; `ret`) → [[04 - Procedimentos, Stack e Calling Conventions]] |
| **Frame / quadro de pilha** (*stack frame*) | região da pilha de uma chamada → [[04 - Procedimentos, Stack e Calling Conventions]] |
| **Frame pointer** | registrador (`rbp`/`x29`) que aponta para o quadro da função → [[04 - Procedimentos, Stack e Calling Conventions]] |
| **Prólogo** | início de uma função (criar o quadro, salvar registradores) → [[04 - Procedimentos, Stack e Calling Conventions]] |
| **Red zone** | 128 bytes abaixo de `rsp` que folhas podem usar (System V) → [[Cheat Sheet de Calling Conventions]] |
| **Ret / retorno** | desempilha o endereço e salta → [[04 - Procedimentos, Stack e Calling Conventions]] |
| **Shadow space** | 32 bytes que o chamador reserva no Windows x64 → [[Cheat Sheet de Calling Conventions]] |
| **Tail call** | chamada final trocada por salto → [[04 - Procedimentos, Stack e Calling Conventions]] |
| **Variádica** | função com número variável de argumentos (`printf`) → [[Cheat Sheet de Calling Conventions]] |

### Segurança de memória

| Termo | Definição |
|---|---|
| **Buffer overflow** | escrita além do fim de um buffer → [[04 - Procedimentos, Stack e Calling Conventions]] |
| **CET** | tecnologia de controle de fluxo da Intel (*shadow stack*, `endbr64`) → [[07 - Assembly Avançado (x86-x64)]] |
| **ROP** | *return-oriented programming*, técnica de exploração → [[11 - Recursos e Referências]] |
| **SEH** | *Structured Exception Handling* do Windows → [[07 - Assembly Avançado (x86-x64)]] |

### Desempenho e microarquitetura

| Termo | Definição |
|---|---|
| **AoS / SoA** | *Array of Structures* / *Structure of Arrays*: dois layouts; SoA favorece SIMD → [[06 - Estruturas de Dados e Arrays]] |
| **Branch / desvio** | instrução que pode alterar o fluxo (`jcc`) → [[03 - Instruções Básicas e Controle de Fluxo]] |
| **Branch predictor** | circuito que adivinha o resultado de desvios; erro custa ~15-20 ciclos → [[09 - Otimização, SIMD e Performance]] |
| **Cache** | memória pequena e rápida entre CPU e RAM (L1, L2, L3), em **linhas de 64 bytes** → [[09 - Otimização, SIMD e Performance]] |
| **Cache line** | unidade de transferência do cache (64 bytes em x86 e na maioria dos Arm) → [[06 - Estruturas de Dados e Arrays]] |
| **Conflict miss** | *miss* de cache causado por muitos endereços no mesmo conjunto (passo potência de 2) → [[09 - Otimização, SIMD e Performance]] |
| **Dependência de dados** | uma instrução precisa do resultado da anterior → [[09 - Otimização, SIMD e Performance]] |
| **Desvio previsível** | desvio cujo resultado segue padrão (barato) → [[09 - Otimização, SIMD e Performance]] |
| **ERMSB / FSRM** | otimizações de `rep movsb`/`rep stosb` em CPUs recentes → [[09 - Otimização, SIMD e Performance]] |
| **False sharing** | duas *threads* escrevendo em variáveis diferentes na mesma linha de cache → [[09 - Otimização, SIMD e Performance]] |
| **Hazard** | situação que impede o pipeline de avançar: dados, controle ou estrutural → [[09 - Otimização, SIMD e Performance]] |
| **Hit / miss** | acerto / falha de cache → [[09 - Otimização, SIMD e Performance]] |
| **ILP** | *Instruction-Level Parallelism* → [[09 - Otimização, SIMD e Performance]] |
| **Latência** | ciclos até o resultado de uma instrução ficar disponível → [[09 - Otimização, SIMD e Performance]] |
| **Localidade** | tendência de reutilizar dados próximos no tempo (temporal) e no espaço (espacial) → [[09 - Otimização, SIMD e Performance]] |
| **Macro-fusão** | `cmp`/`test` + `jcc` virando uma única µop → [[09 - Otimização, SIMD e Performance]] |
| **Número mágico** | constante para dividir por constante via multiplicação → [[09 - Otimização, SIMD e Performance]] |
| **µop** (micro-operação) | operação interna em que a instrução é decodificada → [[09 - Otimização, SIMD e Performance]] |
| **Out-of-order** | execução fora da ordem do programa → [[09 - Otimização, SIMD e Performance]] |
| **Pipeline** | execução de várias instruções em estágios sobrepostos → [[09 - Otimização, SIMD e Performance]] |
| **Pointer chasing** | seguir ponteiros em sequência (lista encadeada): cada leitura depende da anterior → [[09 - Otimização, SIMD e Performance]] |
| **Prefetch** | trazer dados ao cache antes do uso → [[09 - Otimização, SIMD e Performance]] |
| **Renomeação de registradores** | remoção de dependências falsas de nome → [[09 - Otimização, SIMD e Performance]] |
| **Store forwarding** | entrega direta do dado escrito a uma leitura posterior → [[09 - Otimização, SIMD e Performance]] |
| **Stride / passo** | distância entre acessos sucessivos → [[09 - Otimização, SIMD e Performance]] |
| **Superescalar** | executa várias instruções por ciclo → [[09 - Otimização, SIMD e Performance]] |
| **Throughput / vazão** | quantas instruções do mesmo tipo por ciclo → [[09 - Otimização, SIMD e Performance]] |

### SIMD e ponto flutuante

| Termo | Definição |
|---|---|
| **AVX / AVX2 / AVX-512** | extensões SIMD de 256/256/512 bits → [[07 - Assembly Avançado (x86-x64)]] |
| **Dispatch** | escolha da versão de uma função em tempo de execução (por `cpuid`) → [[09 - Otimização, SIMD e Performance]] |
| **FMA** | *fused multiply-add*: `a*b+c` com um só arredondamento → [[07 - Assembly Avançado (x86-x64)]] |
| **Gather / scatter** | carga/escrita SIMD de endereços arbitrários (lentas, usar com cuidado) → [[09 - Otimização, SIMD e Performance]] |
| **Intrínseco** | função C que compila para uma instrução específica (`_mm_add_ps`) → [[09 - Otimização, SIMD e Performance]] |
| **NaN** | *Not a Number* (ponto flutuante) → [[07 - Assembly Avançado (x86-x64)]] |
| **NEON** | SIMD de 128 bits da Arm → [[08 - ARM e AArch64]] |
| **Redução** | combinar muitos valores em um (soma, máximo) → [[09 - Otimização, SIMD e Performance]] |
| **SIMD** | uma instrução sobre vários dados → [[07 - Assembly Avançado (x86-x64)]] |
| **SWAR** | *SIMD within a register*: paralelismo de bits em registradores comuns → [[09 - Otimização, SIMD e Performance]] |
| **Vetorização** | transformar laço escalar em SIMD → [[09 - Otimização, SIMD e Performance]] |
| **vzeroupper** | zera a metade alta dos `ymm`, evitando penalidade AVX/SSE → [[07 - Assembly Avançado (x86-x64)]] |
| **x87** | unidade de ponto flutuante clássica (`st0`-`st7`) → [[07 - Assembly Avançado (x86-x64)]] |
| **XMM / YMM / ZMM** | registradores SIMD de 128 / 256 / 512 bits → [[07 - Assembly Avançado (x86-x64)]] |

**Veja também:** [[Cheat Sheet de Instruções]] · [[Cheat Sheet de Calling Conventions]] · [[Cheat Sheet de GDB]] · [[11 - Recursos e Referências]]


## Python

Voltar ao índice: [[00 - Índice Python]].

### Fundamentos da linguagem

| Termo | Definição |
|---|---|
| **Built-in** | Função/tipo disponível sem `import` (`len`, `print`, `list`…). |
| **Comprehension** | Sintaxe compacta para criar list/set/dict/generator. → [[02 - Controle de Fluxo e Estruturas de Dados/07 - Comprehensions\|Comprehensions]] |
| **Dict** | Mapeamento chave → valor, com ordem de inserção preservada. → [[02 - Controle de Fluxo e Estruturas de Dados/06 - Dicionários\|Dicionários]] |
| **Docstring** | String de documentação no início de módulo/classe/função. → [[03 - Funções e Modularização/06 - Docstrings\|Docstrings]] |
| **Escopo** | Região onde um nome é visível (regra **LEGB**: Local, Enclosing, Global, Built-in). |
| **f-string** | String formatada com `f"{valor}"`. → [[01 - Fundamentos/05 - Entrada e Saída\|Entrada e Saída]] |
| **Hashable** | Objeto com `__hash__` estável; necessário para chaves de `dict` e itens de `set`. |
| **Idempotente** | Operação que, repetida, produz o mesmo efeito de uma única execução. |
| **Imutável** | Não pode ser modificado após criado (`int`, `str`, `tuple`, `frozenset`). |
| **Interpretador** | Programa que executa o código (REPL = laço Ler-Avaliar-Imprimir). |
| **Namespace** | Mapeamento de nomes para objetos (módulo, função, classe, instância). |
| **None** | Único valor do tipo `NoneType`; indica ausência de valor. |
| **Objeto** | Instância de uma classe; em Python, *tudo* é objeto. |
| **Pythônico** | Código que segue os idiomas da comunidade ("The Zen of Python"). |
| **Referência** | "Seta" de um nome para um objeto; atribuir **não copia** o objeto. → [[08 - Avançado/04 - CPython Internals\|CPython]] |
| **REPL** | Interpretador interativo (`python` sem argumentos). |
| **Scope (LEGB)** | Ver *Escopo*. |
| **Sentinela** | Valor especial (ex.: `None`, `object()`) usado para sinalizar "não informado". |
| **Slice** | Fatiamento `seq[início:fim:passo]`. |
| **Tipagem dinâmica** | Tipos pertencem aos valores, não às variáveis. |
| **Tupla** | Sequência imutável. |
| **Walrus (`:=`)** | Operador de atribuição em expressão. |
| **Zen of Python** | 19 aforismos de design (`import this`). |

### Funções e programação funcional

| Termo | Definição |
|---|---|
| **Argumento** | Valor passado a uma função na chamada. (*Parâmetro* é o nome na definição.) → [[03 - Funções e Modularização/02 - args kwargs e Argumentos Padrão\|args/kwargs]] |
| **Callable** | Qualquer objeto que pode ser chamado com `()` (funções, classes, objetos com `__call__`). → [[07 - Programação Funcional e Intermediário/01 - Funções de Ordem Superior\|Ordem Superior]] |
| **Closure** | Função que "lembra" variáveis do escopo onde foi criada. → [[03 - Funções e Modularização/03 - Escopo e Closures\|Closures]] |
| **Decorator** | Função que recebe uma função e devolve outra, "embrulhando" seu comportamento (`@nome`). → [[07 - Programação Funcional e Intermediário/03 - Decorators\|Decorators]] |
| **First-class function** | Função tratada como valor: pode ser atribuída, passada e retornada. |
| **Função de ordem superior** | Função que recebe ou devolve funções. |
| **Generator** | Função com `yield` (ou expressão `( ... for ...)`) que produz valores sob demanda. → [[07 - Programação Funcional e Intermediário/04 - Generators e Iterators\|Generators]] |
| **Iterável / Iterador** | Iterável pode ser percorrido por `for` (`__iter__`); iterador entrega o próximo valor (`__next__`). |
| **kwargs** | `**kwargs`: argumentos nomeados coletados em um `dict`. |
| **Lambda** | Função anônima de uma única expressão. → [[07 - Programação Funcional e Intermediário/02 - Lambda map filter reduce\|Lambda]] |
| **Lazy evaluation** | Calcular apenas quando o valor é necessário. |
| **Memoização** | Guardar resultados de chamadas para não recalcular (`functools.cache`). |
| **Parâmetro** | Nome na assinatura da função. |
| **`yield`** | Entrega um valor e pausa a função geradora. |

### Orientação a objetos

| Termo | Definição |
|---|---|
| **ABC** (*Abstract Base Class*) | Classe base que define métodos obrigatórios para as subclasses (módulo `abc`). → [[04 - Programação Orientada a Objetos/03 - Herança Polimorfismo e Encapsulamento\|Herança]] |
| **Atributo** | Variável associada a um objeto ou classe (`obj.nome`). → [[04 - Programação Orientada a Objetos/02 - Atributos e Métodos\|Atributos]] |
| **Classe** | Molde que define atributos e métodos de objetos. → [[04 - Programação Orientada a Objetos/01 - Classes e Objetos\|Classes]] |
| **Dataclass** | Classe que gera `__init__`, `__repr__`, `__eq__` a partir de anotações. → [[04 - Programação Orientada a Objetos/05 - Dataclasses e Slots\|Dataclasses]] |
| **Descriptor** | Objeto com `__get__`/`__set__`/`__delete__` que controla acesso a atributos (base de `property`). → [[08 - Avançado/01 - Metaprogramação\|Metaprogramação]] |
| **Duck typing** | "Se anda como pato e grasna como pato…": importa o comportamento, não o tipo. → [[07 - Programação Funcional e Intermediário/06 - Type Hints e typing\|Protocol]] |
| **Dunder** | Método com nomes entre `__duplo_sublinhado__` (*double underscore*). → [[04 - Programação Orientada a Objetos/04 - Propriedades e Métodos Mágicos\|Métodos mágicos]] |
| **Herança** | Subclasse reutiliza e estende uma classe base. |
| **Metaclasse** | "Classe de uma classe": controla a criação de classes (`type` é a padrão). → [[08 - Avançado/01 - Metaprogramação\|Metaprogramação]] |
| **Método** | Função definida dentro de uma classe. |
| **MRO** (*Method Resolution Order*) | Ordem em que Python procura métodos em hierarquias com herança múltipla (`Classe.__mro__`). |
| **Overriding** | Subclasse redefine um método da base (`@override`). |
| **Polimorfismo** | Objetos diferentes respondendo à mesma interface. |
| **Property** | Atributo calculado/validado por getter/setter. → [[04 - Programação Orientada a Objetos/04 - Propriedades e Métodos Mágicos\|Propriedades]] |
| **Protocol** | Interface estrutural (duck typing tipado) do módulo `typing`. |
| **Slots** | `__slots__`: fixa atributos da instância, reduzindo memória. → [[04 - Programação Orientada a Objetos/05 - Dataclasses e Slots\|Slots]] |

### Erros e gerenciamento de recursos

| Termo | Definição |
|---|---|
| **Context manager** | Objeto usado com `with`, que prepara e libera recursos. → [[05 - Tratamento de Erros e Arquivos/04 - Context Managers com with\|with]] · [[07 - Programação Funcional e Intermediário/05 - Context Managers Avançados\|avançados]] |
| **EAFP** | *Easier to Ask Forgiveness than Permission*: tente e trate a exceção (estilo Pythônico). Oposto: **LBYL** (*Look Before You Leap*). → [[05 - Tratamento de Erros e Arquivos/01 - try except else finally\|try/except]] |
| **Exceção** | Objeto que representa um erro; interrompe o fluxo até ser tratado. |
| **Traceback** | Relatório da pilha de chamadas no momento de um erro. |

### Execução interna e concorrência

| Termo | Definição |
|---|---|
| **Async / await** | Sintaxe para corrotinas: `async def` define; `await` cede o controle enquanto espera. → [[08 - Avançado/02 - Asyncio\|Asyncio]] |
| **Bytecode** | Instruções intermediárias geradas pelo CPython e executadas pela máquina virtual (`dis`). → [[08 - Avançado/04 - CPython Internals\|CPython]] |
| **Corrotina** | Função `async def`; execução pode ser suspensa e retomada. |
| **CPython** | Implementação de referência do Python, escrita em C. |
| **Event loop** | Laço que agenda e executa corrotinas no `asyncio`. |
| **Garbage collector (GC)** | Mecanismo que libera ciclos de referências não alcançáveis. → [[08 - Avançado/04 - CPython Internals\|CPython]] |
| **GIL** (*Global Interpreter Lock*) | Trava do CPython que permite que só uma thread execute bytecode Python por vez (em builds padrão). → [[08 - Avançado/03 - Multiprocessing\|Multiprocessing]] |
| **Reference counting** | Contagem de referências usada pelo CPython para liberar memória. |
| **Thread / Processo** | Fluxos de execução; threads compartilham memória, processos não. → [[06 - Módulos da Biblioteca Padrão Essenciais/06 - concurrent futures e threading\|Threading]] |

### Módulos, pacotes e ferramentas

| Termo | Definição |
|---|---|
| **Generics** | Tipos parametrizados (`list[int]`, `class Caixa[T]`). |
| **Import** | Carrega um módulo/pacote. → [[03 - Funções e Modularização/04 - Módulos e Packages\|Módulos e Packages]] |
| **Linter** | Ferramenta que aponta erros e problemas de estilo sem executar o código (ex.: Ruff, Flake8). |
| **Mock** | Objeto falso usado em testes. → [[08 - Avançado/06 - Testes com unittest e pytest\|Testes]] |
| **Módulo / Pacote** | Arquivo `.py` / diretório de módulos. |
| **PEP** | *Python Enhancement Proposal*: documento de proposta/padrão da linguagem. → [[10 - Recursos e Referências/02 - Sites e Documentação Oficial\|PEPs]] |
| **pip** | Instalador de pacotes (PyPI). → [[03 - Funções e Modularização/05 - Virtual Environments e pip\|pip]] |
| **PyPI** | *Python Package Index*, repositório público de pacotes. |
| **Type hint** | Anotação de tipo, verificada por ferramentas externas. → [[07 - Programação Funcional e Intermediário/06 - Type Hints e typing\|Type Hints]] |
| **Venv** | Ambiente virtual isolado de dependências. |
| **Virtualenv / pyproject.toml** | Ferramental de ambientes e metadados do projeto. → [[08 - Avançado/07 - Packaging e Distribuição\|Packaging]] |
| **Wheel (`.whl`)** | Formato binário de distribuição de pacotes. |

**Veja também:** [[10 - Recursos e Referências/04 - Cheat Sheets|Cheat Sheets]] · [[09 - Projetos Práticos/Projeto 08 - Projeto Final|Projeto final]]


## Rust

Voltar ao índice: [[Índice geral - Rust]].

### Ownership e memória

| Termo | Definição |
|---|---|
| **Alocador** | Componente que fornece memória do heap → [[Alocadores e memória]] |
| **Arc** | Contador de referências atômico, compartilhável entre threads → [[Arc]] |
| **Borrow** | Empréstimo: uso temporário de um valor por referência → [[Borrowing e referências]] |
| **Borrow checker** | Parte do compilador que valida empréstimos → [[Regras do borrow checker]] |
| **Box** | Ponteiro inteligente para um valor no heap → [[Box]] |
| **Drop** | Trait executada quando um valor sai de escopo → [[Drop e RAII]] |
| **Elisão** | Omissão de lifetimes seguindo regras fixas → [[Elisão de lifetimes]] |
| **Heap** | Região de memória de alocação dinâmica → [[Stack, heap e layout de memória]] |
| **Lifetime** | Região do programa em que uma referência é válida → [[Lifetimes]] |
| **Move** | Transferência de ownership → [[Move, Copy e Clone]] |
| **NLL** | Lifetimes não lexicais: empréstimos terminam no último uso → [[NLL]] |
| **Ownership** | Cada valor tem exatamente um dono → [[Ownership e regras]] |
| **RAII** | Recursos presos ao tempo de vida de valores → [[Drop e RAII]] |
| **Rc** | Contador de referências de uma só thread → [[Rc]] |
| **Slice** | Visão de uma sequência contígua (`&[T]`, `&str`) → [[Slices]] |
| **Stack** | Pilha de chamadas → [[Stack, heap e layout de memória]] |
| **Weak** | Referência fraca que não mantém o valor vivo → [[Weak e ciclos de referência]] |

### Tipos, traits e genéricos

| Termo | Definição |
|---|---|
| **Associated type** | Tipo declarado dentro de uma trait → [[Tipos associados]] |
| **Closure** | Função anônima que captura o ambiente → [[Closures]] |
| **Coerção** | Conversão implícita de tipos (ex.: `&String` para `&str`) → [[Deref e AsRef]] |
| **Derive** | Geração automática de implementações de traits → [[derive]] |
| **dyn Trait** | Objeto de trait: despacho dinâmico → [[impl Trait e dyn Trait]] |
| **Enum** | Tipo soma: um valor entre várias variantes → [[Enums]] |
| **GAT** | Tipo associado genérico → [[GATs]] |
| **Genérico** | Código parametrizado por tipos → [[Genéricos]] |
| **Iterator** | Trait de sequências consumíveis item a item → [[Iteradores]] |
| **Macro** | Código que gera código → [[macro_rules]] |
| **Monomorfização** | Geração de uma cópia especializada de código genérico por tipo concreto → [[Zero-cost abstractions]] |
| **Orphan rule** | Regra de coerência: trait ou tipo deve ser local para implementar → [[Orphan rule]] |
| **Pattern** | Forma de desestruturar e testar valores → [[Pattern matching avançado]] |
| **Trait** | Conjunto de comportamentos que tipos podem implementar → [[Traits]] |
| **Trait object** | Valor `dyn Trait` atrás de ponteiro → [[Object safety]] |
| **Turbofish** | Sintaxe `::<T>` para indicar tipos explicitamente → [[Genéricos]] |
| **Typestate** | Estado codificado no tipo → [[Typestate]] |
| **Zero-cost abstraction** | Abstração sem custo em tempo de execução → [[Zero-cost abstractions]] |

### Erros e valores opcionais

| Termo | Definição |
|---|---|
| **Option** | Valor opcional: `Some(T)` ou `None` → [[Option e Result]] |
| **Panic** | Falha irrecuperável do programa → [[Panic]] |
| **Result** | Valor de sucesso ou erro: `Ok(T)` ou `Err(E)` → [[Option e Result]] |

### Concorrência e async

| Termo | Definição |
|---|---|
| **async / await** | Sintaxe para funções que podem ser suspensas → [[Async e await]] |
| **Atômico** | Tipo cujas operações são indivisíveis entre threads → [[Atômicos]] |
| **Data race** | Acesso concorrente a um dado, ao menos um sendo escrita, sem sincronização → [[Data races]] |
| **Executor** | Motor que executa futures até o fim → [[Executores e runtimes]] |
| **Future** | Valor que representa uma computação assíncrona → [[Future e Poll]] |
| **Mutex** | Exclusão mútua para dados compartilhados → [[Mutex e RwLock]] |
| **Pin** | Impede que um valor seja movido na memória → [[Pin]] |
| **Send** | Marca tipos que podem ser movidos para outra thread → [[Send e Sync]] |
| **Sync** | Marca tipos cujas referências podem ser compartilhadas entre threads → [[Send e Sync]] |

### Ferramentas, compilação e ecossistema

| Termo | Definição |
|---|---|
| **Binário (crate)** | Crate que gera um executável (`main.rs`) → [[Packages, crates e módulos]] |
| **Cargo** | Gerenciador de pacotes e ferramenta de build → [[Cargo básico]] |
| **Clippy** | Linter oficial → [[Clippy]] |
| **Crate** | Unidade de compilação e de distribuição → [[Packages, crates e módulos]] |
| **crates.io** | Registro público de crates → [[Publicar no crates.io]] |
| **Edição** | Versão de compatibilidade da linguagem (2015, 2018, 2021, 2024) → [[Edições do Rust]] |
| **Feature** | Flag de compilação condicional de um crate → [[Features de Cargo]] |
| **LTO** | Otimização em tempo de link entre crates → [[Release profile LTO e codegen]] |
| **MIR** | Representação intermediária do compilador usada pelo borrow checker e pelo Miri → [[Miri]] |
| **no_std** | Programa sem a biblioteca padrão → [[Embarcados e no_std]] |
| **rustc** | O compilador → [[Pipeline de compilação]] |
| **rustup** | Instalador e gerenciador de toolchains → [[Instalação com rustup]] |
| **Workspace** | Conjunto de crates que compartilham `Cargo.lock` e `target` → [[Workspaces - Rust]] |

### Unsafe e interoperabilidade

| Termo | Definição |
|---|---|
| **ABI** | Convenção binária de chamada entre códigos compilados (`extern "C"`) → [[FFI com C e C++]] |
| **FFI** | Interface com código de outras linguagens → [[FFI com C e C++]] |
| **unsafe** | Bloco em que você garante manualmente invariantes → [[Unsafe Rust]] |

**Veja também:** [[Cheat sheet de sintaxe]] · [[Tabela de erros do compilador]] · [[FAQ - Rust]]

## C++

Voltar ao índice: [[Home - Cpp]].

### Memória e ciclo de vida

| Termo | Definição |
|---|---|
| **Alinhamento** (`alignof`) | Endereços múltiplos de N exigidos por um tipo → [[sizeof e alignof]] |
| **Alocador** | Objeto que fornece memória a contêineres → [[Alocadores e pmr]] |
| **Copy elision** | Omissão de cópias/movimentos pelo compilador → [[Copy Elision e RVO]] |
| **Dangling** | Referência/ponteiro/view para objeto destruído → [[Vazamentos e Dangling Pointers]] |
| **Deleter** | Função que libera o recurso de um smart pointer → [[Deleters Customizados]] |
| **Destrutor** | Função chamada ao fim da vida do objeto → [[Construtores e Destrutores]] |
| **Heap** (*free store*) | Memória de alocação dinâmica → [[Stack vs Heap]] |
| **Move** | Transferência de recursos em vez de cópia → [[Semântica de Movimento]] |
| **RAII** | Recurso preso à vida de um objeto → [[RAII]] |
| **RVO / NRVO** | Otimização do valor de retorno → [[Copy Elision e RVO]] |
| **SBO / SSO** | Otimização de buffer pequeno → [[std string em Profundidade]] |
| **Smart pointer** | Ponteiro com posse automática → [[unique_ptr]] |
| **Special member functions** | Construtores, atribuições e destrutor → [[Regra do 0, 3 e 5]] |
| **Stack** (pilha) | Memória de variáveis automáticas → [[Stack vs Heap]] |

### Tipos, templates e metaprogramação

| Termo | Definição |
|---|---|
| **Aggregate** (agregado) | Tipo sem construtores definidos pelo usuário, inicializável com `{}` → [[Variáveis e Inicialização]] |
| **auto** | Dedução de tipo da variável → [[auto e decltype]] |
| **Concept** | Predicado de compilação que restringe templates → [[Concepts e requires]] |
| **constexpr / consteval / constinit** | Avaliação em compilação / obrigatória / inicialização constante → [[constexpr consteval constinit]] |
| **CRTP** | Classe base parametrizada pela derivada (polimorfismo estático) → [[CRTP e Mixins]] |
| **CTAD** | Dedução de argumentos de template de classe → [[CTAD]] |
| **decltype** | Tipo de uma expressão/entidade → [[auto e decltype]] |
| **explicit** | Proíbe conversão implícita por um construtor/operador → [[Conversões Implícitas e explicit]] |
| **Forwarding reference** | `T&&` deduzido: aceita lvalues e rvalues → [[Referências Universais e Perfect Forwarding]] |
| **Lambda** | Objeto-função anônimo com capturas → [[Lambdas e Captura]] |
| **lvalue / rvalue** | Expressão com identidade / temporária movível → [[Lvalue e Rvalue]] |
| **Perfect forwarding** | Encaminhar argumentos preservando categoria de valor → [[std move e std forward]] |
| **POD / trivial / standard-layout** | Categorias de tipos simples → [[Layout de Memória de um Programa]] |
| **SFINAE** | Falha de substituição não é erro → [[SFINAE e enable_if]] |
| **Structured binding** | `auto [a, b] = ...` → [[Structured Bindings]] |
| **Type erasure** | Esconder o tipo concreto atrás de uma interface → [[Type Erasure]] |

### Compilação e linkage

| Termo | Definição |
|---|---|
| **ABI** | Contrato binário: layout, convenção de chamada, *mangling* → [[ABI]] |
| **ADL** (*Argument-Dependent Lookup*) | Busca de funções também nos namespaces dos argumentos → [[Namespaces - Cpp]] |
| **Declaração / definição** | Apresenta um nome / cria a entidade → [[Declaração vs Definição e ODR]] |
| **Header** | Arquivo de declarações incluído por várias TUs → [[Headers vs Sources]] |
| **inline** | Permite múltiplas definições idênticas (e sugere inlining) → [[Argumentos Padrão e inline]] |
| **Linkage** | Visibilidade de nomes entre TUs → [[Linkage]] |
| **Name mangling** | Codificação de nomes de símbolos C++ → [[ABI]] |
| **Namespace** | Escopo nomeado → [[Namespaces - Cpp]] |
| **ODR** | Regra de uma definição → [[Declaração vs Definição e ODR]] |
| **Overload** | Várias funções com o mesmo nome e parâmetros diferentes → [[Sobrecarga de Funções]] |
| **TU** (*translation unit*) | Um `.cpp` com seus includes expandidos → [[Headers vs Sources]] |

### Biblioteca padrão e ranges

| Termo | Definição |
|---|---|
| **Invalidação de iteradores** | Operações que tornam iteradores inválidos → [[Complexidade e Invalidação de Iteradores]] |
| **Range** | Sequência com `begin`/`end` → [[Ranges e Views]] |
| **STL** | Contêineres, iteradores e algoritmos → [[Visão Geral da STL]] |
| **View** | Range leve e não proprietário → [[Ranges e Views]] |

### Concorrência

| Termo | Definição |
|---|---|
| **Atomic** | Tipo com operações indivisíveis entre threads → [[Atomics e Modelo de Memória]] |
| **Data race** | Acesso concorrente não sincronizado com escrita (UB) → [[Data Races e Deadlocks]] |

### Orientação a objetos e boas práticas

| Termo | Definição |
|---|---|
| **const correctness** | Marcar como `const` tudo que não muda → [[const em Métodos]] |
| **Exception safety** | Garantias básicas/fortes/*nothrow* diante de exceções → [[Segurança de Exceções]] |
| **Idiom** | Solução recorrente (RAII, pimpl, copy-and-swap...) → [[Idiomas e Padrões de Projeto em Cpp]] |
| **noexcept** | Promessa de não lançar exceção → [[noexcept e Movimento]] |
| **override / final** | Marcam sobrescrita e fim da hierarquia virtual → [[override e final]] |
| **Pimpl** | Ponteiro para implementação (esconde detalhes) → [[Pimpl]] |
| **RTTI** | Informação de tipo em execução (`typeid`, `dynamic_cast`) → [[Polimorfismo e Funções Virtuais]] |
| **Slicing** | Perda da parte derivada ao copiar por valor → [[Slicing]] |
| **UB** | Comportamento indefinido → [[Comportamento Indefinido e Não Especificado]] |
| **vtable** | Tabela de funções virtuais → [[vtable]] |

**Veja também:** [[Cheat Sheet de Sintaxe - Cpp]] · [[Cheat Sheet da STL]] · [[Comportamento Indefinido e Não Especificado]]

## Sistemas Operacionais

Voltar ao índice: [[Índice Geral - SO]].

### Processos e threads

| Termo | Definição |
|---|---|
| **Context switch** | Troca de contexto entre processos/threads ([[Context Switch (Troca de Contexto)]]) |
| **Fork** | Cria processo filho copiando o pai ([[Criação e Término de Processos]]) |
| **IPC** | Comunicação entre processos ([[IPC - Comunicação entre Processos]]) |
| **PCB** | Bloco de controle de processo ([[PCB - Process Control Block]]) |
| **Pipe** | Canal unidirecional entre processos ([[Pipes]]) |
| **Preempção** | Retirada forçada da CPU ([[Escalonamento de Processos]]) |
| **Sinal** | Notificação assíncrona a um processo ([[Sinais]]) |
| **Thread** | Fluxo de execução dentro de um processo ([[Threads - SO]]) |
| **Zumbi** | Processo terminado cujo pai não coletou o status ([[Estados de Processo]]) |

### Escalonamento

| Termo | Definição |
|---|---|
| **CFS** | Escalonador justo do Linux ([[CFS - Completely Fair Scheduler]]) |
| **MLFQ** | Fila multinível com realimentação ([[MLFQ - Multilevel Feedback Queue]]) |
| **Round Robin** | Escalonamento circular por quantum ([[Round Robin]]) |

### Sincronização

| Termo | Definição |
|---|---|
| **Atomicidade** | Operação indivisível ([[Operações Atômicas e Spinlocks]]) |
| **Banker's algorithm** | Algoritmo de evitação de deadlock ([[Deadlock (Impasse)]]) |
| **Deadlock** | Impasse circular entre processos ([[Deadlock (Impasse)]]) |
| **Futex** | Mutex rápido no espaço de usuário com apoio do kernel ([[Mutex]]) |
| **Monitor** | Construção de sincronização com exclusão mútua embutida ([[Monitores e Variáveis de Condição]]) |
| **Mutex** | Trava de exclusão mútua ([[Mutex]]) |
| **Race condition** | Resultado depende da ordem de execução ([[Condições de Corrida]]) |
| **Semáforo** | Contador de sincronização ([[Semáforos]]) |
| **Spinlock** | Trava com espera ocupada ([[Operações Atômicas e Spinlocks]]) |

### Memória

| Termo | Definição |
|---|---|
| **Buddy system** | Alocador de páginas em potências de 2 ([[Alocadores de Memória]]) |
| **Cache de página** | Cache de arquivos em RAM ([[Buffering, Cache e Spooling]]) |
| **CoW (Copy-on-Write)** | Copia só ao modificar ([[Journaling e Copy-on-Write]], [[Btrfs]]) |
| **Memória virtual** | Abstração de espaço de endereços maior que a RAM ([[Memória Virtual]]) |
| **Page fault** | Acesso a página não residente ([[Page Faults]]) |
| **Paginação** | Divisão em páginas de tamanho fixo ([[Paginação]]) |
| **Segmentação** | Divisão por segmentos lógicos ([[Segmentação]]) |
| **Swap** | Área em disco que estende a RAM ([[Swap e Thrashing]]) |
| **TLB** | Cache de traduções de endereço ([[TLB - Translation Lookaside Buffer]]) |

### Arquivos e entrada e saída

| Termo | Definição |
|---|---|
| **ACL** | Lista de controle de acesso por objeto, mais fina que rwx ([[Permissões de Arquivos]]) |
| **DMA** | Transferência direta de memória sem CPU ([[DMA - Acesso Direto à Memória]]) |
| **Driver** | Software que controla um dispositivo ([[Drivers de Dispositivo]]) |
| **Inode** | Metadados de um arquivo no UNIX ([[Inodes]]) |
| **Interrupção** | Sinal assíncrono ao processador ([[Interrupções]]) |
| **Journaling** | Registro prévio de mudanças para consistência ([[Journaling e Copy-on-Write]]) |
| **VFS** | Camada virtual de sistemas de arquivos ([[VFS - Virtual File System]]) |

### Núcleo e arquitetura

| Termo | Definição |
|---|---|
| **Bootloader** | Programa que carrega o kernel ([[Bootloader]]) |
| **Exokernel** | Kernel mínimo que expõe hardware às aplicações ([[Exokernel]]) |
| **Hypervisor** | Software que cria máquinas virtuais ([[Hypervisors]]) |
| **Kernel** | Núcleo privilegiado do SO ([[Kernel vs User Space]]) |
| **System call** | Interface de serviços do kernel ([[System Calls]]) |
| **Trap** | Exceção síncrona ([[Traps e Exceções]]) |

### Segurança e isolamento

| Termo | Definição |
|---|---|
| **ASLR** | Aleatorização do layout de endereços para dificultar exploração ([[ASLR - Address Space Layout Randomization]]) |
| **cgroups** | Limitação e contabilização de recursos ([[cgroups - SO]]) |
| **DEP/NX** | Impede execução em páginas de dados ([[DEP, NX e Mitigações de Exploração]]) |
| **Namespace** | Isolamento de visão de recursos ([[Namespaces do Linux - SO]]) |
| **Sandbox** | Ambiente restrito de execução ([[Sandboxing]]) |

**Veja também:** [[Mapa de Estudos]] · [[Cheat Sheet - Conceitos]] · [[Cheat Sheet - Comandos]]

## Obsidian

Voltar ao índice: [[Índice geral - Obsidian]].

### Vault, plugins e configuração

| Termo | Definição |
|---|---|
| **Community plugin** | plugin de terceiros ([[MOC - Plugins da Comunidade]]) |
| **Core plugin** | plugin nativo ([[MOC - Plugins Core]]) |
| **Live Preview** | modo de edição renderizado ([[Modos de edição e leitura]]) |
| **Local-first** | dados locais primeiro ([[Local-first e propriedade dos dados]]) |
| **Restricted Mode** | modo sem plugins da comunidade ([[Plugins da comunidade e Restricted Mode]]) |
| **Snippet CSS** | arquivo CSS personalizado ([[Snippets CSS]]) |
| **Vault** | pasta do Obsidian ([[Vault]]) |

### Notas, links e metadados

| Termo | Definição |
|---|---|
| **Alias** | nome alternativo de uma nota ([[Aliases]]) |
| **Backlink** | link recebido de outra nota ([[Backlinks e links de saída]]) |
| **Block ID** | identificador `^id` de um bloco ([[Links para títulos e blocos]]) |
| **Embed** | conteúdo incorporado `![[ ]]` ([[Embeds]]) |
| **Frontmatter** | bloco YAML inicial ([[Sintaxe YAML do frontmatter]]) |
| **Orphan** | nota sem links |
| **Properties** | metadados da nota ([[Properties]]) |
| **Tag** | etiqueta `#tag` ([[Tags]]) |
| **Wikilink** | link `[[ ]]` ([[Wikilinks e links Markdown]]) |

### Recursos de visualização e bases

| Termo | Definição |
|---|---|
| **Base** | visão de banco de dados `.base` ([[Bases]]) |
| **Callout** | bloco de destaque com tipo ([[Callouts]]) |
| **Canvas** | quadro infinito `.canvas` ([[Canvas]]) |
| **Graph view** | visão em grafo ([[Graph view]]) |

### Organização do conhecimento

| Termo | Definição |
|---|---|
| **MOC** | Map of Content ([[MOCs]]) |
| **Nota atômica** | uma ideia por nota ([[Notas atômicas]]) |
| **PKM** | gestão de conhecimento pessoal |
| **Zettelkasten** | método de fichas conectadas ([[Zettelkasten]]) |

**Veja também:** [[FAQ]] · [[Cheat sheet Markdown]]


## Docker

Voltar ao índice: [[Índice geral - Docker]].

### Arquitetura e runtime

| Termo | Definição |
|---|---|
| **cgroups** | Recurso do kernel que limita e contabiliza recursos. Veja [[Cgroups - Docker]] |
| **Container** | Processo isolado (namespaces + cgroups) executado a partir de uma imagem |
| **containerd** | Runtime de alto nível do ciclo de vida de containers. Veja [[containerd e runc]] |
| **Contexto (docker context)** | Endereço/credenciais de um daemon. Veja [[Contextos do Docker]] |
| **Daemon (dockerd)** | Processo que implementa a API e gerencia objetos. Veja [[Docker Daemon dockerd]] |
| **Docker Desktop** | Aplicativo (Win/Mac/Linux) com VM, GUI e extras. Veja [[Docker Desktop vs Docker Engine]] |
| **Docker Engine** | Daemon + API + CLI para Linux |
| **Healthcheck** | Teste periódico de saúde. Veja [[Healthchecks em containers]] |
| **Moby** | Projeto open source base do Docker Engine |
| **Namespace** | Visão isolada de um recurso do kernel. Veja [[Namespaces]] |
| **OCI** | Open Container Initiative: especificações de runtime, imagem e distribuição. Veja [[Padrão OCI]] |
| **PID 1** | Processo principal do container. Veja [[Init, PID 1 e sinais]] |
| **runc** | Runtime de baixo nível (OCI) |
| **Wasm** | WebAssembly. Veja [[WebAssembly e containers]] |

### Imagens e Dockerfile

| Termo | Definição |
|---|---|
| **ARG** | Variável disponível **só durante o build**. Veja [[Instruções ENV e ARG]] |
| **BuildKit** | Motor de build moderno do Docker. Veja [[Buildx e BuildKit]] |
| **Buildx** | Plugin da CLI que expõe o BuildKit (multiplataforma, cache, bake) |
| **Camada (layer)** | Conjunto de mudanças no sistema de arquivos; imagens são pilhas de camadas. Veja [[Camadas de uma imagem]] |
| **CMD** | Comando/argumentos padrão do container. Veja [[Instruções CMD e ENTRYPOINT]] |
| **Contexto de build** | Conjunto de arquivos enviado ao builder. Veja [[Arquivo .dockerignore]] |
| **Dangling** | Imagem sem tag (`<none>`). Veja [[Limpeza com prune]] |
| **Distroless** | Imagens sem shell nem gerenciador de pacotes. Veja [[Superfície de ataque e imagens mínimas]] |
| **Dockerfile** | Receita para construir uma imagem. Veja [[Introdução ao Dockerfile]] |
| **ENTRYPOINT** | Executável fixo do container |
| **ENV** | Variável de ambiente persistida na imagem. Veja [[Instruções ENV e ARG]] |
| **EXPOSE** | Documenta a porta; não publica. Veja [[Instruções EXPOSE e VOLUME]] |
| **Imagem** | Modelo imutável (camadas + metadados). Veja [[Imagens vs Containers]] |
| **Imagem base** | Imagem do `FROM`. Veja [[Escolha da imagem base]] |
| **Label** | Metadado chave=valor. Veja [[Nomes e labels]] |
| **Multi-stage** | Vários `FROM` em um Dockerfile. Veja [[Multi-stage builds]] |
| **Prune** | Remoção de objetos não usados |

### Registries e distribuição

| Termo | Definição |
|---|---|
| **Digest** | Hash SHA-256 imutável de uma imagem. Veja [[Tags e digests de imagens]] |
| **Index (manifest list)** | Manifest que aponta para imagens por plataforma. Veja [[Padrão OCI]] |
| **Manifest** | Documento que descreve uma imagem (config + camadas) |
| **Registry** | Serviço que armazena imagens. Veja [[Registries]] |
| **Repositório** | Conjunto de tags de uma imagem em um registry |
| **Tag** | Rótulo mutável de uma versão de imagem |

### Redes e armazenamento

| Termo | Definição |
|---|---|
| **Bind mount** | Montagem de um diretório/arquivo do host no container. Veja [[Bind mounts]] |
| **Bridge** | Driver de rede padrão (switch virtual no host). Veja [[Redes bridge]] |
| **Overlay** | Rede multi-host. Veja [[Rede overlay]] |
| **OverlayFS / overlay2** | Union filesystem/driver padrão. Veja [[Union filesystems e OverlayFS]] |
| **Publicação de portas** | Mapeia porta do host para o container. Veja [[Publicação de portas]] |
| **tmpfs** | Armazenamento em memória. Veja [[tmpfs mounts]] |
| **Volume** | Armazenamento persistente gerenciado pelo Docker. Veja [[Volumes nomeados]] |

### Compose e orquestração

| Termo | Definição |
|---|---|
| **Compose** | Ferramenta para definir aplicações multi-container. Veja [[Visão geral do Docker Compose]] |
| **Orquestrador** | Gerencia containers em cluster (Swarm, Kubernetes). Veja [[Visão geral do Swarm]] |
| **Service (Swarm)** | Estado desejado de um conjunto de tasks. Veja [[Nodes, services, tasks e stacks]] |
| **Stack** | Conjunto de serviços implantado no Swarm. Veja [[Stacks com docker stack deploy]] |
| **Swarm** | Orquestrador nativo do Docker |
| **Task** | Um container agendado por um serviço do Swarm |

### Segurança em containers

| Termo | Definição |
|---|---|
| **AppArmor** | Módulo de segurança (MAC) do Linux com perfis por caminho. Veja [[AppArmor e SELinux]] |
| **Capabilities** | Fatias do poder do root no Linux. Veja [[Capabilities Linux]] |
| **Provenance** | Atestado de como a imagem foi construída. Veja [[SBOM e provenance]] |
| **Rootless** | Daemon e containers sem root. Veja [[Modo rootless]] |
| **SBOM** | Lista de componentes de uma imagem. Veja [[SBOM e provenance]] |
| **Seccomp** | Filtro de syscalls. Veja [[Seccomp - Docker]] |
| **Secret** | Dado sensível entregue de forma controlada. Veja [[Gerenciamento de segredos]] |

**Veja também:** [[Cheat sheet de comandos Docker]] · [[Erros comuns e soluções]] · [[FAQ Docker]]

## Sandboxes e isolamento

Voltar ao índice: [[Índice Geral - Sandbox]].

### Conceitos de isolamento e segurança

| Termo | Definição |
|---|---|
| Contenção | Limitar o alcance de um dano → [[Isolamento e Contenção]] |
| Defesa em profundidade | Camadas independentes de proteção → [[Defesa em Profundidade]] |
| Efêmero | Criado e destruído sob demanda → [[Ambientes Efêmeros]] |
| Egress | Tráfego de saída → [[Limites de Rede e Sistema de Arquivos para Agentes]] |
| Fuga de sandbox | Escape da fronteira de isolamento → [[Fuga de Sandbox]] |
| Hardening | Endurecimento da configuração → [[Endurecimento (Hardening)]] |
| Isolamento | Separação de recursos → [[Isolamento e Contenção]] |
| Menor privilégio | Só as permissões necessárias → [[Princípio do Menor Privilégio]] |
| Prompt injection | Instruções maliciosas em conteúdo lido por um LLM → [[Prompt Injection e seus Riscos]] |
| Sandbox | Ambiente isolado com acesso restrito → [[O que é um Ambiente Sandbox]] |
| STRIDE | Taxonomia de ameaças → [[Modelo de Ameaças]] |
| Superfície de ataque | Pontos de interação com algo não confiável → [[Superfície de Ataque]] |

### Mecanismos do kernel Linux

| Termo | Definição |
|---|---|
| Capability | Fração dos poderes do root → [[Capabilities do Linux]] |
| Cgroup | Limite e contabilização de recursos → [[Cgroups]] |
| Container | Processo isolado por namespaces/cgroups → [[Sandbox por Containers]] |
| LSM | Módulo de segurança do Linux (AppArmor/SELinux) → [[Ferramenta - AppArmor e SELinux]] |
| Namespace | Visão particionada de recursos do kernel → [[Namespaces do Linux]] |
| Rootless | Container executado sem root no host → [[Criar Sandbox com Podman Rootless]] |
| Seccomp | Filtro de chamadas de sistema → [[Seccomp]] |
| Syscall | Chamada de sistema ao kernel → [[Seccomp]] |

### Virtualização e runtimes isolados

| Termo | Definição |
|---|---|
| gVisor | Kernel em espaço de usuário → [[Sandbox por Kernel em Espaço de Usuário]] |
| Hipervisor | Software que cria e gerencia VMs → [[Hipervisores Tipo 1 e Tipo 2]] |
| MicroVM | VM minimalista de boot rápido → [[Sandbox por MicroVMs]] |
| Snapshot | Captura do estado de uma VM → [[Snapshots e Reversão]] |
| VM | Máquina virtual com kernel próprio → [[Sandbox por Virtualização Completa]] |
| WASI | Interface de sistema por capacidades para Wasm → [[Sandbox por WebAssembly]] |
| WebAssembly (Wasm) | Formato binário executado em VM isolada → [[Sandbox por WebAssembly]] |

### Análise de malware e detecção

| Termo | Definição |
|---|---|
| Análise dinâmica | Observar durante a execução → [[Análise Estática e Dinâmica]] |
| Análise estática | Examinar sem executar → [[Análise Estática e Dinâmica]] |
| Cyber range | Ambiente de treino de segurança → [[Honeypots e Cyber Ranges]] |
| Evasão de sandbox | Tentativa de detectar a análise → [[Evasão de Sandbox por Malware]] |
| Honeypot | Sistema isca → [[Honeypots e Cyber Ranges]] |
| IOC | Indicador de comprometimento → [[Indicadores de Comprometimento]] |
| YARA | Linguagem de regras de detecção → [[YARA e Regras de Detecção]] |

### Desenvolvimento, DevOps e conformidade

| Termo | Definição |
|---|---|
| IaC | Infraestrutura como código → [[Infraestrutura como Código]] |
| LGPD | Lei Geral de Proteção de Dados → [[Conformidade e LGPD]] |
| Mock | Simulação de componente/serviço → [[Dados de Teste e Mocks]] |
| Pseudonimização | Troca de identificadores reversível → [[Sandbox de Dados]] |
| SBOM | Lista de componentes de software → [[Cadeia de Suprimentos de Software]] |

**Veja também:** [[MOC - Referência - Sandbox]] · [[Cheat Sheet - Isolamento no Linux]] · [[FAQ de Sandboxes]]


## Segurança de IA (jailbreaking e prompt injection)

Voltar ao índice: [[00 - Índice Jailbreaking]].

### Fundamentos de LLMs

| Termo | Definição |
|---|---|
| **Alinhamento** | Treinamento que orienta o modelo a seguir preferências e políticas ([[Alinhamento e Guardrails]]). |
| **Generalização descasada** | Capacidade do modelo maior que a cobertura do treino de segurança (Wei et al., 2023). |
| **Hierarquia de instruções** | Prioridade entre system prompt, usuário e conteúdo de ferramentas ([[System Prompt e Hierarquia de Instruções]]). |
| **Janela de contexto** | Limite de tokens que o modelo processa de uma vez ([[Tokens e Contexto]]). |
| **RAG** | Geração com recuperação de documentos inseridos no contexto. |
| **System prompt** | Instruções do desenvolvedor, em geral invisíveis ao usuário. |
| **Token** | Unidade de texto processada pelo modelo. |

### Ataques

| Termo | Definição |
|---|---|
| **Ataque adaptativo** | Ataque que se ajusta à defesa específica do alvo ([[Ataques Adaptativos e Transferência]]). |
| **Injeção direta** | Instrução maliciosa dada pelo próprio usuário à aplicação ([[Injeção Direta]]). |
| **Injeção indireta** | Instrução plantada em conteúdo que a aplicação lê ([[Injeção Indireta]]). |
| **Jailbreak** | Contornar a política de comportamento do modelo ([[Jailbreak vs Prompt Injection]]). |
| **Multiturno** | Ataque distribuído em várias mensagens ([[Jailbreak Multiturno]]). |
| **Prompt injection** | Instrução não confiável tratada como legítima pela aplicação ([[Conceitos Fundamentais]]). |
| **Triângulo de risco** | Conteúdo não confiável + dados privados + ação externa no mesmo fluxo. |
| **Vazamento de system prompt** | Revelação indevida do prompt de sistema (OWASP LLM07). |

### Defesas

| Termo | Definição |
|---|---|
| **Contrato de saída** | Formato obrigatório da resposta, validado por código ([[Validação de Entradas e Saídas]]). |
| **Defesa em camadas** | Vários controles independentes, de modo que a falha de um não basta ([[Defesa em Camadas]]). |
| **Guardrail** | Controle que limita entradas, saídas ou ações, dentro ou fora do modelo. |
| **Menor privilégio** | Conceder só as permissões mínimas necessárias à tarefa. |
| **Spotlighting** | Transformar dados não confiáveis para sinalizar origem (Hines et al., 2024). |

### Avaliação e laboratórios

| Termo | Definição |
|---|---|
| **Alvo de brinquedo** | Aplicação local, fictícia, com segredo-canário e ferramentas simuladas, criada para os laboratórios. |
| **Canário** | String inofensiva (ex.: `ABACAXI-42`) cujo aparecimento na saída prova o efeito, sem opinião. |
| **Intervalo de Wilson** | Intervalo de confiança para proporções, adequado a poucos casos ([[Métricas e Critérios de Sucesso]]). |
| **Recusa indevida** | Recusar um pedido legítimo; mede custo de uma defesa. |
| **Red teaming** | Teste adversarial **autorizado** para achar falhas ([[Metodologia de Testes]]). |
| **Regra dos três** | Com 0 falhas em *n* testes, limite superior aproximado de 3/*n* (95%). |
| **Taxa de sucesso de ataque (ASR)** | Fração de tentativas que atingem o critério de sucesso. |

### Siglas

OWASP ([[OWASP para Aplicações de LLM]]) · ATLAS ([[MITRE ATLAS]]) · LLM · RAG · ASR · IC (intervalo de confiança) · MCP (protocolo de ferramentas para agentes).

**Veja também:** [[Questionário de Fundamentos]] (módulo 9)

## Integração de Segurança

Voltar ao índice: [[Home - Integração]].

### Arquitetura e integração

| Termo | Definição |
|---|---|
| **Adapter** | Padrão que traduz a interface de um sistema para a esperada pela aplicação, isolando fornecedores. → [[Padrão Adapter e Connector]] · [[Padrões de Integração - Point-to-Point Hub-and-Spoke e Event-Driven]] |
| **Backoff exponencial** | Aumento progressivo do intervalo entre tentativas de uma operação que falhou. → [[Retries com Backoff e Tratamento de Falhas]] · [[Rate Limiting]] |
| **Backpressure** | Mecanismo pelo qual o consumidor controla o ritmo de entrega para não ser sobrecarregado. → [[Filas e Streaming - Kafka e RabbitMQ]] · [[Retries com Backoff e Tratamento de Falhas]] |
| **Circuit breaker** | Padrão que interrompe chamadas a uma dependência degradada para evitar falhas em cascata. → [[Retries com Backoff e Tratamento de Falhas]] · [[Padrões de Integração - Point-to-Point Hub-and-Spoke e Event-Driven]] |
| **Connector** | Implementação concreta que integra a aplicação a uma ferramenta específica. → [[Padrão Adapter e Connector]] · [[Plugins e Extensões]] |
| **Dead-letter queue** | Fila de mensagens que falharam repetidamente, para análise. → [[Filas e Streaming - Kafka e RabbitMQ]] · [[Retries com Backoff e Tratamento de Falhas]] |
| **Deduplicação** | Descarte ou agrupamento de eventos ou achados repetidos. → [[Idempotência]] · [[Integração com Ticketing - Jira e GitHub Issues]] · [[Enriquecimento de Alertas e Escalonamento]] |
| **HEC** | HTTP Event Collector do Splunk, para ingestão de eventos via HTTP. → [[Integração com SIEM - Splunk Elastic e Wazuh]] · [[Webhooks e Polling]] |
| **Idempotência** | Propriedade de uma operação repetida produzir o mesmo efeito de uma execução. → [[Idempotência]] · [[Retries com Backoff e Tratamento de Falhas]] · [[Webhooks e Polling]] |
| **Jitter** | Aleatoriedade adicionada ao backoff para evitar picos sincronizados. → [[Retries com Backoff e Tratamento de Falhas]] · [[Rate Limiting]] |
| **Kafka** | Plataforma de log distribuído para streaming de eventos. → [[Filas e Streaming - Kafka e RabbitMQ]] · [[Padrões de Integração - Point-to-Point Hub-and-Spoke e Event-Driven]] |
| **Polling** | Consulta periódica do consumidor à origem para buscar novidades. → [[Webhooks e Polling]] · [[Paginação e Versionamento]] |
| **RabbitMQ** | Message broker AMQP com roteamento flexível e confirmação por mensagem. → [[Filas e Streaming - Kafka e RabbitMQ]] · [[Padrões de Integração - Point-to-Point Hub-and-Spoke e Event-Driven]] |
| **Rate limiting** | Controle do número de requisições por intervalo de tempo. → [[Rate Limiting]] · [[Retries com Backoff e Tratamento de Falhas]] |
| **Replay** | Reenvio de uma mensagem legítima capturada; mitigado com timestamp e id únicos. → [[Webhooks e Polling]] · [[Idempotência]] |
| **Retry** | Nova tentativa de uma operação que falhou, com limites. → [[Retries com Backoff e Tratamento de Falhas]] · [[Idempotência]] |
| **Token bucket** | Algoritmo de limitação de taxa com tokens repostos em ritmo constante. → [[Rate Limiting]] · [[Retries com Backoff e Tratamento de Falhas]] |
| **Webhook** | Callback HTTP enviado por uma origem quando um evento ocorre. → [[Webhooks e Polling]] · [[Padrões de Integração - Point-to-Point Hub-and-Spoke e Event-Driven]] |

### Formatos e padrões de dados

| Termo | Definição |
|---|---|
| **CEF** | Common Event Format: formato textual de eventos, comum em syslog. → [[Normalização de Dados - OCSF ECS CEF STIX e TAXII]] · [[Integração com SIEM - Splunk Elastic e Wazuh]] |
| **ECS** | Elastic Common Schema: nomes de campos padronizados para eventos. → [[Normalização de Dados - OCSF ECS CEF STIX e TAXII]] · [[Integração com SIEM - Splunk Elastic e Wazuh]] |
| **eve.json** | Saída JSON do Suricata com alertas e metadados de protocolo. → [[Suricata - Integração]] · [[Integração com SIEM - Splunk Elastic e Wazuh]] |
| **OCSF** | Open Cybersecurity Schema Framework: esquema aberto de eventos de segurança. → [[Normalização de Dados - OCSF ECS CEF STIX e TAXII]] · [[Integração com SIEM - Splunk Elastic e Wazuh]] |
| **OpenAPI** | Especificação para descrever APIs REST como contrato. → [[OpenAPI]] · [[REST e Design de APIs de Segurança]] · [[Paginação e Versionamento]] |
| **purl** | Package URL: identificador padronizado de componentes de software. → [[SBOM - CycloneDX e SPDX]] · [[Supply Chain da Ferramenta]] |
| **SARIF** | Formato padrão de resultados de análise estática. → [[Parsing de Formatos - SARIF JSON e XML]] · [[Ferramentas de Teste de Aplicação - SAST DAST IAST SCA]] |
| **SPDX** | Padrão de SBOM, forte em licenciamento. → [[SBOM - CycloneDX e SPDX]] · [[Supply Chain da Ferramenta]] |
| **STIX** | Linguagem JSON para descrever inteligência de ameaças. → [[Normalização de Dados - OCSF ECS CEF STIX e TAXII]] · [[Integração com Threat Intelligence - MISP OpenCTI e VirusTotal]] |
| **TAXII** | Protocolo para compartilhar inteligência em STIX. → [[Normalização de Dados - OCSF ECS CEF STIX e TAXII]] · [[Integração com Threat Intelligence - MISP OpenCTI e VirusTotal]] |
| **VEX** | Declaração de explorabilidade de vulnerabilidades em um produto. → [[SBOM - CycloneDX e SPDX]] · [[Integração com Scanners - Nessus OpenVAS Trivy e Nuclei]] |

### APIs e autenticação

| Termo | Definição |
|---|---|
| **ABAC** | Controle de acesso baseado em atributos (usuário, recurso, ambiente), em vez de apenas papéis. → [[Escopos e Menor Privilégio]] · [[API Keys e Gestão de Credenciais]] |
| **Access token** | Token de curta duração que autoriza o acesso a uma API em OAuth 2.0. → [[OAuth 2.0 e OIDC]] · [[JWT]] |
| **API key** | Segredo estático que identifica e autoriza um cliente de API. → [[API Keys e Gestão de Credenciais]] · [[REST e Design de APIs de Segurança]] |
| **BOLA** | Broken Object Level Authorization: falha de autorização por objeto em APIs. → [[REST e Design de APIs de Segurança]] · [[OWASP Top 10 - Integração]] · [[Escopos e Menor Privilégio]] |
| **Client credentials** | Fluxo OAuth 2.0 para autenticação máquina a máquina. → [[OAuth 2.0 e OIDC]] · [[API Keys e Gestão de Credenciais]] |
| **GraphQL** | Linguagem de consulta de APIs sobre esquema tipado, com endpoint único. → [[GraphQL e gRPC]] · [[REST e Design de APIs de Segurança]] |
| **gRPC** | Framework de chamadas remotas sobre HTTP/2 com contratos protobuf. → [[GraphQL e gRPC]] · [[mTLS]] |
| **HMAC** | Código de autenticação de mensagem com chave, usado para assinar webhooks. → [[Webhooks e Polling]] · [[Modelo CIA e Princípios de Segurança]] |
| **JWKS** | Conjunto de chaves públicas publicado por um emissor para validar tokens. → [[JWT]] · [[OAuth 2.0 e OIDC]] |
| **JWT** | JSON Web Token: formato compacto de claims, geralmente assinado. → [[JWT]] · [[OAuth 2.0 e OIDC]] · [[Escopos e Menor Privilégio]] |
| **Mass assignment** | Aceitar campos não previstos que alteram propriedades internas de um objeto. → [[REST e Design de APIs de Segurança]] · [[OpenAPI]] · [[Validacao de Entrada]] |
| **Menor privilégio** | Conceder apenas as permissões necessárias, pelo tempo necessário. → [[Escopos e Menor Privilégio]] · [[Privilégio Mínimo e Hardening de Containers]] · [[Modelo CIA e Princípios de Segurança]] |
| **mTLS** | TLS mútuo: cliente e servidor se autenticam com certificados. → [[mTLS]] · [[OAuth 2.0 e OIDC]] |
| **OAuth 2.0** | Framework de autorização delegada baseado em tokens. → [[OAuth 2.0 e OIDC]] · [[JWT]] · [[Escopos e Menor Privilégio]] |
| **OIDC** | OpenID Connect: camada de autenticação sobre OAuth 2.0. → [[OAuth 2.0 e OIDC]] · [[JWT]] |
| **PKCE** | Extensão que protege o fluxo authorization code contra interceptação. → [[OAuth 2.0 e OIDC]] · [[JWT]] |
| **RBAC** | Controle de acesso baseado em papéis. → [[Escopos e Menor Privilégio]] · [[API Keys e Gestão de Credenciais]] |
| **REST** | Estilo arquitetural de APIs baseado em recursos e métodos HTTP. → [[REST e Design de APIs de Segurança]] · [[OpenAPI]] |
| **Secret zero** | Problema de obter a primeira credencial sem embuti-la. → [[Gestão de Segredos na Ferramenta]] · [[Integração com Gestão de Segredos - Vault e gitleaks]] |

### Fundamentos e frameworks de segurança

| Termo | Definição |
|---|---|
| **ASVS** | Application Security Verification Standard da OWASP: requisitos verificáveis em três níveis. → [[OWASP ASVS]] · [[OWASP Top 10 - Integração]] |
| **ATT&CK** | Base de conhecimento MITRE de táticas e técnicas de adversários. → [[MITRE ATT&CK - Integração]] · [[Modelagem de Ameaças - STRIDE e PASTA]] |
| **Blast radius** | Alcance do impacto de uma ação ou falha; deve ser limitado por desenho. → [[Automação de Resposta a Incidentes]] · [[Privilégio Mínimo e Hardening de Containers]] |
| **CIA** | Tríade Confidencialidade, Integridade e Disponibilidade. → [[Modelo CIA e Princípios de Segurança]] · [[SDLC e SSDLC]] |
| **CIS Controls** | Conjunto priorizado de salvaguardas defensivas do Center for Internet Security. → [[CIS Controls]] · [[NIST CSF]] |
| **CVE** | Identificador público de uma vulnerabilidade conhecida. → [[Integração com Scanners - Nessus OpenVAS Trivy e Nuclei]] · [[Integração com SAST e SCA - Semgrep SonarQube Dependabot e Snyk]] |
| **CVSS** | Sistema de pontuação de severidade de vulnerabilidades. → [[Integração com Scanners - Nessus OpenVAS Trivy e Nuclei]] · [[Enriquecimento de Alertas e Escalonamento]] |
| **CWE** | Catálogo de tipos de fraquezas de software. → [[OWASP Top 10 - Integração]] · [[Ferramentas de Teste de Aplicação - SAST DAST IAST SCA]] |
| **Defesa em profundidade** | Camadas independentes de controles, de modo que a falha de uma não compromete tudo. → [[Modelo CIA e Princípios de Segurança]] · [[Privilégio Mínimo e Hardening de Containers]] |
| **DFD** | Diagrama de fluxo de dados usado na modelagem de ameaças. → [[Modelagem de Ameaças - STRIDE e PASTA]] · [[SDLC e SSDLC]] |
| **EPSS** | Modelo que estima a probabilidade de exploração de uma vulnerabilidade. → [[Integração com Scanners - Nessus OpenVAS Trivy e Nuclei]] · [[Enriquecimento de Alertas e Escalonamento]] |
| **Fail secure** | Falhar em estado seguro: na dúvida, negar ou enfileirar. → [[Modelo CIA e Princípios de Segurança]] · [[Automação de Resposta a Incidentes]] |
| **KEV** | Catálogo da CISA de vulnerabilidades sabidamente exploradas. → [[Integração com Scanners - Nessus OpenVAS Trivy e Nuclei]] · [[Enriquecimento de Alertas e Escalonamento]] |
| **LGPD** | Lei Geral de Proteção de Dados Pessoais (Lei 13.709/2018). → [[LGPD e Privacidade]] · [[Auditoria e Logs de Ações]] |
| **NIST CSF** | Framework de cibersegurança do NIST com as funções Govern, Identify, Protect, Detect, Respond e Recover. → [[NIST CSF]] · [[CIS Controls]] |
| **OWASP Top 10** | Lista de riscos críticos de aplicações web. → [[OWASP Top 10 - Integração]] · [[OWASP ASVS]] |
| **PASTA** | Metodologia de modelagem de ameaças em sete etapas, orientada a risco. → [[Modelagem de Ameaças - STRIDE e PASTA]] · [[SDLC e SSDLC]] |
| **Pseudonimização** | Substituição de identificadores por tokens, mantendo o dado como pessoal. → [[LGPD e Privacidade]] · [[Auditoria e Logs de Ações]] |
| **SSDLC** | Ciclo de vida de desenvolvimento seguro. → [[SDLC e SSDLC]] · [[Security Gates e Shift-Left]] |
| **STRIDE** | Seis categorias de ameaça: spoofing, tampering, repudiation, information disclosure, DoS e elevation of privilege. → [[Modelagem de Ameaças - STRIDE e PASTA]] · [[SDLC e SSDLC]] |
| **Threat modeling** | Identificação estruturada de ameaças e mitigações no design. → [[Modelagem de Ameaças - STRIDE e PASTA]] · [[SDLC e SSDLC]] |
| **TLP** | Traffic Light Protocol: define como a informação pode ser compartilhada. → [[Integração com Threat Intelligence - MISP OpenCTI e VirusTotal]] · [[Enriquecimento de Alertas e Escalonamento]] |

### DevSecOps e cadeia de suprimentos

| Termo | Definição |
|---|---|
| **Attestation** | Declaração assinada sobre um artefato, como proveniência de build ou SBOM. → [[Assinatura de Artefatos - Sigstore e cosign]] · [[SLSA]] |
| **Checkov** | Scanner de infraestrutura como código multi-framework. → [[IaC Scanning - Checkov e tfsec]] · [[Políticas como Código - OPA e Rego]] |
| **Conftest** | Ferramenta que aplica políticas Rego a arquivos de configuração. → [[Políticas como Código - OPA e Rego]] · [[IaC Scanning - Checkov e tfsec]] |
| **Cosign** | Ferramenta do Sigstore para assinar e verificar artefatos e attestations. → [[Assinatura de Artefatos - Sigstore e cosign]] · [[SBOM - CycloneDX e SPDX]] |
| **CSPM** | Cloud Security Posture Management: avaliação contínua de configurações de nuvem. → [[Ferramentas de Postura e Proteção - CSPM WAF Scanners e Segredos]] · [[IaC Scanning - Checkov e tfsec]] |
| **DAST** | Teste dinâmico de segurança de aplicações em execução. → [[Ferramentas de Teste de Aplicação - SAST DAST IAST SCA]] · [[Panorama de Ferramentas de Segurança]] |
| **Dependency confusion** | Resolução indevida de um nome interno para um pacote público homônimo. → [[Supply Chain da Ferramenta]] · [[SBOM - CycloneDX e SPDX]] |
| **Drift** | Divergência entre a configuração desejada (código) e a real. → [[IaC Scanning - Checkov e tfsec]] · [[Ferramentas de Postura e Proteção - CSPM WAF Scanners e Segredos]] |
| **Fulcio** | Autoridade do Sigstore que emite certificados efêmeros ligados a identidades OIDC. → [[Assinatura de Artefatos - Sigstore e cosign]] · [[SLSA]] |
| **Gate** | Ponto de decisão automatizado que bloqueia o fluxo se um critério for violado. → [[Security Gates e Shift-Left]] · [[GitHub Actions]] |
| **Hardening** | Endurecimento da configuração para reduzir a superfície de ataque. → [[Privilégio Mínimo e Hardening de Containers]] · [[Empacotamento e Containers]] |
| **IaC** | Infraestrutura como código. → [[IaC Scanning - Checkov e tfsec]] · [[Políticas como Código - OPA e Rego]] |
| **IAST** | Teste interativo que instrumenta a aplicação durante a execução. → [[Ferramentas de Teste de Aplicação - SAST DAST IAST SCA]] · [[Panorama de Ferramentas de Segurança]] |
| **OPA** | Open Policy Agent: motor de políticas como código. → [[Políticas como Código - OPA e Rego]] · [[IaC Scanning - Checkov e tfsec]] |
| **pre-commit** | Framework para executar verificações em hooks do git. → [[Pré-commit Hooks]] · [[Security Gates e Shift-Left]] |
| **Proveniência** | Registro verificável de como, onde e a partir de quê um artefato foi construído. → [[SLSA]] · [[Assinatura de Artefatos - Sigstore e cosign]] |
| **Rego** | Linguagem declarativa de políticas do OPA. → [[Políticas como Código - OPA e Rego]] · [[IaC Scanning - Checkov e tfsec]] |
| **Rekor** | Log de transparência do Sigstore. → [[Assinatura de Artefatos - Sigstore e cosign]] · [[SLSA]] |
| **SAST** | Análise estática de segurança do código-fonte. → [[Ferramentas de Teste de Aplicação - SAST DAST IAST SCA]] · [[Integração com SAST e SCA - Semgrep SonarQube Dependabot e Snyk]] |
| **SBOM** | Inventário formal de componentes de um software. → [[SBOM - CycloneDX e SPDX]] · [[Supply Chain da Ferramenta]] |
| **SCA** | Análise de composição de software: dependências e vulnerabilidades. → [[Ferramentas de Teste de Aplicação - SAST DAST IAST SCA]] · [[Integração com SAST e SCA - Semgrep SonarQube Dependabot e Snyk]] |
| **Shift-left** | Antecipar atividades de segurança no ciclo de desenvolvimento. → [[Security Gates e Shift-Left]] · [[SDLC e SSDLC]] |
| **Sigstore** | Conjunto de projetos para assinatura e verificação de artefatos. → [[Assinatura de Artefatos - Sigstore e cosign]] · [[SLSA]] |
| **SLSA** | Níveis de garantia da cadeia de construção de software. → [[SLSA]] · [[Assinatura de Artefatos - Sigstore e cosign]] · [[SBOM - CycloneDX e SPDX]] |
| **Supply chain** | Cadeia de suprimentos de software: dependências, builds e distribuição. → [[Supply Chain da Ferramenta]] · [[SLSA]] |
| **Typosquatting** | Pacote com nome parecido com um popular para enganar instalações. → [[Supply Chain da Ferramenta]] · [[SBOM - CycloneDX e SPDX]] |
| **WAF** | Web Application Firewall: filtra tráfego HTTP. → [[Ferramentas de Postura e Proteção - CSPM WAF Scanners e Segredos]] · [[OWASP Top 10 - Integração]] |

### Detecção, observabilidade e resposta

| Termo | Definição |
|---|---|
| **Alert fatigue** | Desgaste causado por excesso de alertas, que leva a ignorá-los, inclusive os verdadeiros. → [[Redução de Falsos Positivos]] · [[Enriquecimento de Alertas e Escalonamento]] |
| **Auditoria** | Registro íntegro de quem fez o quê, quando e com qual resultado. → [[Auditoria e Logs de Ações]] · [[Logging Estruturado]] |
| **Backtesting** | Execução de uma regra de detecção sobre logs históricos para estimar disparos e falsos positivos. → [[Testes de Regras de Detecção]] · [[Redução de Falsos Positivos]] |
| **Baseline** | Referência de comportamento normal ou de estado aceito, usada para comparar mudanças. → [[Redução de Falsos Positivos]] · [[Security Gates e Shift-Left]] |
| **Correlation ID** | Identificador que liga os registros de uma mesma operação entre serviços. → [[Logging Estruturado]] · [[Métricas e Tracing - Prometheus e OpenTelemetry]] |
| **EDR** | Endpoint Detection and Response: telemetria e resposta em endpoints. → [[Ferramentas de Detecção e Resposta - EDR SIEM SOAR]] · [[Automação de Resposta a Incidentes]] |
| **Enriquecimento** | Anexar contexto a alertas, como reputação, dono e criticidade. → [[Enriquecimento de Alertas e Escalonamento]] · [[Integração com Threat Intelligence - MISP OpenCTI e VirusTotal]] |
| **Falso positivo** | Alerta disparado por atividade legítima. → [[Redução de Falsos Positivos]] · [[Regras Sigma]] |
| **Hash chain** | Encadeamento de registros por hash para evidenciar adulteração. → [[Auditoria e Logs de Ações]] · [[Logging Estruturado]] |
| **HITL** | Human-in-the-loop: pessoa na decisão de ações automatizadas relevantes. → [[Human-in-the-Loop]] · [[Automação de Resposta a Incidentes]] |
| **IDS/IPS** | Sistemas de detecção e de prevenção de intrusão. → [[Suricata - Integração]] · [[Ferramentas de Detecção e Resposta - EDR SIEM SOAR]] |
| **IoC** | Indicador de comprometimento, como IP, domínio ou hash associado a atividade maliciosa. → [[Integração com Threat Intelligence - MISP OpenCTI e VirusTotal]] · [[YARA - Integração]] |
| **MISP** | Plataforma open source de compartilhamento de IoCs e eventos. → [[Integração com Threat Intelligence - MISP OpenCTI e VirusTotal]] · [[Normalização de Dados - OCSF ECS CEF STIX e TAXII]] |
| **MTTA** | Tempo médio até o reconhecimento de um alerta. → [[Métricas - MTTD e MTTR]] · [[SOAR - Shuffle TheHive Cortex e n8n]] |
| **MTTD** | Tempo médio de detecção de um incidente. → [[Métricas - MTTD e MTTR]] · [[Ferramentas de Detecção e Resposta - EDR SIEM SOAR]] |
| **MTTR** | Tempo médio de resposta, resolução ou recuperação (defina a variante). → [[Métricas - MTTD e MTTR]] · [[Automação de Resposta a Incidentes]] |
| **Observabilidade** | Capacidade de entender o estado interno do sistema por logs, métricas e traces. → [[Logging Estruturado]] · [[Métricas e Tracing - Prometheus e OpenTelemetry]] |
| **OpenTelemetry** | Padrão aberto de instrumentação para logs, métricas e traces. → [[Métricas e Tracing - Prometheus e OpenTelemetry]] · [[Logging Estruturado]] |
| **Playbook** | Procedimento de resposta orientado a um cenário, com gatilho, decisões e ações. → [[Playbooks e Runbooks]] · [[SOAR - Shuffle TheHive Cortex e n8n]] |
| **Prometheus** | Sistema de métricas baseado em scrape de endpoints /metrics. → [[Métricas e Tracing - Prometheus e OpenTelemetry]] · [[Logging Estruturado]] |
| **Runbook** | Procedimento operacional documentado. → [[Playbooks e Runbooks]] · [[Automação de Resposta a Incidentes]] |
| **SIEM** | Coleta, normaliza e correlaciona logs para gerar alertas. → [[Ferramentas de Detecção e Resposta - EDR SIEM SOAR]] · [[Integração com SIEM - Splunk Elastic e Wazuh]] |
| **Sigma** | Formato genérico de regras de detecção para logs. → [[Regras Sigma]] · [[Detecção como Código]] |
| **SOAR** | Orquestração, automação e resposta de segurança. → [[SOAR - Shuffle TheHive Cortex e n8n]] · [[Ferramentas de Detecção e Resposta - EDR SIEM SOAR]] · [[Playbooks e Runbooks]] |
| **Suricata** | Motor open source de IDS, IPS e NSM. → [[Suricata - Integração]] · [[Ferramentas de Detecção e Resposta - EDR SIEM SOAR]] |
| **YARA** | Linguagem para identificar arquivos ou memória por padrões. → [[YARA - Integração]] · [[Regras Sigma]] |

### Código seguro

| Termo | Definição |
|---|---|
| **Allowlist** | Lista do que é permitido; abordagem mais robusta que a denylist para validação e exceções. → [[Validacao de Entrada]] · [[Redução de Falsos Positivos]] · [[SSRF Injeção e Desserialização Insegura]] |
| **Desserialização insegura** | Reconstrução de objetos a partir de dados não confiáveis com formatos executáveis. → [[SSRF Injeção e Desserialização Insegura]] · [[Validacao de Entrada]] |
| **Exit code** | Código de saída de um programa, usado por pipelines como resultado de gate. → [[CLI de Segurança]] · [[Security Gates e Shift-Left]] |
| **SSRF** | Server-Side Request Forgery: induzir o servidor a requisições indevidas. → [[SSRF Injeção e Desserialização Insegura]] · [[Privilégio Mínimo e Hardening de Containers]] |
| **XXE** | Entidades externas em XML que podem ler arquivos ou fazer requisições. → [[Parsing de Formatos - SARIF JSON e XML]] · [[Validacao de Entrada]] |

**Veja também:** [[MOC - Fundamentos - Integração]] · [[Panorama de Ferramentas de Segurança]]

## Automação de Segurança

Voltar ao índice: [[Home - Automação]].

### Frameworks, métricas e conformidade

| Termo | Definição |
|---|---|
| ATT&CK | Base de conhecimento de táticas e técnicas de adversários → [[Framework MITRE ATT&CK]] |
| CIS Controls | Conjunto priorizado de 18 controles defensivos → [[Framework CIS Controls]] |
| CVSS | Pontuação de severidade técnica de vulnerabilidades (0 a 10) → [[Priorização com CVSS, EPSS e KEV]] |
| EPSS | Probabilidade estimada de exploração de uma vulnerabilidade → [[Priorização com CVSS, EPSS e KEV]] |
| KEV | Catálogo de vulnerabilidades sabidamente exploradas → [[Priorização com CVSS, EPSS e KEV]] |
| LGPD | Lei Geral de Proteção de Dados → [[Aspectos Legais e LGPD]] |
| MTTD / MTTA / MTTR | Tempo médio para detectar / reconhecer / responder → [[Métricas - MTTD, MTTR, Falso Positivo e ROI]] |
| TLP | Protocolo de marcação de sensibilidade da informação → [[Feeds de Inteligência de Ameaças]] |

### Plataformas e detecção

| Termo | Definição |
|---|---|
| CSPM | Gestão da postura de segurança em nuvem → [[CSPM]] |
| Detection as Code | Gestão de detecções com práticas de engenharia de software → [[Detection as Code]] |
| EDR / XDR | Detecção e resposta em endpoints / estendida a várias camadas → [[EDR e XDR]] |
| IOC | Indicador de comprometimento (IP, domínio, hash) → [[Enriquecimento de IOCs]] |
| MISP | Plataforma aberta de compartilhamento de inteligência → [[MISP - Automação]] |
| SIEM | Coleta, correlação e alerta sobre logs → [[SIEM]] |
| Sigma | Formato aberto de regras de detecção para logs → [[Regras Sigma - Automação]] |
| SOAR | Orquestração, automação e resposta → [[SOAR]] |
| STIX / TAXII | Formato e transporte de inteligência de ameaças → [[STIX e TAXII]] |
| YARA | Linguagem de regras para classificar arquivos → [[YARA - Automação]] |

### DevSecOps e vulnerabilidades

| Termo | Definição |
|---|---|
| DAST | Teste dinâmico de aplicações em execução → [[DAST]] |
| Hardening | Redução da superfície de ataque por configuração segura → [[Hardening com CIS Benchmarks]] |
| IaC | Infraestrutura descrita como código → [[Infrastructure as Code]] |
| OPA / Rego | Motor de políticas e sua linguagem → [[Políticas como Código com OPA]] |
| SAST | Análise estática de código → [[SAST]] |
| SBOM | Lista de materiais de software → [[SBOM]] |
| SCA | Análise de composição de software → [[SCA]] |
| VEX | Declaração de explorabilidade de vulnerabilidades → [[SBOM]] |

### Operação e resposta

| Termo | Definição |
|---|---|
| DLQ | Fila de mensagens que falharam repetidamente → [[Webhooks, Filas e Integrações]] |
| HITL | Humano no circuito de decisão → [[Human in the Loop - Automação]] |
| Idempotência | Repetir uma operação não altera o resultado além da primeira vez → [[Orquestração via APIs]] |
| Playbook | Fluxo automatizado de resposta → [[SOAR]] |
| Prompt injection | Instruções maliciosas embutidas em dados processados por um LLM → [[Riscos de IA em Segurança]] |
| Rollback | Reversão de uma ação ao estado anterior → [[Rollback]] |
| Runbook | Procedimento operacional passo a passo → [[Runbooks]] |
| SoD | Segregação de funções → [[Segregação de Funções]] |
| TTL | Tempo de vida de uma ação ou indicador → [[Contenção Automatizada]] |

**Veja também:** [[MOC - Revisão - Automação]] · [[Banco de Exercícios]]

## Cibersegurança (Arsenal)

Voltar ao índice: [[MOC - Arsenal de Cibersegurança]].

### Conceitos fundamentais

| Termo | Definição |
|---|---|
| **Cadeia de Ataque (Cyber Kill Chain)** | Modelo que descreve as etapas sequenciais típicas de um ataque cibernético, da fase de reconhecimento à ação final sobre o objetivo. → [[Cadeia de Ataque - Cyber Kill Chain]] |
| **CIA Triad** | Os três pilares fundamentais da segurança da informação: Confidencialidade, Integridade e Disponibilidade. → [[CIA Triad]] |
| **Modelo OSI/TCP-IP** | Modelos conceituais em camadas que descrevem como a comunicação de rede é estruturada, base para entender onde cada ferramenta de segurança atua. → [[Modelo OSI-TCP-IP]] |

### Padrões e frameworks

| Termo | Definição |
|---|---|
| **ISO/IEC 27001** | Norma internacional certificável para implementação de um Sistema de Gestão de Segurança da Informação (SGSI). → [[ISO-IEC 27001]] |
| **MITRE ATT&CK** | Base de conhecimento pública que cataloga táticas, técnicas e procedimentos (TTPs) reais usados por adversários. → [[MITRE ATT&CK]] |
| **NIST Cybersecurity Framework** | Framework voluntário do governo americano para gestão de risco de cibersegurança em nível organizacional. → [[NIST Cybersecurity Framework]] |
| **OWASP Top 10** | Lista consolidada periodicamente dos dez riscos de segurança mais críticos em aplicações web. → [[OWASP Top 10]] |

**Veja também:** [[MOC - Conceitos]] · [[MOC - Padrões e Frameworks]] · [[Convenções do Arsenal]]
