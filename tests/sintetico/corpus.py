# -*- coding: utf-8 -*-
"""El motor del material sintético: un solo sitio que sabe escribirlo.

    python3 tests/sintetico/corpus.py --selftest

Antes había tres generadores independientes, y cada uno traía su propia función de
escritura y su propia idea de cómo se organiza una carpeta de proyecto. La estructura
se repetía por costumbre y no estaba declarada en ninguna parte. Aquí se declara una
vez, y los tres corpus la usan.

**El corpus se guarda como datos, no como archivos.** Un `Proyecto` es su código, su
carpeta y sus documentos; recién al final se vuelca a disco. Esa separación es lo que
hace posible lo que sigue:

    la misma declaración → cuatro disposiciones en disco

y con eso se puede probar algo que estaba escrito en las seis páginas de los agentes
y no tenía una sola comprobación detrás: **que el descubrimiento no depende de dónde
estén los archivos.** `index()` recorre con `rglob`, y los comandos dicen que si la
estructura no está se agrupa por lo que digan los documentos y no se impone nada. Los
tres corpus, en cambio, usaban todos el mismo árbol ordenado, así que la promesa
«funciona con lo que haya» no se probaba nunca.

La estructura de referencia es solo eso: la que el material sintético usa. **No es un
requisito del agente y no se le propone al que adopta.** Si un día se convirtiera en
recomendación, sería una decisión de producto y no de pruebas.

Nada de lo que se genera con esto es real. Ningún documento de cliente, de empleador
ni dato personal, como exige CONTRIBUTING.md.
"""
import sys
from pathlib import Path

# ── la estructura de referencia, declarada una sola vez ──────────────────
# El prefijo numérico ordena por etapa del ciclo de vida y no por alfabeto, que es
# la única razón por la que está: `00-gobierno` antes que `30-reuniones` aunque la
# g venga antes que la r.
ESTRUCTURA = {
    "proyecto": {
        "gobierno": "00-gobierno",          # acta, contratos, lo que constituye
        "plan": "10-plan",                  # cronogramas y líneas base
        "seguimiento": "20-seguimiento",     # informes, recibos, cambios
        "reuniones": "30-reuniones",         # minutas y comités
    },
    "producto": {
        "definicion": "00-definicion",       # definición y caso de negocio
        "descubrimiento": "10-descubrimiento",  # entrevistas, visitas, tickets
        "metricas": "20-metricas",           # tableros y series
        "decisiones": "30-decisiones",        # comités de producto
    },
}

# Cómo se llama cada bucket cuando la carpeta la organizó una persona y no una
# convención. Se usa en la disposición `revuelta`, y trae a propósito espacios,
# acentos y un nivel de más: son los tres casos donde un recorrido ingenuo falla.
HUMANAS = {
    "00-gobierno": "Actas y contratos",
    "10-plan": "Cronogramas/2026",
    "20-seguimiento": "",                    # sueltos en la raíz del proyecto
    "30-reuniones": "Reuniones/Comité semanal",
    "00-definicion": "Definición",
    "10-descubrimiento": "Investigación/Entrevistas",
    "20-metricas": "",
    "30-decisiones": "Comités",
}

DISPOSICIONES = ("referencia", "plana", "revuelta", "sin_carpeta")


def normal_estandar(texto: str) -> str:
    """Un documento empieza en su primera línea con contenido y termina en un salto."""
    return texto.strip() + "\n"


def normal_crudo(texto: str) -> str:
    """Solo quita los saltos de apertura. La usa el material de producto, cuyos
    documentos llevan tablas al final donde el espacio final es significativo."""
    return texto.lstrip("\n")

# Donde caen los documentos cuando ningún caso tiene carpeta propia. Es el escenario
# que `portfolio-scan` declara y nadie probaba: «un proyecto mencionado solo dentro
# de las minutas de otro también cuenta».
COMUN = "documentos"


class Documento:
    """Un documento del corpus, todavía sin sitio en el disco."""

    __slots__ = ("bucket", "nombre", "cuerpo", "normalizar")

    def __init__(self, bucket: str, nombre: str, cuerpo: str, normalizar=None):
        self.bucket = bucket        # "00-gobierno", o "" si venía sin bucket
        self.nombre = nombre        # "2026-01-12-acta-constitucion.md"
        self.cuerpo = cuerpo
        self.normalizar = normalizar or normal_estandar

    @property
    def fecha(self):
        """La fecha del nombre, que es la convención que ya usaba el material."""
        cabeza = self.nombre[:10]
        return cabeza if cabeza[:4].isdigit() else None

    def texto(self) -> str:
        """Exactamente lo que va al archivo, ya normalizado."""
        return self.normalizar(self.cuerpo)


