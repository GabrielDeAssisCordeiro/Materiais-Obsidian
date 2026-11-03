---
titulo: "SFC e DISM"
tags:
  - sistemas-operacionais
  - ferramenta
  - windows
tipo: ferramenta
nivel: intermediario
relacionados:
  - "[[NTFS]]"
  - "[[cmd (Prompt de Comando)]]"
  - "[[PowerShell]]"
  - "[[MOC - Ferramentas Nativas do Windows]]"
---

# SFC e DISM

## Finalidade

Ferramentas de **reparo da integridade do Windows**, executadas em prompt **elevado** (Administrador):

- **SFC** (*System File Checker*): verifica e substitui **arquivos de sistema protegidos** corrompidos ou alterados.
- **DISM** (*Deployment Image Servicing and Management*): repara o **armazenamento de componentes** (`WinSxS`, a "fonte" que o SFC usa) e gerencia imagens do Windows (`.wim`/`.esd`, online ou offline).

## Como se relacionam

```mermaid
flowchart LR
    A[Sistema em execução] -->|SFC verifica| B[Arquivos protegidos]
    B -->|compara com| C[Component Store - WinSxS]
    C -->|se corrompido: DISM RestoreHealth baixa/obtém fonte| D[Windows Update ou mídia de instalação]
    C -->|reparado| B
```

Ordem recomendada: **DISM primeiro** (conserta a fonte) e **depois SFC** (conserta os arquivos).

## Uso

```cmd
:: 1) Verificar saúde da imagem (rápido, sem reparar)
DISM /Online /Cleanup-Image /CheckHealth
DISM /Online /Cleanup-Image /ScanHealth          :: verificação mais profunda
:: 2) Reparar usando o Windows Update como fonte
DISM /Online /Cleanup-Image /RestoreHealth
:: 2b) Reparar usando mídia local (ISO montada em D:)
DISM /Online /Cleanup-Image /RestoreHealth /Source:WIM:D:\sources\install.wim:1 /LimitAccess
:: 3) Verificar e reparar arquivos de sistema
sfc /scannow
sfc /verifyonly                                  :: só verifica
sfc /scanfile=C:\Windows\System32\kernel32.dll   :: um arquivo
:: Reparo offline (a partir do WinRE)
sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows
```

Limpeza do component store (libera espaço):

```cmd
DISM /Online /Cleanup-Image /AnalyzeComponentStore
DISM /Online /Cleanup-Image /StartComponentCleanup /ResetBase   :: remove versões antigas (sem desinstalar atualizações)
```

PowerShell:

```powershell
Repair-WindowsImage -Online -ScanHealth
Repair-WindowsImage -Online -RestoreHealth
Get-WindowsOptionalFeature -Online | Where State -eq Enabled | Select -First 5 FeatureName
```

## Resultados do `sfc /scannow`

| Mensagem | Significado / ação |
|---|---|
| *Não encontrou nenhuma violação de integridade* | Sistema íntegro |
| *Encontrou arquivos corrompidos e os reparou com êxito* | OK; reinicie |
| *Encontrou arquivos corrompidos e não conseguiu corrigir alguns* | Rode **DISM /RestoreHealth** e repita o SFC; veja `CBS.log` |
| *Não pôde executar a operação solicitada* | Reinicie, execute em modo seguro ou pelo WinRE |

Registros:

```cmd
findstr /c:"[SR]" %windir%\Logs\CBS\CBS.log > "%userprofile%\Desktop\sfclog.txt"
:: DISM: C:\Windows\Logs\DISM\dism.log
```

## Outros reparos relacionados

```cmd
chkdsk C: /scan                  :: verifica o NTFS online (/f /r exigem reinício)
chkdsk C: /f /r
bcdedit /enum                    :: boot
bootrec /fixmbr & bootrec /fixboot & bootrec /rebuildbcd    :: WinRE
wmic logicaldisk get name,volumename,filesystem   :: ou Get-Volume
sfc /scannow && DISM /Online /Cleanup-Image /RestoreHealth
```

> [!tip] Quando usar
> Sintomas: telas azuis recorrentes, "recursos do Windows" que não funcionam, falha de `Windows Update`, apps do sistema que travam, erros `0x800f081f`/`0x80073712`. Antes, descarte problemas de disco ([[NTFS]] com `chkdsk`) e de memória (Diagnóstico de Memória do Windows).

## Limitações

> [!warning]
> SFC/DISM não corrigem **drivers de terceiros**, **dados de usuário** nem configurações do registro. Se o component store estiver muito danificado e sem fonte válida, considere **Redefinir este PC / reparo de atualização in-place** (instalar a mesma versão por cima, mantendo arquivos e apps).

## Pontos-chave

- DISM conserta a "fonte"; SFC conserta os arquivos usando essa fonte.
- Execute como administrador, nessa ordem: `DISM /RestoreHealth` → `sfc /scannow`.
- Logs em `CBS.log` e `dism.log`.

## Veja também

[[cmd (Prompt de Comando)]] · [[NTFS]] · [[MOC - Ferramentas Nativas do Windows]]
