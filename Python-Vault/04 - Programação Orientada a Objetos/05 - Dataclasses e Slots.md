---
titulo: "Dataclasses e Slots"
tags: [python, intermediario, poo]
nivel: intermediario
criado: 2026-10-05
modulo: "04 - Programação Orientada a Objetos"
---

# 🗃️ Dataclasses e Slots

Muitas classes existem **só para guardar dados**. Escrever `__init__`, `__repr__` e `__eq__` à mão, sempre igual, é repetitivo. As **dataclasses** (módulo `dataclasses`, desde o Python 3.7) geram tudo isso para você.

---

## 1. O problema: boilerplate

```python
class Ponto:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Ponto(x={self.x!r}, y={self.y!r}, z={self.z!r})"

    def __eq__(self, outro):
        if not isinstance(outro, Ponto):
            return NotImplemented
        return (self.x, self.y, self.z) == (outro.x, outro.y, outro.z)
```

## 2. A solução: `@dataclass`

```python
from dataclasses import dataclass

@dataclass
class Ponto:
    x: float
    y: float
    z: float = 0.0


p = Ponto(1.5, 2.0)
print(p)                         # Ponto(x=1.5, y=2.0, z=0.0)
print(p == Ponto(1.5, 2.0))      # True
print(p.x)                       # 1.5
```

O decorator lê as **anotações de tipo** e gera automaticamente:

| Método | O que faz |
|--------|-----------|
| `__init__` | Recebe os campos como parâmetros |
| `__repr__` | Representação legível |
| `__eq__` | Compara campo a campo |

> [!note] Os tipos são só anotações
> O `@dataclass` **não valida** os tipos em execução (`Ponto("a", "b")` funciona). Eles servem para documentação e para ferramentas como mypy/pyright ([[07 - Programação Funcional e Intermediário/06 - Type Hints e typing|Type Hints]]).

> [!warning] Todo campo precisa de anotação
> ```python
> @dataclass
> class A:
>     x = 1            # ❌ sem anotação: é atributo de CLASSE, não campo
>     y: int = 1       # ✅ campo
> ```

---

## 3. Valores padrão e `field()`

### Padrões simples
```python
@dataclass
class Usuario:
    nome: str
    ativo: bool = True
    nivel: int = 1
```

> [!warning] Campos com padrão vêm **depois** dos obrigatórios
> ```python
> @dataclass
> class Errada:
>     ativo: bool = True
>     nome: str          # ❌ TypeError: non-default argument 'nome' follows default argument
> ```
> (Solução: reordenar ou usar `kw_only=True`, veja abaixo.)

### Padrões **mutáveis**: use `default_factory`
```python
from dataclasses import dataclass, field

@dataclass
class Turma:
    nome: str
    alunos: list[str] = []          # ❌ ValueError: mutable default is not allowed

@dataclass
class Turma:
    nome: str
    alunos: list[str] = field(default_factory=list)    # ✅ lista nova por instância
```
O Python **protege você** da [[03 - Funções e Modularização/02 - args kwargs e Argumentos Padrão|armadilha do padrão mutável]].

### Opções de `field()`

| Opção | Efeito |
|-------|--------|
| `default=valor` | Valor padrão |
| `default_factory=func` | Função que cria o padrão (listas, dicts, sets, `datetime.now`...) |
| `init=False` | Campo **não** vai para o `__init__` |
| `repr=False` | Fora do `__repr__` (ex.: senhas) |
| `compare=False` | Fora do `__eq__` e da ordenação |
| `kw_only=True` | Campo só nomeado |
| `metadata={...}` | Dados extras para ferramentas |

```python
from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Conta:
    titular: str
    senha: str = field(repr=False)                       # não aparece no print
    criada_em: datetime = field(default_factory=datetime.now)
    historico: list[float] = field(default_factory=list)
    id: int = field(init=False, default=0)
```

---

## 4. Opções do decorator

```python
@dataclass(frozen=True, order=True, slots=True, kw_only=True)
class Versao:
    maior: int
    menor: int = 0
```

