---
titulo: "Comentários e Boas Práticas"
tags: [python, basico, comentarios, boas-praticas]
nivel: iniciante
criado: 2026-10-05
modulo: "01 - Fundamentos"
---

# 💬 Comentários e Boas Práticas

> [!note] Princípio fundamental
> Código é **lido muito mais vezes do que é escrito**. Escreva pensando em quem vai ler (inclusive você daqui a 6 meses).

---

## 1. Comentários

### De uma linha: `#`
```python
# Calcula o preço final com desconto
preco_final = preco * 0.9    # 10% de desconto
```

### De várias linhas
Python **não tem** comentário de bloco. Use várias linhas com `#`:
```python
# Este bloco calcula a média ponderada
# das notas considerando os pesos
# definidos pela coordenação.
```

> [!warning] Strings de várias linhas não são comentários
> `"""texto"""` solto no código funciona *na prática* como comentário, mas é uma **string** avaliada pelo interpretador. Quando colocada logo após `def`, `class` ou no topo do arquivo, vira uma **docstring** (veja [[03 - Funções e Modularização/06 - Docstrings|Docstrings]]).

### Comentários úteis x inúteis

```python
# ❌ Ruim: repete o que o código já diz
x = x + 1   # soma 1 a x

# ❌ Ruim: comentário desatualizado e mentiroso
# Retorna o dobro
def triplo(n):
    return n * 3

# ✅ Bom: explica o PORQUÊ
# A API retorna datas em UTC; convertemos para o fuso local
data_local = converter_fuso(data_utc)

# ✅ Bom: marca pendências (padrão reconhecido por editores)
# TODO: tratar o caso de lista vazia
# FIXME: falha com datas anteriores a 1970
```

> [!tip] Regra de ouro
> **Comente o porquê, não o quê.** Se precisa comentar *o que* o código faz, talvez precise de nomes melhores.

```python
# ❌ Comentário compensando nome ruim
d = 7  # dias da semana

# ✅ Nome autoexplicativo dispensa o comentário
dias_da_semana = 7
```

---

## 2. PEP 8: o guia de estilo oficial

A **PEP 8** define como escrever código Python "pythônico" e consistente.

| Tema | Recomendação | Exemplo |
|------|--------------|---------|
| Indentação | 4 espaços | `    return x` |
| Tamanho da linha | até 79 caracteres (88 com Black) | — |
| Linhas em branco | 2 entre funções/classes de topo; 1 entre métodos | — |
| Imports | Um por linha, no topo, ordenados | `import os` |
| Espaços | Ao redor de operadores | `x = a + b` |
| Espaços (não) | Dentro de parênteses/colchetes | `lista[0]`, não `lista[ 0 ]` |
| Nomes | `snake_case`, `PascalCase`, `MAIUSCULAS` | ver abaixo |

### Espaçamento

```python
# ❌ Errado
x=5+3
lista = [ 1,2,3 ]
def soma (a,b) :
    return a+b

# ✅ Correto
x = 5 + 3
lista = [1, 2, 3]
def soma(a, b):
    return a + b
```

### Imports

```python
# ❌ Errado
import os, sys, json

# ✅ Correto (ordem: biblioteca padrão → terceiros → seus módulos)
import json
import os
import sys

import requests          # terceiros

from meu_pacote import util   # seus módulos
```

