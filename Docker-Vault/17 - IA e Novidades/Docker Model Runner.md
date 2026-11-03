---
tags:
  - docker
  - ia
  - novidades
  - llm
aliases:
  - DMR
  - docker model
tipo: procedimento
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Containers com GPU e NVIDIA Container Toolkit]]"
  - "[[Ambientes para ML e LLMs]]"
  - "[[MCP e containers]]"
  - "[[Docker Desktop vs Docker Engine]]"
---

# Docker Model Runner

O **Docker Model Runner (DMR)** permite **baixar, executar e gerenciar modelos de IA** (LLMs) localmente com comandos no estilo Docker e expõe uma **API compatível com OpenAI**. Está incluído no Docker Desktop e disponível no Docker Engine (instalado dos repositórios oficiais).

## Comandos principais

```bash
docker model status                      # o runner está ativo?
docker model pull ai/smollm2             # baixa um modelo (Docker Hub, namespace "ai", ou Hugging Face)
docker model list                        # modelos locais
docker model run ai/smollm2 "Explique o que é um container em duas frases."
docker model run ai/smollm2              # modo chat interativo
docker model logs                        # logs do runner
docker model inspect ai/smollm2
docker model rm ai/smollm2
```

| Subcomando | Função |
|---|---|
| `pull` / `push` / `tag` | Distribuir modelos como artefatos OCI |
| `package` | Empacota um arquivo GGUF como artefato de modelo e publica em um registry |
| `install-runner` / `uninstall-runner` | Instala/remove o runner (Docker Engine) |
| `version` | Versão do runner |

## Como funciona

- Os modelos são **artefatos OCI** (você os versiona e distribui como imagens).
- A inferência executa **no host** (com aceleração por GPU quando disponível), **não dentro de um container**, para desempenho próximo ao nativo.
- Modelos são carregados em memória sob demanda e descarregados quando ociosos.

## API compatível com OpenAI

Dentro de containers (Docker Desktop):

```text
http://model-runner.docker.internal/engines/v1/
```

No host, habilitando acesso por TCP:

```bash
docker desktop enable model-runner --tcp 12434

curl http://localhost:12434/engines/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"ai/smollm2","messages":[{"role":"user","content":"Olá!"}]}'
```

## Em Compose (modelos como dependência)

```yaml
services:
  app:
    image: minha-app-llm:1.0
    models:
      - llm

models:
  llm:
    model: ai/smollm2
```

> [!question] Verificar na documentação oficial
> O Docker Model Runner evolui rápido (motores de inferência, caminhos da API, o elemento `models:` do Compose, requisitos de hardware e suporte por plataforma). Confirme em `docker model --help` e na documentação oficial; o recurso já foi rotulado como experimental/beta.

> [!warning] Memória e privacidade
> Modelos grandes exigem muita RAM/VRAM. Rodar localmente mantém os dados na sua máquina, mas verifique licenças dos modelos antes de uso comercial.

## Exercício

Habilite o Model Runner, baixe um modelo pequeno (`ai/smollm2`) e consulte-o primeiro pela CLI e depois por `curl` na API compatível com OpenAI.

## Veja também

- [[Containers com GPU e NVIDIA Container Toolkit]]
- [[Ambientes para ML e LLMs]]
- [[MCP e containers]]
- [[Docker Desktop vs Docker Engine]]
- [[MOC - IA e Novidades]]
