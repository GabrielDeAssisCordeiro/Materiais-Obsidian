---
tags: [aparencia]
aliases: [Fontes, Tipografia]
tipo: guia
nivel: iniciante
criado: 2026-10-23
relacionados: ["[[Configurações de Aparência]]", "[[Snippets CSS]]", "[[Temas]]"]
---

# Fontes e tipografia

## Onde ajustar
Em **Settings → Appearance**:
- **Interface font:** menus e painéis.
- **Text font:** corpo das notas.
- **Monospace font:** código ([[Blocos de código]]).
- **Font size:** tamanho do texto.

Digite o nome de uma fonte instalada no sistema.

## Fonte customizada
```css
@font-face {
  font-family: "MinhaFonte";
  src: url("MinhaFonte.woff2");
}
body { --font-text: "MinhaFonte", sans-serif; }
```
Veja [[Snippets CSS]].

## Dicas
- Priorize legibilidade (fontes sem serifa ou com serifa de boa leitura).
- Fonte monoespaçada para código e tabelas alinhadas.
- Teste em claro e escuro ([[Temas]]).

> [!warning] Mobile
> Fontes instaladas no desktop podem não existir no celular ([[iOS e Android]]).

## Veja também
- [[Configurações de Aparência]]
- [[Ideias de interface]]

## Exercício
Troque a fonte de texto e a de código e compare a legibilidade de uma nota longa.
