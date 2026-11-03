---
tags: [rust, anexo, checklist, qualidade]
aliases: ["Code review Rust"]
tipo: checklist
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Clippy]]", "[[rustfmt]]", "[[Rust API Guidelines]]", "[[Boas práticas de tratamento de erros]]", "[[Invariantes e boas práticas de unsafe]]", "[[Checklist de progresso]]"]
---

# Checklist de revisão de código

Use esta lista para revisar seu próprio código (ou de outra pessoa) antes de integrar.

## Automático (rode sempre)

- [ ] `cargo fmt --check` passa ([[rustfmt]]).
- [ ] `cargo clippy --all-targets -- -D warnings` passa ([[Clippy]]).
- [ ] `cargo test` passa, inclusive doc tests ([[cargo test]]).
- [ ] `cargo doc` gera sem avisos ([[cargo doc]]).

## Correção e erros

- [ ] Nenhum `unwrap()`/`expect()` em caminho de produção sem justificativa ([[Boas práticas de tratamento de erros]]).
- [ ] Erros têm contexto suficiente e tipos adequados (biblioteca: [[thiserror e anyhow]]; aplicação: `anyhow`).
- [ ] Casos de borda tratados: vazio, zero, overflow ([[Overflow aritmético]]), texto não ASCII.
- [ ] Sem `panic!` para erros esperados ([[Panic]]).

## Ownership e desempenho

- [ ] Parâmetros usam `&str` e `&[T]` em vez de `String` e `Vec<T>` quando só leem.
- [ ] Sem `clone()` desnecessário ([[Erros comuns de iniciantes]]).
- [ ] Alocações fora de laços quentes; `Vec::with_capacity` quando o tamanho é conhecido ([[Otimização de desempenho]]).
- [ ] Nenhuma otimização sem medição ([[Perfilamento]]).

## API e design

- [ ] Nomes seguem as convenções (`as_`, `to_`, `into_`, `is_`) ([[Rust API Guidelines]]).
- [ ] Tipos públicos implementam as traits comuns (`Debug`, `Clone`, `PartialEq`, `Default`) ([[Traits padrão]]).
- [ ] Campos privados por padrão; `pub` só no necessário ([[Visibilidade e pub]]).
- [ ] Enums públicos que podem crescer usam `#[non_exhaustive]`.
- [ ] Tipos fortes no lugar de primitivos soltos ([[Newtype]]).
- [ ] Documentação com exemplos, `# Errors`, `# Panics` e `# Safety` ([[Doc tests]]).

## Concorrência

- [ ] Nenhum `Mutex` segurado durante `.await` ([[Armadilhas do async]]).
- [ ] Ordem de aquisição de locks consistente (evita deadlock) ([[Mutex e RwLock]]).
- [ ] Atômicos usam o `Ordering` correto, e na dúvida `SeqCst` ([[Atômicos]]).
- [ ] Trabalho bloqueante fora do executor async ([[Async vs threads]]).

## `unsafe`

- [ ] Cada bloco `unsafe` tem `// SAFETY:` e é o menor possível ([[Invariantes e boas práticas de unsafe]]).
- [ ] Testes passam sob Miri ([[Miri]]).

## Veja também

- [[Clippy]]
- [[rustfmt]]
- [[Rust API Guidelines]]
- [[Boas práticas de tratamento de erros]]
- [[Invariantes e boas práticas de unsafe]]
- [[Checklist de progresso]]
