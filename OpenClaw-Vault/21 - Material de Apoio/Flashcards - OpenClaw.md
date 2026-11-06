---
titulo: "Flashcards - OpenClaw"
tags:
  - openclaw
  - revisao
tipo: revisao
aliases: []
nivel: iniciante
fontes:
  - "[[Fontes]]"
  - "https://docs.openclaw.ai/"
relacionados:
  - "[[Glossário#OpenClaw]]"
  - "[[Cheatsheets]]"
  - "[[Home - OpenClaw]]"
---

# Flashcards - OpenClaw

## Objetivo

Praticar a revisão espaçada dos conceitos mais importantes do vault, no formato de cartões simples (`pergunta::resposta`), compatível com o plugin de repetição espaçada do Obsidian.

## Explicação

Cada linha abaixo é um cartão de uma linha. Em plugins de repetição espaçada, o separador `::` define frente e verso. Sem plugin, use como lista de autoteste: cubra a resposta, responda em voz alta e confira.

Porta e endereço padrão do Gateway?::`127.0.0.1:18789` (loopback).
Arquivo de configuração principal?::`~/.openclaw/openclaw.json` (JSON5, esquema estrito).
Diferença entre skill e plugin?::Skill é texto (`SKILL.md`) que orienta o agente; plugin é código que adiciona capacidades.
Valores de `dmPolicy`?::`pairing`, `allowlist`, `open`, `disabled`.
Perfis de `tools.profile`?::`minimal`, `coding`, `messaging`, `full`.
Modos de `tools.exec.mode`?::`deny`, `allowlist`, `ask`, `auto`, `full`.
O que o sandbox NÃO isola?::O processo do Gateway e o que passa por `tools.elevated`.
Padrão do sandbox?::Desligado (`mode: off`).
Formato de um SecretRef?::`{ source: env|file|exec, provider, id }`.
O que o `security audit --fix` NÃO faz?::Não rotaciona segredos, não muda bind/auth, não remove skills ou plugins.
Regra de ouro contra injeção de prompt?::Não combine entrada não confiável, dados privados e capacidade de agir no mesmo agente.
Fases de resposta a incidentes da doc?::Conter, Rotacionar, Auditar, Coletar.
Comando que valida a configuração?::`openclaw config validate`.
Como listar pareamentos pendentes?::`openclaw pairing list <canal>`.
O que `200` em `/hooks/agent` significa?::Run admitido; não significa concluído nem entregue.
Fuso de `--at` sem offset?::UTC.
O que `update --yes` NÃO concede?::Aprovação de exec nem aceitação de mudança de capacidades de plugin.
Endpoints de saúde do Gateway?::`/healthz`, `/startupz`, `/readyz`.
O que o backup completo contém de sensível?::Credenciais e perfis de autenticação: proteja o arquivo.
Restaurar um backup é...?::Um rollback: pode exigir relinkar canais e atualizar plugins.
Por que a URL do Ollama não leva `/v1`?::O `baseUrl` nativo é sem `/v1`; apontar para `/v1` é erro documentado.
Diferença entre compactação e poda?::Compactação resume turnos antigos; poda apara resultados de ferramentas.
Um Gateway, quantas fronteiras de confiança?::Uma.
Qual o risco do perfil `user` do navegador?::Anexa à sua sessão real logada; o agente age como você.
Sinal de alerta num SKILL.md?::Exige baixar/rodar instalador externo ou colar comando codificado.
Escada de diagnóstico: primeiro comando?::`openclaw status`.
Padrão de bind em instalação normal?::Loopback.
Qual o alias de `openclaw automations`?::`openclaw cron`.
Onde ficam standing orders?::Em `AGENTS.md` (ou arquivo referenciado por ele).
O que é ClawHavoc?::Campanha de skills maliciosas no ClawHub, relatada em 2026; contagens variam por fonte.

## Exemplo prático

Sessão de 10 minutos: 15 cartões; marque os que errou e releia as notas relacionadas (veja o [[Glossário#OpenClaw]]). Repita em 1, 3 e 7 dias.

## Armadilhas comuns

- Ler as respostas sem tentar lembrar antes.
- Decorar sem entender: abra a nota de origem nos cartões que errar.
- Não atualizar os cartões quando a doc mudar (veja [[Fontes]]).

## Resumo

- 30 cartões nos tópicos de arquitetura, segurança, operação e automação.
- Revisão espaçada em 1, 3 e 7 dias.

## Relacionados

- [[Glossário#OpenClaw]]
- [[Cheatsheets]]
- [[Home - OpenClaw]]

## Exercícios

1. Escreva três cartões novos sobre skills.
2. Qual a vantagem de testar-se antes de reler?
3. Como você revisaria cartões que errou duas vezes?
