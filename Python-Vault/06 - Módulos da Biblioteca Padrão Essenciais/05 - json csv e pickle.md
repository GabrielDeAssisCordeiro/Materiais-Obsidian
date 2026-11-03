---
titulo: "json, csv e pickle"
tags: [python, intermediario, stdlib, json, csv]
nivel: intermediario
criado: 2026-10-05
modulo: "06 - Módulos da Biblioteca Padrão Essenciais"
---

# 💾 `json`, `csv` e `pickle`

Na nota [[05 - Tratamento de Erros e Arquivos/03 - Arquivos Texto CSV e JSON|Arquivos: texto, CSV e JSON]] você aprendeu o básico de leitura e escrita. Aqui vamos **aprofundar**: serialização de objetos personalizados, dialetos de CSV, e o `pickle` (com seus perigos).

> [!note] Serialização
> **Serializar** é converter um objeto em memória em uma sequência de bytes/texto (para **gravar** ou **enviar**). **Desserializar** é o caminho inverso.

| Formato | Legível por humanos | Interoperável | Tipos suportados | Seguro com dados externos |
|---------|:-------------------:|:-------------:|------------------|:-------------------------:|
| **JSON** | ✅ | ✅ (qualquer linguagem) | dict, list, str, números, bool, None | ✅ |
| **CSV** | ✅ | ✅ (planilhas) | só texto tabular | ✅ |
| **pickle** | ❌ (binário) | ❌ (só Python) | quase **qualquer** objeto | ❌ **PERIGOSO** |
| **TOML** | ✅ | ✅ | configurações | ✅ |

---

## 🧾 JSON avançado

## 1. Revisão rápida

```python
import json

obj = {"nome": "Ada", "notas": [9.5, 10], "ativo": True, "extra": None}

texto = json.dumps(obj, ensure_ascii=False, indent=2)    # Python → str
de_volta = json.loads(texto)                              # str → Python

with open("dados.json", "w", encoding="utf-8") as f:
    json.dump(obj, f, ensure_ascii=False, indent=2)       # → arquivo
with open("dados.json", encoding="utf-8") as f:
    obj = json.load(f)                                    # ← arquivo
```

Opções úteis do `dumps`/`dump`:

| Opção | Efeito |
|-------|--------|
| `indent=2` | Formatação legível |
| `ensure_ascii=False` | Mantém acentos |
| `sort_keys=True` | Chaves em ordem alfabética (saída determinística) |
| `separators=(",", ":")` | JSON **compacto** (sem espaços) |
| `default=func` | Função para tipos não suportados |
| `cls=MeuEncoder` | Classe de *encoder* personalizada |

## 2. Serializando tipos personalizados

### Com `default=`
```python
from datetime import date, datetime
from decimal import Decimal
from pathlib import Path
from dataclasses import dataclass, asdict, is_dataclass
import json

@dataclass
class Pedido:
    id: int
    criado_em: datetime
    total: Decimal

def padrao(o):
    if isinstance(o, (datetime, date)):
        return o.isoformat()
    if isinstance(o, Decimal):
        return str(o)             # string preserva a precisão
    if isinstance(o, Path):
        return str(o)
    if isinstance(o, set):
        return sorted(o)
    if is_dataclass(o):
        return asdict(o)
    raise TypeError(f"Tipo não serializável: {type(o).__name__}")

pedido = Pedido(1, datetime(2026, 10, 5, 14, 30), Decimal("19.90"))
print(json.dumps(pedido, default=padrao, ensure_ascii=False))
# {"id": 1, "criado_em": "2026-10-05T14:30:00", "total": "19.90"}
```

### Com uma classe `JSONEncoder`
```python
class MeuEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, (datetime, date)):
            return o.isoformat()
        return super().default(o)          # deixa o erro padrão para outros tipos

json.dumps({"quando": datetime.now()}, cls=MeuEncoder)
```

## 3. Desserializando tipos personalizados: `object_hook`

