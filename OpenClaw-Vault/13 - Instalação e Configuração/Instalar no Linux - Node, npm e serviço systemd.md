---
titulo: "Instalar no Linux - Node, npm e serviço systemd"
tags:
  - openclaw
  - conceito
  - instalacao
tipo: conceito
aliases: ['systemd user service']
nivel: intermediario
fontes:
  - "[[Fontes]]"
  - "https://docs.openclaw.ai/platforms/linux.md"
relacionados:
  - "[[Requisitos e escolha do método de instalação]]"
  - "[[O Gateway como serviço em segundo plano]]"
  - "[[Acesso remoto - SSH, Tailscale e modos de bind]]"
  - "[[Hospedar o OpenClaw em um VPS com acesso seguro]]"
---

# Instalar no Linux - Node, npm e serviço systemd

## Objetivo

Instalar o Gateway num Linux (desktop ou servidor), registrá-lo como serviço de usuário do systemd e acessá-lo com segurança por túnel SSH.

## Explicação

O Gateway tem suporte completo no Linux. **Node é o runtime padrão e recomendado**; Bun 1.4.4+ é opt-in explícito e `pnpm` é indicado para instalar dependências.

### Caminho rápido (servidor sem tela)

1. Instalar Node (a página recomenda Node 26, ou 24.22.1+ / 26.12.1+).
2. Instalar o OpenClaw.
3. `openclaw onboard --install-daemon`.
4. Abrir um túnel SSH a partir do laptop.
5. Abrir `http://127.0.0.1:18789/` e autenticar com o segredo compartilhado (token por padrão, ou senha se `gateway.auth.mode` for `"password"`).

### Serviço systemd de usuário

`openclaw gateway install` cria por padrão uma unidade de usuário em `~/.config/systemd/user/openclaw-gateway[-<perfil>].service`. O exemplo da doc usa `Restart=always`, `RestartSec=5`, `TimeoutStopSec=330` (para a drenagem de cinco minutos), `OOMPolicy=continue` e `KillMode=mixed`. Unidades escritas à mão **não** recebem o dimensionamento adaptativo de heap do instalador gerenciado.

> [!warning] Lingering
> A página não trata de `loginctl enable-linger`. Sem lingering, serviços de usuário podem parar ao encerrar a sessão; confirme no runbook do Gateway ou na documentação da sua distribuição.

### Tempo de parada do systemd

O gerenciador de usuário (`user@<uid>.service`) pode cortar a drenagem do Gateway. A doc manda checar `TimeoutStopUSec` e, se for menor que 90 s, criar um *drop-in* com `TimeoutStopSec=90` (ou `330`). Doctor e `gateway status` avisam se estiver abaixo de 90 s.

## Exemplo prático

```bash
node -v
npm i -g openclaw@latest --allow-scripts=openclaw   # npm 12 ou 11.16+
# npm 11.15 ou anterior: npm i -g openclaw@latest
openclaw onboard --install-daemon
systemctl --user enable --now openclaw-gateway.service
systemctl --user cat openclaw-gateway.service
openclaw gateway status --deep
```

No laptop, o túnel:

```bash
ssh -N -L 18789:127.0.0.1:18789 usuario@meu-servidor
```

Verificar o tempo de parada:

```bash
systemctl show user@$(id -u).service -p TimeoutStopUSec
```

```mermaid
flowchart LR
  L[Laptop] -- ssh -N -L 18789 --> S[Servidor Linux]
  S --> G[Gateway em 127.0.0.1:18789]
  G --> U[systemd user unit com Restart=always]
```

## Armadilhas comuns

- Expor a 18789 em `0.0.0.0` sem autenticação (o Gateway recusa bind fora do loopback sem auth).
- Matar o processo com `kill` em vez de `openclaw gateway restart`.
- Ignorar mortes por OOM (`exit 137`): aumente a memória ou use `MemoryMax=`.
- Esquecer lingering em servidor e perder o serviço ao sair do SSH.

## Resumo

- Node + `onboard --install-daemon` + unidade systemd de usuário.
- Acesso por túnel SSH ao loopback.
- Cuidado com lingering, OOM e timeout de parada.

## Relacionados

- [[Requisitos e escolha do método de instalação]]
- [[O Gateway como serviço em segundo plano]]
- [[Acesso remoto - SSH, Tailscale e modos de bind]]
- [[Hospedar o OpenClaw em um VPS com acesso seguro]]
- [[Escada de diagnóstico do Gateway - status, logs e doctor]]

## Exercícios

1. Onde fica a unidade systemd criada por `openclaw gateway install`?
2. Como acessar o painel de um servidor sem abrir a porta para a internet?
3. Por que `TimeoutStopSec` importa para o Gateway?
4. O que a nota sinaliza como não confirmado sobre lingering?
