# -*- coding: utf-8 -*-
"""Una organización que cambia, día a día, como cambia una de verdad.

    python3 tests/sintetico/simulador.py <carpeta> --dia 1     crea la organización
    python3 tests/sintetico/simulador.py <carpeta> --dia 2     le pasa una semana encima

**Por qué no basta con generar y correr cinco veces.** Una foto repetida prueba
determinismo. Lo que hay que probar es otra cosa: que el agente siga el rastro cuando la
carpeta cambia — que vea lo que cambió y no lo que ya había visto, que note el proyecto
que dejó de producir documentos, que reconozca la promesa que se movió por tercera vez, y
que no vuelva a reportar lo que alguien ya cerró. Nada de eso se puede ver sin que pase el
tiempo.

Cada día equivale a **una semana de trabajo**: minutas nuevas, informes de avance, actas
de recibo que cierran hitos, replanificaciones, facturas, y proyectos que simplemente se
callan. Qué le pasa a cada caso se sortea, pero con una semilla derivada del día, así que
la corrida del día 3 es siempre la misma corrida del día 3.

**La clave de respuestas se deriva de los hechos, no se declara.** Con material que cambia
no puede haber una tabla fija: el simulador lleva los hechos de cada caso —qué hitos hay,
cuáles tienen acta, qué se prometió y cuándo, cuánto se comprometió del presupuesto— y de
esos hechos deduce, con las reglas escritas en el skill y no con el código que se está
midiendo, qué debe encontrar cada agente.

El estado vive en `organizacion.json`, al lado de los documentos, y es lo que permite que
el día 2 sepa qué pasó el día 1.
"""
import argparse
import datetime as dt
import json
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import corpus  # noqa: E402
import organizacion as org  # noqa: E402  las plantillas de documento, que ya existen

HOY = dt.date.today()

# Umbrales, copiados del skill y no importados del código que se mide. Si el código
# cambia un umbral y este no, la prueba lo dice — que es justo lo que tiene que hacer.
UMBRAL = {"silencio_dias": 15, "declaracion_vieja_dias": 30, "comprometido_pct": 90,
          "variacion_costo_pct": 10, "variacion_tiempo_pct": 10, "reprogramaciones": 3,
          "avance_vs_plan_puntos": 25, "avance_vs_plan_hitos_min": 3, "replan_tolerancia_dias": 0, "supuesto_sin_verificar_dias": 30,
          "evidencia_vieja_meses": 12, "sin_decidir_dias": 60, "brecha_declarado_pct": 20}

# Los estados en que alguien ya decidió que el requerimiento se hace. Son los que exigen
# criterio de aceptación y evidencia de que alguien lo pidió.
DECIDIDOS = ("aceptado", "en_construccion", "entregado")

# Las señales que un semáforo verde tiene que explicar. Está copiada de la regla escrita
# en el skill, no importada del código que se mide: si las dos listas se separan, la
# calificación lo dice, y eso es precisamente lo que se quiere saber.
SENALES_DE_EVIDENCIA = (
    "silent", "variance_time", "variance_cost", "milestone_overdue",
    "milestone_met_without_evidence", "progress_vs_plan",
    "commitment_overdue", "commitment_rescheduled",
    "budget_committed", "vendor_deliverable_late", "vendor_invoiced_without_delivery",
    "vendor_invoiced_over_accepted", "rebaseline_unauthorized", "governance_change",
)

AREAS = ["Banca de Personas", "Banca Empresas", "Medios de Pago", "Tecnología",
         "Riesgo y Cumplimiento", "Canales Digitales", "Operaciones", "Tesorería",
         "Banca Hipotecaria", "Banca PyME"]
COMITES = ["Comité de Transformación Digital", "Comité de Arquitectura",
           "Comité de Riesgos", "Comité de Medios de Pago", "Comité de Banca Empresas"]
NOMBRES = ["María Restrepo", "Andrés Lozano", "Diana Molina", "Carlos Peña",
           "Felipe Arango", "Laura Vélez", "Óscar Ramírez", "Paula Céspedes",
           "Gustavo Neira", "Elena Duarte", "Mauricio Pérez", "Camilo Beltrán",
           "Natalia Ospina", "Ricardo Salas", "Jorge Medina", "Liliana Torres",
           "Sandra Gil", "Rubén Cárdenas", "Javier Hoyos", "Beatriz Cuéllar"]
