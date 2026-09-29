# -*- coding: utf-8 -*-
"""Qué tiene que hacer cada comando, y cómo se sabe que lo hizo.

    python3 tests/sintetico/funcionalidades.py            # la matriz
    python3 tests/sintetico/funcionalidades.py --verificar # puerta

Hasta aquí las pruebas decían «este comando se corrió». Eso no es validar una
funcionalidad: un comando puede correr, imprimir algo razonable y no hacer lo que promete.
Lo que hace falta es escrito de antemano —**qué tiene que producir** y **qué deja escrito
que lo pruebe**— para que después no se juzgue con la vara que convenga.

Tres columnas por comando, y ninguna es opinable:

    produce    lo que tiene que salir. Si no sale, falló.
    deja       lo que queda en disco y cualquiera puede abrir. Sin esto no hay historial.
    se_ve_en   dónde lo lee un director de PMO, un gerente o un patrocinador, sin pedirle
               permiso a nadie. Una funcionalidad que solo se puede verificar preguntándole
               al que la corrió no es transparente.

`deja` es lo que separa este diseño del anterior. Un comando que produce algo y no deja
registro no se puede auditar: su resultado vive en una conversación que se cierra. Los que
no dejan nada están marcados, y son deuda declarada.
"""
import argparse
import sys
from pathlib import Path

RAIZ = Path(__file__).parent.parent.parent
AGENTES = {"portfolio": "criterio-portfolio", "project": "criterio-project",
           "product": "criterio-product"}

# El histórico donde el lector entra. `corridas` es `<estado>/corridas/<fecha>-<que>.md`,
# que la corrida escribe sola; `portal` es una ruta de Rostrum.
PORTAL = "portal · Rostrum"
CORRIDAS = "corridas · <estado>/corridas/"
FICHA = "la ficha · <estado>/records/"

FUNCIONALIDADES = {
    # ── Vera · el portafolio
    "portfolio-setup": ("La configuración y el primer informe sobre los documentos propios",
                        "la configuración y el estado inicial y la corrida", PORTAL),
    "portfolio-wake": ("Lo que toca hoy — y silencio si no toca nada",
                       "la fecha de la última corrida en cadencia.json", CORRIDAS),
    "document-index": ("Qué cambió de verdad y qué no hubo que releer",
                       "la corrida", CORRIDAS),
    "portfolio-scan": ("Una ficha por proyecto, con cita en cada dato",
                       "la ficha, la instantánea y la corrida", FICHA),
    "portfolio-report": ("Qué cambió, qué se contradice, qué está en silencio",
                         "el informe publicado y la corrida", PORTAL),
    "status-report": ("El semáforo declarado contra lo que no explica", "la corrida", PORTAL),
    "health-check": ("El diagnóstico de un proyecto desde cero", "la corrida", CORRIDAS),
    "project-history": ("Desde cuándo lo declarado dejó de sostenerse",
                        "la corrida", PORTAL + " · /historia/<código>"),
    "raid-log": ("Riesgos y dependencias, incluidos los dichos y no registrados",
                 "la corrida", CORRIDAS),
    "change-control": ("A quién alcanza mover un proyecto", "la corrida", CORRIDAS),
    "budget-tracking": ("Las cuatro cifras y la desviación contra las dos líneas base",
                        "la corrida", PORTAL),
    "vendor-tracking": ("Contrato contra acta de recibo contra factura", "la corrida", PORTAL),
    "product-view": ("Un producto a través de los proyectos que lo construyen",
                     "la corrida", PORTAL + " · /productos"),
    "project-charter": ("Qué le falta a un acta y qué consecuencia tiene", "la corrida", CORRIDAS),
    "project-closure": ("El cierre contra el criterio pactado", "la corrida", CORRIDAS),
    "steering-pack": ("El material del comité como paquete de decisiones",
                      "la corrida", PORTAL + " · /decisiones"),
    "portfolio-server": ("Rostrum sirviendo el informe y recibiendo preguntas",
                         "las peticiones en <estado>/peticiones/ y la corrida", PORTAL),
    # ── Samuel · el proyecto
    "pm-setup": ("El agente listo sobre un proyecto", "la configuración y la corrida", CORRIDAS),
    "pm-wake": ("Lo que toca hoy en este proyecto", "la fecha en cadencia.json", CORRIDAS),
    "pm-agenda": ("La agenda de la reunión desde lo que quedó abierto", "la corrida", CORRIDAS),
    "pm-minutes": ("Los compromisos de la minuta, con doliente y fecha",
                   "la ficha y la corrida", CORRIDAS),
    "pm-commitments": ("El compromiso reprogramado reconocido como uno, no como tres",
                       "la corrida", CORRIDAS),
    "pm-report": ("El informe del proyecto contra la corrida anterior",
                  "la instantánea y la corrida", CORRIDAS),
    "pm-plan": ("El plan y su desviación contra la línea base", "la corrida", CORRIDAS),
    "pm-escalate": ("Lo que excede la facultad del gerente", "la corrida", CORRIDAS),
    "pm-publish": ("La ficha publicada donde el portafolio la lea",
                   "la ficha publicada y la corrida", FICHA),
    # ── Alba · el producto
    "product-setup": ("El agente listo sobre un producto", "la configuración y la corrida", CORRIDAS),
    "product-wake": ("Lo que toca hoy en este producto", "la fecha en cadencia.json", CORRIDAS),
    "product-discovery": ("La evidencia de demanda, con quién lo pidió y cuándo",
                          "la corrida", CORRIDAS),
    "product-requirements": ("Los requerimientos con doliente, criterio y evidencia",
                             "el registro y la corrida", CORRIDAS),
    "product-definition": ("Qué de la definición sostiene la evidencia y qué se sostiene solo",
                           "el registro y la corrida", CORRIDAS),
    "product-trace": ("Lo que se decidió construir y nadie está construyendo",
                      "la corrida", CORRIDAS),
    "product-spec": ("La especificación de lo decidido", "la corrida", CORRIDAS),
    "product-business-case": ("Lo declarado contra lo que la métrica mide", "la corrida", CORRIDAS),
    "product-charter": ("El acta que abre el proyecto que lo construye", "la corrida", CORRIDAS),
    "product-overlap": ("Los productos que comparten métrica, proyecto o segmento",
                        "la corrida", CORRIDAS),
    "product-publish": ("El registro publicado donde el portafolio lo cruce",
                        "el registro publicado y la corrida", FICHA),
}


