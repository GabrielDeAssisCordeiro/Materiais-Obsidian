---
titulo: "MOC - Escalonamento"
tags:
  - sistemas-operacionais
  - moc
  - escalonamento
tipo: moc
nivel: intermediario
relacionados:
  - "[[Escalonamento de Processos]]"
  - "[[Round Robin]]"
  - "[[CFS - Completely Fair Scheduler]]"
  - "[[Escalonamento de Tempo Real]]"
---

# MOC - Escalonamento

> [!info] Escopo
> Como o SO decide qual processo ou thread usa a CPU, quando e por quanto tempo.

## Fundamentos

- [[Escalonamento de Processos]]: objetivos, métricas, preemptivo x não preemptivo

## Algoritmos clássicos

| Nota | Resumo |
|---|---|
| [[FCFS - First Come, First Served]] | Primeiro a chegar, primeiro a ser servido |
| [[SJF e SRTF - Menor Job Primeiro]] | Menor job primeiro (e SRTF, versão preemptiva) |
| [[Round Robin]] | Fatias de tempo circulares |
| [[Escalonamento por Prioridades]] | Maior prioridade primeiro; envelhecimento |
| [[MLFQ - Multilevel Feedback Queue]] | Múltiplas filas com realimentação |

## Escalonadores reais e tempo real

- [[CFS - Completely Fair Scheduler]]: Completely Fair Scheduler do Linux (e o sucessor EEVDF)
- [[Escalonamento de Tempo Real]]: RM, EDF, SCHED_FIFO

## Relacionados

[[Context Switch (Troca de Contexto)]] · [[Estados de Processo]] · [[SO de Tempo Compartilhado]] · [[SO de Tempo Real (RTOS)]] · [[MOC - Processos e Threads]]
