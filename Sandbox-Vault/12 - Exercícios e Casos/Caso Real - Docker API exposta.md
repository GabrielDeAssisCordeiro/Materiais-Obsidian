---
tags:
  - estudos-de-caso
  - incidentes
aliases: []
tipo: estudo-de-caso
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Erros Comuns em Sandboxes]]"
  - "[[Sandbox por Containers]]"
---
# Caso Real - Docker API exposta

> [!question] Verificar na documentação oficial
> Resumo educativo, sem detalhes de exploração. Confirme datas, versões e CVEs nos avisos oficiais antes de citar.


**O que foi:** padrão amplamente reportado em que daemons Docker expostos na internet sem autenticação (porta TCP do daemon) foram usados para criar containers e executar mineração de criptomoedas ou obter acesso ao host.

**Lições**
- Nunca exponha a API do Docker sem TLS mútuo e firewall.
- Quem acessa o daemon controla o host.
- Monitore uso anormal de CPU e containers desconhecidos.

**Camadas que ajudam:** [[Endurecimento (Hardening)]], [[Logs e Monitoramento]], [[Erros Comuns em Sandboxes]].

## Veja também

- [[Erros Comuns em Sandboxes]]
- [[Endurecimento (Hardening)]]
- [[MOC - Exercícios e Casos]]
