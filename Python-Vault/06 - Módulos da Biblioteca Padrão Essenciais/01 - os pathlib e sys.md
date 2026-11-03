---
titulo: "os, pathlib e sys"
tags: [python, intermediario, stdlib, pathlib]
nivel: intermediario
criado: 2026-10-05
modulo: "06 - Módulos da Biblioteca Padrão Essenciais"
---

# 🖥️ `os`, `pathlib` e `sys`

> [!note] "Baterias incluídas"
> A **biblioteca padrão** do Python vem com o interpretador: sem `pip install`. Dominá-la evita reinventar a roda e reduz dependências. Neste módulo veremos os módulos mais usados no dia a dia.

Esta nota trata da interação com o **sistema operacional** e o **interpretador**:

| Módulo | Para quê |
|--------|----------|
| `pathlib` | Caminhos e arquivos (forma **moderna**, orientada a objetos) |
| `os` | Variáveis de ambiente, processos, informações do SO |
| `shutil` | Copiar, mover e apagar arquivos/pastas |
| `sys` | Interpretador: argumentos, saída, versão, caminhos de import |
| `subprocess` | Executar outros programas |

---

## 1. `pathlib`: caminhos como objetos

```python
from pathlib import Path

p = Path("dados") / "2026" / "vendas.csv"      # / une partes (multiplataforma)
print(p)                 # dados/2026/vendas.csv  (no Windows: dados\2026\vendas.csv)
```

### Pastas especiais
```python
Path.cwd()               # pasta de trabalho atual
Path.home()              # pasta do usuário
Path(__file__).resolve() # caminho absoluto deste script
Path(__file__).parent    # pasta deste script
```

### Partes de um caminho
```python
p = Path("/home/ada/projeto/relatorio.final.pdf")

p.name        # 'relatorio.final.pdf'
p.stem        # 'relatorio.final'
p.suffix      # '.pdf'
p.suffixes    # ['.final', '.pdf']
p.parent      # PosixPath('/home/ada/projeto')
p.parents[1]  # PosixPath('/home/ada')
p.parts       # ('/', 'home', 'ada', 'projeto', 'relatorio.final.pdf')
p.anchor      # '/'
```

### Derivando novos caminhos (não altera o arquivo, só o objeto)
```python
p.with_suffix(".txt")        # .../relatorio.final.txt
p.with_name("outro.pdf")     # .../outro.pdf
p.relative_to("/home/ada")   # PosixPath('projeto/relatorio.final.pdf')
p.resolve()                  # absoluto, resolvendo '..' e links
```

### Consultas
```python
p.exists()
p.is_file()
p.is_dir()
p.stat().st_size             # tamanho em bytes
p.stat().st_mtime            # última modificação (timestamp)
```

### Criar, ler, escrever, apagar
```python
pasta = Path("saida")
pasta.mkdir(parents=True, exist_ok=True)   # cria (e pais), sem erro se já existir

arq = pasta / "nota.txt"
arq.write_text("olá\n", encoding="utf-8")
print(arq.read_text(encoding="utf-8"))
arq.write_bytes(b"\x00\x01")
dados = arq.read_bytes()

arq.rename(pasta / "nota2.txt")            # renomeia/move
arq.unlink(missing_ok=True)                # apaga arquivo (sem erro se não existir)
pasta.rmdir()                              # apaga pasta VAZIA

with (pasta / "x.txt").open("w", encoding="utf-8") as f:
    f.write("aberto via Path")
```

### Listando e buscando
```python
raiz = Path(".")

for item in raiz.iterdir():              # conteúdo imediato
    print(item.name, "📁" if item.is_dir() else "📄")

list(raiz.glob("*.py"))                  # padrão na pasta
list(raiz.rglob("*.py"))                 # recursivo (todas as subpastas)
list(raiz.glob("dados/**/*.csv"))        # ** = qualquer profundidade

# Os 5 maiores arquivos .py
maiores = sorted(raiz.rglob("*.py"), key=lambda a: a.stat().st_size, reverse=True)[:5]
```

