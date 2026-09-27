# -*- coding: utf-8 -*-
"""Genera el material sintético de criterio-product y los registros de referencia.

    python3 tests/criterio-product/generar.py

Dos productos, y el segundo es la mitad del valor de la prueba:

- **PRD-QR · Pagos QR** — un producto con los diez hallazgos plantados: la cifra del caso
  de negocio que la métrica contradice, el requerimiento aceptado que nadie pidió, el
  decidido que ningún proyecto ejecuta, el que dice ejecutarse en un proyecto cuya ficha
  dice otro producto, el supuesto de marzo que nadie verificó, el propuesto en mayo que
  nadie decide, la evidencia de hace año y medio, y el descarte que no quedó en ningún acta.
- **PRD-NOMINA · Dispersión de nómina** — **control negativo.** Tiene definición,
  entrevistas, métricas, cinco documentos y tres requerimientos, y **no produce ni un
  hallazgo.** Un agente que encuentra algo ahí es un generador de ruido, y eso no se detecta
  mirando solo los casos que sí fallan.

Fecha de referencia: **2026-11-20**, la misma del corpus de criterio-project, para que los dos
se puedan leer juntos.

Regla que este generador respeta y que ya se rompió una vez en el otro corpus: **todo campo
de un registro de referencia cita un documento que de verdad lo dice.** Un registro que cita
un acta que nunca dijo eso es exactamente el error que este diseño existe para evitar,
sentado dentro del material de prueba.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

RAIZ = Path(__file__).parent
INPUT = RAIZ / "input"
EXPECTED = RAIZ / "expected"
HOY = "2026-11-20"


sys.path.insert(0, str(Path(__file__).parent.parent / "sintetico"))
import corpus  # noqa: E402  el motor: la estructura, las disposiciones y la escritura

# El corpus no va a disco a medida que se declara: lo acumula el portafolio, y al final
# `volcar()` lo escribe con la disposición que se le pida. Esa es la razón de ser del
# motor — la misma declaración puede salir ordenada, plana, revuelta o sin carpetas, y
# así se prueba que el descubrimiento no dependa de dónde quedaron los archivos.
PORTAFOLIO = corpus.Portafolio(INPUT, corpus.normal_crudo)


def escribir(ruta, texto):
    """Registra si es material de entrada; escribe de una si es una respuesta.

    Las fichas y los hallazgos de `expected/` son respuestas, no insumo: esos sí se
    escriben aquí mismo.
    """
    ruta = Path(ruta)
    try:
        relativa = ruta.relative_to(INPUT)
    except ValueError:
        return corpus.escribir_suelto(ruta, texto, corpus.normal_crudo)
    return PORTAFOLIO.escribir(relativa, texto)


def json_a(ruta: Path, dato) -> None:
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(json.dumps(dato, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


# ══════════════════════════════════ PRD-QR ══════════════════════════════════

QR = INPUT / "PRD-QR"

CASO_QR = """
# Caso de negocio — Pagos QR

**Producto:** PRD-QR · Pagos QR
**Autora:** Marcela Ruiz, gerente de producto
**Fecha:** 4 de marzo de 2026
**Quién decide qué se construye:** Comité de producto

## El problema

El comercio pequeño que recibe un pago por QR no sabe si la transacción entró hasta que
revisa el extracto del día siguiente. Mientras tanto el cliente ya se fue. Hoy lo resuelve
llamando a la línea de atención, que atiende cerca de 4.000 llamadas al mes por esta única
razón.

## Para quién

Comercios con facturación mensual por debajo de los 30 millones que ya reciben recaudo por
QR y no tienen sistema de punto de venta integrado.

## Criterio de éxito

Al cierre del primer año: **250.000 transacciones mensuales** confirmadas por el canal QR, y
**1.200 comercios activos** en el canal.

## Supuestos de los que depende esto

- **El comercio tiene conexión de datos en el punto de venta al momento del pago.** No
  verificado: no hemos medido conectividad en sitio.
- El switch interoperable responde en menos de 2 s. Verificado con el proveedor en la
  prueba de carga del 18 de febrero de 2026.
"""

VISITA_QR = """
# Notas de visita a comercios — 2 de mayo de 2026

