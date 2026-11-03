---
tags:
  - docker
  - seguranca
  - vulnerabilidades
aliases:
  - Grype
tipo: procedimento
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Docker Scout]]"
  - "[[SBOM e provenance]]"
  - "[[Escolha da imagem base]]"
  - "[[Checklist de segurança de containers]]"
---

# Varredura de vulnerabilidades com Trivy e Grype

Scanners comparam os pacotes e bibliotecas de uma imagem com bancos de **CVEs** conhecidas. Rode-os no CI e periodicamente em imagens já publicadas (novas CVEs surgem todo dia).

## Trivy

```bash
# Instalado localmente
trivy image nginx:1.27
trivy image --severity HIGH,CRITICAL --ignore-unfixed nginx:1.27
trivy image --exit-code 1 --severity CRITICAL meu-app:1.0     # falha o CI se houver críticas

# Via container (baixa a imagem do registry; mantém cache em um volume)
docker run --rm -v trivy-cache:/root/.cache aquasec/trivy image nginx:1.27

# Também examina configurações (Dockerfile, Compose) e segredos
trivy config .
trivy fs --scanners vuln,secret .
```

## Grype (com Syft para SBOM)

```bash
grype nginx:1.27
grype nginx:1.27 --fail-on high

syft nginx:1.27 -o spdx-json > sbom.spdx.json
grype sbom:./sbom.spdx.json
```

## Como interpretar

| Campo | O que significa |
|---|---|
| Severidade | CVSS: CRITICAL, HIGH, MEDIUM, LOW |
| *Fixed version* | Versão em que foi corrigida; vazio = sem correção disponível |
| Pacote do SO vs da aplicação | Corrija atualizando a imagem base ou as dependências |

> [!tip] Reduza o ruído
> Priorize **CVEs exploráveis e com correção disponível**. Imagens menores (slim, distroless) têm menos pacotes e, portanto, menos alertas. Atualize a imagem base regularmente.

> [!warning] Scanner não é prova de segurança
> Ausência de achados não garante que a imagem seja segura (vulnerabilidades desconhecidas, configuração incorreta, segredos).

> [!question] Verificar na documentação oficial
> Em CI, **fixe a versão** do scanner (a tag `latest` usada acima serve só para laboratório) e confirme as opções na documentação do Trivy e do Grype.

## Exercício

Escaneie `nginx:1.27` e `nginx:1.27-alpine` com o Trivy e compare o número de vulnerabilidades HIGH/CRITICAL.

## Veja também

- [[Docker Scout]]
- [[SBOM e provenance]]
- [[Escolha da imagem base]]
- [[Checklist de segurança de containers]]
- [[MOC - Segurança]]
