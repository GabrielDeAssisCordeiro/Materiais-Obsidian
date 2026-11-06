---
titulo: "Exercícios da Biblioteca Padrão"
tags: [python, intermediario, exercicios, pratica, stdlib]
nivel: intermediario
criado: 2026-10-05
modulo: "06 - Módulos da Biblioteca Padrão Essenciais"
---

# 🏋️ Exercícios da Biblioteca Padrão

Exercícios **progressivos** para fixar o **Módulo 06**. Muitos combinam vários módulos, como acontece em projetos reais.

> [!tip] Como praticar
> 1. Antes de escrever código, **consulte a documentação** (`help(modulo.funcao)` ou docs.python.org): ler a doc é uma habilidade central.
> 2. Prefira as ferramentas da stdlib a laços "feitos à mão".
> 3. Registre o que o programa faz com `logging`, e não com `print`.
> 4. Meça com `time.perf_counter()` quando o exercício envolver desempenho.

**Revise antes:** [[06 - Módulos da Biblioteca Padrão Essenciais/01 - os pathlib e sys|os/pathlib/sys]] · [[06 - Módulos da Biblioteca Padrão Essenciais/02 - datetime e time|datetime/time]] · [[06 - Módulos da Biblioteca Padrão Essenciais/03 - collections itertools e functools|collections/itertools/functools]] · [[06 - Módulos da Biblioteca Padrão Essenciais/04 - re Expressões Regulares|re]] · [[06 - Módulos da Biblioteca Padrão Essenciais/05 - json csv e pickle|json/csv/pickle]] · [[06 - Módulos da Biblioteca Padrão Essenciais/06 - concurrent futures e threading|concorrência]] · [[06 - Módulos da Biblioteca Padrão Essenciais/07 - logging|logging]]

---

## 🟢 Nível 1: Aquecimento

> [!question] 1. Inventário de uma pasta
> Mostre, para uma pasta informada por argumento (`sys.argv`, com padrão `.`), o número de arquivos e o tamanho total (em MB) **por extensão**, ordenado do maior para o menor.

> [!success]- Solução
> ```python
> import sys
> from collections import defaultdict
> from pathlib import Path
>
> pasta = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
> qtd, tam = defaultdict(int), defaultdict(int)
>
> for arq in pasta.rglob("*"):
>     if arq.is_file():
>         ext = arq.suffix.lower() or "(sem extensão)"
>         qtd[ext] += 1
>         tam[ext] += arq.stat().st_size
>
> for ext in sorted(tam, key=tam.get, reverse=True):
>     print(f"{ext:<18} {qtd[ext]:>5} arquivos  {tam[ext] / 1_048_576:>8.2f} MB")
> ```

> [!question] 2. Contagem de dias
> Peça a data de nascimento (`dd/mm/aaaa`) e mostre: idade em anos, dias vividos, dia da semana em que nasceu (em português) e quantos dias faltam para o próximo aniversário.

> [!success]- Solução
> ```python
> from datetime import date, datetime
>
> DIAS = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]
>
> def proximo_aniversario(nasc, hoje):
>     for ano in (hoje.year, hoje.year + 1):
>         try:
>             alvo = nasc.replace(year=ano)
>         except ValueError:                 # 29/02
>             alvo = date(ano, 3, 1)
>         if alvo >= hoje:
>             return alvo
>
> nasc = datetime.strptime(input("Nascimento (dd/mm/aaaa): "), "%d/%m/%Y").date()
> hoje = date.today()
> idade = hoje.year - nasc.year - ((hoje.month, hoje.day) < (nasc.month, nasc.day))
>
> print(f"Idade: {idade} anos")
> print(f"Dias vividos: {(hoje - nasc).days:,}")
> print(f"Nasceu numa {DIAS[nasc.weekday()]}-feira" if nasc.weekday() < 5 else f"Nasceu num {DIAS[nasc.weekday()]}")
> print(f"Faltam {(proximo_aniversario(nasc, hoje) - hoje).days} dias para o próximo aniversário")
> ```

> [!question] 3. Palavras mais comuns
> Leia um texto e liste as 5 palavras mais frequentes com mais de 3 letras, ignorando maiúsculas, acentos de pontuação e uma lista de *stopwords* à sua escolha.

