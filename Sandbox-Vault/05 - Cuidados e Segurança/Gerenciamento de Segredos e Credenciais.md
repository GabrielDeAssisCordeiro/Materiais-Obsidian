---
tags:
  - seguranca
aliases:
  - "Secrets"
  - "Segredos"
tipo: cuidado
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Princípio do Menor Privilégio]]"
  - "[[Caso - CI e CD]]"
---
# Gerenciamento de Segredos e Credenciais

Segredos dentro de uma sandbox são alvo natural: se o código for hostil, ele tentará lê-los.

- **Não** coloque segredos em imagens, repositórios ou variáveis de ambiente de sandboxes não confiáveis.
- Use tokens **curtos e de escopo mínimo**; revogue após o uso.
- Use gerenciadores de segredos (Vault, gerenciadores de nuvem) e monte segredos como arquivos somente leitura só onde necessário.
- Separe credenciais de teste e de produção.
- Faça varredura de segredos no código (ex.: gitleaks, trufflehog).

```bash
docker run --rm -v "$PWD/segredo.txt:/run/secrets/token:ro" alpine:3 cat /run/secrets/token
```

> [!danger] Variáveis de ambiente vazam
> Aparecem em `docker inspect`, `/proc` e logs de falha. Para sandboxes de código de terceiros, não passe segredos.

## Exercício

Rode `docker inspect` em um container com variável de ambiente e veja o valor exposto. Que alternativa você usaria?

## Veja também

- [[Princípio do Menor Privilégio]]
- [[Caso - CI e CD]]
- [[Sandbox para Código Gerado por IA]]
- [[MOC - Cuidados e Segurança]]
