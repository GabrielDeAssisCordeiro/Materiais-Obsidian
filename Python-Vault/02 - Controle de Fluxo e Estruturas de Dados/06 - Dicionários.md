---
titulo: "Dicionários (dict)"
tags: [python, basico, estruturas-de-dados, dicionarios]
nivel: iniciante
criado: 2026-10-05
modulo: "02 - Controle de Fluxo e Estruturas de Dados"
---

# 📖 Dicionários (`dict`)

Um **dicionário** guarda pares **chave → valor**. Em vez de acessar por posição (como em listas), você acessa por **chave**.

> [!example] Analogia
> Uma agenda de contatos: você procura pelo **nome** (chave) e encontra o **telefone** (valor). Não importa em que página está.

| Característica | Dict |
|----------------|------|
| Ordenado | ✅ (mantém a ordem de inserção desde o Python 3.7) |
| Mutável | ✅ |
| Chaves | **Únicas** e **hasheáveis** (`str`, `int`, `tuple`...) |
| Valores | Qualquer tipo, podem repetir |
| Busca por chave | O(1) (muito rápida) |
| Sintaxe | `{"chave": valor}` |

---

## 1. Criando dicionários

```python
vazio = {}
pessoa = {"nome": "Ada", "idade": 28, "cidade": "Londres"}

# Com dict()
p2 = dict(nome="Ada", idade=28)
p3 = dict([("a", 1), ("b", 2)])
p4 = dict(zip(["x", "y"], [10, 20]))      # {'x': 10, 'y': 20}

# Chaves com valor inicial igual
contagem = dict.fromkeys(["a", "b", "c"], 0)    # {'a': 0, 'b': 0, 'c': 0}
```

> [!warning] Chaves precisam ser hasheáveis
> ```python
> {[1, 2]: "x"}         # ❌ TypeError: unhashable type: 'list'
> {(1, 2): "x"}         # ✅ tupla funciona
> ```

> [!warning] Chaves duplicadas: a última vence
> ```python
> d = {"a": 1, "a": 2}
> print(d)    # {'a': 2}
> ```

---

## 2. Acessando valores

```python
pessoa = {"nome": "Ada", "idade": 28}

print(pessoa["nome"])        # 'Ada'
print(pessoa.get("idade"))   # 28
print(pessoa.get("email"))   # None      (sem erro)
print(pessoa.get("email", "sem e-mail"))   # valor padrão
```

> [!warning] `KeyError`
> ```python
> # ❌ Quebra se a chave não existir
> print(pessoa["email"])       # KeyError: 'email'
>
> # ✅ Opções seguras
> print(pessoa.get("email"))
> if "email" in pessoa:
>     print(pessoa["email"])
> ```

> [!tip] `in` procura nas **chaves**
> ```python
> print("nome" in pessoa)      # True
> print("Ada" in pessoa)       # False  (é valor, não chave)
> print("Ada" in pessoa.values())   # True
> ```

---

## 3. Adicionando, alterando e removendo

```python
d = {"a": 1}

d["b"] = 2          # adiciona
d["a"] = 10         # altera
d.update({"c": 3, "b": 20})     # várias de uma vez
```

| Método | O que faz |
|--------|-----------|
| `d[k] = v` | Adiciona ou altera |
| `d.update(outro)` | Mescla outro dict (sobrescreve chaves iguais) |
| `d.setdefault(k, v)` | Devolve `d[k]`; se não existir, cria com `v` |
| `d.pop(k)` | Remove e devolve o valor (`KeyError` se não existir) |
| `d.pop(k, padrão)` | Idem, sem erro |
| `d.popitem()` | Remove e devolve o **último** par inserido |
| `del d[k]` | Remove a chave |
| `d.clear()` | Esvazia |

```python
d = {"a": 1, "b": 2, "c": 3}
valor = d.pop("b")          # 2
del d["a"]
d.setdefault("z", 0)        # cria 'z': 0
d.setdefault("z", 99)       # já existe: não altera
```

### Mesclando dicionários (Python 3.9+)
```python
a = {"x": 1, "y": 2}
b = {"y": 20, "z": 30}

print(a | b)     # {'x': 1, 'y': 20, 'z': 30}   (nova, b vence)
a |= b           # atualiza a in-place

# Desempacotamento (qualquer versão 3.5+)
print({**a, **b})
```

