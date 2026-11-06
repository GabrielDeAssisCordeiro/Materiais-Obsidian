---
tags: [rust, inicio, indice]
aliases: []
tipo: indice
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Home - Rust]]", "[[Trilha de aprendizado - Rust]]"]
---

# Índice - Rust

Todas as notas do material, por pasta e em ordem alfabética. Para navegar por tema, comece pelos MOCs na [[Home - Rust]].

## Por pasta

### 01 - Fundamentos

[[MOC - Fundamentos - Rust]]

- [[O que é Rust]]
- [[Filosofia do Rust]]
- [[História do Rust]]
- [[Casos de uso do Rust]]
- [[Rust vs C, C++, Go, Python e Java]]
- [[Instalação com rustup]]
- [[Toolchains stable beta nightly]]
- [[Editores e rust-analyzer]]
- [[Primeiro programa Hello World]]
- [[Cargo básico]]
- [[Pipeline de compilação]]
- [[Edições do Rust]]

### 02 - Básico da Linguagem

[[MOC - Básico da Linguagem]]

- [[Variáveis e mutabilidade]]
- [[Shadowing]]
- [[Constantes e statics]]
- [[Tipos escalares]]
- [[Tuplas]]
- [[Arrays]]
- [[Slices]]
- [[Strings String vs str]]
- [[Operadores]]
- [[Comentários e doc comments]]
- [[Funções]]
- [[Expressões vs instruções]]
- [[if e else]]
- [[loop e break]]
- [[while e for]]
- [[match]]
- [[if let e let else]]
- [[while let]]
- [[Ranges]]
- [[Entrada e saída no console]]
- [[Macros básicas]]
- [[Conversão entre tipos]]
- [[Overflow aritmético]]
- [[Formatação com println]]

### 03 - Ownership e Lifetimes

[[MOC - Ownership e Lifetimes]]

- [[Ownership e regras]]
- [[Move, Copy e Clone]]
- [[Borrowing e referências]]
- [[Regras do borrow checker]]
- [[NLL]]
- [[Lifetimes]]
- [[Elisão de lifetimes]]
- [[Lifetimes em structs]]
- [[Lifetime static]]
- [[Erros comuns do borrow checker]]

### 04 - Tipos Customizados

[[MOC - Tipos Customizados]]

- [[Structs]]
- [[Structs tupla e unit]]
- [[Métodos e funções associadas]]
- [[Enums]]
- [[Option e Result]]
- [[Combinadores de Option e Result]]
- [[Pattern matching avançado]]
- [[Desestruturação]]
- [[Estruturas aninhadas e modelagem]]

### 05 - Módulos e Cargo

[[MOC - Módulos e Cargo]]

- [[Packages, crates e módulos]]
- [[Módulos e mod]]
- [[Visibilidade e pub]]
- [[use e caminhos]]
- [[Re-exports com pub use]]
- [[Estrutura de projetos binário e biblioteca]]
- [[Workspaces - Rust]]
- [[Features de Cargo]]
- [[Cargo.toml e dependências]]
- [[Versionamento semântico]]
- [[Debug vs release]]
- [[Comandos úteis do Cargo]]
- [[Publicar no crates.io]]
- [[Targets e cross-compilation]]
- [[build.rs]]

### 06 - Coleções e Iteradores

[[MOC - Coleções e Iteradores]]

- [[Vec]]
- [[HashMap]]
- [[HashSet]]
- [[BTreeMap]]
- [[VecDeque]]
- [[BinaryHeap]]
- [[Escolhendo uma coleção]]
- [[Iteradores]]
- [[Adaptadores de iterador]]
- [[Consumidores de iterador]]
- [[Closures]]
- [[Fn, FnMut e FnOnce]]
- [[Zero-cost abstractions]]
- [[Implementando Iterator]]
- [[Ordenação e busca]]

### 07 - Erros

[[MOC - Erros]]

- [[Panic]]
- [[Operador de interrogação]]
- [[Erros customizados]]
- [[Conversão de erros com From]]
- [[Box dyn Error]]
- [[thiserror e anyhow]]
- [[Boas práticas de tratamento de erros]]

### 08 - Traits e Genéricos

[[MOC - Traits e Genéricos]]

- [[Genéricos]]
- [[Traits]]
- [[Trait bounds e where]]
- [[impl Trait e dyn Trait]]
- [[Traits padrão]]
- [[derive]]
- [[From e Into]]
- [[Default]]
- [[Deref e AsRef]]
- [[Tipos associados]]
- [[Supertraits]]
- [[Object safety]]
- [[Sobrecarga de operadores]]
- [[Orphan rule]]

### 09 - Memória e Ponteiros

