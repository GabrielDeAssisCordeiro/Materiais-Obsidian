---
titulo: "Exercícios com Gabarito"
tags:
  - sistemas-operacionais
  - exercicio
tipo: exercicio
nivel: intermediario
relacionados:
  - "[[MOC - Extras]]"
  - "[[Trilha de aprendizado - SO]]"
  - "[[Glossário#Sistemas Operacionais]]"
---

# Exercícios com Gabarito

## Resumo

Questões por tema. Responda antes de abrir o gabarito (na seção final).

## Enunciados

### Fundamentos e arquitetura
1. Cite três razões para existir a separação user/kernel ([[Kernel vs User Space]]).
2. Descreva os passos de uma syscall `read()` ([[System Calls]]).
3. Diferencie interrupção, trap e exceção ([[Interrupções]], [[Traps e Exceções]]).
4. Compare microkernel e monolítico quanto a desempenho e isolamento ([[Comparação de Arquiteturas com Exemplos Reais]]).

### Processos e escalonamento
5. Processos P1(chegada 0, burst 7), P2(1, 4), P3(2, 1), P4(3, 4). Calcule o tempo médio de espera com **FCFS** e **SJF não preemptivo** ([[FCFS - First Come, First Served]], [[SJF e SRTF - Menor Job Primeiro]]).
6. Mesmos processos com **Round Robin** (quantum 3, ordem de chegada na fila). Qual o tempo de término de cada um? ([[Round Robin]])
7. O que é *starvation* e como o *aging* resolve? ([[Escalonamento por Prioridades]])
8. Por que `fork()` é barato com copy-on-write? ([[Criação e Término de Processos]])

### Sincronização
9. Dê um exemplo de race condition e corrija com mutex ([[Condições de Corrida]], [[Mutex]]).
10. Cite as quatro condições de Coffman para deadlock ([[Deadlock (Impasse)]]).
11. Sistema com 3 processos e 1 tipo de recurso, total 10. Alocado: P0=3, P1=2, P2=2; máximo: P0=9, P1=4, P2=7. Estado seguro? ([[Soluções para Deadlock]])
12. Diferencie spinlock e mutex, e quando usar cada um ([[Operações Atômicas e Spinlocks]]).

### Memória
13. Endereço virtual de 32 bits, página de 4 KB. Quantos bits de offset e de número de página? Quantas entradas tem a tabela de página de nível único?
14. Referências: 7,0,1,2,0,3,0,4,2,3 com 3 quadros. Conte as faltas em **FIFO** e **LRU** ([[Algoritmos de Substituição de Páginas]]).
15. Por que a TLB melhora o desempenho? Calcule o tempo efetivo: TLB hit 90%, acesso TLB 1 ns, memória 100 ns ([[TLB - Translation Lookaside Buffer]]).
16. Diferencie fragmentação interna e externa ([[Paginação]], [[Segmentação]]).

### Arquivos, E/S e boot
17. O que um inode contém e o que **não** contém? ([[Inodes]])
18. Journaling x CoW: diferença e vantagens ([[Journaling e Copy-on-Write]], [[ZFS]]).
19. Compare polling, interrupção e DMA ([[Entrada e Saída (E-S)]], [[DMA - Acesso Direto à Memória]]).
20. Liste as etapas do boot de um PC UEFI até a tela de login ([[Processo de Boot]]).

### Segurança e virtualização
21. Como ASLR e DEP/NX se complementam? ([[ASLR - Address Space Layout Randomization]], [[DEP, NX e Mitigações de Exploração]])
22. Container x VM: isolamento e custo ([[Containers]], [[Virtualização]]).
23. Quais namespaces o Docker usa e para quê? ([[Namespaces do Linux - SO]])

### Prática
24. Qual comando lista os 5 processos que mais usam memória no Linux? E no PowerShell?
25. Como descobrir qual processo ocupa a porta 8080 em Linux, Windows e macOS?

## Gabarito

