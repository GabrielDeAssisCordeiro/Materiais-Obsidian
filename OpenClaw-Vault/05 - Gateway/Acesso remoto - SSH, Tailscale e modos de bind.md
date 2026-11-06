---
titulo: "Acesso remoto - SSH, Tailscale e modos de bind"
tags:
  - openclaw
  - conceito
  - gateway
tipo: conceito
aliases: ['Acesso remoto', 'Tailscale Serve', 'Bind']
nivel: avancado
fontes:
  - "[[Fontes]]"
  - "https://docs.openclaw.ai/gateway/tailscale"
  - "https://docs.openclaw.ai/gateway/remote"
  - "https://docs.openclaw.ai/gateway/security"
relacionados:
  - "[[O processo Gateway e a porta 18789]]"
  - "[[Control UI e dashboard]]"
  - "[[O protocolo WebSocket do Gateway]]"
  - "[[Fronteiras de confiança na arquitetura]]"
---

# Acesso remoto - SSH, Tailscale e modos de bind

## Objetivo

Acessar um Gateway de outra máquina sem expô-lo desnecessariamente, escolhendo o modo de bind e o método de acesso adequados.

## Explicação

O padrão é seguro: o WebSocket liga em **loopback** na porta 18789 (`gateway.port`). Tudo que for remoto exige uma decisão deliberada. A documentação descreve estes caminhos:

| Método | Como funciona | Quando usar |
|---|---|---|
| **Túnel SSH** | Encaminha a porta de loopback; funciona a partir de qualquer máquina | Acesso ocasional, sem instalar nada no Gateway |
| **Tailscale Serve** | Expõe a Control UI só na tailnet, com HTTPS; o Gateway fica em `127.0.0.1` | Uso diário recomendado quando você precisa de HTTPS |
| **Tailscale Funnel** | HTTPS **público**; exige senha | Só com forte necessidade e senha forte |
| **Bind `tailnet`** | O Gateway escuta no IP da tailnet; clientes usam `ws://<ip-tailscale>:18789`; use autenticação por token | Rede privada confiável |
| **Bind direto em LAN/tailnet** | Uso de `gateway.remote.transport: "direct"` | Rede confiável |

**Exemplos de configuração da documentação:**

```json5
{
  gateway: {
    bind: "loopback",
    tailscale: { mode: "serve" },
  },
}
```

```json5
{
  gateway: {
    bind: "tailnet",
    auth: { mode: "token", token: "seu-token" },
  },
}
```

Equivalentes na CLI:

```bash
openclaw gateway --tailscale serve
openclaw gateway --tailscale funnel --auth password
```

Modos de `gateway.tailscale.mode`: `serve`, `funnel` e `off` (padrão, em que o OpenClaw não gerencia Serve nem Funnel).

**Túnel SSH genérico** (sintaxe padrão do OpenSSH, não específica do OpenClaw):

```bash
ssh -N -L 18789:127.0.0.1:18789 usuario@servidor
```

Depois, abra `http://127.0.0.1:18789/` na sua máquina local.

> [!warning] Cuidados que a documentação destaca
> - Funnel é público: qualquer pessoa que alcance a URL só é barrada pela senha. Use uma senha forte e guarde-a na variável `OPENCLAW_GATEWAY_PASSWORD`, não em arquivo.
> - HTTP simples é transporte rebaixado; prefira Serve.
> - Acesso público ou entre origens precisa de entrada em `gateway.controlUi.allowedOrigins`.
> - Se o endereço da tailnet ainda não existir no início, o Gateway volta a escutar só em loopback; reinicie depois que o Tailscale subir.

## Exemplo prático

Cenário: Gateway em uma VPS, e você quer o painel no notebook.

1. Na VPS, mantenha `gateway.bind: "loopback"`.
2. No notebook, abra o túnel SSH acima.
3. Acesse `http://127.0.0.1:18789/` localmente e valide que a página abre.
4. Confirme na VPS que a porta não está em `0.0.0.0` (`ss -ltnp | grep 18789`).

## Armadilhas comuns

- Trocar o bind para `lan` ou `0.0.0.0` "só para testar" e esquecer aberto.
- Usar Funnel sem senha forte.
- Guardar senha ou token em arquivo versionado.

## Resumo

- Padrão: loopback. Remoto é decisão deliberada.
- Prefira túnel SSH ou Tailscale Serve; Funnel é público e exige senha.
- Bind `tailnet` exige autenticação por token.
- Guarde segredos em variáveis de ambiente ou gestão de segredos.

## Relacionados

- [[O processo Gateway e a porta 18789]]
- [[Control UI e dashboard]]
- [[O protocolo WebSocket do Gateway]]
- [[Fronteiras de confiança na arquitetura]]
- [[MOC - Segurança e Hardening|Segurança e Hardening]]

## Exercícios

1. Qual é o bind padrão do Gateway e por que ele é seguro?
2. Qual a diferença entre Tailscale Serve e Funnel?
3. Em que variável de ambiente se recomenda guardar a senha do Funnel?
4. Escreva o comando de um túnel SSH para a porta do Gateway.
