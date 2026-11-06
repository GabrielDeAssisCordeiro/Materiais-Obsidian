---
titulo: "Licença MIT e OpenClaw Foundation"
tags:
  - openclaw
  - conceito
  - historia
tipo: conceito
aliases: ['MIT', 'OpenClaw Foundation']
nivel: iniciante
fontes:
  - "[[Fontes]]"
  - "https://docs.openclaw.ai/"
  - "https://steipete.me/posts/2026/openclaw"
  - "https://horadecodar.com.br/openclaw-github/"
  - "https://www.storyboard18.com/digital/clawdbot-becomes-openclaw-after-trademark-checks-as-open-source-ai-project-evolves-88639.htm"
relacionados:
  - "[[O que é o OpenClaw]]"
  - "[[Linha do tempo Clawdbot, Moltbot e OpenClaw]]"
  - "[[ClawHub, plugins e o ecossistema]]"
  - "[[Crescimento da comunidade e ritmo de releases]]"
---

# Licença MIT e OpenClaw Foundation

## Objetivo

Entender o que a licença MIT permite, quem mantém o projeto e o que isso significa para quem usa em casa ou na empresa.

## Explicação

**Licença MIT.** A página inicial da documentação descreve o OpenClaw como "MIT licensed". O repositório `openclaw/openclaw` também é relatado como MIT por guias de terceiros. A MIT é uma licença permissiva. Em termos gerais, ela permite usar, copiar, modificar, mesclar, publicar e distribuir o software, inclusive em produtos comerciais, desde que se mantenha o aviso de copyright e a licença nas cópias. Ela não oferece garantia: o software é fornecido "como está".

> [!info] Isto não é aconselhamento jurídico
> Para uso corporativo, confirme o texto da licença no arquivo `LICENSE` do repositório e consulte quem cuida de conformidade na sua organização. Plugins e skills de terceiros podem ter licenças próprias.

**Governança.** O rodapé da documentação descreve o projeto como "An OpenClaw Foundation project", e a página inicial o descreve como desenvolvido em aberto pela OpenClaw Foundation, uma entidade 501(c)(3) independente, sem plano pago e sem telemetria por padrão além de uma verificação de versão que pode ser desligada. Em 14/02/2026, Peter Steinberger escreveu que o projeto migraria para uma fundação, permaneceria aberto e independente, e que a OpenAI já patrocinava o projeto e o deixaria dedicar tempo a ele. Reportagens também mencionam patrocínios em níveis com nomes temáticos de lagosta.

**O que isso significa na prática.**

| Pergunta | Resposta curta |
|---|---|
| Posso usar em casa? | Sim |
| Posso usar na empresa? | Em geral sim; confirme a licença e as dos plugins |
| Existe versão paga oficial? | A documentação afirma que não há plano pago |
| Há coleta de dados? | Sem telemetria por padrão além de uma verificação de versão desligável |
| Quem decide o rumo? | A fundação e a comunidade, de forma aberta |

## Exemplo prático

Para entender a telemetria na sua instalação, leia a página oficial `docs.openclaw.ai/gateway/telemetry` e, ao instalar, confira o que o onboarding pergunta. Registre sua decisão no seu inventário de segurança.

```markdown
- Verificação de versão: [ligada | desligada]  (ver doc de telemetria)
- Licença conferida em LICENSE: [data]
- Plugins de terceiros com licença própria: [lista]
```

## Armadilhas comuns

- Presumir que "open source" significa "auditado". Código aberto permite auditar, mas não garante que alguém tenha feito isso.
- Esquecer que skills e plugins de terceiros não herdam a segurança do núcleo; veja [[ClawHub, plugins e o ecossistema]].
- Confundir fundação com empresa: não há um fornecedor com contrato de suporte padrão.

## Resumo

- MIT: permissiva, sem garantia.
- OpenClaw Foundation: entidade 501(c)(3) independente, segundo a doc.
- Sem plano pago e sem telemetria por padrão além de verificação de versão desligável.
- Plugins e skills podem ter outras licenças.

## Relacionados

- [[O que é o OpenClaw]]
- [[Linha do tempo Clawdbot, Moltbot e OpenClaw]]
- [[ClawHub, plugins e o ecossistema]]
- [[Crescimento da comunidade e ritmo de releases]]

## Exercícios

1. O que a licença MIT permite e o que ela exige?
2. Quem é descrito como mantenedor do projeto na documentação?
3. Por que "código aberto" não é sinônimo de "seguro"?
4. Onde você verifica o que a telemetria coleta?
