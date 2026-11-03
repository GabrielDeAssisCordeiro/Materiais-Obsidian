---
titulo: "Checklist de Revisão de Código - Cpp"
tags: [cpp, anexos, checklist, qualidade]
aliases: ["Checklist de code review"]
tipo: checklist
nivel: intermediario
padrao: C++20
criado: 2026-10-24
relacionados: ["[[Core Guidelines]]", "[[MOC - Checklists e Roteiros - Cpp]]", "[[Catálogo de Armadilhas e UB]]"]
---

# Checklist de Revisão de Código - Cpp

Use em *pull requests* e ao revisar o próprio código. Referência de regras: [[Core Guidelines]].

## Recursos e posse

- [ ] Nenhum `new`/`delete` ou `malloc`/`free` manual (use [[unique_ptr]], contêineres, [[RAII]])
- [ ] `shared_ptr` só com posse realmente compartilhada; sem ciclos ([[Ciclos de Referência]])
- [ ] Ponteiros crus são apenas observadores, nunca donos
- [ ] Classes que gerenciam recurso seguem a [[Regra do 0, 3 e 5]]
- [ ] Destrutor `virtual` em bases polimórficas

## Segurança e UB

- [ ] Variáveis inicializadas; sem leitura de moved-from
- [ ] Índices e tamanhos validados; `span`/`at()` onde cabe ([[span]])
- [ ] Sem referências ou `string_view` para temporários ([[string_view]])
- [ ] Sem overflow de inteiro com sinal; conversões explícitas e justificadas ([[Conversões e Casts]])
- [ ] Compila sem avisos com `-Wall -Wextra -Wpedantic` e roda limpo com [[Sanitizers]]

## API e design

- [ ] Parâmetros: `const&` para leitura de objetos grandes, valor para pequenos/cópias necessárias, `&&` só quando faz sentido ([[Referências Universais e Perfect Forwarding]])
- [ ] Funções curtas, nomes claros; `const` e `noexcept` onde corretos ([[noexcept e Movimento]])
- [ ] `explicit` em construtores de um argumento ([[Conversões Implícitas e explicit]])
- [ ] Erros tratados de forma consistente ([[Segurança de Exceções]], [[Tratamento de Erros com expected]])
- [ ] `[[nodiscard]]` em funções cujo retorno não deve ser ignorado

## Concorrência

- [ ] Todo dado compartilhado mutável protegido ([[Mutex e Locks]], [[Atomics e Modelo de Memória]])
- [ ] Ordem fixa de travas; nenhum lock mantido durante chamadas desconhecidas ([[Data Races e Deadlocks]])
- [ ] Threads sempre unidas (`jthread`) e cancelamento cooperativo ([[stop_token e Cancelamento]])

## Build e testes

- [ ] Includes mínimos e no lugar certo ([[Headers vs Sources]]); sem `using namespace` em headers
- [ ] Testes novos cobrem o caso feliz e os de borda ([[Fundamentos de Testes Unitários]])
- [ ] Formatação automática aplicada ([[clang-format]]); análise estática limpa ([[clang-tidy e cppcheck]])

## Veja também

- [[Core Guidelines]]
- [[Catálogo de Armadilhas e UB]]
- [[Checklist de Novo Projeto - Cpp]]
- [[MOC - Checklists e Roteiros - Cpp]]

## Exercício

Aplique esta lista a um dos [[MOC - Projetos - Cpp|projetos]] do vault e registre 5 melhorias possíveis.
