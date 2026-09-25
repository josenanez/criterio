# -*- coding: utf-8 -*-
"""Verifica que la documentación y el código digan lo mismo.

    python3 tests/coherencia.py

Este proyecto promete que cada comando y cada umbral están escritos y se pueden
auditar. La forma en que esa promesa se rompe no es que el código falle: es que
la documentación describa una señal que nadie calcula, un umbral que no existe, o
un skill que no está. Eso es lo que se verifica aquí.

Falla (exit 1) cuando la documentación afirma algo que el código no sostiene.
Reporta sin fallar lo que el código declara y no usa, que es información útil y
no una inconsistencia.
"""
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).parent.parent
PLUGIN = RAIZ / "plugins" / "criterio-pmo"
PMO = PLUGIN / "scripts" / "pmo.py"

DOCS = [RAIZ / "README.es.md", RAIZ / "README.md",
        RAIZ / "capabilities" / "pmo.es.md", RAIZ / "capabilities" / "pmo.md"]
DOCS += sorted((RAIZ / "docs" / "agents").glob("*.md"))
DOCS += sorted(PLUGIN.glob("*.md"))
DOCS += sorted(PLUGIN.glob("skills/*/SKILL.md"))
DOCS += sorted(PLUGIN.glob("commands/*.md"))

OK, FALLA, NOTA = "OK   ", "FALLA", "nota "
fallas = 0

# Nombres que la documentación usa y el código todavía no sostiene, con el lugar donde
# eso está declarado. No fallan: están dichos. Pero un nombre nuevo que aparezca en la
# documentación sin entrar aquí sí falla, y ese es el punto — la lista obliga a declarar
# el hueco en vez de dejarlo pasar.
PENDIENTES = {
    "source_kind": "decisión de esquema abierta · docs/agents/README.md",
    "source_missing": "señal por construir · docs/agents/pmo.md",
    "stated_on": ("campo del esquema que el cálculo no lee · es lo que falta para detectar "
                  "el compromiso reprogramado · docs/agents/project-manager.md"),
    "no_declarada": ("valor del esquema para un compromiso sin fecha · el cálculo lo ignora "
                     "y no lo cuenta, así que un compromiso sin fecha es invisible"),
    "fields_per_run": "presupuesto de preguntas declarado y no leído · portfolio-health",
}


def decir(marca, texto):
    global fallas
    if marca == FALLA:
        fallas += 1
    print(f"  {marca} {texto}")


codigo = PMO.read_text(encoding="utf-8")
texto_docs = {d: d.read_text(encoding="utf-8") for d in DOCS if d.exists()}
todo = "\n".join(texto_docs.values())

# ── 1 · señales ───────────────────────────────────────────────────────────
print("\nSeñales")
en_codigo = set(re.findall(r'alert\("([a-z_]+)"', codigo))
decir(OK, f"{len(en_codigo)} señales se calculan: {', '.join(sorted(en_codigo))}")

# Un nombre en backticks puede ser una señal, un campo de la salida o una clave del
# esquema. Solo es una inconsistencia si no aparece en NINGUNA parte de pmo.py: si
# está, el código lo sostiene, aunque no sea una alerta. Esa distinción importa —
# `has_baseline` y `approved_without_new_baseline` son campos, no señales, y tratarlos
# como señales inexistentes sería el verificador gritando lobo.
citados = {s for s in re.findall(r"`([a-z][a-z_]{3,40})`", todo) if "_" in s}
ausentes = sorted(s for s in citados if s not in codigo)
inventados = [s for s in ausentes if s not in PENDIENTES]
if inventados:
    for s in inventados:
        decir(FALLA, f"la documentación nombra `{s}`, no aparece en pmo.py y no está "
                     f"declarado como pendiente")
else:
    decir(OK, f"los {len(citados) - len(ausentes)} nombres técnicos citados existen en el código")

declarados_pend = [s for s in ausentes if s in PENDIENTES]
if declarados_pend:
    print("\nDeclarado como pendiente")
    for s in declarados_pend:
        decir(NOTA, f"`{s}` — {PENDIENTES[s]}")

# ── 2 · umbrales ──────────────────────────────────────────────────────────
print("\nUmbrales")
bloque = re.search(r"DEFAULT_THRESHOLDS = \{(.*?)\}", codigo, re.S).group(1)
en_codigo_th = set(re.findall(r'"([a-z_]+)":', bloque))
decir(OK, f"{len(en_codigo_th)} umbrales por defecto: {', '.join(sorted(en_codigo_th))}")