1. Proteção (apps não acessam hardware/memória alheia), estabilidade (falha de app não derruba o sistema) e controle de recursos/segurança (o kernel arbitra).
2. Programa chama wrapper da libc → coloca número da syscall e argumentos em registradores → instrução `syscall`/`svc` → CPU muda para modo kernel e salta para o *handler* → kernel valida argumentos, executa (VFS → driver; processo pode bloquear) → retorna valor em registrador → volta a modo usuário.
3. **Interrupção**: assíncrona, de hardware (teclado, timer). **Trap**: síncrona e intencional (syscall, breakpoint). **Exceção/falta**: síncrona, causada pela instrução (divisão por zero, page fault).
4. Monolítico: mais rápido (chamadas diretas, sem IPC), menos isolado (bug de driver derruba tudo). Microkernel: mais isolado/modular, porém IPC adiciona custo; híbridos buscam equilíbrio.
5. **FCFS** (ordem P1,P2,P3,P4): inícios 0,7,11,12; esperas 0,6,9,9 → média **6,0**. **SJF** (P1 roda 0–7; depois P3(1), P2(4), P4(4)): inícios P1=0, P3=7, P2=8, P4=12; esperas 0, 7−2=5, 8−1=7, 12−3=9 → total 21 → média **5,25**.
6. RR q=3 (fila: P1 chega 0; P2 em 1; P3 em 2; P4 em 3). Linha do tempo: P1 0–3 (resta 4); fila P2,P3,P4,P1. P2 3–6 (resta 1); P3 6–7 (**termina em 7**); P4 7–10 (resta 1); P1 10–13 (resta 1); P2 13–14 (**termina em 14**); P4 14–15 (**termina em 15**); P1 15–16 (**termina em 16**). Términos: P1=16, P2=14, P3=7, P4=15.
7. *Starvation*: processo de baixa prioridade nunca executa. *Aging*: aumentar gradualmente a prioridade de quem espera.
8. Pai e filho compartilham páginas marcadas como somente leitura; só quando um escreve ocorre falha de proteção e a página é copiada. Evita copiar o espaço inteiro (especialmente se seguido de `exec`).
9. Dois threads fazem `contador++` (ler-somar-gravar) e perdem atualizações. Correção: `pthread_mutex_lock(&m); contador++; pthread_mutex_unlock(&m);` ou usar `atomic_fetch_add`.
10. Exclusão mútua, posse e espera (*hold and wait*), não preempção e espera circular.
11. Disponível = 10 − (3+2+2) = 3. Necessidades: P0=6, P1=2, P2=5. P1 pode terminar (2 ≤ 3): libera 2 → disp. 5. P2 (5 ≤ 5): libera 2 → disp. 7. P0 (6 ≤ 7). Sequência segura **P1, P2, P0** → estado **seguro**.
12. Spinlock: espera ocupada, sem dormir; ideal para seções curtíssimas e contextos que não podem dormir (interrupções, multiprocessador). Mutex: bloqueia a thread (sleep); melhor para seções longas ou que podem bloquear.
13. Offset = 12 bits; número de página = 20 bits; **2²⁰ = 1.048.576 entradas**.
14. **FIFO (3 quadros)**: 7F 0F 1F 2F(sai 7) 0H 3F(sai 0) 0F(sai 1) 4F(sai 2) 2F(sai 3) 3F(sai 0) → **9 faltas** (1 acerto). **LRU**: 7F 0F 1F 2F(sai 7) 0H 3F(sai 1) 0H 4F(sai 2) 2F(sai 3) 3F(sai 0) → **8 faltas** (2 acertos).
15. Tempo efetivo = 0,9×(1+100) + 0,1×(1+100+100) = 90,9 + 20,1 = **111 ns** (sem TLB: 200 ns com tabela de 1 nível).
16. Interna: espaço desperdiçado dentro de uma unidade alocada (última página parcial). Externa: espaços livres pequenos e não contíguos entre blocos de tamanho variável (segmentação, alocação contígua).
17. Contém: tipo, permissões, dono, tamanhos, timestamps, contagem de links e ponteiros/extents para blocos. **Não** contém o nome do arquivo (fica na entrada de diretório).
18. Journaling: grava intenção em log e depois aplica (recupera repetindo/descartando). CoW: nunca sobrescreve, escreve em novo local e atualiza ponteiros atomicamente; facilita snapshots e checksums.
19. Polling: CPU consulta repetidamente (simples, desperdiça CPU). Interrupção: dispositivo avisa (CPU livre, custo por evento). DMA: controlador transfere blocos à memória e interrompe só no fim (ideal para grandes volumes).
20. Firmware UEFI (POST) → lê ESP e carrega bootloader (GRUB/systemd-boot/Windows Boot Manager) → carrega kernel + initramfs → kernel inicializa → monta raiz → inicia PID 1 (systemd) → serviços → gerenciador de login.
21. DEP/NX impede executar código injetado em pilha/heap; ASLR dificulta saber endereços para reutilizar código existente (ROP). Juntos reduzem a exploração.
22. VM: kernel próprio por VM, isolamento forte, mais pesada. Container: compartilha o kernel do host, leve e rápido, isolamento menor (superfície de ataque do kernel).
23. `pid` (árvore de processos), `net` (pilha de rede), `mnt` (pontos de montagem), `uts` (hostname), `ipc`, `user` (mapeamento de UIDs) e `cgroup`.
24. Linux: `ps aux --sort=-%mem | head -6`. PowerShell: `Get-Process | Sort WS -Descending | Select -First 5`.
25. Linux: `ss -ltnp 'sport = :8080'` ou `lsof -i :8080`. Windows: `netstat -ano | findstr :8080` + `tasklist /fi "PID eq N"`. macOS: `lsof -nP -iTCP:8080 -sTCP:LISTEN`.

> [!warning] Conferência
> Refaça os cálculos (5, 6, 14, 15) por conta própria; a prática de simulação é o objetivo.

## Pontos-chave

- Treine simulações (escalonamento, substituição de páginas, banqueiro) à mão.
- Relacione cada resposta à nota de origem.

## Veja também

[[Glossário#Sistemas Operacionais]] · [[Trilha de aprendizado - SO]] · [[MOC - Extras]]
