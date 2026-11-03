---
titulo: "Cheat Sheets"
tags: [python, recursos, cheatsheet, referencia]
nivel: todos
criado: 2026-10-14
---

# 🧾 Cheat Sheets

> [!tip] Para consulta rápida
> Cada seção aponta para a nota completa. Dica: fixe esta nota como aba no Obsidian.

## 1. Tipos e conversões — [[01 - Fundamentos/03 - Tipos de Dados Primitivos|nota]]

| Tipo | Exemplo | Mutável? |
|---|---|---|
| `int` / `float` / `complex` | `3`, `3.14`, `2+1j` | não |
| `bool` | `True`, `False` | não |
| `str` | `"olá"` | não |
| `list` | `[1, 2]` | **sim** |
| `tuple` | `(1, 2)` | não |
| `set` | `{1, 2}` | **sim** |
| `dict` | `{"a": 1}` | **sim** |
| `None` | `None` | — |

```python
int("42"); float("3.5"); str(10); bool([])      # False
list("abc"); tuple([1, 2]); set([1, 1, 2]); dict([("a", 1)])
type(x); isinstance(x, (int, float))
```

Valores **falsy**: `0`, `0.0`, `""`, `[]`, `{}`, `set()`, `()`, `None`, `False`.

## 2. Operadores — [[01 - Fundamentos/04 - Operadores|nota]]

```python
+  -  *  /  //  %  **          # aritméticos (/ sempre float; // divisão inteira)
==  !=  <  >  <=  >=           # comparação (encadeia: 0 < x < 10)
and  or  not                   # lógicos (curto-circuito)
in  not in  is  is not         # pertinência / identidade
+=  -=  *=  //=  :=            # atribuição (:= é o "walrus")
```

## 3. Strings — métodos úteis

```python
s.upper(); s.lower(); s.title(); s.strip(); s.lstrip(); s.rstrip()
s.split(","); ",".join(lista); s.replace("a", "b")
s.startswith("x"); s.endswith("y"); s.find("z")     # find → -1 se não achar
s.isdigit(); s.isalpha(); s.count("a"); s[::-1]
```

### f-strings

```python
nome, x, v = "Ana", 3.14159, 1234567.891
f"{nome!r}"          # 'Ana'
f"{x:.2f}"           # 3.14
f"{v:,.2f}"          # 1,234,567.89
f"{42:05d}"          # 00042
f"{0.256:.1%}"       # 25.6%
f"{nome:>10}|{nome:<10}|{nome:^10}"
f"{x=}"              # x=3.14159  (depuração)
```

## 4. Listas — [[02 - Controle de Fluxo e Estruturas de Dados/03 - Listas|nota]]

```python
l.append(x); l.extend(outra); l.insert(i, x)
l.pop(); l.pop(i); l.remove(x); l.clear()
l.sort(key=..., reverse=True)      # in-place, retorna None!
sorted(l)                           # nova lista
l.reverse(); l.index(x); l.count(x); l.copy()
l[1:4]; l[::2]; l[-1]; l[::-1]
```

## 5. Dicionários e sets — [[02 - Controle de Fluxo e Estruturas de Dados/06 - Dicionários|dict]] · [[02 - Controle de Fluxo e Estruturas de Dados/05 - Sets|set]]

```python
d.get("k", padrao); d.setdefault("k", []); d.pop("k", None)
d.keys(); d.values(); d.items(); d.update(outro)
d | outro                 # mescla (3.9+)
for k, v in d.items(): ...

a | b; a & b; a - b; a ^ b          # união, interseção, diferença, simétrica
a <= b; a.isdisjoint(b)
```

## 6. Comprehensions — [[02 - Controle de Fluxo e Estruturas de Dados/07 - Comprehensions|nota]]

```python
[x*x for x in range(10) if x % 2 == 0]
{x: len(x) for x in palavras}
{x % 3 for x in nums}
(x*x for x in range(10))           # generator expression
```

## 7. Controle de fluxo

```python
if x > 0: ...
elif x == 0: ...
else: ...

for i, item in enumerate(lista, start=1): ...
for a, b in zip(xs, ys): ...
for ... else: ...                  # else roda se NÃO houve break
while cond: ...; break; continue

match comando:
    case "sair": ...
    case [x, y]: ...
    case {"tipo": t}: ...
    case int() | float() as n if n > 0: ...
    case _: ...
```

## 8. Funções — [[03 - Funções e Modularização/01 - Definindo Funções|nota]]

```python
def f(a, b=1, /, c=2, *args, d, e=3, **kwargs) -> int: ...
#      posicional-apenas | normal | *args | nomeado-apenas | **kwargs
lambda x, y: x + y
f(*lista, **dicionario)
global x; nonlocal y
```

> [!warning] Pegadinha clássica
> `def f(x, lista=[])` — o padrão mutável é **compartilhado** entre chamadas. Use `None`.

## 9. Classes — [[04 - Programação Orientada a Objetos/01 - Classes e Objetos|nota]]

```python
from dataclasses import dataclass, field

@dataclass(slots=True, frozen=False)
class Ponto:
    x: float
    y: float = 0.0
    tags: list[str] = field(default_factory=list)

class A(Base):
    def __init__(self, v): super().__init__(); self._v = v
    @property
    def v(self): return self._v
    @v.setter
    def v(self, n): self._v = n
    @classmethod
    def criar(cls): ...
    @staticmethod
    def util(): ...
    def __repr__(self): return f"A({self._v!r})"
    def __eq__(self, o): ...
```

