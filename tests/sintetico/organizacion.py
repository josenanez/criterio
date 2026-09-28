# -*- coding: utf-8 -*-
"""Genera una organización sintética completa, para probar los agentes a mano.

    python3 tests/sintetico/organizacion.py <carpeta destino>

No es material de prueba del repositorio: es un banco ficticio sobre el que se puede
correr la familia entera como si fuera una PMO de verdad, sin apuntar los agentes a la
documentación de nadie. Diez proyectos y ocho productos, con la estructura de referencia
de `corpus.py`.

Cada caso trae algo plantado a propósito, y **dos son controles negativos** —un proyecto
y un producto que están al día y no deben producir ni un hallazgo. Un agente que
encuentra algo ahí es un generador de ruido.

Las fechas se calculan **relativas al día de la corrida**, no fijas, porque el punto es
que las señales de silencio, de declaración vieja y de supuesto sin verificar se disparen
cuando alguien corra esto mañana o en tres meses.

Nada aquí es real. Banco Aurora no existe, y ningún nombre, cifra ni documento viene de
una organización o persona real.
"""
import datetime as dt
import json
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import corpus  # noqa: E402

HOY = dt.date.today()


def d(dias_atras: int) -> str:
    """Una fecha, en días hacia atrás desde hoy."""
    return (HOY - dt.timedelta(days=dias_atras)).isoformat()


def f(dias_adelante: int) -> str:
    return (HOY + dt.timedelta(days=dias_adelante)).isoformat()


def plata(n: int) -> str:
    return f"{n:,}".replace(",", ".")


# ── lo que cada caso debe producir, en nombres de señal ──────────────────
# La clave de respuestas en prosa es para una persona. Esta es para el calificador:
# sin ella, medir aciertos y falsos positivos exige leer markdown, y una prueba que
# necesita que alguien lea no corre todos los días.
#
# Se declara a mano, como todo lo esperado en este repositorio. Si se derivara del
# mismo cálculo que se quiere medir, la prueba no probaría nada.
ESPERADO = {
    "PRY-101": ["milestone_overdue", "milestone_met_without_evidence",
                "commitment_undated", "commitment_rescheduled", "declared_vs_evidence"],
    "PRY-102": ["variance_time", "milestone_met_without_evidence",
                "milestone_met_without_evidence", "commitment_overdue",
                "rebaseline_unauthorized"],
    "PRY-103": ["milestone_overdue", "vendor_deliverable_late",
                "vendor_accepted_without_evidence", "vendor_invoiced_over_accepted"],
    "PRY-104": ["silent", "declared_vs_evidence", "declaration_stale"],
    "PRY-105": [],                       # control negativo
    "PRY-106": ["milestone_met_without_evidence", "budget_committed",
                "vendor_deliverable_late", "vendor_invoiced_without_delivery"],
    "PRY-107": ["pm_vs_pmo", "pm_vs_pmo"],
    "PRY-108": [],
    "PRY-109": ["variance_cost", "change_without_baseline"],
    "PRY-110": [],
    "PRD-QR": ["requirement_undecided", "assumption_unverified", "assumption_unverified",
               "claim_vs_metric"],
    "PRD-NOMINA": [],                    # control negativo
    "PRD-HIPO": ["requirement_without_owner", "requirement_without_acceptance",
                 "assumption_unverified"],
    "PRD-PYME": ["requirement_undecided", "requirement_undecided",
                 "assumption_unverified"],
    "PRD-COBROS": ["trace_not_confirmed", "trace_not_confirmed", "assumption_unverified"],
    "PRD-SEGUROS": ["evidence_stale", "evidence_stale", "requirement_untraced",
                    "requirement_undecided", "assumption_unverified"],
    "PRD-REMESAS": ["requirement_untraced", "requirement_untraced",
                    "requirement_untraced"],
    "PRD-TARJETA": ["requirement_untraced", "requirement_untraced",
                    "requirement_accepted_without_evidence",
                    "assumption_unverified", "assumption_unverified"],
}

# Los dos que no deben producir nada. Se nombran aparte porque su fallo es de otra
# clase: un control negativo que encuentra algo no es una señal que falta, es ruido.
CONTROLES = ("PRY-105", "PRD-NOMINA")


# ══════════════════════════════════════════════════════════════════════════
# Plantillas de documento. Una por clase, parametrizada.
# ══════════════════════════════════════════════════════════════════════════

def acta(p) -> str:
    return f"""
# Acta de constitución · {p['nombre']}

**Código:** {p['codigo']}
**Área dueña:** {p['area']}
**Patrocinador:** {p['patrocinador']}
**Gerente de proyecto:** {p['gerente']}
**Comité:** {p['comite']}
**Producto asociado:** {p.get('producto', 'No aplica')}
**Fecha de aprobación:** {p['aprobacion']}

## Objetivo del negocio

{p['objetivo']}

## Alcance

{chr(10).join('- ' + x for x in p['alcance'])}

## Fuera de alcance

{chr(10).join('- ' + x for x in p['fuera'])}

## Presupuesto aprobado

**{plata(p['presupuesto'])} COP**, aprobado por {p['comite']} el {p['aprobacion']}.

## Fechas comprometidas

| | Fecha |
|---|---|
| Inicio | {p['inicio']} |
| Cierre | {p['cierre']} |

## Criterio de éxito

{p['exito']}

## Dependencias declaradas

{chr(10).join('- ' + x for x in p.get('dependencias', ['Ninguna declarada'])) }
"""


def cronograma(p, version: int, hitos) -> str:
    filas = "\n".join(f"{h[0]},{h[1]},{h[2]},{h[3]}" for h in hitos)
    return f"""
hito,fecha_linea_base,fecha_vigente,estado
{filas}
"""


def informe(p, estado: str, fecha: str, avance: int, notas) -> str:
    return f"""
# Informe de avance · {p['nombre']}

**Código:** {p['codigo']}
**Fecha de corte:** {fecha}
**Gerente:** {p['gerente']}

## Estado declarado

**{estado}**

Avance reportado: **{avance}%**

## Lo que pasó en el periodo

{chr(10).join('- ' + x for x in notas)}

## Presupuesto

| | COP |
|---|---|
| Aprobado | {plata(p['presupuesto'])} |
| Comprometido | {plata(p['comprometido'])} |
| Ejecutado | {plata(p['ejecutado'])} |
| Proyección al cierre | {plata(p['proyeccion'])} |

## Riesgos abiertos

{chr(10).join('- ' + x for x in p.get('riesgos', ['Sin riesgos nuevos en el periodo']))}
"""


def minuta(p, fecha: str, asistentes, temas, compromisos) -> str:
    filas = "\n".join(
        f"| {c['quien']} | {c['que']} | {c['para']} |" for c in compromisos)
    return f"""
# {p['comite']} · {p['nombre']}

**Fecha:** {fecha}
**Asistentes:** {', '.join(asistentes)}

## Temas tratados

{chr(10).join(f'{i + 1}. {t}' for i, t in enumerate(temas))}

## Compromisos

| Responsable | Compromiso | Para |
|---|---|---|
{filas}
"""


def recibo(p, fecha: str, entregable: str, quien: str, nota: str) -> str:
    return f"""
# Acta de recibo · {entregable}

**Proyecto:** {p['codigo']} · {p['nombre']}
**Fecha de recibo:** {fecha}
**Recibido por:** {quien}

Se recibe a satisfacción el entregable **{entregable}**.

{nota}
"""


def cambio(p, fecha: str, numero: str, que: str, dias: int, costo: int,
           autorizado: str) -> str:
    return f"""
# Solicitud de cambio {numero}

**Proyecto:** {p['codigo']} · {p['nombre']}
**Fecha:** {fecha}
**Solicitante:** {p['gerente']}

## Qué cambia

{que}

## Impacto

| | |
|---|---|
| Tiempo | {dias:+d} días sobre la línea base vigente |
| Costo | {plata(costo)} COP adicionales |

## Autorización

{autorizado}
"""


def ficha_publicada(p, fecha: str, campos: dict) -> str:
    """La ficha que el gerente publica con /pm-publish, como un documento más.

    Va en JSON a propósito: es un contrato de datos, no una narración. Vera la lee sin
    fusionarla con la suya — la séptima invariante— y la diferencia entre las dos es el
    hallazgo.
    """
    def c(v, fuente):
        return {"value": v, "source": fuente, "source_date": fecha, "state": "found"}
    doc = {"schema_version": "0.1", "written_by": "criterio-project",
           "published_on": fecha,
           "identity": {k: c(v, campos["_fuente"]) for k, v in campos.items()
                        if not k.startswith("_")}}
    return json.dumps(doc, ensure_ascii=False, indent=2)


def contrato(p, fecha: str, numero: str, proveedor: str, entregables) -> str:
    filas = "\n".join(f"| {e[0]} | {e[1]} | {plata(e[2])} | {e[3]} |"
                      for e in entregables)
    return f"""
# Contrato {numero} · {proveedor}

**Proyecto:** {p['codigo']} · {p['nombre']}
**Fecha de firma:** {fecha}
**Proveedor:** {proveedor}

## Entregables contractuales

| Entregable | Fecha comprometida | Monto COP | Estado |
|---|---|---|---|
{filas}

## Condición de pago

Cada entregable se factura contra acta de recibo firmada por el gerente del proyecto.
"""


