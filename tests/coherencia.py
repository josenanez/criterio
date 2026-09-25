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

DOCS = [RAIZ / "README.es.md", RAIZ / "README.md"]
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
    "stated_on": ("campo del esquema que el cálculo no lee. El compromiso reprogramado ya "
                  "se detecta, por `reschedules`; `stated_on` queda para cuando haga falta "
                  "la fecha en que se dijo cada cosa, no solo la que se prometió"),
    "fields_per_run": "presupuesto de preguntas declarado y no leído · portfolio-health",
    "daily_sweep": ("clave de cadencia declarada y no leída. El mecanismo ya existe —el índice "
                    "de documentos—; falta quién lo invoca sin que alguien abra una sesión"),
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

# Un comando no se documenta a sí mismo: su propio archivo sale de la búsqueda.
# La primera versión no lo excluía y daba por documentado cualquier comando nuevo,
# que es el falso negativo más caro que puede tener un verificador.
faltantes = {m for m in re.findall(r"`/([a-z][a-z-]{3,30})`", todo)} - comandos
for m in sorted(faltantes):
    decir(FALLA, f"la documentación promete /{m} y el comando no existe")

# ── 5 · cada señal documentada en su dueño ──────────────────────────────
print("\nCada señal en su dueño")
skill = (PLUGIN / "skills" / "portfolio-health" / "SKILL.md").read_text(encoding="utf-8")
sin_documentar = sorted(x for x in en_codigo if x not in skill)
for x in sin_documentar:
    decir(FALLA, f"`{x}` se calcula y no está en el skill portfolio-health")
if not sin_documentar:
    decir(OK, f"las {len(en_codigo)} señales están documentadas en portfolio-health")

sin_clave = sorted(t for t in en_codigo_th if t not in skill)
for t in sin_clave:
    decir(FALLA, f"el umbral `{t}` existe y el skill portfolio-health no dice qué señal gobierna")
if not sin_clave:
    decir(OK, f"los {len(en_codigo_th)} umbrales están documentados en portfolio-health")

# El inventario de comandos lo verifica scripts/validate_plugins.py, que exige que el
# README del plugin liste cada uno. Ese README es la promesa pública: el plugin viaja
# solo por el market. No se duplica el chequeo aquí.

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
