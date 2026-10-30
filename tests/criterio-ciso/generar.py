#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El material de prueba de la familia CISO: una entidad de banca, una de retail, una de salud y una
de tecnología, y dos entidades de control.

    python3 tests/criterio-ciso/generar.py          escribe tests/criterio-ciso/material/

Cada entidad trae su carpeta de seguridad al 15 de octubre de 2026: las dos políticas —la de gestión
de vulnerabilidades y la de respuesta a incidentes—, la declaración de aplicabilidad, la tabla de
sistemas, el registro de terceros, el inventario de activos, la matriz de notificaciones y el
calendario de continuidad; la evidencia de cada control, las revisiones de acceso y las evaluaciones
de terceros; el registro de riesgos; tres exportaciones del escáner —el 20 de agosto, el 20 de
septiembre y el 10 de octubre— con el catálogo KEV; el seguimiento de la remediación y las
excepciones; y los incidentes del trimestre con sus notificaciones, sus revisiones y las pruebas de
continuidad. Trae también lo que nunca se abre: una llave, un archivo de credenciales y un respaldo
comprimido, que el motor tiene que excluir sin levantar nada.

Las exportaciones del escáner se reparten: cabeceras en inglés en CSV, en español en Excel, unas que
no se reconocen y piden su mapeo en `scanner.columns`, y otras que traen el puntaje CVSS y no la
severidad, que sale de la escala del CVSS v4.0 (F-05).

**La clave la escribe este archivo, no el motor.** Cada defecto se siembra a propósito y su señal
esperada queda escrita en `clave.json`, junto con lo que el agente tendría que extraer de los
documentos escritos —la evidencia de cada control, las revisiones, las evaluaciones, cada incidente
con sus notificaciones, sus revisiones y cada prueba— y los plazos que el setup toma de cada política.
El motor no la ve; `evaluar.py` compara lo que el motor levanta contra ella, y una señal de más cuenta
igual que una de menos.

**Cada entidad de industria siembra veinticinco señales**, las dieciséis de la familia y nueve que se
repiten: cien en total, más de las 73 que pide un piso del 95 % sin fallas (decisión 0020).

