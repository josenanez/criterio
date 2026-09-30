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
PLUGIN = RAIZ / "plugins" / "criterio-portfolio"
PMO = PLUGIN / "scripts" / "portafolio.py"
PRODUCT = RAIZ / "plugins" / "criterio-product"
PRODUCTO = PRODUCT / "scripts" / "producto.py"

# Todos los plugins construidos, no solo criterio-portfolio. Un comando de Samuel nombrado
# en la documentación de Vera tiene que resolver igual: la familia se lee junta.
CONSTRUIDOS = sorted(d for d in (RAIZ / "plugins").iterdir()
                     if d.is_dir() and (d / "commands").exists())

# Las hojas de diseño viven dentro de su plugin desde que dejaron docs/agents/: cada
# agente viaja con la suya, y el enlace que su README promete resuelve también en el
# equipo de quien instaló el plugin, no solo en GitHub.
DOCS = [RAIZ / "README.es.md", RAIZ / "README.md"]
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


# «El código» son las dos capas de aritmética de la familia. Un requerimiento no tiene
# línea base ni presupuesto, así que Alba calcula aparte — y un nombre suyo citado en la
# documentación tiene que resolver igual que uno de Vera. Leer solo portafolio.py dejaba a la
# mitad de la familia sin verificar, que es el falso negativo que este archivo existe
# para no tener.
codigo = PMO.read_text(encoding="utf-8")
if PRODUCTO.exists():
    codigo += "\n" + PRODUCTO.read_text(encoding="utf-8")
texto_docs = {d: d.read_text(encoding="utf-8") for d in DOCS if d.exists()}
todo = "\n".join(texto_docs.values())

# ── 1 · señales ───────────────────────────────────────────────────────────
print("\nSeñales")
# Las de Vera y las de Alba se cuentan aparte: cada familia tiene su dueño
# documental, y mezclarlas haría que una señal de producto pareciera faltar en el
# skill de portafolio.
en_codigo = set(re.findall(r'alert\("([a-z_]+)"', PMO.read_text(encoding="utf-8")))
decir(OK, f"{len(en_codigo)} señales de portafolio se calculan: {', '.join(sorted(en_codigo))}")
en_producto = set()
if PRODUCTO.exists():
    fuente_prod = PRODUCTO.read_text(encoding="utf-8")
    en_producto = (set(re.findall(r'alert\("([a-z_]+)"', fuente_prod))
                   | set(re.findall(r'"signal": "([a-z_]+)"', fuente_prod)))
    decir(OK, f"{len(en_producto)} señales de producto: {', '.join(sorted(en_producto))}")