def factura(p, fecha: str, numero: str, proveedor: str, concepto: str,
            monto: int) -> str:
    return f"""
# Factura {numero} · {proveedor}

**Proyecto:** {p['codigo']} · {p['nombre']}
**Fecha:** {fecha}
**Concepto:** {concepto}
**Valor:** {plata(monto)} COP

Radicada en cuentas por pagar.
"""


# ══════════════════════════════════════════════════════════════════════════
# Los diez proyectos
# ══════════════════════════════════════════════════════════════════════════

def proyectos(port: corpus.Portafolio) -> list:
    """Cada uno con lo que planta, declarado en el comentario de arriba."""
    plantado = []

    # ── PRY-101 · verde contradicho, hito vencido sin evidencia,
    #              compromiso reprogramado tres veces
    p = dict(codigo="PRY-101", nombre="Originación digital hipotecaria",
             carpeta="PRY-101-originacion-hipotecaria",
             area="Banca Hipotecaria", patrocinador="María Restrepo, VP de Operaciones",
             gerente="Andrés Lozano", comite="Comité de Transformación Digital",
             producto="PRD-HIPO · Crédito hipotecario digital", aprobacion=d(250),
             objetivo="Reducir el tiempo de originación hipotecaria de quince días "
                      "hábiles a cuatro, para solicitudes de vivienda no VIS.",
             alcance=["Formulario digital con validación de ingresos",
                      "Integración con centrales de riesgo",
                      "Firma electrónica de la promesa de compraventa"],
             fuera=["Avalúo, que sigue siendo presencial",
                    "Desembolso, que lo opera Tesorería"],
             inicio=d(240), cierre=f(120),
             presupuesto=4_200_000_000, comprometido=2_800_000_000,
             ejecutado=2_100_000_000, proyeccion=4_600_000_000,
             exito="80% de las solicitudes no VIS originadas por el canal digital "
                   "en los tres meses siguientes al cierre.",
             dependencias=["PRY-109 · Motor de decisión de crédito, para el scoring"],
             riesgos=["La integración con la central de riesgo depende de un contrato "
                      "que Jurídica no ha devuelto"])
    c = port.caso(p["codigo"], "proyecto", p["carpeta"])
    c.gobierno(p["aprobacion"], "acta-constitucion.md", acta(p))
    c.plan(d(235), "cronograma-v1.csv", cronograma(p, 1, [
        ("Formulario digital", d(120), d(120), "cerrado"),
        ("Integración centrales de riesgo", d(40), d(40), "en curso"),
        ("Firma electrónica", f(30), f(30), "no iniciado"),
        ("Salida a producción", f(120), f(120), "no iniciado")]))
    # el hito de hace 40 días está vencido y no hay acta de recibo que lo sustente
    c.seguimiento(d(18), "informe-avance.md", informe(
        p, "Verde", d(18), 72,
        ["Se cerró el formulario digital y pasó pruebas de usuario",
         "La integración con centrales de riesgo sigue pendiente del contrato",
         "Se inició el diseño de la firma electrónica"]))
    # Cada comité vuelve a prometer lo mismo con fecha NUEVA y más adelante, que es
    # como se reprograma de verdad: la de hace 60 días ya venció sin evidencia, la de
    # hace 35 también, y la última todavía no. Tres promesas, dos incumplidas.
    for fecha, promete in ((d(60), d(30)), (d(35), d(10)), (d(12), f(5))):
        c.reunion(fecha, "comite-transformacion.md", minuta(
            p, fecha,
            ["María Restrepo", "Andrés Lozano", "Rubén Cárdenas", "Sandra Gil"],
            ["Avance de la integración con centrales de riesgo",
             "Estado del contrato con la central",
             "Preparación de la firma electrónica"],
            [{"quien": "Rubén Cárdenas",
              "que": "Entregar el contrato firmado con la central de riesgo",
              "para": promete},
             {"quien": "Sandra Gil",
              "que": "Confirmar el alcance de la firma electrónica con Jurídica",
              "para": "por definir"}]))
    plantado.append((p["codigo"], p["nombre"], [
        "**Verde contradicho**: declara Verde y la integración de centrales, que es "
        "ruta crítica, lleva 40 días vencida",
        "**Hito vencido sin evidencia**: «Integración centrales de riesgo» venció hace "
        "40 días y no hay acta de recibo que lo cierre",
        "**Compromiso reprogramado tres veces**: Rubén Cárdenas y el contrato con la "
        "central, con fecha nueva en cada comité",
        "**Compromiso sin fecha**: Sandra Gil, «por definir» — no puede estar vencido, "
        "y por eso desaparece de todos los informes",
        "**Dependencia declarada y no confirmada**: PRY-109 no la menciona",
        "**Y una que NO debe reportarse**: la proyección está 9,5% por encima del "
        "aprobado (4.600 contra 4.200 millones), justo **bajo** el umbral de 10%. "
        "Sirve para ver si el agente respeta el umbral en vez de reportar toda "
        "diferencia. La desviación de costo que sí debe salir está en PRY-109"]))

    # ── PRY-102 · replanificación sin autorizar, desviación de tiempo
    p = dict(codigo="PRY-102", nombre="Core de depósitos",
             carpeta="PRY-102-core-depositos",
             area="Tecnología", patrocinador="Carlos Peña, CIO",
             gerente="Diana Molina", comite="Comité de Arquitectura",
             producto="Cuenta de ahorros", aprobacion=d(400),
             objetivo="Reemplazar el core de depósitos por una plataforma que permita "
                      "cerrar el día en menos de dos horas.",
             alcance=["Migración de cuentas de ahorro y corriente",
                      "Nuevo motor de intereses", "Cierre diario paralelo"],
             fuera=["Cartera, que va en una segunda fase"],
             inicio=d(390), cierre=f(300),
             presupuesto=18_000_000_000, comprometido=11_500_000_000,
             ejecutado=9_800_000_000, proyeccion=19_200_000_000,
             exito="Cierre diario en menos de dos horas durante treinta días seguidos.",
             riesgos=["La ventana de migración depende del calendario regulatorio"])
    c = port.caso(p["codigo"], "proyecto", p["carpeta"])
    c.gobierno(p["aprobacion"], "acta-constitucion.md", acta(p))
    c.plan(d(385), "cronograma-v1.csv", cronograma(p, 1, [
        ("Diseño de la migración", d(300), d(300), "cerrado"),
        ("Motor de intereses", d(120), d(120), "cerrado"),
        ("Migración de ahorros", d(30), f(90), "en curso"),
        ("Cierre paralelo", f(60), f(180), "no iniciado"),
        ("Salida a producción", f(300), f(300), "no iniciado")]))
    c.plan(d(25), "cronograma-v2.csv", cronograma(p, 2, [
        ("Diseño de la migración", d(300), d(300), "cerrado"),
        ("Motor de intereses", d(120), d(120), "cerrado"),
        ("Migración de ahorros", d(30), f(90), "en curso"),
        ("Cierre paralelo", f(60), f(180), "no iniciado"),
        ("Salida a producción", f(300), f(420), "no iniciado")]))
    c.seguimiento(d(10), "informe-avance.md", informe(
        p, "Amarillo", d(10), 54,
        ["La migración de ahorros se movió noventa días por la ventana regulatoria",
         "Se replanificó el cronograma y se publicó la versión 2",
         "El motor de intereses pasó pruebas de paralelo"]))
    c.reunion(d(22), "comite-arquitectura.md", minuta(
        p, d(22), ["Carlos Peña", "Diana Molina", "Javier Hoyos"],
        ["Ventana de migración y su impacto en el cronograma",
         "Resultado del paralelo del motor de intereses"],
        [{"quien": "Javier Hoyos", "que": "Publicar el cronograma replanificado",
          "para": d(20)}]))
    plantado.append((p["codigo"], p["nombre"], [
        "**Dos hitos declarados cerrados sin acta de recibo**: «Diseño de la "
        "migración» y «Motor de intereses». Este proyecto no produce actas de recibo, "
        "que es una forma común de cerrar un hito: marcarlo cerrado en el cronograma",
        "**Replanificación sin autorizar**: el cronograma v2 mueve la salida a "
        "producción 60 días y no hay solicitud de cambio ni acta del comité que lo "
        "autorice",
        "**Desviación de tiempo** contra la línea base original en dos hitos",
        "**Proyección 6,7% por encima del aprobado** (19.200 contra 18.000 millones): "
        "bajo el umbral de 10%, no debe salir como desviación de costo",
        "La dependencia que PRY-101 declara sobre este proyecto **no aparece aquí**"]))

    # ── PRY-103 · proveedor: entregable tardío y facturado sin entrega
    p = dict(codigo="PRY-103", nombre="Migración a la nube",
             carpeta="PRY-103-migracion-nube",
             area="Infraestructura", patrocinador="Carlos Peña, CIO",
             gerente="Felipe Arango", comite="Comité de Arquitectura",
             producto="No aplica", aprobacion=d(320),
             objetivo="Mover las cargas no core a nube pública y cerrar un centro de "
                      "datos propio.",
             alcance=["Landing zone", "Migración de 40 aplicaciones no core",
                      "Cierre del centro de datos de la 26"],
             fuera=["El core, que se queda en sitio"],
             inicio=d(310), cierre=f(200),
             presupuesto=9_500_000_000, comprometido=6_200_000_000,
             ejecutado=5_400_000_000, proyeccion=9_300_000_000,
             exito="40 aplicaciones operando en nube y el centro de datos cerrado.",
             riesgos=["El proveedor concentra el conocimiento de la landing zone"])
    c = port.caso(p["codigo"], "proyecto", p["carpeta"])
    c.gobierno(p["aprobacion"], "acta-constitucion.md", acta(p))
    c.gobierno(d(300), "contrato-oc-4471.md", contrato(
        p, d(300), "OC-4471", "Nubia Cloud Services S.A.S.", [
            ("Landing zone certificada", d(210), 1_800_000_000, "recibido"),
            ("Plan de reversión", d(150), 300_000_000, "recibido"),
            ("Migración de las primeras 20 aplicaciones", d(45), 2_400_000_000,
             "pendiente"),
            ("Migración de las 20 restantes", f(90), 2_000_000_000, "pendiente")]))
    c.plan(d(305), "cronograma-v1.csv", cronograma(p, 1, [
        ("Landing zone", d(210), d(210), "cerrado"),
        ("Primeras 20 aplicaciones", d(45), d(45), "en curso"),
        ("20 restantes", f(90), f(90), "no iniciado"),
        ("Cierre del centro de datos", f(200), f(200), "no iniciado")]))
    c.seguimiento(d(205), "acta-recibo-landing-zone.md", recibo(
        p, d(205), "Landing zone certificada", p["gerente"],
        "Se verificó la línea base de seguridad y el etiquetado de recursos."))
    c.seguimiento(d(30), "factura-NCS-2291.md", factura(
        p, d(30), "NCS-2291", "Nubia Cloud Services S.A.S.",
        "Migración de las primeras 20 aplicaciones", 2_400_000_000))
    c.seguimiento(d(14), "informe-avance.md", informe(
        p, "Amarillo", d(14), 61,
        ["La landing zone está recibida y operando",
         "Las primeras 20 aplicaciones siguen en migración: van 14 de 20",
         "Se radicó la factura del segundo entregable"]))
    c.reunion(d(16), "seguimiento-proveedor.md", minuta(
        p, d(16), ["Felipe Arango", "Representante de Nubia Cloud"],
        ["Avance de la migración de las primeras 20 aplicaciones",
         "Radicación de la factura NCS-2291"],
        [{"quien": "Nubia Cloud",
          "que": "Cerrar las 6 aplicaciones faltantes del primer lote",
          "para": f(15)}]))
    plantado.append((p["codigo"], p["nombre"], [
        "**Entregable de proveedor tardío**: «primeras 20 aplicaciones» venció hace 45 "
        "días y van 14 de 20",
        "**Facturado sin entrega**: la factura NCS-2291 cobra 2.400 millones de un "
        "entregable que no tiene acta de recibo",
        "El único entregable con acta de recibo es la landing zone, y está al día"]))

    # ── PRY-104 · silencio y declaración vieja
    p = dict(codigo="PRY-104", nombre="Open Banking fase 2",
             carpeta="PRY-104-open-banking-f2",
             area="Canales Digitales", patrocinador="Laura Vélez, VP Digital",
             gerente="Óscar Ramírez", comite="Comité de Transformación Digital",
             producto="APIs de datos de cuenta", aprobacion=d(500),
             objetivo="Exponer las APIs de datos de cuenta y de iniciación de pago "
                      "bajo el estándar del regulador.",
             alcance=["API de datos de cuenta", "API de iniciación de pago",
                      "Portal de desarrolladores"],
             fuera=["Modelo de monetización, que lo define Producto"],
             inicio=d(490), cierre=f(60),
             presupuesto=3_100_000_000, comprometido=1_900_000_000,
             ejecutado=1_700_000_000, proyeccion=3_000_000_000,
             exito="Las dos APIs certificadas por el regulador.",
             riesgos=["El estándar del regulador sigue en consulta"])
    c = port.caso(p["codigo"], "proyecto", p["carpeta"])
    c.gobierno(p["aprobacion"], "acta-constitucion.md", acta(p))
    c.seguimiento(d(52), "nota-avance.md", informe(
        p, "Verde", d(52), 65,
        ["Se publicó la API de datos de cuenta en ambiente de certificación",
         "La iniciación de pago espera la versión final del estándar"]))
    plantado.append((p["codigo"], p["nombre"], [
        "**Silencio**: el último documento tiene 52 días, muy por encima del umbral de 15",
        "**Declaración vieja**: el estado Verde se declaró hace 52 días, por encima del "
        "umbral de 30",
        "**Sin cronograma**: no hay línea base contra la que medir nada, y eso es un "
        "hallazgo y no una omisión del generador",
        "Cierra en 60 días con 65% de avance declarado hace casi dos meses"]))

    # ── PRY-105 · CONTROL NEGATIVO
    p = dict(codigo="PRY-105", nombre="Tarjeta débito contactless",
             carpeta="PRY-105-debito-contactless",
             area="Medios de Pago", patrocinador="Gustavo Neira, VP de Medios de Pago",
             gerente="Paula Céspedes", comite="Comité de Medios de Pago",
             producto="Tarjeta débito", aprobacion=d(150),
             objetivo="Emitir la tarjeta débito con tecnología contactless y habilitar "
                      "el pago sin contacto en la red propia.",
             alcance=["Emisión contactless", "Habilitación en datáfonos propios",
                      "Campaña de activación"],
             fuera=["Tarjeta de crédito, que va en otro proyecto"],
             inicio=d(145), cierre=f(45),
             presupuesto=2_400_000_000, comprometido=1_600_000_000,
             ejecutado=1_500_000_000, proyeccion=2_350_000_000,
             exito="60% de la base con tarjeta contactless al cierre.",
             riesgos=["Sin riesgos nuevos en el periodo"])
    c = port.caso(p["codigo"], "proyecto", p["carpeta"])
    c.gobierno(p["aprobacion"], "acta-constitucion.md", acta(p))
    c.plan(d(143), "cronograma-v1.csv", cronograma(p, 1, [
        ("Certificación de la marca", d(90), d(90), "cerrado"),
        ("Emisión del primer lote", d(30), d(30), "cerrado"),
        ("Habilitación de datáfonos", f(10), f(10), "en curso"),
        ("Campaña de activación", f(45), f(45), "no iniciado")]))
    c.seguimiento(d(88), "acta-recibo-certificacion.md", recibo(
        p, d(88), "Certificación de la marca", p["gerente"],
        "Certificado emitido por la franquicia, vigente por 24 meses."))
    c.seguimiento(d(28), "acta-recibo-primer-lote.md", recibo(
        p, d(28), "Emisión del primer lote", p["gerente"],
        "Se recibieron 50.000 plásticos y se verificó el 1% por muestreo."))
    c.seguimiento(d(6), "informe-avance.md", informe(
        p, "Verde", d(6), 78,
        ["Los dos hitos vencidos están cerrados con acta de recibo",
         "La habilitación de datáfonos va conforme al plan",
         "La campaña arranca la primera semana del mes entrante"]))
    c.reunion(d(7), "comite-medios-pago.md", minuta(
        p, d(7), ["Gustavo Neira", "Paula Céspedes"],
        ["Avance de la habilitación de datáfonos", "Plan de la campaña de activación"],
        [{"quien": "Paula Céspedes", "que": "Presentar el plan de campaña",
          "para": f(12)}]))
    plantado.append((p["codigo"], p["nombre"], [
        "**CONTROL NEGATIVO · no debe producir ni un hallazgo.** Todos los hitos "
        "vencidos tienen acta de recibo, la declaración tiene 6 días, el último "
        "documento tiene 6 días, la proyección está bajo el aprobado y el único "
        "compromiso abierto vence en 12 días.",
        "Un agente que reporte algo de este proyecto está generando ruido."]))

    # ── PRY-106 · cambio sin línea base, presupuesto comprometido
    p = dict(codigo="PRY-106", nombre="Monitoreo transaccional SARLAFT",
             carpeta="PRY-106-sarlaft",
             area="Riesgo y Cumplimiento", patrocinador="Elena Duarte, Oficial de Cumplimiento",
             gerente="Mauricio Pérez", comite="Comité de Riesgos",
             producto="No aplica", aprobacion=d(260),
             objetivo="Reemplazar el monitoreo transaccional por una plataforma con "
                      "reglas configurables y trazabilidad de alerta a reporte.",
             alcance=["Motor de reglas", "Cola de alertas con trazabilidad",
                      "Reporte automático al regulador"],
             fuera=["Debida diligencia de clientes, que es de otro frente"],
             inicio=d(255), cierre=f(90),
             presupuesto=6_800_000_000, comprometido=6_460_000_000,
             ejecutado=4_900_000_000, proyeccion=7_100_000_000,
             exito="Cero hallazgos de la auditoría regulatoria sobre trazabilidad.",
             riesgos=["El presupuesto comprometido está al 95% del aprobado"])
    c = port.caso(p["codigo"], "proyecto", p["carpeta"])
    c.gobierno(p["aprobacion"], "acta-constitucion.md", acta(p))
    c.plan(d(250), "cronograma-v1.csv", cronograma(p, 1, [
        ("Motor de reglas", d(100), d(100), "cerrado"),
        ("Cola de alertas", d(20), f(25), "en curso"),
        ("Reporte al regulador", f(60), f(60), "no iniciado")]))
    c.gobierno(d(240), "contrato-oc-5580.md", contrato(
        p, d(240), "OC-5580", "Vigía Analítica S.A.S.", [
            ("Modelo de segmentación de clientes", d(60), 480_000_000, "pendiente"),
            ("Tablero de alertas", f(40), 520_000_000, "pendiente")]))
    c.seguimiento(d(35), "factura-VA-118.md", factura(
        p, d(35), "VA-118", "Vigía Analítica S.A.S.",
        "Anticipo del modelo de segmentación", 240_000_000))
    c.seguimiento(d(45), "solicitud-cambio-cc-07.md", cambio(
        p, d(45), "CC-07",
        "Ampliar la cola de alertas para cubrir los canales digitales, que no estaban "
        "en el alcance original.", 45, 620_000_000,
        "Pendiente de presentación al Comité de Riesgos."))
    c.seguimiento(d(9), "informe-avance.md", informe(
        p, "Amarillo", d(9), 66,
        ["La cola de alertas se amplió a canales digitales, según CC-07",
         "El motor de reglas está cerrado y en producción",
         "El comprometido llegó al 95% del presupuesto aprobado"]))
    c.reunion(d(11), "comite-riesgos.md", minuta(
        p, d(11), ["Elena Duarte", "Mauricio Pérez", "Auditoría Interna"],
        ["Ampliación de alcance a canales digitales",
         "Situación del presupuesto comprometido"],
        [{"quien": "Mauricio Pérez",
          "que": "Presentar CC-07 al comité para autorización formal", "para": f(8)}]))
    plantado.append((p["codigo"], p["nombre"], [
        "**Cambio sin línea base nueva**: CC-07 mueve 45 días y 620 millones, el "
        "cronograma vigente ya lo refleja, y no hay línea base v2 ni autorización",
        "**Un hito declarado cerrado sin acta de recibo**: «Motor de reglas»",
        "**Presupuesto comprometido al 95%**, por encima del umbral de 90%",
        "**Proyección por encima del aprobado**: 7.100 contra 6.800 millones, 4,4% — "
        "también bajo el umbral, así que tampoco debe salir como desviación de costo"]))

    # ── PRY-107 · patrocinador contradicho, cambio de gobernanza
    p = dict(codigo="PRY-107", nombre="Billetera y pagos QR",
             carpeta="PRY-107-billetera-qr",
             area="Canales Digitales", patrocinador="Laura Vélez, VP Digital",
             gerente="Camilo Beltrán", comite="Comité de Transformación Digital",
             producto="PRD-QR · Pagos QR comercios", aprobacion=d(300),
             objetivo="Lanzar la billetera propia con pago QR interoperable en "
                      "comercios aliados.",
             alcance=["Billetera con QR interoperable",
                      "Vinculación de comercios", "Conciliación diaria"],
             fuera=["Crédito dentro de la billetera"],
             inicio=d(295), cierre=f(150),
             presupuesto=5_600_000_000, comprometido=3_400_000_000,
             ejecutado=2_900_000_000, proyeccion=5_500_000_000,
             exito="120.000 comercios activos en los seis meses siguientes al cierre.",
             riesgos=["La interoperabilidad depende del esquema del banco central"])
    c = port.caso(p["codigo"], "proyecto", p["carpeta"])
    c.gobierno(p["aprobacion"], "acta-constitucion.md", acta(p))
    c.plan(d(290), "cronograma-v1.csv", cronograma(p, 1, [
        ("Billetera con QR", d(60), d(60), "cerrado"),
        ("Vinculación de comercios", f(30), f(30), "en curso"),
        ("Conciliación diaria", f(150), f(150), "no iniciado")]))
    c.seguimiento(d(58), "acta-recibo-billetera.md", recibo(
        p, d(58), "Billetera con QR", p["gerente"],
        "Pruebas de interoperabilidad superadas con dos adquirentes."))
    c.seguimiento(d(13), "informe-avance.md", informe(
        p, "Verde", d(13), 58,
        ["La billetera está en producción con QR interoperable",
         "La vinculación de comercios va por 34.000 de los 120.000 esperados",
         "El proyecto pasó al Comité de Medios de Pago"]))
    # Samuel publica su ficha, y la escribe con lo que él vio en el comité: el
    # patrocinador nuevo. El acta de constitución sigue diciendo el anterior.
    c.gobierno(d(13), "ficha-proyecto.json", ficha_publicada(p, d(13), {
        "_fuente": "30-reuniones/comite-medios-pago.md",
        "code": "PRY-107", "sponsor": "Gustavo Neira, VP de Medios de Pago",
        "manager": "Camilo Beltrán", "committee": "Comité de Medios de Pago",
        "product": "PRD-QR"}))
    c.reunion(d(15), "comite-medios-pago.md", minuta(
        p, d(15),
        ["Gustavo Neira", "Camilo Beltrán", "Equipo de Canales"],
        ["Traslado del proyecto del Comité de Transformación al de Medios de Pago",
         "Nuevo patrocinio del proyecto",
         "Avance de vinculación de comercios"],
        [{"quien": "Camilo Beltrán",
          "que": "Actualizar el acta de constitución con el nuevo patrocinador y comité",
          "para": f(5)}]))
    plantado.append((p["codigo"], p["nombre"], [
        "**Patrocinador contradicho**: el acta dice Laura Vélez y la minuta de hace 15 "
        "días dice que el patrocinio pasó a Gustavo Neira. El acta nunca se actualizó",
        "**Cambio de gobernanza**: el comité cambió de Transformación Digital a Medios "
        "de Pago, y el documento de gobierno sigue diciendo el anterior",
        "Este es el caso donde **el gerente tiene razón y la PMO está leyendo papel "
        "viejo**"]))

    # ── PRY-108 · contradicción entre dos documentos
    p = dict(codigo="PRY-108", nombre="Onboarding digital PyME",
             carpeta="PRY-108-onboarding-pyme",
             area="Banca PyME", patrocinador="Ricardo Salas, VP Banca Empresas",
             gerente="Natalia Ospina", comite="Comité de Banca Empresas",
             producto="PRD-PYME · Cuenta PyME", aprobacion=d(200),
             objetivo="Abrir cuenta PyME de forma remota en menos de un día hábil.",
             alcance=["Validación de existencia y representación legal",
                      "Debida diligencia simplificada", "Apertura y activación remota"],
             fuera=["Cupo de crédito, que es de otro proyecto"],
             inicio=d(195), cierre=f(75),
             presupuesto=2_900_000_000, comprometido=1_700_000_000,
             ejecutado=1_500_000_000, proyeccion=2_850_000_000,
             exito="70% de las aperturas PyME por canal remoto.",
             riesgos=["La debida diligencia simplificada necesita concepto de "
                      "Cumplimiento"])
    c = port.caso(p["codigo"], "proyecto", p["carpeta"])
    c.gobierno(p["aprobacion"], "acta-constitucion.md", acta(p))
    c.plan(d(190), "cronograma-v1.csv", cronograma(p, 1, [
        ("Validación de existencia", d(80), d(80), "cerrado"),
        ("Debida diligencia simplificada", f(20), f(20), "en curso"),
        ("Apertura remota", f(75), f(105), "no iniciado")]))
    c.seguimiento(d(78), "acta-recibo-validacion.md", recibo(
        p, d(78), "Validación de existencia y representación legal", p["gerente"],
        "Integración con la cámara de comercio verificada en 200 casos."))
    c.seguimiento(d(8), "informe-avance.md", informe(
        p, "Verde", d(8), 62,
        ["La validación de existencia está recibida",
         "La debida diligencia simplificada espera concepto de Cumplimiento",
         "El cierre se mantiene en la fecha comprometida"]))
    c.reunion(d(10), "comite-banca-empresas.md", minuta(
        p, d(10), ["Ricardo Salas", "Natalia Ospina", "Cumplimiento"],
        ["Concepto de Cumplimiento sobre la debida diligencia simplificada",
         "Confirmación de la fecha de cierre"],
        [{"quien": "Cumplimiento", "que": "Emitir el concepto sobre debida diligencia "
                                          "simplificada", "para": f(6)}]))
    plantado.append((p["codigo"], p["nombre"], [
        "**Contradicción entre dos documentos**: el cronograma pone la apertura remota "
        "30 días después del cierre que declara el acta, y el informe dice que el "
        "cierre se mantiene. Los tres documentos no pueden ser ciertos a la vez",
        "Es el caso donde **la respuesta correcta es señalar el conflicto, no elegir "
        "una fuente**"]))

    # ── PRY-109 · desviación de costo
    p = dict(codigo="PRY-109", nombre="Motor de decisión de crédito",
             carpeta="PRY-109-motor-decision",
             area="Riesgo de Crédito", patrocinador="Elena Duarte, Oficial de Cumplimiento",
             gerente="Jorge Medina", comite="Comité de Riesgos",
             producto="No aplica", aprobacion=d(280),
             objetivo="Centralizar la decisión de crédito de consumo e hipotecario en "
                      "un motor con modelos versionados y trazabilidad de decisión.",
             alcance=["Motor de reglas y modelos", "Versionado y trazabilidad",
                      "Integración con originación de consumo"],
             fuera=["Originación hipotecaria, que consume el motor desde PRY-101"],
             inicio=d(275), cierre=f(110),
             presupuesto=7_400_000_000, comprometido=5_900_000_000,
             ejecutado=5_600_000_000, proyeccion=8_600_000_000,
             exito="Todas las decisiones de consumo pasando por el motor, con traza.",
             riesgos=["El costo de la plataforma de modelos superó lo estimado"])
    c = port.caso(p["codigo"], "proyecto", p["carpeta"])
    c.gobierno(p["aprobacion"], "acta-constitucion.md", acta(p))
    c.plan(d(270), "cronograma-v1.csv", cronograma(p, 1, [
        ("Motor de reglas", d(150), d(150), "cerrado"),
        ("Versionado y trazabilidad", d(50), d(50), "cerrado"),
        ("Integración con consumo", f(40), f(40), "en curso"),
        ("Cierre", f(110), f(110), "no iniciado")]))
    c.seguimiento(d(148), "acta-recibo-motor.md", recibo(
        p, d(148), "Motor de reglas", p["gerente"], "Pruebas de carga superadas."))
    c.seguimiento(d(47), "acta-recibo-versionado.md", recibo(
        p, d(47), "Versionado y trazabilidad", p["gerente"],
        "Se verificó la traza de 500 decisiones contra su versión de modelo."))
    c.seguimiento(d(70), "solicitud-cambio-cc-11.md", cambio(
        p, d(70), "CC-11",
        "Ampliar el versionado a los modelos de crédito hipotecario, que PRY-101 "
        "consume desde este motor.", 30, 380_000_000,
        "Autorizada por el Comité de Riesgos el " + d(64) + "."))
    c.seguimiento(d(5), "informe-avance.md", informe(
        p, "Amarillo", d(5), 71,
        ["Los dos hitos vencidos están cerrados con acta",
         "La integración con consumo va conforme al plan",
         "La proyección al cierre está 16% por encima del aprobado por el costo de la "
         "plataforma de modelos"]))
    c.reunion(d(6), "comite-riesgos.md", minuta(
        p, d(6), ["Elena Duarte", "Jorge Medina"],
        ["Desviación de costo por la plataforma de modelos",
         "Avance de la integración con consumo"],
        [{"quien": "Jorge Medina",
          "que": "Traer las opciones para cubrir la desviación de costo", "para": f(9)}]))
    plantado.append((p["codigo"], p["nombre"], [
        "**Desviación de costo · la única que dispara**: proyección de 8.600 contra "
        "7.400 millones aprobados, **+16,2%**, por encima del umbral de 10%",
        "Todo lo demás está al día: es el caso donde debe salir **una sola señal** y no "
        "un informe entero",
        "**PRY-101 declara depender de este proyecto y aquí no se menciona** — la "
        "dependencia no está confirmada de los dos lados"]))

    # ── PRY-110 · el proyecto que ejecuta un producto
    p = dict(codigo="PRY-110", nombre="Nómina electrónica empresarial",
             carpeta="PRY-110-nomina-electronica",
             area="Banca Empresas", patrocinador="Ricardo Salas, VP Banca Empresas",
             gerente="Liliana Torres", comite="Comité de Banca Empresas",
             producto="PRD-NOMINA · Nómina empresarial", aprobacion=d(120),
             objetivo="Dispersar nómina de empresas clientes con archivo único y "
                      "conciliación automática.",
             alcance=["Carga de archivo de nómina", "Dispersión masiva",
                      "Conciliación y certificado de pago"],
             fuera=["Préstamos sobre nómina"],
             inicio=d(115), cierre=f(170),
             presupuesto=3_300_000_000, comprometido=1_400_000_000,
             ejecutado=1_200_000_000, proyeccion=3_250_000_000,
             exito="500 empresas dispersando nómina por el canal.",
             riesgos=["Sin riesgos nuevos en el periodo"])
    c = port.caso(p["codigo"], "proyecto", p["carpeta"])
    c.gobierno(p["aprobacion"], "acta-constitucion.md", acta(p))
    c.plan(d(113), "cronograma-v1.csv", cronograma(p, 1, [
        ("Carga de archivo", d(40), d(40), "cerrado"),
        ("Dispersión masiva", f(50), f(50), "en curso"),
        ("Conciliación y certificado", f(170), f(170), "no iniciado")]))
    c.seguimiento(d(38), "acta-recibo-carga.md", recibo(
        p, d(38), "Carga de archivo de nómina", p["gerente"],
        "Se procesaron archivos de 12 empresas piloto sin rechazo."))
    c.seguimiento(d(11), "informe-avance.md", informe(
        p, "Verde", d(11), 41,
        ["La carga de archivo está recibida y en piloto con 12 empresas",
         "La dispersión masiva va conforme al plan"]))
    c.reunion(d(12), "comite-banca-empresas.md", minuta(
        p, d(12), ["Ricardo Salas", "Liliana Torres"],
        ["Resultado del piloto de carga de archivo", "Plan de dispersión masiva"],
        [{"quien": "Liliana Torres", "que": "Ampliar el piloto a 30 empresas",
          "para": f(20)}]))
    plantado.append((p["codigo"], p["nombre"], [
        "Está al día. Su razón de estar es **el enlace con el producto**: es el "
        "proyecto que construye PRD-NOMINA, y `/product-view` tiene que encontrarlo",
        "PRD-COBROS también declara ejecutarse por este proyecto, y eso es la "
        "**superposición de producto** que Alba debe reportar"]))

    return plantado


