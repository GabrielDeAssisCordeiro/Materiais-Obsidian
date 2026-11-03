---
tags: [markdown, comentarios]
aliases: [Comentários, Footnotes, Notas de rodapé]
tipo: referencia
nivel: iniciante
criado: 2026-10-23
relacionados: ["[[Sintaxe estendida]]", "[[Modos de edição e leitura]]", "[[Sintaxe básica]]"]
---

# Comentários e notas de rodapé

## Comentários
Texto entre `%%` não aparece em Reading view:
```markdown
Texto visível %%anotação oculta%% mais texto.

%%
Bloco inteiro
comentado
%%
```
Em Source e Live Preview eles ainda aparecem ([[Modos de edição e leitura]]).

Comentários HTML também funcionam: `<!-- oculto -->`.

> [!warning] Não é segredo
> Comentários continuam no arquivo `.md`. Não guarde informações sensíveis neles, especialmente se for publicar ([[Obsidian Publish]]).

## Notas de rodapé
```markdown
Texto com referência[^1] e outra[^nome].

[^1]: Conteúdo da nota.
[^nome]: Outra nota de rodapé.
```
Também há a forma inline: `^[nota escrita no próprio texto]`.

> [!tip] Uso
> Ótimo para fontes e esclarecimentos em notas de estudo ([[Fluxo de estudos acadêmicos]]).

## Veja também
- [[Sintaxe estendida]]
- [[Cheat sheet Markdown]]

## Exercício
Escreva um parágrafo com duas notas de rodapé e um comentário oculto; confirme o comportamento em Reading view.
