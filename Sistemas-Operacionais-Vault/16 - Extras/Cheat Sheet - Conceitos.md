---
titulo: "Cheat Sheet - Conceitos"
tags:
  - sistemas-operacionais
  - cheatsheet
tipo: cheatsheet
nivel: intermediario
relacionados:
  - "[[Cheat Sheet - Comandos]]"
  - "[[Glossário#Sistemas Operacionais]]"
  - "[[MOC - Extras]]"
---

# Cheat Sheet - Conceitos

## Fórmulas

| Tema | Fórmula |
|---|---|
| Tempo de retorno | término − chegada |
| Tempo de espera | retorno − burst |
| Tempo de resposta | primeira execução − chegada |
| Utilização RM (tempo real) | Σ Cᵢ/Tᵢ ≤ n(2^(1/n) − 1) |
| EDF | Σ Cᵢ/Tᵢ ≤ 1 |
| Endereço físico | quadro × tamanho da página + offset |
| Bits de offset | log₂(tamanho da página) |
| Entradas da tabela | 2^(bits de endereço − bits de offset) |
| Tempo efetivo de acesso | h·(t_TLB + t_mem) + (1−h)·(t_TLB + 2·t_mem) |
| Taxa de falta de páginas efetiva | EAT = (1−p)·t_mem + p·t_falta |
| Lei de Amdahl | S = 1 / ((1−f) + f/n) |

## Números de referência

| Item | Ordem de grandeza |
|---|---|
| Acesso a registrador | < 1 ns |
| Cache L1/L2/L3 | ~1 / 4 / 15 ns |
| Memória RAM | ~100 ns |
| SSD NVMe (leitura) | ~20–100 µs |
| HDD (seek) | ~5–10 ms |
| Context switch | ~1–5 µs |
| Syscall simples | ~100 ns–1 µs |
| Página padrão | 4 KB (16 KB em Apple Silicon) |

## Comparativos rápidos

| Algoritmo | Preemptivo | Vantagem | Problema |
|---|---|---|---|
| [[FCFS - First Come, First Served]] | Não | Simples | Efeito comboio |
| [[SJF e SRTF - Menor Job Primeiro]] | Opcional (SRTF) | Mínima espera média | Starvation, previsão |
| [[Round Robin]] | Sim | Justo, boa resposta | Escolha do quantum |
| [[Escalonamento por Prioridades]] | Opcional | Controle | Starvation |
| [[MLFQ - Multilevel Feedback Queue]] | Sim | Adaptativo | Ajuste complexo |

| Primitiva | Espera | Uso |
|---|---|---|
| [[Operações Atômicas e Spinlocks|Spinlock]] | Ocupada | Seções curtas |
| [[Mutex]] | Bloqueia | Exclusão mútua |
| [[Semáforos|Semáforo]] | Bloqueia | Contagem de recursos |
| [[Monitores e Variáveis de Condição|Monitor]] | Bloqueia | Encapsulamento + variáveis de condição |

| Substituição de páginas | Ideia | Observação |
|---|---|---|
| FIFO | Mais antiga | Anomalia de Belady |
| LRU | Menos recentemente usada | Boa, custosa de implementar |
| Clock | Aproxima LRU | Usado na prática |
| Ótimo | Futuro mais distante | Teórico (referência) |

Ver [[Algoritmos de Substituição de Páginas]].

## Arquiteturas

| Arquitetura | Característica | Exemplos |
|---|---|---|
| [[Kernel Monolítico]] | Tudo no kernel | Linux, FreeBSD |
| [[Microkernel]] | Mínimo no kernel, serviços em user space | Minix, QNX |
| [[Kernel Híbrido]] | Mistura | Windows NT, XNU |
| [[Exokernel]] | Expõe hardware | Pesquisa |
| [[Unikernel]] | App + SO em uma imagem | MirageOS |

## Deadlock

Coffman: exclusão mútua, posse e espera, não preempção, espera circular. Estratégias: prevenir, evitar (banqueiro), detectar e recuperar, ignorar ([[Deadlock (Impasse)]]).

## Sistemas de arquivos

| FS | Destaque |
|---|---|
| [[ext4]] | Journal, extents, padrão Linux |
| [[NTFS]] | Journal, ACLs, MFT |
| [[APFS]] | CoW, snapshots, clones |
| [[Btrfs]] / [[ZFS]] | CoW, checksums, snapshots, RAID |

## Pontos-chave

- Memorize as fórmulas de escalonamento e paginação.
- Saiba as ordens de grandeza para raciocinar sobre desempenho.

## Veja também

[[Cheat Sheet - Comandos]] · [[Glossário#Sistemas Operacionais]]
