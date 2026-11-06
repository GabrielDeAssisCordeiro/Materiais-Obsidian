#!/usr/bin/env python3
"""Valida o vault Materiais Obsidian.

Uso:  python scripts/validate_vault.py [caminho-do-vault]
Sai com código 1 se houver erros. Requer PyYAML (pip install pyyaml).
"""
import collections
import json
import os
import re
import sys
import unicodedata

import yaml

ROOT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), ".."))
SKIP_DIRS = {".obsidian", ".trash", ".git", ".github", "scripts", "node_modules"}
NO_FRONTMATTER = {"README.md"}
OLD_KEYS = {"título", "nível", "title", "level", "data", "status"}
NIVEIS = {"iniciante", "intermediario", "avancado", "todos"}
ALLOWED_SINGLE_TAGS = {"glossario"}
FM = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.S)
WIKILINK = re.compile(r"\[\[([^\]|#]+)(#[^\]|]*)?(\|[^\]]*)?\]\]")
FENCE = re.compile(r"^\s*(`{3,}|~{3,})")

errors = []
warnings = []


def err(msg):
    errors.append(msg)


def walk(exts):
    for dp, dn, fn in os.walk(ROOT):
        dn[:] = sorted(d for d in dn if d not in SKIP_DIRS)
        for f in sorted(fn):
            if f.endswith(exts):
                yield os.path.join(dp, f)


def rel(p):
    return os.path.relpath(p, ROOT).replace(os.sep, "/")


def strip_code(text):
    text = re.sub(r"```.*?```|~~~.*?~~~", "", text, flags=re.S)
    return re.sub(r"`[^`\n]*`", "", text)


def h1s(body):
    found, fence = [], None
    for line in body.split("\n"):
        m = FENCE.match(line)
        if m:
            if fence is None:
                fence = m.group(1)[0] * 3
            elif line.strip().startswith(fence):
                fence = None
            continue
        if fence is None and re.match(r"^# (.+)$", line):
            found.append(line[2:].strip())
    return found


def clean_title(h):
    h = re.sub(r"^[^\w(\[`\"']+", "", h).strip()
    return h.replace("`", "").strip()


def fold(s):
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()


notes = {}  # caminho relativo -> (frontmatter, corpo)
for p in walk((".md",)):
    r = rel(p)
    if r in NO_FRONTMATTER:
        continue
    text = open(p, encoding="utf-8").read()
    m = FM.match(text)
    if not m:
        err(f"{r}: sem frontmatter")
        continue
    try:
        y = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError as e:
        err(f"{r}: YAML inválido ({str(e).splitlines()[0]})")
        continue
    notes[r] = (y, text[m.end():])

# 1) propriedades, H1 e titulo
tags_count = collections.Counter()
for r, (y, body) in notes.items():
    in_templates = r.startswith("Templates/")
    for k in OLD_KEYS & set(y):
        err(f"{r}: propriedade antiga/removida '{k}'")
    if "nivel" in y and str(y["nivel"]) not in NIVEIS:
        err(f"{r}: nivel inválido '{y['nivel']}'")
    for t in y.get("tags") or []:
        tags_count[str(t)] += 1
    if in_templates:
        continue
    hs = h1s(body)
    if len(hs) != 1:
        err(f"{r}: esperado 1 H1, encontrado {len(hs)}")
    elif "titulo" in y and str(y["titulo"]).strip() != clean_title(hs[0]):
        err(f"{r}: titulo '{y['titulo']}' difere do H1 '{hs[0]}'")

for t, c in tags_count.items():
    if c == 1 and t not in ALLOWED_SINGLE_TAGS:
        warnings.append(f"tag de uso único: {t}")

# 2) nomes únicos
names = collections.defaultdict(list)
for r in notes:
    names[os.path.basename(r)[:-3].lower()].append(r)
for n, l in names.items():
    if len(l) > 1:
        err(f"nome de nota repetido '{n}': {l}")

# 3) aliases
alias_owner = collections.defaultdict(list)
for r, (y, _) in notes.items():
    a = y.get("aliases") or []
    if isinstance(a, str):
        a = [a]
    seen = set()
    for x in a:
        x = str(x).lower()
        if x in seen:
            err(f"{r}: alias repetido na própria nota '{x}'")
        seen.add(x)
        alias_owner[x].append(r)
