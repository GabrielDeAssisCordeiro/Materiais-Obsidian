---
titulo: "re: Expressões Regulares"
tags: [python, intermediario, stdlib]
nivel: intermediario
criado: 2026-10-05
modulo: "06 - Módulos da Biblioteca Padrão Essenciais"
---

# 🔍 `re`: Expressões Regulares

Uma **expressão regular** (*regex*) é um **padrão** que descreve um conjunto de textos. Serve para **validar**, **buscar**, **extrair** e **substituir** trechos de texto de forma muito mais poderosa do que `in`, `startswith` ou `split`.

> [!example] Analogia
> É como um "coringa" turbinado: `*.txt` no explorador de arquivos encontra todos os `.txt`; uma regex faz isso (e muito mais) **dentro de qualquer texto**.

```python
import re

print(re.search(r"\d{3}-\d{4}", "Ligue para 555-1234 hoje"))
# <re.Match object; span=(14, 22), match='555-1234'>
```

> [!tip] Sempre use **raw strings** (`r"..."`)
> ```python
> re.search("\d+", texto)     # ❌ funciona por sorte (aviso de escape inválido)
> re.search(r"\d+", texto)    # ✅ \d chega intacto à regex
> ```
> Sem o `r`, o Python interpreta `\n`, `\t`, `\b` **antes** da regex ver.

---

## 1. Funções principais

| Função | O que faz | Retorno |
|--------|-----------|---------|
| `re.search(p, s)` | Procura o padrão **em qualquer posição** | `Match` ou `None` |
| `re.match(p, s)` | Casa **somente no início** da string | `Match` ou `None` |
| `re.fullmatch(p, s)` | Casa a string **inteira** | `Match` ou `None` |
| `re.findall(p, s)` | **Todas** as ocorrências | lista |
| `re.finditer(p, s)` | Todas as ocorrências, com detalhes | iterador de `Match` |
| `re.sub(p, novo, s)` | **Substitui** ocorrências | string |
| `re.split(p, s)` | **Divide** pelo padrão | lista |
| `re.compile(p)` | Pré-compila o padrão para reuso | objeto `Pattern` |

```python
texto = "Contato: ada@exemplo.com ou alan@teste.org"

re.search(r"\w+@\w+\.\w+", texto).group()      # 'ada@exemplo.com'
re.findall(r"\w+@\w+\.\w+", texto)             # ['ada@exemplo.com', 'alan@teste.org']
re.sub(r"\d", "#", "CPF 123.456")              # 'CPF ###.###'
re.split(r"[,;]\s*", "a, b;c,  d")             # ['a', 'b', 'c', 'd']
```

> [!warning] `match` não é `search`
> ```python
> re.match(r"\d+", "abc 123")      # None  ← match só olha o INÍCIO
> re.search(r"\d+", "abc 123")     # <Match '123'>
> ```
> Para **validar** uma string inteira, use `fullmatch` (ou `^...$`).

### O objeto `Match`
```python
m = re.search(r"(\d{2})/(\d{2})/(\d{4})", "Nasci em 05/10/1990.")

m.group()       # '05/10/1990'  (tudo; igual a m.group(0))
m.group(1)      # '05'          (1º grupo)
m.groups()      # ('05', '10', '1990')
m.start(), m.end(), m.span()      # 9 19 (9, 19)
```

> [!warning] Sempre verifique o `None`
> ```python
> m = re.search(r"\d+", "sem números")
> m.group()          # ❌ AttributeError: 'NoneType' object has no attribute 'group'
>
> if m := re.search(r"\d+", texto):     # ✅ operador morsa
>     print(m.group())
> ```

---

## 2. Sintaxe essencial

### Caracteres e classes

| Padrão | Casa com |
|--------|----------|
| `.` | **Qualquer** caractere (exceto `\n`) |
| `\d` | Dígito `[0-9]` |
| `\D` | **Não** dígito |
| `\w` | Letra, dígito ou `_` (inclui acentos em `str`) |
| `\W` | **Não** `\w` |
| `\s` | Espaço, tab, quebra de linha |
| `\S` | **Não** espaço |
| `[abc]` | `a`, `b` **ou** `c` |
| `[a-z]` | Letra minúscula (intervalo) |
| `[^abc]` | **Qualquer menos** `a`, `b`, `c` |
| `\.` | Ponto literal (escape de caractere especial) |

### Quantificadores

| Padrão | Repete | Exemplo |
|--------|--------|---------|
| `*` | 0 ou mais | `ab*` → `a`, `ab`, `abbb` |
| `+` | 1 ou mais | `\d+` → `7`, `2026` |
| `?` | 0 ou 1 (opcional) | `colou?r` → `color`, `colour` |
| `{n}` | Exatamente n | `\d{4}` → `2026` |
| `{n,m}` | Entre n e m | `\d{2,4}` |
| `{n,}` | n ou mais | `\w{3,}` |