**Quién fue:** Marcela Ruiz · **Comercios visitados:** 5, zona centro

Notas tomadas en sitio, sin grabación.

- **Comercio 11 (papelería).** Pregunta si se puede devolver solo una parte del pago cuando
  el cliente se lleva menos de lo que pagó. *«Me toca devolverle en efectivo y me queda el
  cuadre mal.»*
- **Comercio 12 (cafetería).** Lo mismo, y agrega que le pasa dos o tres veces por semana.
- **Comercio 13 (droguería).** No lo menciona. Le preocupa más la comisión.
- **Comercio 14 (miscelánea).** *«Si eso se puede devolver por el mismo QR, mejor.»*
- **Comercio 15 (panadería).** No lo menciona.

**Supuesto que estoy asumiendo al escribir esto:** que el comercio acepta hacer la
devolución por el mismo canal en vez de en efectivo. No lo hemos preguntado directamente.
"""

ENTREVISTAS_QR = """
# Entrevistas a comercios — ronda de septiembre

**Fechas:** 28 de agosto al 1 de septiembre de 2026
**Quién:** Marcela Ruiz y Julián Estrada · **Comercios:** 8 · **Transcripción:** completa

## Lo que se preguntó

Cómo saben hoy que un pago entró, qué hacen cuando no están seguros, y qué les costaría más
si no existiera el canal.

## Comercio 1 — ferretería

> *«Yo termino llamando para saber si entró. Y si hay fila, no llamo, y quedo con la duda.»*

## Comercio 2 — restaurante

> *«A mí el mesero me pregunta y yo no sé qué decirle. Eso es lo que me molesta.»*

## Comercio 3 — tienda de barrio

> *«El cliente ya se fue y yo todavía no sé. Después me toca buscarlo en el extracto.»*

## Comercio 4 — óptica

> *«Con la factura electrónica ya me pasó que cobré dos veces por no saber.»*

## Comercio 5 — papelería

No lo menciona como problema. Dice que revisa el extracto en la noche y le sirve así.

## Comercio 6 — carnicería

> *«Necesito que me suene el teléfono cuando entra la plata. Nada más.»*

## Comercio 7 — floristería

> *«Yo llamo. Todos los días llamo por lo menos una vez.»*

## Comercio 8 — panadería

No lo menciona. Le preocupa el tiempo que tarda el dinero en estar disponible.

## Conteo

**6 de 8** describen no saber si el pago entró como su problema principal con el canal.
**2 de 8** no lo mencionan.
"""

TICKET_QR = """
# Ticket 4471 — conciliación diaria

**Abierto:** 10 de junio de 2025 · **Quién:** Operaciones, Andrés Peña
**Producto:** PRD-QR

Operaciones pide que la conciliación del canal QR se haga automática contra el archivo del
switch. Hoy se hace a mano, una persona, dos horas cada mañana.

**Estado del ticket:** abierto, sin movimiento desde la fecha de apertura.
"""

TABLERO_QR = """
# Tablero transaccional — canal QR

**Fuente:** reporte mensual del tablero transaccional · **Corte:** 1 de septiembre de 2026

**Definición de la métrica:** transacciones confirmadas del canal QR, sin reversiones.

| Mes | Transacciones |
|---|---|
| junio 2026 | 132.000 |
| julio 2026 | 141.000 |
| agosto 2026 | 150.000 |
| septiembre 2026 | 180.000 |

**Comercios activos** — comercios con al menos una transacción en el mes.

| Mes | Comercios |
|---|---|
| septiembre 2026 | 1.150 |
"""

COMITE_QR = """
# Comité de producto — 8 de octubre de 2026

**Asistieron:** Comité de producto · Marcela Ruiz (gerente de producto)

## Decisiones

**1. Confirmación del pago al comercio.** Se aprueba construirlo. Entra en el alcance del
proyecto **PRY-101 Pasarela de pagos QR**. Doliente: Marcela Ruiz.

**2. Cobro recurrente para comercios de suscripción.** Se aprueba construirlo. **No se
asigna proyecto todavía**; se revisará en el comité siguiente. Doliente: Marcela Ruiz.

**3. Conciliación diaria automática.** Se aprueba construirlo. Se asigna al proyecto
**PRY-105**. Doliente: el área de Operaciones.

