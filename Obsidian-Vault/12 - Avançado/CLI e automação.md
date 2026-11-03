---
tags: [avancado, automacao, cli]
aliases: [Scripts, Automação]
tipo: guia
nivel: avancado
criado: 2026-10-23
relacionados: ["[[URI scheme]]", "[[Obsidian Git]]", "[[API de plugins]]"]
---

# CLI e automação

Como o vault é uma pasta de arquivos, é fácil automatizar com ferramentas comuns.

## Linha de comando
- O Obsidian passou a oferecer uma **interface de linha de comando oficial** em versões recentes.

> [!question] Verificar na documentação oficial
> Confirme disponibilidade, instalação e comandos atuais da CLI em help.obsidian.md; este material não lista comandos para não induzir a erro.

## Ferramentas gerais
```bash
# Listar notas sem frontmatter
grep -L '^---' *.md

# Contar notas por pasta
find . -name '*.md' | cut -d/ -f2 | sort | uniq -c
```

## Opções de automação
| Opção | Uso |
|---|---|
| Scripts shell/Python | análise e limpeza em lote |
| [[Templater]] e [[QuickAdd]] | automação dentro do app |
| [[URI scheme]] | acionar o app de fora |
| Plugin *Local REST API* | controlar o vault por HTTP (verificar) |
| Pandoc | converter para PDF, Word e HTML ([[Importar e exportar]]) |
| [[Obsidian Git]] | commit e backup automáticos |

> [!warning] Faça backup
> Scripts que alteram arquivos em lote exigem [[Backup]] antes e testes em cópia.

## Veja também
- [[Migração de e para outras ferramentas]]
- [[API de plugins]]

## Exercício
Escreva um script que liste as notas sem propriedade `nivel`.
