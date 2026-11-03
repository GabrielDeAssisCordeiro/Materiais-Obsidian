---
titulo: "Tuplas (tuple)"
tags: [python, basico, estruturas-de-dados]
nivel: iniciante
criado: 2026-10-05
modulo: "02 - Controle de Fluxo e Estruturas de Dados"
---

# 📦 Tuplas (`tuple`)

Uma **tupla** é uma coleção **ordenada** e **imutável**. Pense nela como uma **lista "congelada"**: depois de criada, não dá para adicionar, remover ou trocar itens.

| Característica | Tupla | [[02 - Controle de Fluxo e Estruturas de Dados/03 - Listas\|Lista]] |
|----------------|-------|-------|
| Ordenada | ✅ | ✅ |
| Mutável | ❌ | ✅ |
| Permite repetidos | ✅ | ✅ |
| Sintaxe | `(1, 2, 3)` | `[1, 2, 3]` |
| Pode ser chave de dict / item de set | ✅ (se os itens forem imutáveis) | ❌ |
| Uso típico | Dados fixos, registros, retornos múltiplos | Coleções que mudam |

---

## 1. Criando tuplas

```python
vazia = ()
ponto = (3, 4)
mista = ("Ada", 28, True)
sem_parenteses = 1, 2, 3        # os parênteses são opcionais!
convertida = tuple([1, 2, 3])
letras = tuple("abc")           # ('a', 'b', 'c')
```

> [!note] É a vírgula que faz a tupla
> Os parênteses são só agrupamento. O que define uma tupla é a **vírgula**.

> [!warning] Armadilha: tupla de um elemento
> ```python
> # ❌ Isso é só um int entre parênteses!
> t = (5)
> print(type(t))      # <class 'int'>
>
> # ✅ Precisa da vírgula
> t = (5,)
> print(type(t))      # <class 'tuple'>
> ```

---

## 2. Acessando elementos

Igual às listas: índices, negativos e fatias.

```python
cor = (255, 128, 0)
print(cor[0])        # 255
print(cor[-1])       # 0
print(cor[:2])       # (255, 128)
print(len(cor))      # 3
```

---

## 3. Imutabilidade

```python
t = (1, 2, 3)

# ❌ Errado
t[0] = 10            # TypeError: 'tuple' object does not support item assignment
t.append(4)          # AttributeError: 'tuple' object has no attribute 'append'

# ✅ Crie uma nova tupla
t = (10,) + t[1:]    # (10, 2, 3)
```

> [!warning] Imutável "por fora", não necessariamente "por dentro"
> Se a tupla contiver um objeto **mutável**, esse objeto ainda pode mudar:
> ```python
> t = (1, [2, 3])
> t[1].append(4)
> print(t)             # (1, [2, 3, 4])  😮
> ```
> A tupla guarda **referências** que não mudam, mas a lista referenciada pode mudar. Consequência: uma tupla com lista dentro **não** pode ser usada como chave de dicionário.

---

## 4. Métodos disponíveis

Como é imutável, a tupla tem só dois métodos:

```python
t = (1, 2, 2, 3)
print(t.count(2))    # 2
print(t.index(3))    # 3
```

Funções nativas que também servem: `len`, `min`, `max`, `sum`, `sorted` (devolve **lista**), `in`.

```python
print(sorted((3, 1, 2)))     # [1, 2, 3]  ← lista!
print(tuple(sorted((3, 1, 2))))   # (1, 2, 3)
```

---

## 5. Desempacotamento (*unpacking*)

O recurso mais usado com tuplas:

```python
ponto = (3, 4)
x, y = ponto
print(x, y)          # 3 4

nome, idade, cidade = ("Ada", 28, "Londres")
```

> [!warning] A quantidade precisa bater
> ```python
> a, b = (1, 2, 3)    # ❌ ValueError: too many values to unpack (expected 2)
> ```

### Com `*` (itens restantes)
```python
primeiro, *resto = (1, 2, 3, 4)
print(primeiro, resto)       # 1 [2, 3, 4]    (resto vira lista)

*inicio, ultimo = (1, 2, 3, 4)
a, *meio, z = (1, 2, 3, 4, 5)
```

### Ignorando valores com `_`
```python
nome, _, cidade = ("Ada", 28, "Londres")
```

### Troca de variáveis
```python
a, b = 1, 2
a, b = b, a          # na verdade cria a tupla (b, a) e desempacota
```

---

## 6. Retornando vários valores de funções

Funções retornam **uma** coisa, mas essa coisa pode ser uma tupla:

```python
def min_max(numeros):
    return min(numeros), max(numeros)    # tupla (min, max)

menor, maior = min_max([4, 9, 1, 7])
print(menor, maior)      # 1 9

resultado = min_max([4, 9, 1, 7])
print(resultado)         # (1, 9)
```
Veja [[03 - Funções e Modularização/01 - Definindo Funções|Funções]].

---

## 7. Tuplas como chaves e em sets

Como são imutáveis (e hasheáveis, se os itens forem), servem de **chave**:

