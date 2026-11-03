---
titulo: "MOC — RAII e Move"
tags: [cpp, moc, raii, move, smart-pointers]
aliases: ["MOC RAII e Move", "Gerenciamento de Recursos"]
tipo: moc
nivel: intermediario
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Home - Cpp]]", "[[MOC - Classes e POO]]"]
---

# MOC — RAII e Move

Como o C++ moderno gerencia recursos de forma automática e eficiente: tempo de vida determinístico, cópia, movimento e posse expressa em tipos.

## Idioma central

- [[RAII]]
- [[Regra do 0, 3 e 5]]

## Cópia e movimento

- [[Construtores de Cópia e Atribuição]]
- [[Semântica de Movimento]]
- [[std move e std forward]]
- [[Referências Universais e Perfect Forwarding]]
- [[Copy Elision e RVO]]
- [[noexcept e Movimento]]

## Smart pointers

- [[unique_ptr]]
- [[shared_ptr]]
- [[weak_ptr]]
- [[make_unique e make_shared]]
- [[Deleters Customizados]]
- [[Ciclos de Referência]]

## Guia de decisão: qual tipo de ponteiro?

| Pergunta | Resposta |
|---|---|
| Há **um** dono claro? | `std::unique_ptr<T>` |
| Há **vários** donos com vida compartilhada? | `std::shared_ptr<T>` |
| Preciso **observar** sem possuir, objeto pode morrer? | `std::weak_ptr<T>` |
| Preciso **usar** sem possuir, objeto sobrevive à chamada? | `T&` ou `T*` |
| Recurso não é memória? | Smart pointer com [[Deleters Customizados\|deleter]] ou classe RAII própria |
| Valor pequeno ou coleção? | Valor/`std::vector` (sem ponteiro) |

## Mapa de gerenciamento de recursos

Veja também o mapa conceitual (Canvas) em `Anexos`.

## Veja também

- [[Home - Cpp]]
- [[MOC - Classes e POO]]
- [[MOC - Ponteiros e Memória]]
