# -*- coding: utf-8 -*-
"""Genera el material sintético de prueba de criterio-project.

Nada aquí es real. Ningún documento de cliente, de empleador ni dato personal.
Todo se construyó desde cero, como exige CONTRIBUTING.md.

    python3 tests/criterio-project/generar.py

Este corpus mira **un proyecto desde adentro**, que es lo que Samuel ve. El de
`tests/criterio-portfolio/` mira cuarenta desde arriba, y no sirve para probar esto: un
barrido de portafolio no lee minutas semana a semana, y la función central de
Samuel vive exactamente ahí.

Produce:

    input/              la carpeta de un proyecto, con sus reuniones
    expected/fichas/    la extracción de referencia
    expected/hallazgos.json   las respuestas conocidas, escritas a mano

Fecha de referencia fija: 2026-11-20. Una prueba que use la fecha de hoy cambia de
respuesta cada semana.

Los hallazgos esperados **no se calculan aquí.** Se escriben a mano leyendo las
minutas, y el trabajo del código es derivarlos de la ficha. Si se derivaran con las
mismas fórmulas, la prueba no probaría nada.

## Qué se plantó, y qué prueba cada cosa

**PRY-101 · Pasarela de pagos QR** — el proyecto con vida de reunión. Ocho semanas
de comité, y dentro:

  · Un compromiso **reprogramado tres veces** por la misma persona sobre lo mismo.
    Es un bloqueo que nadie nombró, y es información distinta de tres vencidos.
  · Un compromiso **sin fecha** — «lo vemos la otra semana». No puede estar vencido,
    y por eso mismo desaparecía del informe.
  · Un compromiso **cumplido con evidencia**, para que no todo sea hallazgo.
  · Un compromiso **vencido y sin evidencia**.
  · Un **riesgo dicho al pasar** en la minuta del 16 de octubre que nunca entró al
    registro formal. La persona lo dijo; nadie lo escribió donde va.
  · El gerente declara **amarillo** — y aquí la declaración sí coincide con la
    evidencia, porque un agente que contradice siempre es tan inútil como uno que
    nunca contradice.

**PRY-102 · Portal de proveedores** — **control negativo.** Tiene reuniones, tiene
compromisos, y **no produce ni un hallazgo**: todo lo prometido se cumplió con
evidencia, nada venció, nada se reprogramó. Un agente que encuentra algo aquí está
roto.
"""
import json
import shutil
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
PORTAFOLIO = corpus.Portafolio(INPUT)


def escribir(ruta, texto):
    """Registra si es material de entrada; escribe de una si es una respuesta.

    Las fichas y los hallazgos de `expected/` son respuestas, no insumo: esos sí se
    escriben aquí mismo.
    """
    ruta = Path(ruta)
    try:
        relativa = ruta.relative_to(INPUT)
    except ValueError:
        return corpus.escribir_suelto(ruta, texto)
    return PORTAFOLIO.escribir(relativa, texto)


def campo(valor, fuente, fecha, estado="found"):
    return {"value": valor, "source": fuente, "source_date": fecha, "state": estado}


def vacio():
    return {"value": None, "source": None, "source_date": None, "state": "not_found"}


# ══════════════════════════════════════════════ PRY-101 · los documentos

P1 = "PRY-101-pasarela-qr"

escribir(INPUT / P1 / "00-gobierno/2026-08-03-acta-constitucion.md", """
# Acta de constitución · Pasarela de pagos QR

**Código:** PRY-101
**Área dueña:** Medios de Pago
**Patrocinador:** Marcela Ibáñez, VP de Medios de Pago
**Gerente de proyecto:** Daniel Ospina
**Comité:** Comité de Medios de Pago
**Producto:** Pagos QR
**Autoridad del gerente:** hasta 60.000.000 y ajustes de cronograma menores a 10 días.

## Objetivo del negocio

Habilitar el cobro por código QR interoperable en los comercios afiliados, con
liquidación el mismo día.

## Plan aprobado

Inicio 10 de agosto de 2026. Cierre 27 de febrero de 2027.

## Presupuesto aprobado

1.100.000.000 COP.

## Criterio de éxito

Cinco mil comercios transaccionando en los primeros noventa días posteriores a la
salida a producción.
""")

