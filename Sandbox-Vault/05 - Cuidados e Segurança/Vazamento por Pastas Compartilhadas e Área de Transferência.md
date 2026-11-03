---
tags:
  - seguranca
aliases:
  - "Shared folders"
  - "Clipboard"
  - "Guest Additions"
tipo: cuidado
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Fuga de Sandbox]]"
  - "[[Criar Sandbox com VMs]]"
  - "[[Criar Sandbox com Windows Sandbox]]"
---
# Vazamento por Pastas Compartilhadas e Área de Transferência

Recursos de conveniência de VMs e sandboxes criam **canais bidirecionais** entre o convidado e o host.

| Canal | Risco | Mitigação |
|---|---|---|
| Pastas compartilhadas | Escrita no host; leitura de dados sensíveis | Desativar ou usar somente leitura, uma única pasta de entrada |
| Área de transferência | Exfiltração e injeção de conteúdo | Desativar |
| Arrastar e soltar | Mesmo risco | Desativar |
| Guest Additions/Tools | Mais código e drivers com acesso privilegiado | Instalar só se necessário |
| Impressoras/áudio/câmera | Superfície adicional | Desativar |

```bash
# VirtualBox
VBoxManage modifyvm lab01 --clipboard-mode disabled --draganddrop disabled
```

> [!warning] Transferência de arquivos
> Prefira um canal unidirecional (ISO somente leitura, pasta somente leitura) e verifique hashes (`sha256sum`).

## Exercício

Liste todos os canais de comunicação habilitados na sua VM de laboratório e desative os desnecessários.

## Veja também

- [[Fuga de Sandbox]]
- [[Dispositivos USB e Periféricos]]
- [[Criar Sandbox com VMs]]
- [[MOC - Cuidados e Segurança]]