# ══════════════════════════════════════════════════════════════════════════
# Los ocho productos
# ══════════════════════════════════════════════════════════════════════════

def definicion_producto(x) -> str:
    return f"""
# Definición de producto · {x['nombre']}

**Código:** {x['codigo']}
**Gerente de producto:** {x['gerente']}
**Segmento:** {x['segmento']}
**Fecha de la definición:** {x['fecha']}

## El problema

{x['problema']}

## La propuesta

{chr(10).join('- ' + a for a in x['propuesta'])}

## Supuestos

{chr(10).join(f"- **{s['que']}** · declarado el {s['desde']} · " + ("verificado" if s.get('verificado') else "sin verificar") for s in x['supuestos'])}

## Proyectos que lo construyen

{chr(10).join('- ' + p for p in x.get('proyectos', ['Ninguno declarado']))}
"""


def caso_negocio(x) -> str:
    filas = "\n".join(f"| {m['clave']} | {plata(m['declarado'])} | {m['fuente']} |"
                      for m in x['cifras'])
    return f"""
# Caso de negocio · {x['nombre']}

**Código:** {x['codigo']}
**Fecha:** {x['fecha_caso']}
**Preparado por:** {x['gerente']}

## Cifras que sostienen el caso

| Métrica | Valor declarado | Fuente |
|---|---|---|
{filas}

## Retorno esperado

{x['retorno']}
"""


