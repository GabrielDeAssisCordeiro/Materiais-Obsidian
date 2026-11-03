---
titulo: "cmd (Prompt de Comando)"
tags:
  - sistemas-operacionais
  - ferramenta
  - windows
tipo: ferramenta
nivel: iniciante
relacionados:
  - "[[PowerShell]]"
  - "[[netstat]]"
  - "[[SFC e DISM]]"
  - "[[MOC - Ferramentas Nativas do Windows]]"
---

# cmd (Prompt de Comando)

## Finalidade

Interpretador de comandos **clássico** do Windows (`cmd.exe`), herdeiro do COMMAND.COM do MS-DOS. Executa comandos internos, utilitários externos e arquivos em lote (`.bat`/`.cmd`). Menos poderoso que o [[PowerShell]], mas presente em tudo e útil para ferramentas de rede e reparo.

## Comandos essenciais

```cmd
dir /a /o:-s              :: lista incluindo ocultos, ordenado por tamanho
cd /d D:\Projetos         :: /d troca de unidade também
cls                       :: limpa a tela
copy origem destino       :: ou xcopy / robocopy (melhor)
robocopy C:\dados D:\bkp /MIR /R:2 /W:5 /LOG:bkp.log   :: espelhamento robusto
move, ren, del, rmdir /s /q pasta, mkdir
type arquivo.txt          :: cat
more < arquivo.txt
find "erro" log.txt       :: busca simples;  findstr = grep com regex limitado
findstr /i /s /n "senha" *.config
echo %PATH%               :: variáveis: %VAR%
set VAR=valor             :: define na sessão;  setx VAR valor  persiste
where notepad             :: localiza executável
tree /f
attrib +h arquivo         :: atributos
```

## Informações do sistema e rede

```cmd
systeminfo                :: SO, hotfixes, memória, domínio
ver & hostname & whoami /all
tasklist /v               :: processos;   taskkill /PID 1234 /F /T
ipconfig /all             :: IP, DNS, MAC
ipconfig /flushdns & ipconfig /renew
ping -n 4 8.8.8.8
tracert exemplo.com       :: rota
nslookup exemplo.com
netstat -ano              :: conexões e PIDs (ver [[Netstat]])
net user & net localgroup administrators
net use Z: \\srv\share /persistent:yes
sc query & sc qc servico  :: serviços
schtasks /query /fo table :: tarefas agendadas
shutdown /r /t 0          :: reiniciar
```

## Redirecionamento e operadores

| Operador | Efeito |
|---|---|
| `>` / `>>` | Redireciona saída (sobrescreve / acrescenta) |
| `2>` / `2>&1` | stderr / junta stderr no stdout |
| `<` | Entrada a partir de arquivo |
| `\|` | Pipe (texto) |
| `&` / `&&` / `\|\|` | Sequência / só se sucesso / só se falha |
| `%errorlevel%` | Código de saída do último comando |

## Arquivo em lote

```bat
@echo off
setlocal
set ORIGEM=C:\dados
set DESTINO=D:\backup\%date:~-4%-%date:~3,2%-%date:~0,2%
if not exist "%DESTINO%" mkdir "%DESTINO%"
robocopy "%ORIGEM%" "%DESTINO%" /E /R:1 /W:1 >nul
if %errorlevel% GEQ 8 (
    echo FALHA no backup >> C:\logs\backup.log
    exit /b 1
)
echo Backup concluido
endlocal
```

> [!info] Códigos do robocopy
> 0-7 = sucesso (bits indicam o que foi copiado); **8 ou mais = erro**. Por isso o teste `GEQ 8`.

## cmd x PowerShell

| Aspecto | cmd | PowerShell |
|---|---|---|
| Pipeline | Texto | Objetos |
| Linguagem | Limitada (`for`, `if`, `goto`) | Completa (.NET) |
| Administração moderna (AD, Azure, registro) | Pouca | Excelente |
| Presença | Em tudo, WinPE/recuperação | Windows 7+ |
| Quando usar | Scripts legados, ferramentas de rede/reparo, ambiente de recuperação | Automação e administração |

## Dicas

- Execute como **Administrador** para `sfc`, `DISM`, `sc`, `netsh` (ver [[SFC e DISM]]).
- `doskey /history` e **F7** mostram histórico; `Tab` completa.
- Para rodar o equivalente: `powershell -Command "Get-Process | Select -First 5"`.

## Pontos-chave

- `cmd` continua útil para utilitários de rede/reparo e compatibilidade.
- `robocopy`, `findstr`, `netsh`, `schtasks` e `sc` compensam suas limitações.
- Para automação nova, use [[PowerShell]].

## Veja também

[[PowerShell]] · [[netstat]] · [[MOC - Ferramentas Nativas do Windows]]
