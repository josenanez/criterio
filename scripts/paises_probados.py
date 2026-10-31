#!/usr/bin/env python3
"""Los países probados de la CFO y de la CLO, en una tabla de cada README de la familia.

    python3 scripts/paises_probados.py           escribe la sección en los cuatro README
    python3 scripts/paises_probados.py --check   falla si un README no es el que sale de la evidencia

Nada de la tabla se escribe a mano. Cada fila sale de:
  - la evidencia de las rondas (tests/evidencias/familias/<familia>/ronda-N/<entidad>/calificacion.json):
    la ronda en que el país entró, las rondas en que corrió, y las señales y los datos de la corrida
    más reciente de cada una de sus entidades;
  - la clave de cada entidad del material (tests/criterio-<familia>/material/<entidad>/clave.json): su
    país y su industria, y si es de control;
  - el registro de países (plugins/criterio-finance/scripts/paises.json): lo propio del país —la
    factura y su impuesto en la CFO, la regla de la contratación pública en la CLO—, con su fuente.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PAISES = {p["codigo"]: p for p in json.loads((RAIZ / "plugins/criterio-finance/scripts/paises.json").read_text(encoding="utf-8"))["paises"]}
INICIO = "<!-- países probados: generado por scripts/paises_probados.py desde la evidencia de las rondas; no se edita a mano -->"
FIN = "<!-- /países probados -->"
ORDEN = ["banca", "cooperativas", "retail", "mineria", "publica"]

T = {
    "es": {"archivo": "README.es.md", "titulo": "## Los países probados",
           "lead": "{n} países, en el orden en que entraron, con todas las entidades de su material —una de control, sin "
                   "ningún defecto sembrado, en cada país—. Las señales y los datos son los de la corrida más reciente "
                   "de cada entidad con todos sus agentes; las rondas cuentan también las verificaciones. Las entidades, los defectos sembrados y las señales esperadas, en "
                   "[`EVIDENCIA.md`](../../tests/criterio-{s}/EVIDENCIA.md); cada corrida con su costo y su calificación, en "
                   "[las rondas de la familia](../../tests/evidencias/familias/{s}/RONDAS.md).",
           "cab": {"cfo": "| País | Desde | Entidades del material | Rondas | Señales | Datos | La factura y su impuesto |",
                   "clo": "| País | Desde | Entidades del material | Rondas | Señales | Datos | La contratación pública |"},
           "ronda": "ronda {r}", "control": "control", "publica": "entidad pública",
           "ind": {"banca": "banca", "cooperativas": "cooperativas", "retail": "retail", "mineria": "minería"},
           "de": "{a} de {b}", "mas": " · {n} de más",
           "factura": "{emisor} · {clave} · {impuesto} del {iva} % ({fuentes})",
           "sin_publica": "Sin entidad pública: la regla de la garantía no está entre las fuentes verificadas",
           "sistema": "{sistema}", "gmin": "garantía mínima del {p} %", "gmax": "garantía hasta el {p} %",
           "gmaxj": "hasta el {p} % justificada", "gdesde": "garantía exigida desde {v}", "entrega": "garantía entregada en {d} días {t}",
           "pub": "publicación en {d} días {t}", "pubd": "{d} en la directa", "umbral": "sobre el umbral de la política",
           "habiles": "hábiles", "naturales": "naturales"},
    "en": {"archivo": "README.md", "titulo": "## The countries tested",
           "lead": "{n} countries, in the order they came in, with every entity of their material —one control, with no "
                   "seeded defect, in each country—. The signals and fields are those of each entity's latest run with "
                   "all its agents; the rounds also count the verifications. The entities, seeded defects and expected signals, in "
                   "[`EVIDENCIA.md`](../../tests/criterio-{s}/EVIDENCIA.md) (Spanish); every run with its cost and grade, in "
                   "[the family's rounds](../../tests/evidencias/familias/{s}/RONDAS.md).",
           "cab": {"cfo": "| Country | Since | Material entities | Rounds | Signals | Fields | The invoice and its tax |",
                   "clo": "| Country | Since | Material entities | Rounds | Signals | Fields | Public procurement |"},
           "ronda": "round {r}", "control": "control", "publica": "public entity",
           "ind": {"banca": "banking", "cooperativas": "cooperatives", "retail": "retail", "mineria": "mining"},
           "de": "{a} of {b}", "mas": " · {n} extra",
           "factura": "{emisor} · {impuesto} at {iva} % ({fuentes})",
           "sin_publica": "No public entity: the guarantee rule is not among the verified sources",
           "sistema": "{sistema}", "gmin": "minimum guarantee of {p} %", "gmax": "guarantee up to {p} %",
           "gmaxj": "up to {p} % when justified", "gdesde": "guarantee required from {v}", "entrega": "guarantee lodged within {d} {t} days",
           "pub": "published within {d} {t} days", "pubd": "{d} for direct awards", "umbral": "above the policy threshold",
           "habiles": "business", "naturales": "calendar"},
}


def _j(p: Path):
    return json.loads(p.read_text(encoding="utf-8"))


def tramo(numeros) -> str:
    """1, 2, 3, 5 → «1–3, 5»."""
    partes, ini, ant = [], None, None
    for n in sorted(set(numeros)):
        if ini is None:
            ini = ant = n
        elif n == ant + 1:
            ant = n
        else:
            partes.append(f"{ini}–{ant}" if ant != ini else str(ini))
            ini = ant = n
    if ini is not None:
        partes.append(f"{ini}–{ant}" if ant != ini else str(ini))
    return ", ".join(partes)


def corridas(sigla: str) -> list[dict]:
    """Cada corrida publicada: su ronda, su entidad del material y su calificación."""
    mat = RAIZ / "tests" / f"criterio-{sigla}" / "material"
    nombres = [e.name for e in mat.iterdir() if (e / "clave.json").is_file()]
    out = []
    for d in (RAIZ / "tests" / "evidencias" / "familias" / sigla).glob("ronda-*/*"):
        m = re.fullmatch(r"ronda-(\d+)", d.parent.name)
        if not m or not (d / "calificacion.json").is_file():
            continue
        ent = max((e for e in nombres if d.name == e or d.name.startswith(f"{e}-")), key=len, default=None)
        if not ent:
            continue
        k, c = _j(mat / ent / "clave.json"), _j(d / "calificacion.json")
        s = k["siembra"]
        sembrado = int(s) if isinstance(s, bool) else len(s) if isinstance(s, list) else sum(len(v) for v in s.values())
        out.append({"ronda": int(m.group(1)), "carpeta": d.name, "entidad": ent, "pais": k["pais"], "agentes": set(c["agentes"]),
                    "industria": k["industria"], "control": sembrado == 0 and k["industria"] != "publica",
                    "acertadas": c["senales"]["acertadas"], "esperadas": c["senales"]["esperadas"],
                    "de_mas": len(c["senales"]["de_mas"]), "bien": c["extraccion"]["bien"], "campos": c["extraccion"]["campos"]})
    return out


def propio(sigla: str, c: str, i: str) -> str:
    t, p = T[i], PAISES[c]
    pct = (lambda x: f"{x * 100:g}".replace(".", ",") if i == "es" else f"{x * 100:g}")
    if sigla == "cfo":
        f = p["factura"]
        return t["factura"].format(emisor=f["emisor"], clave=f["clave"], impuesto=f["impuesto"], iva=pct(f["iva"]), fuentes=", ".join(f["fuentes"]))
    r = p.get("contratacion_publica")
    if not r:
        return t["sin_publica"]
    g, pub, partes = r.get("garantia") or {}, r.get("publicacion") or {}, [r["sistema"]]
    if pub:
        x = t["pub"].format(d=pub["plazo"], t=t[pub["dias"]])
        partes.append(x + (f" ({t['pubd'].format(d=pub['plazo_directa'])})" if pub.get("plazo_directa") else ""))
    if "minimo" in g:
        partes.append(t["gmin"].format(p=pct(g["minimo"])) + (f", {t['umbral']}" if g.get("umbral") else ""))
    if "maximo" in g:
        partes.append(t["gmax"].format(p=pct(g["maximo"])) + (f", {t['gmaxj'].format(p=pct(g['maximo_justificado']))}" if g.get("maximo_justificado") else ""))
    if "exigida_desde" in g:
        partes.append(t["gdesde"].format(v=f"{g['exigida_desde']:,}".replace(",", " ")))
    if "entrega" in g:
        partes.append(t["entrega"].format(d=g["entrega"], t=t[g["dias"]]))
    fuentes = sorted({x.get("fuente") for x in (g, pub) if x.get("fuente")})
    return " · ".join(partes) + f" ({', '.join(fuentes)})"


def seccion(sigla: str, i: str) -> str:
    t, cs = T[i], corridas(sigla)
    primera = {}
    for x in cs:
        primera[x["pais"]] = min(primera.get(x["pais"], 99), x["ronda"])
    orden = sorted(primera, key=lambda c: (primera[c], list(PAISES).index(c)))
    filas = []
    for c in orden:
        de_c = [x for x in cs if x["pais"] == c]
        # La corrida más reciente de cada entidad con todos sus agentes: una verificación que repite a
        # uno solo deja ver ese agente, no la entidad, y no reemplaza la corrida completa.
        ultima = []
        for e in sorted({x["entidad"] for x in de_c}):
            de_e = [x for x in de_c if x["entidad"] == e]
            todos = set().union(*(x["agentes"] for x in de_e))
            ultima.append(max((x for x in de_e if x["agentes"] == todos), key=lambda x: (x["ronda"], x["carpeta"])))
        ents = sorted({(x["control"], x["industria"]) for x in de_c},
                      key=lambda v: (v[0], ORDEN.index(v[1]) if v[1] in ORDEN else len(ORDEN)))
        nombres = [t["control"] if ctl else t["publica"] if ind == "publica" else t["ind"].get(ind, ind) for ctl, ind in ents]
        a, b = sum(x["acertadas"] for x in ultima), sum(x["esperadas"] for x in ultima)
        mas = sum(x["de_mas"] for x in ultima)
        pais = PAISES[c]["nombre"][i]
        filas.append(f"| **{pais}** | {t['ronda'].format(r=primera[c])} | {', '.join(nombres)} | {tramo(x['ronda'] for x in de_c)} | "
                     f"{t['de'].format(a=a, b=b)}{t['mas'].format(n=mas) if mas else ''} | "
                     f"{t['de'].format(a=sum(x['bien'] for x in ultima), b=sum(x['campos'] for x in ultima))} | {propio(sigla, c, i)} |")
    return "\n".join([INICIO, t["titulo"], "", t["lead"].format(n=len(orden), s=sigla), "", t["cab"][sigla],
                      "|---|---|---|---|---:|---:|---|", *filas, FIN])


def escribir(check: bool) -> int:
    malos = []
    for sigla in ("cfo", "clo"):
        for i in ("es", "en"):
            p = RAIZ / "families" / f"criterio-{sigla}" / T[i]["archivo"]
            s = p.read_text(encoding="utf-8")
            if INICIO not in s or FIN not in s:
                malos.append(f"{p.relative_to(RAIZ)} no tiene la sección de los países probados")
                continue
            a, b = s.index(INICIO), s.index(FIN) + len(FIN)
            nuevo = s[:a] + seccion(sigla, i) + s[b:]
            if nuevo != s:
                if check:
                    malos.append(f"{p.relative_to(RAIZ)}: la tabla de los países probados no es la que sale de la evidencia")
                else:
                    p.write_text(nuevo, encoding="utf-8")
                    print(f"  escrito {p.relative_to(RAIZ)}")
    for m in malos:
        print(f"  ✗ {m}")
    if not malos:
        print("  los países probados de la CFO y de la CLO salen de la evidencia")
    return 1 if malos else 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true")
    sys.exit(escribir(ap.parse_args().check))
