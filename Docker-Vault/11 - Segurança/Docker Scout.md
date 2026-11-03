---
tags:
  - docker
  - seguranca
  - vulnerabilidades
  - supply-chain
aliases: []
tipo: procedimento
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Varredura de vulnerabilidades com Trivy e Grype]]"
  - "[[SBOM e provenance]]"
  - "[[Escolha da imagem base]]"
  - "[[Ecossistema Docker]]"
---

# Docker Scout

O **Docker Scout** analisa imagens, gera SBOM, aponta vulnerabilidades e **recomenda atualizações da imagem base**. Integra-se ao Docker Desktop, à CLI e ao Docker Hub.

```bash
docker login                              # necessário para usar o Scout

docker scout quickview nginx:1.27         # resumo rápido
docker scout cves nginx:1.27              # lista de CVEs
docker scout cves --only-severity critical,high nginx:1.27
docker scout recommendations nginx:1.27   # sugestões de imagem base melhor
docker scout compare --to nginx:1.27-alpine nginx:1.27   # compara duas imagens
docker scout sbom nginx:1.27              # SBOM
```

## O que oferece

| Recurso | Descrição |
|---|---|
| Análise contínua | Reanalisa imagens quando surgem novas CVEs |
| Recomendações | Sugere tags de base com menos vulnerabilidades |
| Políticas | Regras (sem CVEs críticas, base atualizada, sem licenças proibidas) |
| Integração CI | GitHub Actions (`docker/scout-action`) |
| Docker Desktop | Exibe achados ao lado de cada imagem |

> [!question] Verificar na documentação oficial
> Limites de repositórios analisados, recursos de políticas e disponibilidade variam por plano. Consulte a documentação do Docker Scout antes de adotar.

> [!tip] Uso combinado
> Use o Scout para a análise integrada e recomendações, e Trivy/Grype como segunda opinião ou em pipelines independentes do ecossistema Docker.

## Exercício

Execute `docker scout quickview` e `docker scout recommendations` em uma imagem sua e aplique a recomendação de base. Meça a variação nas CVEs.

## Veja também

- [[Varredura de vulnerabilidades com Trivy e Grype]]
- [[SBOM e provenance]]
- [[Escolha da imagem base]]
- [[Ecossistema Docker]]
- [[MOC - Segurança]]