def comandos() -> dict:
    return {c.stem: plug for plug in AGENTES.values()
            for c in (RAIZ / "plugins" / plug / "commands").glob("*.md")}


def matriz() -> int:
    cmds = comandos()
    por_plugin = {}
    for c, plug in cmds.items():
        por_plugin.setdefault(plug, []).append(c)
    for plug in AGENTES.values():
        print(f"\n{plug}")
        print(f"  {'comando':24} {'qué produce':52} {'qué deja':38} dónde se lee")
        for c in sorted(por_plugin.get(plug, [])):
            f = FUNCIONALIDADES.get(c)
            if not f:
                print(f"  {c:24} SIN DECLARAR")
                continue
            produce, deja, ve = f
            print(f"  {c:24} {produce[:52]:52} "
                  f"{(deja or '— nada'):38} {ve or '— solo en la sesión'}")
    sin_rastro = [c for c, f in FUNCIONALIDADES.items() if not f[1]]
    sin_lector = [c for c, f in FUNCIONALIDADES.items() if not f[2]]
    print(f"\n{len(FUNCIONALIDADES)} funcionalidades declaradas")
    print(f"  {len(FUNCIONALIDADES) - len(sin_rastro)} dejan rastro en disco · "
          f"{len(sin_rastro)} no dejan nada")
    print(f"  {len(FUNCIONALIDADES) - len(sin_lector)} se pueden leer sin preguntarle a "
          f"nadie · {len(sin_lector)} solo viven en la sesión")
    print("\nLos que no dejan rastro son deuda declarada, no un descuido: su resultado "
          "vive\nen una conversación que se cierra, y eso no se puede auditar.")
    return 0


def verificar() -> int:
    """Puerta: la declaración y los comandos que existen tienen que coincidir."""
    cmds, malas = comandos(), []
    for c in sorted(cmds):
        if c not in FUNCIONALIDADES:
            malas.append(f"{c} existe y no declara qué tiene que producir")
    for c in sorted(FUNCIONALIDADES):
        if c not in cmds:
            malas.append(f"{c} está declarado y no existe como comando")
    for c, f in FUNCIONALIDADES.items():
        if len(f) != 3 or not f[0]:
            malas.append(f"{c} no dice qué produce")
    if malas:
        for m in malas:
            print(f"  FALLA {m}")
        print(f"\n{len(malas)} funcionalidades sin cuadrar")
        return 1
    con_rastro = sum(1 for f in FUNCIONALIDADES.values() if f[1])
    print(f"  OK    las {len(cmds)} funcionalidades declaran qué producen · "
          f"{con_rastro} dejan rastro auditable")
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--verificar", action="store_true")
    a = ap.parse_args()
    raise SystemExit(verificar() if a.verificar else matriz())