JSON não tem datas: elas viram `str`. Para reconstruir objetos, use `object_hook` (chamado para **cada** dict decodificado):

```python
def decodificar(d):
    for chave, valor in d.items():
        if isinstance(valor, str) and chave.endswith("_em"):
            try:
                d[chave] = datetime.fromisoformat(valor)
            except ValueError:
                pass
    return d

dados = json.loads('{"id": 1, "criado_em": "2026-10-05T14:30:00"}', object_hook=decodificar)
print(type(dados["criado_em"]))        # <class 'datetime.datetime'>
```

Números decimais sem perder precisão:
```python
json.loads('{"preco": 19.90}', parse_float=Decimal)     # {'preco': Decimal('19.90')}
```

## 4. Validação e erros

```python
try:
    json.loads("{'a': 1}")                 # aspas simples: inválido
except json.JSONDecodeError as e:
    print(e.msg, "linha", e.lineno, "coluna", e.colno)
```

> [!warning] O `json` aceita coisas "estranhas"
> - `NaN`, `Infinity` (use `allow_nan=False` ao gravar para garantir JSON estrito)
> - Chaves duplicadas (a última vence)
> - Não valida **estrutura**: para garantir os campos esperados, use *Pydantic*, `jsonschema` ou valide manualmente.

> [!tip] Validação manual simples
> ```python
> def validar_usuario(d):
>     obrigatorios = {"nome": str, "idade": int}
>     for campo, tipo in obrigatorios.items():
>         if campo not in d:
>             raise ValueError(f"Falta o campo {campo!r}")
>         if not isinstance(d[campo], tipo):
>             raise TypeError(f"{campo!r} deve ser {tipo.__name__}")
>     return d
> ```

## 5. JSON Lines, streams e arquivos grandes

`json.load` carrega **tudo** na memória. Para volumes grandes, use **JSON Lines** (`.jsonl`): um JSON por linha.

```python
def gravar_jsonl(caminho, registros):
    with open(caminho, "w", encoding="utf-8") as f:
        for r in registros:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

def ler_jsonl(caminho):                          # gerador: memória constante
    with open(caminho, encoding="utf-8") as f:
        for linha in f:
            if linha.strip():
                yield json.loads(linha)
```

## 6. Linha de comando: `python -m json.tool`
```bash
echo '{"a":1,"b":[1,2]}' | python -m json.tool
python -m json.tool dados.json --indent 2 --no-ensure-ascii
```

---

## 📊 CSV avançado

## 7. Revisão e dialetos

```python
import csv

with open("dados.csv", newline="", encoding="utf-8") as f:
    for linha in csv.DictReader(f):
        ...
```

### Dialetos (formatos de CSV)

| Parâmetro | Significado | Exemplo |
|-----------|-------------|---------|
| `delimiter` | Separador de campos | `;` (Excel brasileiro), `\t` (TSV) |
| `quotechar` | Caractere de aspas | `"` |
| `quoting` | Quando usar aspas | `csv.QUOTE_MINIMAL`, `QUOTE_ALL`, `QUOTE_NONNUMERIC` |
| `lineterminator` | Fim de linha ao escrever | `"\n"` |
| `skipinitialspace` | Ignora espaço após o delimitador | `True` |

```python
# CSV "brasileiro": separador ; e decimal com vírgula
with open("planilha.csv", newline="", encoding="utf-8-sig") as f:
    for linha in csv.DictReader(f, delimiter=";"):
        preco = float(linha["preco"].replace(".", "").replace(",", "."))   # '1.234,56'
```

### Descobrindo o formato com `Sniffer`
```python
with open("misterio.csv", newline="", encoding="utf-8") as f:
    amostra = f.read(2048)
    f.seek(0)
    dialeto = csv.Sniffer().sniff(amostra, delimiters=",;\t|")
    tem_cabecalho = csv.Sniffer().has_header(amostra)
    leitor = csv.reader(f, dialeto)
```

## 8. Lidando com dados reais "sujos"

