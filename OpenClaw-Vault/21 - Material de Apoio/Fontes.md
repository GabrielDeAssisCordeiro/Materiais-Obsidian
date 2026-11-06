---
titulo: "Fontes consultadas"
tags:
  - openclaw
  - referencia
tipo: referencia
aliases: []
nivel: iniciante
fontes:
  - "[[Fontes]]"
relacionados:
  - "[[Home - OpenClaw]]"
---

# Fontes consultadas

Pesquisa feita em 27/10/2026. Esta lista cresce a cada parte do vault.

> [!warning] Divergências encontradas na pesquisa
> - **Versão do Node.js**: três páginas dizem coisas diferentes. A página "Getting started" no GitHub (copiada há cerca de 120 dias) cita Node 24.16+ ou 26.1+. A página inicial da doc atual recomenda Node 26 e aceita 24.22.1+ ou 26.12.1+. O arquivo `skill.md` da doc cita Node 24 ou 22.14+. Confirme em `docs.openclaw.ai/install/node` antes de instalar.
> - **Última versão**: o banner da página inicial mostra v2026.10.8, enquanto o menu lateral lista v2026.10.7 como a mais recente. Veja `docs.openclaw.ai/releases`.
> - **Arquivo de configuração**: a doc oficial indica `~/.openclaw/openclaw.json` (formato JSON5). Guias de terceiros citam outros nomes (por exemplo YAML); trate-os como não confirmados.
> - **Contagens de skills maliciosas** (campanha ClawHavoc) variam entre fontes: de 341 a 820, conforme a semana de remoções.

## Fontes oficiais

| Fonte | URL | Usada para |
|---|---|---|
| Documentação oficial (página inicial) | https://docs.openclaw.ai/ | Visão geral, navegação, requisitos, instalação rápida, Control UI, fundação |
| Getting started | https://docs.openclaw.ai/start/getting-started | Instalação, onboarding, `openclaw gateway install`, `openclaw dashboard` |
| Getting started (GitHub) | https://github.com/openclaw/openclaw/blob/main/docs/start/getting-started.md | Comparação de requisitos |
| skill.md da doc | https://docs.openclaw.ai/skill.md | Comandos de CLI, caminhos de configuração e workspace |
| Repositório principal | https://github.com/openclaw/openclaw | Licença MIT, docs versionadas em `docs/` |
| Segurança do Gateway | https://docs.openclaw.ai/gateway/security | Modelo de segurança (a ser lido em detalhe na parte de Segurança) |
| Site do projeto | https://openclaw.ai | Script de instalação |

## Estrutura da documentação oficial

Seções do menu: Get started, Install, Channels, Agents, Capabilities (plugins, skills, automação, ferramentas), ClawHub, Models, Platforms, Gateway & Ops (incluindo Security and sandboxing), Reference (CLI, templates, referência técnica), Releases, Help (FAQ e diagnósticos). Esse mapa guia as próximas partes.

## Fatos confirmados na doc oficial

- Gateway autohospedado conecta apps de chat a agentes de IA; processo único na sua máquina ou servidor.
- Instalação: `curl -fsSL https://openclaw.ai/install.sh | bash` (macOS, Linux, WSL2) e `iwr -useb https://openclaw.ai/install.ps1 | iex` (Windows PowerShell).
- Onboarding oferece Quick start e Custom setup; `openclaw onboard --classic` abre o assistente clássico.
- `openclaw gateway install` instala o serviço em segundo plano; `openclaw dashboard` abre a Control UI.
- Control UI local padrão: `http://127.0.0.1:18789/`.
- Config principal em `~/.openclaw/openclaw.json`.
- Projeto licenciado sob MIT e desenvolvido pela OpenClaw Foundation, uma entidade 501(c)(3) independente, segundo a doc.

## Fontes de terceiros (contexto histórico e segurança)

Usadas apenas como contexto; onde divergem da doc oficial, vale a doc.