> [!success]- Solução
> ```python
> import re
> from collections import Counter
>
> STOPWORDS = {"para", "com", "uma", "mas", "que", "dos", "das", "como", "mais", "isso"}
>
> def top_palavras(texto, n=5):
>     palavras = re.findall(r"[^\W\d_]{4,}", texto.lower())      # só letras, 4+
>     return Counter(p for p in palavras if p not in STOPWORDS).most_common(n)
> ```

---

## 🟡 Nível 2: Combinando módulos

> [!question] 4. Organizador de arquivos por data
> Mova os arquivos de uma pasta para subpastas `AAAA/MM` com base na **data de modificação**. Faça um modo `--simular` (só mostra o que faria) com `argparse`. Registre cada ação com `logging`.

> [!success]- Solução
> ```python
> import argparse
> import logging
> import shutil
> from datetime import datetime
> from pathlib import Path
>
> log = logging.getLogger("organizador")
>
> def organizar(pasta, simular):
>     movidos = 0
>     for arq in Path(pasta).iterdir():
>         if not arq.is_file():
>             continue
>         quando = datetime.fromtimestamp(arq.stat().st_mtime)
>         destino = Path(pasta) / f"{quando:%Y}" / f"{quando:%m}"
>         alvo = destino / arq.name
>         if alvo.exists():
>             alvo = destino / f"{arq.stem}_{int(arq.stat().st_mtime)}{arq.suffix}"
>         log.info("%s → %s%s", arq.name, alvo.relative_to(pasta), "  [simulação]" if simular else "")
>         if not simular:
>             destino.mkdir(parents=True, exist_ok=True)
>             shutil.move(str(arq), alvo)
>         movidos += 1
>     return movidos
>
> if __name__ == "__main__":
>     ap = argparse.ArgumentParser(description="Organiza arquivos por data")
>     ap.add_argument("pasta")
>     ap.add_argument("--simular", action="store_true")
>     args = ap.parse_args()
>     logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
>     print(f"{organizar(args.pasta, args.simular)} arquivo(s) processado(s)")
> ```

> [!question] 5. Extrator de dados de texto
> A partir de um texto qualquer, extraia com `re`: e-mails, telefones brasileiros, datas `dd/mm/aaaa` e valores em reais (`R$ 1.234,56`). Converta datas para `date`, valores para `Decimal` e grave tudo em `extraidos.json`.

> [!success]- Solução
> ```python
> import json
> import re
> from datetime import datetime
> from decimal import Decimal
>
> EMAIL = re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+")
> TEL = re.compile(r"\(?\d{2}\)?\s?9?\d{4}-?\d{4}")
> DATA = re.compile(r"\b(\d{2})/(\d{2})/(\d{4})\b")
> VALOR = re.compile(r"R\$\s?(\d{1,3}(?:\.\d{3})*,\d{2})")
>
> def extrair(texto):
>     datas = []
>     for d, m, a in DATA.findall(texto):
>         try:
>             datas.append(datetime(int(a), int(m), int(d)).date())
>         except ValueError:
>             pass                              # 31/02, por exemplo
>     valores = [Decimal(v.replace(".", "").replace(",", ".")) for v in VALOR.findall(texto)]
>     return {
>         "emails": sorted(set(EMAIL.findall(texto))),
>         "telefones": sorted({re.sub(r"\D", "", t) for t in TEL.findall(texto)}),
>         "datas": sorted(datas),
>         "valores": valores,
>     }
>
> dados = extrair(open("texto.txt", encoding="utf-8").read())
> with open("extraidos.json", "w", encoding="utf-8") as f:
>     json.dump(dados, f, ensure_ascii=False, indent=2,
>               default=lambda o: o.isoformat() if hasattr(o, "isoformat") else str(o))
> ```

> [!question] 6. Cache com `lru_cache` e métricas
> Escreva uma função lenta `consultar_cep(cep)` (simule com `sleep`), aplique `@lru_cache(maxsize=128)` e mostre o ganho de tempo e `cache_info()` após consultar uma lista de CEPs com repetições.

