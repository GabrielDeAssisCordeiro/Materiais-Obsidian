---
tags: [rust, flashcards, traits, erros, concorrencia]
aliases: ["Flashcards 2"]
tipo: flashcards
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Traits]]", "[[Option e Result]]", "[[Threads]]", "[[Send e Sync]]", "[[Flashcards de Cargo, async e avançado]]"]
---

# Flashcards de traits, erros e concorrência

Cartões sobre abstrações, tratamento de erros e programação concorrente. Veja [[Traits]], [[Erros customizados]] e [[Concorrência sem medo]].

> [!tip] Como usar
> Leia a pergunta, responda mentalmente e confira. Para repetição espaçada, qualquer plugin de flashcards que aceite o formato `pergunta::resposta` (linha única) funciona; sem plugin, as notas continuam legíveis.

O que é uma trait?::Um conjunto de métodos que tipos podem implementar, definindo comportamento compartilhado.
Diferença entre impl Trait e dyn Trait?::impl Trait usa despacho estático (monomorfização); dyn Trait usa despacho dinâmico via vtable.
O que é a orphan rule?::Você só pode implementar uma trait para um tipo se a trait ou o tipo for definido no seu crate.
Como contornar a orphan rule?::Com o padrão newtype: embrulhe o tipo externo em uma struct local.
O que é uma trait object-safe (dyn compatible)?::Uma trait cujos métodos podem ser chamados via dyn: sem métodos genéricos nem retorno Self (exceto com where Self: Sized).
O que derive faz?::Gera automaticamente implementações de traits como Debug, Clone, PartialEq, Hash e Default.
Debug versus Display?::Debug ({:?}) é para programadores e pode ser derivado; Display ({}) é para usuários finais e é implementado manualmente.
O que o operador ? faz?::Em Err ou None retorna cedo da função (convertendo o erro via From); em Ok ou Some extrai o valor.
Quando usar panic!?::Para erros de programação e invariantes violadas; erros esperados devem usar Result.
thiserror versus anyhow?::thiserror define tipos de erro para bibliotecas; anyhow oferece um erro dinâmico conveniente para aplicações.
O que é Option?::Um enum com Some(T) ou None que representa a possível ausência de valor, substituindo null.
O que é um tipo associado?::Um tipo declarado dentro de uma trait e escolhido por quem a implementa, como Item em Iterator.
Por que iteradores são chamados de preguiçosos?::Porque adaptadores como map e filter nada fazem até que um consumidor (collect, sum, for) peça os itens.
O que significa Fn, FnMut e FnOnce?::Closures que só leem o ambiente, que o modificam ou que o consomem (podem ser chamadas apenas uma vez).
Rc versus Arc?::Rc é um contador de referências para uma thread; Arc usa contagem atômica e pode ser compartilhado entre threads.
Para que serve RefCell?::Mutabilidade interior verificada em tempo de execução: o borrow checker é aplicado dinamicamente.
Como evitar ciclos de Rc?::Usando Weak para as referências que apontam de volta.
O que são Send e Sync?::Send: o valor pode ser movido para outra thread. Sync: &T pode ser compartilhado entre threads.
Por que Rc não é Send?::Porque sua contagem de referências não é atômica; duas threads poderiam corrompê-la.
Mutex versus RwLock?::Mutex dá acesso exclusivo; RwLock permite vários leitores ou um escritor.
O que é um data race e Rust o permite?::Acesso concorrente sem sincronização com ao menos uma escrita; em Rust seguro é impossível pelo sistema de tipos.
Como encerrar um canal mpsc corretamente?::Descartando todos os transmissores (drop), o que faz o receptor terminar a iteração.
O que thread scope permite?::Criar threads que emprestam dados locais, pois todas terminam antes de o escopo acabar.

## Veja também

- [[Traits]]
- [[Option e Result]]
- [[Threads]]
- [[Send e Sync]]
- [[Flashcards de Cargo, async e avançado]]