def entrevistas(x) -> str:
    bloques = []
    for e in x['entrevistas']:
        bloques.append(f"""### {e['quien']} · {e['cuando']}

> {e['dijo']}

**Tema:** {e['tema']}""")
    return f"""
# Entrevistas · {x['nombre']}

**Ronda:** {x['ronda']}
**Realizadas por:** {x['gerente']}

{chr(10).join(bloques)}
"""


def tablero(x) -> str:
    filas = "\n".join(f"| {m['clave']} | {plata(m['medido'])} | {m['corte']} |"
                      for m in x['cifras'] if m.get('medido'))
    return f"""
# Tablero de métricas · {x['nombre']}

**Fuente:** bodega de datos, tablero de producto
**Última actualización:** {x['corte_tablero']}

| Métrica | Valor medido | Corte |
|---|---|---|
{filas}
"""


def comite_producto(x) -> str:
    filas = "\n".join(
        f"| {r['id']} | {r['que']} | {r['doliente']} | {r.get('criterio') or '—'} "
        f"| {r.get('evidencia') or '—'} | {r['estado']} | {r['desde']} "
        f"| {r.get('proyecto') or '—'} |"
        for r in x['requerimientos'])
    return f"""
# Comité de producto · {x['nombre']}

**Fecha:** {x['comite_fecha']}
**Asistentes:** {', '.join(x['asistentes'])}

## Requerimientos revisados

| ID | Requerimiento | Doliente | Criterio de aceptación | Quién lo pidió | Estado | Desde | Proyecto que lo ejecuta |
|---|---|---|---|---|---|---|---|
{filas}

## Decisiones

{chr(10).join('- ' + y for y in x['decisiones'])}
"""


