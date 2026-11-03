---
titulo: "Controle de Acesso"
tags:
  - sistemas-operacionais
  - conceito
  - seguranca
tipo: conceito
nivel: intermediario
relacionados:
  - "[[Autenticação]]"
  - "[[Permissões de Arquivos]]"
  - "[[SELinux e AppArmor]]"
  - "[[Sandboxing]]"
---

# Controle de Acesso

## Resumo

Após autenticar, o SO decide, para cada **sujeito** (processo/usuário) e **objeto** (arquivo, socket, memória), se uma **operação** é permitida. A decisão é feita pelo **monitor de referência** do kernel, a cada acesso.

## Modelos

| Modelo | Quem decide | Exemplo |
|---|---|---|
| **DAC** (discricionário) | O **dono** do objeto define as permissões | rwx do UNIX, ACLs NTFS |
| **MAC** (obrigatório) | Uma **política central** do sistema; o dono não pode alterar | SELinux, AppArmor, SMACK ([[SELinux e AppArmor]]) |
| **RBAC** (por papéis) | Permissões atribuídas a **papéis**; usuários assumem papéis | Grupos do AD, `sudo` por grupo, Kubernetes RBAC |
| **ABAC** (por atributos) | Regras sobre atributos do sujeito, objeto e contexto | Políticas em nuvem (IAM) |
| **Capabilities** | O sujeito carrega **tokens de autoridade** | Linux capabilities, seL4 |

> [!info] DAC não basta
> Em DAC, um processo comprometido herda **todo o poder do usuário** (ex.: lê `~/.ssh`). MAC e sandbox limitam esse dano.

## Matriz de acesso

|  | arquivo1 | arquivo2 | impressora |
|---|---|---|---|
| Ana | r, w | r | imprimir |
| Bruno | r | r, w | - |

Implementações: **ACL** (por coluna: lista por objeto) ou **capacidades** (por linha: lista por sujeito).

## Capabilities do Linux

O poder de **root** é dividido em ~40 capacidades, permitindo conceder só o necessário.

| Capability | Permite |
|---|---|
| `CAP_NET_BIND_SERVICE` | Abrir portas < 1024 |
| `CAP_NET_ADMIN` | Configurar rede |
| `CAP_SYS_ADMIN` | Muitíssimas operações (quase root) |
| `CAP_DAC_OVERRIDE` | Ignorar permissões de arquivo |
| `CAP_KILL`, `CAP_SYS_PTRACE`, `CAP_CHOWN`... | Operações específicas |

```bash
# Servidor web sem root, só com a capacidade de abrir porta 80
sudo setcap 'cap_net_bind_service=+ep' /usr/local/bin/meu_servidor
getcap /usr/local/bin/meu_servidor
capsh --print                                # capacidades do shell atual
grep Cap /proc/self/status                   # máscaras em hexadecimal
# Em contêineres: descartar tudo e adicionar o mínimo
docker run --cap-drop ALL --cap-add NET_BIND_SERVICE nginx
```

## UID efetivo, setuid e `sudo`

- Cada processo tem UID **real**, **efetivo** e **salvo**; o kernel usa o **efetivo** para verificar permissões.
- `setuid` troca o UID efetivo para o dono do arquivo executável; deve ser mínimo e cuidadosamente programado.
- `sudo` executa comandos como outro usuário conforme `sudoers` (RBAC simples).

```c
// Servidor que abre a porta 80 como root e descarta privilégios em seguida
bind(sock, ...);               // precisa de privilégio
setgid(1000); setuid(1000);    // abandona (grupo primeiro, depois usuário)
// A partir daqui roda sem privilégios
```

## Windows

| Elemento | Descrição |
|---|---|
| **SID** | Identificador de segurança de usuário/grupo |
| **Access token** | Contém SID, grupos, **privilégios** (`SeDebugPrivilege`...), nível de integridade |
| **ACL/ACE** | Lista de permitir/negar em cada objeto |
| **UAC** | Executa como usuário padrão e eleva sob consentimento |
| **Níveis de integridade** | Baixo, médio, alto, sistema; processo de integridade baixa não escreve em objetos de integridade mais alta (base do sandbox do navegador) |
| **AppLocker, WDAC** | Controle de quais programas rodam |

```powershell
whoami /priv
icacls C:\dados
Get-Acl C:\dados | Format-List
```

## macOS

Permissões UNIX + ACLs + **TCC** (consentimento do usuário por app para câmera, arquivos, etc.) + **SIP** (proteção de integridade do sistema, nem o root altera `/System`) + **Gatekeeper/notarização**.

```bash
csrutil status
tccutil reset Camera
codesign -dv --verbose=4 /Applications/App.app
```

## Auditoria

```bash
sudo ausearch -m avc -ts recent              # negativas de MAC (auditd)
sudo auditctl -w /etc/passwd -p wa -k passwd # observa alterações
journalctl _AUDIT_TYPE_NAME=USER_AUTH
```

## Vantagens e desvantagens

| Modelo | Vantagens | Desvantagens |
|---|---|---|
| DAC | Simples, flexível | Vulnerável a erros e a processos comprometidos |
| MAC | Contenção forte, política central | Complexidade; difícil de administrar |
| RBAC | Escala em organizações | "Explosão de papéis" |
| Capabilities | Menor privilégio fino | Concessões amplas (`CAP_SYS_ADMIN`) enfraquecem o modelo |

## Pontos-chave

- DAC (dono decide) x MAC (política central).
- Divida o poder de root com capabilities.
- Use auditoria para detectar negações e abusos.

## Veja também

[[Autenticação]] · [[SELinux e AppArmor]] · [[Sandboxing]] · [[MOC - Segurança - SO]]
