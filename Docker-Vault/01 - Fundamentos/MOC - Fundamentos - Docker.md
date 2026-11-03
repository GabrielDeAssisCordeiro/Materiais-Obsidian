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

# MOC - Fundamentos - Docker

Conceitos que sustentam todo o resto do material: o que é Docker, como ele se compara a VMs, sua arquitetura interna (cliente, daemon, containerd, runc), o padrão OCI e os recursos do kernel Linux que tornam os containers possíveis.

> [!tip] Ordem sugerida
> Comece por [[O que é Docker]], siga para [[Containers vs Máquinas Virtuais]] e [[Arquitetura do Docker]], e só depois mergulhe em [[Namespaces]], [[Cgroups - Docker]] e [[Union filesystems e OverlayFS]].

> [!info] Navegação
> Volte para [[Home - Docker]] a qualquer momento.

## Notas desta seção

- [[O que é Docker]] — Definição, ideia central e primeiros comandos
- [[O problema que o Docker resolve]] — Dores que motivaram a conteinerização
- [[Containers vs Máquinas Virtuais]] — Diferenças de arquitetura, desempenho e isolamento
- [[História do Docker]] — Do chroot ao Docker, OCI e BuildKit
- [[Arquitetura do Docker]] — Cliente, daemon, containerd, runc e registry (diagrama)
- [[Docker CLI e API]] — Cliente como interface da Engine API
- [[Docker Daemon dockerd]] — Papel, operação com systemd e data-root
- [[containerd e runc]] — Runtimes de alto e baixo nível; shim
- [[Padrão OCI]] — Runtime, Image e Distribution specs
- [[Namespaces]] — Isolamento de PID, rede, mount, UTS, IPC, user
- [[Cgroups - Docker]] — Limites e contabilização de recursos; OOM
- [[Union filesystems e OverlayFS]] — Camadas, overlay2 e copy-on-write
- [[Imagens vs Containers]] — Modelo imutável vs instância em execução
- [[Camadas de uma imagem]] — Camadas, cache e compartilhamento
- [[Registries]] — Repositórios, tags e anatomia do nome da imagem
- [[Ecossistema Docker]] — Mapa dos produtos e projetos do ecossistema

## Veja também

- [[Home - Docker]]