def productos(port: corpus.Portafolio) -> list:
    plantado = []
    casos = [
        # ── PRD-QR · el negocio declara una cifra que la métrica no sostiene
        dict(codigo="PRD-QR", nombre="Pagos QR comercios", gerente="Camilo Beltrán",
             segmento="Comercios de barrio y microcomercio", fecha=d(207),
             fecha_caso=d(207), corte_tablero=d(26), ronda=f"Comercios · {d(148)}",
             comite_fecha=d(19),
             problema="El microcomercio no acepta pagos digitales porque el datáfono "
                      "tiene costo fijo y el QR no está interoperado.",
             propuesta=["QR interoperable sin costo fijo para el comercio",
                        "Liquidación al día siguiente",
                        "Conciliación en la app del comercio"],
             supuestos=[dict(que="El comercio acepta liquidación a un día y no exige "
                                 "inmediata", desde=d(207)),
                        dict(que="La interoperabilidad del banco central estará "
                                 "disponible este año", desde=d(207))],
             proyectos=["PRY-107 · Billetera y pagos QR"],
             cifras=[dict(clave="tx_mensuales", declarado=250_000, medido=180_000,
                          fuente=f"Proyección del caso de negocio, {d(207)}",
                          corte=d(26)),
                     dict(clave="comercios_activos", declarado=40_000, medido=34_000,
                          fuente=f"Proyección del caso de negocio, {d(207)}",
                          corte=d(26))],
             retorno="Retorno en 18 meses con 250.000 transacciones mensuales.",
             entrevistas=[
                 dict(quien="Tienda La Esquina, Kennedy", cuando=d(148),
                      dijo="El datáfono me cobra fijo así no venda. El QR lo uso "
                           "porque no me cuesta.",
                      tema="Costo fijo del datáfono"),
                 dict(quien="Panadería El Trigal, Suba", cuando=d(148),
                      dijo="Yo necesito la plata el mismo día, no al otro día.",
                      tema="Tiempo de liquidación")],
             asistentes=["Camilo Beltrán", "Laura Vélez", "Equipo de Canales"],
             requerimientos=[
                 dict(id="REQ-201", que="QR interoperable con dos adquirentes",
                      criterio="dos adquirentes distintos liquidan una transacción de prueba",
                      evidencia="Tienda La Esquina, Kennedy",
                      doliente="Camilo Beltrán", estado="aceptado", desde=d(180)),
                 dict(id="REQ-202", que="Liquidación mismo día para comercios con más "
                                        "de 200 transacciones al mes",
                      criterio="una transacción de un comercio con más de 200 al mes queda liquidada el mismo día",
                      evidencia="Panadería El Trigal, Suba",
                      doliente="Camilo Beltrán", estado="propuesto", desde=d(95))],
             decisiones=["Se construye la liquidación a un día y se evalúa la del "
                         "mismo día con la evidencia de la ronda siguiente"],
             planta=["**El negocio declara una cifra que la métrica no sostiene**: el "
                     "caso dice 250.000 transacciones mensuales y el tablero mide "
                     "180.000 — 28% de diferencia, por encima del umbral de 20%",
                     "**Supuesto sin verificar**: la liquidación a un día lleva 207 "
                     "días declarada, y la entrevista de la panadería la contradice",
                     "**Requerimiento sin decidir**: REQ-202 lleva 95 días propuesto, "
                     "por encima del umbral de 60",
                     "**Superposición con PRD-COBROS**: comparten la métrica "
                     "`tx_mensuales` y el proyecto PRY-107"]),

        # ── PRD-NOMINA · CONTROL NEGATIVO
        dict(codigo="PRD-NOMINA", nombre="Nómina empresarial", gerente="Liliana Torres",
             segmento="Empresas de 50 a 500 empleados", fecha=d(40),
             fecha_caso=d(40), corte_tablero=d(9), ronda=f"Empresas · {d(52)}",
             comite_fecha=d(14),
             problema="Las empresas medianas dispersan nómina con archivo plano y "
                      "conciliación manual, y el error cuesta un día de tesorería.",
             propuesta=["Archivo único con validación previa",
                        "Dispersión masiva con confirmación",
                        "Certificado de pago por empleado"],
             supuestos=[dict(que="La empresa mantiene su archivo de nómina en un "
                                 "formato exportable", desde=d(25))],
             proyectos=["PRY-110 · Nómina electrónica empresarial"],
             cifras=[dict(clave="dispersiones_mensuales", declarado=12_000,
                          medido=11_600,
                          fuente=f"Piloto de 12 empresas, {d(40)}", corte=d(9))],
             retorno="Retorno en 24 meses con 500 empresas activas.",
             entrevistas=[
                 dict(quien="Distribuidora Andina, Gerente de Gente", cuando=d(52),
                      dijo="Nosotros armamos el archivo a mano y siempre se cae uno. "
                           "Si el banco lo valida antes, me ahorra el día.",
                      tema="Validación previa del archivo"),
                 dict(quien="Textiles del Norte, Tesorería", cuando=d(52),
                      dijo="Necesito el certificado por empleado para el fondo.",
                      tema="Certificado de pago")],
             asistentes=["Liliana Torres", "Ricardo Salas"],
             requerimientos=[
                 dict(id="REQ-301", que="Validación del archivo antes de dispersar",
                      criterio="un archivo con un registro inválido se rechaza antes de dispersar, y dice cuál",
                      evidencia="Distribuidora Andina",
                      doliente="Liliana Torres", estado="aceptado", desde=d(45)),
                 dict(id="REQ-302", que="Certificado de pago por empleado",
                      criterio="el certificado de un empleado se descarga desde la app de la empresa",
                      evidencia="Textiles del Norte",
                      doliente="Liliana Torres", estado="aceptado", desde=d(45))],
             decisiones=["Se construyen los dos requerimientos en PRY-110, con la "
                         "evidencia de las entrevistas de hace 52 días"],
             planta=["**CONTROL NEGATIVO · no debe producir ni un hallazgo.** Los dos "
                     "requerimientos tienen doliente, criterio y evidencia; el supuesto "
                     "tiene 25 días; la evidencia tiene 52 días; la cifra declarada y "
                     "la medida difieren 3%; y el proyecto que lo construye confirma "
                     "que lo construye.",
                     "Un agente que reporte algo de este producto está generando ruido."]),

        # ── PRD-HIPO · requerimientos sin doliente y sin criterio
        dict(codigo="PRD-HIPO", nombre="Crédito hipotecario digital",
             gerente="Andrés Lozano", segmento="Vivienda no VIS", fecha=d(230),
             fecha_caso=d(230), corte_tablero=d(20), ronda=f"Compradores · {d(190)}",
             comite_fecha=d(22),
             problema="El comprador abandona la solicitud hipotecaria porque le piden "
                      "quince documentos en papel y no sabe en qué va.",
             propuesta=["Solicitud digital con estado visible",
                        "Validación de ingresos sin papel",
                        "Firma electrónica de la promesa"],
             supuestos=[dict(que="El comprador acepta firma electrónica para la "
                                 "promesa de compraventa", desde=d(230))],
             proyectos=["PRY-101 · Originación digital hipotecaria"],
             cifras=[dict(clave="solicitudes_mensuales", declarado=3_200, medido=2_950,
                          fuente=f"Histórico de canal, {d(230)}", corte=d(20))],
             retorno="Retorno en 30 meses con 80% de originación digital.",
             entrevistas=[
                 dict(quien="Comprador, Chapinero", cuando=d(190),
                      dijo="Entregué los papeles y durante tres semanas nadie me dijo "
                           "nada. Llamé yo.",
                      tema="Estado visible de la solicitud")],
             asistentes=["Andrés Lozano", "María Restrepo"],
             requerimientos=[
                 dict(id="REQ-401", que="Estado de la solicitud visible para el cliente",
                      criterio="el cliente ve el estado de su solicitud sin llamar a nadie",
                      evidencia="Comprador, Chapinero",
                      doliente="Andrés Lozano", estado="aceptado", desde=d(200)),
                 dict(id="REQ-402", que="Validación de ingresos sin soporte físico",
                      criterio="una solicitud se aprueba sin un solo soporte en papel",
                      evidencia="Comprador, Chapinero",
                      doliente="sin asignar", estado="aceptado", desde=d(200)),
                 dict(id="REQ-403", que="Firma electrónica de la promesa",
                      evidencia="Comprador, Chapinero",
                      doliente="Andrés Lozano", estado="aceptado", desde=d(200))],
             decisiones=["Se priorizan los tres requerimientos para PRY-101"],
             planta=["**Requerimiento sin doliente**: REQ-402 está aceptado y no tiene "
                     "quién responda por él",
                     "**Requerimiento sin criterio de aceptación**: REQ-403 dice «firma "
                     "electrónica de la promesa» y no dice cómo se verifica que está "
                     "hecho",
                     "**Supuesto sin verificar**: la firma electrónica lleva 230 días "
                     "declarada sin que nadie la valide con un comprador"]),

        # ── PRD-PYME · requerimiento sin decidir hace mucho
        dict(codigo="PRD-PYME", nombre="Cuenta PyME", gerente="Natalia Ospina",
             segmento="PyME de 5 a 50 empleados", fecha=d(175),
             fecha_caso=d(175), corte_tablero=d(17), ronda=f"PyME · {d(160)}",
             comite_fecha=d(28),
             problema="La PyME tarda ocho días en abrir cuenta porque la debida "
                      "diligencia exige presencia del representante legal.",
             propuesta=["Apertura remota con validación de cámara de comercio",
                        "Debida diligencia simplificada por nivel de riesgo",
                        "Activación el mismo día"],
             supuestos=[dict(que="Cumplimiento aprueba la debida diligencia "
                                 "simplificada para riesgo bajo", desde=d(175))],
             proyectos=["PRY-108 · Onboarding digital PyME"],
             cifras=[dict(clave="aperturas_mensuales", declarado=1_800, medido=1_700,
                          fuente=f"Histórico de canal, {d(175)}", corte=d(17))],
             retorno="Retorno en 20 meses con 70% de apertura remota.",
             entrevistas=[
                 dict(quien="Ferretería industrial, gerente", cuando=d(160),
                      dijo="Perdí dos días yendo a la oficina y al final me faltaba un "
                           "papel que nadie me había pedido.",
                      tema="Documentación exigida")],
             asistentes=["Natalia Ospina", "Ricardo Salas", "Cumplimiento"],
             requerimientos=[
                 dict(id="REQ-501", que="Validación de existencia por cámara de comercio",
                      criterio="la existencia se valida contra cámara de comercio en menos de un minuto",
                      evidencia="Ferretería industrial",
                      doliente="Natalia Ospina", estado="aceptado", desde=d(170)),
                 dict(id="REQ-502", que="Debida diligencia simplificada para riesgo bajo",
                      criterio="un cliente de riesgo bajo abre sin presencia del representante legal",
                      evidencia="Ferretería industrial",
                      doliente="Cumplimiento", estado="propuesto", desde=d(150)),
                 dict(id="REQ-503", que="Activación el mismo día de la apertura",
                      criterio="la cuenta queda operativa el mismo día de la apertura",
                      evidencia="Ferretería industrial",
                      doliente="Natalia Ospina", estado="propuesto", desde=d(140))],
             decisiones=["Se espera el concepto de Cumplimiento para decidir REQ-502"],
             planta=["**Dos requerimientos sin decidir**: REQ-502 lleva 150 días y "
                     "REQ-503 lleva 140, contra un umbral de 60. Eso no es un "
                     "pendiente: es una decisión que no se está tomando",
                     "**REQ-502 bloquea el proyecto**: PRY-108 depende de ese concepto "
                     "y su minuta lo pide para dentro de 6 días"]),

        # ── PRD-TARJETA · supuesto sin verificar
        dict(codigo="PRD-TARJETA", nombre="Tarjeta de crédito digital",
             gerente="Paula Céspedes", segmento="Asalariados de ingreso medio",
             fecha=d(95), fecha_caso=d(95), corte_tablero=d(13),
             ronda=f"Tarjetahabientes · {d(80)}", comite_fecha=d(16),
             problema="El cliente pide tarjeta y la recibe en diez días por correo "
                      "físico, y en ese tiempo ya compró con otra.",
             propuesta=["Aprobación y tarjeta virtual en minutos",
                        "Plástico opcional", "Cupo ajustable por el cliente"],
             supuestos=[dict(que="El cliente usa la tarjeta virtual sin esperar el "
                                 "plástico", desde=d(95)),
                        dict(que="El cupo ajustable no aumenta la mora", desde=d(95))],
             proyectos=["Ninguno declarado"],
             cifras=[dict(clave="colocaciones_mensuales", declarado=8_500, medido=8_100,
                          fuente=f"Histórico de canal, {d(95)}", corte=d(13))],
             retorno="Retorno en 22 meses con tarjeta virtual en minutos.",
             entrevistas=[
                 dict(quien="Cliente, Medellín", cuando=d(80),
                      dijo="Me aprobaron y me dijeron que esperara el plástico. Usé la "
                           "otra tarjeta.",
                      tema="Espera del plástico")],
             asistentes=["Paula Céspedes", "Gustavo Neira"],
             requerimientos=[
                 dict(id="REQ-601", que="Tarjeta virtual disponible al aprobar",
                      criterio="la tarjeta virtual permite una compra en línea al minuto de aprobada",
                      evidencia="Cliente, Medellín",
                      doliente="Paula Céspedes", estado="aceptado", desde=d(90)),
                 dict(id="REQ-602", que="Cupo ajustable por el cliente en la app",
                      criterio="el cliente sube y baja su cupo desde la app, dentro del rango aprobado",
                      doliente="Paula Céspedes", estado="aceptado", desde=d(90))],
             decisiones=["Se construyen los dos requerimientos, sujeto a que Riesgo "
                         "valide el efecto del cupo ajustable en la mora"],
             planta=["**Dos supuestos sin verificar**, los dos con 95 días contra un "
                     "umbral de 30. El del cupo ajustable y la mora es del tipo que "
                     "debería estar en el registro de riesgos y no en una definición",
                     "**Requerimiento sin traza**: REQ-601 y REQ-602 están aceptados y "
                     "**ningún proyecto los está construyendo** — «Ninguno declarado»",
                     "Es el caso de *lo decidido que nadie está construyendo*"]),

        # ── PRD-COBROS · superposición con PRD-QR
        dict(codigo="PRD-COBROS", nombre="Recaudos y cobros", gerente="Óscar Ramírez",
             segmento="Comercios de barrio y microcomercio", fecha=d(140),
             fecha_caso=d(140), corte_tablero=d(24), ronda=f"Comercios · {d(130)}",
             comite_fecha=d(21),
             problema="El comercio recauda por varios canales y concilia a mano al "
                      "final del día.",
             propuesta=["Recaudo unificado por QR y transferencia",
                        "Conciliación única", "Reporte de ventas del día"],
             supuestos=[dict(que="El comercio prefiere un solo canal de recaudo",
                             desde=d(140))],
             proyectos=["PRY-107 · Billetera y pagos QR"],
             cifras=[dict(clave="tx_mensuales", declarado=95_000, medido=88_000,
                          fuente=f"Proyección del caso de negocio, {d(140)}",
                          corte=d(24))],
             retorno="Retorno en 26 meses con recaudo unificado.",
             entrevistas=[
                 dict(quien="Minimercado, Bosa", cuando=d(130),
                      dijo="Me llegan por QR, por transferencia y en efectivo. Al final "
                           "del día no sé cuánto vendí.",
                      tema="Conciliación única")],
             asistentes=["Óscar Ramírez", "Laura Vélez"],
             requerimientos=[
                 dict(id="REQ-701", que="Recaudo unificado por QR y transferencia",
                      criterio="una venta por QR y una por transferencia salen en el mismo reporte",
                      evidencia="Minimercado, Bosa",
                      doliente="Óscar Ramírez", estado="aceptado", desde=d(135)),
                 dict(id="REQ-702", que="Reporte de ventas del día",
                      criterio="el comercio ve el total del día antes de cerrar",
                      evidencia="Minimercado, Bosa",
                      doliente="Óscar Ramírez", estado="aceptado", desde=d(135))],
             decisiones=["Se construye el recaudo unificado sobre PRY-107"],
             planta=["**Superposición de producto con PRD-QR**, en los tres ejes que "
                     "Alba mira: la misma métrica `tx_mensuales` contada dos veces, el "
                     "mismo proyecto PRY-107, y el mismo segmento de microcomercio",
                     "Es la pregunta que ningún tablero responde: **dos gerentes de "
                     "producto contando la misma transacción en dos casos de negocio**"]),

        # ── PRD-SEGUROS · evidencia envejecida
        dict(codigo="PRD-SEGUROS", nombre="Microseguros", gerente="Diana Molina",
             segmento="Base de la pirámide", fecha=d(520), fecha_caso=d(520),
             corte_tablero=d(30), ronda=f"Asegurados · {d(560)}", comite_fecha=d(35),
             problema="El cliente de ingreso bajo no compra seguro porque la prima "
                      "mensual es alta y el trámite de reclamación es presencial.",
             propuesta=["Prima diaria descontada del saldo",
                        "Reclamación por la app", "Cobertura básica sin examen"],
             supuestos=[dict(que="El cliente acepta débito diario del saldo",
                             desde=d(520))],
             proyectos=["Ninguno declarado"],
             cifras=[dict(clave="polizas_activas", declarado=45_000, medido=41_000,
                          fuente=f"Estudio de mercado, {d(520)}", corte=d(30))],
             retorno="Retorno en 36 meses con 45.000 pólizas activas.",
             entrevistas=[
                 dict(quien="Cliente, Soacha", cuando=d(560),
                      dijo="Si me lo quitan de a poquitos no lo siento. Pero si tengo "
                           "que ir a una oficina a reclamar, no sirve.",
                      tema="Prima diaria y reclamación remota")],
             asistentes=["Diana Molina", "Gustavo Neira"],
             requerimientos=[
                 dict(id="REQ-801", que="Prima diaria descontada del saldo",
                      criterio="la prima se descuenta a diario sin generar sobregiro",
                      evidencia="Cliente, Soacha",
                      doliente="Diana Molina", estado="aceptado", desde=d(500)),
                 dict(id="REQ-802", que="Reclamación por la app",
                      criterio="una reclamación se radica por la app y recibe número de caso",
                      evidencia="Cliente, Soacha",
                      doliente="Diana Molina", estado="propuesto", desde=d(500))],
             decisiones=["Se mantiene la definición a la espera de capacidad de "
                         "desarrollo"],
             planta=["**Evidencia de demanda envejecida**: la única entrevista tiene "
                     "560 días, muy por encima del umbral de 12 meses. La definición "
                     "sigue igual de convincente y su sustento ya no vale",
                     "**Supuesto sin verificar** con 520 días",
                     "**Requerimiento sin decidir** con 500 días: REQ-802",
                     "**Sin proyecto que lo construya**, y decidido hace año y medio"]),

        # ── PRD-REMESAS · decisión sin fuente, requerimiento sin traza
        dict(codigo="PRD-REMESAS", nombre="Remesas familiares", gerente="Felipe Arango",
             segmento="Receptores de remesas", fecha=d(110), fecha_caso=d(110),
             corte_tablero=d(15), ronda=f"Receptores · {d(100)}", comite_fecha=d(18),
             problema="El receptor de remesas cobra en efectivo en un punto físico y "
                      "pierde entre 4% y 6% entre comisión y tasa.",
             propuesta=["Abono directo a cuenta o billetera",
                        "Tasa visible antes de aceptar", "Sin comisión de retiro"],
             supuestos=[dict(que="El receptor abre cuenta si el abono es inmediato",
                             desde=d(28))],
             proyectos=["Ninguno declarado"],
             cifras=[dict(clave="remesas_mensuales", declarado=62_000, medido=59_500,
                          fuente=f"Datos del corresponsal, {d(110)}", corte=d(15))],
             retorno="Retorno en 28 meses con abono directo a cuenta.",
             entrevistas=[
                 dict(quien="Receptora, Pereira", cuando=d(100),
                      dijo="Me toca ir al punto, hacer fila y me cobran. Si me llegara "
                           "a la cuenta sería mejor, pero no tengo cuenta.",
                      tema="Abono a cuenta y bancarización")],
             asistentes=["Felipe Arango", "Laura Vélez"],
             requerimientos=[
                 dict(id="REQ-901", que="Abono directo a cuenta del receptor",
                      criterio="la remesa queda abonada en cuenta sin paso por oficina",
                      evidencia="Receptora, Pereira",
                      doliente="Felipe Arango", estado="aceptado", desde=d(105)),
                 dict(id="REQ-902", que="Tasa visible antes de aceptar la operación",
                      criterio="la tasa se muestra antes de que el receptor acepte",
                      evidencia="Receptora, Pereira",
                      doliente="Felipe Arango", estado="aceptado", desde=d(105)),
                 dict(id="REQ-903", que="Apertura de cuenta dentro del flujo de cobro",
                      criterio="el receptor sin cuenta abre una dentro del mismo flujo de cobro",
                      evidencia="Receptora, Pereira",
                      doliente="Felipe Arango", estado="aceptado", desde=d(105))],
             decisiones=["Se decide construir los tres requerimientos en el primer "
                         "trimestre disponible",
                         "Se define la tasa objetivo en 2% sobre el monto recibido"],
             planta=["**Decisión sin fuente**: la tasa objetivo de 2% se decide en el "
                     "comité y no hay ningún documento que la sustente — ni análisis, "
                     "ni comparación de mercado, ni concepto de Tesorería",
                     "**Tres requerimientos aceptados sin traza a ningún proyecto**",
                     "**Supuesto sin verificar** con 28 días, justo bajo el umbral de "
                     "30: es el que **NO** debe reportarse todavía, y sirve para ver si "
                     "el agente respeta el umbral en vez de reportar todo"]),
    ]

    for x in casos:
        c = port.caso(x["codigo"], "producto", x["codigo"])
        c.definicion(x["fecha"], "definicion-producto.md", definicion_producto(x))
        c.definicion(x["fecha_caso"], "caso-de-negocio.md", caso_negocio(x))
        c.descubrimiento(x["entrevistas"][0]["cuando"], "entrevistas.md", entrevistas(x))
        c.metrica(x["corte_tablero"], "tablero-metricas.md", tablero(x))
        c.decision(x["comite_fecha"], "comite-producto.md", comite_producto(x))
        plantado.append((x["codigo"], x["nombre"], x["planta"]))

    return plantado


