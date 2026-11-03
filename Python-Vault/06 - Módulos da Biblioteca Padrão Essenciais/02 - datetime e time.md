---
titulo: "datetime e time"
tags: [python, intermediario, stdlib]
nivel: intermediario
criado: 2026-10-05
modulo: "06 - Módulos da Biblioteca Padrão Essenciais"
---

# 🕒 `datetime` e `time`

Datas e horas parecem simples, mas escondem armadilhas (fusos, horário de verão, meses de tamanhos diferentes). Aqui você aprende o essencial para usar a biblioteca padrão **sem se enrolar**.

| Módulo/Classe | Representa | Exemplo |
|---------------|------------|---------|
| `datetime.date` | Só a **data** | `2026-10-05` |
| `datetime.time` | Só a **hora** | `14:30:00` |
| `datetime.datetime` | **Data + hora** | `2026-10-05 14:30:00` |
| `datetime.timedelta` | **Duração** (diferença) | `3 dias, 2 horas` |
| `datetime.timezone` / `zoneinfo.ZoneInfo` | **Fusos horários** | `America/Sao_Paulo` |
| `time` | Tempo do sistema, cronometragem, `sleep` | `time.perf_counter()` |

---

## 1. Criando datas e horas

```python
from datetime import date, time, datetime, timedelta

hoje = date.today()                      # data de hoje
agora = datetime.now()                   # data e hora locais (naive)

d = date(2026, 10, 5)                    # ano, mês, dia
t = time(14, 30, 15)                     # hora, minuto, segundo
dt = datetime(2026, 10, 5, 14, 30)       # ano, mês, dia, hora, minuto

print(d, t, dt)
# 2026-10-05 14:30:15 2026-10-05 14:30:00
```

### Acessando componentes
```python
dt.year, dt.month, dt.day                # 2026 10 5
dt.hour, dt.minute, dt.second            # 14 30 0
dt.weekday()                             # 0=segunda ... 6=domingo  → 0
dt.isoweekday()                          # 1=segunda ... 7=domingo
dt.date(), dt.time()                     # separar as partes
dt.replace(hour=0, minute=0)             # nova data com campos trocados
```

---

## 2. Formatando e interpretando texto

### `strftime`: datetime → texto
```python
agora = datetime(2026, 10, 5, 14, 30, 7)
print(agora.strftime("%d/%m/%Y %H:%M:%S"))    # 05/10/2026 14:30:07
print(f"{agora:%d/%m/%Y}")                    # 05/10/2026 (f-string!)
print(agora.isoformat())                      # 2026-10-05T14:30:07
```

### `strptime`: texto → datetime
```python
dt = datetime.strptime("05/10/2026 14:30", "%d/%m/%Y %H:%M")
d = datetime.strptime("2026-10-05", "%Y-%m-%d").date()
```

### ISO 8601 (o formato recomendado para trocar dados)
```python
datetime.fromisoformat("2026-10-05T14:30:07")
date.fromisoformat("2026-10-05")
```

### Códigos de formato mais usados

| Código | Significado | Exemplo |
|--------|-------------|---------|
| `%Y` | Ano com 4 dígitos | `2026` |
| `%y` | Ano com 2 dígitos | `26` |
| `%m` | Mês (01–12) | `10` |
| `%d` | Dia (01–31) | `05` |
| `%H` | Hora 24h (00–23) | `14` |
| `%I` + `%p` | Hora 12h + AM/PM | `02 PM` |
| `%M` | Minuto | `30` |
| `%S` | Segundo | `07` |
| `%f` | Microssegundos | `000123` |
| `%A` / `%a` | Dia da semana (completo/abrev.) | `Monday` / `Mon` |
| `%B` / `%b` | Mês (completo/abrev.) | `October` / `Oct` |
| `%j` | Dia do ano | `278` |
| `%U` / `%W` | Semana do ano | `40` |
| `%z` / `%Z` | Offset / nome do fuso | `-0300` / `-03` |

