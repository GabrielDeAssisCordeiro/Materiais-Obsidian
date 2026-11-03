---
titulo: "Design Patterns Avançados e Clean Code"
tags: [python, avancado, design-patterns]
nivel: avancado
criado: 2026-10-09
modulo: "08 - Avançado"
---

# 🏛️ Design Patterns Avançados e Clean Code

> [!note] Contexto
> Padrões básicos (Singleton, Factory, Observer...) estão em [[04 - Programação Orientada a Objetos/06 - Design Patterns Básicos|Design Patterns Básicos]]. Aqui: padrões mais avançados, **como Python os simplifica** e princípios de código limpo.

> [!tip] Pythonic
> Muitos padrões "de livro" (pensados para Java/C++) viram **uma função, um módulo ou um decorator** em Python, porque funções são objetos de primeira classe ([[07 - Programação Funcional e Intermediário/01 - Funções de Ordem Superior|Ordem Superior]]).

## 1. Strategy: algoritmos intercambiáveis

### ❌ Hierarquia de classes desnecessária
```python
class DescontoBase:
    def calcular(self, valor): ...
class SemDesconto(DescontoBase): ...
class Black(DescontoBase): ...
```

### ✅ Funções
```python
from collections.abc import Callable

type Desconto = Callable[[float], float]

def sem_desconto(v: float) -> float: return v
def black_friday(v: float) -> float: return v * 0.7
def cupom10(v: float) -> float: return v - 10

def total(valor: float, estrategia: Desconto = sem_desconto) -> float:
    return estrategia(valor)

print(total(100, black_friday))   # 70.0
```

## 2. Command: ações como objetos (com desfazer)

```python
from dataclasses import dataclass
from typing import Protocol

class Comando(Protocol):
    def executar(self) -> None: ...
    def desfazer(self) -> None: ...

@dataclass
class Inserir:
    doc: list[str]
    texto: str
    def executar(self): self.doc.append(self.texto)
    def desfazer(self):  self.doc.pop()

doc: list[str] = []
historico: list[Comando] = []

for t in ["Olá", "mundo"]:
    c = Inserir(doc, t)
    c.executar()
    historico.append(c)

historico.pop().desfazer()
print(doc)    # ['Olá']
```

## 3. Observer com callbacks / sinais

```python
from collections import defaultdict
from collections.abc import Callable

class EventBus:
    def __init__(self):
        self._ouvintes: dict[str, list[Callable]] = defaultdict(list)

    def on(self, evento: str, fn: Callable) -> None:
        self._ouvintes[evento].append(fn)

    def emitir(self, evento: str, **dados) -> None:
        for fn in self._ouvintes[evento]:
            fn(**dados)

bus = EventBus()
bus.on("pedido", lambda id: print(f"email para pedido {id}"))
bus.on("pedido", lambda id: print(f"estoque baixado {id}"))
bus.emitir("pedido", id=42)
```

## 4. Decorator (padrão) = decorators do Python

Adicionar comportamento sem alterar o objeto ([[07 - Programação Funcional e Intermediário/03 - Decorators|Decorators]]): cache, log, retry, autenticação.

## 5. Adapter e Facade

```python
# Adapter: encaixa uma API externa na interface que você espera
class APIAntiga:
    def get_data_json(self) -> str: return '{"x": 1}'

class Adaptador:
    def __init__(self, antigo: APIAntiga): self._a = antigo
    def obter(self) -> dict:
        import json
        return json.loads(self._a.get_data_json())

# Facade: interface simples sobre subsistema complexo
class Video:
    def converter(self, arq: str) -> str:
        decoder, codec, mixer = ..., ..., ...   # (várias etapas escondidas)
        return arq.replace(".avi", ".mp4")
```

## 6. Dependency Injection

### ❌ Dependência embutida (difícil de testar)
```python
class Relatorio:
    def __init__(self):
        self.db = ConexaoPostgres()      # acoplado
```

### ✅ Injetada
```python
class Relatorio:
    def __init__(self, repo):            # qualquer objeto com .listar()
        self.repo = repo

class RepoFalso:
    def listar(self): return [1, 2, 3]

assert Relatorio(RepoFalso()).repo.listar() == [1, 2, 3]
```