class Caso:
    """Base de Proyecto y Producto: un código, una carpeta y sus documentos."""

    CLASE = None

    def __init__(self, codigo: str, carpeta: str = None, normalizar=None):
        self.codigo = codigo
        self.carpeta = carpeta or codigo
        self.normalizar = normalizar or normal_estandar
        self.documentos: list[Documento] = []

    # ── construcción
    def agregar(self, bucket: str, nombre: str, cuerpo: str) -> Documento:
        d = Documento(bucket, nombre, cuerpo, self.normalizar)
        self.documentos.append(d)
        return d

    def _bucket(self, clave: str) -> str:
        buckets = ESTRUCTURA[self.CLASE]
        if clave not in buckets:
            raise KeyError(f"{self.CLASE} no tiene el bucket {clave!r}; "
                           f"hay {', '.join(sorted(buckets))}")
        return buckets[clave]

    def documento(self, clave: str, fecha: str, nombre: str, cuerpo: str) -> Documento:
        """`p.documento("gobierno", "2026-01-12", "acta-constitucion.md", ...)`"""
        return self.agregar(self._bucket(clave), f"{fecha}-{nombre}", cuerpo)

    # ── lectura
    def __len__(self):
        return len(self.documentos)

    def __repr__(self):
        return f"<{type(self).__name__} {self.codigo} · {len(self)} documentos>"


class Proyecto(Caso):
    """Un proyecto sintético: acta, plan, seguimiento y reuniones."""

    CLASE = "proyecto"

    def gobierno(self, fecha, nombre, cuerpo):
        return self.documento("gobierno", fecha, nombre, cuerpo)

    def plan(self, fecha, nombre, cuerpo):
        return self.documento("plan", fecha, nombre, cuerpo)

    def seguimiento(self, fecha, nombre, cuerpo):
        return self.documento("seguimiento", fecha, nombre, cuerpo)

    def reunion(self, fecha, nombre, cuerpo):
        return self.documento("reuniones", fecha, nombre, cuerpo)


class Producto(Caso):
    """Un producto sintético: definición, descubrimiento, métricas y decisiones."""

    CLASE = "producto"

    def definicion(self, fecha, nombre, cuerpo):
        return self.documento("definicion", fecha, nombre, cuerpo)

    def descubrimiento(self, fecha, nombre, cuerpo):
        return self.documento("descubrimiento", fecha, nombre, cuerpo)

    def metrica(self, fecha, nombre, cuerpo):
        return self.documento("metricas", fecha, nombre, cuerpo)

    def decision(self, fecha, nombre, cuerpo):
        return self.documento("decisiones", fecha, nombre, cuerpo)


# ── dónde queda cada documento, según la disposición ─────────────────────

def ubicar(caso: Caso, doc: Documento, disposicion: str) -> str:
    """La ruta relativa del documento, sin la raíz. Determinista siempre.

    Nada de azar: una prueba que cambie de árbol entre corridas no es una prueba.
    """
    if disposicion == "referencia":
        partes = [caso.carpeta, doc.bucket, doc.nombre]
    elif disposicion == "plana":
        partes = [caso.carpeta, doc.nombre]
    elif disposicion == "revuelta":
        partes = [caso.carpeta, HUMANAS.get(doc.bucket, doc.bucket), doc.nombre]
    elif disposicion == "sin_carpeta":
        # Sin carpeta propia, el código va al nombre: es como lo nombra alguien que
        # guarda todo junto, y mantiene único el archivo.
        partes = [COMUN, f"{doc.nombre[:10]}-{caso.codigo}-{doc.nombre[11:]}"
                  if doc.fecha else f"{caso.codigo}-{doc.nombre}"]
    else:
        raise ValueError(f"disposición desconocida: {disposicion!r}; "
                         f"hay {', '.join(DISPOSICIONES)}")
    return "/".join(p for p in partes if p)


