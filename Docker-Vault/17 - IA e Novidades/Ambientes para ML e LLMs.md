---
tags:
  - docker
  - ia
  - llm
  - ollama
aliases: []
tipo: procedimento
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Docker Model Runner]]"
  - "[[Containers com GPU e NVIDIA Container Toolkit]]"
  - "[[Volumes nomeados]]"
  - "[[Resiliência em produção]]"
---

# Ambientes para ML e LLMs

Containers resolvem a "dependency hell" de ML: versões de Python, CUDA e bibliotecas ficam **fixas e reproduzíveis**.

## LLM local com Ollama + interface web

```yaml
services:
  ollama:
    image: ollama/ollama:latest      # em projetos reais, fixe a versão
    volumes:
      - ollama_models:/root/.ollama
    ports:
      - "127.0.0.1:11434:11434"
    # Para usar GPU NVIDIA, descomente:
    # deploy:
    #   resources:
    #     reservations:
    #       devices:
    #         - driver: nvidia
    #           count: all
    #           capabilities: [gpu]

  webui:
    image: ghcr.io/open-webui/open-webui:main    # fixe uma tag de versão em uso real
    environment:
      OLLAMA_BASE_URL: http://ollama:11434
    ports:
      - "127.0.0.1:3000:8080"
    volumes:
      - webui_data:/app/backend/data
    depends_on:
      - ollama

volumes:
  ollama_models:
  webui_data:
```

```bash
docker compose up -d
docker compose exec ollama ollama pull llama3.2     # baixa um modelo
docker compose exec ollama ollama run llama3.2 "Olá!"
```

## Notebook Jupyter

```bash
docker run --rm -p 127.0.0.1:8888:8888 \
  -v "$PWD":/home/jovyan/work \
  quay.io/jupyter/scipy-notebook
```

## Boas práticas

| Prática | Motivo |
|---|---|
| **Volume para modelos e dados** | Modelos pesam GBs; não os coloque na imagem |
| Fixar versões (Python, CUDA, frameworks) | Reprodutibilidade de experimentos |
| Limitar memória/GPU | Evita derrubar o host |
| Não expor APIs de modelos na Internet | Não têm autenticação por padrão |
| Imagens separadas para treino e inferência | Inferência fica menor e mais segura |

> [!warning] APIs de inferência abertas
> Servidores como o Ollama não autenticam por padrão. Publique em `127.0.0.1` e proteja com proxy autenticado se precisar expor.

> [!question] Verificar na documentação oficial
> As imagens e variáveis dos projetos (Ollama, Open WebUI, Jupyter) mudam com frequência; fixe versões e confirme as opções nas páginas oficiais.

## Exercício

Suba o Ollama com um modelo pequeno, faça uma pergunta pela CLI e depois pela interface web, confirmando que os modelos persistem após `docker compose down` (sem `-v`).

## Veja também

- [[Docker Model Runner]]
- [[Containers com GPU e NVIDIA Container Toolkit]]
- [[Volumes nomeados]]
- [[Resiliência em produção]]
- [[MOC - IA e Novidades]]
