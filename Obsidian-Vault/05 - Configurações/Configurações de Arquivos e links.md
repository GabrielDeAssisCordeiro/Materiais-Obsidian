---
tags: [configuracoes, arquivos, links]
aliases: [Settings Files and links, Files and links]
tipo: referencia
nivel: intermediario
criado: 2026-10-23
relacionados: ["[[Wikilinks e links Markdown]]", "[[Gerenciamento de anexos]]", "[[Estrutura de pastas]]"]
---

# Configurações de Arquivos e links

| Opção | Efeito | Recomendação |
|---|---|---|
| **Confirm file deletion** | Pede confirmação ao apagar | Ligar |
| **Deleted files** | Destino: lixeira do sistema, `.trash` ou permanente | Lixeira do sistema |
| **Automatically update internal links** | Atualiza links ao renomear/mover | **Ligar** |
| **Default location for new notes** | Raiz, pasta específica ou pasta atual | Caixa de entrada ou pasta atual |
| **New link format** | Caminho mais curto, relativo ou absoluto | Mais curto; absoluto se houver nomes repetidos |
| **Use Wikilinks** | Alterna entre `[[ ]]` e `[](...)` | Wikilinks para uso interno ([[Wikilinks e links Markdown]]) |
| **Detect all file extensions** | Mostra arquivos de outros tipos | Ligar só se precisar |
| **Default location for new attachments** | Pasta de anexos ([[Gerenciamento de anexos]]) | Pasta dedicada, como `Anexos` |
| **Excluded files** | Esconde pastas da busca e dos links | Use para rascunhos e arquivo morto |
| **Override config folder** | Usa outra pasta de configuração | Avançado ([[Configurações por dispositivo ou por vault]]) |

> [!warning] Mover fora do Obsidian
> Se mover ou renomear arquivos pelo sistema operacional, links podem quebrar. Prefira fazê-lo no app ([[Links não resolvidos]]).

> [!tip] Excluir da busca
> *Excluded files* reduz ruído em [[Busca e operadores]] e no [[Graph view]].

## Veja também
- [[Estrutura de pastas]]
- [[Pasta .obsidian]]

## Exercício
Configure uma pasta de anexos e uma pasta padrão para novas notas e teste colando uma imagem.
