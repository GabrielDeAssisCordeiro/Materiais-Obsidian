---
titulo: "Para quem é o OpenClaw e o que ele exige"
tags:
  - openclaw
  - conceito
  - visao-geral
tipo: conceito
aliases: ['Público-alvo']
nivel: iniciante
fontes:
  - "[[Fontes]]"
  - "https://docs.openclaw.ai/"
  - "https://docs.openclaw.ai/start/getting-started"
  - "https://github.com/openclaw/openclaw/blob/main/docs/start/getting-started.md"
  - "https://docs.openclaw.ai/skill.md"
relacionados:
  - "[[O que é o OpenClaw]]"
  - "[[Principais capacidades do OpenClaw]]"
  - "[[Tour rápido de instalação e primeira conversa]]"
  - "[[Fontes]]"
---

# Para quem é o OpenClaw e o que ele exige

## Objetivo

Decidir se o OpenClaw serve ao seu perfil e listar o que você precisa preparar antes de instalar.

## Explicação

A documentação descreve o público como **desenvolvedores, usuários avançados e equipes** que querem um assistente acessível de qualquer lugar, sem abrir mão do controle dos dados e sem depender de um serviço hospedado. O mesmo Gateway serve a um uso pessoal em um laptop ou a uma implantação compartilhada por uma equipe; a diferença é a configuração.

O que você precisa:

1. **Node.js**. A documentação atual recomenda Node 26 e aceita outras versões suportadas.
2. **Acesso a um modelo**: uma chave de API de um provedor, ou um login já existente do Claude Code ou do Codex CLI, que o onboarding pode reaproveitar.
3. **Uma máquina que fique ligada**, se você quer o assistente sempre disponível: um servidor, uma VPS, um Raspberry Pi ou um computador dedicado. Há páginas oficiais de instalação para Docker, Linux server, Raspberry Pi e vários provedores de nuvem.
4. **Cerca de 5 minutos** para o caminho rápido de instalação.

> [!warning] Versão do Node diverge entre páginas
> A página inicial atual cita Node 26 (recomendado) e as versões 24.22.1+ ou 26.12.1+. Uma cópia mais antiga da página Getting started no GitHub cita 24.16+ ou 26.1+, e o arquivo `skill.md` cita Node 24 (ou 22.14+). Confirme sempre em `docs.openclaw.ai/install/node` e verifique a sua versão com:

```bash
node --version
```

Para melhor qualidade e segurança, a documentação aconselha usar o modelo mais forte e recente disponível. Modelos fracos tendem a seguir instruções maliciosas com mais facilidade, ponto aprofundado em [[MOC - Ameaças e Riscos|Ameaças e Riscos]].

## Exemplo prático

Checklist antes de instalar:

```markdown
- [ ] Node instalado e versão conferida na doc
- [ ] Chave de API (ou login do Claude Code / Codex CLI)
- [ ] Máquina de teste isolada (VM, container ou usuário dedicado)
- [ ] Conta de chat de teste (não a sua conta principal)
```

## Armadilhas comuns

- Instalar na máquina pessoal principal, cheia de chaves SSH e tokens, antes de entender as permissões.
- Ignorar o requisito de versão do Node e depurar erros que são só incompatibilidade.
- Escolher o modelo mais barato para tudo e depois estranhar respostas ruins; custo e qualidade são tratados em [[MOC - Provedores e Modelos|Provedores e Modelos]].

## Resumo

- Público: desenvolvedores, usuários avançados e equipes.
- Requisitos: Node (confirmar versão), acesso a modelo, máquina disponível.
- Teste primeiro em ambiente isolado.
- As páginas oficiais divergem sobre o Node; confirme na doc.

## Relacionados

- [[O que é o OpenClaw]]
- [[Principais capacidades do OpenClaw]]
- [[Tour rápido de instalação e primeira conversa]]
- [[MOC - Instalação e Configuração - OpenClaw|Instalação e Configuração]]

## Exercícios

1. Que tipo de pessoa a documentação indica como público do OpenClaw?
2. Quais são os três requisitos principais antes de instalar?
3. Por que não é boa ideia testar na máquina pessoal principal?
4. Como você confirma a versão do Node instalada?