escribir(INPUT / P1 / "10-plan/2026-08-10-cronograma-v1.csv", """
hito,fecha,estado
Diseño de la experiencia de cobro,2026-09-18,cumplido
Certificación con el switch interoperable,2026-11-06,pendiente
Piloto con veinte comercios,2027-01-15,pendiente
Salida a producción,2027-02-27,pendiente
""")

escribir(INPUT / P1 / "30-reuniones/2026-09-25-comite-semanal.md", """
# Comité semanal · PRY-101 · 25 de septiembre de 2026

**Asisten:** Daniel Ospina (gerente), Marcela Ibáñez (patrocinadora), Rubén Ferreira
(arquitectura), Lorena Pineda (operaciones).

## Avance

El diseño de la experiencia de cobro quedó cerrado el 18 de septiembre. Se adjuntó
el documento aprobado al expediente.

## Acuerdos

- **Rubén** entrega el documento de integración con el switch interoperable **el 9 de
  octubre**.
- **Lorena** levanta el inventario de comercios del piloto **el 16 de octubre**.
""")

escribir(INPUT / P1 / "30-reuniones/2026-10-09-comite-semanal.md", """
# Comité semanal · PRY-101 · 9 de octubre de 2026

**Asisten:** Daniel Ospina, Rubén Ferreira, Lorena Pineda.

## Avance

Rubén presentó el documento de integración. Queda adjunto al expediente y se da por
recibido.

## Acuerdos

- **Rubén** entrega el plan de pruebas de certificación **el 23 de octubre**.
""")

escribir(INPUT / P1 / "20-seguimiento/2026-10-09-recibo-documento-integracion.md", """
# Recibo · Documento de integración con el switch

**Fecha:** 9 de octubre de 2026
**Entregado por:** Rubén Ferreira
**Recibido por:** Daniel Ospina

Se recibe el documento de integración con el switch interoperable, en la versión
presentada al comité de hoy. Se da por cumplido el compromiso del 25 de septiembre.
""")

escribir(INPUT / P1 / "30-reuniones/2026-10-16-comite-semanal.md", """
# Comité semanal · PRY-101 · 16 de octubre de 2026

**Asisten:** Daniel Ospina, Rubén Ferreira, Lorena Pineda.

## Avance

Lorena entregó el inventario de comercios del piloto. Sin observaciones.

## Discusión

Rubén comentó que el switch interoperable **va a cambiar su versión de certificación
en enero**, y que si el piloto se corre después de esa fecha habría que certificar
dos veces. Se acordó mirarlo más adelante. *(No quedó en el registro de riesgos.)*

## Acuerdos

- **Rubén** entrega el plan de pruebas de certificación **el 30 de octubre**. Se
  reprograma el compromiso del 9 de octubre.
- **Lorena** revisa con jurídico el contrato de afiliación de comercios. **Sin fecha:
  se define cuando jurídico confirme disponibilidad.**
""")

escribir(INPUT / P1 / "20-seguimiento/2026-10-16-recibo-inventario-comercios.md", """
# Recibo · Inventario de comercios del piloto

**Fecha:** 16 de octubre de 2026
**Entregado por:** Lorena Pineda
**Recibido por:** Daniel Ospina

Se recibe el inventario de comercios candidatos al piloto, con 24 comercios
identificados. Se da por cumplido el compromiso del 25 de septiembre.
""")

escribir(INPUT / P1 / "30-reuniones/2026-10-30-comite-semanal.md", """
# Comité semanal · PRY-101 · 30 de octubre de 2026

**Asisten:** Daniel Ospina, Rubén Ferreira.

## Avance

Sin novedades en la certificación. Rubén informa que el equipo de arquitectura está
atendiendo una incidencia de producción y no alcanzó a preparar el plan de pruebas.

## Acuerdos

- **Rubén** entrega el plan de pruebas de certificación **el 13 de noviembre**. Se
  reprograma por segunda vez.
""")

