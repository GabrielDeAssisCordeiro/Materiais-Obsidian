---
titulo: "MCP - conectar servidores externos"
tags:
  - openclaw
  - conceito
  - mcp
tipo: conceito
aliases: ['Model Context Protocol', 'openclaw mcp', 'mcp.servers']
nivel: intermediario
fontes:
  - "[[Fontes]]"
  - "https://docs.openclaw.ai/tools/mcp"
  - "https://docs.openclaw.ai/pt-BR/cli/mcp.md"
relacionados:
  - "[[Perfis e política de ferramentas]]"
  - "[[Visão geral das ferramentas do agente]]"
  - "[[Pontos de extensão - plugins, skills e hooks]]"
  - "[[Fronteiras de confiança na arquitetura]]"
---

# MCP - conectar servidores externos

## Objetivo

Conectar servidores MCP ao OpenClaw, verificá-los e restringir suas ferramentas, sem esquecer que eles passam pela mesma política que as ferramentas nativas.

## Explicação

MCP (Model Context Protocol) permite que o agente use ferramentas de outro programa. O servidor expõe *tools*, *resources* e *prompts*. As definições ficam em `mcp.servers` na configuração e passam pelo **mesmo perfil e política de ferramentas**: conectar um servidor não contorna a política. Se o servidor publica instruções de uso, o OpenClaw as repassa ao agente limitadas aos primeiros 2.000 caracteres por servidor.

Pela interface: **Settings → MCP → Add server**, escolher transporte (Streamable HTTP, SSE ou Stdio). Pela CLI (página `cli/mcp`):

| Comando | Função |
|---|---|
| `openclaw mcp list` / `show [nome]` | Lista ou mostra definições |
| `openclaw mcp add <nome> ...` | Cria a partir de flags e testa antes de salvar (`--no-probe` para pular) |
| `openclaw mcp set <nome> <json>` | Grava a definição completa em JSON |
| `openclaw mcp doctor [nome] [--probe]` | Checagens estáticas; `--probe` testa conexão |
| `openclaw mcp probe [nome]` | Conecta e lista tools, resources e prompts |
| `openclaw mcp tools <nome> [--include csv] [--exclude csv] [--clear]` | Filtros por servidor |
| `openclaw mcp login/logout <nome>` | OAuth para servidores HTTP |
| `openclaw mcp unset <nome>` | Remove |
| `openclaw mcp serve` | Expõe o **próprio OpenClaw** como servidor MCP |

> [!info] Dois sentidos
> `openclaw mcp serve` faz o OpenClaw ser *servidor* MCP (outros clientes o usam). Os demais comandos tratam o OpenClaw como *cliente* de servidores externos.

## Exemplo prático

Formato salvo para um servidor stdio e outro HTTP (da doc):

```json
{
  "command": "uvx",
  "args": ["context7-mcp"],
  "env": { "API_BASE": "https://interno.example" },
  "cwd": "/srv/tools"
}
```

```json
{
  "url": "https://mcp.example.com/mcp",
  "transport": "streamable-http",
  "timeout": 20,
  "toolFilter": { "include": ["search_*"], "exclude": ["admin_*"] }
}
```

Se `transport` for omitido num servidor HTTP, o OpenClaw usa `sse`. Verifique:

```bash
openclaw mcp set docs '{"url":"https://mcp.example.com/mcp","transport":"streamable-http"}'
openclaw mcp doctor docs --probe
openclaw mcp tools docs --include "search_*"
```

Com recarga a quente do Gateway, mudanças valem no próximo turno. Se um servidor cai, o OpenClaw mantém o último catálogo de tools, mas as chamadas informam indisponibilidade: o esquema retido não concede acesso.

## Armadilhas comuns

- Colocar token em `headers` no JSON e versionar o arquivo (use referências de segredo e permissões restritas).
- Instalar servidores de origem desconhecida: cada tool é superfície de ataque e cada descrição pode carregar instruções (veja [[Fronteiras de confiança na arquitetura]]).
- Não filtrar tools administrativas (`admin_*`).
- Confundir com o registro `config/mcporter.json`: `list`, `show`, `set` e `unset` **não** o leem.

## Resumo

- Cliente via `mcp.servers`; servidor via `openclaw mcp serve`.
- Sempre `doctor --probe` depois de salvar.
- Filtre tools por servidor; a política global continua valendo.

## Relacionados

- [[Perfis e política de ferramentas]]
- [[Visão geral das ferramentas do agente]]
- [[Pontos de extensão - plugins, skills e hooks]]
- [[Fronteiras de confiança na arquitetura]]
- [[Aprovações de exec e allowlists]]

## Exercícios

1. Qual a diferença entre `openclaw mcp serve` e `openclaw mcp add`?
2. Qual transporte é usado quando `transport` é omitido num servidor HTTP?
3. Como restringir um servidor a tools que começam com `search_`?
4. Por que "salvar" a definição não prova que o servidor funciona?