```python
from collections import defaultdict

erros = []
totais = defaultdict(float)

with open("vendas.csv", newline="", encoding="utf-8-sig") as f:
    leitor = csv.DictReader(f, delimiter=";")
    for numero, linha in enumerate(leitor, start=2):        # linha 1 = cabeçalho
        try:
            valor = float(linha["valor"].replace(".", "").replace(",", "."))
            totais[linha["vendedor"].strip().title()] += valor
        except (KeyError, ValueError, AttributeError) as e:
            erros.append((numero, repr(e), linha))

print(f"{len(erros)} linha(s) com problema")
```

Colunas **extras** ou **faltando**:
```python
csv.DictReader(f, restkey="extras", restval="")
```

## 9. Escrevendo CSV compatível com o Excel
```python
with open("saida.csv", "w", newline="", encoding="utf-8-sig") as f:   # BOM p/ acentos no Excel
    w = csv.DictWriter(f, fieldnames=["produto", "preco"], delimiter=";")
    w.writeheader()
    w.writerow({"produto": "Café", "preco": "12,50"})
```

> [!tip] Muitos dados ou análises? Pandas
> ```python
> import pandas as pd
> df = pd.read_csv("vendas.csv", sep=";", decimal=",", thousands=".", encoding="utf-8-sig")
> print(df.groupby("vendedor")["valor"].sum())
> ```
> Para ler/escrever e processar, o `csv` basta; para **análise** (filtros, agrupamentos, estatísticas), o pandas é a ferramenta certa ([[09 - Projetos Práticos/Projeto 03 - Análise de Dados com CSV|Projeto 03]]).

---

## 🥒 `pickle`: serializando objetos Python

O `pickle` converte **quase qualquer objeto Python** em bytes e vice-versa.

## 10. Uso básico

```python
import pickle

dados = {"lista": [1, 2, 3], "conjunto": {1, 2}, "tupla": (1, "a"), "chave": b"bytes"}

with open("dados.pkl", "wb") as f:               # sempre modo BINÁRIO
    pickle.dump(dados, f)

with open("dados.pkl", "rb") as f:
    recuperado = pickle.load(f)

print(recuperado == dados)      # True

# Em memória (bytes)
blob = pickle.dumps(dados)
de_novo = pickle.loads(blob)
```

Funciona com **objetos de classes suas** (se a classe estiver importável ao carregar):

```python
class Jogador:
    def __init__(self, nome, pontos):
        self.nome, self.pontos = nome, pontos

with open("jogador.pkl", "wb") as f:
    pickle.dump(Jogador("Ada", 100), f)
```

## 11. ⚠️ Segurança: **nunca** carregue pickle não confiável

> [!warning] `pickle.load` pode **executar código arbitrário**
> Um arquivo `.pkl` malicioso pode rodar comandos no seu computador **ao ser carregado**:
> ```python
> import pickle, os
>
> class Malicioso:
>     def __reduce__(self):
>         return (os.system, ("echo 💥 código executado!",))
>
> payload = pickle.dumps(Malicioso())
> pickle.loads(payload)      # ← executa o comando!
> ```
> **Regras:**
> - ❌ Nunca use `pickle.load` em dados vindos da internet, de usuários ou de fontes desconhecidas.
> - ✅ Para trocar dados com terceiros, use **JSON**, CSV, Protobuf, etc.
> - ✅ Use pickle só para dados **que você mesmo gerou** e guarda em local confiável (cache local, resultados intermediários).

## 12. Limitações e compatibilidade

- Funções **lambda**, geradores, conexões de rede, arquivos abertos e *locks* **não** são serializáveis.
- Só funciona entre programas **Python** (e a versão do pickle/classes pode quebrar compatibilidade entre versões).
- O arquivo depende do **código das classes**: se você renomear/mover uma classe, os pickles antigos deixam de carregar.
- Escolha o protocolo: `pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)`.