for a, l in alias_owner.items():
    if len(set(l)) > 1:
        err(f"alias repetido '{a}': {sorted(set(l))}")
    if a in names and any(os.path.basename(x)[:-3].lower() != a for x in l):
        err(f"alias '{a}' coincide com o nome de outra nota ({names[a]}) em {l}")

# 4) links
all_files = {}
for dp, dn, fn in os.walk(ROOT):
    dn[:] = [d for d in dn if d not in SKIP_DIRS]
    for f in fn:
        all_files[rel(os.path.join(dp, f)).lower()] = rel(os.path.join(dp, f))
lows = list(all_files)


def resolve(target):
    t = target.strip().rstrip("\\").strip().lower()
    if not t:
        return []
    return [k for k in lows if k in (t, t + ".md") or k.endswith("/" + t) or k.endswith("/" + t + ".md")]


headings = {}
for r in ("Glossário.md",):
    p = os.path.join(ROOT, r)
    if os.path.exists(p):
        headings[r] = set(re.findall(r"^#{2,4} (.+)$", open(p, encoding="utf-8").read(), re.M))

for r, (y, body) in notes.items():
    text = open(os.path.join(ROOT, r), encoding="utf-8").read()
    for m in WIKILINK.finditer(strip_code(text)):
        if m.group(1).strip() == "":
            continue
        c = resolve(m.group(1))
        if not c:
            err(f"{r}: link quebrado {m.group(0)}")
        elif len(c) > 1:
            err(f"{r}: link ambíguo {m.group(0)} -> {c}")
        elif m.group(1).strip().lower() in ("glossário",) and m.group(2):
            anchor = m.group(2)[1:]
            if anchor not in headings.get("Glossário.md", set()):
                err(f"{r}: âncora inexistente no Glossário '{anchor}'")

# 5) canvases
for p in walk((".canvas",)):
    r = rel(p)
    try:
        data = json.load(open(p, encoding="utf-8"))
    except ValueError as e:
        err(f"{r}: JSON inválido ({e})")
        continue
    ids = {n["id"] for n in data.get("nodes", [])}
    for n in data.get("nodes", []):
        if n.get("type") == "file" and not os.path.exists(os.path.join(ROOT, n["file"])):
            err(f"{r}: arquivo inexistente no canvas '{n['file']}'")
    for e in data.get("edges", []):
        if e["fromNode"] not in ids or e["toNode"] not in ids:
            err(f"{r}: aresta aponta para nó inexistente")

# 6) 00 - Início de cada material
for d in sorted(os.listdir(ROOT)):
    full = os.path.join(ROOT, d)
    if not os.path.isdir(full) or d in SKIP_DIRS or d in ("Templates", "Anexos"):
        continue
    ini = os.path.join(full, "00 - Início")
    if not os.path.isdir(ini):
        err(f"{d}: falta a pasta '00 - Início'")
        continue
    files = [f[:-3] for f in os.listdir(ini) if f.endswith(".md")]
    for pref in ("Home - ", "Índice - ", "Trilha de aprendizado - "):
        found = [f for f in files if f.startswith(pref)]
        if len(found) != 1:
            err(f"{d}/00 - Início: esperada 1 nota '{pref}<Material>', encontrada(s) {len(found)}")
    extras = [f for f in files if not f.startswith(("Home - ", "Índice - ", "Trilha de aprendizado - "))]
    if extras:
        err(f"{d}/00 - Início: notas além das três padrão: {extras}")
    if [f for f in os.listdir(ini) if not f.endswith(".md")]:
        err(f"{d}/00 - Início: arquivos que não são notas")

total = len(notes)
for w in warnings[:20]:
    print("AVISO:", w)
if len(warnings) > 20:
    print(f"AVISO: ... e mais {len(warnings) - 20} avisos")
if errors:
    for e in errors:
        print("ERRO:", e)
    print(f"\n{len(errors)} erro(s) em {total} notas.")
    sys.exit(1)
print(f"OK: {total} notas validadas, nenhum erro.")
