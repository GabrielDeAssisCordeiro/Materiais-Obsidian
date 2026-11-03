---
titulo: "Flashcards - Cpp"
tags: [cpp, flashcards, revisao]
aliases: ["Flashcards de C++"]
tipo: referencia
nivel: intermediario
padrao: C++20
criado: 2026-10-24
relacionados: ["[[Glossário#C++]]", "[[MOC - Exercícios - Cpp]]", "[[FAQ - Cpp]]"]
---

# Flashcards - Cpp

Formato `pergunta::resposta` (uma por linha), compatível com plugins de repetição espaçada como o *Spaced Repetition* (opcional; o vault **não** instala plugins). Também funciona como autoteste: cubra o lado direito.

> [!tip] Como usar
> Revise 10 cartões por dia. Errou? Abra a nota do **Veja também** ao lado da seção e refaça o exemplo.

## Fundamentos e básico
Qual a diferença entre declaração e definição?::Declaração apresenta o nome/tipo; definição aloca/implementa. Uma entidade pode ser declarada várias vezes, definida uma ([[Declaração vs Definição e ODR]]).
O que `constexpr` garante?::Que o valor **pode** ser calculado em compilação (e deve, em contexto constante) ([[const e constexpr]]).
Diferença entre `auto` e `decltype(auto)`?::`auto` remove ref/const de topo; `decltype(auto)` preserva a categoria exata da expressão ([[auto e decltype]]).
`i++` ou `++i` para iteradores?::`++i` (evita cópia temporária).
Por que `'\n'` em vez de `std::endl`?::`endl` também descarrega o buffer (lento).
O que é UB?::Comportamento indefinido: o padrão não impõe requisito; o compilador assume que não ocorre ([[Comportamento Indefinido e Não Especificado]]).
Overflow de `int` é definido?::Não (UB). Em tipos sem sinal faz *wrap*.

## Ponteiros e memória
Quem libera memória de `new[]`?::`delete[]` (nunca `delete`).
O que é *dangling pointer*?::Ponteiro/referência para objeto já destruído ([[Vazamentos e Dangling Pointers]]).
Diferença entre referência e ponteiro?::Referência é alias não nulo e não reatribuível; ponteiro pode ser nulo e reapontado ([[Referências - Cpp]]).
Onde vivem variáveis locais?::Na pilha (*stack*); `new` aloca no *heap* ([[Stack vs Heap]]).
O que `nullptr` resolve?::Ambiguidade de `0`/`NULL` com inteiros; tem tipo `std::nullptr_t` ([[nullptr]]).

## Classes e POO
Quando o destrutor precisa ser `virtual`?::Quando se destrói objeto derivado via ponteiro/referência para a base ([[Polimorfismo e Funções Virtuais]]).
O que é *slicing*?::Copiar derivado para base por valor, perdendo a parte derivada ([[Slicing]]).
Para que serve `explicit`?::Impede conversões implícitas por construtor/operador ([[Conversões Implícitas e explicit]]).
O que `override` faz?::Pede ao compilador verificar que a função realmente sobrescreve uma virtual ([[override e final]]).
Ordem de construção em herança?::Bases → membros (na ordem de declaração) → corpo do construtor; destruição na ordem inversa.

## RAII e move
O que é RAII?::Atrelar o ciclo de vida de um recurso ao de um objeto: adquire no construtor, libera no destrutor ([[RAII]]).
Regra do zero?::Se possível, não declare nenhum membro especial; deixe membros RAII cuidarem ([[Regra do 0, 3 e 5]]).
O que `std::move` faz?::Só converte para rvalue (*cast*); quem move é o construtor/atribuição de movimento ([[std move e std forward]]).
Estado de objeto movido?::Válido, porém não especificado: só destrua ou reatribua.
`unique_ptr` vs `shared_ptr`?::Posse exclusiva (custo zero) vs posse compartilhada com contagem de referências ([[unique_ptr]], [[shared_ptr]]).
Para que `weak_ptr`?::Observar sem possuir; quebra ciclos de `shared_ptr` ([[weak_ptr]]).
Por que `make_unique`?::Segurança de exceção, menos repetição e sem `new` explícito ([[make_unique e make_shared]]).

