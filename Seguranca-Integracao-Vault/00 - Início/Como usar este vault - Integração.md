---
titulo: "Como usar este vault - Integração"
aliases: ["Guia de uso", "Manual do vault"]
tags:
  - integracao-seguranca
  - moc
  - inicio
tipo: moc
nivel: iniciante
criado: 2026-10-26
relacionados:
  - "[[Home - Integração]]"
  - "[[MOC - Fundamentos - Integração]]"
  - "[[MOC - Revisão - Integração]]"
---

# Como usar este vault - Integração

## Resumo

Este vault organiza o estudo de desenvolvimento e integração de ferramentas de segurança em 12 módulos numerados. Todas as notas seguem o mesmo padrão, o que facilita a leitura, a revisão e a consulta rápida. Volte à [[Home - Integração]] a qualquer momento.

## Conceitos-chave

- **MOC (Map of Content):** nota-índice de cada pasta (`MOC - tema`).
- **Front matter:** metadados YAML (`titulo`, `tipo`, `nivel`, `criado`, `relacionados`).
- **Tags:** toda nota leva `integracao-seguranca`, a tag do seu `tipo` e a do tema da pasta (por exemplo `devsecops` ou `deteccao`).

## Como funciona

1. No Obsidian, use *Abrir pasta como cofre* e escolha a pasta `Materiais-Obsidian`. Este material fica na subpasta `Seguranca-Integracao-Vault` (veja o [[GUIA]]).
2. Comece pela [[Home - Integração]] e siga a trilha sugerida.
3. Leia cada nota, execute os exemplos em ambiente de laboratório.
4. Ao final de cada módulo, faça os flashcards e questões em [[MOC - Revisão - Integração]].
5. Consolide o aprendizado com os projetos de [[MOC - Projetos Práticos]].

### Plugins recomendados (instale pela comunidade)

| Plugin | Uso |
|---|---|
| Dataview | Listar notas por `nivel` ou `tipo` |
| Spaced Repetition | Revisar flashcards no formato `pergunta::resposta` |

### Templates e anexos

- Modelos (plugin Templates do Obsidian): [[Template - Nota de Conceito - Integração]], [[Template - Nota de Ferramenta]] e [[Template - Nota de Projeto]].
- Imagens, canvases e arquivos de apoio: pasta `Anexos` na raiz do vault ([[MOC - Anexos]]).

## Exemplo prático

Consulta Dataview para listar as notas de conteúdo por nível:

```dataview
TABLE nivel, tipo
FROM ""
WHERE tipo != "moc" AND tipo != "revisao"
SORT nivel ASC
```

> [!tip] Templates
> Use os modelos em `Templates` (conceito, ferramenta, projeto) para novas notas. Ficam na pasta `Templates` da raiz do vault (veja [[MOC - Templates]]).

## Boas práticas

- Estude com um laboratório isolado, nunca em produção.
- Registre dúvidas com `> [!question]`.
- Crie notas próprias ligando-as aos MOCs.

## Erros comuns

- Ler sem praticar.
- Criar notas sem links, deixando-as órfãs no grafo.

## Referências para aprofundar

- Documentação oficial do Obsidian, Dataview e Spaced Repetition.

## Veja também

- [[Home - Integração]]
- [[MOC - Fundamentos - Integração]]
- [[MOC - Revisão - Integração]]
