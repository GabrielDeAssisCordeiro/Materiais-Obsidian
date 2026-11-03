---
tags: [markdown, anexos]
aliases: [Incorporar, Transclusão, Embed]
tipo: referencia
nivel: iniciante
criado: 2026-10-23
relacionados: ["[[Links para títulos e blocos]]", "[[Gerenciamento de anexos]]", "[[Canvas]]"]
---

# Embeds

Embed (transclusão) mostra o conteúdo de outro arquivo **dentro** da nota atual. A sintaxe é `!` + wikilink.

## Notas, títulos e blocos
```markdown
![[Outra nota]]
![[Outra nota#Título]]
![[Outra nota#^id-do-bloco]]
```
Veja [[Links para títulos e blocos]].

## Imagens
```markdown
![[foto.png]]
![[foto.png|300]]         largura em pixels
![[foto.png|300x200]]     largura x altura
![texto](foto.png)
```

## Outros arquivos
```markdown
![[documento.pdf]]
![[documento.pdf#page=3]]
![[audio.mp3]]
![[video.mp4]]
![[Mapa.canvas]]
![[Exemplo de Base.base]]
```
- PDFs, áudio, vídeo, [[Canvas]] e [[Bases]] podem ser incorporados.
- Na Web: iframes e vídeos com HTML ou links, conforme suporte ([[Web viewer]]).

> [!tip] Reuso
> Embute um bloco numa nota de projeto para reaproveitar uma definição sem copiar.

> [!warning] Caminhos e anexos
> Se o arquivo estiver fora do local esperado, ajuste a pasta de anexos ([[Gerenciamento de anexos]]).

## Veja também
- [[Sintaxe estendida]]
- [[Wikilinks e links Markdown]]

## Exercício
Incorpore uma imagem com 250 px de largura e um título de outra nota na nota de hoje ([[Notas diárias]]).
