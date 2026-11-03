---
titulo: "chmod e chown"
tags:
  - sistemas-operacionais
  - ferramenta
  - linux
tipo: ferramenta
nivel: iniciante
relacionados:
  - "[[Permissões de Arquivos]]"
  - "[[Controle de Acesso]]"
  - "[[Inodes]]"
  - "[[MOC - Ferramentas Nativas do Linux]]"
---

# chmod e chown

## Finalidade

- **`chmod`**: altera o **modo** (permissões `rwx`, setuid/setgid/sticky).
- **`chown`** / **`chgrp`**: alteram **dono** e **grupo**.
Modelo completo em [[Permissões de Arquivos]].

## Sintaxe do `chmod`

```bash
chmod 644 arquivo                 # numérico: rw-r--r--
chmod 755 script.sh               # rwxr-xr-x
chmod 600 ~/.ssh/id_ed25519       # só o dono
chmod u+x script.sh               # simbólico: dono ganha x
chmod g-w,o-rwx dados.txt         # remove w do grupo e tudo dos outros
chmod a+r publico.txt             # todos leem
chmod u=rwx,g=rx,o= pasta
chmod -R go-rwx ~/.ssh            # recursivo
chmod +x script                   # x para todos (respeita umask)
chmod 2775 pasta_compartilhada    # setgid: novos arquivos herdam o grupo
chmod 1777 /tmp/pub               # sticky: só o dono remove seus arquivos
chmod 4755 programa               # setuid (cuidado!)
chmod --reference=modelo alvo     # copia o modo de outro arquivo
find . -type d -exec chmod 755 {} +   # pastas
find . -type f -exec chmod 644 {} +   # arquivos
```

Tabela rápida (soma: `r=4`, `w=2`, `x=1`):

| Octal | Simbólico | Uso típico |
|---|---|---|
| 600 | `rw-------` | Chaves privadas, segredos |
| 640 | `rw-r-----` | Arquivos de configuração com grupo |
| 644 | `rw-r--r--` | Arquivos comuns |
| 700 | `rwx------` | Diretório privado |
| 750 | `rwxr-x---` | Programas/pastas do grupo |
| 755 | `rwxr-xr-x` | Executáveis e diretórios públicos |
| 777 | `rwxrwxrwx` | **Evite** |

## Sintaxe do `chown`

```bash
sudo chown ana arquivo                 # dono
sudo chown ana:devs arquivo            # dono e grupo
sudo chown :devs arquivo               # só o grupo (ou: chgrp devs arquivo)
sudo chown -R www-data: /var/www       # recursivo, grupo = grupo de login do usuário
sudo chown --reference=modelo alvo
sudo chown -h ana link_simbolico       # altera o link, não o alvo
sudo chown -R 1000:1000 ./dados        # por UID:GID numéricos (útil com volumes Docker)
```

Apenas **root** muda o dono; o dono pode mudar o grupo para um grupo do qual faça parte.

## Verificação

```bash
ls -l arquivo; ls -ld pasta            # modo e dono
stat -c '%A %a %U:%G %n' arquivo       # -rw-r--r-- 644 ana:devs arquivo
namei -l /var/www/html/index.html      # permissões de cada componente do caminho
id; groups                             # meus UID, GID e grupos
getfacl arquivo                        # ACLs
```

## Erros comuns

| Sintoma | Causa | Solução |
|---|---|---|
| `Permission denied` ao acessar arquivo | Falta `x` em algum **diretório** do caminho | `namei -l caminho`; `chmod +x` na pasta |
| Script não executa | Sem `x` ou sistema montado `noexec` | `chmod +x`; `mount | grep noexec` |
| Servidor web não lê | Dono/grupo errados ou SELinux | `chown`, `chmod`; `ls -Z`, `restorecon` |
| `chmod -R 777` "resolve" | Abre falha de segurança | Corrija dono/grupo e use o menor modo |
| `ssh` ignora a chave | Modo muito aberto | `chmod 700 ~/.ssh; chmod 600 ~/.ssh/*` |

> [!warning] Cuidado com `-R`
> `chmod -R` e `chown -R` em `/` ou em diretórios errados quebram o sistema. Confira o caminho, use `-v`/`--preserve-root` e teste com `find ... -print` antes.

## Pontos-chave

- Octal para modos exatos; simbólico para ajustes.
- `x` em diretório = atravessar.
- Menor privilégio: 600/640/644/755; evite 777; use grupos e `setgid` para colaboração.

## Veja também

[[Permissões de Arquivos]] · [[Controle de Acesso]] · [[MOC - Ferramentas Nativas do Linux]]