Facilita **testes** ([[08 - Avançado/06 - Testes com unittest e pytest|pytest]]) e troca de implementação.

## 7. Repository

Isola o acesso a dados da regra de negócio:

```python
from typing import Protocol

class RepoUsuarios(Protocol):
    def obter(self, id: int) -> dict | None: ...
    def salvar(self, u: dict) -> None: ...

class RepoMemoria:
    def __init__(self): self._d: dict[int, dict] = {}
    def obter(self, id): return self._d.get(id)
    def salvar(self, u): self._d[u["id"]] = u
```

Reaparece em [[09 - Projetos Práticos/Projeto 07 - Login com SQLite|Login com SQLite]].

## 8. Builder (fluent) e Registry

```python
from typing import Self

class Query:
    def __init__(self): self._p = []
    def select(self, *c) -> Self: self._p.append(f"SELECT {', '.join(c)}"); return self
    def from_(self, t) -> Self:   self._p.append(f"FROM {t}"); return self
    def where(self, c) -> Self:   self._p.append(f"WHERE {c}"); return self
    def build(self) -> str: return " ".join(self._p)

print(Query().select("id", "nome").from_("usuarios").where("id = 1").build())
```

Registry com decorator:

```python
HANDLERS = {}
def handler(nome):
    def deco(f): HANDLERS[nome] = f; return f
    return deco

@handler("csv")
def ler_csv(p): ...
```

## 9. Padrões em Python vs. outras linguagens

| Padrão | Em Java/C++ | Em Python |
|---|---|---|
| Singleton | classe com `getInstance` | **módulo** (já é singleton) |
| Strategy | interface + classes | **funções** |
| Iterator | classe iteradora | **generators** |
| Decorator | wrapper de classes | `@decorator` |
| Factory | classe Factory | **função** ou `dict` de classes |
| Template Method | herança | herança ou função com callbacks |
| Observer | interfaces | callbacks/sinais |

## 10. Princípios SOLID (com Python)

| Letra | Princípio | Em uma frase | Dica em Python |
|---|---|---|---|
| **S** | Responsabilidade Única | uma razão para mudar | funções/classes pequenas |
| **O** | Aberto/Fechado | estender sem modificar | strategy, registry, `Protocol` |
| **L** | Substituição de Liskov | subclasse substitui a base sem surpresa | não enfraqueça contratos |
| **I** | Segregação de Interfaces | interfaces pequenas | `Protocol`s específicos |
| **D** | Inversão de Dependência | dependa de abstrações | injeção de dependência |

> [!warning] Composição > herança
> ```python
> class Pilha(list): ...         # ❌ herda 40 métodos que não fazem sentido (insert, sort...)
> class Pilha:                   # ✅ expõe só push/pop
>     def __init__(self): self._itens = []
>     def push(self, x): self._itens.append(x)
>     def pop(self): return self._itens.pop()
> ```

## 11. Clean Code em Python

### Nomes

```python
# ❌
def f(l, d): ...
# ✅
def filtrar_ativos(usuarios: list[Usuario], desde: date) -> list[Usuario]: ...
```

Convenções PEP 8: `snake_case` funções/variáveis, `PascalCase` classes, `UPPER_CASE` constantes.

### Funções pequenas e com uma tarefa

```python
# ❌ faz tudo
def processar(arquivo):
    ...  # lê, valida, calcula, imprime, grava

# ✅
def ler(arquivo): ...
def validar(dados): ...
def calcular(dados): ...
def salvar(resultado): ...
```

### Guard clauses (retorno antecipado)

```python
# ❌ aninhamento profundo
def desconto(u):
    if u:
        if u.ativo:
            if u.compras > 10:
                return 0.1
    return 0

# ✅
def desconto(u):
    if not u or not u.ativo:
        return 0
    return 0.1 if u.compras > 10 else 0
```

### Sem "números mágicos"

```python
# ❌
if idade >= 18: ...
# ✅
MAIORIDADE = 18
if idade >= MAIORIDADE: ...
```

### Retorne tipos consistentes

```python
# ❌ às vezes list, às vezes None
def buscar(x): return [] if not x else None
# ✅ sempre list
```