> [!success]- Solução
> ```python
> import random
> import time
> from functools import lru_cache
>
> @lru_cache(maxsize=128)
> def consultar_cep(cep):
>     time.sleep(0.2)                    # simula rede
>     return {"cep": cep, "cidade": "São Paulo"}
>
> ceps = [random.choice(["01001-000", "20040-020", "30140-071"]) for _ in range(20)]
> ini = time.perf_counter()
> for c in ceps:
>     consultar_cep(c)
> print(f"{time.perf_counter() - ini:.2f}s")      # ≈ 0.6s em vez de ≈ 4s
> print(consultar_cep.cache_info())
> ```

---

## 🟠 Nível 3: Dados, concorrência e logging

> [!question] 7. Relatório de vendas (CSV + collections + itertools + JSON)
> Dado `vendas.csv` (`data;vendedor;produto;valor`, separador `;`, valor com vírgula decimal), gere `relatorio.json` com: total por vendedor, produto mais vendido, total por mês (`AAAA-MM`) e o melhor vendedor de cada mês. Linhas inválidas devem ser ignoradas e **logadas**.

> [!success]- Solução
> ```python
> import csv
> import json
> import logging
> from collections import Counter, defaultdict
> from datetime import datetime
> from decimal import Decimal, InvalidOperation
>
> log = logging.getLogger("vendas")
> logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
>
> por_vendedor = defaultdict(Decimal)
> por_produto = Counter()
> por_mes = defaultdict(Decimal)
> vendedor_mes = defaultdict(lambda: defaultdict(Decimal))
>
> with open("vendas.csv", newline="", encoding="utf-8-sig") as f:
>     for n, linha in enumerate(csv.DictReader(f, delimiter=";"), start=2):
>         try:
>             data = datetime.strptime(linha["data"], "%d/%m/%Y")
>             valor = Decimal(linha["valor"].replace(".", "").replace(",", "."))
>         except (KeyError, ValueError, InvalidOperation) as e:
>             log.warning("Linha %d ignorada (%s): %s", n, type(e).__name__, linha)
>             continue
>         mes = f"{data:%Y-%m}"
>         vend = linha["vendedor"].strip().title()
>         por_vendedor[vend] += valor
>         por_produto[linha["produto"].strip()] += 1
>         por_mes[mes] += valor
>         vendedor_mes[mes][vend] += valor
>
> relatorio = {
>     "total_por_vendedor": {k: str(v) for k, v in por_vendedor.items()},
>     "produto_mais_vendido": por_produto.most_common(1)[0] if por_produto else None,
>     "total_por_mes": {k: str(v) for k, v in sorted(por_mes.items())},
>     "melhor_vendedor_por_mes": {
>         mes: max(v, key=v.get) for mes, v in sorted(vendedor_mes.items())
>     },
> }
> with open("relatorio.json", "w", encoding="utf-8") as f:
>     json.dump(relatorio, f, ensure_ascii=False, indent=2)
> ```

> [!question] 8. Baixador paralelo com relatório
> Dada uma lista de URLs, baixe-as em paralelo (`ThreadPoolExecutor`, 8 *workers*), com *timeout* de 5 s e **até 3 tentativas** (backoff de 0,5 s). Registre sucesso/falha com `logging` (incluindo o nome da thread) e gere um CSV com `url, status, tamanho_bytes, tempo_s, tentativas`.

> [!success]- Solução
> ```python
> import csv
> import logging
> import time
> import urllib.request
> from concurrent.futures import ThreadPoolExecutor, as_completed
>
> logging.basicConfig(level=logging.INFO,
>                     format="%(asctime)s [%(threadName)s] %(levelname)s %(message)s")
> log = logging.getLogger("baixador")
>
> def baixar(url, tentativas=3, espera=0.5, timeout=5):
>     inicio = time.perf_counter()
>     for n in range(1, tentativas + 1):
>         try:
>             with urllib.request.urlopen(url, timeout=timeout) as r:
>                 corpo = r.read()
>             log.info("OK %s (%d bytes)", url, len(corpo))
>             return {"url": url, "status": r.status, "tamanho_bytes": len(corpo),
>                     "tempo_s": round(time.perf_counter() - inicio, 3), "tentativas": n}
>         except Exception as e:
>             log.warning("Tentativa %d/%d falhou em %s: %s", n, tentativas, url, e)
>             if n < tentativas:
>                 time.sleep(espera * n)
>     return {"url": url, "status": "ERRO", "tamanho_bytes": 0,
>             "tempo_s": round(time.perf_counter() - inicio, 3), "tentativas": tentativas}
>
> def main(urls):
>     resultados = []
>     with ThreadPoolExecutor(max_workers=8, thread_name_prefix="dl") as pool:
>         futuros = [pool.submit(baixar, u) for u in urls]
>         for f in as_completed(futuros):
>             resultados.append(f.result())
>     with open("downloads.csv", "w", newline="", encoding="utf-8") as f:
>         w = csv.DictWriter(f, fieldnames=list(resultados[0]))
>         w.writeheader()
>         w.writerows(sorted(resultados, key=lambda r: r["url"]))
>
> if __name__ == "__main__":
>     main(["https://www.python.org", "https://pypi.org", "https://docs.python.org"])
> ```