### Âncoras e fronteiras

| Padrão | Posição |
|--------|---------|
| `^` | Início da string (ou da linha com `re.M`) |
| `$` | Fim da string (ou da linha com `re.M`) |
| `\b` | **Fronteira de palavra** |
| `\B` | Não é fronteira de palavra |

```python
re.findall(r"\bgato\b", "gato, gatos, agatoado, o gato")   # ['gato', 'gato']
```

### Alternativa e grupos

| Padrão | Significado |
|--------|-------------|
| `a\|b` | `a` **ou** `b` |
| `(...)` | **Grupo de captura** |
| `(?:...)` | Grupo **sem** captura |
| `(?P<nome>...)` | Grupo **nomeado** |
| `\1` | Retrovisor: repete o grupo 1 |

### Caracteres especiais que exigem escape
`. ^ $ * + ? { } [ ] \ | ( )` → use `\.`, `\(`, etc. Ou `re.escape(texto)` para escapar uma string inteira:
```python
re.search(re.escape("1+1=2"), "conta: 1+1=2")      # trata '+' como literal
```

---

## 3. Grupos: extraindo partes

```python
data = "Nasci em 05/10/1990"

m = re.search(r"(\d{2})/(\d{2})/(\d{4})", data)
dia, mes, ano = m.groups()                   # ('05', '10', '1990')
```

### Grupos nomeados (mais legíveis)
```python
padrao = r"(?P<dia>\d{2})/(?P<mes>\d{2})/(?P<ano>\d{4})"
m = re.search(padrao, data)
m.group("ano")           # '1990'
m.groupdict()            # {'dia': '05', 'mes': '10', 'ano': '1990'}
```

### `findall` com grupos
```python
re.findall(r"(\w+)=(\d+)", "a=1, b=22, c=333")
# [('a', '1'), ('b', '22'), ('c', '333')]
dict(re.findall(r"(\w+)=(\d+)", "a=1, b=22"))     # {'a': '1', 'b': '22'}
```
> ⚠️ Com **um** grupo, `findall` devolve só o conteúdo do grupo; com **vários**, devolve tuplas; sem grupos, devolve o trecho inteiro.

### Substituição com grupos
```python
re.sub(r"(\d{2})/(\d{2})/(\d{4})", r"\3-\2-\1", "05/10/2026")     # '2026-10-05'
re.sub(r"(?P<d>\d{2})/(?P<m>\d{2})", r"\g<m>/\g<d>", "05/10")     # '10/05'

# Substituição com função
re.sub(r"\d+", lambda m: str(int(m.group()) * 2), "tenho 3 gatos e 12 cães")
# 'tenho 6 gatos e 24 cães'
```

---

## 4. Guloso (*greedy*) vs preguiçoso (*lazy*)

Quantificadores são **gulosos**: casam o **máximo** possível. Acrescente `?` para torná-los **preguiçosos** (o mínimo).

```python
html = "<b>negrito</b> e <i>itálico</i>"

re.findall(r"<.+>", html)       # ❌ ['<b>negrito</b> e <i>itálico</i>']  (guloso)
re.findall(r"<.+?>", html)      # ✅ ['<b>', '</b>', '<i>', '</i>']       (preguiçoso)
re.findall(r"<(\w+)>", html)    # ['b', 'i']
```

| Guloso | Preguiçoso |
|--------|------------|
| `*` | `*?` |
| `+` | `+?` |
| `?` | `??` |
| `{n,m}` | `{n,m}?` |

---

## 5. Flags (opções)

```python
re.search(r"python", "Python!", re.IGNORECASE)     # ou re.I
```

| Flag | Abrev. | Efeito |
|------|--------|--------|
| `re.IGNORECASE` | `re.I` | Ignora maiúsculas/minúsculas |
| `re.MULTILINE` | `re.M` | `^` e `$` valem para **cada linha** |
| `re.DOTALL` | `re.S` | `.` casa também com `\n` |
| `re.VERBOSE` | `re.X` | Permite espaços e **comentários** na regex |
| `re.ASCII` | `re.A` | `\w`, `\d`... só ASCII |

Combine com `|`: `re.I | re.M`.

### `re.VERBOSE`: regex legível
```python
telefone = re.compile(r"""
    \(?(?P<ddd>\d{2})\)?    # DDD, com ou sem parênteses
    \s?                     # espaço opcional
    (?P<prefixo>9?\d{4})    # 4 ou 5 dígitos
    [-\s]?                  # hífen ou espaço opcional
    (?P<sufixo>\d{4})       # últimos 4 dígitos
""", re.VERBOSE)

m = telefone.search("Ligue (11) 91234-5678")
print(m.groupdict())    # {'ddd': '11', 'prefixo': '91234', 'sufixo': '5678'}
```