## Sin decisión

Devoluciones parciales por el mismo QR: se menciona y **no se decide**. Marcela pide
evidencia adicional antes de llevarlo a decisión.
"""


def qr() -> tuple[dict, dict, list]:
    escribir(QR / "00-definicion" / "2026-03-04-caso-de-negocio.md", CASO_QR)
    escribir(QR / "10-descubrimiento" / "2026-05-02-notas-visita-comercios.md", VISITA_QR)
    escribir(QR / "10-descubrimiento" / "2026-09-01-entrevistas-comercios.md", ENTREVISTAS_QR)
    escribir(QR / "10-descubrimiento" / "2025-06-10-ticket-4471-conciliacion.md", TICKET_QR)
    escribir(QR / "20-metricas" / "2026-09-01-tablero-transaccional.md", TABLERO_QR)
    escribir(QR / "30-decisiones" / "2026-10-08-comite-producto.md", COMITE_QR)

    caso = "00-definicion/2026-03-04-caso-de-negocio.md"
    entrevistas = "10-descubrimiento/2026-09-01-entrevistas-comercios.md"
    visita = "10-descubrimiento/2026-05-02-notas-visita-comercios.md"
    ticket = "10-descubrimiento/2025-06-10-ticket-4471-conciliacion.md"
    comite = "30-decisiones/2026-10-08-comite-producto.md"

    producto = {
        "identity": {
            "code": "PRD-QR",
            "name": {"value": "Pagos QR", "source": caso, "source_date": "2026-03-04"},
            "manager": {"value": "Marcela Ruiz", "source": caso, "source_date": "2026-03-04"},
            "authority": {"value": "Comité de producto", "source": caso,
                          "source_date": "2026-03-04"},
        },
        "definition": {
            "problem": {"value": "el comercio no sabe si el pago entró hasta el extracto "
                                 "del día siguiente", "source": caso,
                        "source_date": "2026-03-04"},
            "who": {"value": "comercios con recaudo QR y sin punto de venta integrado",
                    "source": caso, "source_date": "2026-03-04"},
            "success": {"value": "250.000 transacciones mensuales y 1.200 comercios activos "
                                 "al cierre del primer año", "source": caso,
                        "source_date": "2026-03-04"},
            "claims": [
                {"metric": "tx_mensuales", "declared": 250000, "source": caso,
                 "source_date": "2026-03-04"},
                {"metric": "comercios_activos", "declared": 1200, "source": caso,
                 "source_date": "2026-03-04"},
            ],
            "assumptions": [
                # El que nadie verificó, y está escrito en el caso de negocio como no
                # verificado: el hallazgo no es que falte, es que lleva ocho meses así.
                {"value": "el comercio tiene conexión de datos en el punto de venta al "
                          "momento del pago", "verified": False, "stated_on": "2026-03-04",
                 "source": caso},
                {"value": "el switch interoperable responde en menos de 2 s",
                 "verified": True, "stated_on": "2026-03-04", "source": caso},
            ],
        },
        "activity": {"last_document_date": "2026-10-08"},
    }

    metricas = {
        "tx_mensuales": {
            "metric": "tx_mensuales",
            "source": "20-metricas/2026-09-01-tablero-transaccional.md",
            "definition": "transacciones confirmadas del canal QR, sin reversiones",
            "series": [{"date": "2026-06-01", "value": 132000},
                       {"date": "2026-07-01", "value": 141000},
                       {"date": "2026-08-01", "value": 150000},
                       {"date": "2026-09-01", "value": 180000}],
        },
        "comercios_activos": {
            "metric": "comercios_activos",
            "source": "20-metricas/2026-09-01-tablero-transaccional.md",
            "definition": "comercios con al menos una transacción en el mes",
            "series": [{"date": "2026-09-01", "value": 1150}],
        },
    }

    reqs = [
        # Limpio. Existe para que el grader distinga «no encuentra nada» de «no mira».
        {"id": "REQ-001",
         "title": {"value": "Confirmar el pago sin llamar a la línea de atención",
                   "source": entrevistas, "source_date": "2026-09-01"},
         "product": "PRD-QR", "state": "aceptado", "stated_on": "2026-09-01",
         "owner": {"value": "Marcela Ruiz", "kind": "person", "source": comite},
         "need": {"value": "saber en el momento si la transacción entró",
                  "source": entrevistas, "source_date": "2026-09-01"},
         "acceptance": [{"value": "la confirmación llega al comercio en menos de 3 s en el "
                                  "percentil 95", "source": comite}],
         "evidence": [{"value": "6 de 8 comercios lo describen como su problema principal",
                       "source": entrevistas, "source_date": "2026-09-01"}],
         "decision": {"what": {"value": "se aprueba construirlo", "source": comite},
                      "who": "Comité de producto", "on": "2026-10-08"},
         "traces": {"project": "PRY-101", "deliverables": []}},

        # Aceptado y nadie lo pidió, y sin proyecto. Las dos cosas están en el acta.
        {"id": "REQ-002",
         "title": {"value": "Cobro recurrente para comercios de suscripción",
                   "source": comite, "source_date": "2026-10-08"},
         "product": "PRD-QR", "state": "aceptado", "stated_on": "2026-10-08",
         "owner": {"value": "Marcela Ruiz", "kind": "person", "source": comite},
         "acceptance": [{"value": "el cobro se ejecuta el mismo día del mes sin intervención",
                         "source": comite}],
         "evidence": [],
         "decision": {"what": {"value": "se aprueba construirlo", "source": comite},
                      "who": "Comité de producto", "on": "2026-10-08"},
         "traces": {}},

        # Área en vez de persona, sin criterio, evidencia de hace año y medio, y la traza
        # apunta a un proyecto cuya ficha dice que ejecuta otro producto.
        {"id": "REQ-003",
         "title": {"value": "Conciliación diaria automática contra el archivo del switch",
                   "source": ticket, "source_date": "2025-06-10"},
         "product": "PRD-QR", "state": "aceptado", "stated_on": "2025-06-10",
         "owner": {"value": "Operaciones", "kind": "area", "source": comite},
         "acceptance": [],
         "evidence": [{"value": "ticket 4471 de Operaciones", "source": ticket,
                       "source_date": "2025-06-10"}],
         "decision": {"what": {"value": "se aprueba construirlo", "source": comite},
                      "who": "Comité de producto", "on": "2026-10-08"},
         "traces": {"project": "PRY-105", "deliverables": []}},

        # Propuesto en mayo y nadie lo decide, con su supuesto sin verificar.
        {"id": "REQ-004",
         "title": {"value": "Devolución parcial por el mismo QR", "source": visita,
                   "source_date": "2026-05-02"},
         "product": "PRD-QR", "state": "propuesto", "stated_on": "2026-05-02",
         "owner": {"value": "Marcela Ruiz", "kind": "person", "source": visita},
         "need": {"value": "devolver una parte del pago sin usar efectivo", "source": visita,
                  "source_date": "2026-05-02"},
         "acceptance": [],
         "evidence": [{"value": "3 de 5 comercios visitados lo piden", "source": visita,
                       "source_date": "2026-05-02"}],
         "assumptions": [{"value": "el comercio acepta devolver por el mismo canal en vez "
                                   "de en efectivo", "verified": False,
                          "stated_on": "2026-05-02", "source": visita}],
         "traces": {}},

        # Descartado, y el descarte no está en ningún acta. Es el estado que más se pierde.
        # Y va más lejos: ningún documento del expediente lo menciona, así que su título y
        # su doliente están en `not_found`. Por eso aporta dos hallazgos y no uno — alguien
        # escribió una entrada del registro y no hay papel detrás de nada de ella.
        {"id": "REQ-005",
         "title": {"value": "Pago con QR sin conexión", "source": None,
                   "state": "not_found"},
         "product": "PRD-QR", "state": "descartado", "stated_on": "2026-04-15",
         "owner": {"value": "Julián Estrada", "kind": "person", "source": None,
                   "state": "not_found"},
         "acceptance": [],
         "evidence": [],
         "decision": {"what": "no se hace", "who": "Marcela Ruiz", "on": "2026-06-30"},
         "traces": {}},
    ]
    return producto, metricas, reqs


# ═══════════════════════════ PRD-NOMINA · control negativo ═══════════════════

NOM = INPUT / "PRD-NOMINA"

CASO_NOM = """
# Caso de negocio — Dispersión de nómina