[[MOC - Memória e Ponteiros]]

- [[Stack, heap e layout de memória]]
- [[Box]]
- [[Rc]]
- [[Arc]]
- [[Cell e RefCell]]
- [[Weak e ciclos de referência]]
- [[Drop e RAII]]
- [[Escolhendo ponteiro inteligente]]

### 10 - Concorrência

[[MOC - Concorrência]]

- [[Concorrência sem medo]]
- [[Threads]]
- [[Canais mpsc]]
- [[Mutex e RwLock]]
- [[Send e Sync]]
- [[Atômicos]]
- [[Data races]]
- [[Condvar e Barrier]]
- [[Rayon]]
- [[Crossbeam]]

### 11 - Async

[[MOC - Async]]

- [[Async e await]]
- [[Future e Poll]]
- [[Pin]]
- [[Executores e runtimes]]
- [[Tokio]]
- [[join! e select!]]
- [[Canais assíncronos]]
- [[Streams]]
- [[Armadilhas do async]]
- [[Async vs threads]]

### 12 - Testes e Qualidade

[[MOC - Testes e Qualidade]]

- [[Testes unitários]]
- [[Testes de integração]]
- [[Doc tests]]
- [[cargo test]]
- [[Mocks e injeção de dependência]]
- [[Property-based testing com proptest]]
- [[Benchmarks com criterion]]
- [[Cobertura de testes]]
- [[Clippy]]
- [[rustfmt]]
- [[cargo doc]]
- [[CI com GitHub Actions]]

### 13 - Crates

[[MOC - Crates]]

- [[Escolhendo e avaliando crates]]
- [[serde e serde_json]]
- [[clap]]
- [[reqwest]]
- [[axum]]
- [[actix-web]]
- [[sqlx e diesel]]
- [[tracing]]
- [[rand]]
- [[chrono e time]]
- [[regex]]
- [[itertools]]
- [[LazyLock e OnceLock]]
- [[bevy]]
- [[tauri]]
- [[ratatui]]
- [[Outros crates úteis]]

### 14 - Macros

[[MOC - Macros]]

- [[macro_rules]]
- [[Macros procedurais]]
- [[syn e quote]]
- [[Quando usar e evitar macros]]

### 15 - Unsafe e FFI

[[MOC - Unsafe e FFI]]

- [[Unsafe Rust]]
- [[Raw pointers]]
- [[Traits unsafe]]
- [[FFI com C e C++]]
- [[bindgen e cbindgen]]
- [[cxx e PyO3]]
- [[Miri]]
- [[Invariantes e boas práticas de unsafe]]

### 16 - Áreas de Aplicação

[[MOC - Áreas de Aplicação]]

- [[Áreas de Aplicação]]
- [[CLI com Rust]]
- [[Backend web com Rust]]
- [[WebAssembly]]
- [[Embarcados e no_std]]
- [[Sistemas operacionais em Rust]]
- [[Jogos com Rust]]
- [[Ciência de dados com Rust]]
- [[Blockchain com Rust]]
- [[Infraestrutura e DevOps com Rust]]

### 17 - Avançado e Performance

[[MOC - Avançado e Performance]]

- [[PhantomData]]
- [[Newtype]]
- [[Typestate]]
- [[Builder]]
- [[Const generics]]
- [[GATs]]
- [[Traits avançadas]]
- [[Perfilamento]]
- [[Otimização de desempenho]]
- [[Release profile LTO e codegen]]
- [[SIMD e vetorização]]
- [[Alocadores e memória]]
- [[Rust API Guidelines]]

### 18 - Projetos

[[MOC - Projetos - Rust]]

- [[Projeto 1 - Jogo de adivinhação]]
- [[Projeto 2 - CLI de tarefas]]
- [[Projeto 3 - Minigrep]]
- [[Projeto 4 - Calculadora com parser]]
- [[Projeto 5 - Servidor HTTP com thread pool]]
- [[Projeto 6 - API REST com banco de dados]]
- [[Projeto 7 - Chat assíncrono com Tokio]]
- [[Projeto 8 - Interpretador simples]]

### 19 - Referência

[[MOC - Referência - Rust]]