escribir(INPUT / P1 / "30-reuniones/2026-11-13-comite-semanal.md", """
# Comité semanal · PRY-101 · 13 de noviembre de 2026

**Asisten:** Daniel Ospina, Rubén Ferreira, Lorena Pineda.

## Avance

El hito de certificación con el switch, previsto para el 6 de noviembre, no se
alcanzó. No hay evidencia de certificación en el expediente.

## Acuerdos

- **Rubén** entrega el plan de pruebas de certificación **el 27 de noviembre**. Se
  reprograma por tercera vez.
""")

escribir(INPUT / P1 / "20-seguimiento/2026-11-13-informe-avance.md", """
# Informe de avance · PRY-101 · 13 de noviembre de 2026

**Estado declarado:** amarillo
**Avance:** 38%
**Corte:** 13 de noviembre de 2026

La certificación con el switch interoperable no se alcanzó en la fecha prevista y es
hoy el único frente crítico. El resto del plan avanza según lo acordado.
""")


# ══════════════════════════════════════════════ PRY-102 · control negativo

P2 = "PRY-102-portal-proveedores"

escribir(INPUT / P2 / "00-gobierno/2026-09-01-acta-constitucion.md", """
# Acta de constitución · Portal de proveedores

**Código:** PRY-102
**Área dueña:** Compras
**Patrocinador:** Andrés Villamil, Director de Compras
**Gerente de proyecto:** Paula Restrepo
**Comité:** Comité de Compras
**Producto:** Portal de proveedores
**Autoridad del gerente:** hasta 40.000.000 y ajustes de cronograma menores a 10 días.

## Objetivo del negocio

Que los proveedores radiquen facturas y consulten el estado de pago sin llamar al
área de cuentas por pagar.

## Plan aprobado

Inicio 8 de septiembre de 2026. Cierre 30 de abril de 2027.

## Presupuesto aprobado

480.000.000 COP.

## Criterio de éxito

El 80% de las facturas radicadas por el portal en los primeros seis meses.
""")

escribir(INPUT / P2 / "10-plan/2026-09-08-cronograma-v1.csv", """
hito,fecha,estado
Levantamiento de requisitos,2026-10-30,cumplido
Prototipo validado con proveedores,2026-12-18,pendiente
Salida a producción,2027-04-30,pendiente
""")

escribir(INPUT / P2 / "30-reuniones/2026-10-23-comite-semanal.md", """
# Comité semanal · PRY-102 · 23 de octubre de 2026

**Asisten:** Paula Restrepo (gerente), Andrés Villamil (patrocinador), Iván Mora
(desarrollo).

## Avance

El levantamiento de requisitos está en su etapa final.

## Acuerdos

- **Iván** entrega el documento de requisitos consolidado **el 30 de octubre**.
""")

escribir(INPUT / P2 / "20-seguimiento/2026-10-30-recibo-requisitos.md", """
# Recibo · Documento de requisitos consolidado

**Fecha:** 30 de octubre de 2026
**Entregado por:** Iván Mora
**Recibido por:** Paula Restrepo

Se recibe el documento de requisitos consolidado, con la firma de las cuatro áreas
usuarias. Se da por cumplido el compromiso del 23 de octubre y por alcanzado el hito
de levantamiento de requisitos.
""")

escribir(INPUT / P2 / "30-reuniones/2026-11-13-comite-semanal.md", """
# Comité semanal · PRY-102 · 13 de noviembre de 2026

**Asisten:** Paula Restrepo, Andrés Villamil, Iván Mora.

## Avance

El prototipo avanza según el cronograma. No hay frentes en riesgo.

## Acuerdos

- **Iván** presenta el prototipo navegable **el 18 de diciembre**, según el
  cronograma vigente.
""")

escribir(INPUT / P2 / "20-seguimiento/2026-11-18-informe-avance.md", """
# Informe de avance · PRY-102 · 18 de noviembre de 2026

**Estado declarado:** verde
**Avance:** 31%
**Corte:** 18 de noviembre de 2026

El proyecto avanza según el plan aprobado. Sin desviaciones ni frentes críticos.
""")


