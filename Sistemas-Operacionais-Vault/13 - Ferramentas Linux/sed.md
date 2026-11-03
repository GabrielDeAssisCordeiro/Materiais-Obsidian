---
titulo: "sed"
tags:
  - sistemas-operacionais
  - ferramenta
  - linux
tipo: ferramenta
nivel: intermediario
relacionados:
  - "[[grep]]"
  - "[[awk]]"
  - "[[MOC - Ferramentas Nativas do Linux]]"
---

# sed

## Finalidade

**Stream EDitor**: aplica **comandos de edição** linha a linha em um fluxo (substituir, apagar, inserir, imprimir). O comando mais usado é `s/padrão/substituição/`.

## Sintaxe

```bash
sed 's/antigo/novo/' arq               # 1ª ocorrência por linha
sed 's/antigo/novo/g' arq              # todas (g = global)
sed 's/antigo/novo/gi' arq             # ignora maiúsculas (GNU)
sed -i 's/antigo/novo/g' arq           # edita o arquivo no lugar
sed -i.bak 's/antigo/novo/g' arq       # com backup arq.bak
sed -n '5,10p' arq                     # imprime só as linhas 5 a 10
sed -n '/inicio/,/fim/p' arq           # faixa por padrão
sed '3d' arq                           # apaga a linha 3
sed '/^#/d;/^$/d' arq                  # apaga comentários e linhas vazias
sed '1i\Cabeçalho' arq                 # insere antes da linha 1
sed '$a\Rodapé' arq                    # acrescenta ao final
sed '/padrao/a\Linha depois' arq       # acrescenta depois do casamento
sed '/padrao/c\Linha nova' arq         # troca a linha inteira
sed -E 's/([0-9]+)-([0-9]+)/\2-\1/' arq    # regex estendida e grupos (\1 \2)
sed 's#/usr/local#/opt#g' arq          # outro delimitador (evita escapar /)
sed -e 's/a/b/' -e 's/c/d/' arq        # vários comandos
sed -f comandos.sed arq
sed 's/.*/"&"/' arq                    # & = trecho casado inteiro
sed = arq | sed 'N;s/\n/\t/'           # numera linhas
sed -n '$=' arq                        # conta linhas
sed '1!G;h;$!d' arq                    # inverte a ordem (tac)
```

## Exemplos de administração

```bash
# Alterar configuração (com backup)
sudo sed -i.bak 's/^#\?PermitRootLogin .*/PermitRootLogin no/' /etc/ssh/sshd_config
sudo sshd -t && sudo systemctl reload ssh      # valide antes de recarregar

# Comentar uma linha / descomentar
sed -i 's/^\(.*swap.*\)$/#\1/' /etc/fstab      # comenta linhas de swap
sed -i 's/^#\(.*Include.*\)/\1/' arquivo

# Trocar em vários arquivos
grep -rl "http://" . | xargs sed -i 's#http://#https://#g'
find . -name "*.conf" -exec sed -i 's/8080/9090/g' {} +

# Extrair valor
echo "versao=1.4.2" | sed -n 's/.*=\(.*\)/\1/p'     # 1.4.2

# Remover espaços finais, converter CRLF → LF
sed -i 's/[[:space:]]*$//' arq
sed -i 's/\r$//' arq

# Ver a diferença antes de aplicar
diff <(cat conf) <(sed 's/a/b/g' conf)
```

## Notas importantes

> [!warning] Armadilhas
> - **`-i` altera o arquivo sem volta**: use `-i.bak` ou versione (`git`).
> - macOS/BSD: `sed -i ''` (argumento obrigatório); `\+`/`\?`/`\|` são do GNU (use `-E`).
> - Caracteres especiais (`/`, `&`, `.`, `*`, `[`) precisam de escape ou outro delimitador.
> - Em substituições com variáveis shell, use aspas duplas e cuidado com injeção: `sed "s/$VAR/x/"`.

## Quando preferir outra ferramenta

| Necessidade | Alternativa |
|---|---|
| Colunas e contas | [[awk]] |
| Só buscar | [[grep]] |
| Edição multilinha complexa | `perl -0pe`, Python |
| JSON, YAML, XML | `jq`, `yq`, `xmlstarlet` |

## Pontos-chave

- `s/x/y/g` é 90% do uso; `-n ... p` imprime faixas; `d` apaga.
- `-i.bak` para edição segura.
- Use `-E` para regex estendida e delimitadores alternativos para caminhos.

## Veja também

[[grep]] · [[awk]] · [[MOC - Ferramentas Nativas do Linux]]
