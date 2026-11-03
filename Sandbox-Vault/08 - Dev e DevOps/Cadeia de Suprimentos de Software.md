---
tags:
  - devops
  - dev
aliases: []
tipo: devops
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[Caso - Desenvolvimento Seguro]]"
  - "[[Runners Efêmeros e Pipelines Seguros]]"
---
# Cadeia de Suprimentos de Software

Dependências e ferramentas de build são parte da superfície de ataque.

| Risco | Mitigação |
|---|---|
| Pacote malicioso ou comprometido | Fixar versões e hashes; revisar novas dependências |
| *Typosquatting* | Conferir nome e mantenedores |
| Scripts de instalação | Instalar em sandbox, sem segredos |
| Imagens base desatualizadas | Escanear e atualizar |
| Artefatos adulterados | Assinar (ex.: Sigstore/cosign) e gerar SBOM |

```bash
pip install --require-hashes -r requirements.txt
```

> [!question] Verificar na documentação oficial
> Ferramentas e frameworks (SLSA, SBOM, Sigstore) evoluem; consulte as especificações oficiais.

## Veja também

- [[Caso - Desenvolvimento Seguro]]
- [[Runners Efêmeros e Pipelines Seguros]]
- [[Criar Ambientes Python Isolados]]
- [[MOC - Dev e DevOps]]
