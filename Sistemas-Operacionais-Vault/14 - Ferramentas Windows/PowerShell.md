---
titulo: "PowerShell"
tags:
  - sistemas-operacionais
  - ferramenta
  - windows
tipo: ferramenta
nivel: intermediario
relacionados:
  - "[[cmd (Prompt de Comando)]]"
  - "[[Pipes]]"
  - "[[Regedit (Editor do Registro)]]"
  - "[[MOC - Ferramentas Nativas do Windows]]"
---

# PowerShell

## Finalidade

**Shell e linguagem de script** da Microsoft baseada em **objetos .NET**. Diferente do [[cmd (Prompt de Comando)]] e dos shells UNIX (que passam texto), o *pipeline* do PowerShell passa **objetos** com propriedades e métodos ([[Pipes]]). Há **Windows PowerShell 5.1** (`powershell.exe`, embutido) e **PowerShell 7+** (`pwsh`, multiplataforma, código aberto).

## Conceitos

| Conceito | Descrição |
|---|---|
| **Cmdlet** | Comando `Verbo-Substantivo` (`Get-Process`, `Set-Item`) |
| **Pipeline de objetos** | `Get-Process \| Where CPU -gt 10 \| Sort CPU` |
| **Provedores** | Expõem repositórios como "unidades": arquivos, `HKLM:`/`HKCU:` (registro), `Cert:`, `Env:` |
| **Aliases** | `ls`, `cat`, `ps`, `gci`, `%` (ForEach-Object), `?` (Where-Object) |
| **Política de execução** | `Get-ExecutionPolicy`; `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` |
| **Módulos** | `Import-Module`, `Install-Module` (PowerShell Gallery) |
| **Remoting** | `Enter-PSSession`, `Invoke-Command` (WinRM/SSH) |

## Descoberta

```powershell
Get-Command *process*                  # procurar comandos
Get-Help Get-Process -Examples         # ajuda com exemplos (Update-Help para baixar)
Get-Process | Get-Member               # propriedades e métodos do objeto
Get-Alias; Get-PSDrive
$PSVersionTable
```

## Exemplos do dia a dia

```powershell
# Processos e serviços
Get-Process | Sort WS -Descending | Select -First 5 Name, Id, @{n='MB';e={[int]($_.WS/1MB)}}
Get-Service | Where Status -eq 'Running' | Select -First 5 Name, DisplayName
Restart-Service Spooler; Stop-Process -Name notepad -Force

# Arquivos e texto
Get-ChildItem C:\Logs -Recurse -Filter *.log | Where Length -gt 10MB | Select FullName, Length
Select-String -Path C:\Logs\*.log -Pattern "ERROR" | Select -First 5     # grep
Get-Content app.log -Tail 20 -Wait                                         # tail -f
Get-FileHash arquivo.iso -Algorithm SHA256

# Sistema, disco e rede
Get-ComputerInfo | Select OsName, OsVersion, CsTotalPhysicalMemory
Get-Volume | Select DriveLetter, FileSystemLabel, @{n='Livre(GB)';e={[int]($_.SizeRemaining/1GB)}}
Get-NetTCPConnection -State Listen | Select LocalAddress, LocalPort, OwningProcess
Test-NetConnection exemplo.com -Port 443
Resolve-DnsName exemplo.com

# Registro e eventos
Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion' | Select ProductName, CurrentBuild
Get-WinEvent -FilterHashtable @{LogName='System'; Level=2; StartTime=(Get-Date).AddDays(-1)} | Select -First 5

# Exportar e formatar
Get-Process | Select Name, CPU | Export-Csv processos.csv -NoTypeInformation
Get-Service | ConvertTo-Json | Out-File servicos.json
Get-Process | Format-Table -AutoSize
```

## Script com função

```powershell
function Get-EspacoDisco {
    [CmdletBinding()]
    param([int]$LimitePercentual = 80)
    Get-PSDrive -PSProvider FileSystem | Where-Object { $_.Used -ne $null } | ForEach-Object {
        $total = $_.Used + $_.Free
        $pct = [math]::Round($_.Used / $total * 100, 1)
        [pscustomobject]@{ Unidade = $_.Name; UsadoPct = $pct; Alerta = $pct -gt $LimitePercentual }
    }
}
Get-EspacoDisco -LimitePercentual 70 | Format-Table
```

## Segurança

> [!warning] Boas práticas
> - A *Execution Policy* **não** é fronteira de segurança, apenas proteção contra execuções acidentais.
> - Assine scripts de produção e use **Constrained Language Mode**/AppLocker/WDAC onde necessário.
> - PowerShell é muito usado em ataques ("living off the land"): habilite **Script Block Logging** e **Transcription**; use `-ExecutionPolicy` com consciência.
> - Cuidado com `Invoke-Expression` (`iex`) e `irm | iex` de fontes não confiáveis.

## PowerShell x Bash

| Aspecto | PowerShell | Bash |
|---|---|---|
| Dados no pipeline | Objetos .NET | Texto |
| Nomenclatura | `Verbo-Substantivo` | Curta e variada |
| Plataforma | Windows, Linux, macOS (`pwsh`) | UNIX, WSL |
| Análise de saída | Propriedades (`.Name`) | `grep/awk/cut` |
| Ponto forte | Administração Windows/Azure/AD | Texto, ferramentas UNIX |

## Pontos-chave

- Pipeline de **objetos**; `Get-Help`, `Get-Command` e `Get-Member` ensinam o resto.
- Provedores tratam registro, certificados e variáveis como diretórios.
- Proteja a execução e registre logs de scripts.

## Veja também

[[cmd (Prompt de Comando)]] · [[Regedit (Editor do Registro)]] · [[Task Scheduler (Agendador de Tarefas)]] · [[MOC - Ferramentas Nativas do Windows]]