**Producto:** PRD-NOMINA · Dispersión de nómina
**Autor:** Julián Estrada, gerente de producto
**Fecha:** 12 de agosto de 2026
**Quién decide qué se construye:** Comité de producto

## El problema

La empresa mediana que paga nómina desde el portal carga un archivo plano y no sabe qué
pagos fallaron hasta el día siguiente, cuando el empleado reclama.

## Para quién

Empresas de entre 20 y 300 empleados que ya pagan nómina por el portal empresarial.

## Criterio de éxito

Al cierre del primer semestre: **50.000 dispersiones mensuales** procesadas por el canal.

## Supuestos de los que depende esto

- El archivo de nómina de estas empresas trae el número de cuenta del empleado. **Verificado**
  con la muestra de 40 archivos revisada el 20 de agosto de 2026.
"""

ENTREVISTAS_NOM = """
# Entrevistas a empresas — agosto de 2026

**Fechas:** 18 al 22 de agosto de 2026 · **Quién:** Julián Estrada · **Empresas:** 6

## Empresa 1 — manufactura, 180 empleados

> *«Yo me entero de que un pago falló cuando el empleado me escribe. Eso no puede ser.»*

## Empresa 2 — servicios, 45 empleados

> *«Necesito saber cuál falló y por qué, en la misma pantalla.»*

