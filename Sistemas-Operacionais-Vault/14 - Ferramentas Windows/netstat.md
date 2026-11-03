---
titulo: "netstat"
tags:
  - sistemas-operacionais
  - ferramenta
  - windows
tipo: ferramenta
nivel: iniciante
relacionados:
  - "[[ss]]"
  - "[[Sockets]]"
  - "[[Resource Monitor (Monitor de Recursos)]]"
  - "[[PowerShell]]"
  - "[[MOC - Ferramentas Nativas do Windows]]"
---

# netstat

## Finalidade

Mostra **conexões de rede**, **portas em escuta**, tabela de roteamento e estatísticas de protocolos. Equivalente ao [[ss]] (e ao antigo `netstat` do Linux). Trabalha com [[Sockets]].

## Sintaxe

```cmd
netstat                      :: conexões TCP estabelecidas
netstat -a                   :: todas (escuta e estabelecidas), TCP e UDP
netstat -n                   :: endereços/portas numéricos (sem DNS)
netstat -o                   :: inclui o PID do processo dono
netstat -b                   :: nome do executável (requer Administrador; lento)
netstat -ano                 :: combinação mais usada
netstat -p tcp               :: filtra protocolo (tcp, udp, tcpv6, udpv6)
netstat -e -s                :: estatísticas Ethernet / por protocolo
netstat -r                   :: tabela de roteamento (= route print)
netstat -ano 5               :: repete a cada 5 segundos
netstat -an | findstr :443
netstat -ano | findstr LISTENING
```

## Saída comentada

```text
C:\> netstat -ano | findstr LISTENING
  Proto  Endereço Local        Endereço Externo     Estado       PID
  TCP    0.0.0.0:135           0.0.0.0:0            LISTENING    1112   # RPC
  TCP    0.0.0.0:445           0.0.0.0:0            LISTENING    4      # SMB (PID 4 = System)
  TCP    127.0.0.1:5432        0.0.0.0:0            LISTENING    5120   # PostgreSQL só local
  TCP    192.168.1.20:50234    142.250.0.1:443      ESTABLISHED  8844   # navegador
# 0.0.0.0 = todas as interfaces (exposto à rede); 127.0.0.1 = só máquina local
```

Para descobrir quem é o PID:

```cmd
tasklist /fi "PID eq 8844"
tasklist /svc /fi "PID eq 1112"        :: serviços hospedados no svchost
```

| Estado | Significado |
|---|---|
| `LISTENING` | Servidor aguardando |
| `ESTABLISHED` | Conexão ativa |
| `TIME_WAIT` | Encerrada recentemente, aguardando |
| `CLOSE_WAIT` | O outro lado fechou; o **aplicativo local ainda não** (possível vazamento) |
| `SYN_SENT` / `SYN_RECEIVED` | Handshake; muitos `SYN_RECEIVED` pode indicar ataque SYN flood |

## Receitas

```cmd
:: Quem usa a porta 8080?
for /f "tokens=5" %p in ('netstat -ano ^| findstr :8080 ^| findstr LISTENING') do tasklist /fi "PID eq %p"
:: Encerrar o processo que ocupa a porta
taskkill /PID <PID> /F
:: Contar conexões por estado
netstat -an | find /c "ESTABLISHED"
```

## Equivalentes modernos em PowerShell

```powershell
Get-NetTCPConnection -State Listen |
  Select LocalAddress, LocalPort, OwningProcess,
         @{n='Processo';e={(Get-Process -Id $_.OwningProcess).ProcessName}} |
  Sort LocalPort

Get-NetTCPConnection -State Established | Group RemoteAddress | Sort Count -Descending | Select -First 5
Get-NetUDPEndpoint | Select LocalAddress, LocalPort, OwningProcess
Test-NetConnection exemplo.com -Port 443          # testa conectividade
Get-NetRoute | Where DestinationPrefix -eq '0.0.0.0/0'
```

> [!tip] Conexões e segurança
> Revise **portas em escuta** (`0.0.0.0`) e conexões externas incomuns. Processos desconhecidos com conexões a IPs estrangeiros merecem análise (hash, assinatura, VirusTotal). O [[Resource Monitor (Monitor de Recursos)]] (guia Rede) e o **TCPView** (Sysinternals) oferecem visão gráfica.

## Limitações

- Foto instantânea (use `netstat 5` ou ferramentas de captura como **Wireshark**/`pktmon` para tráfego).
- `-b` exige administrador e pode ser lento.
- Não mostra conteúdo nem largura de banda por conexão.

## Pontos-chave

- `netstat -ano` + `tasklist` ligam portas a processos.
- Atenção a `0.0.0.0` (exposto) e a `CLOSE_WAIT` acumulado.
- Em scripts modernos, prefira `Get-NetTCPConnection`.

## Veja também

[[ss]] · [[Resource Monitor (Monitor de Recursos)]] · [[MOC - Ferramentas Nativas do Windows]]
