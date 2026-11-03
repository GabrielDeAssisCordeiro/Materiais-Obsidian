---
tags:
  - docker
  - ia
aliases: []
tipo: procedimento
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[Docker Model Runner]]"
  - "[[Ambientes para ML e LLMs]]"
  - "[[Docker Desktop vs Docker Engine]]"
---

# Containers com GPU e NVIDIA Container Toolkit

Containers podem usar **GPUs** do host para ML, renderização e computação científica.

## NVIDIA (Linux)

Pré-requisitos: driver NVIDIA instalado no host e o **NVIDIA Container Toolkit**.

```bash
# Após instalar o toolkit seguindo a documentação oficial da NVIDIA:
sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker

# Teste
docker run --rm --gpus all nvidia/cuda:12.4.1-base-ubuntu22.04 nvidia-smi

# GPUs específicas
docker run --rm --gpus '"device=0"' nvidia/cuda:12.4.1-base-ubuntu22.04 nvidia-smi
```

## Em Compose

```yaml
services:
  treino:
    image: nvidia/cuda:12.4.1-base-ubuntu22.04
    command: nvidia-smi
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: all
              capabilities: [gpu]
```

## Outras plataformas

| Plataforma | Observação |
|---|---|
| **AMD (ROCm)** | `--device /dev/kfd --device /dev/dri` e imagens ROCm |
| **Windows (WSL2)** | Docker Desktop com WSL2 e driver NVIDIA compatível |
| **macOS** | Containers **não** acessam a GPU do Mac; o Model Runner executa no host |

> [!question] Verificar na documentação oficial
> A instalação do toolkit (repositórios e passos), as tags da imagem `nvidia/cuda` e a compatibilidade entre versões de driver e CUDA mudam; siga a documentação atual da NVIDIA.

> [!warning] Segurança
> O acesso à GPU expõe dispositivos e drivers do host ao container. Use imagens confiáveis e limite quais containers recebem GPU.

> [!tip] Imagens de runtime
> Para produção, prefira imagens `-runtime` ou `-base` (menores) em vez de `-devel`; use multi-stage para compilar com `-devel` e executar com `-runtime`.

## Exercício

Se tiver uma GPU NVIDIA, execute `nvidia-smi` em um container e depois limite o container a uma GPU específica.

## Veja também

- [[Docker Model Runner]]
- [[Ambientes para ML e LLMs]]
- [[Docker Desktop vs Docker Engine]]
- [[MOC - IA e Novidades]]
