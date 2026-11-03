---
tags:
  - docker
  - moc
aliases: []
tipo: moc
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Home - Docker]]"
---

# MOC - Docker Compose

Defina e execute aplicações multi-container com `compose.yaml`: serviços, redes, volumes, variáveis, dependências, perfis, overrides, secrets, limites de recursos e desenvolvimento com Compose Watch.

> [!tip] Caminho sugerido
> [[Visão geral do Docker Compose]] → [[Estrutura do compose.yaml e Compose Specification]] → [[Portas, volumes e redes no Compose]] → [[depends_on com condition e healthcheck]] → [[Múltiplos arquivos e overrides]].

> [!info] Navegação
> Volte para [[Home - Docker]] a qualquer momento.

## Notas desta seção

- [[Visão geral do Docker Compose]] — Primeiro compose.yaml, comandos básicos e diagrama
- [[Estrutura do compose.yaml e Compose Specification]] — Chaves de nível superior, nomes de arquivo e validação
- [[Serviços com image e build]] — image, build, args, target e pull_policy
- [[Portas, volumes e redes no Compose]] — Publicação, volumes e redes em Compose
- [[Variáveis de ambiente e env_file]] — environment, env_file e precedência
- [[Interpolação e arquivo .env]] — ${VAR:-padrão}, ${VAR:?erro} e precedência
- [[depends_on com condition e healthcheck]] — Ordem, prontidão e tarefas únicas
- [[Profiles]] — Serviços opcionais ativados sob demanda
- [[Múltiplos arquivos e overrides]] — Override automático, -f e regras de mesclagem
- [[extends e include]] — include de arquivos e herança com extends
- [[configs e secrets no Compose]] — secrets em /run/secrets e configs
- [[deploy.resources e limites]] — Limites de CPU, memória e PIDs
- [[Comandos do Docker Compose]] — Referência dos comandos principais
- [[Compose Watch]] — sync, rebuild e sync+restart no desenvolvimento
- [[Projetos nomeados no Compose]] — Prefixos, -p e múltiplas instâncias

## Veja também

- [[Home - Docker]]