TEMAS_PRY = [
    ("Originación digital", "crédito de consumo"), ("Core de depósitos", "cuenta de ahorros"),
    ("Migración a la nube", None), ("Open Banking", "APIs de datos"),
    ("Débito contactless", "tarjeta débito"), ("Monitoreo SARLAFT", None),
    ("Billetera y QR", "pagos QR"), ("Onboarding PyME", "cuenta PyME"),
    ("Motor de decisión", None), ("Nómina electrónica", "nómina empresarial"),
    ("Portal de proveedores", None), ("Cobranza digital", "recaudos"),
    ("Firma electrónica", None), ("Tarjeta de crédito digital", "tarjeta de crédito"),
    ("Remesas", "remesas familiares"), ("Microseguros", "microseguros"),
    ("Banca abierta fase 2", None), ("Conciliación automática", None),
    ("Canal WhatsApp", None), ("Scoring alternativo", None),
]
TEMAS_PRD = [
    "Pagos QR comercios", "Nómina empresarial", "Crédito hipotecario digital",
    "Cuenta PyME", "Tarjeta de crédito digital", "Recaudos y cobros", "Microseguros",
    "Remesas familiares", "Cuenta de ahorros joven", "Crédito de libre inversión",
    "Datáfono móvil", "Factoring digital", "Seguro de desempleo", "CDT digital",
    "Cuenta de nómina", "Adquirencia comercios", "Billetera empresarial",
    "Crédito rotativo", "Pagos recurrentes", "Corresponsal bancario",
]

# Cuánta documentación tiene cada caso. Es lo que más varía en una organización real:
# el mismo comité aprueba dos proyectos y uno documenta todo y el otro casi nada.
PROFUNDIDAD = {
    "completa": dict(plan=True, recibos=True, contrato=True, minutas=3, informes=2),
    "media": dict(plan=True, recibos=True, contrato=False, minutas=2, informes=1),
    "delgada": dict(plan=True, recibos=False, contrato=False, minutas=1, informes=1),
    "minima": dict(plan=False, recibos=False, contrato=False, minutas=0, informes=1),
}


# Las fases de un proyecto bancario, que es lo que un hito nombra de verdad. «Hito 1» y
# «Hito 2» dejaban la tabla más importante del informe ilegible: un comité no decide sobre
# «Hito 1 · 433 días sin evidencia». Lo dijo el propio agente al leer el material.
FASES = (
    "Diseño funcional aprobado",
    "Ambiente de pruebas certificado",
    "Integración con el core",
    "Piloto con usuarios internos",
    "Salida a producción",
    "Estabilización y cierre",
)

# Lo que un informe de avance dice de verdad. «Avance del periodo» no da materia prima
# para un análisis de causa, y sin ella los comandos de diagnóstico se prueban contra
# nada.
AVANCES = (
    "Se cerró la certificación del ambiente de pruebas",
    "El proveedor entregó el componente de integración, pendiente de aceptación",
    "Dos historias quedaron fuera del alcance del sprint por dependencia con el core",
    "Se reprogramó la salida por ventana de cambio del área de operaciones",
    "El equipo perdió dos semanas por rotación de un desarrollador clave",
    "Se levantó un hallazgo de seguridad en la revisión de arquitectura",
    "La prueba de carga no alcanzó el umbral pactado y se repite",
    "Se recibió la aprobación regulatoria pendiente desde el trimestre anterior",
)

RIESGOS = (
    "Dependencia del calendario de liberaciones del core",
    "Disponibilidad del equipo de seguridad para la revisión final",
    "Concentración del conocimiento en una sola persona",
    "Cambio regulatorio en discusión que puede mover el alcance",
    "El proveedor no ha confirmado la fecha de la última entrega",
)

# Los supuestos que sostienen un producto. Son enunciados que alguien puede verificar o
# no, y esa es la única razón por la que están aquí: un supuesto sin verificar es un
# riesgo que nadie registró.
SUPUESTOS = (
    "El segmento paga por esto",
    "El canal actual soporta el volumen",
    "La regulación vigente lo permite",
    "El proveedor cumple el tiempo pactado",
    "La demanda declarada se sostiene sin campaña",
)

def f(base: dt.date, dias: int) -> str:
    return (base + dt.timedelta(days=dias)).isoformat()


# ══════════════════════════════════════════════════════════════════════════
# El estado de la organización: los hechos de cada caso
# ══════════════════════════════════════════════════════════════════════════

def avance(hitos: list, rnd) -> int:
    """El avance que el gerente declara. No el que su cronograma sostiene.

    Hubo un intento de hacerlo coherente con los hitos cerrados, y era un error de
    diseño: aplanaba el material. De treinta y cuatro proyectos con avance imposible
    quedaban cuatro, y lo que se mide aquí es justamente **la capacidad de encontrarlos**.
    Un proyecto real es caos: el cronograma no se mantiene, el informe se copia del mes
    pasado, y el porcentaje lo pone quien lo reporta. Eso pasa todas las semanas en una
    PMO de verdad, y no hay que quitarlo del material — hay que encontrarlo.

    Lo que sí tiene que estar bien es la clave de respuestas. `progress_vs_plan` es
    aritmética —hitos cerrados contra porcentaje declarado—, así que la incoherencia queda
    medida en vez de escondida: el material puede ser todo el desorden que quiera.

    Va sesgado hacia el optimismo, que es el sesgo que existe: nadie declara menos avance
    del que tiene.
    """
    return rnd.randint(20, 80)


