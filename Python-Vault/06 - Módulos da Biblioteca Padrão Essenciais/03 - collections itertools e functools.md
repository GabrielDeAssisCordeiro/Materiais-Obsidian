---
titulo: "collections, itertools e functools"
tags: [python, intermediario, stdlib, collections, itertools, functools]
nivel: intermediario
criado: 2026-10-05
modulo: "06 - Módulos da Biblioteca Padrão Essenciais"
---

# 🧰 `collections`, `itertools` e `functools`

O "kit de ferramentas" que transforma código comum em código **elegante e eficiente**:

| Módulo | Contribui com |
|--------|---------------|
| `collections` | Estruturas de dados especializadas (`Counter`, `defaultdict`, `deque`...) |
| `itertools` | Blocos de construção para **iteradores** (combinações, agrupamentos, fatiamento) |
| `functools` | Ferramentas para **funções** (`partial`, `lru_cache`, `reduce`...) |

---

## 📦 `collections`

## 1. `Counter`: contagem de frequências

```python
from collections import Counter

c = Counter("abracadabra")
print(c)                         # Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
print(c["a"], c["z"])            # 5 0     (ausente = 0, sem KeyError!)
print(c.most_common(2))          # [('a', 5), ('b', 2)]

palavras = "o rato roeu a roupa do rei de roma".split()
print(Counter(palavras).most_common(1))    # [('o', 1)] (empate: ordem de inserção)
```

Operações:
```python
a = Counter(x=3, y=1)
b = Counter(x=1, y=2, z=4)

a + b          # Counter({'x': 4, 'z': 4, 'y': 3})
a - b          # Counter({'x': 2})        (só positivos)
a & b          # mínimos: Counter({'x': 1, 'y': 1})
a | b          # máximos
a.update("xx") # soma contagens
list(a.elements())   # ['x', 'x', 'x', 'x', 'x', 'y']
a.total()            # soma de todas as contagens (3.10+)
```

