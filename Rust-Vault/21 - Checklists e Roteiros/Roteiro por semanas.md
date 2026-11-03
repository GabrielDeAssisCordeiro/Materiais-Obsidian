---
tags: [rust, anexo, roteiro]
aliases: ["Plano de 12 semanas"]
tipo: roteiro
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Trilha de estudos - Rust]]", "[[Checklist de progresso]]", "[[Como usar este vault - Rust]]", "[[Livros, cursos e comunidades]]"]
---

# Roteiro por semanas

Um plano de **12 semanas** com cerca de **6 a 8 horas por semana** (ex.: 1 hora por dia útil + uma sessão maior no fim de semana).

| Semana | Tema | Leitura | Prática |
|---|---|---|---|
| 1 | Ferramentas e primeiro programa | [[O que é Rust]], [[Instalação com rustup]], [[Primeiro programa Hello World]], [[Cargo básico]] | [[Projeto 1 - Jogo de adivinhação]] (primeira versão) |
| 2 | Básico I | [[Variáveis e mutabilidade]], [[Tipos escalares]], [[Tuplas]], [[Arrays]], [[Operadores]] | Exercícios 1 e 2 de [[Exercícios de fundamentos]] |
| 3 | Básico II | [[Funções]], [[if e else]], [[match]], [[while e for]], [[Strings String vs str]], [[Slices]] | Exercícios 3 a 5 de fundamentos |
| 4 | Ownership | [[Ownership e regras]], [[Move, Copy e Clone]], [[Borrowing e referências]], [[Lifetimes]] | [[Exercícios de ownership]] |
| 5 | Tipos customizados | [[Structs]], [[Enums]], [[Option e Result]], [[Pattern matching avançado]] | [[Exercícios de tipos e pattern matching]] e [[Projeto 2 - CLI de tarefas]] |
| 6 | Módulos, Cargo e coleções | [[Módulos e mod]], [[Cargo.toml e dependências]], [[Vec]], [[HashMap]], [[Escolhendo uma coleção]] | Reorganize o Projeto 2 em módulos |
| 7 | Iteradores, closures e erros | [[Iteradores]], [[Closures]], [[Operador de interrogação]], [[Erros customizados]] | [[Exercícios de coleções e iteradores]] e [[Projeto 3 - Minigrep]] |
| 8 | Traits e genéricos | [[Genéricos]], [[Traits]], [[Trait bounds e where]], [[impl Trait e dyn Trait]] | [[Exercícios de erros, traits e genéricos]] e [[Projeto 4 - Calculadora com parser]] |
| 9 | Memória e concorrência | [[Box]], [[Rc]], [[Arc]], [[Threads]], [[Canais mpsc]], [[Mutex e RwLock]] | [[Exercícios de concorrência]] e [[Projeto 5 - Servidor HTTP com thread pool]] |
| 10 | Async | [[Async e await]], [[Future e Poll]], [[Tokio]], [[join! e select!]] | [[Projeto 7 - Chat assíncrono com Tokio]] |
| 11 | Testes, crates e macros | [[Testes unitários]], [[Clippy]], [[serde e serde_json]], [[axum]], [[macro_rules]] | [[Projeto 6 - API REST com banco de dados]] |
| 12 | Unsafe, avanço e revisão | [[Unsafe Rust]], [[Typestate]], [[Perfilamento]], [[Áreas de Aplicação]] | [[Projeto 8 - Interpretador simples]] e revisão com flashcards |

## Estrutura de cada semana

| Dia | Atividade |
|---|---|
| Seg a qua | ler as notas e **digitar** os exemplos |
| Qui | exercícios da semana (sem olhar o gabarito) |
| Sex | revisar erros e flashcards |
| Sáb/Dom | projeto da semana (2 a 3 horas) |

## Variações do plano

| Ritmo | Como adaptar |
|---|---|
| **Intensivo (4 semanas)** | fazer 3 semanas do plano por semana; pule os projetos 6 e 7 na primeira volta |
| **Tranquilo (24 semanas)** | dobre cada semana; faça todos os exercícios com calma |
| **Quem já programa** | comece em [[Conceitos equivalentes em outras linguagens]] e vá direto à semana 4 |
| **Foco em web** | priorize semanas 7, 8, 10, 11 e [[Backend web com Rust]] |
| **Foco em sistemas/embarcados** | priorize 4, 9, 12 e [[Embarcados e no_std]] |

> [!tip] Ajuste o ritmo à sua realidade
> Uma semana "perdida" não invalida o plano. Consistência importa mais do que velocidade: 30 minutos diários valem mais que 5 horas aos domingos.

## Revisão espaçada

Revise os flashcards em D+1, D+3, D+7 e D+21: [[Flashcards de fundamentos e ownership]], [[Flashcards de traits, erros e concorrência]], [[Flashcards de Cargo, async e avançado]].

## Veja também

- [[Trilha de estudos - Rust]]
- [[Checklist de progresso]]
- [[Como usar este vault - Rust]]
- [[Livros, cursos e comunidades]]
