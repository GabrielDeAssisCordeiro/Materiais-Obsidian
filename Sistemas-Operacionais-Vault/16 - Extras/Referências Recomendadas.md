---
titulo: "Referências Recomendadas"
tags:
  - sistemas-operacionais
  - referencia
tipo: referencia
nivel: iniciante
relacionados:
  - "[[MOC - Extras]]"
  - "[[Mapa de Estudos]]"
---

# Referências Recomendadas

## Livros

| Livro | Autor(es) | Foco |
|---|---|---|
| *Operating System Concepts* ("Dinossauros") | Silberschatz, Galvin, Gagne | Texto-base universal |
| *Modern Operating Systems* | Andrew S. Tanenbaum, Herbert Bos | Teoria e estudos de caso; Minix |
| *Operating Systems: Three Easy Pieces* (OSTEP) | Remzi e Andrea Arpaci-Dusseau | Didático, gratuito online (virtualização, concorrência, persistência) |
| *Operating Systems: Internals and Design Principles* | William Stallings | Abrangente |
| *Linux Kernel Development* | Robert Love | Internals do Linux |
| *Understanding the Linux Kernel* | Bovet, Cesati | Detalhes do kernel |
| *The Linux Programming Interface* | Michael Kerrisk | Syscalls e API POSIX/Linux |
| *Windows Internals* (Partes 1 e 2) | Yosifovich, Ionescu, Russinovich, Solomon | Windows NT |
| *macOS and iOS Internals* (*OS Internals*, vols. I–III) | Jonathan Levin | XNU, Mach, launchd |
| *The Design and Implementation of the FreeBSD Operating System* | McKusick et al. | FreeBSD |
| *Systems Performance* | Brendan Gregg | Análise de desempenho |
| *BPF Performance Tools* | Brendan Gregg | Observabilidade moderna |
| *Sistemas Operacionais Modernos* (tradução) | Tanenbaum | Edição em português |
| *Arquitetura de Sistemas Operacionais* | Francis Berenger Machado, Luiz Paulo Maia | Texto em português |

## Documentação oficial

| Recurso | Conteúdo |
|---|---|
| kernel.org/doc (*The Linux Kernel documentation*) | Documentação do kernel Linux |
| `man 7`, `man 2` (páginas de manual) | Syscalls, conceitos (`man 7 signal`, `man 7 namespaces`) |
| systemd.io e `man systemd.unit` | systemd |
| learn.microsoft.com (Windows, PowerShell, Sysinternals) | Documentação do Windows |
| developer.apple.com/documentation, *Kernel Programming Guide* | macOS/XNU |
| docs.freebsd.org | Handbook e Developers' Handbook |
| minix3.org | Minix 3 |
| QNX Documentation (blackberry.qnx.com) | QNX Neutrino |
| source.android.com | Android Open Source Project |
| docs.docker.com, opencontainers.org | Containers e padrões OCI |
| UEFI Specification (uefi.org) | Boot |

## Cursos e laboratórios

- MIT 6.S081 *Operating System Engineering* (xv6): kernel educativo em C.
- OSTEP *projects* (xv6 e simuladores).
- *Linux From Scratch* e *Operating Systems Development* (osdev.org): construir um SO.
- Sysinternals (Microsoft): Process Explorer, Process Monitor, Autoruns.

> [!tip] Como usar
> Leia o texto-base (Silberschatz ou OSTEP) em paralelo ao vault. Para aprofundar em um SO específico, escolha o livro de internals correspondente e consulte a documentação oficial em caso de dúvida sobre versões atuais.

> [!warning] Verifique edições
> Prefira a edição mais recente de cada livro e confirme na documentação oficial o comportamento da versão que você usa.

## Pontos-chave

- Texto-base: Silberschatz, Tanenbaum ou OSTEP.
- Internals específicos: Love/Kerrisk (Linux), Windows Internals, Levin (macOS).
- Pratique com xv6 e VMs.

## Veja também

[[Mapa de Estudos]] · [[MOC - Extras]]