> [!tip] `pathlib` vs `os.path`
> | Tarefa | `os.path` (antigo) | `pathlib` (moderno) |
> |--------|-------------------|---------------------|
> | Unir | `os.path.join(a, b)` | `Path(a) / b` |
> | Nome | `os.path.basename(p)` | `p.name` |
> | Pasta pai | `os.path.dirname(p)` | `p.parent` |
> | Existe? | `os.path.exists(p)` | `p.exists()` |
> | Ler | `open(p).read()` | `p.read_text()` |
>
> Use `pathlib` em código novo. Funções que aceitam `str` também aceitam `Path`.

> [!warning] Armadilhas
> ```python
> Path("a") / "/b"          # ⚠️ caminho absoluto "descarta" o anterior → /b
> Path("a.txt").mkdir()     # cria uma PASTA chamada a.txt, não um arquivo
> str(p)                    # use quando uma API exigir texto
> ```
> No Windows, o separador é `\`; `Path` cuida disso. Veja também [[05 - Tratamento de Erros e Arquivos/03 - Arquivos Texto CSV e JSON|pathlib em arquivos]].

---

## 2. `os`: sistema operacional

### Variáveis de ambiente
```python
import os

home = os.environ["HOME"]                       # KeyError se não existir
chave = os.environ.get("API_KEY")               # None se não existir
porta = int(os.getenv("PORTA", "8000"))         # com padrão
os.environ["MODO"] = "teste"                    # vale só para este processo
```

> [!warning] Segredos
> Guarde chaves/senhas em **variáveis de ambiente** ou arquivos `.env` (fora do Git), nunca no código.

### Informações e utilidades
```python
os.name                  # 'posix' ou 'nt' (Windows)
os.getcwd()              # pasta atual (str)
os.chdir("/tmp")         # muda de pasta (global! prefira caminhos absolutos)
os.cpu_count()           # nº de CPUs lógicas
os.getpid()              # id do processo
os.listdir(".")          # nomes na pasta
os.makedirs("a/b", exist_ok=True)
os.remove("arq.txt")     # apaga arquivo
os.rename("a", "b")
os.replace("tmp", "final")   # troca atômica (sobrescreve)
os.sep, os.linesep       # separador de caminho / de linha
```

### Percorrendo árvores: `os.walk` e `os.scandir`
```python
for pasta, subpastas, arquivos in os.walk("."):
    for nome in arquivos:
        print(os.path.join(pasta, nome))

with os.scandir(".") as it:                # mais rápido que listdir + stat
    for entrada in it:
        print(entrada.name, entrada.is_file(), entrada.stat().st_size)
```
(`Path.rglob` costuma ser suficiente e mais legível.)

### `os.path` (ainda muito visto em código existente)
```python
os.path.join("a", "b", "c.txt")
os.path.exists("x")
os.path.splitext("foto.jpg")       # ('foto', '.jpg')
os.path.abspath("x")
os.path.getsize("x")
os.path.expanduser("~/docs")
```

> [!warning] Evite `os.system`
> ```python
> os.system("rm -rf " + pasta)       # ❌ vulnerável a injeção de comandos
> ```
> Use `subprocess.run([...])` com **lista de argumentos** (abaixo).

---

## 3. `shutil`: operações de alto nível

```python
import shutil

shutil.copy("a.txt", "b.txt")                 # copia conteúdo
shutil.copy2("a.txt", "pasta/")               # copia + metadados
shutil.copytree("origem", "destino", dirs_exist_ok=True)   # copia pasta inteira
shutil.move("a.txt", "pasta/a.txt")           # move/renomeia
shutil.rmtree("pasta")                        # ⚠️ apaga pasta INTEIRA (sem lixeira)
shutil.make_archive("backup", "zip", "pasta") # cria backup.zip
shutil.disk_usage("/")                        # (total, usado, livre)
shutil.which("python")                        # onde está um executável
```

> [!warning] `rmtree` é irreversível
> Confira o caminho **duas vezes** (ou use `send2trash`, de terceiros, para a lixeira).

---

## 4. `sys`: o interpretador

```python
import sys