## Empresa 3 — comercio, 90 empleados

> *«Lo que me sirve es poder reintentar solo el que falló, sin volver a cargar todo.»*

## Empresa 4 — logística, 260 empleados

> *«Igual. Y que quede el registro de quién autorizó el reintento.»*

## Empresa 5 — salud, 120 empleados

> *«A mí me pasa poco, pero cuando pasa es un problema grande.»*

## Empresa 6 — educación, 30 empleados

> *«Sí, saber cuál falló.»*

## Conteo

**6 de 6** piden ver el resultado por empleado en el momento.
**4 de 6** piden reintentar solo el fallido.
**1 de 6** pide el registro de quién autorizó el reintento.
"""

TABLERO_NOM = """
# Tablero de dispersiones — canal nómina

**Fuente:** reporte mensual del tablero de dispersiones · **Corte:** 1 de noviembre de 2026

**Definición de la métrica:** dispersiones procesadas del canal nómina, incluidas las
fallidas.

| Mes | Dispersiones |
|---|---|
| septiembre 2026 | 48.000 |
| octubre 2026 | 52.000 |
"""

COMITE_NOM = """
# Comité de producto — 15 de octubre de 2026

**Asistieron:** Comité de producto · Julián Estrada (gerente de producto)

## Decisiones

**1. Resultado por empleado en el momento de la dispersión.** Se aprueba construirlo. Entra
en el alcance del proyecto **PRY-201 Portal empresarial · nómina**. Doliente: Julián Estrada.

**2. Reintento del pago fallido sin recargar el archivo.** Se aprueba construirlo. Entra en
el alcance del proyecto **PRY-202 Reintentos de dispersión**. Doliente: Paula Mejía.

## Para el comité siguiente