> [!warning] Nomes em português
> `%A` e `%B` seguem o **idioma do sistema** (inglês por padrão). Para português:
> ```python
> import locale
> locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")   # precisa estar instalado no SO
> ```
> Alternativa portátil: use um dicionário/lista dos nomes (ou a biblioteca *Babel*).
> ```python
> DIAS = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]
> print(DIAS[agora.weekday()])
> ```

---

## 3. Aritmética com `timedelta`

```python
from datetime import datetime, timedelta

agora = datetime(2026, 10, 5, 12, 0)

amanha = agora + timedelta(days=1)
semana_passada = agora - timedelta(weeks=1)
em_90_min = agora + timedelta(minutes=90)

# Diferença entre datas → timedelta
natal = datetime(2026, 12, 25)
falta = natal - agora
print(falta)                     # 81 days, 12:00:00
print(falta.days)                # 81
print(falta.total_seconds())     # 7041600.0 (inclui dias e horas)
```

| Atributo/método | Cuidado |
|-----------------|---------|
| `td.days` | Só a parte **de dias** |
| `td.seconds` | Segundos **restantes** do dia (0–86399), **não** o total |
| `td.total_seconds()` | ✅ O total em segundos |

> [!warning] `timedelta` não tem "meses" nem "anos"
> Meses têm tamanhos diferentes. Para somar meses, use `dateutil.relativedelta` (terceiros) ou calcule manualmente:
> ```python
> import calendar
> from datetime import date
>
> def somar_meses(d, n):
>     mes = d.month - 1 + n
>     ano = d.year + mes // 12
>     mes = mes % 12 + 1
>     dia = min(d.day, calendar.monthrange(ano, mes)[1])   # 31/01 + 1 mês → 28/02
>     return date(ano, mes, dia)
>
> print(somar_meses(date(2026, 1, 31), 1))    # 2026-02-28
> ```

### Comparações e ordenação
```python
d1, d2 = date(2026, 1, 1), date(2026, 6, 1)
print(d1 < d2)                       # True
datas = sorted([d2, d1])
print(max(d1, d2))
```

### Calculando idade
```python
def idade(nascimento, hoje=None):
    hoje = hoje or date.today()
    return hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))

print(idade(date(1990, 10, 6), date(2026, 10, 5)))    # 35 (ainda não fez aniversário)
```

---

## 4. Fusos horários: *naive* vs *aware*

| Tipo | Tem fuso? | Uso |
|------|-----------|-----|
| **Naive** (ingênuo) | ❌ | Horário "de parede" local; ambíguo |
| **Aware** (consciente) | ✅ | Instante **preciso** no tempo |

```python
from datetime import datetime, timezone
from zoneinfo import ZoneInfo           # biblioteca padrão desde 3.9

sp = ZoneInfo("America/Sao_Paulo")
utc = timezone.utc

agora_utc = datetime.now(utc)                    # ✅ instante atual em UTC (aware)
agora_sp = datetime.now(sp)                      # ✅ hora de Brasília
print(agora_sp.tzinfo, agora_sp.utcoffset())     # America/Sao_Paulo -1 day, 21:00:00 (-03:00)

# Converter entre fusos
tokyo = agora_utc.astimezone(ZoneInfo("Asia/Tokyo"))

# Tornar aware um naive (quando você SABE o fuso)
naive = datetime(2026, 10, 5, 14, 0)
aware = naive.replace(tzinfo=sp)
```

> [!warning] Armadilhas de fuso
> ```python
> datetime.utcnow()           # ❌ obsoleto (3.12): devolve NAIVE em UTC, enganoso
> datetime.now(timezone.utc)  # ✅
>
> naive - aware               # ❌ TypeError: can't subtract offset-naive and offset-aware
> ```
> **Nunca misture** naive e aware.

