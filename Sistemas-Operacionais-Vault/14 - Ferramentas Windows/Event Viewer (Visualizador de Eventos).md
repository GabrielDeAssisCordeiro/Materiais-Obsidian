---
titulo: "Event Viewer (Visualizador de Eventos)"
tags:
  - sistemas-operacionais
  - ferramenta
  - windows
tipo: ferramenta
nivel: intermediario
relacionados:
  - "[[journalctl]]"
  - "[[PowerShell]]"
  - "[[Gerenciador de Tarefas]]"
  - "[[MOC - Ferramentas Nativas do Windows]]"
---

# Event Viewer (Visualizador de Eventos)

## Finalidade

Console para **ver e filtrar os logs do Windows**: sistema, aplicativos, segurança e logs de serviços/componentes. Equivalente ao [[journalctl]]/`syslog`.

## Como abrir

`eventvwr.msc`, `Win+X` → Visualizador de Eventos.

## Logs principais

| Log | Conteúdo |
|---|---|
| **Windows Logs → Application** | Eventos de aplicativos (falhas, avisos) |
| **Windows Logs → System** | Drivers, serviços, disco, reinícios, kernel |
| **Windows Logs → Security** | **Auditoria**: logons, privilégios, acesso a objetos (requer política de auditoria) |
| **Setup**, **Forwarded Events** | Instalação; eventos coletados de outros hosts |
| **Applications and Services Logs** | Logs por componente: PowerShell, Windows Defender, TaskScheduler, Sysmon, WinRM... |

Níveis: **Informação**, **Aviso**, **Erro**, **Crítico**, **Detalhado** (verbose).

## Eventos importantes (IDs)

| ID | Log | Significado |
|---|---|---|
| 41 | System (Kernel-Power) | **Desligamento inesperado** (queda de energia, travamento) |
| 6005 / 6006 | System | Serviço de log iniciado / parado (boot/desligamento) |
| 6008 | System | Desligamento anterior inesperado |
| 1074 | System | Reinício ou desligamento iniciado por usuário/processo |
| 7034 / 7031 / 7036 | System (SCM) | Serviço terminou inesperadamente / mudou de estado |
| 7045 | System | **Novo serviço instalado** (importante em segurança) |
| 55, 98, 129, 153 | System (disk/ntfs/storahci) | Problemas de disco ou sistema de arquivos |
| 1000 / 1001 | Application | **Falha de aplicativo** / relatório WER |
| 4624 / 4625 | Security | **Logon bem-sucedido / falha** (campo *Logon Type*: 2 interativo, 3 rede, 10 RDP) |
| 4672 | Security | Logon com privilégios especiais |
| 4688 | Security | Criação de processo |
| 4720, 4732 | Security | Conta criada; adicionado a grupo local |
| 1102 | Security | **Log de auditoria limpo** |
| 4104 | PowerShell/Operational | Script block executado |

## Uso: filtros e exibições

- **Filtrar log atual**: por nível, origem, ID, período, palavras-chave.
- **Exibições personalizadas**: "Eventos administrativos" (erros e avisos de tudo).
- **Anexar tarefa a este evento**: executar ação (e-mail/script) quando ocorrer.
- **Assinaturas** (*Subscriptions*): centralizar logs de vários servidores (WEF).

## Linha de comando e PowerShell

```powershell
# Últimos 10 erros do log System
Get-WinEvent -FilterHashtable @{LogName='System'; Level=2} -MaxEvents 10 |
    Select TimeCreated, Id, ProviderName, Message

# Desligamentos inesperados nos últimos 30 dias
Get-WinEvent -FilterHashtable @{LogName='System'; Id=41,6008; StartTime=(Get-Date).AddDays(-30)}

# Falhas de logon (4625) por conta e IP de origem
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4625; StartTime=(Get-Date).AddHours(-24)} |
  ForEach-Object {
    $x = [xml]$_.ToXml()
    [pscustomobject]@{
      Hora    = $_.TimeCreated
      Conta   = ($x.Event.EventData.Data | ? Name -eq 'TargetUserName').'#text'
      Origem  = ($x.Event.EventData.Data | ? Name -eq 'IpAddress').'#text'
    }
  } | Group Conta, Origem | Sort Count -Descending | Select -First 10

# Falhas de aplicativos
Get-WinEvent -FilterHashtable @{LogName='Application'; Id=1000} -MaxEvents 5 | Format-List TimeCreated, Message
```

```cmd
wevtutil el                                   :: lista logs
wevtutil qe System /c:5 /rd:true /f:text      :: últimos 5 eventos, mais recente primeiro
wevtutil epl System C:\backup\system.evtx     :: exporta
wevtutil cl Application                       :: limpa (gera evento 1102 em Security)
```

## Boas práticas

> [!tip] Operação e segurança
> - Ajuste o **tamanho máximo** dos logs (padrão pequeno; Security: 128 MB ou mais) e a retenção.
> - Habilite auditoria avançada (logon, criação de processo com linha de comando) e **Sysmon** para telemetria detalhada.
> - Encaminhe logs a um **SIEM** (WEF, agentes) para não depender do host comprometido.
> - Proteja contra limpeza de logs (alerta no evento 1102/104).

## Pontos-chave

- System, Application e Security são os três logs de rotina.
- IDs 41, 7045, 4624/4625 e 1102 são especialmente reveladores.
- `Get-WinEvent -FilterHashtable` é o jeito eficiente de consultar.

## Veja também

[[journalctl]] · [[PowerShell]] · [[MOC - Ferramentas Nativas do Windows]]
