---
titulo: "Como Usar este Vault - Cpp"
tags: [cpp, inicio, guia]
aliases: ["Como usar", "Guia do vault", "Sobre este vault"]
tipo: guia
nivel: iniciante
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Home - Cpp]]", "[[Convenções - Cpp]]"]
---

# Como Usar este Vault - Cpp

Este vault é um material de estudos completo de **C++ moderno** (C++11 a C++23, com notas sobre C++26), em português do Brasil, organizado para o Obsidian.

## Abrindo

1. Descompacte o `.zip`.
2. No Obsidian: **Abrir pasta como cofre** e selecione a pasta `Materiais-Obsidian`. Este material fica na subpasta `Cpp-Vault` (veja o [[README]]).
3. Comece por [[Home - Cpp]].

## Navegação

| Recurso | Para quê |
|---|---|
| **MOCs** (*Maps of Content*) | Cada pasta tem um `MOC - ...` listando suas notas |
| **Graph view** | Visualize as relações entre conceitos (`Ctrl/Cmd + G`) |
| **Backlinks** | Veja quem aponta para a nota atual |
| **Busca** | `Ctrl/Cmd + Shift + F`; tente `tag:#cpp20` ou `path:"06 - Templates"` |
| **Propriedades** | Filtre por `nivel` e `padrao` no frontmatter |
| **Canvas** | Mapas conceituais na pasta `Anexos` da raiz do vault ([[MOC - Anexos]]) |

## Como estudar

- Siga a numeração das pastas: **01 → 19**. Cada pasta é um bloco coerente.
- **Digite e compile** os exemplos. Todo bloco de código `cpp` compilável começa com um comentário que mostra a flag de compilação.
- Faça os exercícios no fim de cada nota e os da pasta `19 - Exercícios`.
- Leia os callouts: `[!warning]`, `[!bug]` e `[!danger]` marcam armadilhas e comportamento indefinido.

## Convenção de código

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>

int main() {
    std::cout << "Todo exemplo indica como compilar na primeira linha.\n";
}
```

Veja todas as convenções em [[Convenções - Cpp]].

> [!tip] Ambiente de testes
> Se ainda não instalou nada, use o Compiler Explorer (godbolt.org) para experimentar, e depois configure o ambiente local com [[Instalação no Linux - Cpp]], [[Instalação no Windows]] ou [[Instalação no macOS - Cpp]].

## Veja também

- [[Home - Cpp]]
- [[Convenções - Cpp]]
- [[MOC - Fundamentos - Cpp]]
- [[Primeiro Programa]]
