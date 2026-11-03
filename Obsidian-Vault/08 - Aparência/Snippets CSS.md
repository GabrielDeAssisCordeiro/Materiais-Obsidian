---
tags: [aparencia, css]
aliases: [Snippets, CSS personalizado]
tipo: guia
nivel: intermediario
criado: 2026-10-23
relacionados: ["[[cssclasses]]", "[[Callouts]]", "[[Pasta .obsidian]]"]
---

# Snippets CSS

Pequenos arquivos `.css` que ajustam o visual sem trocar de tema.

## Como usar
1. Abra a pasta de snippets (**Settings → Appearance → CSS snippets → ícone de pasta**), que é `.obsidian/snippets/` ([[Pasta .obsidian]]).
2. Crie `meu-estilo.css`.
3. Recarregue a lista e ative o snippet.

## Exemplos
Callout personalizado ([[Callouts]]):
```css
.callout[data-callout="ideia"] {
  --callout-color: 255, 190, 0;
  --callout-icon: lucide-lightbulb;
}
```
Cabeçalhos com cor:
```css
.markdown-rendered h2 { color: var(--text-accent); }
```
Largura maior em notas com a classe `wide`:
```css
.wide .markdown-preview-sizer { max-width: 100% !important; }
```
Combine com [[cssclasses]] para aplicar só a algumas notas.

> [!tip] Ferramentas do desenvolvedor
> Use as ferramentas de inspeção do app (desktop) para descobrir seletores.

> [!warning] Mudanças entre versões
> Seletores internos podem mudar com atualizações; mantenha os snippets pequenos.

## Veja também
- [[Temas]]
- [[Style Settings]]

## Exercício
Crie um callout `> [!ideia]` com cor e ícone próprios.