Registro de quién autorizó el reintento: se recibe la propuesta el 5 de noviembre y queda
para decisión en el comité de diciembre. Doliente propuesto: Paula Mejía.
"""


def nomina() -> tuple[dict, dict, list]:
    escribir(NOM / "00-definicion" / "2026-08-12-caso-de-negocio.md", CASO_NOM)
    escribir(NOM / "10-descubrimiento" / "2026-08-22-entrevistas-empresas.md", ENTREVISTAS_NOM)
    escribir(NOM / "20-metricas" / "2026-11-01-tablero-dispersiones.md", TABLERO_NOM)
    escribir(NOM / "30-decisiones" / "2026-10-15-comite-producto.md", COMITE_NOM)

    caso = "00-definicion/2026-08-12-caso-de-negocio.md"
    entrevistas = "10-descubrimiento/2026-08-22-entrevistas-empresas.md"
    comite = "30-decisiones/2026-10-15-comite-producto.md"

    producto = {
        "identity": {
            "code": "PRD-NOMINA",
            "name": {"value": "Dispersión de nómina", "source": caso,
                     "source_date": "2026-08-12"},
            "manager": {"value": "Julián Estrada", "source": caso,
                        "source_date": "2026-08-12"},
            "authority": {"value": "Comité de producto", "source": caso,
                          "source_date": "2026-08-12"},
        },
        "definition": {
            "problem": {"value": "la empresa no sabe qué pagos de nómina fallaron hasta que "
                                 "el empleado reclama", "source": caso,
                        "source_date": "2026-08-12"},
            "who": {"value": "empresas de 20 a 300 empleados que pagan nómina por el portal",
                    "source": caso, "source_date": "2026-08-12"},
            "success": {"value": "50.000 dispersiones mensuales al cierre del primer semestre",
                        "source": caso, "source_date": "2026-08-12"},
            # Declarado 50.000, medido 52.000: 4% de diferencia. Por debajo del umbral, así
            # que no es contradicción. Está aquí a propósito: es el caso que un agente
            # ruidoso reportaría.
            "claims": [{"metric": "dispersiones_mensuales", "declared": 50000,
                        "source": caso, "source_date": "2026-08-12"}],
            "assumptions": [{"value": "el archivo de nómina trae el número de cuenta del "
                                      "empleado", "verified": True,
                             "stated_on": "2026-08-12", "source": caso}],
        },
        "activity": {"last_document_date": "2026-11-01"},
    }

    metricas = {"dispersiones_mensuales": {
        "metric": "dispersiones_mensuales",
        "source": "20-metricas/2026-11-01-tablero-dispersiones.md",
        "definition": "dispersiones procesadas del canal nómina, incluidas las fallidas",
        "series": [{"date": "2026-09-01", "value": 48000},
                   {"date": "2026-10-01", "value": 52000}]}}

    reqs = [
        {"id": "REQ-101",
         "title": {"value": "Resultado por empleado en el momento de la dispersión",
                   "source": entrevistas, "source_date": "2026-08-22"},
         "product": "PRD-NOMINA", "state": "aceptado", "stated_on": "2026-08-22",
         "owner": {"value": "Julián Estrada", "kind": "person", "source": comite},
         "need": {"value": "saber cuál pago falló sin esperar el reclamo del empleado",
                  "source": entrevistas, "source_date": "2026-08-22"},
         "acceptance": [{"value": "el resultado por empleado se ve en la misma pantalla al "
                                  "terminar la dispersión", "source": comite}],
         "evidence": [{"value": "6 de 6 empresas lo piden", "source": entrevistas,
                       "source_date": "2026-08-22"}],
         "decision": {"what": {"value": "se aprueba construirlo", "source": comite},
                      "who": "Comité de producto", "on": "2026-10-15"},
         "traces": {"project": "PRY-201", "deliverables": []}},

        {"id": "REQ-102",
         "title": {"value": "Reintento del pago fallido sin recargar el archivo",
                   "source": entrevistas, "source_date": "2026-08-22"},
         "product": "PRD-NOMINA", "state": "aceptado", "stated_on": "2026-08-22",
         "owner": {"value": "Paula Mejía", "kind": "person", "source": comite},
         "acceptance": [{"value": "se reintenta solo el registro fallido, sin volver a "
                                  "cargar el archivo", "source": comite}],
         "evidence": [{"value": "4 de 6 empresas lo piden", "source": entrevistas,
                       "source_date": "2026-08-22"}],
         "decision": {"what": {"value": "se aprueba construirlo", "source": comite},
                      "who": "Comité de producto", "on": "2026-10-15"},
         "traces": {"project": "PRY-202", "deliverables": []}},

        # Propuesto hace quince días: todavía no es una decisión que no se toma. Está aquí
        # para que el control negativo tenga un propuesto y siga en cero.
        {"id": "REQ-103",
         "title": {"value": "Registro de quién autorizó el reintento", "source": comite,
                   "source_date": "2026-10-15"},
         "product": "PRD-NOMINA", "state": "propuesto", "stated_on": "2026-11-05",
         "owner": {"value": "Paula Mejía", "kind": "person", "source": comite},
         "evidence": [{"value": "1 de 6 empresas lo pide", "source": entrevistas,
                       "source_date": "2026-08-22"}],
         "acceptance": [],
         "traces": {}},
    ]
    return producto, metricas, reqs


# ═══════════════════════ las fichas de proyecto que confirman ════════════════
# Alba no le cree a su propio registro: la traza se confirma contra la ficha del proyecto,
# que tiene otro dueño. PRY-105 existe y dice que ejecuta otro producto — ese desacuerdo es
# el hallazgo, y tiene que estar en el material para poder probarlo.

FICHAS = {
    "PRY-101": "PRD-QR",
    "PRY-105": "PRD-ORIGINACION",
    "PRY-201": "PRD-NOMINA",
    "PRY-202": "PRD-NOMINA",
}


def fichas() -> None:
    for codigo, producto in FICHAS.items():
        json_a(EXPECTED / "fichas" / f"{codigo}.json", {
            "identity": {"code": codigo,
                         "name": {"value": f"Proyecto {codigo}", "source": "acta"},
                         "product": {"value": producto, "source": "acta"}}})


# ═══════════════════════ los productos que otros publicaron ══════════════════
# Alba trabaja sobre un producto. La pregunta que un producto solo no puede responder
# —¿nos estamos pisando con otro?— necesita que los demás hayan publicado, y eso es un
# acto de otro gerente de producto, no un efecto. Aquí está lo que publicaron.
#
# PRD-COBROS existe por una razón concreta y no por simetría: **PRD-QR aceptó el cobro
# recurrente (REQ-002), no le puso proyecto, y resulta que otro producto lo está
# construyendo.** Ese es el caso real, el que nadie hizo a propósito, y el que solo
# aparece cuando los dos registros se cruzan.

PUBLICADOS = {
    "PRD-COBROS": {
        "code": "PRD-COBROS",
        "name": "Cobros recurrentes",
        "manager": "Julián Estrada",
        "as_of": HOY,
        # el mismo segmento, escrito por otra persona: mayúsculas y tildes distintas
        "who": "Comercios con recaudo QR y sin Punto de Venta integrado",
        # la misma métrica que PRD-QR afirma. Los dos casos de negocio cuentan las
        # mismas transacciones, y el comité vio las dos cifras sumadas.
        "claims": [{"metric": "tx_mensuales", "declared": 90000,
                    "source": "00-definicion/2026-05-02-caso-de-negocio-cobros.md",
                    "source_date": "2026-05-02"}],
        "projects": ["PRY-101"],
        "requirements": [
            {"id": "REQ-501", "title": "Cobro recurrente para comercios de suscripción",
             "state": "aceptado", "project": "PRY-101"},
            {"id": "REQ-502", "title": "Reintento del cobro rechazado",
             "state": "propuesto", "project": None},
        ],
    },
    # El control negativo del cruce: un producto publicado que no se pisa con nada.
    "PRD-NOMINA": {
        "code": "PRD-NOMINA",
        "name": "Dispersión de nómina",
        "manager": "Julián Estrada",
        "as_of": HOY,
        "who": "empresas de 20 a 300 empleados que pagan nómina por el portal",
        "claims": [{"metric": "dispersiones_mensuales", "declared": 50000,
                    "source": "00-definicion/2026-08-12-caso-de-negocio.md",
                    "source_date": "2026-08-12"}],
        "projects": ["PRY-201", "PRY-202"],
        "requirements": [
            {"id": "REQ-101", "title": "Resultado por empleado en el momento de la dispersión",
             "state": "aceptado", "project": "PRY-201"},
            {"id": "REQ-102", "title": "Reintento del pago fallido sin recargar el archivo",
             "state": "aceptado", "project": "PRY-202"},
        ],
    },
}


def publicados() -> None:
    for codigo, ficha in PUBLICADOS.items():
        json_a(EXPECTED / "publicados" / f"{codigo}.json", ficha)


# ══════════════════════════ las respuestas a mano ════════════════════════════
# Escritas leyendo los documentos, no calculándolas. Si salieran de las mismas fórmulas que
# el código, esto no probaría nada.

HALLAZGOS = {
    "as_of": HOY,
    "PRD-QR": {
        "_porque": "los diez hallazgos plantados, cada uno con su documento",
        "requirements": 5,
        "by_state": {"aceptado": 3, "propuesto": 1, "descartado": 1},
        "decided": 3,
        "with_evidence": 2,
        "traced": 2,
        "with_evidence_pct": 66.7,
        "traced_pct": 66.7,
        "unknown": [],
        "por_senal": {
            # Dos: REQ-003 tiene un área en vez de una persona, y el doliente de
            # REQ-005 no sale de ningún documento. Son dos formas distintas de no tener
            # doliente, y las dos son decoración.
            "requirement_without_owner": 2,
            "requirement_without_acceptance": 1,
            "requirement_accepted_without_evidence": 1,
            "requirement_undecided": 1,
            "requirement_untraced": 1,
            "trace_not_confirmed": 1,
            "decision_without_source": 1,
            "assumption_unverified": 2,
            "evidence_stale": 1,
            "claim_vs_metric": 1,
        },
        "claim_gap_pct": 28.0,
        "trace_says": "PRD-ORIGINACION",
        "evidence_stale_months": 17,
        "undecided_days": 202,
        "signals": [
            "assumption_unverified", "claim_vs_metric", "decision_without_source",
            "evidence_stale", "requirement_accepted_without_evidence",
            "requirement_undecided", "requirement_untraced",
            "requirement_without_acceptance", "requirement_without_owner",
            "trace_not_confirmed",
        ],
    },
    # Dónde PRD-QR se pisa con lo que otros publicaron. Leído a mano:
    # PRD-COBROS afirma `tx_mensuales` igual que PRD-QR —los dos casos de negocio
    # cuentan las mismas transacciones—, construye en PRY-101 igual que REQ-001, y
    # dice servir al mismo segmento escrito con otras mayúsculas. PRD-NOMINA no se
    # pisa con nada, y está publicado para probar exactamente eso.
    "solapamiento": {
        "_porque": ("PRD-QR aceptó el cobro recurrente y no le puso proyecto; otro "
                    "producto lo está construyendo, y los dos casos de negocio cuentan "
                    "las mismas transacciones"),
        "producto": "PRD-QR",
        "lee": ["PRD-COBROS", "PRD-NOMINA"],
        "metricas": 1,
        "metrica": "tx_mensuales",
        "mi_cifra": 250000,
        "su_cifra": 90000,
        "proyectos": 1,
        "proyecto": "PRY-101",
        "mis_req": ["REQ-001"],
        "sus_req": ["REQ-501"],
        "segmentos": 1,
        "senales": 3,
        "no_se_pisa_con": "PRD-NOMINA",
        # el control negativo del cruce: PRD-NOMINA contra los mismos publicados.
        # Lee uno y no dos: **un producto nunca se cruza consigo mismo**, y PRD-NOMINA
        # está publicado. Que la cuenta baje a uno es parte de lo que se verifica.
        "negativo": "PRD-NOMINA",
        "negativo_lee": 1,
    },
    "PRD-NOMINA": {
        "_porque": "control negativo · definición, entrevistas, métricas y tres "
                   "requerimientos, y ni un hallazgo",
        "requirements": 3,
        "by_state": {"aceptado": 2, "propuesto": 1},
        "decided": 2,
        "with_evidence": 2,
        "traced": 2,
        "with_evidence_pct": 100.0,
        "traced_pct": 100.0,
        "unknown": [],
        "por_senal": {},
        "signals": [],
    },
}


def main() -> None:
    for nombre, constructor in (("PRD-QR", qr), ("PRD-NOMINA", nomina)):
        producto, metricas, reqs = constructor()
        base = EXPECTED / "registros" / nombre
        json_a(base / "producto.json", producto)
        for clave, dato in metricas.items():
            json_a(base / "metrics" / f"{clave}.json", dato)
        for r in reqs:
            json_a(base / "requirements" / f"{r['id']}.json", r)
    fichas()
    PORTAFOLIO.volcar()   # el árbol de input/, con la estructura de referencia
    publicados()
    json_a(EXPECTED / "hallazgos.json", HALLAZGOS)

    docs = len(list(INPUT.rglob("*.md")))
    registros = len(list((EXPECTED / "registros").rglob("requirements/*.json")))
    print(f"material: {docs} documentos · {registros} registros de referencia · "
          f"{len(FICHAS)} fichas de proyecto · corte {HOY}")
    print("control negativo: PRD-NOMINA, y no produce ni un hallazgo")


if __name__ == "__main__":
    main()
