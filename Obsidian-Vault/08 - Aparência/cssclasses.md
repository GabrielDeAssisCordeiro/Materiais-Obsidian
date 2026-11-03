---
tags: [aparencia, properties, css]
aliases: [cssclass, Classes CSS por nota]
tipo: conceito
nivel: intermediario
criado: 2026-10-23
relacionados: ["[[Snippets CSS]]", "[[Propriedades padrão]]", "[[Temas]]"]
---

# cssclasses

A propriedade `cssclasses` aplica **classes CSS** a uma nota específica ([[Propriedades padrão]]).

```yaml
---
cssclasses: [wide, destaque]
---
```

No snippet:
```css
.destaque h1 { color: var(--text-accent); }
```

## Usos
- Larguras e tabelas diferentes por nota.
- Estilos para dashboards ou diários.
- Alguns temas oferecem classes prontas (ex.: cartões, tabelas largas).

> [!question] Verificar na documentação oficial
> Confirme as classes que o seu tema oferece na documentação dele.

> [!tip] Use o plural
> Em versões atuais, o nome correto é `cssclasses` (lista).

## Veja também
- [[Snippets CSS]]
- [[Properties]]

## Exercício
Crie a classe `compacta` que reduz o espaçamento de listas e aplique-a em uma nota.