sys.version                 # '3.12.x ...'
sys.version_info            # sys.version_info(major=3, minor=12, ...)
sys.version_info >= (3, 12) # True: comparação segura
sys.platform                # 'linux', 'darwin', 'win32'
sys.executable              # caminho do Python em uso
sys.path                    # onde o Python procura módulos
sys.modules                 # módulos já carregados
sys.getrecursionlimit()     # ~1000
sys.getsizeof([1, 2, 3])    # bytes ocupados (só o contêiner, não os itens)
```

### Argumentos de linha de comando
```python
# soma.py
import sys

if len(sys.argv) < 3:
    print("Uso: python soma.py A B", file=sys.stderr)
    sys.exit(1)

a, b = float(sys.argv[1]), float(sys.argv[2])
print(a + b)
```
```bash
python soma.py 2 3     # sys.argv = ['soma.py', '2', '3']  → 5.0
```

> [!tip] Para CLIs de verdade, use `argparse`
> ```python
> import argparse
> parser = argparse.ArgumentParser(description="Soma dois números")
> parser.add_argument("a", type=float)
> parser.add_argument("b", type=float)
> parser.add_argument("--inteiro", action="store_true", help="arredonda o resultado")
> args = parser.parse_args()
> r = args.a + args.b
> print(round(r) if args.inteiro else r)
> ```
> Gera `--help`, valida tipos e mostra erros amigáveis. Usado no [[09 - Projetos Práticos/Projeto 01 - Calculadora CLI|Projeto 01]].

### Entrada/saída padrão
```python
sys.stdout.write("sem quebra de linha")
print("erro!", file=sys.stderr)         # canal de erros (separado do stdout)

for linha in sys.stdin:                  # lê stdin (pipes: cat arq | python prog.py)
    print(linha.upper(), end="")
```

### Encerrar o programa
```python
sys.exit(0)        # sucesso
sys.exit(1)        # erro (código de saída ≠ 0)
sys.exit("Mensagem de erro")   # imprime em stderr e sai com código 1
```
`sys.exit()` levanta `SystemExit` (por isso `finally` e `with` ainda rodam).

---

## 5. `subprocess`: executando outros programas

```python
import subprocess

resultado = subprocess.run(
    ["python", "--version"],       # LISTA de argumentos (seguro)
    capture_output=True,
    text=True,
    check=True,                    # levanta CalledProcessError se código ≠ 0
    timeout=10,
)
print(resultado.stdout.strip())    # Python 3.12.x
print(resultado.returncode)        # 0
```

```python
try:
    subprocess.run(["ls", "pasta_que_nao_existe"], check=True, capture_output=True, text=True)
except subprocess.CalledProcessError as e:
    print("Falhou:", e.stderr)
except FileNotFoundError:
    print("Comando não encontrado")
```

> [!warning] Nunca use `shell=True` com entrada do usuário
> ```python
> subprocess.run(f"ls {entrada}", shell=True)       # ❌ injeção de comandos
> subprocess.run(["ls", entrada])                    # ✅
> ```

---

## 6. Exemplo completo: organizador de downloads

```python
from pathlib import Path
import shutil

CATEGORIAS = {
    "imagens": {".jpg", ".jpeg", ".png", ".gif", ".webp"},
    "documentos": {".pdf", ".docx", ".txt", ".md", ".xlsx"},
    "audio_video": {".mp3", ".wav", ".mp4", ".mkv"},
    "compactados": {".zip", ".tar", ".gz", ".7z"},
}

def categoria(sufixo):
    for nome, extensoes in CATEGORIAS.items():
        if sufixo.lower() in extensoes:
            return nome
    return "outros"

def organizar(pasta):
    pasta = Path(pasta).expanduser()
    movidos = 0
    for arq in pasta.iterdir():
        if not arq.is_file() or arq.name.startswith("."):
            continue
        destino = pasta / categoria(arq.suffix)
        destino.mkdir(exist_ok=True)
        alvo = destino / arq.name
        if alvo.exists():                      # evita sobrescrever
            alvo = destino / f"{arq.stem}_copia{arq.suffix}"
        shutil.move(arq, alvo)
        movidos += 1
    return movidos

if __name__ == "__main__":
    print(f"{organizar('~/Downloads')} arquivo(s) organizado(s)")