# Un nombre en backticks puede ser una señal, un campo de la salida o una clave del
# esquema. Solo es una inconsistencia si no aparece en NINGUNA parte de portafolio.py: si
# está, el código lo sostiene, aunque no sea una alerta. Esa distinción importa —
# `has_baseline` y `approved_without_new_baseline` son campos, no señales, y tratarlos
# como señales inexistentes sería el verificador gritando lobo.
citados = {s for s in re.findall(r"`([a-z][a-z_]{3,40})`", todo) if "_" in s}
ausentes = sorted(s for s in citados if s not in codigo)
inventados = [s for s in ausentes if s not in PENDIENTES]
if inventados:
    for s in inventados:
        decir(FALLA, f"la documentación nombra `{s}`, no aparece en portafolio.py y no está "
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
    # DISENO no tiene pareja a propósito: es un documento de trabajo, no una página de
    # producto. El diseño se discute en castellano y la pareja en inglés duplicaría la
    # rotación mientras el diseño todavía se mueve. Lo que la organización que instala
    # necesita saber está en el README, y ese sí va en los dos idiomas.
    # ACCEPTANCE sigue aquí por los plugins declarados y sin construir, que no tienen
    # hoja de diseño en la que fundirlo.
    inglesas -= {"ACCEPTANCE"}
    paginas -= {"DISENO"}
    huerfanas = sorted((paginas - inglesas) | (inglesas - paginas))
    for x in huerfanas:
        decir(FALLA, f"{plugin.name}/{x} existe en un idioma y no en el otro")
    if not huerfanas and paginas:
        decir(OK, f"{plugin.name} · {len(paginas)} páginas, las dos versiones de cada una")

# ── las cifras que la documentación afirma sobre las pruebas ────────────
# Un «treinta comprobaciones» escrito a mano envejece en la primera corrida que
# agrega una. Se compara contra lo que el selftest realmente hace.
print("\nLas cifras de las pruebas")
NUMEROS = {"diez": 10, "once": 11, "dieciocho": 18, "eighteen": 18, "diecisiete": 17, "dieciocho": 18, "diecinueve": 19,
           "ten": 10, "eleven": 11, "seventeen": 17, "eighteen": 18, "nineteen": 19,
           "quince": 15, "veinte": 20, "veinticinco": 25, "treinta": 30,
           "treinta y cinco": 35, "cuarenta": 40, "cuarenta y dos": 42,
           "doce": 12, "trece": 13, "catorce": 14, "dieciséis": 16,
           "fifteen": 15, "twenty": 20, "twenty-five": 25, "thirty": 30,
           "thirty-five": 35, "forty": 40, "forty-two": 42, "twelve": 12}
for duenio, script, paginas in ((PLUGIN, "servidor.py", ("SERVER.es.md", "SERVER.md")),
                                (PRODUCT, "producto.py", ("README.es.md", "README.md"))):
    fuente = (duenio / "scripts" / script)
    if not fuente.exists():
        continue
    reales = len(re.findall(r"^\s+ok\(", fuente.read_text(encoding="utf-8"), re.M))
    for nombre in paginas:
        doc = duenio / nombre
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

# La cifra de señales que un skill o un README afirma, contra las que el código emite.
# Es la misma clase de defecto que la cifra de comprobaciones y se rompió igual: el skill
# de Vera decía «las dieciocho señales» cuando ya eran diecinueve, y la documentación
# pública repetía el número.
print("\nLas cifras de señales")
for fuente, cuenta, paginas in (
    (PMO, len(en_codigo), [PLUGIN / "skills" / "portfolio-health" / "SKILL.md",
                           PLUGIN / "README.es.md", PLUGIN / "README.md"]),
    (PRODUCTO, len(en_producto), [PRODUCT / "skills" / "product-health" / "SKILL.md",
                                  PRODUCT / "README.es.md", PRODUCT / "README.md"]),
):
    if not fuente.exists() or not cuenta:
        continue
    for doc in paginas:
        if not doc.exists():
            continue
        cuerpo = doc.read_text(encoding="utf-8")
        dichos = set()
        for m in re.finditer(r"\b([\w-]+) (?:señales|signals)\b", cuerpo, re.I):
            crudo = m.group(1).lower()
            n = NUMEROS.get(crudo, int(crudo) if crudo.isdigit() else None)
            if n is not None:
                dichos.add(n)
        malos = sorted(str(d) for d in dichos if d != cuenta)
        if malos:
            decir(FALLA, f"{doc.name} dice {', '.join(malos)} señales y el código emite {cuenta}")
        elif dichos:
            decir(OK, f"{doc.relative_to(RAIZ)} · las {cuenta} señales que dice son las que hay")

# La cifra de skills distintos que la página de la familia afirma. Misma clase de
# defecto: se escribió «quince» sobre una tabla de dieciocho filas.
print("\nLa cifra de skills de la familia")
distintos = len(skills)
for nombre in ("README.es.md", "README.md"):
    pagina = PLUGIN / nombre
    if not pagina.exists():
        continue
    cuerpo = pagina.read_text(encoding="utf-8")
    dichos = set()
    for m in re.finditer(r"\b([\w-]+) (?:skills distintos|distinct skills)\b", cuerpo, re.I):
        crudo = m.group(1).lower()
        n = NUMEROS.get(crudo, int(crudo) if crudo.isdigit() else None)
        if n is not None:
            dichos.add(n)
    malos = sorted(str(x) for x in dichos if x != distintos)
    if malos:
        decir(FALLA, f"{nombre} dice {', '.join(malos)} skills distintos y hay {distintos}")
    elif dichos:
        decir(OK, f"{nombre} · los {distintos} skills distintos que dice son los que hay")

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
    # La frontera puede estar como sección propia o como la segunda mitad de «para qué
    # sirve». Lo que la política exige es que esté dicha, no dónde.
    "lo que nunca hace": ("Lo que nunca hace", "never does",
                          "para qué no sirve", "what it is not for"),
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
    decir(FALLA, "falta plugins/criterio-portfolio/scripts/informe.py")

# Mismo criterio del lado de Alba: su dueño documental es product-health, y una señal
# que se calcula y no está ahí es una señal que nadie va a saber leer.
if en_producto:
    print("\nCada señal de producto en su dueño")
    hoja = (PRODUCT / "skills" / "product-health" / "SKILL.md")
    if not hoja.exists():
        decir(FALLA, "falta el skill product-health, que es el dueño de las señales de producto")
    else:
        cuerpo = hoja.read_text(encoding="utf-8")
        faltan_s = sorted(x for x in en_producto if x not in cuerpo)
        for x in faltan_s:
            decir(FALLA, f"`{x}` se calcula y no está en el skill product-health")
        if not faltan_s:
            decir(OK, f"las {len(en_producto)} señales están documentadas en product-health")
        bloque_p = re.search(r"DEFAULT_THRESHOLDS = \{(.*?)\n\}",
                             PRODUCTO.read_text(encoding="utf-8"), re.S).group(1)
        umbrales_p = set(re.findall(r'"([a-z_]+)":', bloque_p))
        faltan_u = sorted(u for u in umbrales_p if u not in cuerpo)
        for u in faltan_u:
            decir(FALLA, f"el umbral `{u}` existe y product-health no dice qué señal gobierna")
        if not faltan_u:
            decir(OK, f"los {len(umbrales_p)} umbrales están documentados en product-health")

# La página de la familia no repite los comandos de nadie: nombra a cada agente y lleva
# a su página, que es donde está su detalle. Lo que se verifica es que desde la familia se
# llegue a los cuatro —los tres agentes y el servidor—, porque una página de familia desde
# la que no se puede navegar es un índice roto.
print("\nDesde la familia se llega a cada agente")
# Tres niveles, y cada uno enlaza al siguiente: el proyecto lista sus familias, la familia
# lleva a sus agentes y a su servidor, y cada agente se lee solo. Se colapsaron dos veces
# —primero la familia dentro de un agente, después la familia dentro del proyecto— y las
# dos veces el síntoma fue el mismo: quien buscaba un nivel aterrizaba en otro.
FAMILIA = RAIZ / "families" / "criterio-pmo"

DESTINOS = {"es": ["../../plugins/criterio-portfolio/README.es.md",
                   "../../plugins/criterio-portfolio/SERVER.es.md",
                   "../../plugins/criterio-project/README.es.md",
                   "../../plugins/criterio-product/README.es.md"],
            "en": ["../../plugins/criterio-portfolio/README.md",
                   "../../plugins/criterio-portfolio/SERVER.md",
                   "../../plugins/criterio-project/README.md",
                   "../../plugins/criterio-product/README.md"]}
for nombre, idioma in (("README.es.md", "es"), ("README.md", "en")):
    pagina = FAMILIA / nombre
    if not pagina.exists():
        continue
    cuerpo = pagina.read_text(encoding="utf-8")
    faltan = [d for d in DESTINOS[idioma] if f"]({d})" not in cuerpo]
    for d in DESTINOS[idioma]:
        destino = (FAMILIA / d).resolve()
        if not destino.exists():
            faltan.append(f"{d} no existe")
    if faltan:
        decir(FALLA, f"{nombre} no lleva a {', '.join(faltan)}")
    else:
        decir(OK, f"{nombre} · lleva a los tres agentes y al servidor")

print("\nDesde el proyecto se llega a cada familia")
for nombre, suf in (("README.es.md", "es.md"), ("README.md", "md")):
    pagina = RAIZ / nombre
    if not pagina.exists():
        continue
    cuerpo = pagina.read_text(encoding="utf-8")
    destino = f"families/criterio-pmo/README.{suf}"
    if f"]({destino})" in cuerpo:
        decir(OK, f"{nombre} · lleva a criterio-pmo")
    else:
        decir(FALLA, f"{nombre} no lleva a {destino}")

# Y cada agente lista sus propios comandos en su propia página, porque esa página se lee
# sola: alguien puede instalar un agente sin la familia.
print("\nCada agente lista lo suyo en su página")
PROPIAS = {"criterio-portfolio": ["README.es.md", "README.md"],
           "criterio-project": ["README.es.md", "README.md"],
           "criterio-product": ["README.es.md", "README.md"]}
for d in CONSTRUIDOS:
    suyos = sorted(c.stem for c in d.glob("commands/*.md"))
    for nombre in PROPIAS.get(d.name, []):
        pagina = d / nombre
        if not pagina.exists():
            decir(FALLA, f"{d.name}/{nombre} no existe")
            continue
        cuerpo = pagina.read_text(encoding="utf-8")
        # Con el prefijo del plugin, que es la única forma que resuelve en una sesión.
        faltan = [c for c in suyos if f"`/{d.name}:{c}`" not in cuerpo]
        if faltan:
            decir(FALLA, f"{d.name}/{nombre} no lista {', '.join(faltan)}")
        else:
            decir(OK, f"{d.name}/{nombre} · sus {len(suyos)} comandos")

# Y desde la página de la familia se tiene que poder llegar al análisis de pruebas de cada
# agente, en markdown. Un resultado que solo existe en HTML no se ve en GitHub, y uno que no
# está enlazado desde donde la gente llega es uno que nadie abre.
print("\nEl análisis de pruebas de cada agente, alcanzable")
for nombre in ("README.es.md", "README.md"):
    pagina = FAMILIA / nombre
    if not pagina.exists():
        continue
    cuerpo = pagina.read_text(encoding="utf-8")
    faltan = []
    for d in CONSTRUIDOS:
        destino = RAIZ / "tests" / d.name / "RESULTADOS.md"
        if not destino.exists():
            faltan.append(f"{d.name} no tiene RESULTADOS.md")
        elif f"tests/{d.name}/RESULTADOS.md" not in cuerpo:
            faltan.append(f"{d.name} no está enlazado")
    if faltan:
        decir(FALLA, f"{nombre} · {', '.join(faltan)}")
    else:
        decir(OK, f"{nombre} · los {len(CONSTRUIDOS)} análisis de pruebas, en markdown")

# El inventario de comandos lo verifica scripts/validate_plugins.py, que exige que el
# README del plugin liste cada uno. Ese README es la promesa pública: el plugin viaja
# solo por el market. No se duplica el chequeo aquí.

# ── que todo enlace interno resuelva ────────────────────────────────────
# Se escribió a mano dos veces durante la reestructuración, y las dos veces encontró
# algo. Un enlace roto en el README es lo primero que ve quien llega, y no lo atrapaba
# ninguna puerta: el markdown no se compila, así que nada falla hasta que alguien hace
# clic. Se verifica el archivo y también el ancla, porque mover una sección deja el
# enlace apuntando a una página que existe y a un sitio que ya no.
print("\nQue todo enlace interno resuelva")
import unicodedata

def _ancla(titulo: str) -> str:
    t = titulo.strip().lower()
    t = re.sub(r"[^\w\s-]", "", t, flags=re.UNICODE)
    return re.sub(r"\s+", "-", t)


rotos, revisados = [], 0
for pagina in DOCS:
    if not pagina.exists():
        continue
    cuerpo = pagina.read_text(encoding="utf-8")
    for m in re.finditer(r"\[[^\]]*\]\(([^)\s]+)\)", cuerpo):
        destino_txt = m.group(1)
        if destino_txt.startswith(("http:", "https:", "mailto:", "#")):
            continue
        revisados += 1
        archivo, _, anc = destino_txt.partition("#")
        destino = (pagina.parent / archivo).resolve() if archivo else pagina
        rel = pagina.relative_to(RAIZ)
        if not destino.exists():
            rotos.append(f"{rel} → {destino_txt} · no existe")
            continue
        if anc and destino.suffix == ".md":
            anclas = {_ancla(l.lstrip("#")) for l in
                      destino.read_text(encoding="utf-8").splitlines()
                      if l.startswith("#")}
            if anc not in anclas:
                rotos.append(f"{rel} → {destino_txt} · el ancla no está")
if rotos:
    for r in rotos[:12]:
        decir(FALLA, r)
    if len(rotos) > 12:
        decir(FALLA, f"y {len(rotos) - 12} más")
else:
    decir(OK, f"los {revisados} enlaces internos de la documentación resuelven")


# ── las tres páginas de agente, con el mismo esqueleto ──────────────────
# Era la queja, y tenía razón: las tres páginas se habían escrito en momentos distintos y
# la tercera sección se llamaba distinto en cada una, así que no se podían comparar. Quien
# entraba a dos de ellas no sabía si la diferencia era del agente o del redactor.
#
# Seis secciones, y las seis idénticas en las tres páginas: ya no varía ninguna. Están
# cortadas por las preguntas de quien llega y en el orden en que las hace —qué es, qué
# hace, para qué sirve, cómo se instala, cómo se lleva con los otros dos, y si está
# probado— y no por cómo está hecho el software por dentro.
#
# Antes eran once, cortadas por el software, y aunque eran las mismas en las tres se
# llenaban desigual: nada obligaba a que cada casilla pesara lo mismo.
#
# Hubo una segunda sección que declaraba dónde se superponía cada agente con los otros dos, y
# se quitó: que dos roles hagan la misma tarea en momentos distintos no es una superposición
# que haya que justificar, es la tarea. Explicarlo creaba el conflicto que pretendía evitar.
print("\nLas tres páginas de agente, con el mismo esqueleto")
import fnmatch

ESQUELETO = {
    "es": ["Qué es", "Qué hace", "Para qué sirve", "Instalación y configuración",
           "Trabajo en equipo", "Pruebas"],
    "en": ["What it is", "What it does", "What it is for", "Installing and configuring",
           "Working with the others", "Tests"],
}

AGENTES = [(PLUGIN, "README.es.md", "README.md"),
           (RAIZ / "plugins" / "criterio-project", "README.es.md", "README.md"),
           (PRODUCT, "README.es.md", "README.md")]
for carpeta, es, en in AGENTES:
    for nombre, idioma in ((es, "es"), (en, "en")):
        pagina = carpeta / nombre
        if not pagina.exists():
            decir(FALLA, f"{carpeta.name}/{nombre} no existe")
            continue
        vistos = [l[3:].strip() for l in pagina.read_text(encoding="utf-8").splitlines()
                  if l.startswith("## ")]
        esperado = ESQUELETO[idioma]
        if len(vistos) != len(esperado):
            decir(FALLA, f"{carpeta.name}/{nombre} tiene {len(vistos)} secciones y el "
                         f"esqueleto son {len(esperado)}")
            continue
        malas = [f"«{v}» donde va «{e}»"
                 for v, e in zip(vistos, esperado) if not fnmatch.fnmatch(v, e)]
        if malas:
            decir(FALLA, f"{carpeta.name}/{nombre} · {'; '.join(malas)}")
        else:
            decir(OK, f"{carpeta.name}/{nombre} · las {len(esperado)} secciones, en orden")


# ── las capturas del portal contra el código que las produjo ────────────
# Era un cabo suelto declarado: «si cambia el diseño de las páginas, estas capturas
# envejecen, y no hay nada que lo detecte solo». Ya pasó una vez —las capturas siguieron
# diciendo «Plomada» meses después del cambio de nombre—, así que ahora se detecta.
#
# Es `nota` y no `FALLA` a propósito: volver a tomarlas necesita un navegador, y hacer
# que la puerta verde dependa de un navegador rompería la propiedad que hace auditable a
# este repositorio. Lo que se gana es que la podredumbre se vea, no que pare la corrida.
print("\nLas capturas del portal")
SELLO = RAIZ / "docs" / "img" / "portal" / "captura.json"
if SELLO.exists():
    import hashlib
    sello = json.loads(SELLO.read_text(encoding="utf-8"))
    viejas = []
    for nombre, firma in sello.get("tomadas_con", {}).items():
        fuente = PLUGIN / "scripts" / nombre
        if not fuente.exists():
            viejas.append(f"{nombre} ya no existe")
        elif hashlib.sha256(fuente.read_bytes()).hexdigest()[:16] != firma:
            viejas.append(nombre)
    if viejas:
        decir(NOTA, f"se tomaron con otra versión de {', '.join(viejas)} · "
                    f"rehacerlas con docs/img/portal/README.md")
    else:
        decir(OK, "se tomaron con el código que hay hoy")
else:
    decir(NOTA, "las capturas del portal no dicen con qué versión se tomaron")

print("\nReglas que la documentación afirma y el código no implementa")
for nombre, patron, donde in [
    ("el hash de documentos", r"\bhash\b", "portfolio-scan.md y project-record"),
    ("documents_seen", r"documents_seen", "el esquema y portfolio-scan.md"),
]:
    if re.search(patron, codigo):
        decir(OK, f"{nombre} se implementa en portafolio.py")
    else:
        decir(NOTA, f"{nombre} solo existe en markdown ({donde}); el modelo tendría que "
                    f"calcularlo por su cuenta")

# ── que el comando documentado sea el que se puede escribir ───────────────
# Claude Code nombra el comando de un plugin como `/<plugin>:<comando>`, siempre y sin
# forma de evitarlo. Las páginas decían `/portfolio-setup`, que no resuelve: lo primero
# que hace quien descarga el plugin es escribir lo que dice el README, y le fallaba en el
# minuto uno. Ninguna puerta lo atrapaba porque el markdown no se ejecuta.
print("\nQue el comando documentado sea el que se puede escribir")
import subprocess as _sp

MAPA_CMD = {f.stem: plug for plug in ("criterio-portfolio", "criterio-project",
                                      "criterio-product")
            for f in (RAIZ / "plugins" / plug / "commands").glob("*.md")}
_patron_cmd = re.compile(r"(?<![\w:/-])/(" + "|".join(MAPA_CMD) + r")(?![\w-])")
_seguidos = _sp.run(["git", "-C", str(RAIZ), "ls-files", "*.md"],
                    capture_output=True, text=True).stdout.split()
_sin_prefijo = []
for _s in _seguidos:
    _p = RAIZ / _s
    # En commands/ y skills/ el nombre desnudo es el del archivo, no una invocación. Y
    # `evidencias/` es la transcripción de lo que pasó en una corrida: cita la forma que se
    # escribió, incluida la equivocada — ahí está precisamente el hallazgo.
    if ("commands" in Path(_s).parts or "skills" in Path(_s).parts
            or "evidencias" in Path(_s).parts or not _p.is_file()):
        continue
    for _m in _patron_cmd.finditer(_p.read_text(encoding="utf-8")):
        _sin_prefijo.append(f"{_s} · {_m.group(0)}")
if _sin_prefijo:
    decir(FALLA, f"{len(_sin_prefijo)} referencias sin el prefijo del plugin, empezando "
                 f"por {_sin_prefijo[0]} — quien la escriba no encuentra el comando")
    for _x in _sin_prefijo[1:6]:
        decir(FALLA, _x)
else:
    decir(OK, f"los {len(MAPA_CMD)} comandos se citan como /<plugin>:<comando>")

print("\nQue el árbol del portal tenga exactamente los comandos que existen")
# El árbol de Rostrum es la estructura completa de la PMO: cada comando en su grupo. Un
# comando nuevo que no entre al árbol es invisible en el portal, y uno que se borró y
# siga en el árbol es un enlace muerto. Las dos cosas se ven aquí, no en producción.
sys.path.insert(0, str(PLUGIN / "scripts"))
import servidor as _srv  # noqa: E402
_en_arbol = {(a, c) for a, grupos in _srv.GRUPOS.items() for _, _, cmds in grupos for c in cmds}
_agente = {"criterio-portfolio": "portafolio", "criterio-project": "proyecto",
           "criterio-product": "producto"}
_en_disco = {(_agente[plug], f.stem) for plug in _agente
             for f in (RAIZ / "plugins" / plug / "commands").glob("*.md")}
for _a, _c in sorted(_en_disco - _en_arbol):
    decir(FALLA, f"{_c} existe en {_a} y no está en ningún grupo del árbol")
for _a, _c in sorted(_en_arbol - _en_disco):
    decir(FALLA, f"{_c} está en el árbol de {_a} y no existe como comando")
_sin_nombre = sorted(c for _, c in _en_disco if c not in _srv.ETIQUETA)
for _c in _sin_nombre:
    decir(FALLA, f"{_c} no tiene nombre legible en el árbol (ETIQUETA)")
if _en_disco == _en_arbol and not _sin_nombre:
    decir(OK, f"los {len(_en_arbol)} comandos están en el árbol, cada uno en su grupo y con nombre")

print(f"\n{'coherente' if not fallas else f'{fallas} INCONSISTENCIAS'}")
sys.exit(0 if not fallas else 1)
