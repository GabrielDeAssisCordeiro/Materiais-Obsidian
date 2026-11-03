---
tags: [properties, referencia]
aliases: [Properties padrão, tags aliases cssclasses]
tipo: referencia
nivel: iniciante
criado: 2026-10-23
relacionados: ["[[Aliases]]", "[[Tags]]", "[[cssclasses]]"]
---

# Propriedades padrão

O Obsidian reconhece três propriedades especiais:

| Propriedade | Tipo | Efeito |
|---|---|---|
| `tags` | lista | tags da nota, sem `#` ([[Tags]]) |
| `aliases` | lista | nomes alternativos ([[Aliases]]) |
| `cssclasses` | lista | classes CSS na nota ([[cssclasses]]) |

```yaml
---
tags: [estudo, obsidian]
aliases: [Nota de exemplo]
cssclasses: [wide, destaque]
---
```

> [!warning] Nomes antigos
> As formas no singular (`tag`, `alias`, `cssclass`) foram descontinuadas; use sempre o plural.
>
> > [!question] Verificar na documentação oficial
> > Confirme a versão em que foram removidas e se algum plugin ainda lê os nomes antigos.

Propriedades próprias (como `tipo` e `nivel`) são livres: veja [[Nomenclatura de propriedades]].

## Veja também
- [[Properties]]
- [[Tipos de properties]]

## Exercício
Adicione `cssclasses` a uma nota e crie um snippet que a estilize ([[Snippets CSS]]).
