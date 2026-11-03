---
titulo: "awk"
tags:
  - sistemas-operacionais
  - ferramenta
  - linux
tipo: ferramenta
nivel: intermediario
relacionados:
  - "[[grep]]"
  - "[[sed]]"
  - "[[ps]]"
  - "[[MOC - Ferramentas Nativas do Linux]]"
---

# awk

## Finalidade

Linguagem de **processamento de texto orientada a campos e linhas**: lê registros, divide em campos (`$1`, `$2`...), aplica padrão → ação. Ideal para relatórios, somas, filtros e transformações de colunas.

## Estrutura

```bash
awk 'BEGIN { inicializa } padrão { ação } END { finaliza }' arquivo
```

- **BEGIN**: antes de ler a primeira linha. **END**: depois da última.
- **Padrão**: regex (`/erro/`), condição (`$3 > 100`), faixa (`/ini/,/fim/`). Sem padrão = todas as linhas.
- **Variáveis**: `$0` linha inteira; `$1..$NF` campos; `NF` nº de campos; `NR` nº da linha global; `FNR` por arquivo; `FS`/`OFS` separadores de entrada/saída; `RS`/`ORS` de registros.

## Sintaxe e exemplos

```bash
awk '{print $1, $3}' arq                         # colunas 1 e 3
awk -F: '{print $1, $7}' /etc/passwd             # separador ':' (usuário e shell)
awk -F, -v OFS=';' '{print $2,$1}' dados.csv     # CSV simples; muda o separador de saída
awk 'NR>1 && $3>100 {print $1}' vendas.txt       # pula cabeçalho, filtra por valor
awk '/erro/ {c++} END {print c+0 " erros"}' log  # conta
awk '{soma+=$2} END {print soma, soma/NR}' arq   # soma e média
awk '{a[$1]++} END {for (k in a) print k, a[k]}' log | sort -k2 -nr    # frequência por chave
awk 'length($0) > 80' arq                        # linhas longas
awk '!visto[$0]++' arq                           # remove duplicadas mantendo a ordem
awk 'NR==5,NR==10' arq                           # faixa de linhas
awk '{ $2=""; print }' arq                       # remove a coluna 2
awk 'BEGIN{printf "%-10s %5s\n","Nome","Qtd"} {printf "%-10s %5d\n",$1,$2}' arq
awk '{print toupper($1), length($1), substr($2,1,3)}' arq
```

## Exemplos de administração

```bash
# Memória por processo (RSS em MiB), ordenado
ps aux | awk 'NR>1 {m[$11]+=$6} END {for (p in m) printf "%8.1f MiB  %s\n", m[p]/1024, p}' | sort -rn | head

# Zumbis
ps -eo stat,pid,cmd | awk '$1 ~ /^Z/'

# Uso de disco acima de 80%
df -h | awk 'NR>1 && $5+0 > 80 {print $6, $5}'

# IPs mais frequentes em access.log (campo 1) e códigos HTTP (campo 9)
awk '{print $1}' access.log | sort | uniq -c | sort -rn | head
awk '{c[$9]++} END {for (s in c) print s, c[s]}' access.log | sort

# Tempo médio de resposta (último campo) por URL
awk '{t[$7]+=$NF; n[$7]++} END {for (u in t) printf "%.3f %s\n", t[u]/n[u], u}' access.log | sort -rn | head

# Converter /proc/meminfo em MiB
awk '/^(MemTotal|MemAvailable):/ {printf "%s %.0f MiB\n", $1, $2/1024}' /proc/meminfo
```

Script em arquivo:

```awk
# relatorio.awk  →  awk -f relatorio.awk vendas.csv
BEGIN { FS=","; print "Relatório" }
NR > 1 { total[$1] += $3 }
END {
    for (cliente in total)
        printf "%-15s R$ %10.2f\n", cliente, total[cliente]
}
```

> [!tip] Versões
> `awk` pode ser **mawk** (rápido) ou **gawk** (GNU: `strftime`, `asort`, `gensub`, `-i inplace`, `--csv` nas versões novas). `awk --version` indica qual.

## Quando usar `awk`, `sed` ou `grep`?

| Tarefa | Ferramenta |
|---|---|
| Achar linhas | [[grep]] |
| Substituir/editar texto | [[sed]] |
| Trabalhar com **colunas, somas, agrupamentos** | **awk** |
| Estruturas complexas (JSON/CSV com aspas) | `jq`, `csvkit`, Python |

## Pontos-chave

- Modelo `padrão { ação }` sobre campos `$1..$NF`.
- Arrays associativos dão contagem e agrupamento em uma linha.
- `BEGIN` e `END` para cabeçalhos e totais.

## Veja também

[[grep]] · [[sed]] · [[MOC - Ferramentas Nativas do Linux]]