```

---

> [!question] Exercícios
> 1. Liste todos os arquivos `.py` de uma pasta (recursivamente) com tamanho em KB, ordenados do maior para o menor.
> 2. Escreva `espaco_por_extensao(pasta)` que devolva `{".py": bytes, ".txt": bytes}`.
> 3. Escreva um script que receba um nome de pasta por `argv`, crie-a (`parents=True`) e imprima o caminho absoluto; saia com código 1 e mensagem em `stderr` se faltar o argumento.
> 4. Leia a variável `DEBUG` do ambiente e converta para `bool` (`"1"`, `"true"`, `"yes"` → `True`).
> 5. Faça backup de uma pasta para `backup_AAAA-MM-DD.zip` usando `shutil.make_archive`.
> 6. Execute `python --version` via `subprocess.run` e mostre a versão. Trate o comando inexistente.
> 7. Encontre arquivos **duplicados** (mesmo tamanho e mesmo conteúdo) em uma pasta. Dica: agrupe por tamanho e compare `hashlib.sha256`.
> 8. O que há de errado? `Path("dados") / "/tmp" / "x.txt"`

> [!success]- Soluções
> 1. ```python
>    from pathlib import Path
>    arquivos = sorted(Path(".").rglob("*.py"), key=lambda a: a.stat().st_size, reverse=True)
>    for a in arquivos:
>        print(f"{a.stat().st_size / 1024:8.1f} KB  {a}")
>    ```
> 2. ```python
>    from collections import defaultdict
>    def espaco_por_extensao(pasta):
>        total = defaultdict(int)
>        for a in Path(pasta).rglob("*"):
>            if a.is_file():
>                total[a.suffix.lower()] += a.stat().st_size
>        return dict(total)
>    ```
> 3. ```python
>    import sys
>    from pathlib import Path
>    if len(sys.argv) != 2:
>        sys.exit("Uso: python criar.py NOME_DA_PASTA")
>    p = Path(sys.argv[1])
>    p.mkdir(parents=True, exist_ok=True)
>    print(p.resolve())
>    ```
> 4. ```python
>    import os
>    DEBUG = os.getenv("DEBUG", "").strip().lower() in {"1", "true", "yes", "sim"}
>    ```
> 5. ```python
>    import shutil
>    from datetime import date
>    shutil.make_archive(f"backup_{date.today():%Y-%m-%d}", "zip", "minha_pasta")
>    ```
> 6. ```python
>    import subprocess
>    try:
>        r = subprocess.run(["python", "--version"], capture_output=True, text=True, check=True)
>        print(r.stdout.strip() or r.stderr.strip())
>    except FileNotFoundError:
>        print("python não encontrado no PATH")
>    ```
> 7. ```python
>    import hashlib
>    from collections import defaultdict
>    from pathlib import Path
>
>    def hash_arquivo(p):
>        h = hashlib.sha256()
>        with p.open("rb") as f:
>            while bloco := f.read(1 << 20):
>                h.update(bloco)
>        return h.hexdigest()
>
>    por_tamanho = defaultdict(list)
>    for a in Path(".").rglob("*"):
>        if a.is_file():
>            por_tamanho[a.stat().st_size].append(a)
>
>    por_hash = defaultdict(list)
>    for grupo in por_tamanho.values():
>        if len(grupo) > 1:
>            for a in grupo:
>                por_hash[hash_arquivo(a)].append(a)
>
>    for h, arqs in por_hash.items():
>        if len(arqs) > 1:
>            print(h[:10], *arqs, sep="\n  ")
>    ```
> 8. Um segmento **absoluto** (`"/tmp"`) descarta tudo o que veio antes: o resultado é `/tmp/x.txt`, não `dados/tmp/x.txt`.

---

⬅️ [[05 - Tratamento de Erros e Arquivos/05 - Exercícios de Erros e Arquivos|Exercícios do Módulo 05]] | ➡️ [[06 - Módulos da Biblioteca Padrão Essenciais/02 - datetime e time|datetime e time]]

#python #intermediario #stdlib #os #pathlib #sys #shutil #subprocess
