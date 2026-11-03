---
titulo: "Pipes"
tags:
  - sistemas-operacionais
  - conceito
  - processos
tipo: conceito
nivel: intermediario
relacionados:
  - "[[IPC - Comunicação entre Processos]]"
  - "[[Criação e Término de Processos]]"
  - "[[Sockets]]"
  - "[[Sinais]]"
---

# Pipes

## Resumo

Um **pipe** é um canal **unidirecional de bytes** gerenciado pelo kernel, com um buffer interno (64 KiB por padrão no Linux). Um processo escreve numa ponta; outro lê na outra. É a base do operador `|` do shell e da filosofia UNIX de compor programas pequenos.

## Tipos

| Tipo | Criação | Característica |
|---|---|---|
| **Anônimo** | `pipe(fd)` | Só entre processos relacionados (herdam os descritores) |
| **Nomeado (FIFO)** | `mkfifo caminho` | Tem nome no sistema de arquivos; processos não relacionados |
| **Named pipe do Windows** | `CreateNamedPipe` | Bidirecional, com suporte a rede |

## Funcionamento

```mermaid
flowchart LR
    W[Processo escritor] -->|write fd1| BUF[Buffer circular no kernel 64 KiB]
    BUF -->|read fd0| R[Processo leitor]
```

- Pipe **cheio**: `write` bloqueia. Pipe **vazio**: `read` bloqueia. Isso dá **controle de fluxo** automático.
- Se todos os leitores fecham, o escritor recebe `SIGPIPE`/`EPIPE`.
- Fim de arquivo (EOF) ocorre quando todos os escritores fecham.

## Exemplo em C

```c
#include <stdio.h>
#include <string.h>
#include <sys/wait.h>
#include <unistd.h>

int main(void) {
    int fd[2];                       // fd[0] leitura, fd[1] escrita
    pipe(fd);

    if (fork() == 0) {               // filho: leitor
        close(fd[1]);                // fecha ponta não usada
        char buf[64];
        ssize_t n = read(fd[0], buf, sizeof buf - 1);
        buf[n] = '\0';
        printf("filho recebeu: %s\n", buf);
        _exit(0);
    }
    close(fd[0]);                    // pai: escritor
    const char *msg = "ola pelo pipe";
    write(fd[1], msg, strlen(msg));
    close(fd[1]);
    wait(NULL);
    return 0;
}
```

## Como o shell implementa `a | b`

```c
// ls | wc -l  (esboço)
int fd[2]; pipe(fd);
if (fork() == 0) { dup2(fd[1], STDOUT_FILENO); close(fd[0]); close(fd[1]); execlp("ls","ls",NULL); }
if (fork() == 0) { dup2(fd[0], STDIN_FILENO);  close(fd[0]); close(fd[1]); execlp("wc","wc","-l",NULL); }
close(fd[0]); close(fd[1]); wait(NULL); wait(NULL);
```

## Linha de comando

```bash
ls -l | grep ".md" | wc -l       # pipeline de três processos
mkfifo /tmp/canal                # pipe nomeado
cat /tmp/canal &                 # leitor
echo "oi" > /tmp/canal           # escritor
rm /tmp/canal
ls -l /proc/$$/fd                # veja pipes como "pipe:[inode]"
```

```powershell
# PowerShell: pipeline passa OBJETOS, não apenas texto
Get-Process | Where-Object CPU -gt 10 | Sort-Object CPU -Descending | Select -First 5
```

## Vantagens e desvantagens

| Vantagens | Desvantagens |
|---|---|
| Muito simples e eficiente | Unidirecional (anônimo) |
| Sincronização e controle de fluxo embutidos | Só fluxo de bytes; sem fronteiras de mensagem |
| Composição de programas | Anônimo exige parentesco entre processos |
| FIFO permite processos independentes | Limitado à mesma máquina |

## Pontos-chave

- Pipe = fila de bytes no kernel com bloqueio automático.
- `dup2` + `pipe` + `fork` formam os pipelines do shell.
- Para comunicação bidirecional ou em rede, use [[Sockets]].

## Veja também

[[IPC - Comunicação entre Processos]] · [[Sockets]] · [[MOC - Processos e Threads]]