- [[Glossário#Rust]]
- [[Cheat sheet de sintaxe]]
- [[Cheat sheet de ownership]]
- [[Cheat sheet de traits]]
- [[Cheat sheet de iteradores]]
- [[Cheat sheet de Cargo]]
- [[Tabela de erros do compilador]]
- [[Erros comuns de iniciantes]]
- [[FAQ - Rust]]
- [[Conceitos equivalentes em outras linguagens]]
- [[Livros, cursos e comunidades]]

### 20 - Exercícios

[[MOC - Exercícios - Rust]]

- [[Exercícios de fundamentos]]
- [[Exercícios de ownership]]
- [[Exercícios de tipos e pattern matching]]
- [[Exercícios de coleções e iteradores]]
- [[Exercícios de erros, traits e genéricos]]
- [[Exercícios de concorrência]]
- [[Flashcards de fundamentos e ownership]]
- [[Flashcards de traits, erros e concorrência]]
- [[Flashcards de Cargo, async e avançado]]

### 21 - Checklists e Roteiros

[[MOC - Checklists e Roteiros]]

- [[Roteiro por semanas]]
- [[Checklist de progresso]]
- [[Checklist de revisão de código]]
- [[Checklist para publicar um crate]]
- [[Checklist de novo projeto]]

### Templates

[[MOC - Templates]]

- [[Template de nota de conceito]]
- [[Template de exercício]]
- [[Template de projeto]]
- [[Template de flashcards]]
- [[Template de revisão semanal]]

### 00 - Início

- [[Trilha de aprendizado - Rust]]

## Ordem alfabética

**A** — [[actix-web]] · [[Adaptadores de iterador]] · [[Alocadores e memória]] · [[Arc]] · [[Armadilhas do async]] · [[Arrays]] · [[Async e await]] · [[Async vs threads]] · [[Atômicos]] · [[axum]] · [[Áreas de Aplicação]]

**B** — [[Backend web com Rust]] · [[Benchmarks com criterion]] · [[bevy]] · [[BinaryHeap]] · [[bindgen e cbindgen]] · [[Blockchain com Rust]] · [[Boas práticas de tratamento de erros]] · [[Borrowing e referências]] · [[Box]] · [[Box dyn Error]] · [[BTreeMap]] · [[build.rs]] · [[Builder]]

**C** — [[Canais assíncronos]] · [[Canais mpsc]] · [[Cargo básico]] · [[cargo doc]] · [[cargo test]] · [[Cargo.toml e dependências]] · [[Casos de uso do Rust]] · [[Cell e RefCell]] · [[Cheat sheet de Cargo]] · [[Cheat sheet de iteradores]] · [[Cheat sheet de ownership]] · [[Cheat sheet de sintaxe]] · [[Cheat sheet de traits]] · [[Checklist de novo projeto]] · [[Checklist de progresso]] · [[Checklist de revisão de código]] · [[Checklist para publicar um crate]] · [[chrono e time]] · [[CI com GitHub Actions]] · [[Ciência de dados com Rust]] · [[clap]] · [[CLI com Rust]] · [[Clippy]] · [[Closures]] · [[Cobertura de testes]] · [[Comandos úteis do Cargo]] · [[Combinadores de Option e Result]] · [[Comentários e doc comments]] · [[Conceitos equivalentes em outras linguagens]] · [[Concorrência sem medo]] · [[Condvar e Barrier]] · [[Const generics]] · [[Constantes e statics]] · [[Consumidores de iterador]] · [[Conversão de erros com From]] · [[Conversão entre tipos]] · [[Crossbeam]] · [[cxx e PyO3]]

**D** — [[Data races]] · [[Debug vs release]] · [[Default]] · [[Deref e AsRef]] · [[derive]] · [[Desestruturação]] · [[Doc tests]] · [[Drop e RAII]]

**E** — [[Editores e rust-analyzer]] · [[Edições do Rust]] · [[Elisão de lifetimes]] · [[Embarcados e no_std]] · [[Entrada e saída no console]] · [[Enums]] · [[Erros comuns de iniciantes]] · [[Erros comuns do borrow checker]] · [[Erros customizados]] · [[Escolhendo e avaliando crates]] · [[Escolhendo ponteiro inteligente]] · [[Escolhendo uma coleção]] · [[Estrutura de projetos binário e biblioteca]] · [[Estruturas aninhadas e modelagem]] · [[Executores e runtimes]] · [[Exercícios de coleções e iteradores]] · [[Exercícios de concorrência]] · [[Exercícios de erros, traits e genéricos]] · [[Exercícios de fundamentos]] · [[Exercícios de ownership]] · [[Exercícios de tipos e pattern matching]] · [[Expressões vs instruções]]

**F** — [[FAQ - Rust]] · [[Features de Cargo]] · [[FFI com C e C++]] · [[Filosofia do Rust]] · [[Flashcards de Cargo, async e avançado]] · [[Flashcards de fundamentos e ownership]] · [[Flashcards de traits, erros e concorrência]] · [[Fn, FnMut e FnOnce]] · [[Formatação com println]] · [[From e Into]] · [[Funções]] · [[Future e Poll]]

**G** — [[GATs]] · [[Genéricos]] · [[Glossário#Rust]]

**H** — [[HashMap]] · [[HashSet]] · [[História do Rust]]

**I** — [[if e else]] · [[if let e let else]] · [[impl Trait e dyn Trait]] · [[Implementando Iterator]] · [[Infraestrutura e DevOps com Rust]] · [[Instalação com rustup]] · [[Invariantes e boas práticas de unsafe]] · [[Iteradores]] · [[itertools]]

**J** — [[Jogos com Rust]] · [[join! e select!]]

**L** — [[LazyLock e OnceLock]] · [[Lifetime static]] · [[Lifetimes]] · [[Lifetimes em structs]] · [[Livros, cursos e comunidades]] · [[loop e break]]

**M** — [[macro_rules]] · [[Macros básicas]] · [[Macros procedurais]] · [[match]] · [[Miri]] · [[Mocks e injeção de dependência]] · [[Move, Copy e Clone]] · [[Mutex e RwLock]] · [[Métodos e funções associadas]] · [[Módulos e mod]]

**N** — [[Newtype]] · [[NLL]]

**O** — [[O que é Rust]] · [[Object safety]] · [[Operador de interrogação]] · [[Operadores]] · [[Option e Result]] · [[Ordenação e busca]] · [[Orphan rule]] · [[Otimização de desempenho]] · [[Outros crates úteis]] · [[Overflow aritmético]] · [[Ownership e regras]]

**P** — [[Packages, crates e módulos]] · [[Panic]] · [[Pattern matching avançado]] · [[Perfilamento]] · [[PhantomData]] · [[Pin]] · [[Pipeline de compilação]] · [[Primeiro programa Hello World]] · [[Projeto 1 - Jogo de adivinhação]] · [[Projeto 2 - CLI de tarefas]] · [[Projeto 3 - Minigrep]] · [[Projeto 4 - Calculadora com parser]] · [[Projeto 5 - Servidor HTTP com thread pool]] · [[Projeto 6 - API REST com banco de dados]] · [[Projeto 7 - Chat assíncrono com Tokio]] · [[Projeto 8 - Interpretador simples]] · [[Property-based testing com proptest]] · [[Publicar no crates.io]]

**Q** — [[Quando usar e evitar macros]]

**R** — [[rand]] · [[Ranges]] · [[ratatui]] · [[Raw pointers]] · [[Rayon]] · [[Rc]] · [[Re-exports com pub use]] · [[regex]] · [[Regras do borrow checker]] · [[Release profile LTO e codegen]] · [[reqwest]] · [[Roteiro por semanas]] · [[Rust API Guidelines]] · [[Rust vs C, C++, Go, Python e Java]] · [[rustfmt]]

**S** — [[Send e Sync]] · [[serde e serde_json]] · [[Shadowing]] · [[SIMD e vetorização]] · [[Sistemas operacionais em Rust]] · [[Slices]] · [[Sobrecarga de operadores]] · [[sqlx e diesel]] · [[Stack, heap e layout de memória]] · [[Streams]] · [[Strings String vs str]] · [[Structs]] · [[Structs tupla e unit]] · [[Supertraits]] · [[syn e quote]]

**T** — [[Tabela de erros do compilador]] · [[Targets e cross-compilation]] · [[tauri]] · [[Template de exercício]] · [[Template de flashcards]] · [[Template de nota de conceito]] · [[Template de projeto]] · [[Template de revisão semanal]] · [[Testes de integração]] · [[Testes unitários]] · [[thiserror e anyhow]] · [[Threads]] · [[Tipos associados]] · [[Tipos escalares]] · [[Tokio]] · [[Toolchains stable beta nightly]] · [[tracing]] · [[Trait bounds e where]] · [[Traits]] · [[Traits avançadas]] · [[Traits padrão]] · [[Traits unsafe]] · [[Trilha de aprendizado - Rust]] · [[Tuplas]] · [[Typestate]]

**U** — [[Unsafe Rust]] · [[use e caminhos]]

**V** — [[Variáveis e mutabilidade]] · [[Vec]] · [[VecDeque]] · [[Versionamento semântico]] · [[Visibilidade e pub]]

**W** — [[Weak e ciclos de referência]] · [[WebAssembly]] · [[while e for]] · [[while let]] · [[Workspaces - Rust]]

**Z** — [[Zero-cost abstractions]]

## Canvases

- [[Mapa do Ownership.canvas]]
- [[Trilha de Aprendizado em Rust.canvas]]
- [[Mapa de Traits e Genéricos.canvas]]

## Veja também

- [[Home - Rust]]
- [[Trilha de aprendizado - Rust]]