| Fonte | URL | Uso |
|---|---|---|
| Morph, histórico do Clawdbot | https://www.morphllm.com/clawdbot | Linha do tempo e renomeações |
| Storyboard18, rebrand para OpenClaw | https://www.storyboard18.com/digital/clawdbot-becomes-openclaw-after-trademark-checks-as-open-source-ai-project-evolves-88639.htm | Confirmação do rebrand e verificação de marca |
| AlternativeTo, rebrand para Moltbot | https://alternativeto.net/news/2026/1/trending-open-source-ai-agent-clawdbot-rebrands-to-moltbot-after-pressure-from-anthropic/ | Primeira renomeação |
| Hora de Codar, repositório oficial | https://horadecodar.com.br/openclaw-github/ | Estrutura de repositórios e fundação |
| Nebius, segurança e hardening | https://nebius.com/blog/posts/openclaw-security | Contexto de segurança |
| DeepInfra, prompt injection e supply chain | https://deepinfra.com/blog/openclaw-security-prompt-injection-supply-chain-attacks-hardening | Contexto de ameaças |
| Adversa AI, SecureClaw | https://adversa.ai/secureclaw | Contexto de ameaças e ferramentas de terceiros |
| Guia explain-openclaw (comunidade) | https://github.com/centminmod/explain-openclaw | Cruzamento de comandos com a doc |
| Guia OpenClaw Beginner to Expert | https://yeasy.gitbook.io/openclaw_guide/readme_en.md | Contexto geral |

## Linha do tempo (a confirmar com mais fontes)

| Data | Evento | Fonte |
|---|---|---|
| Fim de 2025 | Início do projeto como Clawdbot | Morph, jitendrazaa |
| 27/01/2026 | Renomeado para Moltbot após pedido de marca da Anthropic | Morph, AlternativeTo |
| 30/01/2026 | Renomeado para OpenClaw | Morph, Storyboard18 |
| 14/02/2026 | Steinberger anuncia em seu blog que vai para a OpenAI e que o projeto migrará para uma fundação aberta e independente | steipete.me |
| 08/07/2026 | Anúncio de que a OpenClaw Foundation passa a manter o projeto | Hora de Codar (terceiro; confirmar em openclaw.org) |

> [!warning] Datas de terceiros
> As datas acima vêm de matérias e blogs, não da doc oficial. A parte de História e Ecossistema deve reconfirmá-las, de preferência no blog em openclaw.ai e no GitHub.

## Fontes adicionadas na PARTE 2

| Fonte | URL | Usada para |
|---|---|---|
| Recursos (features) | https://docs.openclaw.ai/concepts/features | Canais do núcleo e plugins, modelos, mídia, ferramentas |
| Why OpenClaw | https://docs.openclaw.ai/start/why-openclaw | Fronteira de confiança, política em código, sandbox desligado por padrão |
| Arquitetura do Gateway | https://docs.openclaw.ai/concepts/architecture | Gateway único por host, porta padrão 127.0.0.1:18789, protocolo WebSocket |
| Agent loop | https://docs.openclaw.ai/concepts/agent-loop | Sequência de execução, `runId`, eventos, `agent.wait` |
| ClawHub, como funciona | https://docs.openclaw.ai/clawhub/how-it-works | Registro, versões imutáveis, comandos de instalação e publicação |
| Blog do criador | https://steipete.me/posts/2026/openclaw | Anúncio de 14/02/2026 sobre OpenAI e fundação |
| Artigo ReAct | https://arxiv.org/abs/2210.03629 | Definição do padrão ReAct (Yao et al., 6/10/2022) |
| Análise do fluxo de desenvolvimento | https://www.heyuan110.com/posts/ai/2026-01-31-openclaw-claude-code-workflow/ | Contexto de desenvolvimento e métricas de estrelas (terceiro) |
| Comunicado de imprensa (openclaw.my) | https://pr.capitalpress.com/article/The-Final-Evolution-Viral-Sensation-Clawdbot-Completes-Its-Journey-from-Moltbot-to-OpenClaw/697dbd36ca2cd60002adabd0 | Citado apenas como exemplo de domínio não confirmado |

> [!warning] Páginas não lidas
> As páginas `docs.openclaw.ai/start/lore` e `docs.openclaw.ai/help/faq/what-is-openclaw` não puderam ser consultadas nesta sessão (não permitidas pelo ambiente). A linha do tempo depende, portanto, de fontes de terceiros e do blog do criador.

## Fontes adicionadas na PARTE 3

