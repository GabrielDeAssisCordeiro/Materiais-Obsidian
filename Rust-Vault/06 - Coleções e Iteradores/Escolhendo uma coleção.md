---
tags: [rust, colecoes, comparacao]
aliases: ["qual coleção usar", "complexidade das coleções"]
tipo: comparacao
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Vec]]", "[[HashMap]]", "[[HashSet]]", "[[BTreeMap]]", "[[VecDeque]]", "[[BinaryHeap]]"]
---

# Escolhendo uma coleção

| Preciso de... | Use | Observação |
|---|---|---|
| Sequência indexável | `Vec<T>` | padrão; comece por aqui |
| Fila FIFO ou deque | `VecDeque<T>` | O(1) nas duas pontas |
| Chave → valor, sem ordem | `HashMap<K, V>` | O(1) médio |
| Chave → valor, ordenado/intervalos | `BTreeMap<K, V>` | O(log n) |
| Conjunto sem ordem | `HashSet<T>` | |
| Conjunto ordenado | `BTreeSet<T>` | |
| Prioridade | `BinaryHeap<T>` | `pop` dá o maior |
| Lista encadeada | `LinkedList<T>` | raramente a melhor escolha |

## Complexidade resumida

| Operação | Vec | VecDeque | HashMap | BTreeMap |
|---|---|---|---|---|
| Acesso por índice/chave | O(1) | O(1) | O(1) | O(log n) |
| Inserir no fim | O(1)* | O(1)* | O(1)* | O(log n) |
| Inserir no início | O(n) | O(1) | n/a | n/a |
| Buscar valor | O(n) | O(n) | O(1) | O(log n) |

\* amortizado

> [!tip] Meça antes de trocar
> Por localidade de cache, `Vec` costuma superar estruturas "teoricamente melhores" para tamanhos pequenos.

## Veja também

- [[Vec]]
- [[HashMap]]
- [[HashSet]]
- [[BTreeMap]]
- [[VecDeque]]
- [[BinaryHeap]]
