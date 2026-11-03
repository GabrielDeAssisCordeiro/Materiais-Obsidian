---
tags: [funcoes]
aliases: [Quadro infinito, Whiteboard]
tipo: funcao
nivel: intermediario
criado: 2026-10-23
relacionados: ["[[Core - Canvas]]", "[[Excalidraw]]", "[[Diagramas Mermaid]]"]
---

# Canvas

Quadro infinito para organizar notas, imagens e ideias espacialmente. Os arquivos têm extensão `.canvas` e formato **JSON Canvas**, aberto e legível.

## Elementos
- **Cartões** de texto.
- **Notas** do vault incorporadas.
- **Mídia** (imagens, PDFs...).
- **Páginas web**.
- **Grupos** para agrupar visualmente.
- **Conexões** com setas e rótulos.

## Como usar
1. Paleta de comandos → *Create new canvas* ([[Core - Canvas]]).
2. Arraste notas do explorador.
3. Dê duplo clique para criar cartão.
4. Arraste das bordas para conectar.

## Estrutura do arquivo
```json
{
  "nodes": [
    {"id": "a1", "type": "text", "text": "Ideia", "x": 0, "y": 0, "width": 250, "height": 100}
  ],
  "edges": [
    {"id": "e1", "fromNode": "a1", "toNode": "a2"}
  ]
}
```

## Canvas × outros
| Recurso | Quando |
|---|---|
| Canvas | pensar espacialmente, mapas |
| [[Diagramas Mermaid]] | diagramas como texto |
| [[Excalidraw]] | desenho livre |

> [!tip] Exemplos neste vault
> Veja os mapas na pasta `Anexos`; incorpore-os com `![[nome.canvas]]` ([[Embeds]]).

## Veja também
- [[Graph view]]
- [[Fluxo de estudos acadêmicos]]

## Exercício
Monte um canvas com 5 notas e 4 conexões rotuladas sobre um tema de estudo.