### EAFP vs LBYL

```python
# LBYL ("olhe antes de pular")
if "chave" in d: v = d["chave"]
# EAFP ("mais fácil pedir perdão") — idiomático
try: v = d["chave"]
except KeyError: v = None
# ou melhor: v = d.get("chave")
```

### Use a biblioteca padrão e idiomas Python

```python
# ❌
for i in range(len(lista)): print(i, lista[i])
# ✅
for i, x in enumerate(lista): print(i, x)

# ❌ if x == True
# ✅ if x
```

### Comentários explicam o **porquê**, não o **quê**

```python
# ❌ incrementa i
i += 1
# ✅ compensa o cabeçalho do CSV
i += 1
```

### Docstrings e tipos
Veja [[03 - Funções e Modularização/07 - Exercícios de Funções e Modularização|funções]] e [[07 - Programação Funcional e Intermediário/06 - Type Hints e typing|type hints]].

## 12. Code smells comuns

| Smell | Sintoma | Cura |
|---|---|---|
| Função gigante | > 30–40 linhas | extrair funções |
| Muitos parâmetros | > 4–5 | agrupar em `dataclass` |
| Duplicação | copiar/colar | extrair função (DRY) |
| `except:` nu / `except Exception: pass` | esconde erros | tratar o específico |
| Variáveis globais mutáveis | efeitos colaterais | passar parâmetros/classe |
| Classe "Deus" | faz tudo | dividir responsabilidades |
| Comentário que explica código obscuro | código ruim | renomear/refatorar |

## 13. Ferramentas

| Ferramenta | Função |
|---|---|
| **ruff** | lint + format (rápido) |
| **black** | formatador |
| **mypy / pyright** | tipos |
| **pytest + coverage** | testes |
| **pre-commit** | automatiza antes do commit |
| `python -m this` | O Zen do Python 🧘 |

> [!tip] O Zen do Python
> *Explícito é melhor que implícito. Simples é melhor que complexo. Legibilidade conta.* Rode `import this` no REPL.

## 14. Pegadinhas

> [!warning] 1. Padrão por padrão
> Aplicar patterns sem necessidade gera *overengineering*. Comece simples (YAGNI) e refatore quando a dor aparecer.

> [!warning] 2. Herança profunda
> Mais de 2–3 níveis vira pesadelo. Prefira composição.

> [!warning] 3. Abstrair cedo demais
> "Três repetições, então abstraia" (*rule of three*).

## 15. Exercícios

> [!question] 1. Refatore para Strategy com funções: um `if/elif` que escolhe entre `"pix"`, `"cartao"`, `"boleto"` para calcular taxas (0%, 3%, 1,5%).

> [!success]- Solução
> ```python
> TAXAS = {
>     "pix":    lambda v: v,
>     "cartao": lambda v: v * 1.03,
>     "boleto": lambda v: v * 1.015,
> }
>
> def cobrar(valor: float, metodo: str) -> float:
>     try:
>         return TAXAS[metodo](valor)
>     except KeyError:
>         raise ValueError(f"método inválido: {metodo}") from None
> ```

> [!question] 2. Implemente um sistema de **desfazer/refazer** com o padrão Command para uma lista de números.

> [!success]- Dica
> Duas pilhas: `desfeitos` e `refeitos`. Ao `executar`, limpe `refeitos`. Ao desfazer, mova o comando para `refeitos`.

> [!question] 3. Refatore a função abaixo aplicando guard clauses e nomes melhores:
> ```python
> def p(x):
>     if x is not None:
>         if len(x) > 0:
>             r = []
>             for i in x:
>                 if i > 0:
>                     r.append(i * 2)
>             return r
>     return []
> ```

> [!success]- Solução
> ```python
> def dobrar_positivos(numeros: list[int] | None) -> list[int]:
>     if not numeros:
>         return []
>     return [n * 2 for n in numeros if n > 0]
> ```

---

⬅️ [[08 - Avançado/07 - Packaging e Distribuição|Packaging e Distribuição]] | ➡️ [[08 - Avançado/09 - Exercícios de Python Avançado|Exercícios do Módulo 08]]

#python #avancado #design-patterns #clean-code #solid #refatoracao
