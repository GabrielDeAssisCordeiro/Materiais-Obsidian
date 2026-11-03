---
tags:
  - docker
  - instalacao
  - comparativo
aliases: []
tipo: comparativo
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Instalação no Linux]]"
  - "[[Instalação no Windows com WSL2]]"
  - "[[Instalação no macOS]]"
  - "[[Ecossistema Docker]]"
---

# Docker Desktop vs Docker Engine

Há duas formas principais de ter Docker na sua máquina.

| Característica | Docker Engine | Docker Desktop |
|---|---|---|
| Plataformas | Linux (servidores e desktops) | Windows, macOS e Linux |
| Como roda | Nativo no host Linux | Dentro de uma VM Linux gerenciada |
| Interface gráfica | Não | Sim (containers, imagens, volumes, extensões) |
| Inclui | `dockerd`, CLI, containerd, Buildx e Compose (plugins) | Engine, CLI, Compose, Buildx, Scout, Kubernetes opcional, Model Runner e mais |
| Desempenho de I/O em bind mounts | Nativo | Depende do sistema (macOS e Windows têm overhead) |
| Licença | Open source (Apache 2.0) | Uso gratuito para uso pessoal, educação, projetos open source e pequenas empresas; assinatura paga para empresas maiores |
| Uso recomendado | **Servidores e produção** | **Desenvolvimento local** |

> [!info] Licenciamento do Docker Desktop
> As regras de gratuidade (porte da empresa) podem mudar. Consulte os termos de serviço oficiais antes de adotar em ambiente corporativo.

> [!tip] Qual escolher?
> - **Servidor Linux**: instale o Docker Engine.
> - **Notebook com Windows ou macOS**: Docker Desktop (ou alternativas, veja [[Alternativas ao Docker Desktop]]).
> - **Linux no desktop**: ambos são possíveis. O Docker Desktop for Linux usa VM própria e um contexto separado (`desktop-linux`); o Engine usa o contexto `default`.

> [!warning] Não misture sem cuidado
> No Linux, Docker Engine e Docker Desktop mantêm **daemons, imagens e volumes separados**. Use [[Contextos do Docker]] para saber em qual deles você está falando.

## Veja também

- [[Instalação no Linux]]
- [[Instalação no Windows com WSL2]]
- [[Instalação no macOS]]
- [[Ecossistema Docker]]
- [[MOC - Instalação e Configuração]]
