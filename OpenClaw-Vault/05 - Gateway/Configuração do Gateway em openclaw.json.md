---
titulo: "Configuração do Gateway em openclaw.json"
tags:
  - openclaw
  - conceito
  - gateway
tipo: conceito
aliases: ['openclaw.json', 'Config do OpenClaw']
nivel: intermediario
fontes:
  - "[[Fontes]]"
  - "https://docs.openclaw.ai/gateway/configuration"
  - "https://docs.openclaw.ai/"
  - "https://docs.openclaw.ai/skill.md"
relacionados:
  - "[[Onde o OpenClaw guarda estado em disco]]"
  - "[[O Gateway como serviço em segundo plano]]"
  - "[[Control UI e dashboard]]"
  - "[[O processo Gateway e a porta 18789]]"
---

# Configuração do Gateway em openclaw.json

## Objetivo

Saber onde fica a configuração, como é validada e as quatro formas de editá-la com segurança.

## Explicação

O OpenClaw lê um arquivo opcional em **JSON5** em `~/.openclaw/openclaw.json`. Se ele não existir, valem padrões seguros. Pontos da documentação:

- O caminho precisa ser um **arquivo regular**. O OpenClaw o substitui de forma atômica nas escritas, por isso links simbólicos são desencorajados. Para guardar a configuração em outro lugar, defina `OPENCLAW_CONFIG_PATH` com o arquivo real.
- A configuração deve **corresponder totalmente ao esquema**: chaves desconhecidas, tipos errados ou valores inválidos **impedem o Gateway de iniciar**. A exceção na raiz é `$schema`.
- O Gateway **observa o arquivo** e aplica mudanças automaticamente (recarga a quente), com detalhes em página própria.
- Regra de layout: irmãos na raiz guardam infraestrutura e padrões entre agentes; `agents.defaults` guarda o comportamento do laço do agente.

Seções de topo citadas: `agents` (`agents.defaults`, `agents.entries`), `channels`, `plugins`, além de modelos, ferramentas, sandbox, automação, sessões, mídia, rede e UI.

**Exemplo mínimo da documentação:**

```json5
{
  agents: { defaults: { workspace: "~/.openclaw/workspace" } },
  channels: { whatsapp: { allowFrom: ["+15555550123"] } },
}
```

**Quatro formas de editar:**

```bash
openclaw configure
openclaw config get agents.defaults.workspace
openclaw config set agents.defaults.userTimezone "Europe/Vienna"
openclaw config unset plugins.entries.brave.config.webSearch.apiKey
```

Além disso, a aba **Config** da Control UI gera um formulário a partir do esquema ao vivo e tem um editor **Raw JSON**, e você pode editar o arquivo direto em um editor de texto.

**Validação e reparo:**

```bash
openclaw config validate
openclaw config schema
openclaw doctor --fix
```

`openclaw config schema` imprime o esquema JSON usado na validação, e `openclaw doctor --fix` repara chaves legadas.

> [!warning] Chaves exatas
> Sempre confirme o nome de uma chave com `openclaw config schema` ou na página "Configuration reference". Guias de terceiros citam arquivos e formatos diferentes (por exemplo YAML); a documentação oficial indica `openclaw.json`.

## Exemplo prático

Mudar o fuso horário do agente e conferir:

```bash
openclaw config set agents.defaults.userTimezone "America/Sao_Paulo"
openclaw config get agents.defaults.userTimezone
openclaw config validate
```

Se a validação falhar, o Gateway não sobe com esse arquivo; reverta o valor antes de reiniciar.

## Armadilhas comuns

- Inventar uma chave que "deveria existir": o esquema estrito recusa.
- Editar o arquivo por um link simbólico e quebrar a escrita atômica.
- Colocar segredos no arquivo em vez de usar a gestão de segredos; veja [[MOC - Segurança e Hardening|Segurança e Hardening]].

## Resumo

- `~/.openclaw/openclaw.json`, JSON5, esquema estrito.
- Edite com `openclaw configure`, `openclaw config get/set/unset`, Control UI ou editor.
- Valide com `openclaw config validate`; repare com `openclaw doctor --fix`.
- Mudanças são recarregadas a quente.

## Relacionados

- [[Onde o OpenClaw guarda estado em disco]]
- [[O Gateway como serviço em segundo plano]]
- [[Control UI e dashboard]]
- [[O protocolo WebSocket do Gateway]]

## Exercícios

1. Onde fica o arquivo de configuração e em que formato?
2. O que acontece se o arquivo tiver uma chave desconhecida?
3. Cite três formas de editar a configuração.
4. Que comando imprime o esquema de validação?