def nuevo_proyecto(rnd, i: int, hoy: dt.date) -> dict:
    tema, producto = TEMAS_PRY[i % len(TEMAS_PRY)]
    prof = rnd.choice(["completa", "completa", "media", "media", "delgada", "minima"])
    arranque = rnd.randint(90, 500)
    duracion = rnd.randint(200, 600)
    presupuesto = rnd.choice([800, 1_200, 2_400, 3_300, 4_200, 6_800, 9_500, 18_000]) * 1_000_000
    n_hitos = {"completa": 5, "media": 4, "delgada": 3, "minima": 2}[prof]
    hitos = []
    for h in range(n_hitos):
        cuando = -arranque + int(duracion * (h + 1) / (n_hitos + 0.5))
        hitos.append({"nombre": FASES[h % len(FASES)], "base": f(hoy, cuando),
                      "vigente": f(hoy, cuando), "cerrado": cuando < 0,
                      "recibo": None})
    return {
        "codigo": f"PRY-{200 + i}", "nombre": tema,
        "carpeta": f"PRY-{200 + i}-" + tema.lower().replace(" ", "-"),
        "profundidad": prof, "area": rnd.choice(AREAS), "comite": rnd.choice(COMITES),
        "patrocinador": rnd.choice(NOMBRES), "gerente": rnd.choice(NOMBRES),
        "producto": producto, "aprobacion": f(hoy, -arranque - 10),
        "inicio": f(hoy, -arranque), "cierre": f(hoy, -arranque + duracion),
        "presupuesto": presupuesto,
        "comprometido": int(presupuesto * rnd.uniform(0.25, 0.75)),
        "ejecutado": int(presupuesto * rnd.uniform(0.15, 0.55)),
        "proyeccion": int(presupuesto * rnd.uniform(0.92, 1.05)),
        "hitos": hitos, "compromisos": [], "lineas_base": 1, "cambios": [],
        "declarado": {"estado": rnd.choice(["verde", "verde", "amarillo"]),
                      "pct": avance(hitos, rnd),
                      "fecha": f(hoy, -rnd.randint(2, 10))},
        "ultimo_doc": f(hoy, -rnd.randint(2, 10)), "silencioso": False,
        "docs": [], "semana": 0,
    }


def nuevo_producto(rnd, i: int, hoy: dt.date) -> dict:
    nombre = TEMAS_PRD[i % len(TEMAS_PRD)]
    prof = rnd.choice(["completa", "media", "media", "delgada"])
    n_req = {"completa": 4, "media": 3, "delgada": 2, "minima": 1}[prof]
    reqs = []
    for r in range(n_req):
        reqs.append({"id": f"REQ-{1000 + i * 10 + r}", "estado": "aceptado",
                     "doliente": rnd.choice(NOMBRES), "criterio": True,
                     "evidencia": True, "desde": f(hoy, -rnd.randint(30, 200)),
                     "proyecto": None})
    return {
        "codigo": f"PRD-{300 + i}", "nombre": nombre, "carpeta": f"PRD-{300 + i}",
        "profundidad": prof, "gerente": rnd.choice(NOMBRES),
        "segmento": rnd.choice(["Personas", "PyME", "Empresas", "Microcomercio",
                                "Base de la pirámide"]),
        "fecha": f(hoy, -rnd.randint(60, 400)),
        "entrevista": f(hoy, -rnd.randint(30, 420)),
        "requerimientos": reqs,
        "supuestos": [{"que": rnd.choice(SUPUESTOS), "desde": f(hoy, -rnd.randint(5, 200)),
                       "verificado": rnd.random() < 0.5}],
        "declarado": rnd.randint(50_000, 300_000),
        "medido": None, "corte": f(hoy, -rnd.randint(2, 25)),
        "ultimo_doc": f(hoy, -rnd.randint(2, 20)), "docs": [], "semana": 0,
    }


# ══════════════════════════════════════════════════════════════════════════
# Una semana de trabajo encima de lo que ya había
# ══════════════════════════════════════════════════════════════════════════

