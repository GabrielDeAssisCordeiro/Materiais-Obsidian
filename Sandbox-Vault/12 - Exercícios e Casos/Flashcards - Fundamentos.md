---
tags:
  - exercicios
aliases: []
tipo: flashcards
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Glossário#Sandboxes e isolamento]]"
  - "[[Namespaces do Linux]]"
  - "[[Cgroups]]"
---
# Flashcards - Fundamentos

Formato `pergunta::resposta` (compatível com plugins de repetição espaçada, que **não** vêm instalados).

O que é uma sandbox?::Ambiente isolado com acesso restrito ao sistema, que contém falhas e ataques.
Princípio do menor privilégio?::Conceder só as permissões estritamente necessárias, pelo tempo necessário.
Namespaces controlam o quê?::O que o processo **vê** (PIDs, rede, montagens, usuários, etc.).
Cgroups controlam o quê?::Quanto o processo **consome** (CPU, memória, processos, E/S).
Capabilities?::Divisão dos poderes do root em permissões independentes.
Seccomp?::Filtro de chamadas de sistema aceitas pelo kernel para um processo.
Containers compartilham...?::O kernel do host.
`chroot` é fronteira de segurança?::Não.
Diferença entre VM e microVM?::A microVM tem hardware virtual mínimo e boot rápido, mantendo isolamento por hipervisor.
O que o gVisor faz?::Implementa um kernel em espaço de usuário que intercepta syscalls da aplicação.
Wasm: o que um módulo acessa por padrão?::Nada além da própria memória linear; o hospedeiro concede capacidades.
Por que `--privileged` é perigoso?::Concede quase todas as capabilities e acesso a dispositivos, anulando a contenção.

## Veja também

- [[Flashcards - Segurança e Ferramentas]]
- [[MOC - Exercícios e Casos]]