---

## 4. Percorrendo dicionários

```python
preco = {"café": 5.0, "pão": 1.5, "leite": 4.2}

for chave in preco:                  # chaves (padrão)
    print(chave)

for chave in preco.keys():           # igual ao anterior, explícito
    ...

for valor in preco.values():
    print(valor)

for produto, valor in preco.items(): # pares  ← o mais usado
    print(f"{produto}: R$ {valor:.2f}")
```

`keys()`, `values()` e `items()` devolvem **visões** (*views*) que refletem mudanças no dicionário. Use `list(d.keys())` se precisar de uma lista.

> [!warning] Não altere o tamanho do dict enquanto percorre
> ```python
> d = {"a": 1, "b": 2, "c": 3}
>
> # ❌ RuntimeError: dictionary changed size during iteration
> for k in d:
>     if d[k] == 2:
>         del d[k]
>
> # ✅ Itere sobre uma cópia das chaves
> for k in list(d):
>     if d[k] == 2:
>         del d[k]
>
> # ✅ Ou construa um novo
> d = {k: v for k, v in d.items() if v != 2}
> ```

### Ordenando
```python
for k, v in sorted(preco.items()):                     # por chave
    print(k, v)

for k, v in sorted(preco.items(), key=lambda par: par[1], reverse=True):   # por valor
    print(k, v)

mais_caro = max(preco, key=preco.get)     # chave com maior valor
```

---

## 5. Dicionários aninhados

```python
alunos = {
    "ana": {"idade": 20, "notas": [8, 9, 7]},
    "bruno": {"idade": 22, "notas": [6, 7, 5]},
}

print(alunos["ana"]["notas"][0])      # 8
alunos["ana"]["email"] = "ana@x.com"

for nome, dados in alunos.items():
    media = sum(dados["notas"]) / len(dados["notas"])
    print(f"{nome.title()}: média {media:.1f}")
```

Acesso seguro em estruturas profundas:
```python
email = alunos.get("bruno", {}).get("email", "não informado")
```

> [!note] JSON
> Dicionários aninhados casam perfeitamente com **JSON**. Veja [[05 - Tratamento de Erros e Arquivos/03 - Arquivos Texto CSV e JSON|Arquivos: texto, CSV e JSON]].

---

## 6. Padrões clássicos

### Contagem de frequência
```python
texto = "banana"
contagem = {}

for letra in texto:
    contagem[letra] = contagem.get(letra, 0) + 1

print(contagem)    # {'b': 1, 'a': 3, 'n': 2}
```

Versões mais enxutas, com a biblioteca padrão:
```python
from collections import Counter, defaultdict

print(Counter("banana"))                   # Counter({'a': 3, 'n': 2, 'b': 1})
print(Counter("banana").most_common(1))    # [('a', 3)]

# defaultdict: valor padrão automático
grupos = defaultdict(list)
for palavra in ["ola", "oi", "bom", "bye"]:
    grupos[palavra[0]].append(palavra)
print(dict(grupos))    # {'o': ['ola', 'oi'], 'b': ['bom', 'bye']}
```
Detalhes em [[06 - Módulos da Biblioteca Padrão Essenciais/03 - collections itertools e functools|collections]].

### Agrupar itens
```python
alunos = [("Ana", "A"), ("Bruno", "B"), ("Carla", "A")]
por_turma = {}
for nome, turma in alunos:
    por_turma.setdefault(turma, []).append(nome)
# {'A': ['Ana', 'Carla'], 'B': ['Bruno']}
```

### Inverter chaves e valores
```python
original = {"a": 1, "b": 2}
invertido = {v: k for k, v in original.items()}   # {1: 'a', 2: 'b'}
```
(Só funciona bem se os valores forem únicos e hasheáveis.)

### Substituindo longos `if/elif` por um dicionário
```python
# ❌
if op == "+": r = a + b
elif op == "-": r = a - b
elif op == "*": r = a * b

# ✅ Tabela de despacho
import operator
operacoes = {"+": operator.add, "-": operator.sub, "*": operator.mul}
r = operacoes[op](a, b)
```

---

## 7. Cópias (a mesma lição das listas)

