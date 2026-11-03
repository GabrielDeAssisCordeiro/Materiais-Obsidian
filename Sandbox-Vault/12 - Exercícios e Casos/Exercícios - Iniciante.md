---
tags:
  - exercicios
aliases: []
tipo: exercicio
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Criar Sandbox com Docker]]"
  - "[[Criar Sandbox com Windows Sandbox]]"
  - "[[Princípio do Menor Privilégio]]"
---
# Exercícios - Iniciante

Todos os exercícios devem ser feitos em **ambiente de laboratório**, com arquivos e dados fictícios.

1. **Mapa de sandboxes do cotidiano:** liste 5 sandboxes que você usa (navegador, apps do celular, etc.).
2. **Container restrito:** rode `docker run --rm --network none --read-only alpine:3 sh -c 'touch /x; ping -c1 8.8.8.8'` e explique cada erro.
3. **Windows Sandbox/VM:** abra um arquivo de texto inofensivo sem rede nem pasta compartilhada gravável.
4. **Tabela:** preencha de memória a tabela de [[Sandbox vs VM vs Container vs Jail vs chroot]] e confira.
5. **Menor privilégio:** reduza as permissões de um script seu ao mínimo e documente.

## Veja também

- [[Exercícios - Intermediário]]
- [[Flashcards - Fundamentos]]
- [[MOC - Exercícios e Casos]]
