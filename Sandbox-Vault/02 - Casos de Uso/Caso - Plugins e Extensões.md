---
tags:
  - casos-de-uso
aliases:
  - "Extensões isoladas"
  - "Plugin sandbox"
tipo: caso-de-uso
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Sandbox por WebAssembly]]"
  - "[[Sandbox em Linguagem]]"
---
# Caso - Plugins e Extensões

Editores, navegadores, CMS e plataformas SaaS permitem extensões de terceiros. Uma extensão não deve ler dados de outra nem do sistema.

Abordagens: processos separados com permissões declaradas (manifest), WebAssembly com capacidades explícitas, *realms*/iframes com `sandbox`, e execução remota isolada.

> [!info] Modelo de permissões declaradas
> O usuário/administrador aprova o que a extensão pode acessar (rede, arquivos, API). Quanto mais granular, melhor.

## Exercício

Desenhe o manifesto de permissões de uma extensão fictícia de editor de texto.

## Veja também

- [[Sandbox por WebAssembly]]
- [[Sandbox em Linguagem]]
- [[Sandbox de Aplicação]]
- [[MOC - Casos de Uso]]