### Nomes (resumo)
```python
total_vendas = 100        # variável: snake_case
TAXA_JUROS = 0.05         # constante: MAIÚSCULAS
class ContaBancaria: ...  # classe: PascalCase
def calcular_media(): ... # função: snake_case
```
Veja mais em [[01 - Fundamentos/02 - Sintaxe Básica e Variáveis#3. Regras de nomes|Regras de nomes]].

---

## 3. Boas práticas essenciais

### 3.1 Evite "números mágicos"
```python
# ❌ O que é 0.15?
total = preco * 1.15

# ✅ Constante nomeada
TAXA_SERVICO = 0.15
total = preco * (1 + TAXA_SERVICO)
```

### 3.2 Prefira clareza a "esperteza"
```python
# ❌ Compacto demais
r = [x for x in range(100) if x % 2 == 0 if x % 3 == 0 if x > 10][:5]

# ✅ Legível (passos nomeados)
numeros = range(100)
multiplos_de_6 = [n for n in numeros if n % 6 == 0 and n > 10]
primeiros_cinco = multiplos_de_6[:5]
```

### 3.3 Uma coisa por vez
Cada linha, e depois cada função, deve fazer **uma** coisa bem feita (ver [[03 - Funções e Modularização/01 - Definindo Funções|Funções]]).

### 3.4 Evite repetição (DRY: *Don't Repeat Yourself*)
```python
# ❌ Repetido
print("=" * 30)
print("RELATÓRIO")
print("=" * 30)

# ✅ Reaproveitado
SEPARADOR = "=" * 30
print(SEPARADOR)
print("RELATÓRIO")
print(SEPARADOR)
```

### 3.5 Use `if __name__ == "__main__"`
Permite que o arquivo seja **importado** sem executar tudo (detalhes em [[03 - Funções e Modularização/04 - Módulos e Packages|Módulos e Packages]]):
```python
def main():
    print("Programa rodando")

if __name__ == "__main__":
    main()
```

### 3.6 Booleans: seja direto
```python
# ❌ Redundante
if ativo == True:
    ...
if len(lista) == 0:
    ...

# ✅ Pythônico
if ativo:
    ...
if not lista:
    ...
```

---

## 4. O Zen do Python

Abra o REPL e digite:
```python
>>> import this
```
Algumas linhas (parafraseadas):
- **Bonito é melhor que feio.**
- **Explícito é melhor que implícito.**
- **Simples é melhor que complexo.**
- **Legibilidade conta.**
- **Erros nunca devem passar silenciosamente.**

---

## 5. Ferramentas que ajudam

| Ferramenta | Função |
|------------|--------|
| **Ruff** | Linter ultrarrápido (aponta erros e problemas de estilo) |
| **Black** / `ruff format` | Formata o código automaticamente |
| **mypy** / **pyright** | Verificação de tipos (veja [[07 - Programação Funcional e Intermediário/06 - Type Hints e typing\|Type Hints]]) |
| **isort** (ou Ruff) | Ordena imports |

```bash
pip install ruff
ruff check .        # verifica
ruff format .       # formata
```

> [!tip] Automatize no VS Code
> Ative *Format on Save* nas configurações e instale a extensão do Ruff. O editor corrige o estilo toda vez que você salva.

---

## 6. Hábitos de quem aprende rápido

> [!tip] Checklist de estudo
> - ✅ Digite o código em vez de copiar e colar.
> - ✅ Use o **REPL** para testar ideias pequenas.
> - ✅ Use o **debugger** para entender fluxos ([[01 - Fundamentos/01 - Instalação e Ambiente#5. Primeiro contato com o debugger|veja como]]).
> - ✅ Leia as **mensagens de erro** (a última linha diz o tipo do erro; as de cima, onde ocorreu).
> - ✅ Quebre problemas grandes em passos pequenos.
> - ✅ Faça mini-projetos o quanto antes.

### Lendo um *traceback*
```text
Traceback (most recent call last):
  File "app.py", line 3, in <module>
    print(10 / 0)
ZeroDivisionError: division by zero
```
Leia **de baixo para cima**: o tipo do erro (`ZeroDivisionError`), a descrição, e em qual linha (`line 3`) aconteceu.

---

> [!question] Exercício
> Melhore o código abaixo aplicando nomes claros, PEP 8, constante nomeada e comentário apenas onde faz sentido:
> ```python
> a=input("v:")
> b=float(a)*0.85
> print("t:",b)
> ```

> [!success]- Solução sugerida
> ```python
> DESCONTO = 0.15
>
> valor_original = float(input("Valor do produto: "))
> valor_final = valor_original * (1 - DESCONTO)
> print(f"Total com desconto: R$ {valor_final:.2f}")
> ```
> Melhorias: nomes descritivos, `float()` direto, constante no lugar do "número mágico" (`0.85` → `1 - DESCONTO`), mensagens claras, f-string e espaçamento correto.

---

⬅️ [[01 - Fundamentos/05 - Entrada e Saída|Entrada e Saída]] | ➡️ [[01 - Fundamentos/07 - Exercícios de Fundamentos|Exercícios de Fundamentos]]

#python #basico #comentarios #pep8 #boas-praticas #clean-code
