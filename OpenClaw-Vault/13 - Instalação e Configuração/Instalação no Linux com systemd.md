---
titulo: "Instalação no Linux com systemd"
tags:
  - openclaw
  - conceito
  - instalacao
tipo: conceito
aliases: ['Serviço de usuário systemd']
nivel: intermediario
fontes:
  - "[[Fontes]]"
  - "https://docs.openclaw.ai/platforms/linux.md"
  - "https://docs.openclaw.ai/install/index.md"
relacionados:
  - "[[Requisitos e escolha do método de instalação]]"
  - "[[O Gateway como serviço em segundo plano]]"
  - "[[Acesso remoto - SSH, Tailscale e modos de bind]]"
  - "[[Hospedar em um VPS com segurança]]"
---

# Instalação no Linux com systemd

## Objetivo

Instalar o Gateway em Linux, registrá-lo como serviço de usuário do systemd e acessá-lo com segurança a partir de outra máquina.

## Explicação

O Gateway tem suporte completo em Linux; o Node é o runtime recomendado (a página sugere `pnpm` em vez de Bun). Passos da doc:

1. Instalar Node (versão: veja o aviso na nota [[Requisitos e escolha do método de instalação]]).
2. Instalar o pacote global.
3. Rodar o onboarding com o daemon.

O serviço padrão é uma **unidade de usuário** do systemd (`openclaw-gateway.service`, ou `openclaw-gateway-<perfil>.service`). Existe também uma unidade de sistema no runbook do Gateway. Três formas de instalar o serviço: `openclaw onboard --install-daemon`, `openclaw gateway install` ou `openclaw configure` (opção "Gateway service"). Reparar ou migrar: `openclaw doctor`.

> [!info] Unidades escritas à mão
> A doc avisa que unidades feitas à mão **não recebem** o ajuste adaptativo de heap do instalador gerenciado. Prefira o instalador.

### Tempo de parada

A unidade gerenciada usa `TimeoutStopSec=330` para o dreno de cinco minutos do Gateway. O desligamento do host também para `user@<uid>.service`, cujo timeout padrão pode cortar o dreno (no Ubuntu 24.04 é de 5 segundos). O doctor e o status avisam quando está abaixo de 90 segundos.

## Exemplo prático

```bash
npm i -g openclaw@latest --allow-scripts=openclaw   # ver nota de versao do npm abaixo
openclaw onboard --install-daemon
systemctl --user enable --now openclaw-gateway.service
systemctl --user cat openclaw-gateway.service
openclaw gateway status --deep
```

> [!warning] Flag do npm
> A doc inclui `--allow-scripts=openclaw` para npm 12 ou npm 11.16+, e manda omitir em npm 11.15 ou anterior. Confirme sua versão com `npm -v`.

Verificar e elevar o timeout de parada:

```bash
systemctl show user@$(id -u).service -p TimeoutStopUSec
sudo mkdir -p /etc/systemd/system/user@$(id -u).service.d
printf '[Service]\nTimeoutStopSec=90\n' | sudo tee /etc/systemd/system/user@$(id -u).service.d/zz-openclaw-stop-timeout.conf
sudo systemctl daemon-reload
```

Acesso remoto recomendado para hosts sem tela, via túnel SSH:

```bash
ssh -N -L 18789:127.0.0.1:18789 usuario@servidor
# depois abra http://127.0.0.1:18789/
```

```mermaid
flowchart LR
  L[Laptop] -- ssh -L 18789 --> S[Servidor Linux]
  S --> U[systemd user: openclaw-gateway.service]
  U --> G[Gateway em loopback]
```

> [!warning] Lingering
> A página não cobre `loginctl enable-linger`. Sem ele, serviços de usuário podem parar quando a sessão encerra; a página do Windows/WSL2 usa `sudo loginctl enable-linger "$(whoami)"`. Verifique no seu servidor com `loginctl show-user $(whoami) -p Linger`.

## Armadilhas comuns

- Expor a porta 18789 na internet em vez de túnel SSH ou Tailscale.
- Usar HTTP/`ws://` fora de loopback, rede privada ou Tailnet; a doc pede HTTPS/`wss://` em hosts públicos.
- Hosts sem gerenciador de serviço suportado: o `status --deep` reporta; rode em primeiro plano ou sob seu supervisor.
- Mortes por falta de memória (`exit 137`) em VMs pequenas.

## Resumo

- Unidade de usuário `openclaw-gateway.service`, criada pelo onboarding.
- Túnel SSH para acesso remoto; nada de porta pública.
- Ajuste `TimeoutStopSec` do `user@<uid>.service`.

## Relacionados

- [[O Gateway como serviço em segundo plano]]
- [[Acesso remoto - SSH, Tailscale e modos de bind]]
- [[Hospedar em um VPS com segurança]]
- [[Requisitos e escolha do método de instalação]]
- [[Onboarding e verificação pós-instalação]]

## Exercícios

1. Qual o nome padrão da unidade systemd do Gateway?
2. Por que `TimeoutStopSec=330` existe?
3. Qual a forma recomendada de acessar o dashboard de um servidor sem tela?
4. O que o lingering resolve e por que a doc de Linux não o cobre?
