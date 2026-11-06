---
titulo: "Control UI e dashboard"
tags:
  - openclaw
  - conceito
  - gateway
tipo: conceito
aliases: ['Control UI', 'Painel web', 'Dashboard']
nivel: iniciante
fontes:
  - "[[Fontes]]"
  - "https://docs.openclaw.ai/web/control-ui"
  - "https://docs.openclaw.ai/start/getting-started"
  - "https://docs.openclaw.ai/"
relacionados:
  - "[[O processo Gateway e a porta 18789]]"
  - "[[Configuração do Gateway em openclaw.json]]"
  - "[[Acesso remoto - SSH, Tailscale e modos de bind]]"
  - "[[Gateway, clientes e nodes]]"
---

# Control UI e dashboard

## Objetivo

Usar o painel web do Gateway para conversar, ver atividade e editar configuração, sabendo como ele é servido e protegido.

## Explicação

A Control UI é um **aplicativo de página única pequeno (Vite + Solid) servido pelo próprio Gateway**. Ela fala diretamente com o WebSocket do Gateway, na mesma porta. As áreas citadas são chat, atividade, nodes e configuração; a documentação tem páginas dedicadas a conexão e pareamento, sessões e barra lateral, chat, painéis, configurações, referência de recursos e RPC, comportamento offline e modelo de segurança.

**Como abrir.** Com o Gateway no ar:

```bash
openclaw dashboard
```

O endereço padrão é `http://<host>:18789/`; localmente, `http://127.0.0.1:18789/`.

**Opções de configuração citadas:**

| Chave | Efeito |
|---|---|
| `gateway.controlUi.enabled` | Liga ou desliga a UI; vale sem reinício. Desligar para de servir páginas e assets, mas bots e conexões existentes continuam |
| `gateway.controlUi.basePath` | Prefixo de caminho (por exemplo `/openclaw`); mudar exige reinício do Gateway |
| `gateway.controlUi.allowedOrigins` | Origens permitidas para acesso público ou entre origens |
| `gateway.controlUi.root` | Pasta de assets customizados |

Um exemplo de pasta customizada aparece no guia de primeiros passos:

```bash
mkdir -p "$HOME/.openclaw/control-ui-custom"
```

```json5
{
  gateway: {
    controlUi: {
      enabled: true,
      root: "${HOME}/.openclaw/control-ui-custom",
    },
  },
}
```

**Pequenos recursos úteis:** paleta de comandos com Cmd+K (macOS) ou Ctrl+K (demais), anexar arquivos ou imagens para iniciar uma sessão em segundo plano, e títulos de conversa gerados a partir da tarefa inicial. Se a conexão cair, a UI mantém dados e rascunhos em memória e mostra um indicador; ações como salvar edições exigem conexão ativa.

**Segurança.** O acesso depende das permissões concedidas à conexão atual, e o Gateway autoriza cada requisição. Com autenticação por token ou senha, o navegador ainda cria uma **identidade de dispositivo própria**; o segredo compartilhado não a substitui. Em HTTP simples, a assinatura de identidade do dispositivo não criptografa a página nem o tráfego.

> [!warning] Não exponha a UI diretamente
> Uma Control UI acessível pela internet dá a quem entrar controle do agente. Para uso remoto, prefira Tailscale Serve com HTTPS ou um túnel SSH, como em [[Acesso remoto - SSH, Tailscale e modos de bind]].

## Exemplo prático

1. Rode `openclaw dashboard`.
2. Abra a aba **Config**, vá a um campo avançado e veja o esquema ao vivo.
3. Envie "olá" na aba de chat e acompanhe a atividade.

## Armadilhas comuns

- Abrir a UI por um endereço de rede em HTTP e achar que o tráfego é criptografado.
- Mudar `basePath` e esquecer o reinício.
- Desligar a UI e achar que os bots pararam: eles continuam.

## Resumo

- Control UI: SPA servida pelo Gateway, mesma porta, falando WebSocket.
- Abra com `openclaw dashboard`; padrão `http://127.0.0.1:18789/`.
- Chaves `gateway.controlUi.*` controlam ativação, prefixo, origens e assets.
- Prefira HTTPS (Serve) ou túnel SSH para acesso remoto.

## Relacionados

- [[O processo Gateway e a porta 18789]]
- [[Configuração do Gateway em openclaw.json]]
- [[Acesso remoto - SSH, Tailscale e modos de bind]]
- [[Gateway, clientes e nodes]]

## Exercícios

1. Como se abre a Control UI e em que endereço ela fica por padrão?
2. O que acontece com os bots quando `gateway.controlUi.enabled` é desligado?
3. Qual chave exige reinício do Gateway ao ser alterada?
4. Por que HTTP simples é um transporte rebaixado?