def semana_proyecto(rnd, p: dict, hoy: dt.date, dia: int, todos: bool = False):
    """Lo que le pasa a un proyecto en una semana. Se sortea, con semilla del día."""
    p["semana"] = dia
    eventos = []

    # Uno de cada seis se calla: nadie produce un documento esa semana. Es el caso que
    # ningún tablero muestra, porque no hay nada que mostrar.
    if rnd.random() < 0.17:
        p["silencioso"] = True
        return ["se calló"]
    p["silencioso"] = False

    # Minuta de la semana, con compromisos: unos nuevos, otros que se reprograman.
    if PROFUNDIDAD[p["profundidad"]]["minutas"]:
        abiertos = [c for c in p["compromisos"] if not c["cumplido"]]
        if abiertos and rnd.random() < 0.45:
            c = rnd.choice(abiertos)
            c["fechas"].append(f(hoy, rnd.randint(5, 25)))
            eventos.append(f"reprogramó el compromiso de {c['quien']}")
        if abiertos and rnd.random() < 0.35:
            c = rnd.choice(abiertos)
            c["cumplido"] = True
            eventos.append(f"cerró el compromiso de {c['quien']}")
        if rnd.random() < 0.7:
            quien = rnd.choice(NOMBRES)
            sin_fecha = rnd.random() < 0.15
            p["compromisos"].append({
                "quien": quien, "que": f"Entregar el punto {rnd.randint(1, 40)}",
                "fechas": [None if sin_fecha else f(hoy, rnd.randint(-20, 30))],
                "cumplido": False, "dicho": f(hoy, -rnd.randint(0, 6))})
            eventos.append("compromiso nuevo" + (" sin fecha" if sin_fecha else ""))

    # Actas de recibo: cierran hitos vencidos, si el proyecto documenta recibos.
    if PROFUNDIDAD[p["profundidad"]]["recibos"]:
        vencidos = [h for h in p["hitos"]
                    if h["vigente"] < hoy.isoformat() and not h["recibo"]]
        if vencidos and rnd.random() < 0.5:
            h = rnd.choice(vencidos)
            h["recibo"] = f(hoy, -rnd.randint(0, 6))
            h["cerrado"] = True
            eventos.append(f"recibió «{h['nombre']}»")

    # Replanificación: mueve el último hito, y a veces sin autorizar.
    if rnd.random() < 0.18 and p["hitos"]:
        dias = rnd.randint(20, 120)
        ultimo = p["hitos"][-1]
        ultimo["vigente"] = f(dt.date.fromisoformat(ultimo["vigente"]), dias)
        p["lineas_base"] += 1
        autorizado = rnd.random() < 0.5
        p["cambios"].append({"ref": f"CC-{len(p['cambios']) + 1:02d}", "dias": dias,
                             "autorizado": autorizado, "fecha": f(hoy, -rnd.randint(0, 6))})
        eventos.append(f"replanificó {dias} días" + ("" if autorizado else ", sin autorizar"))

    # El dinero se mueve, y a veces el comprometido se dispara.
    p["ejecutado"] = min(p["presupuesto"], int(p["ejecutado"] * rnd.uniform(1.0, 1.12)))
    p["comprometido"] = min(p["presupuesto"],
                            int(p["comprometido"] * rnd.uniform(1.0, 1.15)))
    if rnd.random() < 0.12:
        p["proyeccion"] = int(p["presupuesto"] * rnd.uniform(1.10, 1.30))
        eventos.append("la proyección se fue por encima")

    # El informe de avance: el gerente declara. A veces no lo escribe, y la declaración
    # envejece — que es una señal distinta de que el proyecto esté callado.
    if rnd.random() < 0.75:
        p["declarado"] = {"estado": rnd.choice(["verde", "verde", "amarillo", "rojo"]),
                          # El avance declarado sube, porque nadie reporta retroceso.
                          "pct": min(99, p["declarado"]["pct"] + rnd.randint(1, 9)),
                          "fecha": f(hoy, -rnd.randint(0, 5))}
        eventos.append("informe de avance")
    p["ultimo_doc"] = f(hoy, -rnd.randint(0, 5))
    return eventos


def semana_producto(rnd, x: dict, hoy: dt.date, dia: int, todos: bool = False):
    x["semana"] = dia
    eventos = []
    # En `todos`, ningún producto se queda quieto: el silencio de una semana es realista
    # y también lo es una semana en que todo se mueve, y esa segunda es la que estresa el
    # índice de documentos —si nada quedó sin cambiar, hay que releerlo todo— y el diff.
    if not todos and rnd.random() < 0.2:
        return ["sin movimiento"]
    if rnd.random() < 0.5:
        r = rnd.choice(x["requerimientos"])
        if rnd.random() < 0.3:
            r["estado"] = "propuesto"
            r["desde"] = f(hoy, -rnd.randint(70, 200))
            eventos.append(f"{r['id']} volvió a propuesto")
        if rnd.random() < 0.2:
            r["doliente"] = None
            eventos.append(f"{r['id']} se quedó sin doliente")
        if rnd.random() < 0.2:
            r["evidencia"] = False
            eventos.append(f"{r['id']} perdió su evidencia")
    if rnd.random() < 0.35:
        n = len(x["requerimientos"])
        x["requerimientos"].append({
            "id": f"REQ-{2000 + n + dia * 7}", "estado": "aceptado",
            "doliente": rnd.choice(NOMBRES), "criterio": rnd.random() < 0.8,
            "evidencia": rnd.random() < 0.7,
            "desde": f(hoy, -rnd.randint(1, 20)), "proyecto": None})
        eventos.append("requerimiento nuevo")
    if rnd.random() < 0.3:
        x["medido"] = int(x["declarado"] * rnd.uniform(0.6, 1.05))
        x["corte"] = f(hoy, -rnd.randint(0, 10))
        eventos.append("tablero actualizado")
    x["ultimo_doc"] = f(hoy, -rnd.randint(0, 6))
    return eventos


