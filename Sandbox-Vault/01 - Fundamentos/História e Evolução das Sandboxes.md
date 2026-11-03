---
tags:
  - fundamentos
aliases:
  - "Linha do tempo das sandboxes"
tipo: referencia
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[O que é um Ambiente Sandbox]]"
  - "[[Sandbox vs VM vs Container vs Jail vs chroot]]"
  - "[[Namespaces do Linux]]"
---
# História e Evolução das Sandboxes

A ideia de confinar programas é antiga e evoluiu de simples restrições de diretório até microVMs e WebAssembly.

> [!question] Verificar na documentação oficial
> Anos e versões abaixo são aproximados e servem como linha do tempo de estudo; confirme datas exatas nas fontes de cada projeto.

| Período | Marco | Observação |
|---|---|---|
| 1979–1982 | `chroot` (Unix V7 / BSD) | Muda a raiz do sistema de arquivos; **não** é fronteira de segurança |
| 1995–1996 | Sandbox do Java (applets) | Código remoto executado com restrições na JVM |
| 2000 | FreeBSD Jails | Isolamento de processos, rede e usuários no mesmo kernel |
| 2001–2002 | Primeiros namespaces no Linux (mount) | Base dos containers modernos |
| 2005 | Solaris Zones; seccomp (modo estrito) no Linux | Isolamento por SO e filtro mínimo de syscalls |
| 2007–2008 | cgroups; LXC; sandbox do Google Chrome | Limites de recursos, containers de sistema, navegador multiprocesso |
| 2012 | seccomp-bpf; Capsicum (FreeBSD) | Filtros programáveis de syscalls; modelo de capacidades |
| 2013 | Docker | Popularização de containers e imagens |
| 2016–2018 | `pledge`/`unveil` (OpenBSD); gVisor; Firecracker | Autorrestrição simples; kernel em espaço de usuário; microVMs |
| 2017–2019 | WebAssembly; WASI | Sandbox portável por *design* |
| 2019 | Windows Sandbox | Ambiente descartável baseado em Hyper-V |
| 2021 | Landlock (Linux 5.13) | Restrição de acesso a arquivos por processos sem privilégio |
| Hoje | Sandboxes para agentes de IA | Execução de código gerado por LLM — ver [[Sandbox para Código Gerado por IA]] |

## Tendências

- **Do compartilhamento de kernel ao isolamento por hardware** em cargas multi-inquilino (microVMs).
- **Sandbox por padrão** em linguagens e runtimes (Deno, WASI).
- **Efêmero e descartável** como norma em CI/CD e nuvem.

## Veja também

- [[O que é um Ambiente Sandbox]]
- [[Sandbox vs VM vs Container vs Jail vs chroot]]
- [[Namespaces do Linux]]
- [[Sandbox por MicroVMs]]