# ══════════════════════════════════════════════ las fichas de referencia

def ficha_101():
    g = f"{P1}/00-gobierno/2026-08-03-acta-constitucion.md"
    cr = f"{P1}/10-plan/2026-08-10-cronograma-v1.csv"
    r0925 = f"{P1}/30-reuniones/2026-09-25-comite-semanal.md"
    r1009 = f"{P1}/30-reuniones/2026-10-09-comite-semanal.md"
    r1016 = f"{P1}/30-reuniones/2026-10-16-comite-semanal.md"
    r1030 = f"{P1}/30-reuniones/2026-10-30-comite-semanal.md"
    r1113 = f"{P1}/30-reuniones/2026-11-13-comite-semanal.md"
    ev1009 = f"{P1}/20-seguimiento/2026-10-09-recibo-documento-integracion.md"
    ev1016 = f"{P1}/20-seguimiento/2026-10-16-recibo-inventario-comercios.md"
    inf = f"{P1}/20-seguimiento/2026-11-13-informe-avance.md"
    return {
        "identity": {
            "code": campo("PRY-101", g, "2026-08-03"),
            "name": campo("Pasarela de pagos QR", g, "2026-08-03"),
            "business_area": campo("Medios de Pago", g, "2026-08-03"),
            "sponsor": campo("Marcela Ibáñez, VP de Medios de Pago", g, "2026-08-03"),
            "manager": campo("Daniel Ospina", g, "2026-08-03"),
            "committee": campo("Comité de Medios de Pago", g, "2026-08-03"),
            "product": campo("Pagos QR", g, "2026-08-03"),
            "authority": campo("hasta 60.000.000 y ajustes de cronograma menores a 10 días",
                               g, "2026-08-03"),
        },
        "declared": {
            "status": campo("amarillo", inf, "2026-11-13"),
            "progress_pct": campo(38, inf, "2026-11-13"),
            "as_of": campo("2026-11-13", inf, "2026-11-13"),
        },
        "plan": {
            "start_date": campo("2026-08-10", g, "2026-08-03"),
            "end_date": campo("2027-02-27", g, "2026-08-03"),
            "milestones": [
                {"name": campo("Diseño de la experiencia de cobro", cr, "2026-08-10"),
                 "baseline_date": campo("2026-09-18", cr, "2026-08-10"),
                 "current_date": campo("2026-09-18", cr, "2026-08-10"),
                 "state": campo("met", cr, "2026-08-10"),
                 "evidence": campo("Cerrado el 18 de septiembre", r0925, "2026-09-25")},
                {"name": campo("Certificación con el switch interoperable", cr, "2026-08-10"),
                 "baseline_date": campo("2026-11-06", cr, "2026-08-10"),
                 "current_date": campo("2026-11-06", cr, "2026-08-10"),
                 "state": campo("pending", cr, "2026-08-10"),
                 "evidence": vacio()},
                {"name": campo("Piloto con veinte comercios", cr, "2026-08-10"),
                 "baseline_date": campo("2027-01-15", cr, "2026-08-10"),
                 "current_date": campo("2027-01-15", cr, "2026-08-10"),
                 "state": campo("pending", cr, "2026-08-10"),
                 "evidence": vacio()},
                {"name": campo("Salida a producción", cr, "2026-08-10"),
                 "baseline_date": campo("2027-02-27", cr, "2026-08-10"),
                 "current_date": campo("2027-02-27", cr, "2026-08-10"),
                 "state": campo("pending", cr, "2026-08-10"),
                 "evidence": vacio()},
            ],
            "baselines": [{"version": campo("v1", cr, "2026-08-10"),
                           "end_date": campo("2027-02-27", cr, "2026-08-10"),
                           "approved_on": campo("2026-08-10", cr, "2026-08-10")}],
        },
        "money": {
            "currency": campo("COP", g, "2026-08-03"),
            "approved": campo(1100000000, g, "2026-08-03"),
            "committed": vacio(), "executed": vacio(), "projection": vacio(),
        },
        "commitments": [
            # cumplido con evidencia · que no todo sea hallazgo
            {"who": campo("Rubén Ferreira", r0925, "2026-09-25"),
             "what": campo("Entregar el documento de integración con el switch interoperable",
                           r0925, "2026-09-25"),
             "due_date": campo("2026-10-09", r0925, "2026-09-25"),
             "stated_on": campo("2026-09-25", r0925, "2026-09-25"),
             "state": campo("met", ev1009, "2026-10-09"),
             "evidence": campo("Recibo del 9 de octubre", ev1009, "2026-10-09")},
            # cumplido con evidencia
            {"who": campo("Lorena Pineda", r0925, "2026-09-25"),
             "what": campo("Levantar el inventario de comercios del piloto", r0925, "2026-09-25"),
             "due_date": campo("2026-10-16", r0925, "2026-09-25"),
             "stated_on": campo("2026-09-25", r0925, "2026-09-25"),
             "state": campo("met", ev1016, "2026-10-16"),
             "evidence": campo("Recibo del 16 de octubre", ev1016, "2026-10-16")},
            # reprogramado tres veces · el bloqueo que nadie nombró
            {"who": campo("Rubén Ferreira", r1113, "2026-11-13"),
             "what": campo("Entregar el plan de pruebas de certificación", r1009, "2026-10-09"),
             "due_date": campo("2026-11-27", r1113, "2026-11-13"),
             "stated_on": campo("2026-11-13", r1113, "2026-11-13"),
             "state": campo("open", r1113, "2026-11-13"),
             "evidence": vacio(),
             "reschedules": [
                 {"due_date": campo("2026-10-23", r1009, "2026-10-09"),
                  "stated_on": campo("2026-10-09", r1009, "2026-10-09")},
                 {"due_date": campo("2026-10-30", r1016, "2026-10-16"),
                  "stated_on": campo("2026-10-16", r1016, "2026-10-16")},
                 {"due_date": campo("2026-11-13", r1030, "2026-10-30"),
                  "stated_on": campo("2026-10-30", r1030, "2026-10-30")},
             ]},
            # sin fecha · no puede estar vencido, y por eso desaparecía
            {"who": campo("Lorena Pineda", r1016, "2026-10-16"),
             "what": campo("Revisar con jurídico el contrato de afiliación de comercios",
                           r1016, "2026-10-16"),
             "due_date": campo("no_declarada", r1016, "2026-10-16"),
             "stated_on": campo("2026-10-16", r1016, "2026-10-16"),
             "state": campo("open", r1016, "2026-10-16"),
             "evidence": vacio()},
        ],
        "raid": {
            "risks": [
                # dicho al pasar y nunca registrado
                {"what": campo("El switch interoperable cambia su versión de certificación "
                               "en enero; si el piloto corre después habría que certificar "
                               "dos veces", r1016, "2026-10-16"),
                 "owner": vacio(),
                 "formally_registered": campo(False, r1016, "2026-10-16")},
            ],
            "issues": [], "dependencies": [],
        },
        "vendors": [],
        "changes": [],
        "activity": {"last_document_date": campo("2026-11-13", inf, "2026-11-13")},
    }