```python
distancias = {
    ("SP", "RJ"): 430,
    ("SP", "BH"): 586,
}
print(distancias[("SP", "RJ")])      # 430

visitados = {(0, 0), (0, 1)}         # set de coordenadas
```
Veja [[02 - Controle de Fluxo e Estruturas de Dados/05 - Sets|Sets]] e [[02 - Controle de Fluxo e Estruturas de Dados/06 - Dicionários|Dicionários]].

---

## 8. Percorrendo tuplas

```python
for valor in (10, 20, 30):
    print(valor)

pares = [("a", 1), ("b", 2)]
for letra, numero in pares:        # desempacota a cada volta
    print(letra, numero)
```

---

## 9. `namedtuple`: tuplas com nomes

Quando os índices (`t[0]`, `t[1]`) ficam confusos, use `namedtuple`:

```python
from collections import namedtuple

Pessoa = namedtuple("Pessoa", ["nome", "idade"])
p = Pessoa("Ada", 28)

print(p.nome)        # 'Ada'
print(p[1])          # 28   (ainda é tupla!)
print(p)             # Pessoa(nome='Ada', idade=28)

nome, idade = p      # desempacota normalmente
```

### Versão moderna com tipos: `typing.NamedTuple`
```python
from typing import NamedTuple

class Ponto(NamedTuple):
    x: float
    y: float = 0.0

p = Ponto(3.5)
print(p)       # Ponto(x=3.5, y=0.0)
```
Se precisar de **mutabilidade**, prefira [[04 - Programação Orientada a Objetos/05 - Dataclasses e Slots|dataclasses]].

---

## 10. Quando usar tupla em vez de lista?

> [!tip] Regra prática
> - **Tupla** → itens de **natureza diferente** que formam um registro (`("Ada", 28, "SP")`), coordenadas, retorno múltiplo, dados que **não devem mudar**.
> - **Lista** → itens de **mesma natureza** (todas notas, todos nomes) cuja quantidade pode variar.

Vantagens extras das tuplas:
- Levemente **mais rápidas** e usam **menos memória** que listas
- Servem como **chaves** de dicionário
- Comunicam intenção: "estes dados são fixos"

```python
import sys
print(sys.getsizeof([1, 2, 3]))   # maior
print(sys.getsizeof((1, 2, 3)))   # menor
```

---

## 11. Comparando tuplas

A comparação é **lexicográfica** (item a item):
```python
print((1, 2, 3) < (1, 2, 4))     # True
print((1, 5) < (2, 0))           # True
print((1, 2) == (1, 2))          # True
```
Útil para ordenar por vários critérios:
```python
alunos = [("Ana", 8), ("Bruno", 9), ("Carla", 8)]
alunos.sort(key=lambda a: (-a[1], a[0]))
```

---

> [!question] Exercícios
> 1. Crie a tupla `(10, 20, 30, 40)` e imprima o segundo e o último elemento.
> 2. Por que `t = (7)` não cria uma tupla? Corrija.
> 3. Escreva uma função `estatisticas(lista)` que retorne **menor, maior e média**, e use desempacotamento para receber.
> 4. Dado `dados = ("Ada", 28, "Londres", "Matemática")`, use desempacotamento com `*` para pegar nome e idade e guardar o resto numa variável.
> 5. Crie um dicionário que use coordenadas `(x, y)` como chave para guardar o nome de lugares.
> 6. O que acontece?
>    ```python
>    t = ([1], [2])
>    t[0].append(9)
>    print(t)
>    ```
> 7. Crie uma `namedtuple` `Produto` com `nome` e `preco`, e ordene uma lista de produtos por preço.

> [!success]- Soluções
> 1. `t = (10, 20, 30, 40); print(t[1], t[-1])`
> 2. Sem vírgula, os parênteses são só agrupamento → `int`. Correto: `t = (7,)`.
> 3. ```python
>    def estatisticas(lista):
>        return min(lista), max(lista), sum(lista) / len(lista)
>
>    menor, maior, media = estatisticas([4, 9, 1, 7])
>    ```
> 4. ```python
>    nome, idade, *resto = dados
>    print(nome, idade, resto)    # Ada 28 ['Londres', 'Matemática']
>    ```
> 5. ```python
>    lugares = {(0, 0): "Origem", (3, 4): "Escola"}
>    print(lugares[(3, 4)])
>    ```
> 6. Funciona e imprime `([1, 9], [2])`: a tupla é imutável, mas as listas dentro dela não.
> 7. ```python
>    from collections import namedtuple
>    Produto = namedtuple("Produto", ["nome", "preco"])
>    itens = [Produto("Café", 12.5), Produto("Pão", 1.5), Produto("Leite", 5)]
>    itens.sort(key=lambda p: p.preco)
>    ```

---

⬅️ [[02 - Controle de Fluxo e Estruturas de Dados/03 - Listas|Listas]] | ➡️ [[02 - Controle de Fluxo e Estruturas de Dados/05 - Sets|Sets]]

#python #basico #tuplas #estruturas-de-dados #unpacking #namedtuple
