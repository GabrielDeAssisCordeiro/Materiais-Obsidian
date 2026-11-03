"""Contrato de saída: valida, por código, o que o modelo devolveu antes de a aplicação usá-lo.

Biblioteca padrão apenas. Material didático do curso: não é uma biblioteca de produção.
A ideia central: a saída do modelo é ENTRADA NÃO CONFIÁVEL para o resto do sistema.
Só o que cumpre o contrato segue adiante; o resto é descartado, nunca "consertado" por adivinhação.
"""
from __future__ import annotations

import json
import re
import unicodedata
from dataclasses import dataclass, field

# Canais comuns de exfiltração em saídas renderizadas: imagem markdown, link markdown, URL solta.
_IMG_MD = re.compile(r"!\[[^\]]*\]\([^)]*\)")
_LINK_MD = re.compile(r"\[[^\]]*\]\([^)]*\)")
_URL = re.compile(r"(?i)\b(?:https?://|ftp://|www\.)\S+")
_TAG_HTML = re.compile(r"<\s*/?\s*[a-zA-Z][^>]*>")


def normalizar(texto: str) -> str:
    """minúsculas, sem acentos, só letras e dígitos (para comparar segredos sem separadores)."""
    d = unicodedata.normalize("NFKD", texto)
    d = "".join(c for c in d if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]", "", d.lower())


@dataclass
class Campo:
    tipo: type = str
    obrigatorio: bool = True
    max_len: int = 2000
    opcoes: tuple | None = None          # enumeração fechada
    padrao: str | None = None            # regex que o valor inteiro deve cumprir
    permitir_urls: bool = False
    permitir_html: bool = False


@dataclass
class Contrato:
    campos: dict[str, Campo]
    segredos: tuple[str, ...] = ()       # nunca podem aparecer (comparação normalizada)
    permitir_extras: bool = False
    max_bytes: int = 8000


@dataclass
class Resultado:
    ok: bool
    erros: list[str] = field(default_factory=list)
    dados: dict | None = None


def validar(saida: str, contrato: Contrato) -> Resultado:
    """Valida `saida` (texto bruto do modelo). Exige JSON objeto, sem texto antes ou depois."""
    erros: list[str] = []
    if len(saida.encode("utf-8")) > contrato.max_bytes:
        return Resultado(False, ["saída maior que o limite de bytes"])
    try:
        dados = json.loads(saida)
    except json.JSONDecodeError:
        return Resultado(False, ["saída não é JSON válido (texto extra conta como violação)"])
    if not isinstance(dados, dict):
        return Resultado(False, ["JSON precisa ser um objeto"])

    extras = set(dados) - set(contrato.campos)
    if extras and not contrato.permitir_extras:
        erros.append(f"campos não previstos: {sorted(extras)}")

    for nome, c in contrato.campos.items():
        if nome not in dados:
            if c.obrigatorio:
                erros.append(f"campo obrigatório ausente: {nome}")
            continue
        v = dados[nome]
        if type(v) is not c.tipo:                      # bool não passa por int, etc.
            erros.append(f"{nome}: tipo {type(v).__name__}, esperado {c.tipo.__name__}")
            continue
        if isinstance(v, str):
            if len(v) > c.max_len:
                erros.append(f"{nome}: excede {c.max_len} caracteres")
            if c.opcoes is not None and v not in c.opcoes:
                erros.append(f"{nome}: valor fora da lista permitida")
            if c.padrao is not None and not re.fullmatch(c.padrao, v):
                erros.append(f"{nome}: não cumpre o padrão exigido")
            if not c.permitir_urls and (_URL.search(v) or _IMG_MD.search(v) or _LINK_MD.search(v)):
                erros.append(f"{nome}: contém URL/link/imagem (possível canal de exfiltração)")
            if not c.permitir_html and _TAG_HTML.search(v):
                erros.append(f"{nome}: contém marcação HTML")
        elif c.opcoes is not None and v not in c.opcoes:
            erros.append(f"{nome}: valor fora da lista permitida")

    alvo = normalizar(json.dumps(dados, ensure_ascii=False))
    for s in contrato.segredos:
        if normalizar(s) and normalizar(s) in alvo:
            erros.append("saída contém segredo protegido (comparação normalizada)")
            break

    return Resultado(not erros, erros, dados if not erros else None)


# Exemplo do curso: o tradutor fictício. O contrato fecha o espaço de saída:
# um modelo "sequestrado" que escreva só um canário, ou texto livre, deixa de cumprir.
CONTRATO_TRADUTOR = Contrato(
    campos={
        "idioma": Campo(opcoes=("en",)),
        "traducao": Campo(max_len=2000),
    },
    segredos=("PIPA-77",),
)