| Opção | Efeito |
|-------|--------|
| `frozen=True` | **Imutável**: atribuir a um campo levanta `FrozenInstanceError`; gera `__hash__` |
| `order=True` | Gera `<`, `<=`, `>`, `>=` comparando os campos **em ordem** |
| `slots=True` | Usa `__slots__` (3.10+): menos memória, sem `__dict__` |
| `kw_only=True` | Todos os campos só **nomeados** (3.10+) |
| `eq=False` | Não gera `__eq__` |
| `repr=False` | Não gera `__repr__` |
| `unsafe_hash=True` | Força `__hash__` mesmo sendo mutável (cuidado) |

### 4.1 `frozen=True`: objetos imutáveis
```python
@dataclass(frozen=True)
class Coordenada:
    lat: float
    lon: float

c = Coordenada(-23.55, -46.63)
c.lat = 0                        # ❌ FrozenInstanceError: cannot assign to field 'lat'
print({c: "São Paulo"})          # ✅ hasheável: pode ser chave de dict ou item de set
```
> [!tip] Prefira imutáveis sempre que possível
> Objetos imutáveis são mais **seguros** (sem mudanças inesperadas), **hasheáveis** e ótimos em código concorrente.

### 4.2 `order=True`
```python
@dataclass(order=True)
class Aluno:
    nota: float
    nome: str

alunos = [Aluno(8.5, "Bruno"), Aluno(9.0, "Ana"), Aluno(8.5, "Alice")]
print(sorted(alunos))
# [Aluno(nota=8.5, nome='Alice'), Aluno(nota=8.5, nome='Bruno'), Aluno(nota=9.0, nome='Ana')]
```
Compara como **tuplas**: primeiro `nota`, depois `nome`. Para ordenar só por um campo, use `field(compare=False)` nos outros.

### 4.3 `kw_only=True`: chamadas legíveis
```python
@dataclass(kw_only=True)
class Config:
    host: str = "localhost"
    porta: int = 8080
    debug: bool = False

Config(porta=3000, debug=True)    # ✅
Config("x", 3000)                 # ❌ TypeError: só aceita argumentos nomeados
```

---

## 5. `__post_init__`: validação e campos derivados

Roda **logo após** o `__init__` gerado:

```python
from dataclasses import dataclass, field

@dataclass
class Retangulo:
    base: float
    altura: float
    area: float = field(init=False)

    def __post_init__(self):
        if self.base <= 0 or self.altura <= 0:
            raise ValueError("Dimensões devem ser positivas")
        self.area = self.base * self.altura

r = Retangulo(3, 4)
print(r)    # Retangulo(base=3, altura=4, area=12)
```

> [!warning] Com `frozen=True`, atribua via `object.__setattr__`
> ```python
> @dataclass(frozen=True)
> class R:
>     base: float
>     area: float = field(init=False)
>     def __post_init__(self):
>         object.__setattr__(self, "area", self.base ** 2)
> ```
> (Muitas vezes, uma `@property` é mais simples.)

### `InitVar`: parâmetro só para o `__init__`
```python
from dataclasses import dataclass, InitVar

@dataclass
class Usuario:
    nome: str
    senha: InitVar[str]            # recebido, mas NÃO vira atributo
    hash_senha: str = ""

    def __post_init__(self, senha):
        self.hash_senha = f"hash({senha})"
```

---

## 6. Utilitários

```python
from dataclasses import asdict, astuple, replace, fields, is_dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int

p = Pessoa("Ada", 36)

print(asdict(p))               # {'nome': 'Ada', 'idade': 36}  (ótimo para JSON)
print(astuple(p))              # ('Ada', 36)
p2 = replace(p, idade=37)      # cópia com alteração (útil com frozen=True!)
print(p2)                      # Pessoa(nome='Ada', idade=37)
print([f.name for f in fields(p)])   # ['nome', 'idade']
print(is_dataclass(p))         # True
```

Serialização com [[05 - Tratamento de Erros e Arquivos/03 - Arquivos Texto CSV e JSON|JSON]]:
```python
import json
print(json.dumps(asdict(p), ensure_ascii=False))
```

---

## 7. Herança com dataclasses