# ══════════════════════════════════════════════════════════════════════════
# Lo que cada agente debe encontrar, deducido de los hechos
# ══════════════════════════════════════════════════════════════════════════

def piso_proyecto(rnd, p: dict, hoy: dt.date) -> list:
    """Lo mínimo que le pasa a un proyecto en una semana en que algo pasa.

    Un informe de avance, que es lo que un gerente escribe sí o sí, y un compromiso
    nuevo de la reunión. No se inventa nada distinto de lo que la semana normal ya hace:
    se garantiza que ocurra.
    """
    p["declarado"] = {"estado": rnd.choice(["verde", "verde", "amarillo", "rojo"]),
                      "pct": min(99, p["declarado"]["pct"] + rnd.randint(1, 9)),
                      "fecha": f(hoy, -rnd.randint(0, 5))}
    p["ultimo_doc"] = f(hoy, -rnd.randint(0, 5))
    p["silencioso"] = False
    eventos = ["informe de avance"]
    if PROFUNDIDAD[p["profundidad"]]["minutas"]:
        p["compromisos"].append({
            "quien": rnd.choice(NOMBRES), "que": f"Entregar el punto {rnd.randint(1, 40)}",
            "fechas": [f(hoy, rnd.randint(-20, 30))], "cumplido": False,
            "dicho": f(hoy, -rnd.randint(0, 6))})
        eventos.append("compromiso nuevo")
    return eventos


def piso_producto(rnd, x: dict, hoy: dt.date) -> list:
    """Lo mínimo que le pasa a un producto: el comité revisa y queda un requerimiento más."""
    n = len(x["requerimientos"])
    x["requerimientos"].append({
        "id": f"REQ-{3000 + n + x['semana'] * 11}", "estado": "aceptado",
        "doliente": rnd.choice(NOMBRES), "criterio": rnd.random() < 0.8,
        "evidencia": rnd.random() < 0.7,
        "desde": f(hoy, -rnd.randint(1, 20)), "proyecto": None})
    x["ultimo_doc"] = f(hoy, -rnd.randint(0, 6))
    return ["requerimiento nuevo"]


def esperado_proyecto(p: dict, hoy: dt.date) -> list:
    """Las señales que los hechos de este proyecto obligan.

    Se deduce de las reglas escritas en `portfolio-health`, no del código que se mide.
    Si el código cambia una regla y esto no, la corrida lo reporta — y esa es la razón
    de escribirlo dos veces.
    """
    s, h = [], hoy.isoformat()
    # Lo esperado se deriva de **lo que quedó escrito**, no de lo que el simulador sabe.
    # Un proyecto de profundidad mínima no tiene cronograma: sus hitos existen en el
    # estado y en ningún documento, y un agente que los reportara estaría inventando.
    # Esperar que los encuentre es medir contra una vara torcida.
    hitos = p["hitos"] if PROFUNDIDAD[p["profundidad"]]["plan"] else []
    for hi in hitos:
        vencido = hi["vigente"] < h
        if vencido and not hi["recibo"]:
            s.append("milestone_met_without_evidence" if hi["cerrado"]
                     else "milestone_overdue")
    for c in p["compromisos"]:
        if c["cumplido"]:
            continue
        if c["fechas"][-1] is None:
            s.append("commitment_undated")
        elif c["fechas"][-1] < h:
            s.append("commitment_overdue")
        # Reprogramaciones, no fechas: tres fechas son dos reprogramaciones. La primera
        # es el compromiso.
        if len([x for x in c["fechas"] if x]) - 1 >= UMBRAL["reprogramaciones"]:
            s.append("commitment_rescheduled")
    if p["presupuesto"] and p["comprometido"] / p["presupuesto"] * 100 >= UMBRAL["comprometido_pct"]:
        s.append("budget_committed")
    if p["presupuesto"]:
        exceso = (p["proyeccion"] / p["presupuesto"] - 1) * 100
        if exceso >= UMBRAL["variacion_costo_pct"]:
            s.append("variance_cost")
    base = dt.date.fromisoformat(p["hitos"][0]["base"]) if p["hitos"] else None
    fin_base = dt.date.fromisoformat(p["hitos"][-1]["base"]) if p["hitos"] else None
    fin_vig = dt.date.fromisoformat(p["hitos"][-1]["vigente"]) if p["hitos"] else None
    ini = dt.date.fromisoformat(p["inicio"])
    if fin_base and fin_vig and fin_base > ini:
        atraso = (fin_vig - fin_base).days
        span = (fin_base - ini).days
        if span > 0 and atraso / span * 100 >= UMBRAL["variacion_tiempo_pct"]:
            s.append("variance_time")
    # Las líneas base que el material deja escritas: la versión 1 el día de la
    # aprobación, y la versión vigente el día del último informe. Nada más existe en
    # papel, y contra eso se mide.
    # El avance declarado contra el que sostiene el cronograma. El material es todo el
    # desorden que quiera: mientras la clave lo calcule, queda medido.
    if len(hitos) >= UMBRAL["avance_vs_plan_hitos_min"]:
        sostiene = round(100 * sum(1 for h in hitos if h["cerrado"]) / len(hitos))
        if abs(sostiene - p["declarado"]["pct"]) >= UMBRAL["avance_vs_plan_puntos"]:
            s.append("progress_vs_plan")

    lineas = []
    if PROFUNDIDAD[p["profundidad"]]["plan"]:
        lineas.append(p["aprobacion"])
        if p["lineas_base"] > 1:
            lineas.append(p["declarado"]["fecha"])

    # Los días que la línea base se movió salen de restar la versión vigente de la
    # original —no de sumar las solicitudes—, así que sin cronograma no hay nada que
    # restar y la señal no puede sonar. Es la diferencia entre lo que el simulador sabe
    # y lo que el proyecto documenta.
    if len(lineas) > 1:
        movido = sum(c["dias"] for c in p["cambios"])
        autorizado = sum(c["dias"] for c in p["cambios"] if c["autorizado"])
        if movido - autorizado > UMBRAL["replan_tolerancia_dias"]:
            s.append("rebaseline_unauthorized")

    # Un cambio autorizado con impacto en tiempo y ninguna línea base aprobada desde
    # que se pidió: se dijo sí y el plan nunca se rehízo.
    for c in p["cambios"]:
        if c["autorizado"] and c["dias"] and not any(b >= c["fecha"] for b in lineas[1:]):
            s.append("change_without_baseline")
    dias_silencio = (hoy - dt.date.fromisoformat(p["ultimo_doc"])).days
    if dias_silencio >= UMBRAL["silencio_dias"]:
        s.append("silent")
    dias_decl = (hoy - dt.date.fromisoformat(p["declarado"]["fecha"])).days
    if dias_decl >= UMBRAL["declaracion_vieja_dias"]:
        s.append("declaration_stale")
    if p["declarado"]["estado"] == "verde" and any(x in SENALES_DE_EVIDENCIA for x in s):
        s.append("declared_vs_evidence")
    return sorted(s)


