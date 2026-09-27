# -*- coding: utf-8 -*-
"""Que el descubrimiento no dependa de dónde estén los archivos.

    python3 tests/sintetico/disposiciones.py

Las seis páginas de los agentes prometen lo mismo con distintas palabras: *«la carpeta
de documentación de todos ellos, como esté»*, *«funciona con lo que haya»*, *«no pide
ordenar la carpeta antes de empezar»*. Y `portfolio-scan` lo dice como regla: **si la
estructura no está, agrupa por lo que digan los documentos y propón la estructura; no
la impongas.**

Esa promesa no tenía una sola comprobación detrás. Los tres corpus usaban todos el
mismo árbol ordenado, así que una regresión que hiciera el recorrido dependiente de la
estructura habría pasado las diecisiete puertas en verde.

Aquí se toma el corpus de Vera —el más grande, veintiocho documentos en seis
proyectos— y se emite **cuatro veces, en cuatro disposiciones distintas**, sin cambiar
una letra de su declaración. Después se corre `index()` sobre cada árbol y se compara:

    mismo número de documentos encontrados
    mismos hashes de contenido, sin importar la ruta
    ningún archivo perdido y ninguno duplicado

**Lo que esto NO prueba**, y hay que decirlo con el mismo tamaño de letra: que el modelo
agrupe bien los documentos en proyectos cuando no hay carpeta que los agrupe. Eso es
extracción, la hace el modelo y no el código, y sigue en la lista de lo que no se ha
probado. Lo que queda probado es el piso: que el recorrido los encuentra todos.
"""
import importlib.util
import shutil
import sys
import tempfile
from pathlib import Path

RAIZ = Path(__file__).parent.parent.parent
sys.path.insert(0, str(RAIZ / "plugins" / "criterio-portfolio" / "scripts"))
sys.path.insert(0, str(Path(__file__).parent))

import corpus  # noqa: E402
import portafolio  # noqa: E402

OK, FALLA = "ok   ", "FALLA"
fallas = []


def decir(marca, texto):
    print(f"  {marca}  {texto}")
    if marca == FALLA:
        fallas.append(texto)


def declaracion(plugin: str):
    """Importa un generador sin dejarlo escribir nada.

    Sus llamadas de nivel de módulo registran en el portafolio; el volcado a disco
    solo ocurre en su `__main__`, que aquí no corre. Por eso se puede leer el corpus
    como datos sin ensuciar el repositorio.
    """
    ruta = RAIZ / "tests" / plugin / "generar.py"
    spec = importlib.util.spec_from_file_location(f"gen_{plugin}", ruta)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo.PORTAFOLIO


def encontrados(carpeta: Path) -> dict:
    """Lo que `index()` ve en una carpeta vacía de estado: todo es nuevo."""
    with tempfile.TemporaryDirectory() as estado:
        d = portafolio.index(carpeta, Path(estado))
    return {f["path"]: f["hash"] for f in d["new"]}


print(__doc__.strip().splitlines()[0])

port = declaracion("criterio-portfolio")
print(f"\nEl corpus de Vera, leído como datos: {port.documentos} documentos en "
      f"{len(port.casos)} proyectos, sin tocar el disco")

base = Path(tempfile.mkdtemp(prefix="criterio-disposiciones-"))
try:
    vistos = {}
    for d in corpus.DISPOSICIONES:
        arbol = base / d
        port.volcar(d, arbol)
        vistos[d] = encontrados(arbol)
        print(f"\n{d}")
        if not vistos[d]:
            # Cero documentos encontrados es el modo de falla que esta prueba existe
            # para atrapar. Se reporta y se sigue: una prueba que se cae con un
            # traceback en vez de fallar limpio no dice qué se rompió.
            decir(FALLA, f"{d} · el recorrido no encontró NINGÚN documento")
            continue
        profundidad = max(len(Path(r).parts) for r in vistos[d])
        carpetas = len({str(Path(r).parent) for r in vistos[d]})
        print(f"  {len(vistos[d])} documentos · {carpetas} carpetas · "
              f"{profundidad} niveles de profundidad")

    print("\nEl recorrido encuentra lo mismo en las cuatro")
    referencia = vistos["referencia"]
    decir(OK if len(referencia) == port.documentos else FALLA,
          f"referencia · los {port.documentos} documentos declarados, encontrados")

    for d in corpus.DISPOSICIONES[1:]:
        decir(OK if len(vistos[d]) == len(referencia) else FALLA,
              f"{d} · {len(vistos[d])} documentos, contra {len(referencia)} de referencia")

    print("\nY el contenido es el mismo, aunque las rutas no lo sean")
    for d in corpus.DISPOSICIONES[1:]:
        iguales = bool(vistos[d]) and (
            sorted(vistos[d].values()) == sorted(referencia.values()))
        decir(OK if iguales else FALLA,
              f"{d} · los mismos hashes de contenido, uno a uno")
        distintas = set(vistos[d]) != set(referencia)
        decir(OK if distintas else FALLA,
              f"{d} · y las rutas sí cambiaron, así que la prueba no es trivial")

    print("\nNinguna disposición pierde ni duplica un archivo")
    for d in corpus.DISPOSICIONES:
        unicos = len(set(vistos[d].values()))
        decir(OK if len(vistos[d]) == port.documentos else FALLA,
              f"{d} · {len(vistos[d])} archivos en disco para "
              f"{port.documentos} documentos declarados ({unicos} contenidos distintos)")

    print("\nY el caso que nadie probaba")
    sin = vistos["sin_carpeta"]
    una_sola = bool(sin) and len({Path(r).parts[0] for r in sin}) == 1
    decir(OK if una_sola else FALLA,
          "sin_carpeta · ningún proyecto tiene carpeta propia y el recorrido los "
          "encuentra igual")
    hondo = max((len(Path(r).parts) for r in vistos["revuelta"]), default=0)
    decir(OK if hondo > 3 else FALLA,
          "revuelta · hay documentos más profundos que en la estructura de referencia")
finally:
    shutil.rmtree(base, ignore_errors=True)

print(f"\n{'el descubrimiento no depende del layout' if not fallas else f'{len(fallas)} FALLAS'}")
print("\nLo que esto no prueba: que el modelo agrupe bien los documentos en proyectos\n"
      "cuando no hay carpeta que los agrupe. Eso es extracción y sigue sin probarse.")
sys.exit(1 if fallas else 0)