> [!question] 9. Agrupamento com `itertools`
> Dada uma lista de eventos `(timestamp_iso, usuario, acao)`, use `groupby` para agrupar por **dia** e `Counter` para mostrar as ações mais comuns de cada dia. Depois, use `pairwise` para calcular o **intervalo médio** (em minutos) entre eventos consecutivos de cada dia.

> [!success]- Solução
> ```python
> from collections import Counter
> from datetime import datetime
> from itertools import groupby, pairwise
> from statistics import mean
>
> eventos = [
>     ("2026-10-05T09:00:00", "ana", "login"),
>     ("2026-10-05T09:30:00", "ana", "compra"),
>     ("2026-10-05T10:30:00", "bia", "login"),
>     ("2026-10-06T08:00:00", "ana", "login"),
>     ("2026-10-06T08:20:00", "ana", "login"),
> ]
>
> parsed = sorted((datetime.fromisoformat(t), u, a) for t, u, a in eventos)
>
> for dia, grupo in groupby(parsed, key=lambda e: e[0].date()):
>     lista = list(grupo)
>     print(dia, Counter(a for _, _, a in lista).most_common())
>     if len(lista) > 1:
>         intervalos = [(b[0] - a[0]).total_seconds() / 60 for a, b in pairwise(lista)]
>         print(f"  intervalo médio: {mean(intervalos):.1f} min")
> ```

---

## 🔴 Nível 4: Desafios

> [!question] 10. Descubra os bugs
> ```python
> # (a)
> from datetime import datetime
> agora = datetime.utcnow()
> local = datetime.now()
> print(agora - local.astimezone())
>
> # (b)
> import re
> if re.match(r"\d+", "valor: 123"):
>     print("tem número")
>
> # (c)
> from itertools import groupby
> dados = ["b", "a", "b", "a"]
> print({k: list(g) for k, g in groupby(dados)})
>
> # (d)
> from functools import lru_cache
> @lru_cache
> def somar(lista):
>     return sum(lista)
> somar([1, 2, 3])
>
> # (e)
> import logging
> logging.basicConfig(level=logging.INFO)
> logging.debug(f"Processando {dados}")
>
> # (f)
> import pickle
> obj = pickle.loads(dados_vindos_da_internet)
>
> # (g)
> from collections import defaultdict
> d = defaultdict(list)
> if d["x"]:
>     ...
> print("x" in d)       # surpresa?
>
> # (h)
> import csv
> with open("a.csv", "w") as f:
>     csv.writer(f).writerow([1, 2])
> ```

> [!success]- Solução
> ```python
> # (a) utcnow() é obsoleto e devolve datetime NAIVE; misturar naive/aware dá TypeError.
> from datetime import timezone
> agora = datetime.now(timezone.utc)
>
> # (b) match só olha o INÍCIO: retorna None. Use re.search.
>
> # (c) groupby agrupa apenas consecutivos: ordene antes.
> {k: list(g) for k, g in groupby(sorted(dados))}
>
> # (d) list não é hasheável → TypeError. Use tupla: somar((1, 2, 3)).
> #     (e @lru_cache sem parênteses exige Python 3.8+)
>
> # (e) f-string é formatada mesmo com DEBUG desligado. Use:
> logging.debug("Processando %s", dados)
>
> # (f) pickle.loads de fonte não confiável executa código arbitrário. Use JSON.
>
> # (g) d["x"] CRIA a chave 'x' com [] → "x" in d é True. Use d.get("x") ou "x" in d.
>
> # (h) falta newline="" e encoding no open (linhas em branco extras no Windows).
> with open("a.csv", "w", newline="", encoding="utf-8") as f:
>     csv.writer(f).writerow([1, 2])
> ```