> [!tip] Substitui o padrão manual
> ```python
> # ❌ Manual
> freq = {}
> for x in itens:
>     freq[x] = freq.get(x, 0) + 1
> # ✅
> freq = Counter(itens)
> ```
> Revise em [[02 - Controle de Fluxo e Estruturas de Dados/06 - Dicionários#6. Padrões clássicos|padrões de dicionários]].

## 2. `defaultdict`: dicionário com valor padrão

```python
from collections import defaultdict

grupos = defaultdict(list)             # chave nova → lista vazia automaticamente
for nome, turma in [("Ana", "A"), ("Bruno", "B"), ("Carla", "A")]:
    grupos[turma].append(nome)
print(dict(grupos))                    # {'A': ['Ana', 'Carla'], 'B': ['Bruno']}

soma = defaultdict(int)                # int() → 0
for produto, valor in [("café", 10), ("pão", 2), ("café", 5)]:
    soma[produto] += valor

arvore = lambda: defaultdict(arvore)   # dicionário infinitamente aninhado
t = arvore()
t["a"]["b"]["c"] = 1
```

> [!warning] `defaultdict` **cria** a chave ao consultar
> ```python
> d = defaultdict(list)
> d["x"]                  # cria 'x': []  (efeito colateral!)
> "y" in d                # False (consulta com `in` NÃO cria)
> d.get("y")              # None  (get NÃO cria)
> ```

## 3. `deque`: fila dupla eficiente

Listas são lentas para remover/inserir no **início** (O(n)). O `deque` faz isso em O(1).

```python
from collections import deque

fila = deque([1, 2, 3])
fila.append(4)            # direita
fila.appendleft(0)        # esquerda
fila.pop()                # remove da direita → 4
fila.popleft()            # remove da esquerda → 0
fila.rotate(1)            # gira: [3, 1, 2]
print(fila)               # deque([3, 1, 2])

# Janela deslizante com tamanho máximo
ultimos = deque(maxlen=3)
for n in range(1, 7):
    ultimos.append(n)
print(ultimos)            # deque([4, 5, 6], maxlen=3)
```

| Estrutura | Fila (`popleft`) | Pilha (`pop`) | Acesso por índice `[i]` |
|-----------|------------------|---------------|-------------------------|
| `list` | O(n) 🐢 | O(1) | O(1) |
| `deque` | O(1) ⚡ | O(1) | O(n) no meio |

## 4. `namedtuple`, `OrderedDict`, `ChainMap`

```python
from collections import namedtuple, ChainMap, OrderedDict

Ponto = namedtuple("Ponto", "x y")
p = Ponto(1, 2)
print(p.x, p._asdict(), p._replace(x=10))
```
Veja [[02 - Controle de Fluxo e Estruturas de Dados/04 - Tuplas|namedtuple]].

```python
# ChainMap: consulta vários dicionários em ordem (ótimo para configurações)
padrao = {"tema": "claro", "fonte": 12}
usuario = {"fonte": 16}
cli = {}
cfg = ChainMap(cli, usuario, padrao)
print(cfg["fonte"], cfg["tema"])      # 16 claro
```
> `OrderedDict` é pouco necessário hoje (dicts já mantêm a ordem), mas oferece `move_to_end()`, útil para implementar caches LRU.

---

## 🔁 `itertools`

Funções que produzem **iteradores preguiçosos** (geram os itens sob demanda, sem criar listas gigantes). Complementa [[07 - Programação Funcional e Intermediário/04 - Generators e Iterators|Generators e Iterators]].

## 5. Infinitos

```python
from itertools import count, cycle, repeat, islice

list(islice(count(10, 5), 4))      # [10, 15, 20, 25]
list(islice(cycle("ABC"), 7))      # ['A','B','C','A','B','C','A']
list(repeat("x", 3))               # ['x', 'x', 'x']
```
> [!warning] Cuidado com laços infinitos
> `list(count())` trava o programa. Sempre limite com `islice`, `zip` ou `break`.

## 6. Combinando e fatiando

```python
from itertools import chain, islice, zip_longest, pairwise, batched

list(chain([1, 2], (3, 4), "ab"))                 # [1, 2, 3, 4, 'a', 'b']
list(chain.from_iterable([[1, 2], [3], [4, 5]]))  # achatar um nível

list(islice(range(100), 2, 8, 2))                 # [2, 4, 6]  (fatia de iterador)

list(zip_longest([1, 2, 3], ["a"], fillvalue="-"))
# [(1, 'a'), (2, '-'), (3, '-')]

list(pairwise([1, 4, 9, 16]))                     # [(1, 4), (4, 9), (9, 16)]  (3.10+)
list(batched(range(7), 3))                        # [(0,1,2), (3,4,5), (6,)]  (3.12+)
```

## 7. Acumulando

```python
from itertools import accumulate
import operator

list(accumulate([1, 2, 3, 4]))                    # [1, 3, 6, 10]  (soma acumulada)
list(accumulate([1, 2, 3, 4], operator.mul))      # [1, 2, 6, 24]
list(accumulate([3, 1, 4, 1, 5], max))            # [3, 3, 4, 4, 5]
```

## 8. Combinatória

```python
from itertools import product, permutations, combinations, combinations_with_replacement

list(product("AB", [1, 2]))
# [('A', 1), ('A', 2), ('B', 1), ('B', 2)]       produto cartesiano

list(product([0, 1], repeat=3))                  # todos os bytes de 3 bits (8 itens)

list(permutations("ABC", 2))                     # ordem importa
# [('A','B'), ('A','C'), ('B','A'), ('B','C'), ('C','A'), ('C','B')]

list(combinations("ABC", 2))                     # ordem NÃO importa
# [('A','B'), ('A','C'), ('B','C')]

list(combinations_with_replacement("AB", 2))
# [('A','A'), ('A','B'), ('B','B')]
```

| Função | Ordem importa? | Repete itens? | Total (n=4, r=2) |
|--------|:--------------:|:-------------:|:----------------:|
| `product(x, repeat=r)` | ✅ | ✅ | 16 |
| `permutations(x, r)` | ✅ | ❌ | 12 |
| `combinations(x, r)` | ❌ | ❌ | 6 |
| `combinations_with_replacement(x, r)` | ❌ | ✅ | 10 |

> [!warning] Explosão combinatória
> `permutations(range(15))` tem mais de **1 trilhão** de itens. Iteradores são preguiçosos, mas percorrer tudo continua inviável.

## 9. Filtrando e agrupando

```python
from itertools import takewhile, dropwhile, filterfalse, compress, starmap, groupby

list(takewhile(lambda x: x < 5, [1, 3, 5, 2]))    # [1, 3]    (para no 1º falso)
list(dropwhile(lambda x: x < 5, [1, 3, 5, 2]))    # [5, 2]    (descarta enquanto verdadeiro)
list(filterfalse(lambda x: x % 2, range(6)))      # [0, 2, 4] (inverso do filter)
list(compress("ABCDE", [1, 0, 1, 0, 1]))          # ['A', 'C', 'E']
list(starmap(pow, [(2, 3), (3, 2)]))              # [8, 9]    (desempacota argumentos)
```

### `groupby`: agrupa itens **consecutivos**
```python
dados = [("A", 1), ("A", 2), ("B", 3), ("A", 4)]

for chave, grupo in groupby(dados, key=lambda x: x[0]):
    print(chave, list(grupo))
# A [('A', 1), ('A', 2)]
# B [('B', 3)]
# A [('A', 4)]        ← 'A' aparece de novo: não estava consecutivo!
```

> [!warning] `groupby` exige dados **ordenados** pela mesma chave
> ```python
> dados.sort(key=lambda x: x[0])        # ✅ ordene primeiro
> for chave, grupo in groupby(dados, key=lambda x: x[0]):
>     print(chave, sum(v for _, v in grupo))     # A 7  /  B 3
> ```
> Cada `grupo` é um iterador **compartilhado**: consuma-o antes de avançar (ou use `list(grupo)`). Para agrupar sem ordenar, use `defaultdict(list)`.

## 10. `tee`: duplicar um iterador
```python
from itertools import tee
a, b = tee(iter([1, 2, 3]))
print(list(a), list(b))      # [1, 2, 3] [1, 2, 3]
```
> Depois do `tee`, **não use** o iterador original.

---

## 🔧 `functools`

## 11. `reduce`: dobrar uma sequência em um valor

```python
from functools import reduce
import operator

reduce(lambda acc, x: acc + x, [1, 2, 3, 4])        # 10
reduce(operator.mul, range(1, 6))                    # 120 (fatorial de 5)
reduce(lambda acc, x: acc * 10 + x, [1, 2, 3], 0)    # 123 (valor inicial 0)
```
> Quase sempre há uma opção mais legível (`sum`, `math.prod`, `max`...). Veja [[07 - Programação Funcional e Intermediário/02 - Lambda map filter reduce|Lambda, map, filter, reduce]].

## 12. `partial`: fixar argumentos

```python
from functools import partial

def potencia(base, expoente):
    return base ** expoente

quadrado = partial(potencia, expoente=2)
cubo = partial(potencia, expoente=3)
print(quadrado(5), cubo(2))        # 25 8

binario = partial(int, base=2)
print(binario("1010"))             # 10

# Útil em callbacks e threads
ler_utf8 = partial(open, encoding="utf-8")
```
Também resolve o *late binding* de [[03 - Funções e Modularização/03 - Escopo e Closures|lambdas em loops]].

## 13. Cache: `lru_cache` e `cache`

Guarda resultados de chamadas anteriores (**memoização**):

```python
from functools import cache, lru_cache
import time

@cache                                   # cache ilimitado (3.9+)
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)

print(fib(200))                          # instantâneo (sem cache seria impossível)

@lru_cache(maxsize=256)                  # mantém só os 256 mais recentes
def consultar(id_):
    time.sleep(1)                        # simula operação lenta
    return {"id": id_}

consultar(1)      # 1s
consultar(1)      # instantâneo
print(consultar.cache_info())            # CacheInfo(hits=1, misses=1, maxsize=256, currsize=1)
consultar.cache_clear()
```

> [!warning] Cuidados com cache
> - Os argumentos precisam ser **hasheáveis** (`list` e `dict` não servem; use tupla).
> - Só para funções **puras** (mesmo argumento → mesmo resultado). Não cacheie funções que dependem de relógio, rede ou estado mutável.
> - O cache ilimitado (`@cache`) **cresce sem parar**: use `lru_cache(maxsize=N)` em processos longos.
> - Em **métodos**, o cache segura referências a `self` (vazamento de memória): prefira `cached_property` ou cache em nível de função.

### `cached_property`
```python
from functools import cached_property

class Relatorio:
    def __init__(self, dados):
        self.dados = dados

    @cached_property
    def total(self):               # calcula 1x por instância
        return sum(self.dados)
```

## 14. `wraps`: preservando metadados em decorators

```python
from functools import wraps

def log(func):
    @wraps(func)                       # copia __name__, __doc__, etc.
    def wrapper(*args, **kwargs):
        print(f"Chamando {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
```
Sem `@wraps`, `funcao.__name__` viraria `"wrapper"`. Aprofunde em [[07 - Programação Funcional e Intermediário/03 - Decorators|Decorators]].

## 15. Outras ferramentas

```python
from functools import total_ordering, singledispatch, cmp_to_key

# total_ordering: gera <, <=, >, >= a partir de __eq__ e __lt__
# (veja Métodos Mágicos)

# singledispatch: polimorfismo por TIPO do 1º argumento
@singledispatch
def formatar(valor):
    return str(valor)

@formatar.register
def _(valor: int):
    return f"inteiro {valor:,}"

@formatar.register
def _(valor: list):
    return ", ".join(map(formatar, valor))

print(formatar(1234567))         # inteiro 1,234,567
print(formatar([1, 2]))          # inteiro 1, inteiro 2

# cmp_to_key: usar função de comparação antiga em sorted
sorted(["b", "A", "c"], key=cmp_to_key(lambda a, b: (a.lower() > b.lower()) - (a.lower() < b.lower())))
```
Mais sobre [[04 - Programação Orientada a Objetos/04 - Propriedades e Métodos Mágicos#Ordenação|total_ordering]].

---

## 16. Exemplo completo: análise de pedidos

```python
from collections import Counter, defaultdict
from itertools import groupby, islice, chain
from functools import reduce
import operator

pedidos = [
    {"cliente": "Ana",   "itens": ["café", "pão"],           "total": 20.5},
    {"cliente": "Bruno", "itens": ["leite", "café"],         "total": 14.0},
    {"cliente": "Ana",   "itens": ["pão"],                   "total": 3.0},
    {"cliente": "Carla", "itens": ["café", "leite", "pão"],  "total": 25.0},
]

# Itens mais vendidos
todos = chain.from_iterable(p["itens"] for p in pedidos)
print(Counter(todos).most_common(2))              # [('café', 3), ('pão', 3)]

# Total por cliente
por_cliente = defaultdict(float)
for p in pedidos:
    por_cliente[p["cliente"]] += p["total"]
print(dict(por_cliente))                          # {'Ana': 23.5, 'Bruno': 14.0, 'Carla': 25.0}

# Quantidade de pedidos por cliente (groupby com dados ordenados)
ordenados = sorted(pedidos, key=lambda p: p["cliente"])
for cliente, grupo in groupby(ordenados, key=lambda p: p["cliente"]):
    print(cliente, len(list(grupo)))

# Faturamento total
print(reduce(operator.add, (p["total"] for p in pedidos)))   # 62.5
```

---

> [!question] Exercícios
> 1. Descubra a letra mais comum de um texto (ignorando espaços) e as 3 palavras mais comuns.
> 2. Agrupe uma lista de palavras pelo **tamanho** usando `defaultdict(list)`.
> 3. Mantenha um histórico dos **últimos 5** comandos digitados com `deque(maxlen=5)`.
> 4. Gere todas as **senhas de 3 dígitos** (`000`–`999`) com `product`.
> 5. Calcule a média móvel de janela 3 de `[1, 2, 3, 4, 5, 6]` usando `deque` ou `batched`/`islice`.
> 6. Gere todos os **pares (sem repetir)** de uma lista de 5 pessoas e conte-os (`combinations`).
> 7. Use `groupby` para comprimir `"aaabbbccd"` em `[('a', 3), ('b', 3), ('c', 2), ('d', 1)]`.
> 8. Implemente `fib` com `@cache` e meça a diferença para a versão sem cache com `n=35`.
> 9. Crie, com `partial`, a função `arredondar_2(x)` baseada em `round`.
> 10. Achate `[[1, 2], [3], [4, 5, 6]]` com `chain.from_iterable` e some com `accumulate`.

> [!success]- Soluções
> 1. ```python
>    from collections import Counter
>    texto = "o rato roeu a roupa do rei de roma"
>    print(Counter(texto.replace(" ", "")).most_common(1))
>    print(Counter(texto.split()).most_common(3))
>    ```
> 2. ```python
>    from collections import defaultdict
>    g = defaultdict(list)
>    for p in ["sol", "lua", "estrela", "mar", "céu"]:
>        g[len(p)].append(p)
>    ```
> 3. ```python
>    from collections import deque
>    historico = deque(maxlen=5)
>    while (cmd := input("> ")) != "sair":
>        historico.append(cmd)
>        print(list(historico))
>    ```
> 4. ```python
>    from itertools import product
>    senhas = ["".join(p) for p in product("0123456789", repeat=3)]
>    print(len(senhas), senhas[:3])      # 1000 ['000', '001', '002']
>    ```
> 5. ```python
>    from collections import deque
>    janela, medias = deque(maxlen=3), []
>    for x in [1, 2, 3, 4, 5, 6]:
>        janela.append(x)
>        if len(janela) == 3:
>            medias.append(sum(janela) / 3)
>    print(medias)    # [2.0, 3.0, 4.0, 5.0]
>    ```
> 6. ```python
>    from itertools import combinations
>    pares = list(combinations(["Ana", "Bia", "Caio", "Davi", "Eva"], 2))
>    print(len(pares))    # 10
>    ```
> 7. ```python
>    from itertools import groupby
>    print([(c, len(list(g))) for c, g in groupby("aaabbbccd")])
>    ```
> 8. ```python
>    import time
>    from functools import cache
>    def fib_lento(n): return n if n < 2 else fib_lento(n-1) + fib_lento(n-2)
>    @cache
>    def fib_rapido(n): return n if n < 2 else fib_rapido(n-1) + fib_rapido(n-2)
>    for f in (fib_lento, fib_rapido):
>        t = time.perf_counter(); f(35)
>        print(f.__name__, f"{time.perf_counter() - t:.4f}s")
>    ```
> 9. ```python
>    from functools import partial
>    arredondar_2 = partial(round, ndigits=2)
>    print(arredondar_2(3.14159))     # 3.14
>    ```
> 10. ```python
>     from itertools import chain, accumulate
>     print(list(accumulate(chain.from_iterable([[1, 2], [3], [4, 5, 6]]))))
>     # [1, 3, 6, 10, 15, 21]
>     ```

---

⬅️ [[06 - Módulos da Biblioteca Padrão Essenciais/02 - datetime e time|datetime e time]] | ➡️ [[06 - Módulos da Biblioteca Padrão Essenciais/04 - re Expressões Regulares|re (Expressões Regulares)]]

#python #intermediario #stdlib #collections #itertools #functools #counter #deque #cache