| Fonte | URL | Usada para |
|---|---|---|
| Configuração | https://docs.openclaw.ai/gateway/configuration | `openclaw.json` (JSON5), validação, `openclaw config get/set/unset`, recarga a quente |
| System prompt | https://docs.openclaw.ai/concepts/system-prompt | Camadas de montagem do prompt (leitura parcial) |
| Workspace do agente | https://docs.openclaw.ai/concepts/agent-workspace | Local do workspace, variáveis de ambiente (leitura parcial) |
| Sessões | https://docs.openclaw.ai/concepts/session | Propriedade do estado, tipos de sessão (leitura parcial) |
| Roteamento de canais | https://docs.openclaw.ai/channels/channel-routing | Chaves de sessão, `session.dmScope`, `session.groupScope` |
| Multiagente | https://docs.openclaw.ai/concepts/multi-agent | `agentDir`, bindings, skills por agente (leitura parcial) |
| Streaming | https://docs.openclaw.ai/concepts/streaming | Block e preview streaming (leitura parcial) |
| Fila de comandos | https://docs.openclaw.ai/concepts/queue | Modo `steer`, faixas de concorrência (leitura parcial) |
| Agente (runtime embutido) | https://docs.openclaw.ai/concepts/agent | Bootstrap files, ferramentas nativas (leitura parcial) |
| Contexto | https://docs.openclaw.ai/concepts/context | Comandos `/context`, `/status`, `/compact` (leitura parcial) |
| CLI daemon | https://docs.openclaw.ai/pt-BR/cli/daemon.md | Comandos e flags do serviço do Gateway |
| Acesso remoto (Tailscale) | https://docs.openclaw.ai/gateway/tailscale | Serve, Funnel, bind `tailnet`, autenticação |
| Acesso remoto | https://docs.openclaw.ai/gateway/remote | Loopback padrão, SSH, topologias (leitura parcial) |
| Control UI | https://docs.openclaw.ai/web/control-ui | Chaves `gateway.controlUi.*` (leitura parcial) |

> [!warning] Leituras parciais
> Várias páginas acima foram truncadas pela ferramenta de leitura (cerca de 100 mil caracteres) ou tinham seções visíveis só como títulos. As notas sinalizam isso com callouts. `docs.openclaw.ai/gateway`, `/cli/gateway`, `/gateway/protocol` e `/web/control-ui` (na primeira tentativa) não foram permitidas pelo ambiente.

## Fontes adicionadas na PARTE 4

| Fonte | URL | Usada para |
|---|---|---|
| Canais (visão geral) | https://docs.openclaw.ai/channels | Núcleo versus plugins, `channels add`, `status --probe` (leitura parcial) |
| Pareamento | https://docs.openclaw.ai/channels/pairing | Códigos, validade, limite, `pairing list/approve` (leitura parcial) |
| Telegram | https://docs.openclaw.ai/channels/telegram | Visão geral e transportes |
| Telegram, setup | https://docs.openclaw.ai/channels/telegram/setup | BotFather, `botToken`, `TELEGRAM_BOT_TOKEN`, grupos, privacidade |
| Telegram, controle de acesso | https://docs.openclaw.ai/channels/telegram/access-control | `dmPolicy`, `allowFrom`, política de ferramentas por chat (leitura parcial) |
| WhatsApp | https://docs.openclaw.ai/channels/whatsapp | Plugin, login por QR, chaves de acesso (leitura parcial) |
| Grupos | https://docs.openclaw.ai/channels/groups | `requireMention`, `groupPolicy` (leitura parcial) |
| Discord | https://docs.openclaw.ai/channels/discord | Visão geral e DMs em pareamento por padrão |
| CLI models | https://docs.openclaw.ai/cli/models | `openclaw models ...`, `agents.defaults.model` (leitura parcial) |
| Anthropic (espelho zh-CN) | https://docs.openclaw.ai/zh-CN/providers/anthropic | Chave de API, Claude CLI, setup-token, thinking, cache |
| Ollama | https://docs.openclaw.ai/providers/ollama | `baseUrl` nativo, sem `/v1` |
| Modelos locais | https://docs.openclaw.ai/gateway/local-models | llama.cpp gerenciado, cautelas (leitura parcial) |
| Failover de modelos | https://docs.openclaw.ai/concepts/model-failover | Estágios, TPM, `agents.defaults.model.fallbacks` (leitura parcial) |
| Uso de tokens e custos | https://docs.openclaw.ai/reference/token-use.md | Fatores de custo, `/usage`, chaves de orçamento |
| Memória (visão geral) | https://docs.openclaw.ai/concepts/memory | Arquivos de memória e injeção (leitura parcial) |
| Memória, cópia antiga (terceiro) | https://cdn.jsdelivr.net/npm/activeclaw@2026.4.9/docs/concepts/memory.md | Chaves de busca híbrida e memory flush; **versão de abril de 2026, validar** |
| Compactação | https://docs.openclaw.ai/concepts/compaction | Resumo, limites, transcrição preservada (leitura parcial) |
| Poda de sessão | https://docs.openclaw.ai/concepts/session-pruning | `agents.defaults.contextPruning.mode` (leitura parcial) |

> [!warning] Páginas não lidas na PARTE 4
> Não foi possível ler: `docs.openclaw.ai/concepts/model-providers`, `/concepts/recommended-models`, `/providers/openai` e `/providers/anthropic` (a versão em inglês; usado o espelho zh-CN), além de páginas de Slack, Signal e iMessage. As notas que dependem delas têm callouts de cobertura limitada.