def esperado_producto(x: dict, hoy: dt.date) -> list:
    s, h = [], hoy.isoformat()
    for r in x["requerimientos"]:
        if not r["doliente"]:
            s.append("requirement_without_owner")
        # El criterio de aceptación se le exige a lo que ya se decidió hacer. A un
        # requerimiento propuesto todavía no: falta la decisión, no el criterio.
        if r["estado"] in DECIDIDOS and not r["criterio"]:
            s.append("requirement_without_acceptance")
        if r["estado"] == "aceptado" and not r["evidencia"]:
            s.append("requirement_accepted_without_evidence")
        if r["estado"] == "propuesto":
            dias = (hoy - dt.date.fromisoformat(r["desde"])).days
            if dias >= UMBRAL["sin_decidir_dias"]:
                s.append("requirement_undecided")
        if r["estado"] == "aceptado" and not r["proyecto"]:
            s.append("requirement_untraced")
    for a in x["supuestos"]:
        if (not a["verificado"] and (hoy - dt.date.fromisoformat(a["desde"])).days
                >= UMBRAL["supuesto_sin_verificar_dias"]):
            s.append("assumption_unverified")
    # La evidencia envejece por requerimiento, y solo se le puede envejecer a quien
    # tiene alguna. Un requerimiento sin una sola cita no produce evidencia vieja:
    # produce el hallazgo anterior, que es peor y lo sustituye.
    ent = dt.date.fromisoformat(x["entrevista"])
    # Meses completos de calendario, no días / 30: del 29 de septiembre al 28 del
    # septiembre siguiente hay once meses y treinta días, y eso no es un año.
    meses = ((hoy.year - ent.year) * 12 + (hoy.month - ent.month)
             - (hoy.day < ent.day))
    if meses >= UMBRAL["evidencia_vieja_meses"]:
        s += ["evidence_stale"] * len([r for r in x["requerimientos"] if r["evidencia"]])
    if x["medido"] and x["declarado"]:
        if (abs(x["declarado"] - x["medido"]) / x["declarado"] * 100
                >= UMBRAL["brecha_declarado_pct"]):
            s.append("claim_vs_metric")
    return sorted(s)


# ══════════════════════════════════════════════════════════════════════════