def ficha_102():
    g = f"{P2}/00-gobierno/2026-09-01-acta-constitucion.md"
    cr = f"{P2}/10-plan/2026-09-08-cronograma-v1.csv"
    r1023 = f"{P2}/30-reuniones/2026-10-23-comite-semanal.md"
    r1113 = f"{P2}/30-reuniones/2026-11-13-comite-semanal.md"
    ev = f"{P2}/20-seguimiento/2026-10-30-recibo-requisitos.md"
    inf = f"{P2}/20-seguimiento/2026-11-18-informe-avance.md"
    return {
        "identity": {
            "code": campo("PRY-102", g, "2026-09-01"),
            "name": campo("Portal de proveedores", g, "2026-09-01"),
            "business_area": campo("Compras", g, "2026-09-01"),
            "sponsor": campo("Andrés Villamil, Director de Compras", g, "2026-09-01"),
            "manager": campo("Paula Restrepo", g, "2026-09-01"),
            "committee": campo("Comité de Compras", g, "2026-09-01"),
            "product": campo("Portal de proveedores", g, "2026-09-01"),
            "authority": campo("hasta 40.000.000 y ajustes de cronograma menores a 10 días",
                               g, "2026-09-01"),
        },
        "declared": {
            "status": campo("verde", inf, "2026-11-18"),
            "progress_pct": campo(31, inf, "2026-11-18"),
            "as_of": campo("2026-11-18", inf, "2026-11-18"),
        },
        "plan": {
            "start_date": campo("2026-09-08", g, "2026-09-01"),
            "end_date": campo("2027-04-30", g, "2026-09-01"),
            "milestones": [
                {"name": campo("Levantamiento de requisitos", cr, "2026-09-08"),
                 "baseline_date": campo("2026-10-30", cr, "2026-09-08"),
                 "current_date": campo("2026-10-30", cr, "2026-09-08"),
                 "state": campo("met", ev, "2026-10-30"),
                 "evidence": campo("Recibo del 30 de octubre", ev, "2026-10-30")},
                {"name": campo("Prototipo validado con proveedores", cr, "2026-09-08"),
                 "baseline_date": campo("2026-12-18", cr, "2026-09-08"),
                 "current_date": campo("2026-12-18", cr, "2026-09-08"),
                 "state": campo("pending", cr, "2026-09-08"),
                 "evidence": vacio()},
                {"name": campo("Salida a producción", cr, "2026-09-08"),
                 "baseline_date": campo("2027-04-30", cr, "2026-09-08"),
                 "current_date": campo("2027-04-30", cr, "2026-09-08"),
                 "state": campo("pending", cr, "2026-09-08"),
                 "evidence": vacio()},
            ],
            "baselines": [{"version": campo("v1", cr, "2026-09-08"),
                           "end_date": campo("2027-04-30", cr, "2026-09-08"),
                           "approved_on": campo("2026-09-08", cr, "2026-09-08")}],
        },
        "money": {
            "currency": campo("COP", g, "2026-09-01"),
            "approved": campo(480000000, g, "2026-09-01"),
            "committed": vacio(), "executed": vacio(), "projection": vacio(),
        },
        "commitments": [
            {"who": campo("Iván Mora", r1023, "2026-10-23"),
             "what": campo("Entregar el documento de requisitos consolidado", r1023, "2026-10-23"),
             "due_date": campo("2026-10-30", r1023, "2026-10-23"),
             "stated_on": campo("2026-10-23", r1023, "2026-10-23"),
             "state": campo("met", ev, "2026-10-30"),
             "evidence": campo("Recibo del 30 de octubre", ev, "2026-10-30")},
            {"who": campo("Iván Mora", r1113, "2026-11-13"),
             "what": campo("Presentar el prototipo navegable", r1113, "2026-11-13"),
             "due_date": campo("2026-12-18", r1113, "2026-11-13"),
             "stated_on": campo("2026-11-13", r1113, "2026-11-13"),
             "state": campo("open", r1113, "2026-11-13"),
             "evidence": vacio()},
        ],
        "raid": {"risks": [], "issues": [], "dependencies": []},
        "vendors": [],
        "changes": [],
        "activity": {"last_document_date": campo("2026-11-18", inf, "2026-11-18")},
    }