## Fontes adicionadas na PARTE 5

| Fonte | URL | Usada para |
|---|---|---|
| Skills | https://docs.openclaw.ai/tools/skills | Pastas e precedência (leitura parcial) |
| Criar skills | https://docs.openclaw.ai/tools/creating-skills | Tutorial hello-world (publicação truncada) |
| Config de skills | https://docs.openclaw.ai/tools/skills-config | Chaves `skills.*` (leitura parcial) |
| Formato de skill no ClawHub | https://docs.openclaw.ai/clawhub/skill-format | Frontmatter e `requires` (limites truncados) |
| CLI skills | https://docs.openclaw.ai/cli/skills.md | Subcomandos de `openclaw skills` |
| Visão geral de ferramentas | https://docs.openclaw.ai/tools | Categorias (navegação) |
| Política de ferramentas | https://docs.openclaw.ai/gateway/config-tools/tool-policy | Perfis e grupos (leitura parcial) |
| Exec | https://docs.openclaw.ai/tools/exec | Parâmetros e hosts (leitura parcial) |
| Aprovações de exec | https://docs.openclaw.ai/tools/exec-approvals | Modelo de confiança e precedência (leitura parcial) |
| Modos de permissão | https://docs.openclaw.ai/tools/permission-modes | `tools.exec.mode` |
| MCP | https://docs.openclaw.ai/tools/mcp | Visão geral e runtime (leitura parcial) |
| CLI mcp (pt-BR) | https://docs.openclaw.ai/pt-BR/cli/mcp.md | Subcomandos e formato JSON |
| Navegador | https://docs.openclaw.ai/tools/browser | Perfis (índice) |
| Automações | https://docs.openclaw.ai/automation/cron-jobs | CLI e quick start |
| Agendamentos | https://docs.openclaw.ai/automation/cron-jobs/schedules | at, every, cron, fuso |
| Webhooks | https://docs.openclaw.ai/automation/cron-jobs/webhooks | `hooks.*`, `/hooks/agent` (leitura parcial) |
| Hooks | https://docs.openclaw.ai/automation/hooks | Hooks internos e CLI (leitura parcial) |
| Standing orders | https://docs.openclaw.ai/automation/standing-orders | Escopo, gatilhos, escalonamento |

> [!warning] Não confirmado na PARTE 5
> Instalação de skills por `install` no frontmatter, `security.installPolicy`, sintaxe de `tools.allow/deny`, `tools.byProvider`, `timeout/background/pty` de exec, formato do arquivo de aprovações, chaves `browser.*`, `/hooks/wake`, subcomandos `automations run/remove` e flags de `clawhub skill publish`. As notas sinalizam cada caso. A página `docs.openclaw.ai/clawhub/security-audits` foi bloqueada.

## Fontes adicionadas na PARTE 6

| Fonte | URL | Usada para |
|---|---|---|
| Instalação (índice) | https://docs.openclaw.ai/install/index.md | Métodos, Node, verificação, PATH |
| Docker | https://docs.openclaw.ai/install/docker.md | setup.sh, imagens, variáveis, health checks |
| Linux | https://docs.openclaw.ai/platforms/linux.md | systemd de usuário, timeouts, túnel SSH |
| VPS (pt-BR) | https://docs.openclaw.ai/pt-BR/vps.md | Provedores, loopback, endurecimento da unidade |
| macOS | https://docs.openclaw.ai/platforms/macos.md | App de menu, modos local e remoto |
| Windows | https://docs.openclaw.ai/platforms/windows.md | Hub, nativo, WSL2, Tarefa Agendada |
| Atualização | https://docs.openclaw.ai/install/updating | Rotina e tipos de instalação (leitura parcial) |
| CLI update | https://docs.openclaw.ai/cli/update.md | Subcomandos, flags e canais |
| Migração | https://docs.openclaw.ai/install/migrating | O que copiar e cuidados |
| Desinstalação | https://docs.openclaw.ai/install/uninstall | Escopos e remoção manual (leitura parcial) |
| CLI backup | https://docs.openclaw.ai/cli/backup.md | create, verify, restore, sqlite, git |
| Logging (ko) | https://docs.openclaw.ai/ko/logging.md | Arquivo, níveis, `openclaw logs`, redação |
| CLI doctor | https://docs.openclaw.ai/cli/doctor/running.md | Posturas, flags e códigos de saída |

