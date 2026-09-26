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

# Todos los plugins construidos, no solo criterio-pmo. Un comando de Samuel nombrado
# en la documentación de Vera tiene que resolver igual: la familia se lee junta.
CONSTRUIDOS = sorted(d for d in (RAIZ / "plugins").iterdir()
                     if d.is_dir() and (d / "commands").exists())

DOCS = [RAIZ / "README.es.md", RAIZ / "README.md"]
DOCS += sorted((RAIZ / "docs" / "agents").glob("*.md"))
for _p in CONSTRUIDOS:
    DOCS += sorted(_p.glob("*.md"))
    DOCS += sorted(_p.glob("skills/*/SKILL.md"))
    DOCS += sorted(_p.glob("commands/*.md"))

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
skills = {s.parent.name for d in CONSTRUIDOS for s in d.glob("skills/*/SKILL.md")}
comandos = {c.stem for d in CONSTRUIDOS for c in d.glob("commands/*.md")}
decir(OK, f"{len(comandos)} comandos · {len(skills)} skills")

for d in CONSTRUIDOS:
    for archivo in sorted(d.glob("commands/*.md")):
        cuerpo = archivo.read_text(encoding="utf-8")
        for ref in set(re.findall(r"\*\*([a-z][a-z-]{4,30})\*\*", cuerpo)):
            if ref.count("-") and ref not in skills and ref not in comandos:
                decir(FALLA, f"/{archivo.stem} invoca **{ref}** y no existe como skill")

# Un comando no se documenta a sí mismo: su propio archivo sale de la búsqueda.
# La primera versión no lo excluía y daba por documentado cualquier comando nuevo,
# que es el falso negativo más caro que puede tener un verificador.
# Las rutas del servidor se escriben igual que un comando —`/decisiones`— y no lo son.
# Se importan de donde están declaradas, para que una ruta nueva no obligue a nadie a
# escribir una excepción aquí, y un comando nuevo sí siga fallando.
SRV = PLUGIN / "scripts" / "servidor.py"
rutas = set()
if SRV.exists():
    sys.path.insert(0, str(SRV.parent))
    rutas = {r.lstrip("/").split("/")[0] for r in __import__("servidor").RUTAS}

faltantes = {m for m in re.findall(r"`/([a-z][a-z-]{3,30})`", todo)} - comandos - rutas
for m in sorted(faltantes):
    decir(FALLA, f"la documentación promete /{m} y el comando no existe")

# ── las imágenes que la documentación referencia ────────────────────────
# Una imagen rota en GitHub se ve como un icono gris y no la nota nadie hasta que
# alguien de afuera abre la página. Y con dos idiomas, la que se rompe es siempre
# la que uno no mira.
print("\nImágenes referenciadas")
rotas, total = [], 0
for md in sorted(list(RAIZ.glob("*.md")) + list(RAIZ.glob("plugins/*/*.md"))
                 + list(RAIZ.glob("docs/**/*.md"))):
    for ruta in re.findall(r"!\[[^\]]*\]\(([^)]+)\)", md.read_text(encoding="utf-8")):
        total += 1
        if not (md.parent / ruta).resolve().exists():
            rotas.append((md.relative_to(RAIZ), ruta))
for md, ruta in rotas:
    decir(FALLA, f"{md} referencia una imagen que no existe: {ruta}")
if not rotas:
    decir(OK, f"las {total} imágenes referenciadas existen")

# y que las dos versiones de idioma tengan las mismas piezas
img = RAIZ / "docs" / "img"
if (img / "es").exists() and (img / "en").exists():
    es = {p.name for p in (img / "es").glob("*.png")}
    en = {p.name for p in (img / "en").glob("*.png")}
    faltan = sorted((es - en) | (en - es))
    for x in faltan:
        decir(FALLA, f"la pieza {x} existe en un idioma y no en el otro")
    if not faltan:
        decir(OK, f"las {len(es)} piezas están en los dos idiomas")

# ── cada página del plugin, en los dos idiomas ──────────────────────────
# El plugin se distribuye solo y se enlaza desde los dos README raíz. Una página que
# existe en un idioma y no en el otro es un enlace roto para la mitad de quien llega,
# y ya pasó una vez: el README del plugin estuvo solo en castellano mientras el README
# raíz en inglés lo enlazaba.
print("\nCada página del plugin en los dos idiomas")
for plugin in sorted((RAIZ / "plugins").iterdir()):
    if not plugin.is_dir():
        continue
    # Mismo criterio que la política de valor: a un plugin declarado y sin construir
    # no se le exige. Se le exigirá el día que tenga comandos.
    if not (plugin / "commands").exists():
        decir(NOTA, f"{plugin.name} · declarado y sin construir, no se le exige")
        continue
    paginas = {f.name[:-len(".es.md")] for f in plugin.glob("*.es.md")}
    inglesas = {f.stem for f in plugin.glob("*.md") if not f.name.endswith(".es.md")}
    # ACCEPTANCE no tiene pareja a propósito: es un documento de trabajo, no una
    # página de producto. Si algún día la tiene, esta línea sobra.
    inglesas -= {"ACCEPTANCE"}
    huerfanas = sorted((paginas - inglesas) | (inglesas - paginas))
    for x in huerfanas:
        decir(FALLA, f"{plugin.name}/{x} existe en un idioma y no en el otro")
    if not huerfanas and paginas:
        decir(OK, f"{plugin.name} · {len(paginas)} páginas, las dos versiones de cada una")

