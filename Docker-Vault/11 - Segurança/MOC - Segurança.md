---
tags:
  - docker
  - moc
aliases: []
tipo: moc
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Home - Docker]]"
---

# MOC - Segurança

Abordagem **defensiva e educacional** de segurança em Docker: privilégios mínimos, isolamento, segredos, varredura, assinatura, proteção do daemon e hardening do host.

> [!danger] Uso responsável
> Os exemplos devem ser executados somente em ambiente de laboratório próprio. Nunca teste contra sistemas de terceiros.

> [!tip] Visão geral
> Comece por [[Princípio do menor privilégio - Docker]] e finalize com o [[Checklist de segurança de containers]].

> [!info] Navegação
> Volte para [[Home - Docker]] a qualquer momento.

## Notas desta seção

- [[Princípio do menor privilégio - Docker]] — Camadas de defesa e exemplo endurecido
- [[Containers não-root]] — USER, UID numérico e imagens prontas
- [[Sistema de arquivos somente leitura]] — --read-only com tmpfs e volumes
- [[Capabilities Linux]] — cap-drop, cap-add e conjunto padrão
- [[Opções security-opt e no-new-privileges]] — no-new-privileges, seccomp, apparmor e label
- [[Seccomp - Docker]] — Filtro de syscalls e perfis
- [[AppArmor e SELinux]] — MAC: perfis docker-default e rótulos :z/:Z
- [[User namespaces e userns-remap]] — Mapeamento de UID do container para o host
- [[Gerenciamento de segredos]] — Build, execução e repositório; detecção de vazamentos
- [[Varredura de vulnerabilidades com Trivy e Grype]] — Scanners de CVE e integração com CI
- [[Docker Scout]] — Análise, SBOM e recomendações da Docker
- [[Assinatura de imagens com Cosign e Content Trust]] — Cosign, keyless e DCT
- [[Superfície de ataque e imagens mínimas]] — Distroless, scratch e multi-stage para segurança
- [[Proteção do docker.sock]] — Por que o socket equivale a root e como mitigar
- [[Riscos do --privileged]] — O que --privileged concede e alternativas
- [[Escape de container]] — Categorias de risco e defesas (visão defensiva)
- [[CIS Docker Benchmark e Docker Bench for Security]] — Benchmark CIS e script de auditoria
- [[Hardening do host Docker]] — Medidas para o host, daemon e auditoria
- [[Checklist de segurança de containers]] — Checklist consolidado de imagem, execução, rede e plataforma

## Veja também

- [[Home - Docker]]
