---
tags:
  - docker
  - ia
  - novidades
aliases: []
tipo: referencia
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Docker Hardened Images]]"
  - "[[Docker Model Runner]]"
  - "[[WebAssembly e containers]]"
  - "[[Podman, containerd e nerdctl]]"
---

# Tendências em containers

O que acompanhar nos próximos anos:

| Tendência | Resumo |
|---|---|
| **Segurança da cadeia de suprimentos** | SBOM, provenance (SLSA), assinatura (Sigstore), VEX, imagens endurecidas |
| **IA e containers** | Modelos como artefatos OCI, Model Runner, servidores MCP em containers, agentes executando em sandboxes |
| **Imagens mínimas por padrão** | Distroless, DHI, *chiseled*; builds multi-stage como norma |
| **containerd como base** | Image store do containerd como padrão; snapshotters e *lazy pulling* |
| **Rootless e sandboxing** | Rootless, user namespaces, gVisor, Kata, microVMs (Firecracker) |
| **Wasm** | Cargas leves e rápidas, ao lado de containers |
| **nftables** | Backends de firewall modernos no Engine |
| **Desenvolvimento remoto/nuvem** | Dev Containers, Codespaces, builds e execução remotos (Offload/Build Cloud) |
| **Platform engineering e GitOps** | Plataformas internas, Kubernetes gerenciado, implantação declarativa |
| **Observabilidade padronizada** | OpenTelemetry para métricas, logs e traços |

> [!tip] Como se manter atualizado
> Leia as *release notes* do Docker Engine e do Desktop a cada versão, acompanhe os blogs de Docker, containerd, Kubernetes e CNCF, e revise periodicamente suas imagens e pipelines.

> [!question] Verificar na documentação oficial
> Tendências são projeções; confirme o estado atual de cada tecnologia nas fontes oficiais antes de decisões de arquitetura.

## Exercício

Escolha duas tendências e descreva como poderiam afetar um projeto seu nos próximos 12 meses, e o que você faria para se preparar.

## Veja também

- [[Docker Hardened Images]]
- [[Docker Model Runner]]
- [[WebAssembly e containers]]
- [[Podman, containerd e nerdctl]]
- [[MOC - IA e Novidades]]
