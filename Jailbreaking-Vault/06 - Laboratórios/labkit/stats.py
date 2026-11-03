"""Estatística para taxas observadas em N repetições."""

import math
from math import comb


def wilson(k: int, n: int, z: float = 1.96):
    """Intervalo de Wilson para a proporção k/n. Retorna (taxa, inferior, superior)."""
    if n <= 0:
        return (float("nan"), float("nan"), float("nan"))
    p = k / n
    denom = 1 + z**2 / n
    centro = (p + z**2 / (2 * n)) / denom
    margem = z * math.sqrt(p * (1 - p) / n + z**2 / (4 * n**2)) / denom
    return (p, max(0.0, centro - margem), min(1.0, centro + margem))


def regra_dos_tres(n: int) -> float:
    """Limite superior aproximado (95%) da taxa quando há 0 eventos em n tentativas."""
    return 3.0 / n if n > 0 else 1.0


def n_minimo_zero_falhas(limite: float = 0.03, z: float = 1.96) -> int:
    """Menor n tal que 0 falhas em n execuções dá limite superior de Wilson < limite."""
    n = 1
    while wilson(0, n, z)[2] >= limite:
        n += 1
    return n


def fisher_exato(a: int, b: int, c: int, d: int) -> float:
    """Teste exato de Fisher bilateral para a tabela [[a, b], [c, d]].

    a, b = (eventos, não eventos) no grupo 1; c, d = idem no grupo 2.
    """
    linha1, linha2, col1 = a + b, c + d, a + c
    total = linha1 + linha2
    if total == 0:
        return 1.0

    def prob(x: int) -> float:
        return comb(linha1, x) * comb(linha2, col1 - x) / comb(total, col1)

    inferior = max(0, col1 - linha2)
    superior = min(linha1, col1)
    p_obs = prob(a)
    soma = sum(prob(x) for x in range(inferior, superior + 1) if prob(x) <= p_obs * (1 + 1e-9))
    return min(1.0, soma)


def formatar_taxa(k: int, n: int) -> str:
    """Ex.: '4/30 = 13.3% [IC95% 5.3%–29.7%]'."""
    if n <= 0:
        return "n/d"
    p, lo, hi = wilson(k, n)
    return f"{k}/{n} = {p:.1%} [IC95% {lo:.1%}–{hi:.1%}]"
