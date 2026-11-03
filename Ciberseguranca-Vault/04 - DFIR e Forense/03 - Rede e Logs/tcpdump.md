---
titulo: "tcpdump"
tipo: ferramenta
nome: "tcpdump"
categoria: "DFIR/Rede-e-Logs"
subcategoria: "Captura de Pacotes via CLI"
plataformas: ["Linux", "macOS", "BSD"]
licenca: "BSD-3-Clause"
linguagem: "C"
mitre_attack: []
nivel: iniciante
situacao: ativo
link_oficial: "https://www.tcpdump.org/"
tags:
  - ciberseguranca
  - ferramenta
  - dfir/rede
---

# tcpdump

> Utilitário de linha de comando para captura de pacotes de rede, baseado na biblioteca libpcap.

## Como funciona
Coloca a interface de rede em modo promíscuo (capturando todo tráfego que passa pelo segmento, não apenas o destinado ao próprio host) e aplica filtros BPF (Berkeley Packet Filter) para selecionar, já no momento da captura, apenas o tráfego de interesse, salvando o resultado em formato PCAP compatível com Wireshark para análise posterior.

## Como usar
`tcpdump -i eth0 -w captura.pcap port 443` captura todo tráfego na porta 443 e salva em arquivo; filtros mais complexos combinam `and`/`or` (ex.: `host 10.0.0.5 and port 80`), e `-A` exibe o conteúdo ASCII dos pacotes diretamente no terminal.

## Casos de uso
- Captura rápida de tráfego em servidores sem interface gráfica
- Coleta de evidência de rede durante resposta a incidente

## Alternativas
[[Wireshark]]

## Categoria
[[MOC - Rede e Logs]]

## Link oficial
https://www.tcpdump.org/