### Controlando o que é salvo: `__getstate__` / `__setstate__`
```python
class Conexao:
    def __init__(self, url):
        self.url = url
        self._socket = abrir_socket(url)         # não serializável

    def __getstate__(self):
        estado = self.__dict__.copy()
        del estado["_socket"]                    # não salva o socket
        return estado

    def __setstate__(self, estado):
        self.__dict__.update(estado)
        self._socket = abrir_socket(self.url)    # recria ao carregar
```

## 13. Alternativas ao pickle

| Alternativa | Quando usar |
|-------------|-------------|
| `json` | Dados simples, interoperabilidade, **segurança** |
| `shelve` | "Dicionário persistente" em disco (usa pickle por baixo) |
| `sqlite3` | Dados estruturados, consultas ([[09 - Projetos Práticos/Projeto 07 - Login com SQLite\|Projeto 07]]) |
| `marshal` | Interno do Python (bytecode); **não** use para dados |
| `dataclasses.asdict` + JSON | Objetos de dados |
| `msgpack`, `protobuf`, `parquet` | Desempenho/esquema/grandes volumes (terceiros) |
| `joblib` | Objetos científicos grandes (ex.: modelos de ML) |

```python
import shelve

with shelve.open("cache_db") as db:
    db["usuarios"] = ["ada", "alan"]
    db["config"] = {"tema": "escuro"}

with shelve.open("cache_db") as db:
    print(db["usuarios"])
```

---

## 🧩 Bônus: configurações com `tomllib` e `configparser`

## 14. TOML (`tomllib`, Python 3.11+)

Formato de configuração legível, usado em `pyproject.toml` ([[08 - Avançado/07 - Packaging e Distribuição|Packaging]]).

`config.toml`:
```toml
titulo = "Meu App"
debug = false

[banco]
host = "localhost"
porta = 5432

[[servidores]]
nome = "alfa"
ip = "10.0.0.1"
```

```python
import tomllib

with open("config.toml", "rb") as f:         # note: modo BINÁRIO
    cfg = tomllib.load(f)

print(cfg["banco"]["porta"])                 # 5432
print(cfg["servidores"][0]["nome"])          # 'alfa'
```
> `tomllib` só **lê**. Para escrever TOML, use `tomli_w` (terceiros).

## 15. INI (`configparser`)

```ini
; config.ini
[banco]
host = localhost
porta = 5432
```
```python
import configparser

cfg = configparser.ConfigParser()
cfg.read("config.ini", encoding="utf-8")
print(cfg["banco"]["host"], cfg.getint("banco", "porta"))
```

---

## 16. Exemplo completo: repositório de dados com JSON + cache pickle

```python
import json
import pickle
from dataclasses import dataclass, asdict
from datetime import date
from pathlib import Path

@dataclass
class Tarefa:
    id: int
    titulo: str
    prazo: date
    feita: bool = False

class Repositorio:
    def __init__(self, caminho="tarefas.json"):
        self.caminho = Path(caminho)

    def salvar(self, tarefas):
        dados = [{**asdict(t), "prazo": t.prazo.isoformat()} for t in tarefas]
        self.caminho.write_text(json.dumps(dados, ensure_ascii=False, indent=2), encoding="utf-8")

    def carregar(self):
        try:
            bruto = json.loads(self.caminho.read_text(encoding="utf-8"))
        except FileNotFoundError:
            return []
        return [Tarefa(**{**d, "prazo": date.fromisoformat(d["prazo"])}) for d in bruto]

repo = Repositorio()
repo.salvar([Tarefa(1, "Estudar Python", date(2026, 10, 12)), Tarefa(2, "Praticar", date(2026, 10, 15), True)])
print(repo.carregar())
```
Fonte de verdade em **JSON** (seguro e legível); `pickle` só para caches temporários e locais.

---