def escribir(estado: dict, destino: Path, hoy: dt.date, disp: str) -> tuple:
    docs = destino / "documentos"
    proy = corpus.Portafolio(docs / "proyectos")
    prod = corpus.Portafolio(docs / "productos")

    for p in estado["proyectos"]:
        c = proy.caso(p["codigo"], "proyecto", p["carpeta"])
        d = dict(codigo=p["codigo"], nombre=p["nombre"], area=p["area"],
                 patrocinador=p["patrocinador"], gerente=p["gerente"],
                 comite=p["comite"], producto=p["producto"] or "No aplica",
                 aprobacion=p["aprobacion"], inicio=p["inicio"], cierre=p["cierre"],
                 presupuesto=p["presupuesto"], comprometido=p["comprometido"],
                 ejecutado=p["ejecutado"], proyeccion=p["proyeccion"],
                 objetivo=f"Entregar {p['nombre'].lower()} para {p['area']}.",
                 alcance=[f"Componente {i}" for i in range(1, 4)],
                 fuera=["Lo que otro proyecto cubre"],
                 exito=f"{p['nombre']} en producción y medido.",
                 riesgos=rnd.sample(RIESGOS, rnd.randint(1, 2)))
        c.gobierno(p["aprobacion"], "acta-constitucion.md", org.acta(d))
        if PROFUNDIDAD[p["profundidad"]]["plan"]:
            # La versión 1 es la línea base original: la fecha comprometida y la vigente
            # son la misma, porque cuando se aprobó nada se había movido todavía. Solo la
            # versión actual muestra las dos distintas. Escribir las mismas filas en
            # todas las versiones dejaba la replanificación sin rastro documental: el
            # proyecto se movía noventa días y ningún documento lo decía, así que
            # `variance_time` y `rebaseline_unauthorized` no podían sonar nunca.
            original = [(h["nombre"], h["base"], h["base"],
                         "cerrado" if h["cerrado"] else "en curso") for h in p["hitos"]]
            c.plan(p["aprobacion"], "cronograma-v1.csv", org.cronograma(d, 1, original))
            if p["lineas_base"] > 1:
                vigente = [(h["nombre"], h["base"], h["vigente"],
                            "cerrado" if h["cerrado"] else "en curso") for h in p["hitos"]]
                c.plan(p["declarado"]["fecha"], f"cronograma-v{p['lineas_base']}.csv",
                       org.cronograma(d, p["lineas_base"], vigente))
        for h in p["hitos"]:
            if h["recibo"]:
                c.seguimiento(h["recibo"], f"acta-recibo-{h['nombre'].lower().replace(' ', '-')}.md",
                              org.recibo(d, h["recibo"], h["nombre"], p["gerente"], ""))
        c.seguimiento(p["declarado"]["fecha"], "informe-avance.md", org.informe(
            d, p["declarado"]["estado"].capitalize(), p["declarado"]["fecha"],
            p["declarado"]["pct"],
            rnd.sample(AVANCES, rnd.randint(1, 3))))
        for ch in p["cambios"]:
            c.seguimiento(ch["fecha"], f"solicitud-cambio-{ch['ref'].lower()}.md",
                          org.cambio(d, ch["fecha"], ch["ref"], "Ampliación de alcance",
                                     ch["dias"], ch["dias"] * 2_000_000,
                                     "Autorizada por el comité." if ch["autorizado"]
                                     else "Pendiente de presentación al comité."))
        abiertos = [x for x in p["compromisos"] if not x["cumplido"]]
        if abiertos:
            ult = max(x["dicho"] for x in abiertos)
            c.reunion(ult, "comite-semanal.md", org.minuta(
                d, ult, [p["gerente"], p["patrocinador"]], ["Avance", "Compromisos"],
                [{"quien": x["quien"], "que": x["que"],
                  "para": x["fechas"][-1] or "por definir"} for x in abiertos]))

    for x in estado["productos"]:
        c = prod.caso(x["codigo"], "producto", x["carpeta"])
        d = dict(codigo=x["codigo"], nombre=x["nombre"], gerente=x["gerente"],
                 segmento=x["segmento"], fecha=x["fecha"], fecha_caso=x["fecha"],
                 corte_tablero=x["corte"], ronda=f"Ronda · {x['entrevista']}",
                 comite_fecha=x["ultimo_doc"],
                 problema=f"El segmento {x['segmento']} no tiene {x['nombre'].lower()}.",
                 propuesta=["Propuesta principal"],
                 # La verificación viaja al documento. Si el material no dice si el
                 # supuesto se verificó, el lector no tiene más opción que asumir que no,
                 # y `assumption_unverified` se dispara en los sesenta y cinco productos:
                 # una señal que siempre suena no distingue nada.
                 supuestos=[{"que": a["que"], "desde": a["desde"],
                             "verificado": a["verificado"]} for a in x["supuestos"]],
                 proyectos=[r["proyecto"] for r in x["requerimientos"] if r["proyecto"]]
                 or ["Ninguno declarado"],
                 cifras=[dict(clave="volumen_mensual", declarado=x["declarado"],
                              medido=x["medido"], fuente=f"Caso de negocio, {x['fecha']}",
                              corte=x["corte"])],
                 retorno="Retorno esperado en 24 meses.",
                 entrevistas=[dict(quien="Cliente entrevistado", cuando=x["entrevista"],
                                   dijo="Lo necesito y hoy no lo tengo.",
                                   tema="Necesidad principal")],
                 asistentes=[x["gerente"]],
                 requerimientos=[dict(id=r["id"], que=f"Requerimiento {r['id']}",
                                      doliente=r["doliente"] or "sin asignar",
                                      criterio="se verifica en producción" if r["criterio"] else None,
                                      evidencia="Cliente entrevistado" if r["evidencia"] else None,
                                      estado=r["estado"], desde=r["desde"])
                                for r in x["requerimientos"]],
                 decisiones=["Se mantiene el plan"])
        c.definicion(x["fecha"], "definicion-producto.md", org.definicion_producto(d))
        c.definicion(x["fecha"], "caso-de-negocio.md", org.caso_negocio(d))
        c.descubrimiento(x["entrevista"], "entrevistas.md", org.entrevistas(d))
        if x["medido"]:
            c.metrica(x["corte"], "tablero-metricas.md", org.tablero(d))
        c.decision(x["ultimo_doc"], "comite-producto.md", org.comite_producto(d))

    if docs.exists():
        import shutil
        shutil.rmtree(docs)
    return proy.volcar(disp), prod.volcar(disp)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("destino")
    ap.add_argument("--dia", type=int, required=True, help="1 crea; 2..5 pasan una semana")
    ap.add_argument("--proyectos", type=int, default=50)
    ap.add_argument("--productos", type=int, default=65)
    ap.add_argument("--disposicion", default=None)
    ap.add_argument("--todos", action="store_true",
                    help="que se mueva cada proyecto y cada producto, sin excepción")
    a = ap.parse_args()

    destino = Path(a.destino).expanduser()
    destino.mkdir(parents=True, exist_ok=True)
    banco = destino / "organizacion.json"
    rnd = random.Random(20260928 + a.dia * 7919)
    disp = a.disposicion or corpus.DISPOSICIONES[(a.dia - 1) % len(corpus.DISPOSICIONES)]

    if a.dia == 1 or not banco.exists():
        estado = {"dia": 1, "creada": HOY.isoformat(),
                  "proyectos": [nuevo_proyecto(rnd, i, HOY) for i in range(a.proyectos)],
                  "productos": [nuevo_producto(rnd, i, HOY) for i in range(a.productos)]}
        bitacora = [f"día 1 · organización creada: {a.proyectos} proyectos, "
                    f"{a.productos} productos"]
    else:
        estado = json.loads(banco.read_text(encoding="utf-8"))
        estado["dia"] = a.dia
        bitacora = []
        for p in estado["proyectos"]:
            movidos = semana_proyecto(rnd, p, HOY, a.dia, a.todos)
            if a.todos and not [e for e in movidos if e != "sin movimiento"]:
                movidos = piso_proyecto(rnd, p, HOY)
            for e in movidos:
                bitacora.append(f"{p['codigo']} · {e}")
        for x in estado["productos"]:
            movidos = semana_producto(rnd, x, HOY, a.dia, a.todos)
            if a.todos and not [e for e in movidos if e != "sin movimiento"]:
                movidos = piso_producto(rnd, x, HOY)
            for e in movidos:
                bitacora.append(f"{x['codigo']} · {e}")

    n1, n2 = escribir(estado, destino, HOY, disp)
    banco.write_text(json.dumps(estado, ensure_ascii=False, indent=1), encoding="utf-8")

    esperado = {p["codigo"]: esperado_proyecto(p, HOY) for p in estado["proyectos"]}
    esperado.update({x["codigo"]: esperado_producto(x, HOY) for x in estado["productos"]})
    corpus.escribir_suelto(destino / "esperado.json", json.dumps(
        {"generado": HOY.isoformat(), "dia": a.dia, "disposicion": disp,
         # `solo_modelo` queda para lo que el script no puede calcular y el agente sí
         # tiene que encontrar. Hoy está vacío a propósito: `progress_vs_plan` se pasó a
         # aritmética, y las dos que siguen siendo del modelo —`contradiction` y
         # `governance_change`— todavía no tienen material plantado aquí. Están en el
         # corpus de dieciocho casos, no en esta organización de ciento quince.
         "esperado": esperado, "controles": [], "solo_modelo": {}},
        ensure_ascii=False, indent=1))
    corpus.escribir_suelto(destino / f"bitacora-dia-{a.dia}.md",
                           f"# Día {a.dia} · qué pasó\n\n"
                           f"Disposición **{disp}**. {n1 + n2} documentos.\n\n"
                           + "\n".join(f"- {b}" for b in bitacora))

    total = sum(len(v) for v in esperado.values())
    print(f"día {a.dia} · disposición {disp}")
    print(f"  {len(estado['proyectos'])} proyectos · {n1} documentos")
    print(f"  {len(estado['productos'])} productos · {n2} documentos")
    print(f"  {total} hallazgos esperados · {len(bitacora)} cambios en la bitácora")