candidatos = set(re.findall(r"`(silent_days|variance_\w+|committed_pct|stale_\w+|"
                            r"declaration_\w+|rebaseline_\w+)`", todo)) - en_codigo
huerfanos = sorted(t for t in candidatos if t not in en_codigo_th)
for th in huerfanos:
    decir(FALLA, f"la documentación nombra el umbral `{th}` y no existe")
if not huerfanos:
    decir(OK, "todo umbral nombrado en la documentación existe")

# ── 3 · configuración declarada y no leída ────────────────────────────────
print("\nConfiguración")
cfg = json.loads((PLUGIN / "scripts" / "config.example.json").read_text(encoding="utf-8"))


def hojas(nodo, ruta=""):
    if isinstance(nodo, dict):
        for k, v in nodo.items():
            yield from hojas(v, f"{ruta}.{k}" if ruta else k)
    else:
        yield ruta


sin_leer = [r for r in hojas(cfg) if r.split(".")[-1] not in codigo]
if sin_leer:
    decir(NOTA, f"{len(sin_leer)} claves declaradas que ninguna línea de código lee:")
    for r in sin_leer:
        print(f"         {r}")
else:
    decir(OK, "toda clave de la configuración se lee en algún punto")

# ── 4 · comandos y skills ─────────────────────────────────────────────────
print("\nComandos y skills")
skills = {p.parent.name for p in PLUGIN.glob("skills/*/SKILL.md")}
comandos = {p.stem for p in PLUGIN.glob("commands/*.md")}
decir(OK, f"{len(comandos)} comandos · {len(skills)} skills")

for cmd in sorted(comandos):
    cuerpo = (PLUGIN / "commands" / f"{cmd}.md").read_text(encoding="utf-8")
    for ref in set(re.findall(r"\*\*([a-z][a-z-]{4,30})\*\*", cuerpo)):
        if ref.count("-") and ref not in skills and ref not in comandos:
            decir(FALLA, f"/{cmd} invoca **{ref}** y no existe como skill")

huerfanos = [c for c in sorted(comandos) if f"/{c}" not in todo]
for c in huerfanos:
    decir(FALLA, f"/{c} no está documentado en ninguna hoja ni capacidad")
if not huerfanos:
    decir(OK, "todo comando aparece documentado")

nombrados = set(re.findall(r"/([a-z][a-z-]{3,30})\b", todo)) & {f"{c}" for c in comandos}
faltantes = {m for m in re.findall(r"`/([a-z][a-z-]{3,30})`", todo)} - comandos
for m in sorted(faltantes):
    decir(FALLA, f"la documentación promete /{m} y el comando no existe")

# ── 5 · el conteo del selftest ────────────────────────────────────────────
print("\nSelftest")
cuerpo = codigo.split("checks = [")[1].split("\n    ]")[0]
n = len(re.findall(r'^        \("', cuerpo, re.M))
decir(OK, f"{n} resultados conocidos en el selftest")
declarados = []
for ruta, cuerpo_doc in texto_docs.items():
    for d in re.findall(r"(\d+) (?:resultados conocidos|known results)", cuerpo_doc):
        declarados.append((ruta.relative_to(RAIZ), int(d)))
for ruta, d in declarados:
    if d != n:
        decir(FALLA, f"{ruta} dice {d} resultados conocidos y hay {n}")
if declarados and all(d == n for _, d in declarados):
    decir(OK, f"el número correcto está declarado en {len(declarados)} documentos")
elif not declarados:
    decir(NOTA, "ningún documento declara cuántos resultados tiene el selftest")

# ── 6 · lo que solo vive en markdown ──────────────────────────────────────
print("\nReglas que la documentación afirma y el código no implementa")
for nombre, patron, donde in [
    ("el hash de documentos", r"\bhash\b", "portfolio-scan.md y project-record"),
    ("documents_seen", r"documents_seen", "el esquema y portfolio-scan.md"),
]:
    if re.search(patron, codigo):
        decir(OK, f"{nombre} se implementa en pmo.py")
    else:
        decir(NOTA, f"{nombre} solo existe en markdown ({donde}); el modelo tendría que "
                    f"calcularlo por su cuenta")

print(f"\n{'coherente' if not fallas else f'{fallas} INCONSISTENCIAS'}")
sys.exit(0 if not fallas else 1)
