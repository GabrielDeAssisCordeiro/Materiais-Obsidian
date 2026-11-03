---
tags:
  - como-criar
aliases:
  - "Windows Sandbox .wsb"
tipo: procedimento
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Sandbox de Sistema Operacional]]"
  - "[[Caso - Abertura de Arquivos e Navegação Suspeitos]]"
---
# Criar Sandbox com Windows Sandbox

**Requisitos:** Windows 10/11 Pro, Enterprise ou Education, virtualização habilitada na BIOS/UEFI. (Não disponível na edição Home.)

## 1. Habilitar o recurso (PowerShell como administrador)

```powershell
Enable-WindowsOptionalFeature -Online -FeatureName "Containers-DisposableClientVM" -All
# Reinicie o computador quando solicitado
```

## 2. Arquivo de configuração `.wsb` (laboratório restrito)

Salve como `lab-seguro.wsb` e dê duplo clique:

```xml
<Configuration>
  <VGpu>Disable</VGpu>
  <Networking>Disable</Networking>
  <AudioInput>Disable</AudioInput>
  <VideoInput>Disable</VideoInput>
  <PrinterRedirection>Disable</PrinterRedirection>
  <ClipboardRedirection>Disable</ClipboardRedirection>
  <ProtectedClient>Enable</ProtectedClient>
  <MemoryInMB>4096</MemoryInMB>
  <MappedFolders>
    <MappedFolder>
      <HostFolder>C:\Lab\Entrada</HostFolder>
      <SandboxFolder>C:\Users\WDAGUtilityAccount\Desktop\Entrada</SandboxFolder>
      <ReadOnly>true</ReadOnly>
    </MappedFolder>
  </MappedFolders>
  <LogonCommand>
    <Command>explorer.exe C:\Users\WDAGUtilityAccount\Desktop\Entrada</Command>
  </LogonCommand>
</Configuration>
```

| Opção | Efeito | Recomendação |
|---|---|---|
| `Networking` | Liga/desliga a rede | `Disable` para arquivos suspeitos |
| `ClipboardRedirection` | Área de transferência | `Disable` |
| `ReadOnly` (pasta mapeada) | Impede escrita no host | `true` |
| `ProtectedClient` | Camada extra de proteção da sessão | `Enable` |

> [!warning] Pasta mapeada é uma ponte
> Mapeie **apenas** uma pasta de entrada, somente leitura. Nunca mapeie `C:\` ou o perfil do usuário.

> [!question] Verificar na documentação oficial
> Opções do `.wsb` variam conforme a versão do Windows; confirme na documentação da Microsoft.

## Exercício

Crie o `.wsb` acima, abra-o e confirme que não há internet e que a pasta de entrada não aceita gravação.

## Veja também

- [[Sandbox de Sistema Operacional]]
- [[Caso - Abertura de Arquivos e Navegação Suspeitos]]
- [[Fuga de Sandbox]]
- [[MOC - Como Criar]]