```python
@dataclass
class Pessoa:
    nome: str
    idade: int

@dataclass
class Aluno(Pessoa):
    curso: str = "Python"

a = Aluno("Ada", 36, "Matemática")
print(a)    # Aluno(nome='Ada', idade=36, curso='Matemática')
```
> [!warning] Campos da mãe com padrão + filha sem padrão = erro
> A ordem dos campos é: mãe primeiro, depois filha. Se a mãe tem campo **com** padrão, todos os da filha também precisam ter. Solução moderna: `kw_only=True`.

---

## 8. Dataclass vs outras opções

| Opção | Mutável | Hasheável | Tipos | Quando usar |
|-------|:-------:|:---------:|:-----:|-------------|
| **`dataclass`** | ✅ | só `frozen` | ✅ | Padrão para classes de dados |
| **`dataclass(frozen=True)`** | ❌ | ✅ | ✅ | Valores imutáveis |
| `NamedTuple` | ❌ | ✅ | ✅ | Registros leves e imutáveis ([[02 - Controle de Fluxo e Estruturas de Dados/04 - Tuplas\|veja]]) |
| `dict` | ✅ | ❌ | ❌ | Dados dinâmicos / JSON bruto |
| Classe comum | ✅ | você decide | ❌ | Muita lógica e comportamento |
| Pydantic / attrs | ✅ | | ✅ + **validação** | Validação em runtime, APIs |

---

## 🧊 Slots: economizando memória

## 9. O que é `__slots__`?

Normalmente cada objeto guarda seus atributos em um **dicionário** (`obj.__dict__`), flexível, porém **gasta memória**. Com `__slots__`, você declara **quais atributos** existem e o Python usa uma estrutura compacta.

```python
class PontoNormal:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class PontoSlots:
    __slots__ = ("x", "y")
    def __init__(self, x, y):
        self.x = x
        self.y = y

import sys
a, b = PontoNormal(1, 2), PontoSlots(1, 2)
print(hasattr(a, "__dict__"), hasattr(b, "__dict__"))   # True False
print(sys.getsizeof(a.__dict__))                         # ~100+ bytes só pelo dict
```

### Benefícios
- 📉 **Menos memória** por instância (relevante com milhões de objetos)
- ⚡ Acesso a atributos ligeiramente mais rápido
- 🛡️ **Impede atributos acidentais** (erros de digitação viram erro)

```python
p = PontoSlots(1, 2)
p.z = 3          # ❌ AttributeError: 'PontoSlots' object has no attribute 'z'
p.nmoe = 1       # ❌ idem (um typo é pego na hora!)
```

### Limitações
> [!warning] Pegadinhas dos slots
> - Sem `__dict__`: não dá para criar atributos dinâmicos
> - Sem `__weakref__` por padrão (adicione `"__weakref__"` aos slots se precisar de referências fracas)
> - **Herança**: a subclasse sem `__slots__` volta a ter `__dict__`; slots repetidos na filha desperdiçam espaço
> - Incompatível com valores padrão no corpo da classe iguais ao nome do slot:
>   ```python
>   class A:
>       __slots__ = ("x",)
>       x = 0          # ❌ ValueError: 'x' in __slots__ conflicts with class variable
>   ```
> - Não use "por precaução": só vale a pena com **muitas instâncias**

### O jeito moderno: `@dataclass(slots=True)`
```python
@dataclass(slots=True)
class Ponto:
    x: float
    y: float

p = Ponto(1, 2)
p.z = 3        # ❌ AttributeError
```
Simples e sem escrever `__slots__` à mão.

### Medindo a diferença
```python
import tracemalloc
from dataclasses import dataclass

@dataclass
class Normal:
    a: int; b: int; c: int

@dataclass(slots=True)
class ComSlots:
    a: int; b: int; c: int

for cls in (Normal, ComSlots):
    tracemalloc.start()
    objs = [cls(1, 2, 3) for _ in range(100_000)]
    atual, _ = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"{cls.__name__:<10} {atual / 1024 / 1024:.1f} MB")
```
Em geral, a versão com slots usa **bem menos memória**. Ferramentas de medição em [[08 - Avançado/05 - Performance e Profiling|Performance e Profiling]].

---

## 10. Exemplo completo: inventário

