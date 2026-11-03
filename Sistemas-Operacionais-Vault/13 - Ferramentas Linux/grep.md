---
titulo: "grep"
tags:
  - sistemas-operacionais
  - ferramenta
  - linux
tipo: ferramenta
nivel: iniciante
relacionados:
  - "[[sed]]"
  - "[[awk]]"
  - "[[journalctl]]"
  - "[[MOC - Ferramentas Nativas do Linux]]"
---

# grep

## Finalidade

Busca **linhas que casam com um padrão** (texto ou expressão regular) em arquivos ou na entrada padrão. Base de quase toda investigação de logs.

## Sintaxe

```bash
grep padrão arquivo
grep -i erro app.log                 # ignora maiúsculas
grep -v "DEBUG" app.log              # inverte: linhas SEM o padrão
grep -n falha app.log                # número da linha
grep -c erro app.log                 # contagem de linhas
grep -o "[0-9]\{1,3\}\(\.[0-9]\{1,3\}\)\{3\}" log   # só o trecho que casa (IPs)
grep -w root /etc/passwd             # palavra inteira
grep -x "ok" lista                   # linha inteira
grep -r "TODO" src/                  # recursivo;  -R segue links
grep -rn --include="*.py" "import os" .
grep -rl "senha" /etc 2>/dev/null    # só nomes dos arquivos
grep -L padrao *.conf                # arquivos SEM o padrão
grep -A3 -B1 "Exception" app.log     # 3 linhas depois e 1 antes;  -C2 contexto
grep -E "erro|falha|fatal" log       # regex estendida (alternância, +, ?)
grep -P "\d{3}-\d{4}" arq            # PCRE (lookaheads, \d)
grep -F "a.b*c" arq                  # texto literal (sem regex)
grep -f padroes.txt log              # vários padrões em arquivo
grep -m5 erro log                    # para após 5 casamentos
grep -q root /etc/passwd && echo achou   # silencioso, usa o código de saída
zgrep erro /var/log/syslog.*.gz      # em arquivos compactados
```

Código de saída: `0` achou, `1` não achou, `2` erro.

## Expressões regulares essenciais

| Padrão | Significado |
|---|---|
| `.` | Qualquer caractere |
| `^` / `$` | Início / fim da linha |
| `*` `+` `?` | 0+ , 1+ , 0 ou 1 (com `-E`) |
| `[abc]` `[^abc]` `[a-z]` | Classe, negação, intervalo |
| `(a\|b)` | Alternância/grupo (`-E`) |
| `{n,m}` | Repetição |
| `\b` | Limite de palavra |
| `[[:digit:]]`, `[[:space:]]` | Classes POSIX |

## Exemplos práticos

```bash
# Tentativas de login falhas por IP
grep "Failed password" /var/log/auth.log | grep -oE "[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+" | sort | uniq -c | sort -rn | head

# Erros 5xx em log de acesso
grep -E '" 5[0-9]{2} ' access.log | wc -l

# Processos sem o próprio grep
ps aux | grep '[n]ginx'          # truque do colchete
pgrep -a nginx                   # melhor alternativa

# Configuração ativa sem comentários e linhas vazias
grep -vE '^\s*(#|$)' /etc/ssh/sshd_config

# Seguir log filtrando
journalctl -u meuapp -f | grep --line-buffered -i erro

# Encontrar quem usa uma função no código
grep -rnw "malloc" --include="*.c" .
```

> [!tip] Alternativas rápidas
> **ripgrep (`rg`)** e **ag** são muito mais velozes em repositórios (respeitam `.gitignore`); `grep` está em todo lugar e é o padrão POSIX.

## Pontos-chave

- Flags de ouro: `-i -n -r -v -E -o -c -A/-B/-C`.
- `-E`/`-P` para regex avançada; `-F` para texto literal.
- Combine com [[awk]], [[sed]] e `sort | uniq -c` para análise.

## Veja também

[[awk]] · [[sed]] · [[MOC - Ferramentas Nativas do Linux]]
