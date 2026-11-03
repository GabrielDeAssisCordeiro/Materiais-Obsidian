---
tags: [rust, flashcards, ownership, fundamentos]
aliases: ["Flashcards 1"]
tipo: flashcards
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Ownership e regras]]", "[[Borrowing e referências]]", "[[Lifetimes]]", "[[Move, Copy e Clone]]", "[[Flashcards de traits, erros e concorrência]]"]
---

# Flashcards de fundamentos e ownership

Cartões sobre os alicerces da linguagem. Veja [[Ownership e regras]] e [[Cheat sheet de ownership]].

> [!tip] Como usar
> Leia a pergunta, responda mentalmente e confira. Para repetição espaçada, qualquer plugin de flashcards que aceite o formato `pergunta::resposta` (linha única) funciona; sem plugin, as notas continuam legíveis.

O que é ownership?::O modelo em que cada valor tem exatamente um dono; quando o dono sai de escopo, o valor é liberado.
Quais são as 3 regras de ownership?::Cada valor tem um dono; só há um dono por vez; o valor é descartado quando o dono sai de escopo.
O que acontece ao atribuir uma String a outra variável?::O ownership é movido (move); a variável original deixa de ser válida.
Qual a diferença entre Copy e Clone?::Copy é uma cópia implícita bit a bit de tipos simples; Clone é uma duplicação explícita via .clone(), possivelmente cara.
Quais tipos são Copy?::Inteiros, floats, bool, char, referências compartilhadas e tuplas/arrays formados só por tipos Copy.
Qual a regra de borrowing?::Ou várias referências compartilhadas (&T), ou uma única referência mutável (&mut T), nunca as duas ao mesmo tempo.
O que é NLL?::Non-Lexical Lifetimes: um empréstimo termina no último uso da referência, não no fim do escopo.
O que significa uma anotação de lifetime como &'a str?::Que a referência é válida pelo menos durante o lifetime 'a; relaciona a validade de entradas e saídas.
O que é elisão de lifetimes?::Regras que permitem omitir lifetimes em assinaturas quando a relação é óbvia.
O que é &'static?::Uma referência válida durante todo o programa, como literais de string.
Por que não se pode retornar uma referência para uma variável local?::Porque a variável é destruída no fim da função, deixando a referência pendente (dangling).
Quando preferir &str a String em parâmetros?::Quando a função só lê o texto; aceita tanto &String quanto literais.
Qual a diferença entre let mut x e let x = &mut y?::O primeiro permite alterar a variável x; o segundo cria uma referência mutável ao valor de y.
O que o compilador diz em E0382?::Que um valor foi usado depois de movido (borrow of moved value).
O que é shadowing?::Declarar uma nova variável com o mesmo nome, ocultando a anterior; permite mudar o tipo.
Qual a diferença entre expressão e instrução?::Expressões produzem um valor; instruções executam uma ação e não produzem valor. Um ponto e vírgula transforma uma expressão em instrução.
Para que serve o tipo ()?::É o tipo unit: o valor de retorno de funções que não retornam nada.
O que é um slice?::Uma visão (referência) para uma sequência contígua de elementos, como &[T] ou &str.
Quantos bytes tem um char em Rust?::Quatro: representa um valor escalar Unicode.
Overflow aritmético em debug e em release?::Em debug causa panic; em release faz wrapping, a menos que se use checked_*, wrapping_*, saturating_* ou overflowing_*.

## Veja também

- [[Ownership e regras]]
- [[Borrowing e referências]]
- [[Lifetimes]]
- [[Move, Copy e Clone]]
- [[Flashcards de traits, erros e concorrência]]