Dunders comuns: `__init__ __repr__ __str__ __eq__ __lt__ __hash__ __len__ __getitem__ __iter__ __next__ __call__ __enter__ __exit__ __contains__`.

## 10. Exceções — [[05 - Tratamento de Erros e Arquivos/01 - try except else finally|nota]]

```python
try:
    ...
except (ValueError, KeyError) as e:
    ...
except Exception:
    raise                     # re-levanta
else:
    ...                       # sem erro
finally:
    ...                       # sempre

raise MeuErro("msg") from causa
```

## 11. Arquivos e `pathlib` — [[05 - Tratamento de Erros e Arquivos/03 - Arquivos Texto CSV e JSON|nota]] · [[06 - Módulos da Biblioteca Padrão Essenciais/01 - os pathlib e sys|nota]]

```python
from pathlib import Path
p = Path("dados") / "x.txt"
p.exists(); p.is_file(); p.parent; p.name; p.stem; p.suffix
p.read_text(encoding="utf-8"); p.write_text("oi", encoding="utf-8")
p.mkdir(parents=True, exist_ok=True)
list(Path(".").glob("**/*.py"))

with open("a.txt", "r", encoding="utf-8") as f:    # modos: r w a x + b
    for linha in f: ...

import json, csv
json.dumps(obj, ensure_ascii=False, indent=2); json.loads(txt)
csv.DictReader(f); csv.DictWriter(f, fieldnames=[...])
```

## 12. `datetime` — [[06 - Módulos da Biblioteca Padrão Essenciais/02 - datetime e time|nota]]

| Código | Significado |
|---|---|
| `%Y` `%m` `%d` | ano 4 díg., mês, dia |
| `%H` `%M` `%S` | hora (24h), minuto, segundo |
| `%A` `%B` | dia da semana, nome do mês |
| `%j` | dia do ano |

```python
from datetime import datetime, timedelta, date
agora = datetime.now()
agora.strftime("%d/%m/%Y %H:%M")
datetime.strptime("25/12/2026", "%d/%m/%Y")
date.fromisoformat("2026-10-14") + timedelta(days=30)
```

## 13. Regex — [[06 - Módulos da Biblioteca Padrão Essenciais/04 - re Expressões Regulares|nota]]

| Padrão | Significa |
|---|---|
| `.` `\d` `\w` `\s` | qualquer / dígito / letra-número-_ / espaço |
| `*` `+` `?` `{n,m}` | 0+ / 1+ / 0 ou 1 / entre n e m |
| `^` `$` `\b` | início / fim / limite de palavra |
| `[abc]` `[^abc]` `(a\|b)` | conjunto / negado / alternativa |
| `(?P<nome>...)` | grupo nomeado |

```python
import re
re.search(r"(\d+)-(\d+)", s); re.findall(r"\w+", s)
re.sub(r"\s+", " ", s); re.compile(r"...", re.I)
```

## 14. `collections`, `itertools`, `functools` — [[06 - Módulos da Biblioteca Padrão Essenciais/03 - collections itertools e functools|nota]]

```python
from collections import Counter, defaultdict, deque, namedtuple
from itertools import chain, islice, groupby, product, permutations, combinations, batched, pairwise
from functools import lru_cache, partial, reduce, wraps, cache
```

## 15. Decorators, generators, context managers — [[07 - Programação Funcional e Intermediário/03 - Decorators|Decorators]] · [[07 - Programação Funcional e Intermediário/04 - Generators e Iterators|Generators]] · [[07 - Programação Funcional e Intermediário/05 - Context Managers Avançados|Context Managers]]

```python
def deco(func):
    @wraps(func)
    def wrapper(*a, **kw):
        return func(*a, **kw)
    return wrapper

def gen():
    yield 1
    yield from outro()

from contextlib import contextmanager
@contextmanager
def cm():
    try: yield
    finally: ...
```

## 16. Type hints — [[07 - Programação Funcional e Intermediário/06 - Type Hints e typing|nota]]

```python
def f(a: int, b: str | None = None) -> list[int]: ...
def primeiro[T](xs: list[T]) -> T: ...
type ID = int | str
from typing import Protocol, TypedDict, Literal, Callable, Self, override
```

## 17. Terminal: ambiente, pip, testes — [[03 - Funções e Modularização/05 - Virtual Environments e pip|nota]]

| Tarefa | Comando |
|---|---|
| Criar venv | `python -m venv .venv` |
| Ativar (Linux/macOS) | `source .venv/bin/activate` |
| Ativar (Windows) | `.venv\Scripts\activate` |
| Instalar | `pip install pacote` · `pip install -r requirements.txt` |
| Listar / congelar | `pip list` · `pip freeze > requirements.txt` |
| Executar módulo | `python -m modulo` |
| Testes | `pytest -q` · `pytest -k nome -x` · `pytest --cov` |
| Tipos | `mypy .` |
| Perfil de tempo | `python -m cProfile -s cumtime script.py` |
| Medir trecho | `python -m timeit "sum(range(1000))"` |

## 18. Depuração

```python
breakpoint()      # abre o pdb
```

| Comando `pdb` | Ação |
|---|---|
| `n` / `s` / `c` | próxima linha / entrar na função / continuar |
| `p expr` / `pp expr` | imprimir |
| `l` / `ll` | mostrar código |
| `b 42` | breakpoint na linha 42 |
| `q` | sair |

---

⬅️ [[10 - Recursos e Referências/03 - Canais e Cursos|Canais e Cursos]] | ➡️ [[Glossário#Python|Glossário]]

#python #recursos #cheatsheet #referencia