# ══════════════════════════════════════════════ los hallazgos, escritos a mano

HALLAZGOS = {
    "_nota": ("Escritos leyendo las minutas, no calculados. Si salieran de las mismas "
              "fórmulas que el código, esta prueba no probaría nada."),
    "as_of": HOY,
    "PRY-101": {
        "_porque": "El proyecto con vida de reunión.",
        "commitments_overdue": 0,
        "_overdue_porque": ("Ninguno. El reprogramado vence el 27 de noviembre, que es "
                            "después del 20. Que esté reprogramado tres veces es otra cosa, "
                            "y es la que importa."),
        "commitments_undated": 1,
        "commitments_rescheduled": 1,
        "reschedule_times": 3,
        "milestones_overdue": 1,
        "_hito_porque": ("La certificación con el switch, del 6 de noviembre, sin evidencia "
                         "en el expediente. La minuta del 13 lo dice con todas las letras."),
        "days_silent": 7,
        "_silencio_porque": "El último documento es el informe del 13 de noviembre.",
        "declared": "amarillo",
        "declared_vs_evidence": False,
        "_declaracion_porque": ("El gerente declara amarillo y la evidencia lo sostiene. Un "
                                "agente que contradice siempre es tan inútil como uno que "
                                "nunca contradice."),
        "risks_not_registered": 1,
        "signals": ["commitment_rescheduled", "commitment_undated", "milestone_overdue"],
    },
    "PRY-102": {
        "_porque": "Control negativo. Tiene reuniones y compromisos, y no produce nada.",
        "commitments_overdue": 0,
        "commitments_undated": 0,
        "commitments_rescheduled": 0,
        "milestones_overdue": 0,
        "days_silent": 2,
        "declared": "verde",
        "declared_vs_evidence": False,
        "risks_not_registered": 0,
        "signals": [],
    },
}