class Portafolio:
    """El conjunto de casos y el único que toca el disco.

    Se usa de dos formas. Declarando los casos con las clases, o —y es como los tres
    corpus migraron sin reescribir un solo documento— pasándole rutas relativas con
    `escribir`, que las parte en caso, bucket y nombre.
    """

    def __init__(self, raiz: Path, normalizar=None):
        self.raiz = Path(raiz)
        self.normalizar = normalizar or normal_estandar
        self.casos: dict[str, Caso] = {}

    # ── construcción
    def caso(self, codigo: str, clase: str = "proyecto", carpeta: str = None) -> Caso:
        if codigo not in self.casos:
            tipo = Proyecto if clase == "proyecto" else Producto
            self.casos[codigo] = tipo(codigo, carpeta, self.normalizar)
        return self.casos[codigo]

    def escribir(self, ruta, texto: str) -> Documento:
        """Registra un documento dado por su ruta, relativa a la raíz o absoluta.

        Deduce el caso de la primera carpeta y el bucket de la segunda. Un bucket que
        no esté en la estructura de referencia se conserva tal cual: el material puede
        traer carpetas propias y no es asunto del motor corregirlas.
        """
        ruta = Path(ruta)
        if ruta.is_absolute():
            ruta = ruta.relative_to(self.raiz)
        partes = ruta.parts
        if len(partes) < 2:
            raise ValueError(f"{ruta} no tiene carpeta de caso")
        carpeta, resto, nombre = partes[0], partes[1:-1], partes[-1]
        bucket = resto[0] if resto else ""
        clase = "producto" if _es_producto(bucket, carpeta) else "proyecto"
        codigo = _codigo(carpeta)
        caso = self.caso(codigo, clase, carpeta)
        return caso.agregar(bucket, nombre, texto)

    # ── lectura
    @property
    def documentos(self) -> int:
        return sum(len(c) for c in self.casos.values())

    def rutas(self, disposicion: str = "referencia") -> dict[str, str]:
        """Ruta relativa → cuerpo, sin tocar el disco. Para comparar disposiciones."""
        salida = {}
        for caso in self.casos.values():
            for doc in caso.documentos:
                r = ubicar(caso, doc, disposicion)
                if r in salida:
                    raise ValueError(f"dos documentos caen en {r} con «{disposicion}»")
                salida[r] = doc.texto()
        return salida

    # ── escritura
    def volcar(self, disposicion: str = "referencia", raiz: Path = None) -> int:
        """Escribe el árbol. Devuelve cuántos documentos escribió."""
        destino = Path(raiz) if raiz else self.raiz
        for relativa, texto in self.rutas(disposicion).items():
            archivo = destino / relativa
            archivo.parent.mkdir(parents=True, exist_ok=True)
            archivo.write_text(texto, encoding="utf-8")
        return self.documentos


def _codigo(carpeta: str) -> str:
    """`PRY-001-originacion-digital` → `PRY-001`; `PRD-QR` → `PRD-QR`."""
    trozos = carpeta.split("-")
    if len(trozos) >= 2 and trozos[1].isdigit():
        return "-".join(trozos[:2])
    return carpeta


def _es_producto(bucket: str, carpeta: str) -> bool:
    return bucket in ESTRUCTURA["producto"].values() or carpeta.startswith("PRD-")


def escribir_suelto(ruta: Path, texto: str, normalizar=None) -> None:
    """Para lo que no es material de entrada: las fichas y respuestas de `expected/`.

    Va aquí y no en cada generador porque era la única función que los tres copiaban
    igual, y copiarla tres veces es exactamente la deuda que este repositorio no
    acumula.
    """
    ruta = Path(ruta)
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text((normalizar or normal_estandar)(texto), encoding="utf-8")


# ── selftest ─────────────────────────────────────────────────────────────