---

## 6. `re.compile`: reuso e desempenho

```python
EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")

for texto in textos:                 # padrão compilado uma vez
    if EMAIL.search(texto):
        ...

EMAIL.findall(texto)
EMAIL.sub("[oculto]", texto)
```
Por padrão, o `re` mantém um cache interno; `compile` é útil para **nomear** o padrão, **reaproveitar** e usar flags de forma organizada.

---

## 7. Lookarounds (avançado)

Condições que **olham ao redor** sem consumir caracteres:

| Padrão | Significado |
|--------|-------------|
| `(?=...)` | **Seguido de** (*lookahead*) |
| `(?!...)` | **Não** seguido de |
| `(?<=...)` | **Precedido de** (*lookbehind*) |
| `(?<!...)` | **Não** precedido de |

```python
re.findall(r"\d+(?= reais)", "10 reais, 20 dólares, 30 reais")       # ['10', '30']
re.findall(r"(?<=R\$)\d+", "R$50 e US$70")                           # ['50']
re.search(r"^(?=.*\d)(?=.*[A-Z]).{8,}$", "Senha123x")                # senha com número e maiúscula, 8+
```

---

## 8. Receitas práticas

```python
# E-mail (simples; validação 100% correta é complexa)
EMAIL = re.compile(r"[\w.+-]+@[\w-]+(\.[\w-]+)+")

# Telefone brasileiro (com ou sem máscara)
TEL = re.compile(r"\(?\d{2}\)?\s?9?\d{4}-?\d{4}")

# CPF formatado
CPF = re.compile(r"\d{3}\.\d{3}\.\d{3}-\d{2}")

# CEP
CEP = re.compile(r"\d{5}-?\d{3}")

# Data dd/mm/aaaa (formato, não valida o calendário)
DATA = re.compile(r"(0[1-9]|[12]\d|3[01])/(0[1-9]|1[0-2])/\d{4}")

# URL (simples)
URL = re.compile(r"https?://[^\s/$.?#].[^\s]*")

# Palavras repetidas ("o o")
REPETIDA = re.compile(r"\b(\w+)\s+\1\b", re.I)

# Remover espaços em excesso
re.sub(r"\s+", " ", "  muitos    espaços   aqui ").strip()

# Somente dígitos de um texto (CPF, CEP, telefone)
re.sub(r"\D", "", "123.456.789-09")        # '12345678909'

# snake_case → camelCase
re.sub(r"_([a-z])", lambda m: m.group(1).upper(), "meu_nome_completo")  # meuNomeCompleto

# Dividir por vários separadores
re.split(r"[,;|\s]+", "a, b;c|d e")         # ['a', 'b', 'c', 'd', 'e']
```

### Extraindo dados de logs
```python
log = '192.168.0.10 - - [05/Oct/2026:14:03:21] "GET /index.html HTTP/1.1" 200 1534'

padrao = re.compile(
    r'(?P<ip>\d+\.\d+\.\d+\.\d+).*?\[(?P<data>[^\]]+)\] '
    r'"(?P<metodo>\w+) (?P<caminho>\S+).*?" (?P<status>\d{3}) (?P<bytes>\d+)'
)
print(padrao.search(log).groupdict())
```

---

## 9. Armadilhas e boas práticas

> [!warning] Armadilhas
> - **Esquecer o `r`** nas strings.
> - **Usar `match` esperando `search`**.
> - **`.*` guloso demais**: use `.*?` ou classes negadas (`[^"]*`).
> - **Validar tudo com regex**: e-mail e CPF completos têm regras que regex não cobre bem (dígitos verificadores, domínios existentes). Use regex para o **formato** e código para as **regras**.
> - **Não parseie HTML/XML/JSON com regex**: use `html.parser`/BeautifulSoup, `xml.etree`, `json`.
> - **Backtracking catastrófico (ReDoS)**: padrões como `(a+)+$` aplicados a `"aaaa...b"` podem travar o programa. Evite quantificadores aninhados e limite o tamanho da entrada não confiável.
> - **Acentos**: em `str`, `\w` inclui letras acentuadas (`é`, `ç`). `[a-z]` **não**.

