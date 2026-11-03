---
titulo: "Checklist de desempenho e segurança"
tags: [cpp, anexos, checklist, desempenho, seguranca]
aliases: ["Checklist de performance", "Checklist de hardening"]
tipo: checklist
nivel: avancado
padrao: C++20
criado: 2026-10-24
relacionados: ["[[Profiling e Benchmarking]]", "[[Segurança e Hardening]]", "[[MOC - Checklists e Roteiros - Cpp]]"]
---

# Checklist de desempenho e segurança

## Desempenho

- [ ] **Meça antes** de otimizar ([[Profiling e Benchmarking]], [[Google Benchmark]])
- [ ] Compilado em `-O2`/`-O3` sem sanitizers para medir; considere [[Otimizações do Compilador LTO e PGO]]
- [ ] Algoritmo e estrutura de dados adequados ([[Escolhendo um Contêiner]])
- [ ] Localidade de dados avaliada ([[Cache e Localidade de Dados]]); `reserve` em vetores
- [ ] Sem cópias desnecessárias: movimento, `const&`, `string_view` ([[Semântica de Movimento]])
- [ ] Alocações no caminho quente reduzidas ([[Alocadores e pmr]])
- [ ] Concorrência sem *false sharing* nem contenção excessiva ([[False Sharing]])
- [ ] Vetorização verificada quando relevante ([[SIMD e Vetorização - Cpp]])

## Segurança

- [ ] Biblioteca padrão em modo reforçado/hardened (`_GLIBCXX_ASSERTIONS`, `_LIBCPP_HARDENING_MODE`) ([[Segurança e Hardening]])
- [ ] Flags de mitigação: `-fstack-protector-strong`, `-D_FORTIFY_SOURCE=2`, PIE, RELRO
- [ ] Entradas externas validadas; tamanhos e limites checados
- [ ] Sem funções inseguras (`strcpy`, `sprintf`, `gets`); use `std::string`, `snprintf`/`std::format`
- [ ] [[Fuzzing]] nos parsers e interfaces de entrada
- [ ] Dependências atualizadas e auditadas
- [ ] Revisão contra [[Catálogo de Armadilhas e UB]]
- [ ] Considerar [[Safety Profiles e Memória Segura]] e tipos seguros (`span`, `optional`)

> [!warning] Medir não é opcional
> Otimizações sem medição costumam piorar a legibilidade sem ganho real.

## Veja também

- [[Profiling e Benchmarking]]
- [[Segurança e Hardening]]
- [[Checklist de Revisão de Código - Cpp]]
- [[Checklist de Novo Projeto - Cpp]]
- [[MOC - Checklists e Roteiros - Cpp]]

## Exercício

Escolha um dos [[MOC - Projetos - Cpp|projetos]], meça o ponto mais lento com um profiler e aplique **uma** otimização, registrando o antes e depois.