# ── las cifras que la documentación afirma sobre las pruebas ────────────
# Un «treinta comprobaciones» escrito a mano envejece en la primera corrida que
# agrega una. Se compara contra lo que el selftest realmente hace.
print("\nLas cifras de las pruebas")
NUMEROS = {"quince": 15, "veinte": 20, "veinticinco": 25, "treinta": 30,
           "treinta y cinco": 35, "cuarenta": 40, "cuarenta y dos": 42,
           "doce": 12, "trece": 13, "catorce": 14, "dieciséis": 16,
           "fifteen": 15, "twenty": 20, "twenty-five": 25, "thirty": 30,
           "thirty-five": 35, "forty": 40, "forty-two": 42, "twelve": 12}
for script, paginas in (("servidor.py", ("SERVER.es.md", "SERVER.md")),):
    fuente = (PLUGIN / "scripts" / script)
    if not fuente.exists():
        continue
    reales = len(re.findall(r"^\s+ok\(", fuente.read_text(encoding="utf-8"), re.M))
    for nombre in paginas:
        doc = PLUGIN / nombre
        if not doc.exists():
            continue
        texto = doc.read_text(encoding="utf-8")
        dichos = set()
        for m in re.finditer(r"\b([\w-]+(?: y \w+)?) (?:comprobaciones|checks)\b", texto, re.I):
            crudo = m.group(1).lower()
            dichos.add(NUMEROS.get(crudo, int(crudo) if crudo.isdigit() else None))
        malos = sorted(str(d) for d in dichos if d is not None and d != reales)
        if malos:
            decir(FALLA, f"{nombre} dice {', '.join(malos)} comprobaciones y {script} hace {reales}")
        elif dichos:
            decir(OK, f"{nombre} · las {reales} comprobaciones que dice son las que hay")

# ── los scripts que dos plugins comparten ───────────────────────────────
# Una copia que se separó en silencio es peor que no tenerla: los dos plugins
# calcularían distinto sobre los mismos documentos y nadie sabría cuál creerle.
print("\nScripts compartidos entre plugins")
SINC = RAIZ / "scripts" / "sincronizar.py"
if SINC.exists():
    import subprocess
    r = subprocess.run([sys.executable, str(SINC), "--check"],
                       capture_output=True, text=True)
    for linea in r.stdout.splitlines():
        if linea.strip().startswith("igual"):
            decir(OK, linea.strip())
        elif "FALLA" in linea:
            decir(FALLA, linea.split("FALLA", 1)[1].strip())
    if r.returncode and "FALLA" not in r.stdout:
        decir(FALLA, "sincronizar.py --check falló sin decir por qué")
else:
    decir(NOTA, "no hay scripts compartidos todavía")

# ── la política de valor, de docs/design.md ─────────────────────────────
# Una pieza para nivel C dice cómo se instala, en cuánto da el primer resultado, y
# qué nunca hace. Sin esas tres, no la leen: la confianza es la puerta y el tiempo
# hasta el primer resultado es el argumento.
print("\nLa política de valor en el README de cada plugin")
EXIGIDO = {
    "cómo se instala": ("## Instalar", "## Instalación", "## Install"),  # noqa: E501
    "el primer resultado": ("primeros quince minutos", "primer resultado", "first result",
                            "first fifteen minutes"),
    "lo que nunca hace": ("Lo que nunca hace", "never does"),
}
for plugin in sorted(p for p in (RAIZ / "plugins").iterdir() if p.is_dir()):
    if not (plugin / "commands").exists():
        decir(NOTA, f"{plugin.name} · declarado y sin construir, no se le exige")
        continue
    # los dos idiomas, y cada uno tiene que cumplir la política por su cuenta
    for nombre, idioma in (("README.md", "en"), ("README.es.md", "es")):
        readme = plugin / nombre
        if not readme.exists():
            decir(FALLA, f"{plugin.name} · falta {nombre}")
            continue
        cuerpo = readme.read_text(encoding="utf-8")
        faltan = [q for q, marcas in EXIGIDO.items() if not any(m in cuerpo for m in marcas)]
        for q in faltan:
            decir(FALLA, f"{plugin.name}/{nombre} · no dice {q}")
        # y las imágenes de su propio idioma: una página en inglés con figuras en
        # español es el error que nadie nota porque nadie relee la que no es la suya
        otro = "es" if idioma == "en" else "en"
        if f"docs/img/{otro}/" in cuerpo:
            decir(FALLA, f"{plugin.name}/{nombre} · usa imágenes de docs/img/{otro}/")
            faltan.append("idioma")
        if not faltan:
            decir(OK, f"{plugin.name}/{nombre} · completo y con sus propias imágenes")

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

# El informe imprime el nombre de cada señal. Una señal nueva sin nombre en castellano
# no rompe nada: sale la clave en inglés, en un informe que va a un comité. Por eso
# también es dueño, y también se verifica.
INFORME = PLUGIN / "scripts" / "informe.py"
if INFORME.exists():
    # Se importa en vez de leerse con una expresión regular: la tabla es un dato del
    # programa, y leerla como texto falla en silencio el día que alguien pone dos
    # entradas en un renglón.
    sys.path.insert(0, str(INFORME.parent))
    nombrados = set(__import__("informe").NOMBRES)
    sin_nombre = sorted(x for x in en_codigo if x not in nombrados)
    for x in sin_nombre:
        decir(FALLA, f"`{x}` se calcula y el informe no sabe cómo decirlo en castellano")
    if not sin_nombre:
        decir(OK, f"las {len(en_codigo)} señales tienen nombre en el informe")
else:
    decir(FALLA, "falta plugins/criterio-pmo/scripts/informe.py")

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
