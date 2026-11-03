---
tags:
  - fundamentos
  - seguranca
aliases:
  - "Attack Surface"
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Princípio do Menor Privilégio]]"
  - "[[Isolamento e Contenção]]"
  - "[[Modelo de Ameaças]]"
  - "[[Fuga de Sandbox]]"
---
# Superfície de Ataque

A **superfície de ataque** é o conjunto de pontos pelos quais algo não confiável pode interagir com um sistema: interfaces, chamadas de sistema, portas, dispositivos, formatos de arquivo, APIs.

## Reduzir a superfície é o objetivo de toda sandbox

| Interface exposta | Como reduzir |
|---|---|
| Syscalls do kernel (~350+ no Linux) | Filtro [[Seccomp]], gVisor |
| Dispositivos emulados da VM | MicroVMs com poucos dispositivos (ex.: Firecracker) |
| Rede | `--network none`, regras de saída |
| Sistema de arquivos | Montagens somente leitura, sem montagens do host |
| Pacotes na imagem | Imagens mínimas (*distroless*, Alpine) |
| Socket do Docker | Nunca montar `/var/run/docker.sock` em sandboxes |

> [!danger] Montar o socket do Docker equivale a dar root no host
> Quem controla `/var/run/docker.sock` pode iniciar containers privilegiados. Jamais exponha esse socket a código não confiável.

## Relação com o hipervisor

A fronteira de uma VM é pequena (poucas instruções e dispositivos virtuais), mas **não é zero**: falhas em emulação de dispositivos já geraram fugas. Veja [[Fuga de Sandbox]].

Para raciocinar sobre quais superfícies importam no seu cenário, use um [[Modelo de Ameaças]].

## Exercício

Execute `docker run --rm alpine ls /dev` (em laboratório) e compare com `ls /dev` no host. Que dispositivos o container enxerga? O que isso diz sobre superfície de ataque?

## Veja também

- [[Princípio do Menor Privilégio]]
- [[Isolamento e Contenção]]
- [[Modelo de Ameaças]]
- [[Defesa em Profundidade]]
