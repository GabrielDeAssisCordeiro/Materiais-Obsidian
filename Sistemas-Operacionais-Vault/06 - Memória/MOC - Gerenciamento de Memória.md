---
titulo: "MOC - Gerenciamento de Memória"
tags:
  - sistemas-operacionais
  - moc
  - memoria
tipo: moc
nivel: intermediario
relacionados:
  - "[[Gerenciamento de Memória]]"
  - "[[Memória Virtual]]"
  - "[[Paginação]]"
  - "[[Algoritmos de Substituição de Páginas]]"
---

# MOC - Gerenciamento de Memória

> [!info] Escopo
> Como o SO aloca, protege e virtualiza a memória física para dar a cada processo um espaço de endereços próprio e maior que a RAM disponível.

## Trilha

1. [[Gerenciamento de Memória]]: objetivos, alocação contígua, fragmentação
2. [[Segmentação]]: divisão lógica do espaço de endereços
3. [[Paginação]]: páginas, quadros e tabelas de páginas
4. [[Memória Virtual]]: endereços virtuais, paginação sob demanda, proteção
5. [[TLB - Translation Lookaside Buffer]]: cache de traduções
6. [[Page Faults]]: tipos e tratamento
7. [[Algoritmos de Substituição de Páginas]]: FIFO, LRU, Clock, Ótimo
8. [[Swap e Thrashing]]: área de troca, thrashing, memória comprimida
9. [[Alocadores de Memória]]: `malloc`, buddy, slab

## Ferramentas relacionadas

[[free]] · [[vmstat]] · [[cgroups - SO]]

## Pré-requisitos

[[Processos]] · [[Traps e Exceções]] · [[Kernel vs User Space]]
