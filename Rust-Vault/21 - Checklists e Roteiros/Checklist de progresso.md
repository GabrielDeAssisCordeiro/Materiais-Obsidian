---
tags: [rust, anexo, checklist]
aliases: ["Meu progresso", "Autoavaliação"]
tipo: checklist
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Trilha de estudos - Rust]]", "[[Roteiro por semanas]]", "[[Checklist de revisão de código]]", "[[MOC - Exercícios - Rust]]"]
---

# Checklist de progresso

Marque (`- [x]`) o que você consegue fazer **sem consultar**. Se não conseguir, clique no link e revise.

## Nível iniciante

- [ ] Instalo e atualizo o Rust com `rustup` ([[Instalação com rustup]]).
- [ ] Crio, compilo e executo um projeto com Cargo ([[Cargo básico]]).
- [ ] Explico a diferença entre `let` e `let mut` ([[Variáveis e mutabilidade]]).
- [ ] Uso `if`, `match`, `loop`, `while` e `for` ([[match]], [[while e for]]).
- [ ] Diferencio `String` e `&str` ([[Strings String vs str]]).
- [ ] Explico as três regras de ownership ([[Ownership e regras]]).
- [ ] Sei quando um valor é movido, copiado ou clonado ([[Move, Copy e Clone]]).
- [ ] Uso `&` e `&mut` e sei por que o compilador recusa alguns usos ([[Regras do borrow checker]]).
- [ ] Defino `struct` e `enum` com métodos ([[Structs]], [[Enums]]).
- [ ] Uso `Option` e `Result` em vez de `null` e exceções ([[Option e Result]]).
- [ ] Concluí os projetos 1 e 2 ([[Projeto 1 - Jogo de adivinhação]], [[Projeto 2 - CLI de tarefas]]).

## Nível intermediário

- [ ] Organizo código em módulos e uso `pub` ([[Visibilidade e pub]]).
- [ ] Uso `Vec`, `HashMap` e `HashSet` ([[Escolhendo uma coleção]]).
- [ ] Escrevo cadeias de iteradores e closures ([[Iteradores]], [[Closures]]).
- [ ] Propago erros com `?` e crio tipos de erro próprios ([[Erros customizados]]).
- [ ] Escrevo funções genéricas com limites de trait ([[Trait bounds e where]]).
- [ ] Implemento traits e uso `dyn Trait` ([[Traits]], [[impl Trait e dyn Trait]]).
- [ ] Anoto lifetimes quando necessário ([[Lifetimes]]).
- [ ] Escolho entre `Box`, `Rc`, `Arc` e `RefCell` ([[Escolhendo ponteiro inteligente]]).
- [ ] Crio threads e compartilho dados com `Arc<Mutex<T>>` e canais ([[Threads]], [[Canais mpsc]]).
- [ ] Escrevo testes unitários, de integração e doc tests ([[Testes unitários]], [[Doc tests]]).
- [ ] Rodo `cargo clippy` e `cargo fmt` ([[Clippy]], [[rustfmt]]).
- [ ] Concluí os projetos 3 a 5.

## Nível avançado

- [ ] Escrevo código `async` com Tokio e evito bloqueios ([[Tokio]], [[Armadilhas do async]]).
- [ ] Explico `Future`, `Poll` e `Pin` ([[Future e Poll]], [[Pin]]).
- [ ] Escrevo `macro_rules!` simples ([[macro_rules]]).
- [ ] Uso `unsafe` com `// SAFETY:` e abstrações seguras ([[Invariantes e boas práticas de unsafe]]).
- [ ] Integro com C via FFI ([[FFI com C e C++]]).
- [ ] Uso typestate, builder e newtype ([[Typestate]], [[Builder]], [[Newtype]]).
- [ ] Perfilo e otimizo com dados ([[Perfilamento]]).
- [ ] Sigo as API Guidelines em uma biblioteca ([[Rust API Guidelines]]).
- [ ] Concluí os projetos 6 a 8.
- [ ] Publiquei (ou preparei) um crate ([[Checklist para publicar um crate]]).

## Veja também

- [[Trilha de estudos - Rust]]
- [[Roteiro por semanas]]
- [[Checklist de revisão de código]]
- [[MOC - Exercícios - Rust]]
