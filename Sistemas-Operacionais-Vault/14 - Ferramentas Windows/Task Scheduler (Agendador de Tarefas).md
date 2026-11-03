---
titulo: "Task Scheduler (Agendador de Tarefas)"
tags:
  - sistemas-operacionais
  - ferramenta
  - windows
tipo: ferramenta
nivel: intermediario
relacionados:
  - "[[cron]]"
  - "[[PowerShell]]"
  - "[[Event Viewer (Visualizador de Eventos)]]"
  - "[[MOC - Ferramentas Nativas do Windows]]"
---

# Task Scheduler (Agendador de Tarefas)

## Finalidade

Executa **programas ou scripts** por agenda ou por **gatilhos** (eventos). Equivalente ao [[cron]] e aos timers do systemd, com mais recursos: eventos, logon, ociosidade, bloqueio de sessão, execução como outro usuário ou SYSTEM.

## Como abrir

`taskschd.msc`, ou Iniciar → *Agendador de Tarefas*.

## Estrutura de uma tarefa

| Aba | Conteúdo |
|---|---|
| **Geral** | Nome, descrição, **conta de execução**, "Executar estando o usuário conectado ou não", **privilégios mais altos**, configurar para qual versão do Windows |
| **Gatilhos** | Quando: única vez, diária/semanal/mensal, **ao iniciar**, **ao fazer logon**, **ao ocorrer um evento** (log/ID), ociosidade, bloqueio/desbloqueio, conexão de sessão remota |
| **Ações** | O que: iniciar programa (com argumentos e diretório inicial); e-mail e mensagem estão obsoletos |
| **Condições** | Só se ocioso, só em tomada, só com rede, acordar o computador |
| **Configurações** | Executar o quanto antes se perdeu o agendamento, repetir em falhas, parar se durar mais de X, regra para instância já em execução (não iniciar nova / fila / parar existente) |
| **Histórico** | Eventos da tarefa (habilitar em *Ação → Habilitar histórico de todas as tarefas*) |

> [!tip] "Executar o quanto antes após uma inicialização perdida"
> Resolve o que o cron não faz: se o PC estava desligado, a tarefa roda ao ligar (como o `anacron` ou `Persistent=true`).

## PowerShell (recomendado para automação)

```powershell
$acao     = New-ScheduledTaskAction -Execute "powershell.exe" `
              -Argument "-NoProfile -ExecutionPolicy Bypass -File C:\Scripts\backup.ps1"
$gatilho  = New-ScheduledTaskTrigger -Daily -At 02:30
$conf     = New-ScheduledTaskSettingsSet -StartWhenAvailable -RestartCount 3 `
              -RestartInterval (New-TimeSpan -Minutes 5) -MultipleInstances IgnoreNew
$principal= New-ScheduledTaskPrincipal -UserId "SYSTEM" -LogonType ServiceAccount -RunLevel Highest

Register-ScheduledTask -TaskName "BackupDiario" -Action $acao -Trigger $gatilho `
  -Settings $conf -Principal $principal -Description "Backup às 02:30"

Get-ScheduledTask | Where State -ne Disabled | Select TaskName, State, TaskPath
Start-ScheduledTask -TaskName "BackupDiario"
Get-ScheduledTaskInfo -TaskName "BackupDiario" | Select LastRunTime, LastTaskResult, NextRunTime
Disable-ScheduledTask -TaskName "BackupDiario"
Unregister-ScheduledTask -TaskName "BackupDiario" -Confirm:$false
```

## `schtasks` (CMD)

```cmd
schtasks /create /tn "Limpeza" /tr "C:\Scripts\limpa.bat" /sc daily /st 03:00 /ru SYSTEM /rl HIGHEST
schtasks /create /tn "NaInicializacao" /tr "C:\app\start.exe" /sc onstart /ru SYSTEM
schtasks /create /tn "AoLogon" /tr "notepad.exe" /sc onlogon
schtasks /query /fo table /v
schtasks /run /tn "Limpeza"
schtasks /delete /tn "Limpeza" /f
```

## Leitura do resultado

| `LastTaskResult` | Significado |
|---|---|
| `0` | Sucesso |
| `1` | Erro geral do programa/código de saída 1 |
| `0x41301` | Tarefa em execução |
| `0x41303` | Tarefa ainda não executou |
| `0x80070005` | Acesso negado (permissões/conta) |
| `0x8007010B` | Diretório inválido ("Iniciar em") |
| `0xC000013A` | Interrompida (Ctrl+C) |

Histórico e eventos: `Microsoft-Windows-TaskScheduler/Operational` no [[Event Viewer (Visualizador de Eventos)]] (IDs 100 iniciada, 102 concluída, 201 ação concluída, 111 encerrada).

## Segurança

> [!warning] Persistência e escalonamento
> Tarefas agendadas são método comum de **persistência** e execução como SYSTEM. Audite `C:\Windows\System32\Tasks`, restrinja quem pode criá-las, use contas de serviço com **menor privilégio** (gMSA) e monitore o evento 4698 (tarefa criada) no log Security.

## Armadilhas

- Caminho com espaços sem aspas; **diretório inicial** não definido (scripts que usam caminhos relativos).
- Senha da conta expirada → falha ("Executar estando o usuário conectado ou não" requer credencial).
- Mapeamentos de rede (`Z:`) não existem em contexto de tarefa: use **UNC** (`\\srv\share`).
- Sempre registre saída: `>> C:\logs\tarefa.log 2>&1` ou `Start-Transcript`.

## cron x Task Scheduler

| Aspecto | cron | Task Scheduler |
|---|---|---|
| Gatilhos | Só tempo | Tempo, eventos, logon, ociosidade, boot |
| Tarefas perdidas | Não | Sim (opção) |
| Conta e privilégios | Usuário do crontab | Qualquer conta/SYSTEM, elevação |
| Histórico/log | Syslog | Histórico integrado |
| Formato | Texto simples | XML/GUI/PowerShell |

## Pontos-chave

- Gatilhos ricos (eventos, logon, boot) e execução como SYSTEM.
- Use `Register-ScheduledTask` para automação e UNC para rede.
- Audite tarefas: são vetor de persistência.

## Veja também

[[cron]] · [[PowerShell]] · [[MOC - Ferramentas Nativas do Windows]]