**Las entidades de control no tienen ningún defecto**, y sí los casos que se parecen a uno: un control
que no aplica sin evidencia, uno en implementación sin evidencia, una evidencia mensual que vence
mañana, un tercero no crítico sin evaluar, una aceptación de riesgo que vence hoy, una vulnerabilidad
fuera de plazo con su excepción vigente, una del catálogo KEV cuya fecha todavía no llega, un cierre
que el escaneo posterior prueba, un activo fuera de alcance sin escanear, una notificación hecha justo
en el plazo y una prueba de restauración con observaciones. Todo es determinista: el mismo material
cada vez, byte a byte. Los nombres, las normas, las cifras y los CVE son sintéticos: los CVE llevan el
año 2099 para que ninguno se confunda con una vulnerabilidad real.
"""
from __future__ import annotations

import datetime as dt
import json
import re
import shutil
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent.parent
sys.path.insert(0, str(RAIZ / "plugins" / "criterio-security" / "scripts"))
import seguridad as S  # noqa: E402
sys.path.insert(0, str(RAIZ / "tests" / "sintetico"))
import formatos as FMT  # noqa: E402  (Word, Excel y PDF sin dependencias y con fecha fija, los mismos de las demás familias)

SALIDA = AQUI / "material"
HOY, PERIODO = dt.date(2026, 10, 15), "2026-10"
ESCANEOS = ("2026-08-20", "2026-09-20", "2026-10-10")


def slug(t: str) -> str:
    return S.norm(t).replace("_", "-")


def csv_(ruta: Path, filas: list[list]) -> None:
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text("\n".join(";".join(str(x) for x in f) for f in filas) + "\n", encoding="utf-8")


def tabla(ruta: Path, filas: list[list], excel: bool) -> str:
    if excel:
        ruta = ruta.with_suffix(".xlsx")
        ruta.parent.mkdir(parents=True, exist_ok=True)
        FMT.a_xlsx_tipado(filas, ruta, "Hoja1")
    else:
        csv_(ruta.with_suffix(".csv"), filas)
        ruta = ruta.with_suffix(".csv")
    return ruta.name


def documento(ruta: Path, md: str) -> str:
    """Un documento escrito en el formato que dice su extensión: .md, .docx o .pdf."""
    ruta.parent.mkdir(parents=True, exist_ok=True)
    if ruta.suffix == ".docx":
        FMT.a_docx(md, ruta)
    elif ruta.suffix == ".pdf":
        FMT.a_pdf(md, ruta)
    else:
        ruta.write_text(md, encoding="utf-8")
    return ruta.name


# ================================================================ las entidades

ENTIDADES = [
    {"carpeta": "banca-co", "industria": "banca", "pais": "CO", "id": "901555123", "nombre": "Banco Cordillera Sintético", "moneda": "COP",
     "sla": {"critica": 15, "alta": 30, "media": 60, "baja": 120}, "contencion": {"critica": 4, "alta": 24, "media": 72, "baja": 168}, "revision": 10,
     "escaner": "ingles-csv", "excel": True, "pref": "bco", "sistema": "Core bancario",
     "supervisor": "Superintendencia Financiera", "datos": "Autoridad de protección de datos", "siembra": True},
    {"carpeta": "retail-mx", "industria": "retail", "pais": "MX", "id": "TBA110315K21", "nombre": "Tiendas del Bajío Sintéticas", "moneda": "MXN",
     "sla": {"critica": 15, "alta": 30, "media": 90, "baja": 180}, "contencion": {"critica": 6, "alta": 24, "media": 72, "baja": 168}, "revision": 15,
     "escaner": "espanol-xlsx", "excel": False, "pref": "tda", "sistema": "ERP de tiendas",
     "supervisor": "Comisión supervisora", "datos": "Autoridad de protección de datos", "siembra": True},
    {"carpeta": "salud-pe", "industria": "salud", "pais": "PE", "id": "20512345678", "nombre": "Clínica del Pacífico Sintética", "moneda": "PEN",
     "sla": {"critica": 10, "alta": 30, "media": 90, "baja": 180}, "contencion": {"critica": 4, "alta": 12, "media": 48, "baja": 120}, "revision": 20,
     "escaner": "mapeo-csv", "excel": True, "pref": "cli", "sistema": "Historia clínica",
     "supervisor": "Superintendencia de salud", "datos": "Autoridad de protección de datos", "siembra": True},
    {"carpeta": "tecnologia-cl", "industria": "tecnologia", "pais": "CL", "id": "76543210-K", "nombre": "Nube Austral Software Sintética", "moneda": "CLP",
     "sla": {"critica": 7, "alta": 30, "media": 60, "baja": 120}, "contencion": {"critica": 2, "alta": 8, "media": 48, "baja": 120}, "revision": 14,
     "escaner": "puntaje-csv", "excel": False, "pref": "nub", "sistema": "Plataforma de clientes",
     "supervisor": "Agencia de ciberseguridad", "datos": "Autoridad de protección de datos", "siembra": True},
    {"carpeta": "control-co", "industria": "banca", "pais": "CO", "id": "900777888", "nombre": "Cooperativa Control Sintética", "moneda": "COP",
     "sla": {"critica": 15, "alta": 30, "media": 90, "baja": 180}, "contencion": {"critica": 4, "alta": 24, "media": 72, "baja": 168}, "revision": 15,
     "escaner": "ingles-csv", "excel": False, "pref": "ctl", "sistema": "Core de la cooperativa",
     "supervisor": "Superintendencia Financiera", "datos": "Autoridad de protección de datos", "siembra": False},
    {"carpeta": "control-mx", "industria": "retail", "pais": "MX", "id": "CCM090101AB3", "nombre": "Comercial Control Sintética", "moneda": "MXN",
     "sla": {"critica": 15, "alta": 30, "media": 90, "baja": 180}, "contencion": {"critica": 6, "alta": 24, "media": 72, "baja": 168}, "revision": 15,
     "escaner": "espanol-xlsx", "excel": True, "pref": "ccm", "sistema": "ERP comercial",
     "supervisor": "Comisión supervisora", "datos": "Autoridad de protección de datos", "siembra": False},
]

# ================================================================ Alexis

CONTROLES = [  # control, nombre como lo escribe la organización, periodicidad, fecha de la evidencia sana
    ("A.5.1", "Políticas de seguridad de la información", "anual", "2026-02-20"),
    ("A.5.9", "Inventario de información y otros activos", "semestral", "2026-07-31"),
    ("A.5.15", "Control de acceso", "trimestral", "2026-09-30"),
    ("A.5.18", "Derechos de acceso", "trimestral", "2026-08-15"),
    ("A.5.19", "Seguridad en las relaciones con proveedores", "anual", "2026-03-15"),
    ("A.5.24", "Preparación para la gestión de incidentes", "anual", "2026-01-30"),
    ("A.5.30", "Preparación de las TIC para la continuidad", "anual", "2026-04-10"),
    ("A.8.7", "Protección contra el malware", "mensual", "2026-09-30"),
    ("A.8.8", "Gestión de las vulnerabilidades técnicas", "mensual", "2026-09-30"),
    ("A.8.13", "Copias de seguridad de la información", "mensual", "2026-09-30"),
    ("A.8.15", "Registro de eventos", "mensual", "2026-09-30"),
    ("A.8.16", "Actividades de seguimiento", "mensual", "2026-09-15"),      # vence el 16 de octubre: mañana, no hoy
    ("A.8.24", "Uso de la criptografía", "anual", "2026-05-20"),
]
RESPONSABLES = ("Jefe de seguridad de la información", "Gerente de tecnología", "Oficial de cumplimiento", "Jefe de infraestructura")


def alexis(e: dict, docs: Path) -> tuple[dict, list]:
    siembra = e["siembra"]
    esperado, ficha = [], {"evidence": [], "access_reviews": [], "third_party_assessments": [], "reviewed": [], "questions": []}
    soa = [["Control", "Nombre", "Aplicable", "Estado", "Responsable", "Periodicidad", "Justificación"]]
    for i, (c, n, per, f) in enumerate(CONTROLES):
        resp = RESPONSABLES[i % len(RESPONSABLES)]
        cid = S.control_id(c)
        if siembra and c == "A.8.24":                                         # sin responsable
            resp = ""
            esperado.append(("soa_control_unassigned", f"responsable:{cid}"))
        soa.append([c, n, "Sí", "Implementado", resp, per, ""])
        if siembra and c == "A.8.15":                                         # sin ninguna evidencia
            esperado.append(("control_without_evidence", f"evidencia:{cid}"))
            continue
        if siembra and c == "A.5.18":                                         # trimestral, la última de junio
            f = "2026-06-30"
            esperado.append(("control_evidence_stale", f"vigencia:{cid}"))
        ext = (".pdf", ".md", ".docx")[i % 3]
        nombre = documento(docs / "10-controles" / f"{c}_{slug(n)}_{f[:7]}{ext}",
                           f"# {n}\n\n**Control:** {c} · **Periodo que cubre:** hasta el {f}\n\n"
                           f"Evidencia de que el control operó: {('informe', 'registro', 'acta')[i % 3]} del periodo, revisado por {resp or 'el área de seguridad'}.\n\n"
                           f"Fecha de corte de la evidencia: {f}.\n")
        ficha["evidence"].append({"control": c, "date": f, "source": f"10-controles/{nombre}"})
    soa.append(["A.7.4", "Seguimiento de la seguridad física", "No", "", "", "", "Los servidores están en la nube del proveedor"])
    soa.append(["A.8.28", "Codificación segura", "Sí", "En implementación", "Gerente de tecnología", "anual", ""])
    # Un borrador en la carpeta de controles: no es evidencia, y el agente lo deja en lo revisado.
    nombre = documento(docs / "10-controles" / "A.8.28_borrador-guia-codificacion.docx",
                       "# Guía de codificación segura\n\nBORRADOR · sin aprobar · versión de trabajo del equipo de desarrollo.\n")
    ficha["reviewed"].append({"source": f"10-controles/{nombre}"})
    tabla(docs / "00-referencia" / "declaracion-aplicabilidad", soa, e["excel"])

    # Las revisiones de acceso de cada sistema.
    sistemas = [(e["sistema"], 90, "2026-08-10"), ("Correo corporativo", 180, "2026-05-02"),
                ("Directorio activo", 90, "2026-07-20"), ("Portal de clientes", 180, "2026-06-01")]
    filas = [["sistema", "revision_dias", "criticidad", "responsable"]]
    for s, d, f in sistemas:
        filas.append([s, d, "alta" if d == 90 else "media", "Jefe de seguridad de la información"])
        if siembra and s == "Directorio activo":
            f = "2026-06-30"                                                  # tocaba el 28 de septiembre
            esperado.append(("access_review_overdue", f"accesos:{S.norm(s)}"))
        if siembra and s == "Portal de clientes":
            esperado.append(("access_review_overdue", f"accesos:{S.norm(s)}"))
            continue
        nombre = documento(docs / "20-accesos" / f"revision-accesos_{slug(s)}_{f}.pdf",
                           f"# Revisión de accesos · {s}\n\nFecha de la revisión: {f}\n\nRevisó: Jefe de seguridad de la información\n\n"
                           f"Se revisaron las cuentas activas del sistema contra la nómina vigente; se retiraron las cuentas de personas que salieron.\n")
        ficha["access_reviews"].append({"system": s, "date": f, "reviewer": "Jefe de seguridad de la información", "source": f"20-accesos/{nombre}"})
    csv_(docs / "00-referencia" / "sistemas.csv", filas)

    # Los terceros críticos.
    terceros = [("Nube Andina Servicios", "infraestructura en la nube", "sí", "2026-02-10", "sin hallazgos"),
                ("Pasarela de Pagos Sintética", "procesamiento de pagos", "sí", "2025-11-20", "con observaciones"),
                ("Mesa de Ayuda Externa", "soporte a usuarios", "sí", "2026-04-01", "sin hallazgos"),
                ("Papelería del Centro", "insumos de oficina", "no", None, None)]
    if siembra:
        terceros.append(("Centro de Datos Alterno", "sitio de recuperación", "sí", None, None))
    filas = [["tercero", "servicio", "critico", "evaluacion_dias"]]
    for t, serv, crit, f, res in terceros:
        filas.append([t, serv, crit, 365])
        if siembra and t == "Mesa de Ayuda Externa":
            f = "2025-09-30"
            esperado.append(("third_party_assessment_overdue", f"tercero:{S.norm(t)}"))
        if siembra and t == "Centro de Datos Alterno":
            esperado.append(("third_party_assessment_overdue", f"tercero:{S.norm(t)}"))
        if not f:
            continue
        nombre = documento(docs / "30-terceros" / f"evaluacion_{slug(t)}_{f}.pdf",
                           f"# Evaluación de seguridad · {t}\n\nFecha de la evaluación: {f}\n\nServicio: {serv}\n\nResultado: {res}.\n")
        ficha["third_party_assessments"].append({"third_party": t, "date": f, "result": res, "source": f"30-terceros/{nombre}"})
    csv_(docs / "00-referencia" / "terceros.csv", filas)

    # El registro de riesgos.
    riesgos = [["riesgo", "descripcion", "decision", "aceptado_por", "revision"],
               ["R-01", "Sistema heredado sin soporte del fabricante", "Aceptar", "Gerente general", "2026-12-31"],
               ["R-02", "Correo sin doble factor para proveedores", "Mitigar", "", "2026-12-31"],
               ["R-03", "Respaldo fuera de sitio a más de 24 horas", "Aceptar", "Comité de riesgos", "2026-09-30" if siembra else "2027-03-31"],
               ["R-04", "Equipos personales en la red de invitados", "Aceptar", "Gerente de tecnología", "2026-10-15"]]   # vence hoy: no es señal
    if siembra:
        esperado.append(("risk_acceptance_expired", "riesgo:r_03"))
    tabla(docs / "40-riesgos" / "registro-riesgos", riesgos, not e["excel"])
    documento(docs / "40-riesgos" / "aceptacion-R-01.pdf", "# Aceptación del riesgo R-01\n\nEl Gerente general acepta el riesgo hasta el 31 de diciembre de 2026.\n")
    return ficha, esperado


# ================================================================ Guillermo

def cve(n: int) -> str:
    return f"CVE-2099-{n:05d}"


CABECERAS = {
    "ingles-csv": ["Host", "Plugin ID", "CVE", "Name", "Risk", "CVSS v4.0 Base Score", "First Found"],
    "espanol-xlsx": ["Activo", "Id", "Vulnerabilidad", "Título", "Severidad", "Puntaje CVSS", "Primera detección"],
    "mapeo-csv": ["Equipo afectado", "Regla", "Identificador", "Descripción", "Criticidad del hallazgo", "Puntuación", "Detectado desde"],
    "puntaje-csv": ["Host", "Plugin ID", "CVE", "Name", "Risk", "CVSS v4.0 Base Score", "First Found"],
}
MAPEO = {"mapeo-csv": {"activo": "Equipo afectado", "vulnerabilidad": "Identificador", "titulo": "Descripción",
                       "severidad": "Criticidad del hallazgo", "cvss": "Puntuación", "primera": "Detectado desde"}}
SEV_TEXTO = {"ingles-csv": {"critica": "Critical", "alta": "High", "media": "Medium", "baja": "Low", "ninguna": "None"},
             "espanol-xlsx": {"critica": "Crítica", "alta": "Alta", "media": "Media", "baja": "Baja", "ninguna": "Informativa"},
             "mapeo-csv": {"critica": "Urgente", "alta": "Importante", "media": "Moderada", "baja": "Baja", "ninguna": "Info"},
             "puntaje-csv": {s: "" for s in ("critica", "alta", "media", "baja", "ninguna")}}
PUNTAJE = {"critica": "9.8", "alta": "8.1", "media": "5.3", "baja": "3.1", "ninguna": "0.0"}


def guillermo(e: dict, docs: Path) -> tuple[dict, list]:
    siembra, p = e["siembra"], e["pref"]
    esperado = []
    a = lambda x: f"{p}-{x}"  # noqa: E731
    activos = ["web-01", "app-01", "db-01", "fw-borde-01", "vpn-01", "ad-01", "correo-01", "backup-01", "ws-finanzas-01"]
    inv = [["activo", "tipo", "criticidad", "responsable", "alcance"]]
    inv += [[a(x), "servidor" if x not in ("fw-borde-01", "vpn-01", "ws-finanzas-01") else ("red" if x != "ws-finanzas-01" else "estación"),
             "alta" if x in ("web-01", "db-01", "fw-borde-01", "ad-01") else "media", "Jefe de infraestructura", "sí"] for x in activos]
    inv.append([a("laptop-gerencia"), "estación", "baja", "Gerencia", "no"])            # fuera de alcance, sin escanear: no es señal
    tabla(docs / "00-referencia" / "inventario-activos", inv, e["excel"])

    # Lo que encuentra cada escaneo: (activo, vulnerabilidad, título, severidad, primera detección, escaneos en que aparece).
    base = {0: ["web-01", "app-01", "db-01", "fw-borde-01", "vpn-01", "ad-01", "correo-01", "backup-01"],
            1: ["web-01", "app-01", "db-01", "fw-borde-01", "ad-01", "correo-01", "backup-01", "prueba-07"],
            2: ["web-01", "app-01", "db-01", "fw-borde-01", "ad-01", "correo-01", "backup-01", "prueba-07"]}
    if not siembra:
        base[1] = base[1] + ["vpn-01", "ws-finanzas-01"]     # en el control, la VPN y la estación se escanean en la ventana
        base[2] = base[2] + ["vpn-01"]
    hallazgos = [
        # vulnerabilidad sana: baja, reciente
        ("web-01", cve(11001), "Cabecera de seguridad ausente", "baja", "2026-10-10", (2,)),
        # vulnerabilidad corregida a tiempo: el escaneo de octubre ya no la encuentra
        ("app-01", cve(11002), "Biblioteca de plantillas desactualizada", "alta", "2026-08-20", (0,)),
        # fuera de plazo con excepción vigente: no es señal
        ("app-01", "TLS-DEBIL", "Suites de cifrado débiles", "baja", "2026-02-01", (0, 1, 2)),
        # del catálogo KEV, con su fecha de corrección después de hoy
        ("web-01", cve(11003), "Desbordamiento en el servidor web", "media", "2026-10-10", (2,)),
    ]
    excepciones = [["vulnerabilidad", "activo", "aprobada_por", "aprobada_el", "vence"],
                   ["TLS-DEBIL", a("app-01"), "Jefe de seguridad de la información", "2026-06-15", "2026-12-31"]]
    seguimiento = [["ticket", "activo", "vulnerabilidad", "estado", "fecha_cierre"],
                   ["TK-201", a("app-01"), cve(11002), "Cerrada", "2026-09-01"]]          # el escaneo del 20 de septiembre lo prueba
    kev = [("11003", "Servidor Web Sintético", "Desbordamiento en el servidor web", "2026-10-08", "2026-10-29", "Unknown")]
    if siembra:
        hallazgos += [
            ("web-01", cve(12001), "Ejecución remota en el portal", "critica", "2026-08-20", (0, 1, 2)),          # fuera de plazo
            ("fw-borde-01", cve(12002), "Omisión de autenticación en el cortafuegos", "alta", "2026-09-20", (1, 2)),  # KEV vencido
            ("db-01", cve(12003), "Escalamiento en el motor de base de datos", "media", "2026-06-01", (0, 1, 2)),     # excepción vencida
            ("backup-01", cve(12004), "Servicio de respaldo expuesto", "media", "2026-09-20", (1, 2)),               # cerrada sin escaneo posterior
            ("correo-01", cve(12005), "Inyección en el servidor de correo", "alta", "2026-09-20", (1, 2)),           # cerrada y la sigue encontrando
            ("ad-01", cve(12006), "Delegación insegura en el directorio", "critica", "2026-09-20", (1, 2)),          # fuera de plazo
        ]
        kev.append(("12002", "Cortafuegos Sintético", "Omisión de autenticación en el cortafuegos", "2026-09-17", "2026-10-01", "Known"))
        excepciones.append([cve(12003), a("db-01"), "Gerente de tecnología", "2026-07-01", "2026-09-30"])
        seguimiento += [["TK-202", a("backup-01"), cve(12004), "Cerrada", "2026-10-12"],
                        ["TK-203", a("correo-01"), cve(12005), "Resuelta", "2026-09-25"]]
        n = lambda x: S.norm(a(x))  # noqa: E731
        esperado += [("vuln_past_sla", f"sla:{n('web-01')}:{cve(12001)}"), ("kev_past_due", f"kev:{n('fw-borde-01')}:{cve(12002)}"),
                     ("vuln_exception_expired", f"excepcion:{cve(12003)}:{n('db-01')}"), ("vuln_past_sla", f"sla:{n('db-01')}:{cve(12003)}"),
                     ("vuln_closed_without_rescan", f"cierre:{n('backup-01')}:{cve(12004)}"),
                     ("vuln_closed_without_rescan", f"cierre:{n('correo-01')}:{cve(12005)}"),
                     ("asset_not_scanned", f"cobertura:{n('vpn-01')}"), ("asset_not_scanned", f"cobertura:{n('ws-finanzas-01')}"),
                     ("vuln_past_sla", f"sla:{n('ad-01')}:{cve(12006)}")]
    cab = CABECERAS[e["escaner"]]
    sev = SEV_TEXTO[e["escaner"]]
    for k, f in enumerate(ESCANEOS):
        filas = [cab]
        for x in base[k]:
            filas.append([a(x), "19506", "", "Información del escaneo", sev["ninguna"], "" if e["escaner"] != "puntaje-csv" else "0.0", ""])
        for (x, v, tit, s, primera, en) in hallazgos:
            if k in en:
                pid = str(30000 + int(re.sub(r"\D", "", v)[-4:] or 0)) if v.startswith("CVE") else "40001"
                filas.append([a(x), pid, v, tit, sev[s], PUNTAJE[s], primera])
        nombre = f"escaneo-{f}"
        (docs / "50-escaneos").mkdir(parents=True, exist_ok=True)
        if e["escaner"] == "espanol-xlsx":
            FMT.a_xlsx_tipado(filas, docs / "50-escaneos" / f"{nombre}.xlsx", "Hallazgos")
        else:
            csv_(docs / "50-escaneos" / f"{nombre}.csv", filas)
    cat = [["cveID", "vendorProject", "product", "vulnerabilityName", "dateAdded", "shortDescription", "requiredAction", "dueDate",
            "knownRansomwareCampaignUse", "forensicTriage", "notes", "cwes"]]
    for nn, prod, nom, ag, ve, rans in kev + [("10901", "Gestor Documental Sintético", "Carga de archivos sin validar", "2026-03-02", "2026-03-23", "Unknown")]:
        cat.append([f"CVE-2099-{nn}", "Proveedor Sintético", prod, nom, ag, "Vulnerabilidad sintética del material de prueba.",
                    "Aplicar las mitigaciones del fabricante.", ve, rans, "No", "", "CWE-20"])
    csv_(docs / "50-escaneos" / "known_exploited_vulnerabilities.csv", cat)
    tabla(docs / "60-remediacion" / "excepciones", excepciones, not e["excel"])
    tabla(docs / "60-remediacion" / "seguimiento", seguimiento, e["excel"])
    sla = e["sla"]
    documento(docs / "00-referencia" / "politica-gestion-vulnerabilidades.pdf",
              f"# Política de gestión de vulnerabilidades técnicas\n\n**{e['nombre']}** · versión 3 · aprobada por el comité de seguridad\n\n"
              "## 1. Objetivo\n\nEstablecer cómo se identifican, priorizan y corrigen las vulnerabilidades técnicas de los activos de información.\n\n"
              "## 4. Plazos de corrección\n\nCada vulnerabilidad se corrige dentro del plazo que corresponde a su severidad, contado desde su primera detección:\n\n"
              f"- Crítica: {sla['critica']} días calendario.\n- Alta: {sla['alta']} días calendario.\n- Media: {sla['media']} días calendario.\n- Baja: {sla['baja']} días calendario.\n\n"
              "La severidad es la que asigna el escáner. Una excepción al plazo la aprueba el jefe de seguridad de la información o el gerente de tecnología, por escrito y con fecha de vencimiento.\n\n"
              "## 5. Escaneo\n\nTodo activo del inventario en alcance se escanea al menos una vez al mes.\n")
    return {"questions": []}, esperado


# ================================================================ Amparo

def amparo(e: dict, docs: Path) -> tuple[dict, list]:
    siembra, cont = e["siembra"], e["contencion"]
    esperado = []
    ficha = {"incidents": [], "reviews": [], "tests": [], "reviewed": [], "questions": []}
    sup, dat = e["supervisor"], e["datos"]
    matriz = [["destinatario", "cuando", "plazo_horas", "norma"],
              [sup, "crítica", 24, "Reglamento sectorial de ciberseguridad (sintético)"],
              [dat, "datos personales", 72, "Ley de protección de datos (sintética)"],
              ["Clientes afectados", "clientes afectados", 72, "Política de comunicación con clientes"],
              ["Comité de riesgos", "todos", 48, "Política de respuesta a incidentes"]]
    tabla(docs / "00-referencia" / "matriz-notificaciones", matriz, not e["excel"])
    documento(docs / "00-referencia" / "politica-respuesta-incidentes.docx",
              f"# Política de respuesta a incidentes de seguridad\n\n**{e['nombre']}** · versión 2\n\n"
              "## 3. Clasificación\n\nCada incidente se clasifica como crítico, alto, medio o bajo al momento de su detección.\n\n"
              "## 5. Contención\n\nEl incidente se contiene dentro de las siguientes horas desde su detección:\n\n"
              f"| Severidad | Horas para contenerlo |\n|---|---|\n| Crítica | {cont['critica']} |\n| Alta | {cont['alta']} |\n| Media | {cont['media']} |\n| Baja | {cont['baja']} |\n\n"
              f"## 7. Revisión posterior\n\nTodo incidente cerrado tiene su revisión de lecciones aprendidas dentro de los {e['revision']} días calendario siguientes a su cierre.\n\n"
              "## 8. Notificaciones\n\nLas notificaciones externas e internas se hacen según la matriz de notificaciones vigente.\n")
    p = e["pref"].upper()
    def h(base: str, horas: float) -> str:
        t = dt.datetime.fromisoformat(base) + dt.timedelta(hours=horas)
        return t.isoformat(timespec="minutes")
    incs = []
    # INC-1: crítico, sano; el supervisor justo a las 24 horas.
    incs.append({"id": f"INC-{p}-101", "title": "Ransomware contenido en un servidor de archivos", "severity": "crítica", "detected_at": "2026-09-03T09:10",
                 "contained_at": h("2026-09-03T09:10", cont["critica"] - 0.5), "closed_on": "2026-09-08", "personal_data": False, "customers_affected": False,
                 "notif": [(sup, 24), ("Comité de riesgos", 6)], "review": "2026-09-12"})
    if siembra:
        lim = cont["alta"]
        incs.append({"id": f"INC-{p}-102", "title": "Acceso indebido a una cuenta privilegiada", "severity": "alta", "detected_at": "2026-09-10T14:00",
                     "contained_at": h("2026-09-10T14:00", lim + 6), "closed_on": "2026-09-15", "personal_data": False, "customers_affected": False,
                     "notif": [("Comité de riesgos", 10)], "review": "2026-09-20"})
        esperado.append(("incident_response_late", f"contencion:INC-{p}-102"))
        incs.append({"id": f"INC-{p}-103", "title": "Exfiltración de una base de datos de clientes", "severity": "crítica", "detected_at": "2026-09-22T07:30",
                     "contained_at": h("2026-09-22T07:30", cont["critica"] - 0.5), "closed_on": "2026-09-26", "personal_data": True, "customers_affected": False,
                     "notif": [(sup, 30), (dat, 40), ("Comité de riesgos", 5)], "review": "2026-09-30"})
        esperado.append(("incident_notification_late", f"notificacion:INC-{p}-103:{S.norm(sup)}"))
        incs.append({"id": f"INC-{p}-104", "title": "Indisponibilidad del portal por denegación de servicio", "severity": "media", "detected_at": "2026-10-01T11:00",
                     "contained_at": h("2026-10-01T11:00", 20), "closed_on": None, "personal_data": False, "customers_affected": True,
                     "notif": [("Comité de riesgos", 8)], "review": None})
        esperado.append(("incident_notification_late", f"notificacion:INC-{p}-104:clientes_afectados"))
        incs.append({"id": f"INC-{p}-105", "title": "Correo de suplantación con un enlace malicioso", "severity": "baja", "detected_at": "2026-08-18T10:00",
                     "contained_at": h("2026-08-18T10:00", 30), "closed_on": "2026-08-25", "personal_data": False, "customers_affected": False,
                     "notif": [("Comité de riesgos", 12)], "review": None})
        esperado.append(("incident_without_review", f"revision:INC-{p}-105"))
        incs.append({"id": f"INC-{p}-106", "title": "Malware en una estación de trabajo de finanzas", "severity": "alta", "detected_at": "2026-09-28T16:45",
                     "contained_at": None, "closed_on": None, "personal_data": False, "customers_affected": False,
                     "notif": [("Comité de riesgos", 4)], "review": None})
        esperado.append(("incident_response_late", f"contencion:INC-{p}-106"))
    for i in incs:
        base = f"70-incidentes/{i['id']}"
        lineas = [f"# Informe del incidente {i['id']}", "", f"**Título:** {i['title']}", "", f"**Severidad asignada:** {i['severity']}", "",
                  "## Línea de tiempo", "", "| Hito | Fecha y hora |", "|---|---|",
                  f"| Detección | {i['detected_at'].replace('T', ' ')} |",
                  f"| Contención | {i['contained_at'].replace('T', ' ') if i['contained_at'] else 'pendiente'} |",
                  f"| Cierre | {i['closed_on'] or 'abierto'} |", "",
                  f"**Datos personales comprometidos:** {'sí' if i['personal_data'] else 'no'}", "",
                  f"**Clientes afectados:** {'sí' if i['customers_affected'] else 'no'}", "", "## Notificaciones", ""]
        notifs = []
        for k, (dest, horas) in enumerate(i["notif"]):
            cuando = h(i["detected_at"], horas)
            nom = documento(docs / "70-incidentes" / f"{i['id']}_notificacion-{slug(dest)}.pdf",
                            f"# Constancia de notificación\n\nIncidente: {i['id']}\n\nDestinatario: {dest}\n\nFecha y hora de envío: {cuando.replace('T', ' ')}\n\nRadicado: {i['id']}-N{k + 1}\n")
            notifs.append({"to": dest, "at": cuando, "source": f"70-incidentes/{nom}"})
            lineas.append(f"- {dest}: {cuando.replace('T', ' ')} (constancia adjunta).")
        nom = documento(docs / "70-incidentes" / f"{i['id']}_informe.docx", "\n".join(lineas) + "\n")
        ficha["incidents"].append({"id": i["id"], "severity": i["severity"], "detected_at": i["detected_at"], "contained_at": i["contained_at"],
                                   "closed_on": i["closed_on"], "personal_data": i["personal_data"], "customers_affected": i["customers_affected"],
                                   "notifications": notifs, "source": f"{base}_informe.docx"})
        if i["review"]:
            nom = documento(docs / "80-revisiones" / f"{i['id']}_revision.md",
                            f"# Revisión posterior del incidente {i['id']}\n\nFecha de la revisión: {i['review']}\n\nLecciones aprendidas y acciones con responsable y fecha.\n")
            ficha["reviews"].append({"incident": i["id"], "date": i["review"], "source": f"80-revisiones/{nom}"})

    # El calendario de continuidad y sus pruebas.
    cal = [["prueba", "tipo", "sistema", "frecuencia_dias", "responsable"],
           ["Plan de continuidad del negocio", "continuidad", "Toda la entidad", 365, "Gerente de riesgos"],
           ["Recuperación del centro de datos alterno", "recuperación", "Centro de datos", 180, "Jefe de infraestructura"],
           [f"Restauración del {e['sistema'].lower()}", "restauración", e["sistema"], 90, "Jefe de infraestructura"],
           ["Restauración del correo corporativo", "restauración", "Correo corporativo", 90, "Jefe de infraestructura"],
           ["Restauración de la base de clientes", "restauración", "Base de clientes", 180, "Jefe de infraestructura"]]
    tabla(docs / "00-referencia" / "calendario-continuidad", cal, e["excel"])
    pruebas = [("Plan de continuidad del negocio", "2026-03-15", "exitosa"),
               ("Recuperación del centro de datos alterno", "2026-02-20" if siembra else "2026-05-10", "exitosa"),
               (f"Restauración del {e['sistema'].lower()}", "2026-08-01", "con observaciones"),
               ("Restauración del correo corporativo", "2026-06-20" if siembra else "2026-08-20", "exitosa"),
               ("Restauración de la base de clientes", None if siembra else "2026-07-01", "exitosa")]
    if siembra:
        esperado += [("continuity_test_overdue", f"prueba:{S.norm('Recuperación del centro de datos alterno')}"),
                     ("restore_test_overdue", f"prueba:{S.norm('Restauración del correo corporativo')}"),
                     ("restore_test_overdue", f"prueba:{S.norm('Restauración de la base de clientes')}")]
    for t, f, res in pruebas:
        if not f:
            continue
        nom = documento(docs / "90-continuidad" / f"prueba_{slug(t)}_{f}.pdf",
                        f"# Informe de prueba · {t}\n\nFecha de ejecución de la prueba: {f}\n\nResultado: {res}.\n\nObjetivos de tiempo de recuperación verificados en la prueba.\n")
        ficha["tests"].append({"test": t, "date": f, "result": res, "source": f"90-continuidad/{nom}"})
    return ficha, esperado


# ================================================================ lo que nunca se abre

def nunca(docs: Path) -> list[str]:
    (docs / "10-controles" / "A.8.24_certificados").mkdir(parents=True, exist_ok=True)
    (docs / "10-controles" / "A.8.24_certificados" / "servidor-web.pem").write_text(
        "-----BEGIN PRIVATE KEY-----\nMATERIAL-SINTETICO-NO-ES-UNA-LLAVE\n-----END PRIVATE KEY-----\n", encoding="utf-8")
    (docs / "00-referencia" / "credenciales-vpn.txt").write_text("usuario: sintetico\nclave: no-es-una-clave\n", encoding="utf-8")
    (docs / "90-continuidad" / "respaldo-correo-2026-06-20.zip").write_bytes(b"PK\x05\x06" + b"\x00" * 18)
    return ["00-referencia/credenciales-vpn.txt", "10-controles/A.8.24_certificados/servidor-web.pem", "90-continuidad/respaldo-correo-2026-06-20.zip"]


# ================================================================ cada entidad

def una(e: dict) -> dict:
    raiz = SALIDA / e["carpeta"]
    base = f"{e['id'].lower().replace('-', '')}-{slug(e['nombre'])}"
    docs_rel, estado_rel = f"seguridad/{base}", f"estado-seguridad/{base}"
    docs = raiz / docs_rel
    fa, ea = alexis(e, docs)
    fg, eg = guillermo(e, docs)
    fm, em = amparo(e, docs)
    excl = nunca(docs)
    ent = {"id": e["id"], "name": e["nombre"], "country": e["pais"], "currency": e["moneda"]}
    comun = {"entity": ent, "paths": {"documents": docs_rel, "state": estado_rel}, "period": PERIODO}
    cfg = {"alexis": dict(comun),
           "guillermo": dict(comun, vulnerability={"sla_days": dict(e["sla"]), "publish": False},
                             scanner={"columns": MAPEO.get(e["escaner"], {})}, thresholds={"scan_window_days": 30}),
           "amparo": dict(comun, incident={"containment_hours": dict(e["contencion"]), "review_days": e["revision"]})}
    esperado = [{"signal": s, "key": k} for s, k in ea + eg + em]
    clave = {"entidad": e["nombre"], "industria": e["industria"], "pais": e["pais"], "escaner": e["escaner"],
             "hoy": HOY.isoformat(), "periodo": PERIODO, "siembra": bool(e["siembra"]), "excluidos": excl, "config": cfg,
             "extraccion": {"seguridad": fa, "vulnerabilidades": fg, "resiliencia": fm}, "esperado": esperado}
    (raiz / "clave.json").write_text(json.dumps(clave, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return clave


def main() -> int:
    if SALIDA.exists():
        shutil.rmtree(SALIDA)
    total = 0
    for e in ENTIDADES:
        c = una(e)
        total += len(c["esperado"])
        print(f"  {e['carpeta']:<15} {e['pais']}  {e['escaner']:<13} {len(c['esperado']):>3} señales esperadas")
    print(f"\n  {len(ENTIDADES)} entidades, {total} señales en la clave, en tests/criterio-ciso/material/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