```python
from dataclasses import dataclass, field, asdict
import json

@dataclass(frozen=True, slots=True)
class Produto:
    sku: str
    nome: str
    preco: float

    def __post_init__(self):
        if self.preco < 0:
            raise ValueError("Preço negativo")


@dataclass
class Inventario:
    itens: dict[str, int] = field(default_factory=dict)

    def adicionar(self, produto: Produto, qtd: int = 1):
        self.itens[produto.sku] = self.itens.get(produto.sku, 0) + qtd

    def total(self, catalogo: dict[str, Produto]) -> float:
        return sum(catalogo[sku].preco * q for sku, q in self.itens.items())


cafe = Produto("CAF-01", "Café 500g", 18.9)
pao = Produto("PAO-01", "Pão", 1.5)
catalogo = {p.sku: p for p in (cafe, pao)}

inv = Inventario()
inv.adicionar(cafe, 3)
inv.adicionar(pao, 10)

print(f"Total: R$ {inv.total(catalogo):.2f}")           # R$ 71.70
print(json.dumps(asdict(cafe), ensure_ascii=False))
```

---

> [!question] Exercícios
> 1. Crie a dataclass `Livro` (`titulo`, `autor`, `ano`, `paginas=0`) e mostre `print`, igualdade e `asdict`.
> 2. Crie `Playlist` com lista de músicas usando `field(default_factory=list)`. Mostre o erro de usar `[]` direto.
> 3. Crie `Ponto` imutável com `frozen=True` e use-o como chave de dicionário.
> 4. Crie `Funcionario(order=True)` e ordene por salário (use `field(compare=False)` no nome).
> 5. Adicione validação em `__post_init__` à classe `Circulo(raio)` (raio > 0) e um campo calculado `area` (`init=False`).
> 6. Use `replace` para criar uma cópia de uma dataclass imutável com um campo alterado.
> 7. Compare a memória de 200 mil objetos com e sem `slots=True`.
> 8. Quando **não** usar dataclass?

> [!success]- Soluções
> 1. ```python
>    from dataclasses import dataclass, asdict
>    @dataclass
>    class Livro:
>        titulo: str
>        autor: str
>        ano: int
>        paginas: int = 0
>    l = Livro("Dom Casmurro", "Machado de Assis", 1899)
>    print(l, l == Livro("Dom Casmurro", "Machado de Assis", 1899), asdict(l))
>    ```
> 2. ```python
>    from dataclasses import dataclass, field
>    @dataclass
>    class Playlist:
>        nome: str
>        musicas: list[str] = field(default_factory=list)
>    # musicas: list[str] = []   → ValueError: mutable default <class 'list'> ... use default_factory
>    ```
> 3. ```python
>    @dataclass(frozen=True)
>    class Ponto:
>        x: int
>        y: int
>    mapa = {Ponto(0, 0): "origem"}
>    ```
> 4. ```python
>    @dataclass(order=True)
>    class Funcionario:
>        salario: float
>        nome: str = field(compare=False)
>    print(sorted([Funcionario(3000, "Ana"), Funcionario(2500, "Bruno")]))
>    ```
> 5. ```python
>    @dataclass
>    class Circulo:
>        raio: float
>        area: float = field(init=False)
>        def __post_init__(self):
>            if self.raio <= 0:
>                raise ValueError("Raio deve ser positivo")
>            self.area = 3.14159 * self.raio ** 2
>    ```
> 6. ```python
>    from dataclasses import replace
>    c1 = Coordenada(-23.5, -46.6)
>    c2 = replace(c1, lat=-22.9)
>    ```
> 7. Use o código de `tracemalloc` da seção 9 com `range(200_000)`; a versão `slots=True` consome visivelmente menos.
> 8. Quando há **muita lógica** e pouco "dado puro", quando precisa de **validação robusta em runtime** (prefira Pydantic/attrs) ou quando uma estrutura simples (`dict`, `tuple`, `NamedTuple`) resolve.

---

⬅️ [[04 - Programação Orientada a Objetos/04 - Propriedades e Métodos Mágicos|Propriedades e Métodos Mágicos]] | ➡️ [[04 - Programação Orientada a Objetos/06 - Design Patterns Básicos|Design Patterns Básicos]]

#python #intermediario #poo #dataclasses #slots #imutabilidade
