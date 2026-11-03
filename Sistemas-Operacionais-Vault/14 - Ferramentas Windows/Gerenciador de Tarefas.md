---
titulo: "Gerenciador de Tarefas"
tags:
  - sistemas-operacionais
  - ferramenta
  - windows
tipo: ferramenta
nivel: iniciante
relacionados:
  - "[[Resource Monitor (Monitor de Recursos)]]"
  - "[[PowerShell]]"
  - "[[top e htop]]"
  - "[[MOC - Ferramentas Nativas do Windows]]"
---

# Gerenciador de Tarefas

## Finalidade

Ferramenta gráfica para **ver e controlar processos**, acompanhar **desempenho em tempo real**, gerenciar **aplicativos de inicialização**, **usuários** e **serviços**. Equivalente ao [[top e htop|top/htop]].

## Como abrir

`Ctrl+Shift+Esc`, `Ctrl+Alt+Del` → Gerenciador de Tarefas, clique direito na barra de tarefas, ou `taskmgr`.

## Guias

| Guia | O que mostra |
|---|---|
| **Processos** | Apps e processos em segundo plano, com CPU, memória, disco, rede, GPU e consumo de energia; agrupados por aplicativo |
| **Desempenho** | Gráficos de CPU (núcleos, uptime, processos, threads, handles), memória (uso, confirmada, em cache, paginada), disco (tempo ativo, resposta), Ethernet/Wi-Fi, GPU |
| **Histórico de aplicativos** | Uso acumulado por app (UWP) |
| **Inicializar** | Programas que iniciam com o Windows e o **impacto** de cada um: desabilite os desnecessários |
| **Usuários** | Consumo por usuário/sessão |
| **Detalhes** | Lista clássica: **PID**, status, usuário, CPU, memória, arquitetura, descrição; permite afinidade e prioridade |
| **Serviços** | Serviços e atalho para `services.msc` |

## Ações importantes (clique direito → em Detalhes)

| Ação | Efeito |
|---|---|
| **Finalizar tarefa / árvore de processos** | Encerra (como `kill`); a árvore inclui filhos |
| **Definir prioridade** | Tempo real, alta, acima do normal, normal, abaixo, baixa ([[Escalonamento por Prioridades]]) |
| **Definir afinidade** | Restringe a núcleos específicos |
| **Criar arquivo de despejo** | `.dmp` do processo para depuração |
| **Abrir local do arquivo**, **Pesquisar online**, **Ir para serviço(s)** | Investigação rápida |
| **Colunas extras** | Linha de comando, caminho da imagem, handles, threads, *commit size*, *page faults*, operações de E/S |

## Interpretação

| Indicador | Leitura |
|---|---|
| **Memória confirmada** (`Committed`) > RAM + pagefile | Risco de falta de memória virtual |
| **Memória em uso x em cache x em espera** | Cache é recuperável (como o *buff/cache* do Linux) |
| **Disco 100% ativo** com baixa vazão | Gargalo de HDD ou paginação intensa |
| **Processo "System" com CPU alta** | Drivers, antivírus ou interrupções (use Process Explorer/Perfmon) |
| **Muitos handles/threads crescendo** | Possível vazamento |

## Linha de comando equivalente

```powershell
Get-Process | Sort CPU -Descending | Select -First 10 Name, Id, CPU, WS
Stop-Process -Id 1234 -Force
Get-Process notepad | ForEach-Object { $_.PriorityClass = "BelowNormal" }
Get-CimInstance Win32_StartupCommand | Select Name, Command, Location
```

```cmd
tasklist /v | findstr /i chrome
tasklist /svc                       :: serviços hospedados por cada svchost
taskkill /PID 1234 /F /T            :: /T inclui filhos
taskkill /IM notepad.exe /F
```

> [!tip] Process Explorer
> A suíte **Sysinternals** (Microsoft) tem o **Process Explorer** (árvore, DLLs, handles, verificação de assinatura) e **Process Monitor**, muito mais detalhados que o Gerenciador de Tarefas.

## Pontos-chave

- Visão geral rápida; use **Detalhes** para PID, prioridade e afinidade.
- Verifique **Inicializar** para acelerar o boot.
- Para análise profunda: [[Resource Monitor (Monitor de Recursos)]], [[Perfmon (Monitor de Desempenho)]], [[Event Viewer (Visualizador de Eventos)]].

## Veja também

[[Resource Monitor (Monitor de Recursos)]] · [[PowerShell]] · [[MOC - Ferramentas Nativas do Windows]]