# ══════════════════════════════════════════════════════════════════════════

def clave(pl_proy: list, pl_prod: list, destino: Path) -> str:
    def bloque(titulo, filas):
        out = [f"## {titulo}", ""]
        for codigo, nombre, puntos in filas:
            out.append(f"### {codigo} · {nombre}")
            out.append("")
            out += [f"- {p}" for p in puntos]
            out.append("")
        return "\n".join(out)

    return f"""# Lo que hay plantado en esta organización

**Banco Aurora no existe.** Ningún nombre, cifra ni documento de aquí viene de una
organización o una persona real. Se generó el {HOY.isoformat()} con
`tests/sintetico/organizacion.py`.

Esta página es **para ti, no para el agente**: está fuera de `documentos/` a propósito,
para que el barrido no la lea. Es la clave de respuestas contra la que se compara lo que
los agentes reporten.

**Diez proyectos y ocho productos.** Dos son controles negativos —PRY-105 y PRD-NOMINA—
y no deben producir ni un hallazgo. Un agente que encuentre algo ahí está generando
ruido, y eso es tan importante de verificar como que encuentre lo demás.

Las fechas son relativas al día de la generación, así que las señales de silencio, de
declaración vieja y de supuesto sin verificar se disparan igual si esto se corre en tres
meses.

---

{bloque("Proyectos", pl_proy)}
---

{bloque("Productos", pl_prod)}
---

## Lo que el extractor de referencia no puede encontrar

`tests/sintetico/extractor.py` convierte estos documentos en fichas sin modelo, para
poder probar la aritmética a escala. Dos de los hallazgos plantados **no los produce, y
no es un defecto suyo**: necesitan leer prosa y cruzarla entre documentos, que es
justamente lo que hace el modelo y no hace un parser.

| Dónde | Qué hace falta leer |
|---|---|
| **PRY-107** · patrocinador contradicho y cambio de gobernanza | El acta dice un patrocinador y una minuta, en prosa, dice que el patrocinio pasó a otra persona. Hay que entender la frase, no extraer un campo |
| **PRY-108** · contradicción entre dos documentos | El cronograma pone un hito después de la fecha de cierre que declara el acta, y el informe dice que el cierre se mantiene. Los tres no pueden ser ciertos a la vez, y verlo exige cruzarlos |

**Son la vara de la corrida con el agente**: si el modelo los encuentra y el extractor no,
ahí está medido lo que el modelo agrega. Y `decision_without_source` en PRD-REMESAS es el
tercero de la misma clase.

## Cómo se corre

A `documentos/proyectos/` se le apunta Vera. A la carpeta de un producto bajo
`documentos/productos/`, Alba. A la carpeta de un proyecto, Samuel. El estado que cada
agente escriba va en `estado/`, que empieza vacía.

**Ningún agente declara el estado de un proyecto.** El estado declarado ya está escrito
en los informes de avance de cada carpeta, que es donde lo pondría un gerente.
"""


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("uso: python3 tests/sintetico/organizacion.py <carpeta destino>")
    destino = Path(sys.argv[1]).expanduser()
    docs = destino / "documentos"

    # El generador tiene que ser idempotente, y no lo era. Los nombres de archivo
    # llevan la fecha, y la fecha es relativa al día de la corrida: regenerar al día
    # siguiente no reemplazaba nada, dejaba dos generaciones mezcladas en la misma
    # carpeta. Pasó, y se vio porque un compromiso apareció con seis reprogramaciones
    # donde había tres.
    if docs.exists():
        shutil.rmtree(docs)

    proy = corpus.Portafolio(docs / "proyectos")
    prod = corpus.Portafolio(docs / "productos")
    pl_proy = proyectos(proy)
    pl_prod = productos(prod)

    # La disposición rota con el día del mes: así cinco corridas seguidas ejercitan
    # cuatro formas distintas de organizar la misma carpeta, y lo esperado no cambia.
    disp = (sys.argv[2] if len(sys.argv) > 2
            else corpus.DISPOSICIONES[HOY.day % len(corpus.DISPOSICIONES)])
    n1 = proy.volcar(disp)
    n2 = prod.volcar(disp)
    (destino / "estado").mkdir(parents=True, exist_ok=True)
    corpus.escribir_suelto(destino / "LO-QUE-HAY-PLANTADO.md",
                           clave(pl_proy, pl_prod, destino))

    corpus.escribir_suelto(destino / "esperado.json",
                           json.dumps({"generado": HOY.isoformat(), "disposicion": disp,
                                       "esperado": ESPERADO,
                                       "controles": list(CONTROLES)},
                                      ensure_ascii=False, indent=2))
    resumen = {
        "generado": HOY.isoformat(), "disposicion": disp,
        "proyectos": len(proy.casos), "documentos_proyecto": n1,
        "productos": len(prod.casos), "documentos_producto": n2,
        "controles_negativos": ["PRY-105", "PRD-NOMINA"],
    }
    corpus.escribir_suelto(destino / "resumen.json",
                           json.dumps(resumen, ensure_ascii=False, indent=2))

    print(f"{destino}")
    print(f"  documentos/proyectos/   {len(proy.casos)} proyectos · {n1} documentos")
    print(f"  documentos/productos/   {len(prod.casos)} productos · {n2} documentos")
    print(f"  estado/                 vacía, la llenan los agentes")
    print(f"  esperado.json           la clave de respuestas, para el calificador")
    print(f"  disposición             {disp}")
    print(f"  LO-QUE-HAY-PLANTADO.md  la clave de respuestas, fuera del barrido")
    print(f"\ncontroles negativos: PRY-105 y PRD-NOMINA · no deben dar ni un hallazgo")