> [!tip] Regra de ouro: **UTC por dentro, local por fora**
> 1. Armazene e calcule sempre em **UTC** (aware).
> 2. Converta para o fuso do usuário **só ao exibir**.
> 3. Em JSON/banco, use ISO 8601 com offset: `2026-10-05T17:30:00+00:00`.

> [!note] Horário de verão
> Fusos como `America/New_York` têm DST. Ao somar `timedelta(days=1)` em datetimes aware, o relógio de parede é mantido; para somar **24 horas reais**, converta para UTC, some e converta de volta.

> [!note] Windows e `zoneinfo`
> Se aparecer `ZoneInfoNotFoundError` no Windows: `python -m pip install tzdata`.

---

## 5. O módulo `time`

```python
import time

time.time()              # segundos desde 1970-01-01 UTC (epoch) → float
time.sleep(1.5)          # pausa o programa (bloqueia a thread)
time.strftime("%H:%M:%S")                      # hora atual formatada
time.localtime()         # struct_time local
```

### Cronometrando código: `perf_counter`
```python
inicio = time.perf_counter()
sum(range(10_000_000))
print(f"{time.perf_counter() - inicio:.3f}s")
```

| Função | Quando usar |
|--------|-------------|
| `time.perf_counter()` | ✅ Medir **durações** (alta resolução, monotônico) |
| `time.monotonic()` | Timeouts/intervalos (nunca volta no tempo) |
| `time.time()` | **Timestamp** (data/hora real); pode saltar se o relógio for ajustado |
| `time.process_time()` | Tempo de **CPU** do processo |

> [!tip] Para benchmarks reais, use `timeit`
> ```python
> import timeit
> print(timeit.timeit("sum(range(1000))", number=10_000))
> ```
> Veja [[08 - Avançado/05 - Performance e Profiling|Performance e Profiling]].

### Timestamps ↔ datetime
```python
from datetime import datetime, timezone

ts = time.time()
dt = datetime.fromtimestamp(ts, tz=timezone.utc)   # timestamp → datetime (aware)
back = dt.timestamp()                              # datetime → timestamp
```

---

## 6. `calendar`: calendários e utilidades

```python
import calendar

print(calendar.month(2026, 10))          # calendário do mês em texto
calendar.isleap(2028)                    # True
calendar.monthrange(2026, 2)             # (6, 28): (dia da semana do dia 1, nº de dias)
calendar.weekday(2026, 10, 5)            # 0 (segunda)
```

---

## 7. Receitas úteis

### Primeiro e último dia do mês
```python
import calendar
from datetime import date

def limites_mes(ano, mes):
    return date(ano, mes, 1), date(ano, mes, calendar.monthrange(ano, mes)[1])
```

### Dias úteis entre duas datas
```python
from datetime import date, timedelta

def dias_uteis(inicio, fim):
    total, d = 0, inicio
    while d <= fim:
        if d.weekday() < 5:
            total += 1
        d += timedelta(days=1)
    return total
```

### Gerar um intervalo de datas
```python
def intervalo(inicio, fim):
    for n in range((fim - inicio).days + 1):
        yield inicio + timedelta(days=n)

semana = list(intervalo(date(2026, 10, 5), date(2026, 10, 11)))
```

### Texto "há X tempo"
```python
def ha_quanto_tempo(dt, agora=None):
    agora = agora or datetime.now(dt.tzinfo)
    seg = int((agora - dt).total_seconds())
    for limite, nome in ((86400, "dia"), (3600, "hora"), (60, "minuto")):
        if seg >= limite:
            n = seg // limite
            return f"há {n} {nome}{'s' if n > 1 else ''}"
    return "agora há pouco"
```

