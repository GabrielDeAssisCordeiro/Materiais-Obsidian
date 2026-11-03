---
tags:
  - docker
  - cicd
  - registry
  - testes
aliases: []
tipo: procedimento
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[Registry privado local com registry 2]]"
  - "[[Pipeline CI-CD com Docker]]"
  - "[[GitHub Actions para build e push]]"
---

# Registries efêmeros em CI

Um **registry efêmero** é um registry temporário, criado só durante o job de CI. Serve para:

- Compartilhar **imagens intermediárias** entre etapas/serviços sem publicá-las no registry real.
- Testar o fluxo de `push`/`pull` e imagens multiplataforma.
- Evitar poluir o registry de produção com imagens de PRs.

## GitHub Actions: serviço `registry:2`

```yaml
jobs:
  integracao:
    runs-on: ubuntu-latest
    services:
      registry:
        image: registry:2
        ports:
          - 5000:5000
    steps:
      - uses: actions/checkout@v4

      - uses: docker/setup-buildx-action@v3
        with:
          driver-opts: network=host      # o builder precisa alcançar localhost:5000

      - name: Build e push para o registry efêmero
        uses: docker/build-push-action@v6
        with:
          context: .
          push: true
          tags: localhost:5000/app:teste

      - name: Testa a imagem a partir do registry efêmero
        run: |
          docker run --rm localhost:5000/app:teste --version
```

## Em qualquer CI com Docker

```bash
docker run -d --name reg -p 5000:5000 registry:2
docker build -t localhost:5000/app:teste .
docker push localhost:5000/app:teste
# ... testes que fazem pull de localhost:5000/app:teste ...
docker rm -f reg
```

> [!tip] Alternativas
> Para PRs, muitos times publicam tags efêmeras (`pr-123`) no registry real com política de limpeza automática. Veja [[Políticas de retenção e limpeza]].

> [!info] `localhost` é confiável
> O Docker permite HTTP apenas para `localhost`; por isso o uso de `localhost:5000` evita configurar TLS.

## Exercício

Reproduza o fluxo localmente: suba `registry:2`, construa e publique uma imagem, e confirme com `curl http://localhost:5000/v2/_catalog`.

## Veja também

- [[Registry privado local com registry 2]]
- [[Pipeline CI-CD com Docker]]
- [[GitHub Actions para build e push]]
- [[MOC - CI-CD e DevOps]]
