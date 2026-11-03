---
tags:
  - tipos
aliases:
  - "Realms"
  - "Security Manager"
  - "Deno"
  - "iframe sandbox"
tipo: tipo-de-sandbox
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Sandbox por WebAssembly]]"
  - "[[Sandbox de Aplicação]]"
---
# Sandbox em Linguagem

Restrições aplicadas pela **linguagem ou runtime**.

| Tecnologia | Situação |
|---|---|
| **Deno** | Permissões explícitas: `--allow-read=./dados`, `--allow-net=api.exemplo.com`; sem flags, sem acesso |
| **iframe `sandbox`** (web) | Atributo restringe scripts, formulários, navegação do conteúdo embutido |
| **Java Security Manager** | Obsoleto e removido nas versões recentes do Java; não use em projetos novos |
| **Node `vm`** | **Não** é mecanismo de segurança, apesar do nome |
| **Realms/ShadowRealm (JS)** | Isolamento de objetos globais; não substitui isolamento de processo |

```bash
deno run --allow-read=./dados script.ts
```

> [!danger] Sandbox em linguagem raramente basta contra código hostil
> Falhas do runtime levam a fugas. Combine com isolamento de processo/VM.

> [!question] Verificar na documentação oficial
> Versões exatas em que o Java Security Manager foi desativado.

## Veja também

- [[Sandbox por WebAssembly]]
- [[Sandbox de Aplicação]]
- [[Caso - Plugins e Extensões]]
- [[MOC - Tipos de Sandbox]]
