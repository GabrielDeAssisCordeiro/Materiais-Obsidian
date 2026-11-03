---
tags:
  - docker
  - redes
  - host
  - desempenho
aliases: []
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Visão geral das redes Docker]]"
  - "[[Namespaces]]"
  - "[[Publicação de portas]]"
---

# Rede host

Com `--network host`, o container **compartilha a pilha de rede do host**: usa seus IPs e portas diretamente, sem NAT e sem isolamento de rede.

```bash
# Nginx escutando direto na porta 80 do host (não precisa de -p)
docker run -d --name web --network host nginx:1.27
curl -I http://localhost

docker rm -f web
```

| Vantagem | Desvantagem |
|---|---|
| Menor latência (sem NAT) | Sem isolamento de rede |
| Muitas portas sem mapear uma a uma | `-p` é **ignorado** |
| Útil para ferramentas de rede/monitoramento | Conflitos de porta com o host |

> [!info] Disponibilidade
> No Linux funciona nativamente. No Docker Desktop (macOS/Windows), o "host" é a VM interna, não o seu computador; versões recentes oferecem suporte opcional a *host networking*, que precisa ser habilitado.

> [!question] Verificar na documentação oficial
> O suporte a `--network host` no Docker Desktop depende da versão e de uma configuração específica. Consulte a documentação do Docker Desktop.

> [!danger] Aumenta a superfície de ataque
> O container pode acessar serviços que escutam em `127.0.0.1` do host. Evite em containers expostos ou de terceiros.

## Exercício

Rode `docker run --rm --network host alpine ip addr` e compare com `ip addr` no host. Explique por que as interfaces coincidem.

## Veja também

- [[Visão geral das redes Docker]]
- [[Namespaces]]
- [[Publicação de portas]]
- [[MOC - Redes]]
