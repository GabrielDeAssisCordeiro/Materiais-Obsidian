---
titulo: "Docker Bench for Security"
tipo: ferramenta
nome: "Docker Bench for Security"
categoria: "Cloud-e-Container"
subcategoria: "Auditoria de Hardening Docker"
plataformas: ["Linux"]
licenca: "Apache-2.0"
linguagem: "Shell"
mitre_attack: []
nivel: intermediario
situacao: ativo
link_oficial: "https://github.com/docker/docker-bench-security"
tags:
  - ciberseguranca
  - ferramenta
  - cloud
---

# Docker Bench for Security

> Script de verificação automatizada de boas práticas de segurança para hosts e containers Docker.

## Como funciona
Executa uma checklist baseada no CIS Benchmark for Docker, verificando a configuração do daemon Docker, permissões de arquivos relevantes, parâmetros de execução de containers em produção (privilégios excessivos, montagens de socket sensíveis) e reportando cada item como passou/falhou/aviso, de forma semelhante em espírito ao Lynis mas especializado em Docker.

## Como usar
Executa-se diretamente no host Docker (`./docker-bench-security.sh` ou via container oficial), gerando um relatório no terminal organizado pelas seções do CIS Benchmark, com cada item identificado como `[PASS]`, `[WARN]` ou `[INFO]`.

## Casos de uso
- Auditoria de hardening de hosts Docker em produção
- Checklist de conformidade com CIS Benchmark for Docker

## Alternativas
[[Trivy]] · [[kube-hunter]]

## Categoria
[[MOC - Cloud e Container]]

## Link oficial
https://github.com/docker/docker-bench-security
