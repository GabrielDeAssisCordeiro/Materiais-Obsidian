---
tags:
  - seguranca
aliases:
  - "USB passthrough"
tipo: cuidado
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Vazamento por Pastas Compartilhadas e Área de Transferência]]"
  - "[[Criar Sandbox com VMs]]"
---
# Dispositivos USB e Periféricos

O *passthrough* de USB entrega o dispositivo físico diretamente ao convidado, ampliando a superfície de ataque (firmware, controladores).

- Não conecte dispositivos USB do host a VMs de análise de malware.
- Desabilite controladores USB virtuais quando não precisar.
- Mídias externas contendo amostras: use estação separada e escaneie.
- Em sentido inverso, **não** insira mídias de origem desconhecida no host do laboratório.

```bash
VBoxManage modifyvm lab01 --usbxhci off --usbehci off --usbohci off
```

> [!question] Verificar na documentação oficial
> Opções de USB do VirtualBox variam entre versões e exigem extension pack para USB 2/3.

## Veja também

- [[Vazamento por Pastas Compartilhadas e Área de Transferência]]
- [[Fuga de Sandbox]]
- [[MOC - Cuidados e Segurança]]
