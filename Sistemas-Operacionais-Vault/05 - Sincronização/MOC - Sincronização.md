---
titulo: "MOC - Sincronização"
tags:
  - sistemas-operacionais
  - moc
  - sincronizacao
tipo: moc
nivel: intermediario
relacionados:
  - "[[Condições de Corrida]]"
  - "[[Mutex]]"
  - "[[Semáforos]]"
  - "[[Deadlock (Impasse)]]"
---

# MOC - Sincronização

> [!info] Escopo
> Como coordenar threads e processos que compartilham dados, evitando resultados incorretos (corridas) e travamentos (deadlocks).

## Trilha

1. [[Condições de Corrida]]: o problema
2. [[Seção Crítica]]: o requisito de exclusão mútua
3. [[Operações Atômicas e Spinlocks]]: suporte de hardware
4. [[Mutex]]: trava de exclusão mútua
5. [[Semáforos]]: contadores de recursos e sinalização
6. [[Monitores e Variáveis de Condição]]: sincronização estruturada com variáveis de condição
7. [[Problemas Clássicos de Sincronização]]: produtor-consumidor, leitores-escritores, jantar dos filósofos
8. [[Deadlock (Impasse)]]: condições e detecção
9. [[Soluções para Deadlock]]: prevenção, evitação (banqueiro), detecção e recuperação

## Pré-requisitos

[[Threads - SO]] · [[Processos]] · [[Context Switch (Troca de Contexto)]] · [[Interrupções]]

## Relacionados

[[IPC - Comunicação entre Processos]] · [[Escalonamento por Prioridades]] (inversão de prioridade) · [[Escalonamento de Tempo Real]]
