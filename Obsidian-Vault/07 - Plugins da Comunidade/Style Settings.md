---
tags: [plugins-comunidade, plugin]
aliases: [Style Settings plugin, Configurações de estilo]
tipo: plugin
nivel: intermediario
criado: 2026-10-23
relacionados: ["[[Temas]]", "[[Snippets CSS]]", "[[Ideias de interface]]", "[[MOC - Plugins da Comunidade]]"]
---

# Style Settings

## Para que serve
Expõe configurações de temas e snippets CSS como controles visuais (cores, tamanhos, opções).

## Instalação e configuração
Instale em **Settings → Community plugins → Browse** ([[Instalando e avaliando segurança]]).

- Instale e ative; abra a seção *Style Settings* em Settings.
- Temas compatíveis (como Minimal) aparecem ali.
- Seus próprios snippets podem declarar opções num comentário `@settings`.

## Exemplo prático
```css
/* @settings
name: Meu estilo
id: meu-estilo
settings:
  -
    id: cor-destaque
    title: Cor de destaque
    type: variable-color
    format: hex
    default: '#7c3aed'
*/
```

> [!question] Verificar na documentação oficial
> Confirme os tipos de variáveis suportados no bloco `@settings`.

## Veja também
- [[Temas]]
- [[Snippets CSS]]
- [[Ideias de interface]]
- [[MOC - Plugins da Comunidade]]

## Exercício
Instale em um vault de teste, execute o exemplo e decida se vale manter no vault principal.
