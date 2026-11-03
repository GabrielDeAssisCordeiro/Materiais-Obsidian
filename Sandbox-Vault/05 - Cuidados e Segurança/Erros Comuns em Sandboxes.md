---
tags:
  - seguranca
aliases:
  - "Pitfalls"
tipo: cuidado
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Fuga de Sandbox]]"
  - "[[Endurecimento (Hardening)]]"
---
# Erros Comuns em Sandboxes

| Erro | Consequência | Correção |
|---|---|---|
| Achar que container é VM | Fuga por kernel compartilhado | Usar microVM/VM para código hostil |
| `--privileged` "só para testar" | Contenção anulada | Remover; ajustar capabilities específicas |
| Montar `docker.sock` | Root no host | Nunca em sandboxes |
| Rede liberada por padrão | Exfiltração | `--network none` ou saída filtrada |
| Segredos no ambiente | Vazamento | Gerenciador de segredos, tokens curtos |
| Sem limites de recursos | Negação de serviço | cgroups, timeout |
| Reuso da mesma sandbox | Contaminação entre execuções | Uma sandbox por execução |
| Snapshot sem atualizar | Vulnerabilidades antigas | Atualizar antes do snapshot |
| Pastas compartilhadas abertas | Vazamento/escrita no host | Somente leitura e mínimas |
| Sem logs | Incidentes invisíveis | Logs externos |

## Exercício

Audite uma sandbox sua com esta tabela e marque quantos erros ela comete.

## Veja também

- [[Fuga de Sandbox]]
- [[Endurecimento (Hardening)]]
- [[Limites de Recursos]]
- [[MOC - Cuidados e Segurança]]
