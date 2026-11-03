---
tags:
  - seguranca
aliases:
  - "Isolamento de rede"
  - "DNS leak"
tipo: cuidado
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Sandbox de Rede]]"
  - "[[Criar Laboratório de Malware Seguro]]"
---
# Vazamento por Rede e DNS

"Sem internet" nem sempre significa **sem saída**.

| Vetor | Observação |
|---|---|
| DNS | Consultas podem sair mesmo sem HTTP; teste com `nslookup` |
| ICMP | `ping` pode passar por regras mal feitas |
| NAT acidental | Adaptador em modo NAT/bridge em vez de rede interna |
| IPv6 | Regras só para IPv4 deixam IPv6 aberto |
| Rotas para a LAN | Acesso a impressoras, NAS, roteador |
| Proxies e *tunneling* | Tráfego encapsulado em DNS/HTTPS |

## Teste de isolamento

```bash
ping -c 2 1.1.1.1
nslookup exemplo.com
curl -m 5 -I https://exemplo.com
curl -6 -m 5 -I https://exemplo.com
ip route
```

Tudo deve falhar (exceto, se desejado, serviços simulados internos).

> [!tip] Use um resolvedor simulado
> Um serviço como INetSim responde a DNS/HTTP internamente, permitindo observar o comportamento sem sair da rede.

> [!danger] Verifique também de fora
> Capture tráfego no host/gateway durante um teste para confirmar que nada sai.

## Exercício

Em uma VM em rede interna, execute o teste e capture o tráfego no host com `tcpdump`. Houve algum pacote saindo?

## Veja também

- [[Sandbox de Rede]]
- [[Criar Laboratório de Malware Seguro]]
- [[Fuga de Sandbox]]
- [[MOC - Cuidados e Segurança]]
