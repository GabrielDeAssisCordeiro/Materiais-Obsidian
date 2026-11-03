---
titulo: "MOC - Projetos - Cpp"
tags: [cpp, moc, projetos]
aliases: ["Projetos guiados"]
tipo: moc
nivel: intermediario
padrao: C++20
criado: 2026-10-24
relacionados: ["[[Home - Cpp]]", "[[MOC - Testes e Qualidade - Cpp]]", "[[MOC - Build e Ferramentas]]"]
---

# MOC - Projetos - Cpp

Nove projetos completos, **compilados e testados** (g++ 13, `-std=c++20 -Wall -Wextra -Wpedantic`, CMake + CTest). Cada nota traz objetivos, estrutura de pastas, `CMakeLists.txt`, código comentado, como executar e extensões.

| # | Projeto | Nível | Foco |
|---|---|---|---|
| 1 | [[Projeto 1 - Calculadora de Expressões]] | Intermediário | Parser, AST, `variant` |
| 2 | [[Projeto 2 - Gerenciador de Tarefas CLI]] | Iniciante | Arquivos, STL, CLI |
| 3 | [[Projeto 3 - Biblioteca de Matrizes]] | Avançado | Templates, concepts, `constexpr` |
| 4 | [[Projeto 4 - Thread Pool]] | Avançado | Concorrência, futures |
| 5 | [[Projeto 5 - Servidor de Chat TCP]] | Avançado | Sockets POSIX, `poll`, RAII |
| 6 | [[Projeto 6 - Compressor Huffman]] | Intermediário | Árvores, `priority_queue`, bits |
| 7 | [[Projeto 7 - Máquina Virtual de Bytecode]] | Avançado | VM, assembler, `enum class` |
| 8 | [[Projeto 8 - Jogo da Vida]] | Intermediário | Laço de jogo, grade, testes |
| 9 | [[Projeto 9 - Parser JSON]] | Avançado | `variant` recursivo, parsing |

## Como trabalhar cada projeto

1. Leia **Objetivos** e **Arquitetura**.
2. Crie a estrutura de pastas e **digite** o código (não apenas copie).
3. Compile, rode os testes e depois faça as **Extensões**.
4. Rode com [[Sanitizers]] e leia os avisos do compilador ([[Flags Essenciais do Compilador]]).

## Veja também

- [[Home - Cpp]]
- [[MOC - Testes e Qualidade - Cpp]]
- [[MOC - Build e Ferramentas]]
- [[Estrutura de Projetos]]
