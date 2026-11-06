---
titulo: "Instalação e Ambiente"
tags: [python, basico, instalacao, ambiente]
nivel: iniciante
criado: 2026-10-05
modulo: "01 - Fundamentos"
---

# 🛠️ Instalação e Ambiente

Antes de escrever código, precisamos de duas coisas: o **interpretador Python** (quem executa seu código) e um **editor** (onde você escreve).

> [!note] O que é Python?
> Python é uma linguagem **interpretada**, de **tipagem dinâmica** e de **alto nível**. "Interpretada" significa que o código é lido e executado linha a linha pelo interpretador (na prática, o CPython compila para *bytecode* e executa numa máquina virtual — veja [[08 - Avançado/04 - CPython Internals|CPython Internals]] quando chegar lá).

Este material usa **Python 3.12+**.

---

## 1. Instalando o Python

### Windows
1. Acesse [python.org/downloads](https://www.python.org/downloads/) e baixe a versão mais recente (3.12 ou superior).
2. Execute o instalador e **marque a opção `Add python.exe to PATH`** antes de clicar em *Install Now*.
3. Alternativa: `winget install Python.Python.3.12` no PowerShell.

### macOS
```bash
# Com Homebrew
brew install python
```
Ou baixe o instalador em python.org.

### Linux (Debian/Ubuntu)
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

> [!warning] Armadilha comum: PATH no Windows
> Se você esqueceu de marcar *Add to PATH*, o terminal dirá que `python` "não é reconhecido como comando".
> - ❌ **Errado:** continuar tentando e achar que a instalação falhou.
> - ✅ **Correto:** reinstale marcando a opção, ou use o *Python Launcher*: `py --version`.

### Verificando a instalação
Abra o terminal e rode:
```bash
python --version      # Windows/macOS (às vezes: python3 --version)
python3 --version     # Linux/macOS
```
Saída esperada: `Python 3.12.x` (ou superior).

> [!tip] `python` ou `python3`?
> No Linux e macOS o comando costuma ser `python3`. No Windows costuma ser `python` ou `py`. Neste material escrevemos `python`; adapte ao seu sistema.

---

## 2. O interpretador interativo (REPL)

Digite `python` no terminal e você entra no **REPL** (*Read-Eval-Print Loop*): ele lê o que você digita, executa e imprime o resultado.

```python
>>> 2 + 3
5
>>> nome = "Ada"
>>> nome.upper()
'ADA'
>>> exit()
```

> [!tip] Seu melhor laboratório
> Sempre que tiver dúvida ("o que acontece se eu fizer isso?"), **teste no REPL**. Errar ali não custa nada. Experimente também o `help()`:
> ```python
> >>> help(str.upper)
> >>> dir("texto")      # lista os métodos disponíveis
> ```

> [!note] IPython
> O **IPython** (`pip install ipython`) é um REPL turbinado: autocompletar com Tab, cores, histórico melhor e comandos mágicos como `%timeit`.

---

## 3. Escolhendo um ambiente de desenvolvimento

| Ferramenta | Melhor para | Prós | Contras |
|------------|-------------|------|---------|
| **VS Code** + extensão Python | Uso geral (recomendado) | Leve, gratuito, debugger excelente, extensões | Exige configurar extensões |
| **PyCharm** (Community) | Projetos grandes | Refatoração e inspeções poderosas | Mais pesado |
| **Jupyter Notebook / Lab** | Dados, estudo, experimentos | Código + texto + gráficos em células | Ruim para projetos estruturados |
| **IDLE** | Primeiros minutos | Já vem com o Python | Muito limitado |
| **Google Colab** | Sem instalar nada | Roda no navegador | Precisa de internet |

### Configurando o VS Code (recomendado)
1. Instale o [VS Code](https://code.visualstudio.com/).
2. Abra a aba **Extensions** (`Ctrl+Shift+X`) e instale **Python** (Microsoft).
3. Crie uma pasta `estudos-python` e abra-a com **File → Open Folder**.
4. Crie o arquivo `ola.py`.
5. Selecione o interpretador: `Ctrl+Shift+P` → **Python: Select Interpreter**.

### Jupyter (opcional)
```bash
pip install jupyterlab
jupyter lab
```

---

## 4. Seu primeiro programa

Crie `ola.py`:

```python
print("Olá, mundo!")
```

Execute no terminal (dentro da pasta do arquivo):
```bash
python ola.py
```
Saída:
```text
Olá, mundo!
```

> [!example] Um pouco mais interessante
> ```python
> nome = "Ada"
> ano = 2026
> print(f"Olá, {nome}! Bem-vinda ao Python em {ano}.")
> ```

---

## 5. Primeiro contato com o debugger

O **debugger** permite executar o código passo a passo e ver os valores das variáveis. Use desde o início — é a melhor forma de entender o que o programa realmente faz.

No VS Code:
1. Clique na margem esquerda de uma linha para colocar um **breakpoint** (bolinha vermelha).
2. Pressione `F5` (*Run and Debug*).
3. Use `F10` (*Step Over*) para avançar linha a linha e `F11` (*Step Into*) para entrar numa função.
4. Observe o painel **Variables**.

```python
a = 10
b = 20
soma = a + b      # coloque o breakpoint aqui
print(soma)
```

> [!tip] `print` não é pecado, mas...
> `print()` para investigar valores funciona, mas o debugger mostra **tudo** de uma vez. Vamos aprofundar em [[08 - Avançado/05 - Performance e Profiling|Performance e Profiling]] e [[08 - Avançado/06 - Testes com unittest e pytest|Testes]].

---

## 6. Ambientes virtuais (spoiler)

Para cada projeto, o ideal é um **ambiente virtual** isolado:
```bash
python -m venv .venv
```
Veremos isso em detalhes em [[03 - Funções e Modularização/05 - Virtual Environments e pip|Virtual Environments e pip]]. Por ora, apenas saiba que existe.

---

## 7. Erros comuns de instalação

| Sintoma | Causa provável | Solução |
|---------|----------------|---------|
| `'python' não é reconhecido...` | Python fora do PATH | Reinstale marcando *Add to PATH* ou use `py` |
| `python` abre a Microsoft Store (Windows) | Atalho de alias | *Configurações → Aliases de execução de aplicativo* → desative o alias do Python |
| Versão antiga (2.x ou 3.8) | Vários Pythons instalados | Use `python3.12` ou ajuste o PATH |
| `ModuleNotFoundError` | Pacote instalado em outro Python | Use `python -m pip install ...` |

> [!question] Exercício
> 1. Verifique a versão do Python instalada.
> 2. Abra o REPL e calcule `7 * 6`.
> 3. Use `dir(str)` e conte (aproximadamente) quantos métodos strings têm.
> 4. Crie `ola.py` que imprime seu nome e rode-o pelo terminal.
> 5. Rode o mesmo arquivo com o debugger e inspecione uma variável.

> [!success]- Solução
> ```bash
> python --version
> ```
> ```python
> >>> 7 * 6
> 42
> >>> len(dir(str))      # ~80 itens (inclui métodos "dunder")
> ```
> ```python
> # ola.py
> nome = "Seu Nome"
> print(f"Meu nome é {nome}")
> ```

---

## Próximos passos
➡️ [[01 - Fundamentos/02 - Sintaxe Básica e Variáveis|Sintaxe Básica e Variáveis]]

⬆️ Voltar ao [[Índice - Python|Índice]]

#python #basico #instalacao #ambiente #vscode #repl