> [!question] Exercícios
> 1. Serialize `{"data": date.today(), "valores": {1, 2, 3}}` para JSON usando `default=`.
> 2. Escreva `ler_jsonl(caminho)` como **gerador** e some o campo `"valor"` de um arquivo gigante.
> 3. Leia um CSV brasileiro (`;` e vírgula decimal) e produza o total por categoria.
> 4. Converta `contatos.csv` (nome;email) em JSON Lines e vice-versa.
> 5. Demonstre, num ambiente isolado, por que `pickle.load` é perigoso (use um comando inofensivo como `print`).
> 6. Salve e recarregue com pickle um objeto que contenha um atributo não serializável usando `__getstate__`/`__setstate__`.
> 7. Leia um arquivo `config.toml` e mescle com valores padrão.
> 8. Quando você escolheria JSON, CSV, pickle, SQLite ou TOML? Dê um exemplo para cada.
> 9. Carregue datas de um JSON como objetos `date` usando `object_hook`.

> [!success]- Soluções
> 1. ```python
>    import json
>    from datetime import date
>    def padrao(o):
>        if isinstance(o, date): return o.isoformat()
>        if isinstance(o, set): return sorted(o)
>        raise TypeError(type(o))
>    print(json.dumps({"data": date.today(), "valores": {1, 2, 3}}, default=padrao))
>    ```
> 2. ```python
>    import json
>    def ler_jsonl(caminho):
>        with open(caminho, encoding="utf-8") as f:
>            for linha in f:
>                if linha.strip():
>                    yield json.loads(linha)
>    total = sum(r.get("valor", 0) for r in ler_jsonl("eventos.jsonl"))
>    ```
> 3. ```python
>    import csv
>    from collections import defaultdict
>    totais = defaultdict(float)
>    with open("gastos.csv", newline="", encoding="utf-8-sig") as f:
>        for l in csv.DictReader(f, delimiter=";"):
>            totais[l["categoria"]] += float(l["valor"].replace(".", "").replace(",", "."))
>    ```
> 4. ```python
>    import csv, json
>    with open("contatos.csv", newline="", encoding="utf-8") as f, \
>         open("contatos.jsonl", "w", encoding="utf-8") as out:
>        for l in csv.DictReader(f, delimiter=";"):
>            out.write(json.dumps(l, ensure_ascii=False) + "\n")
>
>    with open("contatos.jsonl", encoding="utf-8") as f, \
>         open("volta.csv", "w", newline="", encoding="utf-8") as out:
>        linhas = [json.loads(l) for l in f]
>        w = csv.DictWriter(out, fieldnames=linhas[0].keys(), delimiter=";")
>        w.writeheader(); w.writerows(linhas)
>    ```
> 5. ```python
>    import pickle
>    class Demo:
>        def __reduce__(self):
>            return (print, ("⚠️ código executado ao carregar o pickle!",))
>    pickle.loads(pickle.dumps(Demo()))
>    ```
> 6. Veja o exemplo de `Conexao` na seção 12: remova o atributo em `__getstate__` e recrie em `__setstate__`.
> 7. ```python
>    import tomllib
>    PADRAO = {"debug": False, "porta": 8000}
>    with open("config.toml", "rb") as f:
>        cfg = {**PADRAO, **tomllib.load(f)}
>    ```
> 8. JSON: resposta de API; CSV: exportar planilha; pickle: cache local de objetos que você mesmo gerou; SQLite: dados relacionais com consultas; TOML: configuração de aplicação/projeto.
> 9. ```python
>    from datetime import date
>    def hook(d):
>        return {k: date.fromisoformat(v) if k.endswith("_data") and isinstance(v, str) else v
>                for k, v in d.items()}
>    json.loads('{"nasc_data": "1990-10-05"}', object_hook=hook)
>    ```

---

⬅️ [[06 - Módulos da Biblioteca Padrão Essenciais/04 - re Expressões Regulares|re (Expressões Regulares)]] | ➡️ [[06 - Módulos da Biblioteca Padrão Essenciais/06 - concurrent futures e threading|concurrent.futures e threading]]

#python #intermediario #stdlib #json #csv #pickle #serializacao #toml