> [!warning] Divergência de versão do Node (PARTE 6)
> `install/index.md` diz Node 24 recomendado ou 22.16+; `platforms/linux.md` diz Node 26 recomendado ou 24.22.1+/26.12.1+. As notas orientam usar o instalador oficial e confirmar `node -v` no dia. Também não confirmado: lingering no Linux (a doc de Linux não cobre), flags de rollback da página de atualização, comandos de remoção manual no Linux e no Windows, ordem de precedência entre `OPENCLAW_STATE_DIR` e perfis, e o rótulo do LaunchAgent (apenas citado na página de desinstalação).

## Fontes adicionadas na PARTE 7

| Fonte | URL | Usada para |
|---|---|---|
| Segurança do Gateway | https://docs.openclaw.ai/gateway/security.md | Modelo de confiança, padrões, incidentes (subpáginas não lidas) |
| Segurança (espelho hindi) | https://docs.openclaw.ai/hi/gateway/security.md | JSON da linha de base e chaves de DM e perigosas |
| CLI security | https://docs.openclaw.ai/cli/security.md | `security audit`, flags e `--fix` |
| Audit checks | https://docs.openclaw.ai/gateway/security/audit-checks | checkIds de runtime e permissões (leitura parcial) |
| Sandboxing (pt-BR) | https://docs.openclaw.ai/pt-BR/gateway/sandboxing.md | Modos, escopo, backends, binds |
| Segredos (espelho ar) | https://docs.openclaw.ai/ar/gateway/secrets.md | SecretRef, provedores, comandos |
| Modelo de ameaças, execução | https://docs.openclaw.ai/security/THREAT-MODEL-ATLAS/execution.md | T-EXEC-001 a 004 |
| Auditorias do ClawHub | https://docs.openclaw.ai/clawhub/security-audits | Estados e riscos (leitura parcial) |
| ClawHavoc (imprensa) | https://esecurityplanet.com/threats/hundreds-of-malicious-skills-found-in-openclaws-clawhub | Caso de cadeia de suprimentos (terceiro; 3 de fev. de 2026) |

> [!warning] Não confirmado na PARTE 7
> Subpágina "hardened baseline" em inglês (JSON tirado do espelho hindi), lista completa de `checkId` (só runtime e permissões de arquivos lidos), demais páginas do modelo ATLAS, detalhes de varredura do ClawHub (VirusTotal citado só pela imprensa), backend Podman do sandbox e formato por agente das políticas de ferramentas. As notas sinalizam cada caso e não inventam chaves.

## Fontes adicionadas na PARTE 8

| Fonte | URL | Usada para |
|---|---|---|
| Showcase (espelho hindi) | https://docs.openclaw.ai/hi/start/showcase.md | Categorias e exemplos de uso da comunidade |
| Receitas de automação (terceiro) | https://www.fast.io/resources/openclaw-automation-recipes.md | Briefing, triagem, alertas de CI (conteúdo de blog, não oficial) |
| OpenClaw vs Claude Code (terceiro) | https://www.fast.io/resources/openclaw-vs-claude-code.md | Tabela comparativa, **com viés comercial**; fatos separados de opinião na nota |
| Webhooks, hooks, cron, sandbox, MCP, backup | (ver Fontes das PARTES 5 a 7) | Projetos práticos |

> [!warning] Cuidados da PARTE 8
> Comparações de terceiros podem estar desatualizadas e são promocionais; as notas sinalizam o que não foi verificado (vulnerabilidade citada, contagem de instâncias expostas, plano de nuvem pago). Gatilhos Gmail Pub/Sub e a sintaxe exata de `automations create` com `--cron` não foram lidos em detalhe: os projetos mandam confirmar com `--help`.

## Fontes adicionadas na PARTE 9

| Fonte | URL | Usada para |
|---|---|---|
| Troubleshooting (espelho ar) | https://docs.openclaw.ai/ar/help/troubleshooting | Escada de 60 segundos e assinaturas de log |
| Troubleshooting de canais | https://docs.openclaw.ai/channels/troubleshooting.md | Falhas por canal, pós-atualização, disjuntor de crash loop |
| Fontes das PARTES 1 a 8 | (ver seções anteriores) | FAQ, glossário, cheatsheets e flashcards |

> [!warning] Cuidados da PARTE 9
> O Glossário, os Cheatsheets e os Flashcards resumem conteúdo já referenciado nas outras notas; a doc muda a cada release. Confirme comandos com `--help` e valide versões antes de aplicar. Nenhuma flag foi inventada: onde a sintaxe não foi confirmada, as notas sinalizam.

## Relacionados

- [[Home - OpenClaw]]
- [[Trilha de aprendizado - OpenClaw]]
