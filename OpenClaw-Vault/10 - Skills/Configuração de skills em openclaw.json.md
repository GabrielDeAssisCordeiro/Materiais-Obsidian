---
titulo: "Configuração de skills em openclaw.json"
tags:
  - openclaw
  - conceito
  - skills
tipo: conceito
aliases: ['skills.entries', 'skills.load']
nivel: intermediario
fontes:
  - "[[Fontes]]"
  - "https://docs.openclaw.ai/tools/skills-config"
relacionados:
  - "[[Configuração do Gateway em openclaw.json]]"
  - "[[Anatomia do SKILL.md e requisitos de elegibilidade]]"
  - "[[A CLI openclaw skills]]"
  - "[[Roteamento multiagente e bindings]]"
---

# Configuração de skills em openclaw.json

## Objetivo

Saber quais chaves da seção `skills` do `~/.openclaw/openclaw.json` foram confirmadas, o que cada uma controla e como limitar quais skills cada agente enxerga.

## Explicação

A configuração de skills fica sob a chave `skills` do arquivo principal (veja [[Configuração do Gateway em openclaw.json]]). A visibilidade por agente fica em `agents.defaults.skills` e `agents.entries.*.skills`.

### Chaves confirmadas

| Chave | Tipo / padrão | Efeito |
|---|---|---|
| `skills.allowBundled` | lista de nomes | Permite apenas as skills bundled listadas |
| `skills.entries.<nome>.enabled` | booleano | Liga ou desliga uma skill |
| `skills.entries.<nome>.apiKey` | objeto de referência | Ex.: `{ source: "env", provider: "default", id: "GEMINI_API_KEY" }` |
| `skills.entries.<nome>.env` | mapa | Variáveis de ambiente injetadas para a skill |
| `skills.load.extraDirs` | `string[]` | Diretórios extras, na menor precedência; `~` é expandido |
| `skills.load.allowSymlinkTargets` | `string[]` | Diretórios reais confiáveis para onde links simbólicos podem apontar |
| `skills.load.watch` | booleano, padrão `true` | Descobre skills por eventos do sistema de arquivos; há nova varredura a cada 30 minutos |
| `skills.install.preferBrew` | booleano, padrão `true` | Prefere instaladores Homebrew quando `brew` existe |
| `skills.install.nodeManager` | `npm`, `pnpm`, `yarn` ou `bun`; padrão `npm` | Gerenciador só para instalar skills |
| `skills.install.allowUploadedArchives` | booleano, padrão `false` | Permite a clientes `operator.admin` instalar zips privados |

> [!warning] Partes não lidas
> A página truncou antes das seções `security.installPolicy`, `workshop` e sandbox. Elas aparecem no índice, mas **não foram verificadas**; consulte a página antes de depender delas.

## Exemplo prático

Exemplo em JSON5 usando só chaves confirmadas (os nomes de skill são ilustrativos):

```json5
{
  skills: {
    allowBundled: ["gemini", "peekaboo"],
    entries: {
      peekaboo: { enabled: true },
      sag: { enabled: false },
      gemini: {
        apiKey: { source: "env", provider: "default", id: "GEMINI_API_KEY" },
      },
    },
    load: {
      extraDirs: ["~/minhas-skills"],
      watch: true,
    },
    install: { nodeManager: "pnpm" },
  },
}
```

Depois de editar, valide e reinicie:

```bash
openclaw config validate
openclaw gateway restart
openclaw skills check
```

## Armadilhas comuns

- Apontar `allowSymlinkTargets` para um diretório amplo como `~`: abre caminho para skills fora do que você revisou.
- Usar `skills.entries` para geração de imagem nativa: a doc manda usar `agents.defaults.mediaModels.image` e a ferramenta `image_generate`.
- Ligar `allowUploadedArchives` sem necessidade: instalações normais do ClawHub não precisam dele.
- Esquecer que o esquema é estrito: chave desconhecida faz a validação falhar (use `openclaw config validate`).

## Resumo

- Tudo vive em `skills.*`; visibilidade por agente em `agents.*.skills`.
- `extraDirs` tem a menor precedência.
- Segredos devem ser referenciados (`apiKey` com `source`), não escritos no texto.

## Relacionados

- [[Configuração do Gateway em openclaw.json]]
- [[Anatomia do SKILL.md e requisitos de elegibilidade]]
- [[A CLI openclaw skills]]
- [[Roteamento multiagente e bindings]]
- [[ClawHub - publicar, versões e verificação]]

## Exercícios

1. Qual chave define diretórios adicionais de skills e qual sua precedência?
2. Qual o padrão de `skills.install.nodeManager`?
3. Por que `allowSymlinkTargets` deve ser uma lista estreita?
4. Que comando valida a configuração antes de reiniciar o Gateway?
