---
titulo: "FAQ - Cpp"
tags: [cpp, referencia, faq]
aliases: ["Dúvidas comuns"]
tipo: referencia
nivel: iniciante
padrao: C++20
criado: 2026-10-24
relacionados: ["[[Glossário#C++]]", "[[Erros Comuns de Iniciantes - Cpp]]", "[[Escolhendo o Padrão com -std]]"]
---

# FAQ - Cpp

## Aprendizado e escolhas

> [!question] Por onde começar?
> Siga a trilha em [[Trilha de Estudos - Cpp]]: [[MOC - Fundamentos - Cpp]] → [[MOC - Básico da Linguagem - Cpp]] → [[MOC - Ponteiros e Memória]] → [[MOC - Classes e POO]] → [[MOC - RAII e Move]] → STL, templates e o resto.

> [!question] Qual padrão (`-std`) devo usar?
> Para projetos novos, **C++20** é um bom piso (concepts, ranges, módulos, `jthread`, `std::format` em GCC 13+). C++23 se seu compilador suporta o que você precisa. C++26 ainda é novo (veja [[Cpp26 Visão Geral]] e [[Suporte dos Compiladores aos Padrões]]). Detalhes em [[Escolhendo o Padrão com -std]].

> [!question] GCC, Clang ou MSVC?
> Use o que sua plataforma pede (MSVC no Windows nativo, Clang no macOS, GCC no Linux), mas **teste com mais de um** — cada um acha problemas diferentes. Veja [[Compiladores GCC Clang e MSVC]].

> [!question] Preciso aprender C antes?
> Não. Aprender C++ moderno diretamente é melhor. Conheça os conceitos de C (ponteiros, strings terminadas em zero) para ler código legado: [[Cpp vs C]].

## Linguagem

> [!question] `struct` ou `class`?
> A única diferença técnica é o acesso padrão (`public` em `struct`, `private` em `class`). Convenção: `struct` para dados simples; `class` quando há invariantes e encapsulamento ([[Classes e Structs]]).

> [!question] Quando usar ponteiros? Referências? Smart pointers?
> Prefira **valores** e **referências**. Use `unique_ptr` quando precisar de heap/polimorfismo com dono único; `shared_ptr` só com posse realmente compartilhada; ponteiro cru para "observar" ([[Cheat Sheet de Smart Pointers]]).

> [!question] `new`/`delete` ainda existem?
> Sim, mas código moderno raramente os usa diretamente: contêineres e smart pointers cuidam da memória ([[RAII]]).

> [!question] Por que `std::endl` é "ruim"?
> Além de pular linha, descarrega o buffer (lento em saída intensa). Use `'\n'` ([[Entrada e Saída Básica]]).

> [!question] `i++` ou `++i`?
> Para tipos nativos é igual; para iteradores/classes, `++i` evita criar cópia. Prefira `++i` por hábito.

> [!question] Por que `main` não retorna nada explicitamente?
> Em `main`, chegar ao fim equivale a `return 0;` (regra especial).

> [!question] Posso comparar `double` com `==`?
> Quase nunca: use tolerância (`std::fabs(a - b) < eps`). Veja [[Tipos Fundamentais]].

> [!question] `auto` deixa o código confuso?
> Use quando o tipo é óbvio ou verboso (iteradores, lambdas); evite quando esconde informação importante ([[auto e decltype]]).

## Biblioteca e ferramentas

> [!question] `vector` ou `array`?
> `std::array` tamanho fixo conhecido em compilação (sem heap); `std::vector` o restante ([[Escolhendo um Contêiner]]).

> [!question] Como ler um número do teclado com segurança?
> Leia a **linha** com `getline` e converta (`stoi`/`from_chars`), tratando erros ([[Streams e iostream]]).

> [!question] Como depurar um *segfault*?
> Compile com `-g -fsanitize=address,undefined`, rode, leia o relatório; confirme com `gdb` (`bt`) — [[Sanitizers]], [[Cheat Sheet de GDB - Cpp]].

> [!question] Por que meu programa funciona em `-O0` e quebra em `-O2`?
> Quase sempre **comportamento indefinido**: [[Catálogo de Armadilhas e UB]].

> [!question] Como organizar meu projeto e compilar?
> [[Estrutura de Projetos]] e [[CMake Moderno e Presets]].

> [!question] Exceções são lentas?
> No caminho **sem erro** o custo é praticamente zero; o caminho **com erro** é lento (microssegundos). Não use para fluxo normal ([[Boas Práticas e Custo das Exceções]]).

> [!question] C++ é difícil/inseguro?
> É grande e permite erros de memória, mas o C++ moderno (RAII, smart pointers, ranges, `span`, hardening, [[Core Guidelines]]) reduz muito os riscos ([[Segurança e Hardening]]).

## Veja também

- [[Glossário#C++]]
- [[Erros Comuns de Iniciantes - Cpp]]
- [[Catálogo de Armadilhas e UB]]
- [[Livros Cursos e Comunidades - Cpp]]
- [[MOC - Referência - Cpp]]

## Exercício

1. Escolha 3 perguntas desta FAQ e escreva uma resposta mais completa com um exemplo de código.
2. Anote 5 dúvidas suas e responda cada uma com links para notas do vault.
