---
tags: [markdown]
aliases: [LaTeX, MathJax, Fórmulas]
tipo: referencia
nivel: intermediario
criado: 2026-10-23
relacionados: ["[[Sintaxe estendida]]", "[[Blocos de código]]", "[[Fluxo de estudos acadêmicos]]"]
---

# Matemática com LaTeX

O Obsidian renderiza fórmulas com MathJax.

## Inline e bloco
```markdown
Fórmula inline: $E = mc^2$

Fórmula em bloco:
$$
\int_0^1 x^2\,dx = \frac{1}{3}
$$
```

## Exemplos úteis
| Objetivo | Código |
|---|---|
| Fração | `\frac{a}{b}` |
| Raiz | `\sqrt{x}` |
| Somatório | `\sum_{i=1}^{n} i` |
| Matriz | `\begin{bmatrix} a & b \\ c & d \end{bmatrix}` |
| Letras gregas | `\alpha, \beta, \pi` |

> [!warning] Cifrão no texto
> Dois `$` na mesma linha podem ser lidos como fórmula. Escape com `\$` ao falar de preços.

> [!info] Escopo
> Nem todo pacote LaTeX está disponível; MathJax cobre o essencial.
>
> > [!question] Verificar na documentação oficial
> > Para pacotes específicos (ex.: `mhchem`), confirme o suporte atual.

## Veja também
- [[Sintaxe estendida]]
- [[Fluxo de estudos acadêmicos]]

## Exercício
Escreva a fórmula de Bhaskara em bloco e o discriminante inline.
