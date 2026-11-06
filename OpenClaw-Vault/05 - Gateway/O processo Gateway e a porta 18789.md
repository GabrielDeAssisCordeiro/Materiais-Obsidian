---
titulo: "O processo Gateway e a porta 18789"
tags:
  - openclaw
  - conceito
  - gateway
tipo: conceito
aliases: ['Gateway', 'Porta padrão']
nivel: intermediario
fontes:
  - "[[Fontes]]"
  - "https://docs.openclaw.ai/concepts/architecture"
  - "https://docs.openclaw.ai/gateway/remote"
  - "https://docs.openclaw.ai/pt-BR/cli/daemon.md"
relacionados:
  - "[[Arquitetura em camadas do OpenClaw]]"
  - "[[O Gateway como serviço em segundo plano]]"
  - "[[O protocolo WebSocket do Gateway]]"
  - "[[Acesso remoto - SSH, Tailscale e modos de bind]]"
---

# O processo Gateway e a porta 18789

## Objetivo

Entender o que é o processo Gateway, onde ele escuta por padrão e como verificar que está saudável.

## Explicação

O Gateway é um **único processo de longa duração** que é dono de todas as superfícies de mensagens. Segundo a página de arquitetura:

- escuta, por padrão, em `127.0.0.1:18789`, ou seja, **somente na própria máquina** (loopback);
- a documentação de acesso remoto reforça que o WebSocket liga em loopback na porta 18789 (chave `gateway.port`) e que o uso remoto exige expô-lo de forma deliberada;
- **roda um Gateway por host**, e ele é o único componente que abre a sessão do WhatsApp;
- serve o painel web (Control UI) e a superfície de widgets na **mesma porta**, por HTTP, além da API WebSocket.

Dentro do Gateway vivem os adaptadores de canal, a API tipada, a resolução de sessões e o roteamento, e a fila de execuções. O runtime do agente é chamado por ele, como em [[O caminho de uma mensagem do chat à resposta]].

**Verificações de saúde.** A documentação e o `skill.md` oficial listam comandos para ver o estado:

```bash
openclaw gateway status
openclaw status
openclaw health
```

O `status` do Gateway mostra o estado de instalação do serviço (launchd, systemd ou schtasks) e checa a saúde. Com `--deep`, ele também procura **outros serviços parecidos com um Gateway** na máquina, já que a recomendação é ter um só.

> [!info] Mais de um Gateway
> A documentação prevê vários Gateways no mesmo host apenas com isolamento de portas, de configuração e estado e de workspaces. Se você não precisa disso, mantenha um só.

## Exemplo prático

Confirme que a porta está em loopback e não exposta à rede:

```bash
ss -ltnp | grep 18789
```

Você deve ver o endereço `127.0.0.1:18789`. Se aparecer `0.0.0.0:18789` ou o IP da sua rede, algo configurou outro modo de bind; revise [[Acesso remoto - SSH, Tailscale e modos de bind]] antes de seguir.

(O comando `ss` é do Linux; no macOS use `lsof -iTCP:18789 -sTCP:LISTEN`.)

## Armadilhas comuns

- Abrir a porta 18789 no firewall "para facilitar". O padrão em loopback existe por segurança.
- Rodar o Gateway em primeiro plano em um terminal e achar que continua após fechá-lo; veja [[O Gateway como serviço em segundo plano]].
- Ter dois Gateways disputando as mesmas portas e a mesma pasta de estado.

## Resumo

- Um Gateway por host, em `127.0.0.1:18789` por padrão.
- Serve WebSocket, Control UI e widgets na mesma porta.
- `openclaw gateway status`, `openclaw status` e `openclaw health` verificam o estado.

## Relacionados

- [[O protocolo WebSocket do Gateway]]
- [[O Gateway como serviço em segundo plano]]
- [[Control UI e dashboard]]
- [[Acesso remoto - SSH, Tailscale e modos de bind]]

## Exercícios

1. Em que endereço e porta o Gateway escuta por padrão?
2. Quantos Gateways a documentação recomenda por host?
3. O que `openclaw gateway status --deep` faz a mais?
4. Como você confirma que a porta não está exposta à rede?