```python
a = {"x": [1, 2]}
b = a.copy()          # cópia rasa
b["x"].append(3)
print(a)              # {'x': [1, 2, 3]}  😱  lista interna compartilhada

import copy
c = copy.deepcopy(a)  # cópia profunda
```
Revise em [[02 - Controle de Fluxo e Estruturas de Dados/03 - Listas|Cópias de listas]].

---

## 8. Comprehension de dicionários

```python
quadrados = {n: n ** 2 for n in range(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

caros = {k: v for k, v in preco.items() if v > 4}
```
Veja [[02 - Controle de Fluxo e Estruturas de Dados/07 - Comprehensions|Comprehensions]].

---

## 9. Resumo dos métodos

| Método | Descrição |
|--------|-----------|
| `get(k, padrão=None)` | Valor ou padrão |
| `keys()` / `values()` / `items()` | Visões de chaves / valores / pares |
| `update(outro)` | Mescla |
| `setdefault(k, v)` | Obtém ou cria |
| `pop(k[, padrão])` | Remove e devolve |
| `popitem()` | Remove o último par |
| `clear()` | Esvazia |
| `copy()` | Cópia rasa |
| `fromkeys(iter, v)` | Cria com mesmo valor inicial |
| `\|` e `\|=` | Mesclar (3.9+) |

---

## 10. Exemplo: agenda de contatos

```python
agenda = {}

while True:
    print("\n1-Adicionar  2-Buscar  3-Listar  4-Sair")
    opcao = input("Opção: ").strip()

    match opcao:
        case "1":
            nome = input("Nome: ").strip().title()
            agenda[nome] = input("Telefone: ").strip()
        case "2":
            nome = input("Buscar: ").strip().title()
            print(agenda.get(nome, "Contato não encontrado"))
        case "3":
            for nome, tel in sorted(agenda.items()):
                print(f"{nome:<15} {tel}")
        case "4":
            break
        case _:
            print("Opção inválida")
```

---

> [!question] Exercícios
> 1. Crie um dicionário com nome, idade e cidade de uma pessoa. Altere a idade e adicione o campo `email`.
> 2. Dado `preco = {"café": 5, "pão": 1.5}`, imprima `café custa R$ 5.00` para cada item.
> 3. Conte quantas vezes cada palavra aparece em uma frase lida.
> 4. Dadas duas listas `chaves` e `valores`, crie um dicionário (use `zip`).
> 5. Dado `notas = {"Ana": 8, "Bruno": 6, "Carla": 9}`, descubra o aluno com a maior nota e a média da turma.
> 6. Explique a diferença entre `d["x"]` e `d.get("x")`.
> 7. Agrupe uma lista de palavras pelo seu tamanho: `{3: [...], 4: [...]}`.
> 8. Mescle `{"a": 1, "b": 2}` com `{"b": 3, "c": 4}` de duas formas.

> [!success]- Soluções
> 1. ```python
>    p = {"nome": "Ada", "idade": 28, "cidade": "Londres"}
>    p["idade"] = 29
>    p["email"] = "ada@x.com"
>    ```
> 2. ```python
>    for produto, valor in preco.items():
>        print(f"{produto} custa R$ {valor:.2f}")
>    ```
> 3. ```python
>    contagem = {}
>    for palavra in input("Frase: ").lower().split():
>        contagem[palavra] = contagem.get(palavra, 0) + 1
>    print(contagem)
>    ```
> 4. `dict(zip(chaves, valores))`
> 5. ```python
>    melhor = max(notas, key=notas.get)
>    media = sum(notas.values()) / len(notas)
>    print(melhor, media)
>    ```
> 6. `d["x"]` levanta `KeyError` se a chave não existir; `d.get("x")` devolve `None` (ou o padrão informado).
> 7. ```python
>    grupos = {}
>    for p in palavras:
>        grupos.setdefault(len(p), []).append(p)
>    ```
> 8. ```python
>    a = {"a": 1, "b": 2}; b = {"b": 3, "c": 4}
>    print(a | b)
>    print({**a, **b})
>    ```

---

⬅️ [[02 - Controle de Fluxo e Estruturas de Dados/05 - Sets|Sets]] | ➡️ [[02 - Controle de Fluxo e Estruturas de Dados/07 - Comprehensions|Comprehensions]]

#python #basico #dicionarios #dict #estruturas-de-dados #hash