> [!tip] Boas práticas
> - Teste interativamente: [regex101.com](https://regex101.com) (escolha o sabor *Python*) mostra cada parte do padrão.
> - Use `re.VERBOSE` e **grupos nomeados** em padrões longos.
> - **Compile** e dê nomes em MAIÚSCULAS aos padrões reutilizados.
> - Prefira métodos de `str` quando bastarem: `texto.startswith("a")` é mais claro que `re.match(r"a", texto)`.
> - Documente o que o padrão aceita **e o que não aceita**.

> [!note] "Algumas pessoas, ao encontrarem um problema, pensam: *'Já sei, vou usar expressões regulares.'* Agora elas têm dois problemas."
> Piada clássica entre programadores: regex é ótima, mas use com **moderação** e **testes**.

---

## 10. Exemplo completo: extrator de contatos

```python
import re

EMAIL = re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+")
TEL = re.compile(r"\(?\d{2}\)?\s?9?\d{4}-?\d{4}")

texto = """
Fale com Ana: ana.silva@empresa.com.br ou (11) 91234-5678.
Suporte: suporte@loja.com, tel 21 3456-7890.
Cobrança: financeiro@loja.com | WhatsApp 11912345678
"""

emails = sorted(set(EMAIL.findall(texto)))
telefones = [re.sub(r"\D", "", t) for t in TEL.findall(texto)]

print("E-mails:", emails)
print("Telefones:", telefones)
# E-mails: ['ana.silva@empresa.com.br', 'financeiro@loja.com', 'suporte@loja.com']
# Telefones: ['11912345678', '2134567890', '11912345678']
```

---

> [!question] Exercícios
> 1. Verifique se uma string é um **CEP** válido no formato `12345-678` (ou `12345678`).
> 2. Extraia todos os **números** (inteiros e decimais com ponto) de `"Gastei 12 reais e 3.50 no ônibus"`.
> 3. Valide uma senha: mínimo 8 caracteres, ao menos uma maiúscula, uma minúscula e um dígito.
> 4. Converta datas `dd/mm/aaaa` em `aaaa-mm-dd` dentro de um texto.
> 5. Encontre palavras **repetidas** consecutivas (`"o o gato"`).
> 6. Remova **tags HTML** simples de um texto (`<p>Olá <b>mundo</b></p>` → `Olá mundo`) e explique por que isso não substitui um parser de HTML.
> 7. Dado `"nome=Ada; idade=36; cidade=Londres"`, produza um dicionário usando regex.
> 8. Mascare números de cartão (`1234 5678 9012 3456` → `**** **** **** 3456`).
> 9. Escreva `slugify("Olá, Mundo! Python 3.12")` → `ola-mundo-python-3-12` (remova acentos com `unicodedata`).
> 10. Explique a diferença entre `<.+>` e `<.+?>`.

> [!success]- Soluções
> 1. ```python
>    CEP = re.compile(r"\d{5}-?\d{3}")
>    eh_cep = lambda s: bool(CEP.fullmatch(s))
>    print(eh_cep("12345-678"), eh_cep("12345678"), eh_cep("1234-567"))   # True True False
>    ```
> 2. ```python
>    re.findall(r"\d+(?:\.\d+)?", "Gastei 12 reais e 3.50 no ônibus")    # ['12', '3.50']
>    ```
> 3. ```python
>    def senha_forte(s):
>        return bool(re.fullmatch(r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}", s))
>    ```
> 4. ```python
>    re.sub(r"(\d{2})/(\d{2})/(\d{4})", r"\3-\2-\1", "Hoje é 05/10/2026")
>    ```
> 5. ```python
>    re.findall(r"\b(\w+)\s+\1\b", "o o gato gato preto", re.I)    # ['o', 'gato']
>    ```
> 6. ```python
>    re.sub(r"<[^>]+>", "", "<p>Olá <b>mundo</b></p>")           # 'Olá mundo'
>    ```
>    HTML real tem atributos com `>`, comentários, `<script>`, aninhamento e entidades (`&amp;`); regex não entende estrutura aninhada. Use `html.parser` ou BeautifulSoup.
> 7. ```python
>    dict(re.findall(r"(\w+)=([^;]+)", "nome=Ada; idade=36; cidade=Londres"))
>    ```
> 8. ```python
>    re.sub(r"\d{4}(?= \d{4} \d{4} \d{4})|\d{4}(?= \d{4} \d{4}$)", "****", "1234 5678 9012 3456")
>    # forma simples:
>    "**** **** **** " + "1234 5678 9012 3456"[-4:]
>    ```
> 9. ```python
>    import re, unicodedata
>    def slugify(texto):
>        sem_acento = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
>        return re.sub(r"[^a-z0-9]+", "-", sem_acento.lower()).strip("-")
>    print(slugify("Olá, Mundo! Python 3.12"))     # ola-mundo-python-3-12
>    ```
> 10. `<.+>` é **gulosa**: vai até o **último** `>`. `<.+?>` é **preguiçosa**: pára no **primeiro** `>` possível.

---

⬅️ [[06 - Módulos da Biblioteca Padrão Essenciais/03 - collections itertools e functools|collections, itertools e functools]] | ➡️ [[06 - Módulos da Biblioteca Padrão Essenciais/05 - json csv e pickle|json, csv e pickle]]

#python #intermediario #stdlib #regex #re #expressoes-regulares #texto
