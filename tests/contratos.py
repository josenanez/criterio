#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cada comando y cada skill contra su contrato, y el contrato contra el código.

    python3 tests/contratos.py

El contrato de cada plugin está en `plugins/<plugin>/contratos.json`: qué hace cada
comando, qué lee, qué muestra y escribe, qué skills aplica, qué acciones del script
llama y si su salida lleva cifras derivadas; y de cada skill, qué campo escribe y qué
señal alimenta. Vive fuera del comando para que el agente no lo cargue en cada corrida.

Esto nació de una semana en que ninguna falla fue de cálculo y todas fueron contratos
rotos entre piezas: un comando que no decía dónde estaba su entrada, un skill que
escribía un campo que ninguna regla leía, una regla que leía un campo que nadie
escribía, un comando que sumaba de cabeza lo que el script ya sabía sumar. Una prueba
de extremo a extremo los ve como «cifras malas»; esto los ve como lo que son.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
P = RAIZ / "plugins"
PLUGINS = {"criterio-portfolio": "portafolio.py", "criterio-project": "portafolio.py",
           "criterio-product": "producto.py"}
# Las acciones que calculan. Un comando cuya salida lleva cifras derivadas llama al menos
# una: si no, las cifras las hizo el modelo, que es lo que el diseño prohíbe.
CALCULO = {"compute", "impact", "diff", "index", "due", "overlap", "publish", "plan-lectura"}

fallas: list[tuple[str, str]] = []


def falla(regla: str, texto: str) -> None:
    fallas.append((regla, texto))


def acciones_cli(script: Path) -> set:
    t = script.read_text(encoding="utf-8")
    m = re.search(r'add_argument\("action", choices=\[(.*?)\]', t, re.S)
    return set(re.findall(r'"([a-z-]+)"', m.group(1))) if m else set()


def senales_emitidas() -> set:
    s = set()
    for f in (P / "criterio-portfolio/scripts/portafolio.py", P / "criterio-product/scripts/producto.py"):
        t = f.read_text(encoding="utf-8")
        s |= set(re.findall(r'alert\("([a-z_]+)"', t)) | set(re.findall(r'"signal": "([a-z_]+)"', t))
    return s


def claves_esquema() -> set:
    t = (P / "criterio-portfolio/skills/project-record/references/schema.yaml").read_text(encoding="utf-8")
    return set(re.findall(r"^([a-z_]+):", t, re.M))


contratos = {pl: json.loads((P / pl / "contratos.json").read_text(encoding="utf-8")) for pl in PLUGINS}
skills_contrato = {}
for pl, c in contratos.items():
    for nombre, s in c["skills"].items():
        skills_contrato[nombre] = (pl, s)

