---
titulo: "Regedit (Editor do Registro)"
tags:
  - sistemas-operacionais
  - ferramenta
  - windows
tipo: ferramenta
nivel: intermediario
relacionados:
  - "[[PowerShell]]"
  - "[[Windows NT]]"
  - "[[Autenticação]]"
  - "[[MOC - Ferramentas Nativas do Windows]]"
---

# Regedit (Editor do Registro)

## Finalidade

O **Registro do Windows** é o banco de dados hierárquico de **configuração** do sistema, drivers, serviços, usuários e aplicativos. O **Regedit** (`regedit.exe`) o edita. Análogo a `/etc`, `sysctl` e *dconf* do Linux, mas centralizado e binário.

## Estrutura

| Hive / chave raiz | Conteúdo |
|---|---|
| **HKEY_LOCAL_MACHINE (HKLM)** | Configuração do **computador**: `SOFTWARE`, `SYSTEM` (serviços, drivers, controle), `SAM`, `SECURITY`, `HARDWARE` |
| **HKEY_CURRENT_USER (HKCU)** | Configuração do **usuário atual** (arquivo `NTUSER.DAT` do perfil) |
| **HKEY_USERS (HKU)** | Todos os perfis carregados (por SID) |
| **HKEY_CLASSES_ROOT (HKCR)** | Associações de arquivo e COM (união de HKLM\Software\Classes e HKCU\...\Classes) |
| **HKEY_CURRENT_CONFIG (HKCC)** | Perfil de hardware atual (link) |

Hives ficam em `C:\Windows\System32\config\` (SYSTEM, SOFTWARE, SAM, SECURITY, DEFAULT) e no perfil do usuário (`NTUSER.DAT`, `UsrClass.dat`).

## Tipos de valores

| Tipo | Uso |
|---|---|
| `REG_SZ` | Texto |
| `REG_EXPAND_SZ` | Texto com variáveis (`%SystemRoot%`) |
| `REG_MULTI_SZ` | Lista de textos |
| `REG_DWORD` / `REG_QWORD` | Número de 32/64 bits (flags, timeouts) |
| `REG_BINARY` | Dados binários |

## Locais importantes

| Caminho | Para quê |
|---|---|
| `HKLM\SYSTEM\CurrentControlSet\Services\<nome>` | Definição de **serviços e drivers** (`Start`: 2 automático, 3 manual, 4 desabilitado) |
| `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run` | Programas que iniciam com o Windows (todos os usuários) |
| `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` | Inicialização do usuário |
| `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion` | Versão do Windows, `Winlogon`, `Image File Execution Options` |
| `HKLM\SYSTEM\CurrentControlSet\Control` | Configurações do kernel e do gerenciador de sessão |
| `HKLM\SOFTWARE\Policies` | Políticas de grupo aplicadas |
| `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall` | Programas instalados |

> [!warning] Persistência de malware
> Chaves `Run`, `RunOnce`, `Services`, `Winlogon\Shell/Userinit`, `Image File Execution Options` e `AppInit_DLLs` são alvos clássicos de **persistência**. Ferramentas como **Autoruns** (Sysinternals) as revisam.

## Usando o Regedit

- **Exportar** (`.reg`) antes de alterar: *Arquivo → Exportar* (cópia de segurança).
- **Procurar** com `Ctrl+F` (chaves, valores, dados).
- **Favoritos** para caminhos frequentes.
- **Carregar Hive** para editar o registro de um Windows offline.
- Executar como administrador para HKLM.

Arquivo `.reg` (importável com duplo clique):

```reg
Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\Software\MeuApp]
"Tema"="escuro"
"Intervalo"=dword:0000001e
"Caminho"=hex(2):25,00,55,00,53,00,45,00,52,00,50,00,52,00,4f,00,46,00,49,00,4c,00,45,00,25,00,00,00
```

## PowerShell e CMD

```powershell
# Ler
Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion' | Select ProductName, CurrentBuild
Get-ChildItem 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Run'

# Criar/alterar (com backup antes)
reg export "HKCU\Software\MeuApp" C:\bkp\meuapp.reg /y
New-Item 'HKCU:\Software\MeuApp' -Force | Out-Null
New-ItemProperty 'HKCU:\Software\MeuApp' -Name Intervalo -Value 30 -PropertyType DWord -Force
Set-ItemProperty 'HKCU:\Software\MeuApp' -Name Tema -Value 'escuro'

# Remover
Remove-ItemProperty 'HKCU:\Software\MeuApp' -Name Tema
Remove-Item 'HKCU:\Software\MeuApp' -Recurse

# Permissões da chave
Get-Acl 'HKLM:\SOFTWARE\MeuApp' | Format-List
```

```cmd
reg query "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
reg add "HKCU\Software\MeuApp" /v Tema /t REG_SZ /d escuro /f
reg delete "HKCU\Software\MeuApp" /f
reg export HKCU\Software\MeuApp meuapp.reg
reg import meuapp.reg
reg load HKU\Offline C:\Users\Ana\NTUSER.DAT   :: carrega hive offline
reg unload HKU\Offline
```

## Boas práticas

> [!warning] Segurança e estabilidade
> - **Sempre faça backup** (exportar chave ou criar ponto de restauração) antes de editar.
> - Prefira **políticas de grupo** (GPO/Intune) a editar manualmente em escala.
> - Registro de 64 bits: aplicativos 32 bits veem `HKLM\SOFTWARE\WOW6432Node`.
> - Evite "otimizadores de registro": raramente ajudam e podem quebrar o sistema.
> - Restrinja permissões em chaves sensíveis; monitore alterações (auditoria, Sysmon).

## Vantagens e desvantagens do Registro

| Vantagens | Desvantagens |
|---|---|
| Configuração centralizada, tipada e com ACLs por chave | Binário e opaco; erros podem impedir o boot |
| Acesso rápido e atômico | Acúmulo de resíduos de programas desinstalados |
| Políticas e gestão remota (GPO) | Ponto único de falha e alvo de persistência de malware |

## Pontos-chave

- Cinco raízes; HKLM (máquina) e HKCU (usuário) são as principais.
- Exporte antes de alterar; use PowerShell/`reg` para automatizar.
- Revise chaves de inicialização em investigações de segurança.

## Veja também

[[PowerShell]] · [[Windows NT]] · [[MOC - Ferramentas Nativas do Windows]]
