---
tags:
  - docker
  - ia
  - novidades
aliases: []
tipo: comparativo
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Docker Desktop vs Docker Engine]]"
  - "[[Instalação no macOS]]"
  - "[[Instalação no Windows com WSL2]]"
  - "[[Podman, containerd e nerdctl]]"
---

# Alternativas ao Docker Desktop

Se o licenciamento, o consumo de recursos ou a preferência por open source pesam, há opções.

| Ferramenta | Plataformas | Características |
|---|---|---|
| **Colima** | macOS, Linux | Open source, leve, usa Lima; expõe um Docker Engine (ou containerd) em uma VM |
| **OrbStack** | macOS | Muito rápido e econômico; Docker + Linux machines; licença comercial para uso profissional |
| **Rancher Desktop** | macOS, Windows, Linux | Open source; escolha entre dockerd (moby) e containerd; Kubernetes opcional |
| **Podman Desktop** | macOS, Windows, Linux | Interface gráfica para Podman e Kubernetes |
| **Docker Engine no WSL2** | Windows | Instale o Engine **dentro** de uma distro WSL2 (como em um servidor Linux) |
| **Lima** | macOS, Linux | VMs Linux com containerd/nerdctl e outras |

## Colima (macOS) em 3 comandos

```bash
brew install colima docker docker-compose
colima start --cpu 4 --memory 8 --disk 60
docker run --rm hello-world
```

## Docker Engine no WSL2 (Windows)

```powershell
wsl --install -d Ubuntu
# Dentro do Ubuntu: siga a instalação do Engine para Linux (apt) e ative o systemd no WSL
```

```bash
# /etc/wsl.conf (dentro da distro) para habilitar o systemd
# [boot]
# systemd=true
```

> [!tip] Compatibilidade
> Todas expõem um socket compatível com a API do Docker (ou o fazem por um contexto), então a CLI `docker`, o Compose e a maioria das ferramentas continuam funcionando. Use `docker context ls` para ver o endpoint ativo. Veja [[Contextos do Docker]].

> [!question] Verificar na documentação oficial
> Licenças, preços e recursos (por exemplo, limites de uso gratuito) mudam; consulte o site de cada projeto. Verifique também a compatibilidade com recursos específicos do Docker Desktop (Scout, Model Runner, Extensões).

## Exercício

Escolha uma alternativa para sua plataforma, instale-a e execute a stack Compose de um dos seus projetos. Anote desempenho, consumo de memória e diferenças percebidas.

## Veja também

- [[Docker Desktop vs Docker Engine]]
- [[Instalação no macOS]]
- [[Instalação no Windows com WSL2]]
- [[Podman, containerd e nerdctl]]
- [[MOC - IA e Novidades]]
