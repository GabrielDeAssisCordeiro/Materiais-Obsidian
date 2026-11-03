---
tags: [rust, referencia]
aliases: []
tipo: referencia
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[O que é Rust]]", "[[Glossário#Rust]]", "[[Erros comuns de iniciantes]]", "[[Escolhendo e avaliando crates]]", "[[Edições do Rust]]"]
---

# FAQ - Rust

> [!question] Rust é difícil?
> A curva de aprendizado é mais íngreme no início por causa de ownership e borrowing. Depois do "clique", muita gente relata que passa a escrever código mais correto em outras linguagens também. Faça os [[Projeto 1 - Jogo de adivinhação|projetos]] em ordem.

> [!question] Rust é mais rápido que C?
> Está na mesma faixa: ambos compilam para código nativo via LLVM. A vantagem do Rust é entregar esse desempenho **com** segurança de memória. Veja [[Rust vs C, C++, Go, Python e Java]].

> [!question] Rust tem garbage collector?
> Não. A memória é liberada deterministicamente quando o dono sai de escopo ([[Drop e RAII]]).

> [!question] Rust tem exceções? E `null`?
> Não. Erros recuperáveis usam `Result`, ausência usa `Option` ([[Option e Result]]); falhas irrecuperáveis usam [[Panic]].

> [!question] Por que o compilador é tão rígido?
> Porque ele move para tempo de compilação erros que, em outras linguagens, aparecem em produção: use-after-free, data races, ponteiros nulos. Veja [[Regras do borrow checker]].

> [!question] Quando usar `String` e quando `&str`?
> `&str` para **parâmetros** de leitura; `String` quando você precisa ser **dono** ou alterar o texto. Veja [[Strings String vs str]].

> [!question] Quando usar `clone()`?
> Quando você realmente precisa de uma cópia independente. Se for só ler, empreste. Veja [[Erros comuns de iniciantes]].

> [!question] `Box`, `Rc` ou `Arc`?
> `Box` = um dono no heap; `Rc` = vários donos, uma thread; `Arc` = vários donos, várias threads. Veja [[Escolhendo ponteiro inteligente]].

> [!question] `async` ou threads?
> `async` brilha em muitas operações de E/S simultâneas (servidores, clientes de rede); threads para trabalho de CPU e simplicidade. Veja [[Async vs threads]].

> [!question] O que é uma "edição"?
> Um marco de compatibilidade que permite pequenas mudanças de sintaxe sem quebrar código antigo; crates de edições diferentes interoperam. A edição atual deste material é a **2024**. Veja [[Edições do Rust]].

> [!question] Preciso usar `unsafe`?
> Raramente no código de aplicação. Ele aparece em FFI, estruturas de dados de baixo nível e otimizações. Veja [[Unsafe Rust]].

> [!question] Como escolho um crate?
> Veja manutenção, downloads, documentação, licença e dependências: [[Escolhendo e avaliando crates]].

> [!question] Por que meu build é lento?
> Use `cargo check` durante o desenvolvimento, mantenha o perfil `dev` padrão e considere um linker rápido (`mold`/`lld`) e `sccache`. Veja [[Debug vs release]].

> [!question] Como depuro um panic?
> `RUST_BACKTRACE=1 cargo run` mostra a pilha. Use `dbg!()` para inspecionar valores e o depurador (`rust-lldb`/`rust-gdb` ou o da sua IDE). Veja [[Editores e rust-analyzer]].

> [!question] Rust serve para web?
> Sim: backend ([[Backend web com Rust]]), frontend via [[WebAssembly]] e desktop com [[tauri]].

> [!question] Como contribuo com o ecossistema?
> Comece por issues rotuladas `good first issue` em projetos que você usa, e por melhorias de documentação. Veja [[Livros, cursos e comunidades]].

## Veja também

- [[O que é Rust]]
- [[Glossário#Rust]]
- [[Erros comuns de iniciantes]]
- [[Escolhendo e avaliando crates]]
- [[Edições do Rust]]
