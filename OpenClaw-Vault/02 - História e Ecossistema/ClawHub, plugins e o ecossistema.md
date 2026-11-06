---
titulo: "ClawHub, plugins e o ecossistema"
tags:
  - openclaw
  - conceito
  - historia
tipo: conceito
aliases: ['ClawHub', 'Ecossistema OpenClaw']
nivel: intermediario
fontes:
  - "[[Fontes]]"
  - "https://docs.openclaw.ai/clawhub/how-it-works"
  - "https://docs.openclaw.ai/"
  - "https://horadecodar.com.br/openclaw-github/"
relacionados:
  - "[[Licença MIT e OpenClaw Foundation]]"
  - "[[Nomes antigos, domínios falsos e como verificar a fonte]]"
  - "[[Crescimento da comunidade e ritmo de releases]]"
  - "[[O que é o OpenClaw]]"
---

# ClawHub, plugins e o ecossistema

## Objetivo

Conhecer as peças do ecossistema (repositórios, ClawHub, plugins) e saber como instalar extensões sem abrir mão da cautela.

## Explicação

**Repositórios.** Guias descrevem a organização `openclaw` no GitHub com repositórios como `openclaw/openclaw` (código e documentação em `docs/`), `openclaw/docs`, `openclaw/clawhub`, `openclaw/rfcs` e `openclaw/openclaw.ai` (site). A fonte de verdade da documentação fica no repositório principal e é publicada em `docs.openclaw.ai`.

**ClawHub.** É a camada de registro de **skills e plugins**: permite descobrir pacotes, publicar versões e fornece os metadados necessários para instalar e atualizar. Cada listagem traz dono, nome, versões, metadados, arquivos, changelog, tags (como `latest`), sinais de instalação e estrelas, além de **status de varredura de segurança e moderação**. A listagem é o lugar canônico para inspecionar um pacote antes de instalar.

- **Skills** são pacotes de texto versionados centrados em um `SKILL.md`, com arquivos de apoio, exemplos e scripts.
- **Plugins** são extensões empacotadas do OpenClaw (canais, provedores, ferramentas), com metadados de compatibilidade.
- Publicar cria uma **versão imutável**.

**Plugins no núcleo e fora dele.** A documentação separa canais do núcleo de plugins oficiais instalados sob demanda, e mantém páginas de plugins da comunidade, do SDK de plugins e de ganchos (hooks).

**Ferramentas de terceiros.** Há um mercado de guias e plugins de hardening feitos por empresas de segurança. Trate-os como material de terceiros: leia o código e as permissões antes de instalar, como qualquer outra extensão.

## Exemplo prático

Comandos da documentação para instalar um skill e um plugin pelo registro, e para publicar:

```bash
openclaw skills install @openclaw/demo
openclaw plugins install clawhub:<pacote>
openclaw plugins install npm:<pacote>
clawhub skill publish ./minha-skill
```

Nas versões lançadas até a `2026.10.4`, a documentação pede o prefixo `clawhub:` para plugins. Builds mais novos podem aceitar nomes sem prefixo. Use `--dry-run` ao publicar pacotes para ver o payload antes do envio.

> [!warning] Inspecione antes de instalar
> Leia a listagem do pacote: dono, histórico, status de varredura e o que o `SKILL.md` declara. A documentação lembra que os metadados precisam ser precisos, porque as varreduras automáticas podem sinalizar diferenças entre o declarado e o observado. A auditoria completa é o tema da pasta [[MOC - Skills|Skills]].

## Armadilhas comuns

- Instalar uma skill só pelo nome parecido com o de outra famosa (typosquatting).
- Confiar cegamente na varredura: ela reduz risco, não o elimina.
- Esquecer que skills podem incluir scripts executáveis.

## Resumo

- ClawHub é o registro de skills e plugins, com versões imutáveis e status de varredura.
- Instalação por `openclaw skills install` e `openclaw plugins install clawhub:<pacote>`.
- Inspecione listagem, dono e conteúdo antes de instalar.
- Ferramentas de segurança de terceiros também exigem revisão.

## Relacionados

- [[Licença MIT e OpenClaw Foundation]]
- [[Nomes antigos, domínios falsos e como verificar a fonte]]
- [[Crescimento da comunidade e ritmo de releases]]
- [[MOC - Skills|Skills]]
- [[MOC - Ameaças e Riscos|Ameaças e Riscos]]

## Exercícios

1. O que é o ClawHub e o que cada listagem mostra?
2. Qual a diferença entre skill e plugin?
3. Por que publicar cria versões imutáveis?
4. Cite três verificações a fazer antes de instalar uma skill.
