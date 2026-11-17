#!/usr/bin/env python3
"""El catálogo de YouTube: el título, la descripción con sus capítulos y las etiquetas de cada video
publicado, en español y en inglés, para que sync_youtube.py los suba.

    python3 scripts/youtube.py            reescribe docs/video/youtube_catalog.json
    python3 scripts/youtube.py --check    falla si no es lo que sale del repositorio
    python3 scripts/youtube.py --medir    anota en videos.json la duración de cada video, del mp4

Aquí no se teclea ningún dato. Cada video publicado está en docs/video/videos.json —su identificador y
su transcripción, con el segundo en que aparece cada texto—. Los capítulos salen de esa transcripción:
el segundo en que aparece cada pantalla. Lo que dice cada descripción sale de su dueño: el rol, las
áreas y con qué se integra cada una, de `nivel_c` de familia.json; los agentes, de familia.json; los
países, de la clave de cada entidad del material de pruebas —igual que «Dónde se probó» en el portal—;
la frase de anonimato, de docs/anonimato.json; las páginas, de las rutas del portal. Solo se escriben
aquí los rótulos de los capítulos y la forma de las frases.

Las reglas de YouTube que se comprueban: título de 100 caracteres o menos, descripción de 5.000 o menos,
etiquetas que suman 500 o menos, y capítulos que empiezan en 0:00, son tres o más y duran 10 segundos
o más cada uno. La regla de la casa: ni «gratis» ni «100 %», los agentes «procesan», no «leen», y es
«área», no «función». Las únicas cifras son las que ya publica su dueño (`nivel_c`).
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
VIDEO = RAIZ / "docs" / "video"
REGISTRO = VIDEO / "videos.json"
SALIDA = VIDEO / "youtube_catalog.json"
TRANS = VIDEO / "transcripciones"
PORTAL = "https://www.josenanez.com"
REPO = "https://github.com/josenanez/criterio"
MARKETPLACE = "josenanez/criterio"
CAPITULO_MIN = 10
# Las marcas con que empieza alguna integración de `nivel_c`: no se pasan a minúscula.
MARCAS = {"Excel", "Microsoft", "Outlook", "Salesforce", "Tenable", "Word", "Zoho", "Google", "Dynamics", "ChileCompra"}

PAISES = {p["codigo"]: p["nombre"] for p in json.loads((RAIZ / "plugins/criterio-finance/scripts/paises.json").read_text(encoding="utf-8"))["paises"]}

# Los rótulos con que cada pantalla aparece en la transcripción en español —los de src/youtube.jsx y
# src/criterio.jsx— y el nombre de su capítulo. `gancho`: la pantalla de entrada, que cede su capítulo
# a la siguiente si esta llega antes de diez segundos.
PRESENTACION = [
    {"rotulo": {"es": r"^Datos de prueba$", "en": r"^Test data$"}, "gancho": True,
     "es": "Un hallazgo en los datos de prueba", "en": "A finding in the test data"},
    {"rotulo": {"es": r"^Criterio {SIGLA}$", "en": r"^Criterio {SIGLA}$"}, "es": "Qué hace Criterio {SIGLA}, área por área", "en": "What Criterio {SIGLA} does, area by area"},
    {"rotulo": {"es": r"^Dónde se probó$", "en": r"^Where it was tested$"}, "es": "Dónde se probó", "en": "Where it was tested"},
    {"rotulo": {"es": r"(agentes?|agente) y un portal$", "en": r"agents? and a portal$"}, "es": "Los agentes y lo que preparan", "en": "The agents and what they prepare"},
    {"rotulo": {"es": r"^Lo que hoy hace tu equipo, a mano$", "en": r"^What your team does by hand today$"},
     "es": "Lo que hoy hace tu equipo, a mano", "en": "What your team does by hand today"},
    {"rotulo": {"es": r"^La evidencia$", "en": r"^The evidence$"}, "es": "La evidencia de las pruebas", "en": "The test evidence"},
    {"rotulo": {"es": r"^Lo que encontró$", "en": r"^What it found$"}, "es": "Lo que encontró cada agente", "en": "What each agent found"},
    {"rotulo": {"es": r"^Código abierto · Apache 2\.0$", "en": r"^Open source · Apache 2\.0$"}, "es": "Cómo se instala", "en": "How to install it"},
]
CRITERIO = [
    {"rotulo": {"es": r"^Criterio$", "en": r"^Criterio$"}, "es": "Qué es Criterio", "en": "What Criterio is"},
    {"rotulo": {"es": r"^De la pirámide de hoy a la de ahora$", "en": r"^From today.s pyramid to the new one$"},
     "es": "De la pirámide de hoy a la de ahora", "en": "From today's pyramid to the new one"},
    {"rotulo": {"es": r"^familias$", "en": r"^families$"}, "es": "Las familias y sus agentes", "en": "The families and their agents"},
    {"rotulo": {"es": r"^Dónde se probó$", "en": r"^Where it was tested$"}, "es": "Dónde se probó", "en": "Where it was tested"},
    {"rotulo": {"es": r"^La evidencia$", "en": r"^The evidence$"}, "es": "La evidencia de las pruebas", "en": "The test evidence"},
    {"rotulo": {"es": r"^Una familia a la vez", "en": r"^One family at a time"}, "es": "Cómo madura cada familia", "en": "How each family matures"},
    {"rotulo": {"es": r"^Hacia dónde vamos$", "en": r"^Where we are going$"}, "es": "Hacia dónde vamos", "en": "Where we are heading"},
    {"rotulo": {"es": r"^Instala Criterio\.$", "en": r"^Install Criterio\.$"}, "es": "Cómo se instala", "en": "How to install it"},
]
# Los capítulos de una familia con una sola agente, en singular.
UNA = {"Los agentes y lo que preparan": {"es": "La agente y lo que prepara", "en": "The agent and what she prepares"},
       "Lo que encontró cada agente": {"es": "Lo que encontró", "en": "What she found"}}
# Los pasos del video de uso, como los escribe uso/transcribir.py: «N · Título. texto». Su nombre en inglés
# es el del guion en inglés (pasos_en).
PASO = re.compile(r"^(\d+) · ([^.]+)\.")
GUIONES = VIDEO / "uso" / "guiones"

T = {
    "es": {
        "titulo": "{nombre} con agentes de IA: {areas} | Criterio {SIGLA}",
        "titulo_uso": "Cómo se usa Criterio {SIGLA} en Claude Code, de la instalación al primer resultado",
        "titulo_criterio": "{lema} | Criterio",
        "que_es": "Criterio {SIGLA} es una familia de agentes de IA de código abierto (Apache 2.0) que trabaja en Claude Code: "
                  "procesa los documentos del área y entrega cada señal con la cita del documento del que sale.",
        "areas": "Qué hace, área por área:",
        "area": "• {a}: {que}. Con {con}.",
        "agentes": "Los agentes: {lista}. Y Rostrum, el portal que publica lo que escriben.",
        "agente_una": "La agente: {lista}. Y Rostrum, el portal que publica lo que escribe.",
        "titulo_uso_en": "",
        "donde": "Dónde se probó: {paises}.",
        "pagina": "La familia, su evidencia y la calculadora: {url}",
        "analisis": "El análisis de las pruebas: {url}",
        "uso": "Cómo se usa, de la instalación al primer resultado: {url}",
        "uso_en": "",
        "presentacion": "Qué hace la familia, en noventa segundos: {url}",
        "codigo": "El código: {url}",
        "uso_que": "Una sesión real de Claude Code, acelerada y sin voz: Criterio {SIGLA} se instala con dos comandos, se configura en "
                   "una conversación y entrega su primer resultado.",
        "instalar": "Para instalarla, en Claude Code o Cowork:",
        "criterio_que": "Criterio es un conjunto de familias de agentes de IA de código abierto (Apache 2.0) para Claude Code, "
                        "una por cada rol del nivel C. Cada familia procesa los documentos de su área y entrega cada señal "
                        "con la cita del documento del que sale; ninguna se anuncia antes de pasar su prueba.",
        "familias": "Las familias de hoy:",
        "familia": "• Criterio {SIGLA} · {rol}: {agentes}",
        "agentes_url": "Todas las familias, con su evidencia: {url}",
        "capitulos": "Capítulos",
        "llm": "Lo ejecuta un modelo de lenguaje (LLM), que puede equivocarse: por eso ningún dato llega sin su fuente, y la decisión es de quien la firma.",
        "pantalla": "Texto en pantalla en inglés.",
        "pantalla_uso": "Los textos en pantalla están en inglés; la sesión de Claude Code, en español.",
        "gemelo": {"en": "En inglés: {url}", "es": "En español: {url}"},
        "y": " y ",
        "hashtags": "#Criterio #AgentesDeIA #ClaudeCode",
        "base_tags": ["Criterio", "José Ñáñez", "Jose Nanez", "josenanez.com", "agentes de IA", "AI agents", "Claude Code",
                      "código abierto", "gobernanza de IA", "AI governance"],
    },
    "en": {
        "titulo": "{nombre} with AI agents: {areas} | Criterio {SIGLA}",
        "titulo_uso": "How to use Criterio {SIGLA} in Claude Code, from install to first result",
        "titulo_criterio": "{lema} | Criterio",
        "que_es": "Criterio {SIGLA} is an open-source (Apache 2.0) family of AI agents that works in Claude Code: it processes "
                  "the area's documents and delivers every signal with a citation to the document it comes from.",
        "areas": "What it does, area by area:",
        "area": "• {a}: {que}. With {con}.",
        "agentes": "The agents: {lista}. And Rostrum, the portal that publishes what they write.",
        "agente_una": "The agent: {lista}. And Rostrum, the portal that publishes what she writes.",
        "titulo_uso_en": "Criterio {SIGLA} · How to use it, from install to first result",
        "donde": "Where it was tested: {paises}.",
        "pagina": "The family, its evidence and the calculator: {url}",
        "analisis": "The analysis of the tests: {url}",
        "uso": "How it is used, from install to first result (in Spanish): {url}",
        "uso_en": "How it is used, from install to first result: {url}",
        "presentacion": "What the family does, in ninety seconds: {url}",
        "codigo": "The code: {url}",
        "uso_que": "A real Claude Code session, sped up and without voice: Criterio {SIGLA} installs with two commands, is set up in a "
                   "conversation and delivers its first result.",
        "instalar": "To install it, in Claude Code or Cowork:",
        "criterio_que": "Criterio is a set of open-source (Apache 2.0) families of AI agents for Claude Code, one for each "
                        "C-level role. Each family processes its area's documents and delivers every signal with a citation "
                        "to the document it comes from; none is announced before it passes its test.",
        "familias": "Today's families:",
        "familia": "• Criterio {SIGLA} · {rol}: {agentes}",
        "agentes_url": "Every family, with its evidence: {url}",
        "capitulos": "Chapters",
        "llm": "It is run by a language model (LLM), which can be wrong: that is why no data point arrives without its source, and the decision belongs to whoever signs it.",
        "pantalla": "On-screen text in Spanish.",
        "pantalla_uso": "The on-screen text is in English; the Claude Code session, in Spanish.",
        "gemelo": {"es": "In Spanish: {url}", "en": "In English: {url}"},
        "y": " and ",
        "hashtags": "#Criterio #AIAgents #ClaudeCode",
        "base_tags": [],
    },
}
PROHIBIDO = [r"\bgratis\b", r"\bfree\b", r"100\s?%", r"\blee\b", r"\bleen\b", r"\breads?\b", r"\bfunci[oó]n\b"]


def _j(p: Path):
    return json.loads(p.read_text(encoding="utf-8"))


def pasos_en() -> dict[str, str]:
    """El nombre en inglés de cada paso del video de uso: el del guion en inglés, capítulo a capítulo sobre
    los de su base. Un mismo paso con dos nombres en inglés es un error."""
    out: dict[str, str] = {}
    for p in sorted(GUIONES.glob("*.en.json")):
        en = _j(p)
        for a, b in zip(_j(GUIONES / en["base"])["capitulos"], en["capitulos"], strict=True):
            if out.setdefault(a["titulo"], b["titulo"]) != b["titulo"]:
                raise SystemExit(f"youtube: el paso «{a['titulo']}» se llama «{out[a['titulo']]}» y, en {p.name}, «{b['titulo']}»")
    return out


def _seg(t: str) -> int:
    m, s = t.split(":")
    return int(m) * 60 + int(s)


def _hms(s: int) -> str:
    return f"{s // 60}:{s % 60:02d}"


def lineas(archivo: str) -> list[tuple[int, str]]:
    out = []
    for l in (TRANS / archivo).read_text(encoding="utf-8").splitlines():
        m = re.match(r"^(\d+:\d{2})\s+(.+)$", l)
        if m:
            out.append((_seg(m.group(1)), m.group(2).strip()))
    if not out:
        raise SystemExit(f"youtube: {archivo} no trae líneas con su tiempo")
    return out


def capitulos(marcas: list[tuple[int, dict]], duracion: float, nombre: str) -> list[tuple[int, dict]]:
    """Cada pantalla con su segundo → los capítulos que YouTube acepta: el primero en 0:00, cada uno de
    diez segundos o más. Una pantalla que llega antes de diez segundos queda dentro del capítulo
    anterior; si el anterior es el gancho de entrada, le cede el nombre."""
    caps: list[tuple[int, dict]] = []
    for t, m in marcas:
        if not caps:
            caps.append((0, m))
        elif t - caps[-1][0] >= CAPITULO_MIN:
            caps.append((t, m))
        elif len(caps) == 1 and caps[0][1].get("gancho"):
            caps[0] = (0, m)
    while caps and duracion - caps[-1][0] < CAPITULO_MIN:
        caps.pop()
    if len(caps) < 3:
        raise SystemExit(f"youtube: {nombre} queda con {len(caps)} capítulos; YouTube pide tres o más")
    return caps


def marcas_de(archivo: str, rotulos: list[dict], idioma: str, sigla: str = "") -> list[tuple[int, dict]]:
    ls = lineas(archivo)
    out = []
    for r in rotulos:
        rx = re.compile(r["rotulo"][idioma].replace("{SIGLA}", sigla.upper()))
        t = next((t for t, x in ls if rx.search(x)), None)
        if t is None:
            raise SystemExit(f"youtube: {archivo} no trae la pantalla «{r['rotulo'][idioma]}»; ¿cambió el rótulo en src/?")
        out.append((t, r))
    if [t for t, _ in out] != sorted(t for t, _ in out):
        raise SystemExit(f"youtube: {archivo}: las pantallas no están en el orden esperado")
    return out


def marcas_uso(archivo: str, f: dict) -> list[tuple[int, dict]]:
    """Cada paso, la primera vez que aparece; en la configuración, además, cada agente cuando su setup
    empieza —«Configurarla: Clara, el cierre», «Tomás, el presupuesto»—, como lo dice la transcripción."""
    vistos, out = set(), []
    agentes = {a["nombre"]: a for a in f["agentes"]}
    PASOS_EN = pasos_en()
    for t, x in lineas(archivo):
        m = PASO.match(x)
        if not m:
            continue
        es = m.group(2).strip()
        if es not in PASOS_EN:
            raise SystemExit(f"youtube: el paso «{es}» de {archivo} no tiene su nombre en inglés en uso/guiones/*.en.json")
        resto = x[m.end():].strip()
        quien = next((n for n in agentes if resto.startswith(f"{n}, ")), None)
        if es.startswith("Configurarla") and quien and quien not in vistos:
            a = agentes[quien]
            primero = not any(k.startswith("Configurar") for k in vistos)
            vistos.add(quien)
            vistos.add(m.group(1))
            out.append((t, {"es": (f"{m.group(1)} · Configurarla: " if primero else "") + f"{a['nombre']}, {a['titulo']}",
                            "en": (f"{m.group(1)} · Set it up: " if primero else "") + f"{a['nombre']}, {a['rol']['en']}"}))
            vistos.add("Configurar")
        elif m.group(1) not in vistos:
            vistos.add(m.group(1))
            out.append((t, {"es": f"{m.group(1)} · {es}", "en": f"{m.group(1)} · {PASOS_EN[es]}"}))
    return out


def setup_de(f: dict) -> str:
    """El comando que configura la familia: el de su paraguas o, con una sola agente, el de su plugin."""
    a = f["agentes"]
    if len(a) == 1:
        s = next(c["id"] for c in a[0]["comandos"] if c["id"].endswith("-setup"))
        return f"/{a[0]['plugin']}:{s}"
    return f"/criterio-{f['sigla']}:{f['sigla']}-setup"


def familia(sigla: str) -> dict:
    return _j(RAIZ / "families" / f"criterio-{sigla}" / "familia.json")


def paises(sigla: str, l: str) -> list[str]:
    """Los países del material de la familia, en el orden del registro de países: «Dónde se probó»."""
    mat = RAIZ / "tests" / f"criterio-{sigla}" / "material"
    if not mat.is_dir():
        return []
    cods = {_j(c).get("pais") for c in mat.glob("*/clave.json")} - {None, ""}
    return [PAISES[c][l] for c in PAISES if c in cods]


TOTAL = re.compile(r"^\d+ (países|countries)$")


def es_nombre(m: str) -> bool:
    """Una integración que es un sistema o una sigla —DIAN, Salesforce, KEV de CISA—, no un documento: va a las etiquetas."""
    w = m.split(" ")[0].rstrip(",")
    return not TOTAL.match(m) and not re.search(r"\b(Excel|CSV|Word|PDF|ERP)\b|cualquier", m) and \
        (w in MARCAS or (len(w) > 1 and w.isupper()) or any(c.isupper() for c in w[1:]))


def minuscula(x: str) -> str:
    """La primera letra en minúscula, salvo una sigla («DIAN», «CVs») o una marca («Tenable»)."""
    w = x.split(" ")[0].rstrip(",")
    return x if w.isupper() or any(c.isupper() for c in w[1:]) or w in MARCAS else x[0].lower() + x[1:]


def unir(xs: list[str], l: str) -> str:
    return xs[0] if len(xs) == 1 else ", ".join(xs[:-1]) + T[l]["y"] + xs[-1]


def url_familia(sigla: str, l: str) -> str:
    return f"{PORTAL}{'/es' if l == 'es' else ''}/agents/criterio-{sigla}"


def yt(i: str) -> str:
    return f"https://youtu.be/{i}"


def titulo_familia(f: dict, l: str) -> str:
    areas = [x[l][0][0].lower() + x[l][0][1:] for x in f["nivel_c"]["portada"]["filas"]]
    nombre = f["nombre"][l]
    for n in range(len(areas), 1, -1):
        t = T[l]["titulo"].format(nombre=nombre, areas=", ".join(areas[:n]), SIGLA=f["sigla"].upper())
        if len(t) <= 100:
            return t
    raise SystemExit(f"youtube: el título de {f['sigla']} no cabe en 100 caracteres")


def lista_agentes(f: dict, l: str) -> str:
    out = []
    for a in f["agentes"]:
        out.append(f"{a['nombre']}, {a['titulo'] if l == 'es' else a['rol']['en']}")
    return " · ".join(out)


def bloque_capitulos(caps, l) -> list[str]:
    return [T[l]["capitulos"]] + [f"{_hms(t)} {m[l].replace('{SIGLA}', m.get('_sigla', ''))}" for t, m in caps]


def etiquetas(base: list[str], extra: list[str]) -> list[str]:
    """Sin repetir, hasta 500 caracteres contados como los cuenta YouTube (comillas si hay espacio)."""
    out, vistos = [], set()
    for x in base + extra:
        k = x.lower()
        if k in vistos:
            continue
        nuevo = out + [x]
        if sum(len(e) + (2 if " " in e else 0) for e in nuevo) + len(nuevo) - 1 > 500:
            break
        out, _ = nuevo, vistos.add(k)
    return out


def anonimato(l: str) -> str:
    return _j(RAIZ / "docs" / "anonimato.json")[l]


def titulo_de(v: dict, par: dict | None, idioma: str, l: str) -> str | None:
    """El título curado de videos.json: el del video en su idioma, y el de su gemelo para la traducción."""
    if l == idioma:
        return v.get("titulo")
    return (par or {}).get("titulo")


def otro(idioma: str) -> str:
    return "en" if idioma == "es" else "es"


def aviso(l: str, idioma: str) -> list[str]:
    """La descripción en otro idioma que el del video dice en qué idioma está el texto en pantalla."""
    return [T[l]["pantalla"]] if l != idioma else []


def gemelo(l: str, idioma: str, par: dict | None) -> list[str]:
    """El enlace al mismo video en el otro idioma, si está publicado."""
    return [T[l]["gemelo"][otro(idioma)].format(url=yt(par["id"]))] if par else []


def presentacion(sigla: str, v: dict, uso: dict | None, idioma: str = "es", par: dict | None = None) -> dict:
    f = familia(sigla)
    p = f["nivel_c"]["portada"]
    una = len(f["agentes"]) == 1
    caps = capitulos([(t, {**m, **(UNA.get(m["es"], {}) if una else {}), "_sigla": sigla.upper()})
                      for t, m in marcas_de(v["transcripcion"], PRESENTACION, idioma, sigla)], v["duracion"], v["transcripcion"])
    out = {"idioma": idioma, "localizaciones": [otro(idioma)]}
    for l in ("es", "en"):
        t = T[l]
        partes = aviso(l, idioma)
        partes += [t["que_es"].format(SIGLA=sigla.upper()), "",
                   t["areas"]] + [t["area"].format(a=x[l][0], que=x[l][1][0].lower() + x[l][1][1:],
                                                   con=minuscula(", ".join(i for i in x[l][2].split(" · ") if not TOTAL.match(i)))) for x in p["filas"]]
        partes += ["", t["agente_una" if len(f["agentes"]) == 1 else "agentes"].format(lista=lista_agentes(f, l))]
        ps = paises(sigla, l)
        if ps:
            partes += [t["donde"].format(paises=unir(ps, l))]
        partes += [anonimato(l), "", t["pagina"].format(url=url_familia(sigla, l)),
                   t["analisis"].format(url=url_familia(sigla, l) + "/analisis")]
        if uso:
            # El video de uso en el idioma de la descripción, si está publicado en ese idioma.
            en = l == "en" and uso.get("en")
            partes.append(t["uso_en" if en else "uso"].format(url=yt(uso["en"]["id"] if en else uso["id"])))
        partes += gemelo(l, idioma, par)
        partes += [t["codigo"].format(url=REPO), ""] + bloque_capitulos(caps, l) + ["", t["llm"], "", t["hashtags"]]
        out[l] = {"title": titulo_de(v, par, idioma, l) or titulo_familia(f, l), "description": "\n".join(partes)}
    marcas = [re.sub(r"\s*\(.*?\)", "", m) for x in p["filas"] for m in x["es"][2].split(" · ") if es_nombre(m)]
    base = T["es"]["base_tags"] + [f"Criterio {sigla.upper()}", p["rol"], f["nombre"]["es"], f["nombre"]["en"]]
    out["tags"] = etiquetas(base, [x["es"][0] for x in p["filas"]] + [a["nombre"] for a in f["agentes"]] + marcas)
    out["chapters"] = [{"t": _hms(t), "es": m["es"].replace("{SIGLA}", sigla.upper()), "en": m["en"].replace("{SIGLA}", sigla.upper())} for t, m in caps]
    return out


def de_uso(sigla: str, v: dict, pres: dict, idioma: str = "es", par: dict | None = None) -> dict:
    """El video de uso. El de inglés es la misma toma —la sesión de Claude Code, en español— con los textos en
    pantalla en inglés: el mismo montaje, así que sus capítulos caen en los mismos segundos que los del español."""
    f = familia(sigla)
    es = v if idioma == "es" else par
    caps = capitulos(marcas_uso(es["transcripcion"], f), es["duracion"], es["transcripcion"])
    out = {"idioma": idioma, "localizaciones": [otro(idioma)]}
    for l in ("es", "en"):
        t = T[l]
        partes = [t["pantalla_uso"]] if idioma == "en" else aviso(l, idioma)
        # La presentación en el idioma de la descripción, si está publicada en ese idioma.
        pres_l = pres.get("en") if l == "en" and pres.get("en") else pres
        partes += [t["uso_que"].format(SIGLA=sigla.upper()), "", t["instalar"],
                   f"/plugin marketplace add {MARKETPLACE}", f"/plugin install criterio-{sigla}@criterio", setup_de(f), "",
                   anonimato(l), "", t["pagina"].format(url=url_familia(sigla, l)),
                   t["presentacion"].format(url=yt(pres_l["id"])), *gemelo(l, idioma, par), t["codigo"].format(url=REPO), ""]
        partes += bloque_capitulos(caps, l) + ["", t["llm"], "", t["hashtags"]]
        out[l] = {"title": titulo_de(v, par, idioma, l) or T["en"]["titulo_uso_en"].format(SIGLA=sigla.upper()), "description": "\n".join(partes)}
    base = T["es"]["base_tags"] + [f"Criterio {sigla.upper()}", f["nivel_c"]["portada"]["rol"], "instalación", "installation", "tutorial"]
    out["tags"] = etiquetas(base, [a["nombre"] for a in f["agentes"]])
    out["chapters"] = [{"t": _hms(t), "es": m["es"], "en": m["en"]} for t, m in caps]
    return out


def de_criterio(v: dict, publicadas: list[str], idioma: str = "es", par: dict | None = None) -> dict:
    caps = capitulos(marcas_de(v["transcripcion"], CRITERIO, idioma), v["duracion"], v["transcripcion"])
    base = v["transcripcion"].replace("-en.", "-es.")
    lema = {"es": lineas(base)[1][1].rstrip("."), "en": lineas(base.replace("-es.", "-en."))[1][1].rstrip(".")}
    out = {"idioma": idioma, "localizaciones": [otro(idioma)]}
    for l in ("es", "en"):
        t = T[l]
        partes = aviso(l, idioma)
        partes += [t["criterio_que"], "", t["familias"]]
        for s in publicadas:
            f = familia(s)
            partes.append(t["familia"].format(SIGLA=s.upper(), rol=f["nivel_c"]["portada"]["rol"],
                                              agentes=unir([a["nombre"] for a in f["agentes"]], l)))
        partes += ["", anonimato(l), "", t["agentes_url"].format(url=f"{PORTAL}{'/es' if l == 'es' else ''}/agents"),
                   *gemelo(l, idioma, par), t["codigo"].format(url=REPO), "", t["instalar"], f"/plugin marketplace add {MARKETPLACE}", ""]
        partes += bloque_capitulos(caps, l) + ["", t["llm"], "", t["hashtags"]]
        out[l] = {"title": titulo_de(v, par, idioma, l) or t["titulo_criterio"].format(lema=lema[l]), "description": "\n".join(partes)}
    roles = [familia(s)["nivel_c"]["portada"]["rol"] for s in publicadas]
    out["tags"] = etiquetas(T["es"]["base_tags"] + ["nivel C", "C-level"], [f"Criterio {s.upper()}" for s in publicadas] + roles)
    out["chapters"] = [{"t": _hms(t), "es": m["es"], "en": m["en"]} for t, m in caps]
    return out


def revisar(cat: dict) -> list[str]:
    malos = []
    for i, v in cat["videos"].items():
        for l in ("es", "en"):
            ti, de = v[l]["title"], v[l]["description"]
            if len(ti) > 100:
                malos.append(f"{i} {l}: título de {len(ti)} caracteres")
            if len(de) > 5000:
                malos.append(f"{i} {l}: descripción de {len(de)} caracteres")
            if "<" in de or ">" in de:
                malos.append(f"{i} {l}: YouTube no acepta < ni > en la descripción")
            for rx in PROHIBIDO:
                if re.search(rx, ti + "\n" + de, re.I):
                    malos.append(f"{i} {l}: dice «{re.search(rx, ti + de, re.I).group(0)}»")
    return malos


def generar() -> dict:
    reg = _j(REGISTRO)
    ultima = _j(RAIZ / "registro" / "versiones.json")["versiones"][-1]
    publicadas = [s for s in sorted(ultima["familias"], key=lambda s: familia(s)["orden"] if (RAIZ / "families" / f"criterio-{s}").is_dir() else 999)
                  if (RAIZ / "families" / f"criterio-{s}").is_dir()]
    videos = {}
    c = reg["criterio"]
    videos[c["id"]] = {"video": "criterio", **de_criterio(c, publicadas, "es", c.get("en"))}
    if c.get("en"):
        videos[c["en"]["id"]] = {"video": "criterio/en", **de_criterio(c["en"], publicadas, "en", c)}
    for s, par in reg["familias"].items():
        pres, uso = par.get("presentacion"), par.get("uso")
        if pres:
            videos[pres["id"]] = {"video": f"{s}/presentacion", **presentacion(s, pres, uso, "es", pres.get("en"))}
            if pres.get("en"):
                videos[pres["en"]["id"]] = {"video": f"{s}/presentacion/en", **presentacion(s, pres["en"], uso, "en", pres)}
        if uso:
            videos[uso["id"]] = {"video": f"{s}/uso", **de_uso(s, uso, pres, "es", uso.get("en"))}
            if uso.get("en"):
                videos[uso["en"]["id"]] = {"video": f"{s}/uso/en", **de_uso(s, uso["en"], pres, "en", uso)}
    # Las listas de reproducción, en el orden de las familias en el portal (`orden` de familia.json): Criterio
    # primero y, después, la presentación y el uso de cada familia, cada lista con los de su idioma.
    orden = sorted(reg["familias"], key=lambda s: familia(s)["orden"])
    pares = [v for s in orden for v in (reg["familias"][s].get("presentacion"), reg["familias"][s].get("uso")) if v]
    listas = {"es": [c["id"]] + [v["id"] for v in pares],
              "en": ([c["en"]["id"]] if c.get("en") else []) + [v["en"]["id"] for v in pares if v.get("en")]}
    listas = {l: {"id": (reg.get("listas") or {}).get(l), "videos": ids} for l, ids in listas.items()}
    return {"nota": "Generado por scripts/youtube.py desde el repositorio; no se edita a mano. Lo sube docs/video/sync_youtube.py.",
            "videos": videos, "listas": listas}


def medir() -> int:
    reg = _j(REGISTRO)

    def mp4(v: dict) -> Path:
        n = v["transcripcion"].replace(".txt", ".mp4")
        if "-uso-" in n:
            # El de inglés se arma sobre la toma en español: queda en su carpeta.
            s = re.match(r"criterio-(\w+)-uso-\w+\.mp4", n).group(1)
            return next(iter(sorted((VIDEO / "uso" / "tomas").glob(f"{s}-*/{n}"))), VIDEO / "uso" / "tomas" / n)
        return VIDEO / "youtube" / n

    todos = [reg["criterio"]] + [v for par in reg["familias"].values() for v in par.values()]
    todos += [v["en"] for v in todos if v.get("en")]
    for v in todos:
        p = mp4(v)
        if not p.exists():
            print(f"  no está {p.relative_to(RAIZ)}: se deja la duración que tenía")
            continue
        d = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)],
                           capture_output=True, text=True, check=True).stdout.strip()
        v["duracion"] = round(float(d), 1)
    REGISTRO.write_text(json.dumps(reg, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"  {len(todos)} duraciones en {REGISTRO.relative_to(RAIZ)}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--medir", action="store_true")
    a = ap.parse_args()
    if a.medir:
        return medir()
    cat = generar()
    malos = revisar(cat)
    if malos:
        print("youtube: el catálogo no pasa:\n  " + "\n  ".join(malos))
        return 1
    texto = json.dumps(cat, ensure_ascii=False, indent=1) + "\n"
    if a.check:
        if not SALIDA.exists() or SALIDA.read_text(encoding="utf-8") != texto:
            print("youtube: docs/video/youtube_catalog.json no es el que sale del repositorio: corre scripts/youtube.py")
            return 1
        print(f"youtube: {len(cat['videos'])} videos, al día")
        return 0
    SALIDA.write_text(texto, encoding="utf-8")
    print(f"youtube: {len(cat['videos'])} videos en {SALIDA.relative_to(RAIZ)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