### Serializando em JSON
```python
import json
from datetime import datetime, timezone

evento = {"quando": datetime.now(timezone.utc)}
print(json.dumps(evento, default=lambda o: o.isoformat()))
```
Mais em [[05 - Tratamento de Erros e Arquivos/03 - Arquivos Texto CSV e JSON#Tipos não serializáveis|JSON: tipos não serializáveis]].

---

> [!question] Exercícios
> 1. Mostre a data de hoje no formato `Segunda-feira, 05 de outubro de 2026` (em português, sem `locale`).
> 2. Quantos dias faltam para o seu próximo aniversário?
> 3. Converta `"15/03/2026 18:45"` para ISO 8601 e para o fuso de Lisboa (`Europe/Lisbon`), assumindo que o horário original é de São Paulo.
> 4. Escreva `idade(nascimento)` e teste com datas de aniversário **hoje**, **amanhã** e **ontem**.
> 5. Gere todas as **sextas-feiras 13** de 2026.
> 6. Cronometre uma função com um *decorator* `@medir_tempo` usando `perf_counter`.
> 7. Por que `datetime.utcnow()` é desencorajado? Qual a alternativa?
> 8. Calcule a diferença em horas entre dois eventos aware em fusos distintos.

> [!success]- Soluções
> 1. ```python
>    from datetime import date
>    DIAS = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira",
>            "Sexta-feira", "Sábado", "Domingo"]
>    MESES = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho",
>             "agosto", "setembro", "outubro", "novembro", "dezembro"]
>    d = date.today()
>    print(f"{DIAS[d.weekday()]}, {d.day:02d} de {MESES[d.month - 1]} de {d.year}")
>    ```
> 2. ```python
>    from datetime import date
>    def dias_para_aniversario(nasc, hoje=None):
>        hoje = hoje or date.today()
>        try:
>            prox = nasc.replace(year=hoje.year)
>        except ValueError:                      # 29/02 em ano não bissexto
>            prox = date(hoje.year, 3, 1)
>        if prox < hoje:
>            try:
>                prox = nasc.replace(year=hoje.year + 1)
>            except ValueError:
>                prox = date(hoje.year + 1, 3, 1)
>        return (prox - hoje).days
>    ```
> 3. ```python
>    from datetime import datetime
>    from zoneinfo import ZoneInfo
>    dt = datetime.strptime("15/03/2026 18:45", "%d/%m/%Y %H:%M").replace(tzinfo=ZoneInfo("America/Sao_Paulo"))
>    print(dt.isoformat())
>    print(dt.astimezone(ZoneInfo("Europe/Lisbon")).isoformat())
>    ```
> 4. Use a função `idade` da seção 3 com `hoje` fixo e as três datas.
> 5. ```python
>    from datetime import date
>    print([date(2026, m, 13) for m in range(1, 13) if date(2026, m, 13).weekday() == 4])
>    ```
> 6. ```python
>    import functools, time
>    def medir_tempo(func):
>        @functools.wraps(func)
>        def wrapper(*a, **kw):
>            ini = time.perf_counter()
>            try:
>                return func(*a, **kw)
>            finally:
>                print(f"{func.__name__}: {time.perf_counter() - ini:.4f}s")
>        return wrapper
>    ```
> 7. Devolve um datetime **naive** (sem fuso) que representa UTC, o que leva a confusões com `now()` local. Use `datetime.now(timezone.utc)`.
> 8. ```python
>    a = datetime(2026, 10, 5, 12, tzinfo=ZoneInfo("America/Sao_Paulo"))
>    b = datetime(2026, 10, 5, 12, tzinfo=ZoneInfo("Asia/Tokyo"))
>    print((a - b).total_seconds() / 3600)     # 12.0
>    ```

---

⬅️ [[06 - Módulos da Biblioteca Padrão Essenciais/01 - os pathlib e sys|os, pathlib e sys]] | ➡️ [[06 - Módulos da Biblioteca Padrão Essenciais/03 - collections itertools e functools|collections, itertools e functools]]

#python #intermediario #stdlib #datetime #time #zoneinfo #timedelta