> [!question] 11. Mini-projeto: Monitor de pasta com relatório
> Crie um programa `monitor.py` que:
> 1. Recebe uma pasta e um intervalo (segundos) por `argparse`.
> 2. A cada intervalo, lista os arquivos (`pathlib`) e **detecta** criados, removidos e modificados desde a última verificação (use `dict` de `{caminho: (tamanho, mtime)}`).
> 3. Registra cada mudança com `logging` (console em INFO, arquivo `monitor.log` rotativo em DEBUG).
> 4. Mantém **contadores** com `Counter` por tipo de mudança e por extensão.
> 5. Ao receber `Ctrl+C`, grava `resumo.json` (com datas em ISO) e encerra com elegância (`KeyboardInterrupt`).
> 6. **Bônus:** calcule o hash SHA-256 dos arquivos modificados em paralelo (`ThreadPoolExecutor`) e inclua no log.

> [!success]- Solução (completa)
> ```python
> import argparse
> import hashlib
> import json
> import logging
> import time
> from collections import Counter
> from concurrent.futures import ThreadPoolExecutor
> from datetime import datetime, timezone
> from logging.handlers import RotatingFileHandler
> from pathlib import Path
>
> log = logging.getLogger("monitor")
>
>
> def configurar_logs():
>     log.setLevel(logging.DEBUG)
>     fmt = logging.Formatter("%(asctime)s | %(levelname)-7s | %(message)s", "%H:%M:%S")
>     console = logging.StreamHandler()
>     console.setLevel(logging.INFO)
>     console.setFormatter(fmt)
>     arquivo = RotatingFileHandler("monitor.log", maxBytes=500_000, backupCount=2, encoding="utf-8")
>     arquivo.setLevel(logging.DEBUG)
>     arquivo.setFormatter(fmt)
>     log.addHandler(console)
>     log.addHandler(arquivo)
>
>
> def instantaneo(pasta):
>     estado = {}
>     for arq in pasta.rglob("*"):
>         if arq.is_file():
>             st = arq.stat()
>             estado[arq] = (st.st_size, st.st_mtime)
>     return estado
>
>
> def sha256(arq):
>     h = hashlib.sha256()
>     try:
>         with arq.open("rb") as f:
>             while bloco := f.read(1 << 20):
>                 h.update(bloco)
>     except OSError as e:
>         return arq, f"erro: {e}"
>     return arq, h.hexdigest()[:12]
>
>
> def comparar(antes, depois):
>     criados = depois.keys() - antes.keys()
>     removidos = antes.keys() - depois.keys()
>     modificados = {a for a in antes.keys() & depois.keys() if antes[a] != depois[a]}
>     return criados, removidos, modificados
>
>
> def main():
>     ap = argparse.ArgumentParser(description="Monitora mudanças em uma pasta")
>     ap.add_argument("pasta", type=Path)
>     ap.add_argument("--intervalo", type=float, default=2.0)
>     args = ap.parse_args()
>
>     if not args.pasta.is_dir():
>         ap.error(f"{args.pasta} não é uma pasta")
>
>     configurar_logs()
>     inicio = datetime.now(timezone.utc)
>     por_tipo, por_ext = Counter(), Counter()
>     estado = instantaneo(args.pasta)
>     log.info("Monitorando %s (%d arquivos). Ctrl+C para sair.", args.pasta, len(estado))
>
>     try:
>         with ThreadPoolExecutor(max_workers=4) as pool:
>             while True:
>                 time.sleep(args.intervalo)
>                 novo = instantaneo(args.pasta)
>                 criados, removidos, modificados = comparar(estado, novo)
>
>                 for a in sorted(criados):
>                     log.info("➕ criado: %s", a.name)
>                     por_tipo["criado"] += 1; por_ext[a.suffix or "(sem ext)"] += 1
>                 for a in sorted(removidos):
>                     log.info("➖ removido: %s", a.name)
>                     por_tipo["removido"] += 1; por_ext[a.suffix or "(sem ext)"] += 1
>                 for a, h in pool.map(sha256, sorted(modificados)):
>                     log.info("✏️  modificado: %s (sha256 %s)", a.name, h)
>                     por_tipo["modificado"] += 1; por_ext[a.suffix or "(sem ext)"] += 1
>
>                 log.debug("Ciclo concluído: %d arquivos", len(novo))
>                 estado = novo
>     except KeyboardInterrupt:
>         log.info("Encerrando...")
>     finally:
>         resumo = {
>             "pasta": str(args.pasta.resolve()),
>             "inicio": inicio.isoformat(),
>             "fim": datetime.now(timezone.utc).isoformat(),
>             "mudancas_por_tipo": dict(por_tipo),
>             "mudancas_por_extensao": dict(por_ext),
>         }
>         Path("resumo.json").write_text(
>             json.dumps(resumo, ensure_ascii=False, indent=2), encoding="utf-8"
>         )
>         log.info("resumo.json gravado")
>
>
> if __name__ == "__main__":
>     main()
> ```