def _selftest() -> int:
    fallas = []

    def ok(cond, que):
        print(f"  {'ok  ' if cond else 'FALLA'}  {que}")
        if not cond:
            fallas.append(que)

    print("La estructura de referencia")
    ok(list(ESTRUCTURA) == ["proyecto", "producto"], "declara proyecto y producto")
    ok(all(v[:2].isdigit() for v in ESTRUCTURA["proyecto"].values()),
       "los buckets de proyecto ordenan por etapa y no por alfabeto")
    ok(all(b in HUMANAS for c in ESTRUCTURA.values() for b in c.values()),
       "cada bucket tiene su nombre humano para la disposición revuelta")

    print("\nLas clases guardan el corpus como datos")
    p = Proyecto("PRY-900", "PRY-900-piloto")
    p.gobierno("2026-01-12", "acta-constitucion.md", "  # Acta  ")
    p.plan("2026-01-15", "cronograma-v1.csv", "hito,fecha")
    p.seguimiento("2026-03-02", "informe-avance.md", "# Avance")
    p.reunion("2026-03-09", "comite.md", "# Comité")
    ok(len(p) == 4, "cuatro documentos, ninguno en disco todavía")
    ok(p.documentos[0].bucket == "00-gobierno", "el bucket sale de la estructura")
    ok(p.documentos[0].nombre == "2026-01-12-acta-constitucion.md",
       "el nombre lleva la fecha por delante")
    ok(p.documentos[0].fecha == "2026-01-12", "y la fecha se lee del nombre")
    ok(p.documentos[0].texto() == "# Acta\n",
       "el texto se normaliza igual que antes: strip y un salto final")

    d = Producto("PRD-TEST")
    d.definicion("2026-03-04", "caso-de-negocio.md", "# Caso")
    d.metrica("2026-09-01", "tablero.md", "# Tablero")
    ok(d.documentos[1].bucket == "20-metricas", "producto tiene sus propios buckets")
    try:
        d.documento("plan", "2026-01-01", "x.md", "y")
        ok(False, "un bucket de proyecto en un producto tiene que fallar")
    except KeyError:
        ok(True, "un bucket de proyecto en un producto falla, y dice cuáles hay")

    crudo = Producto("PRD-CRUDO", normalizar=normal_crudo)
    crudo.definicion("2026-01-01", "caso.md", "\n\n# Caso\n\n| a | b |\n")
    ok(crudo.documentos[0].texto() == "# Caso\n\n| a | b |\n",
       "la normalización cruda respeta el final del documento, y es la de producto")
    ok(Documento("x", "y.md", "  z  ").texto() == "z\n",
       "la estándar recorta por los dos lados y cierra con un salto")

    print("\nLas cuatro disposiciones, y todas deterministas")
    port = Portafolio(Path("/tmp/no-se-escribe"))
    port.casos["PRY-900"] = p
    port.casos["PRD-TEST"] = d
    vistas = {k: port.rutas(k) for k in DISPOSICIONES}
    ok(all(len(v) == 6 for v in vistas.values()),
       "las cuatro colocan los seis documentos, sin perder ni duplicar ninguno")
    ok(sorted(vistas["referencia"].values()) == sorted(vistas["revuelta"].values()),
       "y el contenido es el mismo en todas: cambia dónde, no qué")
    ok(port.rutas("revuelta") == port.rutas("revuelta"),
       "dos lecturas seguidas dan el mismo árbol")

    ref = vistas["referencia"]
    ok("PRY-900-piloto/00-gobierno/2026-01-12-acta-constitucion.md" in ref,
       "referencia · carpeta del caso, bucket, documento")
    ok("PRY-900-piloto/2026-01-12-acta-constitucion.md" in vistas["plana"],
       "plana · sin bucket, todo en la carpeta del caso")
    rev = vistas["revuelta"]
    ok("PRY-900-piloto/Actas y contratos/2026-01-12-acta-constitucion.md" in rev,
       "revuelta · carpetas con espacios, como las nombra una persona")
    ok("PRY-900-piloto/Reuniones/Comité semanal/2026-03-09-comite.md" in rev,
       "revuelta · y con un nivel de más, y con acento")
    ok("PRY-900-piloto/2026-03-02-informe-avance.md" in rev,
       "revuelta · seguimiento queda suelto en la raíz del proyecto")
    sin = vistas["sin_carpeta"]
    ok(f"{COMUN}/2026-01-12-PRY-900-acta-constitucion.md" in sin,
       "sin_carpeta · todo junto, con el código en el nombre")
    ok(len({r.split("/")[0] for r in sin}) == 1,
       "sin_carpeta · ninguna carpeta propia, que es el caso que nadie probaba")
    try:
        port.rutas("inventada")
        ok(False, "una disposición inventada tiene que fallar")
    except ValueError:
        ok(True, "una disposición inventada falla, y dice cuáles hay")

    print("\nRegistro por ruta, que es como migraron los tres corpus")
    q = Portafolio(Path("/tmp/no-se-escribe"))
    q.escribir("PRY-001-originacion-digital/00-gobierno/2026-01-12-acta.md", "# A")
    q.escribir(Path("/tmp/no-se-escribe/PRD-QR/20-metricas/2026-09-01-tablero.md"), "# T")
    q.escribir("PRY-001-originacion-digital/Suelto/2026-02-02-nota.md", "# N")
    ok(q.documentos == 3, "registra sin escribir nada")
    ok(_codigo("PRY-001-originacion-digital") == "PRY-001",
       "el código sale de la carpeta, sin el nombre largo")
    ok(isinstance(q.casos["PRD-QR"], Producto), "PRD- se reconoce como producto")
    ok(isinstance(q.casos["PRY-001"], Proyecto), "PRY- como proyecto")
    ok(q.casos["PRY-001"].documentos[1].bucket == "Suelto",
       "un bucket que no es de la estructura se conserva, no se corrige")
    ok(q.rutas()["PRY-001-originacion-digital/00-gobierno/2026-01-12-acta.md"] == "# A\n",
       "y la ruta de vuelta es la misma con la que entró")
    try:
        q.escribir("suelto-en-la-raiz.md", "x")
        ok(False, "un documento sin carpeta de caso tiene que fallar")
    except ValueError:
        ok(True, "un documento sin carpeta de caso falla")

    print(f"\n{'ok' if not fallas else f'{len(fallas)} FALLAS'} · "
          f"{len(fallas)} de las comprobaciones en rojo")
    return 1 if fallas else 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(_selftest())
    print(__doc__.strip().splitlines()[0])
    print(f"\nEstructura de referencia y disposiciones: "
          f"{', '.join(DISPOSICIONES)}")
    sys.exit(0)
