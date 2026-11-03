---
tags: [fundamentos, organizacao]
aliases: [Pastas]
tipo: conceito
nivel: iniciante
criado: 2026-10-23
relacionados: ["[[Pastas, tags ou links]]", "[[Método PARA]]", "[[Johnny.Decimal]]"]
---

# Estrutura de pastas

Pastas são úteis, mas **não precisam ser o principal mecanismo** de organização: links e [[Properties]] ligam ideias de forma mais flexível ([[Pastas, tags ou links]]).

## Estrutura mínima sugerida
```text
Meu Vault/
├── 00 - Caixa de entrada/   ← captura rápida
├── 10 - Projetos/
├── 20 - Áreas/
├── 30 - Recursos/
├── 90 - Arquivo/
├── Anexos/                  ← imagens, PDFs
└── Templates/
```
Esse formato se inspira no [[Método PARA]]; numerar pastas lembra o [[Johnny.Decimal]].

## Boas práticas
- Poucos níveis (2–3 no máximo).
- Defina uma **caixa de entrada** para capturar sem decidir onde guardar.
- Separe **anexos** ([[Gerenciamento de anexos]]) e **templates** ([[Core - Templates]]).
- Nomes de arquivo sem `\ / : * ? " < > |`, que são inválidos em alguns sistemas.

> [!warning] Renomear e mover
> Com *Automatically update internal links* ativo, mover notas pelo Obsidian atualiza os links ([[Configurações de Arquivos e links]]). Mover por fora do app pode quebrá-los.

## Veja também
- [[Vault]]
- [[Core - Explorador de arquivos]]

## Exercício
Desenhe a estrutura de pastas do seu vault em um bloco de código e justifique cada pasta.