## Templates e concepts
O que é SFINAE?::Falha de substituição não é erro: remove a sobrecarga da resolução ([[SFINAE e enable_if]]).
O que um *concept* faz?::Nomeia requisitos sobre tipos, com erros claros ([[Concepts e requires]]).
Para que `if constexpr`?::Escolher ramo em compilação, descartando o outro na instanciação ([[if constexpr]]).
O que é CTAD?::Dedução de argumentos de template de classe a partir do construtor ([[CTAD]]).
O que é uma *fold expression*?::Reduz um *parameter pack* com um operador: `(args + ...)` ([[Variadic Templates e Fold Expressions]]).

## STL e ranges
Complexidade de `vector::push_back`?::Amortizado O(1); invalida iteradores se realocar.
`map` vs `unordered_map`?::Árvore ordenada O(log n) vs hash médio O(1) ([[map e set]], [[unordered_map e unordered_set]]).
Idioma remove-erase?::`v.erase(std::remove_if(...), v.end())`; em C++20, `std::erase_if(v, pred)`.
O que são *views*?::Visões preguiçosas e não proprietárias sobre ranges ([[Ranges e Views]]).
Quando usar `span`?::Para passar sequência contígua sem dono (ponteiro + tamanho) ([[span]]).
`optional` vs `expected`?::`optional`: valor ou nada; `expected`: valor ou erro (C++23) ([[optional]], [[expected]]).

## Erros e strings
Garantias de segurança de exceção?::Básica, forte, no-throw ([[Segurança de Exceções]]).
Quando usar `noexcept`?::Em funções que não lançam; essencial em movimentos ([[noexcept e Movimento]]).
`string_view` é seguro?::Apenas enquanto o dado apontado viver ([[string_view]]).
Como formatar em C++20?::`std::format("{:>8.2f}", x)` ([[Formatação std format e std print]]).

## Concorrência
O que é *data race*?::Dois acessos concorrentes à mesma memória, ao menos um de escrita, sem sincronização: UB ([[Data Races e Deadlocks]]).
`jthread` vs `thread`?::`jthread` faz join automático e suporta `stop_token` ([[Threads e jthread]]).
Por que predicado em `cv.wait`?::Protege contra despertares espúrios ([[condition_variable]]).
`atomic` substitui `mutex`?::Só para operações simples isoladas; invariantes entre várias variáveis exigem lock ([[Atomics e Modelo de Memória]]).

## Build, testes e performance
Para que servem os sanitizers?::Detectam erros em execução: ASan (memória), UBSan (UB), TSan (races) ([[Sanitizers]]).
Include guard vs `#pragma once`?::Ambos evitam inclusão múltipla; guard é padrão, `pragma once` é amplamente suportado ([[Include Guards e pragma once]]).
O que é a ODR?::Regra de uma definição: entidades têm uma definição no programa ([[Declaração vs Definição e ODR]]).
Por que SoA pode ser mais rápido?::Melhor localidade de cache ([[Cache e Localidade de Dados]]).
O que é *false sharing*?::Threads escrevendo em variáveis distintas na mesma linha de cache ([[False Sharing]]).
CMake moderno em uma frase?::Alvos (`target_*`) com propriedades `PUBLIC/PRIVATE/INTERFACE` ([[CMake Moderno e Presets]]).

## Veja também

- [[Glossário#C++]]
- [[FAQ - Cpp]]
- [[Catálogo de Armadilhas e UB]]
- [[MOC - Exercícios - Cpp]]

## Exercício

Escreva 10 cartões novos sobre os tópicos em que você mais errou e acrescente-os a uma cópia desta nota.