---

## 🧪 Quiz relâmpago

> [!question] Responda sem rodar o código
> 1. Qual a diferença entre `Path.read_text()` e `open(...).read()`? E entre `Path("a") / "/b"` e `Path("a") / "b"`?
> 2. Por que `datetime.utcnow()` é desencorajado? O que usar?
> 3. `td.seconds` e `td.total_seconds()` são equivalentes?
> 4. Qual a diferença entre `re.match`, `re.search` e `re.fullmatch`?
> 5. O que significa um quantificador **guloso** vs **preguiçoso**?
> 6. Quando `groupby` dá resultados "estranhos"?
> 7. Para que serve `functools.partial`? Dê um exemplo.
> 8. Threads aceleram um laço que só faz cálculos? Por quê?
> 9. Por que `logger.debug("x=%s", x)` é melhor que `logger.debug(f"x={x}")`?
> 10. Por que **nunca** carregar pickle de fonte desconhecida?

> [!success]- Respostas
> 1. `Path.read_text()` é um atalho que abre/lê/fecha (com `encoding`); `open(...).read()` exige fechar manualmente (use `with`). `Path("a") / "/b"` → `/b` (absoluto descarta o anterior); `Path("a") / "b"` → `a/b`.
> 2. Devolve datetime **naive**, ambíguo; use `datetime.now(timezone.utc)` (aware).
> 3. Não: `.seconds` é só a parte restante do dia (0–86399); `.total_seconds()` é a duração total.
> 4. `match`: casa no **início**; `search`: em **qualquer posição**; `fullmatch`: a string **inteira**.
> 5. Guloso casa o **máximo** possível (`.+`); preguiçoso o **mínimo** (`.+?`).
> 6. Quando os dados **não estão ordenados** pela chave: `groupby` só agrupa itens **consecutivos**.
> 7. Fixa argumentos de uma função: `partial(int, base=2)("1010")` → `10`.
> 8. Não, por causa do **GIL**: só uma thread executa Python por vez. Use processos para CPU-bound.
> 9. A formatação só ocorre se o nível estiver ativo (evita custo desnecessário).
> 10. O `pickle` pode **executar código arbitrário** ao ser carregado.

---

## ✅ Checklist do módulo

- [ ] Uso `pathlib` para caminhos e `shutil`/`os`/`sys` quando necessário
- [ ] Trabalho com `datetime`, `timedelta` e fusos (`zoneinfo`), e evito misturar naive/aware
- [ ] Aplico `Counter`, `defaultdict`, `deque`, `itertools` e `functools` (`partial`, `cache`)
- [ ] Escrevo e depuro **expressões regulares** com grupos nomeados e `VERBOSE`
- [ ] Serializo com **JSON/CSV** (e conheço os perigos do **pickle**)
- [ ] Escolho entre **threads**, **processos** e **asyncio** conforme I/O-bound ou CPU-bound
- [ ] Uso `ThreadPoolExecutor`, `Lock` e `Queue` com segurança
- [ ] Configuro `logging` (níveis, handlers, rotação) em vez de `print`
- [ ] Resolvi pelo menos 8 dos exercícios acima

---

## 🚀 Próximo módulo
➡️ [[07 - Programação Funcional e Intermediário/01 - Funções de Ordem Superior|Módulo 07: Programação Funcional e Intermediário]]

⬅️ [[06 - Módulos da Biblioteca Padrão Essenciais/07 - logging|logging]] · ⬆️ [[Índice - Python|Índice]]

#python #intermediario #exercicios #pratica #stdlib #logging #concorrencia #regex