# ══════════════════════════════════════════════ escribir

def prefijar(nodo, carpeta):
    """Las citas de la ficha son relativas a la raíz de documentación, no a la
    carpeta del proyecto. Se comprueba aquí para no depender de que quien escribió
    la ficha se acordara."""
    if isinstance(nodo, dict):
        if "source" in nodo and isinstance(nodo.get("source"), str):
            assert nodo["source"].startswith(carpeta), \
                f"cita sin prefijar: {nodo['source']}"
        for v in nodo.values():
            prefijar(v, carpeta)
    elif isinstance(nodo, list):
        for v in nodo:
            prefijar(v, carpeta)


def documentos_leidos(ficha, carpeta):
    """El registro de lo leído, con los dos hashes, a partir de las citas de la
    ficha. Sin esto el silencio no se puede calcular: no hay contra qué contar."""
    import importlib.util
    ruta = RAIZ.parent.parent / "plugins" / "criterio-project" / "scripts" / "portafolio.py"
    spec = importlib.util.spec_from_file_location("pmo_pm", ruta)
    portafolio = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(portafolio)

    citas = set()

    def recoger(nodo):
        if isinstance(nodo, dict):
            v = nodo.get("source")
            if isinstance(v, str) and v.startswith(carpeta):
                citas.add(v)
            for x in nodo.values():
                recoger(x)
        elif isinstance(nodo, list):
            for x in nodo:
                recoger(x)

    recoger(ficha)
    salida = []
    for cita in sorted(citas):
        archivo = INPUT / cita
        if not archivo.exists():
            continue
        salida.append({"path": cita,
                       "hash": portafolio.hash_bytes(archivo),
                       "text_hash": portafolio.hash_texto(archivo),
                       "date": archivo.name[:10] if archivo.name[:4].isdigit() else None})
    return salida


def main():
    PORTAFOLIO.volcar()   # el árbol de input/, con la estructura de referencia
    for d in (EXPECTED / "fichas",):
        if d.exists():
            shutil.rmtree(d)
    (EXPECTED / "fichas").mkdir(parents=True, exist_ok=True)

    for codigo, carpeta, ficha in (("PRY-101", P1, ficha_101()),
                                   ("PRY-102", P2, ficha_102())):
        prefijar(ficha, carpeta)
        ficha["meta"] = {"documents_seen": documentos_leidos(ficha, carpeta)}
        (EXPECTED / "fichas" / f"{codigo}.json").write_text(
            json.dumps(ficha, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    (EXPECTED / "hallazgos.json").write_text(
        json.dumps(HALLAZGOS, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    docs = sorted(p for p in INPUT.rglob("*") if p.is_file())
    reuniones = [p for p in docs if "30-reuniones" in p.parts]
    print(f"input/     {len(docs)} documentos en 2 proyectos, {len(reuniones)} minutas")
    print(f"expected/  2 fichas de referencia y las respuestas conocidas")
    print(f"corrida:   --today {HOY}")


if __name__ == "__main__":
    main()
