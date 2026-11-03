---
tags: [rust, flashcards, cargo, async, avancado]
aliases: ["Flashcards 3"]
tipo: flashcards
nivel: avancado
criado: 2026-10-24
relacionados: ["[[Cargo básico]]", "[[Async e await]]", "[[Unsafe Rust]]", "[[Typestate]]", "[[Flashcards de fundamentos e ownership]]"]
---

# Flashcards de Cargo, async e avançado

Cartões sobre ferramentas, async, unsafe e técnicas avançadas. Veja [[Cheat sheet de Cargo]], [[Async e await]] e [[Unsafe Rust]].

> [!tip] Como usar
> Leia a pergunta, responda mentalmente e confira. Para repetição espaçada, qualquer plugin de flashcards que aceite o formato `pergunta::resposta` (linha única) funciona; sem plugin, as notas continuam legíveis.

Para que serve o Cargo.lock?::Fixa as versões exatas das dependências para builds reprodutíveis; deve ser versionado em binários.
cargo check versus cargo build?::check só valida o código (rápido) e não gera o binário final.
O que é uma feature de Cargo?::Uma flag opcional que habilita código e dependências adicionais de um crate.
O que é um workspace?::Um conjunto de crates que compartilham Cargo.lock e a pasta target.
O que é uma edição (edition)?::Um marco de compatibilidade (2015, 2018, 2021, 2024) que habilita mudanças de sintaxe sem quebrar crates antigos.
O que significa ^1.2.3 em Cargo.toml?::Qualquer versão compatível: maior ou igual a 1.2.3 e menor que 2.0.0.
Para que serve o build.rs?::Um script executado antes da compilação, por exemplo para gerar código ou compilar bibliotecas C.
O que é uma Future?::Um valor que representa uma computação assíncrona que será concluída; só avança quando consultada (poll).
async fn executa algo ao ser chamada?::Não: retorna uma Future preguiçosa que só roda ao ser aguardada (await) ou executada por um executor.
Por que Rust não traz um runtime async na std?::Para deixar a escolha (Tokio, async-std, smol...) ao desenvolvedor e manter a std enxuta.
Quando usar tokio spawn?::Para executar uma tarefa assíncrona concorrentemente; a future precisa ser Send e 'static.
Por que não segurar um std Mutex através de um await?::Pode causar deadlocks e impede a future de ser Send; use tokio Mutex ou reduza o escopo do guard.
O que o bloco unsafe permite?::Desreferenciar ponteiros crus, chamar funções unsafe, acessar static mut, implementar traits unsafe e acessar campos de union.
unsafe desliga o borrow checker?::Não; apenas libera cinco operações. O restante continua verificado.
O que o Miri faz?::Interpreta o programa e detecta comportamento indefinido em código unsafe.
O que é repr(C)?::Atributo que garante o layout de memória compatível com C.
O que é PhantomData?::Tipo de tamanho zero que marca que uma struct se comporta como se contivesse um T, sem armazená-lo.
O que é o padrão typestate?::Codificar o estado de um objeto no tipo, de modo que operações inválidas não compilem.
O que é um newtype?::Uma struct de tupla com um campo que cria um tipo distinto sem custo em execução.
O que são zero-cost abstractions?::Abstrações que não custam mais do que o código escrito à mão equivalente; monomorfização e inlining são exemplos.
Qual a primeira regra de otimização?::Meça antes: use benchmarks e profilers para achar o gargalo real.
O que faz lto = "fat"?::Otimização em tempo de link entre todos os crates, ao custo de compilação mais lenta.

## Veja também

- [[Cargo básico]]
- [[Async e await]]
- [[Unsafe Rust]]
- [[Typestate]]
- [[Flashcards de fundamentos e ownership]]
