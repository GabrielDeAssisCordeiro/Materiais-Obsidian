---
tags: [rust, inicio, guia]
aliases: ["Começando", "Como estudar com este vault"]
tipo: guia
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Trilha de estudos - Rust]]", "[[Roteiro por semanas]]", "[[Livros, cursos e comunidades]]", "[[Template de nota de conceito]]"]
---

# Como usar este vault - Rust

## O que é este vault

Um material de estudos de **Rust** (edição 2024, Rust 1.99) em português do Brasil, organizado como um *vault* do Obsidian: notas curtas e atômicas, ligadas por `[[links]]`, com mapas de conteúdo (**MOCs**) por tema.

## Estrutura

```text
00 - Início/        Home, trilha de estudos, índice geral
01 a 17 /           conteúdo por tema (cada pasta tem um "MOC")
18 - Projetos/      8 projetos guiados completos
19 - Referência/    cheat sheets, erros do compilador, FAQ
20 - Exercícios/    listas com gabarito e flashcards
21 - Checklists e Roteiros/   roteiro semanal e checklists
```

Os canvases ficam em `Anexos/` e os modelos de nota em `Templates/`, ambas na raiz do vault (veja [[MOC - Anexos]] e [[MOC - Templates]]). O glossário do Rust está em [[Glossário#Rust]].

## Como abrir

1. Descompacte o `.zip`.
2. No Obsidian: **Abrir pasta como cofre (vault)** e escolha a pasta `Materiais-Obsidian`. Este material fica na subpasta `Rust-Vault` (veja o [[README]]).
3. Abra [[Home - Rust]].

> [!info] Sem plugins da comunidade
> O vault usa apenas **plugins nativos** (já ativados): Backlinks, Graph view, Canvas, Templates, Outline, Properties e outros. Nada para instalar.

## Como estudar

1. Siga a [[Trilha de estudos - Rust]] (ou o [[Roteiro por semanas]] se preferir um calendário).
2. Ao final de cada tema, faça os [[MOC - Exercícios - Rust|exercícios]] correspondentes.
3. Programe os [[MOC - Projetos - Rust|projetos]]: **digite o código, não cole**.
4. Revise com os flashcards: [[Flashcards de fundamentos e ownership]].
5. Use [[Checklist de progresso]] para marcar o que já dominou.

## Dicas de Obsidian

| Recurso | Como usar |
|---|---|
| **Graph view** (`Ctrl/Cmd + G`) | veja como os temas se conectam |
| **Backlinks** | painel direito: quem aponta para a nota atual |
| **Busca** (`Ctrl/Cmd + Shift + F`) | por exemplo `tag:#ownership` ou `path:"09 - Memória"` |
| **Outline** | índice da nota atual |
| **Canvas** | abra [[Mapa do Ownership.canvas]] e [[Trilha de Aprendizado em Rust.canvas]] |
| **Properties** | filtre notas pelo campo `nivel` (iniciante, intermediario, avancado) |
| **Page preview** | segure `Ctrl/Cmd` e passe o mouse sobre um link |
| **Templates** | `Ctrl/Cmd + P` → "Inserir template": veja [[MOC - Templates]] |

## Convenções das notas

- Todo bloco de código Rust compila na edição 2024, **exceto** quando marcado:
  - `// ❌ NÃO COMPILA`: exemplo de erro **proposital**, sempre seguido da mensagem do compilador e da correção;
  - `// trecho`: fragmento que depende de contexto (por exemplo, firmware);
  - `// requer crate: nome`: usa crate externo (adicione-o com `cargo add`).
- Callouts usados: `info`, `tip`, `warning`, `example`, `question`.
- `> [!question] Verificar na documentação oficial` marca pontos que mudam com frequência (APIs de crates, recursos instáveis).

> [!example] Campos do frontmatter
> `tags`, `aliases`, `tipo` (conceito, pratica, projeto, exercicio, moc...), `nivel` (iniciante, intermediario, avancado), `criado` e `relacionados`.

## Veja também

- [[Trilha de estudos - Rust]]
- [[Roteiro por semanas]]
- [[Livros, cursos e comunidades]]
- [[Template de nota de conceito]]