# ---------------------------------------------------------------- comandos
for pl, script in PLUGINS.items():
    cli = acciones_cli(P / pl / "scripts" / script)
    existentes = {f.stem for f in (P / pl / "commands").glob("*.md")}
    skills_dir = {d.name for d in (P / pl / "skills").iterdir() if d.is_dir()}
    cc = contratos[pl]["comandos"]
    for x in sorted(existentes - set(cc)):
        falla("C1 sin contrato", f"{pl}:{x}")
    for x in sorted(set(cc) - existentes):
        falla("C1 contrato sin comando", f"{pl}:{x}")
    nombrados = set()
    for cmd, k in sorted(cc.items()):
        f = P / pl / "commands" / f"{cmd}.md"
        if not f.is_file():
            continue
        t = f.read_text(encoding="utf-8")
        cuerpo = t.split("\n---\n", 1)[1]
        # C2 · skills
        citados = {s for s in skills_dir if re.search(r"\*\*" + re.escape(s) + r"\*\*|`" + re.escape(s) + r"`", cuerpo)}
        quiere = set(k["reglas"]["skills"])
        nombrados |= quiere
        for s in sorted(quiere - skills_dir):
            falla("C2 skill que el plugin no tiene", f"{pl}:{cmd} → {s}")
        for s in sorted((quiere & skills_dir) - citados):
            falla("C2 el comando no aplica un skill de su contrato", f"{pl}:{cmd} → {s}")
        for s in sorted(citados - quiere):
            falla("C2 el comando aplica un skill fuera de su contrato", f"{pl}:{cmd} → {s}")
        # C3 · acciones del script
        llamadas = set(re.findall(r'scripts/[a-z_]+\.py"? +([a-z][a-z-]*)', cuerpo))
        quiere = set(k["reglas"]["script"])
        for a in sorted(quiere - cli):
            falla("C3 acción que el script no tiene", f"{pl}:{cmd} → {a}")
        for a in sorted(quiere - llamadas):
            falla("C3 el comando no llama una acción de su contrato", f"{pl}:{cmd} → {a}")
        for a in sorted(llamadas - quiere):
            falla("C3 el comando llama una acción fuera de su contrato", f"{pl}:{cmd} → {a}")
        # C4 · cifras derivadas sin cálculo
        if k["reglas"]["calcula"] and not (set(k["reglas"]["script"]) & CALCULO):
            falla("C4 cifras derivadas sin acción de cálculo en el contrato", f"{pl}:{cmd}")
        # C5 · la corrida
        # Solo la llamada a `corrida`, con sus líneas de continuación: `ran --what sweep` es
        # la clave de la cadencia y es otra cosa.
        llamadas_corrida = [m.group(0) for m in
                            re.finditer(r'\bcorrida (?:[^\n]*\\\n)*[^\n]*', cuerpo)]
        whats = {w for c in llamadas_corrida for w in re.findall(r"--what ([a-z-]+)", c)}
        if "corrida" in k["reglas"]["script"]:
            if cmd not in whats:
                falla("C5 la corrida no se registra con el nombre del comando", f"{pl}:{cmd} → --what {', '.join(sorted(whats)) or '∅'}")
            for w in (sorted(whats - {cmd} - set(k["corrida"]["tambien"])) if cmd in whats else []):
                falla("C5 registra con un nombre ajeno", f"{pl}:{cmd} → --what {w}")
            if k["corrida"]["caso"] and not any("--caso" in c for c in llamadas_corrida):
                falla("C5 corrida sobre un caso sin --caso", f"{pl}:{cmd}")
    # C9 · skill que ningún comando nombra
    # Un skill que ningún comando nombra solo vale si el contrato dice cuándo lo carga
    # Claude por su descripción, y cómo se prueba así.
    for s in sorted(skills_dir - nombrados - set(contratos[pl].get("por_descripcion", {}))):
        falla("C9 skill que ningún comando de su plugin aplica", f"{pl} → {s}")

# ---------------------------------------------------------------- skills
esquema = claves_esquema()
emitidas = senales_emitidas()
alimentadas = set()
for pl in PLUGINS:
    for d in sorted((P / pl / "skills").iterdir()):
        if d.name not in skills_contrato:
            falla("C6 skill sin contrato", f"{pl} → {d.name}")
for nombre, (pl, s) in sorted(skills_contrato.items()):
    for campo in s["escribe"]:
        raiz = campo.split(".")[0].split("[")[0]
        if pl == "criterio-portfolio" and raiz not in esquema:
            falla("C7 el skill escribe un campo que el esquema no tiene", f"{nombre} → {campo}")
    for sen in s["alimenta"]:
        alimentadas.add(sen)
        if sen not in emitidas:
            falla("C8 el skill alimenta una señal que el código no emite", f"{nombre} → {sen}")
for sen in sorted(emitidas - alimentadas):
    falla("C8 señal que ningún skill alimenta", sen)

# ---------------------------------------------------------------- informe
if not fallas:
    total = sum(len(c["comandos"]) for c in contratos.values())
    print(f"  OK    {total} comandos y {len(skills_contrato)} skills cumplen su contrato")
    sys.exit(0)
por = {}
for r, t in fallas:
    por.setdefault(r, []).append(t)
for r in sorted(por):
    print(f"\n{r} · {len(por[r])}")
    for t in por[r]:
        print(f"  {t}")
print(f"\n{len(fallas)} contradicciones")
sys.exit(1)
