---
titulo: "Tour rápido de instalação e primeira conversa"
tags:
  - openclaw
  - conceito
  - visao-geral
tipo: conceito
aliases: ['Quick start']
nivel: iniciante
fontes:
  - "[[Fontes]]"
  - "https://docs.openclaw.ai/start/getting-started"
  - "https://docs.openclaw.ai/"
  - "https://docs.openclaw.ai/skill.md"
relacionados:
  - "[[O que é o OpenClaw]]"
  - "[[Para quem é o OpenClaw e o que ele exige]]"
  - "[[Principais capacidades do OpenClaw]]"
  - "[[O OpenClaw versus um chatbot]]"
---

# Tour rápido de instalação e primeira conversa

## Objetivo

Percorrer, só como panorama, o caminho oficial de instalação até a primeira mensagem. Os detalhes por sistema ficam na pasta [[MOC - Instalação e Configuração - OpenClaw|Instalação e Configuração]].

## Explicação

O caminho oficial tem quatro etapas: instalar, fazer o onboarding, instalar o serviço do Gateway e conversar.

```mermaid
flowchart LR
  A["Instalar"] --> B["Onboarding"]
  B --> C["Gateway em primeiro plano"]
  C --> D["openclaw gateway install"]
  D --> E["Conversar"]
```

**1. Instalar.** O instalador detecta o sistema, instala o Node se necessário, instala o OpenClaw e inicia o onboarding.

```bash
curl -fsSL https://openclaw.ai/install.sh | bash
```

No Windows (PowerShell), a documentação indica:

```powershell
iwr -useb https://openclaw.ai/install.ps1 | iex
```

Há também o caminho por npm e a opção de testar com um comando só:

```bash
npm install -g openclaw@latest
npx openclaw@latest
```

**2. Onboarding.** Há duas rotas: **Quick start**, que reaproveita o acesso de IA detectado, verifica com uma chamada real e abre o painel; e **Custom setup**, o fluxo guiado completo. O assistente clássico abre com:

```bash
openclaw onboard --classic
```

**3. Serviço do Gateway.** O Quick start deixa o Gateway em primeiro plano. Para mantê-lo em segundo plano, pare com Ctrl+C e instale o serviço:

```bash
openclaw gateway install
openclaw gateway status
```

**4. Conversar.** Abra o painel web:

```bash
openclaw dashboard
```

Para ajustes posteriores, use `openclaw configure`.

> [!warning] Cuidado com scripts por pipe
> Executar `curl ... | bash` roda código remoto sem revisão. Em ambientes sensíveis, baixe o script, leia-o e só então execute, e confirme que o domínio é exatamente `openclaw.ai`. Veja [[Nomes antigos, domínios falsos e como verificar a fonte]].

## Exemplo prático

Em uma VM de teste: instale, escolha **Quick start**, abra `openclaw dashboard`, envie "olá" e confirme a resposta. Depois rode `openclaw gateway status` e confira que o serviço está ativo.

## Armadilhas comuns

- Fechar o terminal e achar que o Gateway segue rodando: no Quick start ele fica em primeiro plano.
- Usar o comando de um tutorial antigo. Confirme na documentação, pois o projeto evolui rápido.
- Pular a leitura do guia de segurança que o onboarding indica.

## Resumo

- Quatro etapas: instalar, onboarding, serviço do Gateway, conversar.
- Comandos-chave: `openclaw onboard`, `openclaw gateway install`, `openclaw gateway status`, `openclaw dashboard`, `openclaw configure`.
- Teste em ambiente isolado e confira a origem do script.

## Relacionados

- [[Para quem é o OpenClaw e o que ele exige]]
- [[Principais capacidades do OpenClaw]]
- [[O que é o OpenClaw]]
- [[MOC - Gateway|Gateway]]

## Exercícios

1. Quais são as duas rotas de onboarding?
2. Qual comando instala o Gateway como serviço em segundo plano?
3. Como você abre a Control UI?
4. Por que revisar um script antes de executá-lo por pipe?
