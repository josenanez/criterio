#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El material de prueba de la familia CTO: un banco en Colombia, una cadena de retail en México, una
empresa de software en Chile y dos entidades de control.

    python3 tests/criterio-cto/generar.py          escribe tests/criterio-cto/material/

Cada entidad trae su carpeta de tecnología al 25 de noviembre de 2026, con octubre como el periodo que se
evalúa: la política de cambios y de niveles de servicio y el catálogo de servicios en `00-politica/`; la
exportación de cambios, el registro de despliegues y las actas del comité de cambios en `10-cambios/`; los
incidentes, los problemas y la disponibilidad de octubre en `20-servicio/`; el inventario de activos, las
licencias y las actas del comité de arquitectura en `30-activos/`; el contrato, el cumplimiento y las
facturas de cada proveedor en `40-proveedores/`, y la factura y el presupuesto de la nube en `50-nube/`.

**La clave la escribe este archivo, no el motor.** Cada defecto se siembra a propósito y su señal esperada
queda escrita en `clave.json`, junto con lo que el agente tendría que extraer de los documentos escritos
—cada aprobación y cada revisión de un cambio que quedó en un acta, cada excepción aprobada sobre un activo
y cada nivel de servicio de un contrato— y la configuración que deja el setup. El motor no la ve;
`evaluar.py` compara lo que el motor levanta contra ella, y una señal de más cuenta igual que una de menos.

**Cuántas veces.** El banco y el retail traen cada defecto tres veces y la de software, dos (`veces`), cada
repetición en su propia fila —otro cambio, otro activo, otro proveedor—. Así la familia pasa de 73 señales
sembradas desde su primera versión, la muestra que pide el piso del 95 % sin fallas (decisión 0020).

**Las entidades de control no tienen ningún defecto**, y sí los casos que se parecen a uno: un cambio
aprobado el mismo día en que se implementó, un cambio estándar sin aprobación por cambio, uno de emergencia
revisado el último día del plazo, uno revertido con su revisión, un despliegue sin cambio en el ambiente de
pruebas, un incidente mayor resuelto hace menos días que el plazo, un servicio que da exactamente su nivel,
un activo sin soporte con su excepción vigente, uno sin soporte que no está en producción, una licencia en
uso igual a las compradas, un proveedor que incumplió con su crédito en la factura y una cuenta de la nube
por encima de su presupuesto dentro de la tolerancia. Todo es determinista: el mismo material cada vez, byte
a byte. Los nombres, las empresas y los documentos son inventados.
"""
from __future__ import annotations

import datetime as dt
import json
import shutil
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent.parent
sys.path.insert(0, str(RAIZ / "tests" / "sintetico"))
import formatos as FMT  # noqa: E402  (Word, Excel y PDF sin dependencias y con fecha fija, los mismos de las demás familias)

SALIDA = AQUI / "material"
HOY, PERIODO = dt.date(2026, 11, 25), "2026-10"
METODO = {"emergency_review_days": 5, "problem_days": 10, "unused_license_pct": 15, "cloud_tolerance_pct": 5}
TODAS = {"aprobacion", "emergencia", "fallido", "despliegue", "problema", "nivel",
         "dueno", "soporte", "faltante", "sobrante", "credito", "nube"}
COMITE = "Comité de cambios"

ENTIDADES = [
    {"carpeta": "banca-co", "industria": "banca", "pais": "CO", "id": "901222444", "nombre": "Banco Meridiano Sintético", "moneda": "COP",
     "siembra": set(TODAS), "veces": 3, "escala": 1_000_000},
    {"carpeta": "retail-mx", "industria": "retail", "pais": "MX", "id": "RGS180610QW4", "nombre": "Retail del Golfo Sintético", "moneda": "MXN",
     "siembra": set(TODAS), "veces": 3, "escala": 5_000},
    {"carpeta": "tecnologia-cl", "industria": "tecnologia", "pais": "CL", "id": "76543210-K", "nombre": "Software Austral Sintético", "moneda": "CLP",
     "siembra": set(TODAS), "veces": 2, "escala": 250_000},
    {"carpeta": "control-co", "industria": "banca", "pais": "CO", "id": "901333666", "nombre": "Banco Control de Tecnología Sintético", "moneda": "COP",
     "siembra": set(), "veces": 1, "escala": 1_000_000},
    {"carpeta": "control-mx", "industria": "retail", "pais": "MX", "id": "RCT190101AB2", "nombre": "Retail Control de Tecnología Sintético", "moneda": "MXN",
     "siembra": set(), "veces": 1, "escala": 5_000},
]

# Las repeticiones de cada defecto: la primera vez (1), la segunda (2) y la tercera (3), cada una en su fila.
SERVICIOS = {1: ("S-11", "Pagos en línea", 99.9, 99.4), 2: ("S-12", "Aplicación móvil", 99.5, 98.7), 3: ("S-13", "Portal de proveedores", 99.0, 97.9)}
ACTIVOS_SIN_DUENO = {1: ("A-210", "Servidor de integración"), 2: ("A-220", "Balanceador de carga"), 3: ("A-230", "Repositorio de archivos")}
ACTIVOS_SIN_SOPORTE = {1: ("A-310", "Servidor de la base de datos de clientes", "2025-12-31"),
                       2: ("A-320", "Sistema operativo del servidor de pagos", "2026-06-30"),
                       3: ("A-330", "Gestor de colas de mensajes", "2026-04-30")}
SOFTWARE_FALTA = {1: ("Diseño gráfico", 40, 46), 2: ("Herramienta de analítica", 120, 131), 3: ("Gestor de proyectos", 75, 80)}
SOFTWARE_SOBRA = {1: ("Videoconferencia", 600, 410), 2: ("Firma electrónica", 200, 120), 3: ("Antivirus de escritorio", 900, 700)}
PROVEEDORES = {1: ("Nube Andina", "Disponibilidad", 99.95, 99.7, 10), 2: ("Enlaces del Pacífico", "Disponibilidad", 99.8, 99.2, 8),
               3: ("Soporte Integral", "Casos resueltos a tiempo", 95, 89, 5)}
CUENTAS = {1: ("Analítica", 30, 36), 2: ("Canales digitales", 45, 51), 3: ("Respaldo", 12, 14)}


def _pdf(md: str, ruta: Path) -> None:
    ruta.parent.mkdir(parents=True, exist_ok=True)
    FMT.a_pdf(md, ruta)


def _xlsx(filas: list[list], ruta: Path) -> None:
    ruta.parent.mkdir(parents=True, exist_ok=True)
    FMT.a_xlsx_tipado(filas, ruta)


def _norm(s: str) -> str:
    import re
    import unicodedata
    s = unicodedata.normalize("NFKD", str(s)).encode("ascii", "ignore").decode().lower()
    return "_".join(x for x in re.split(r"[^a-z0-9]+", s) if x)


def _porc(x: float) -> str:
    return f"{x:g}".replace(".", ",")


def construir(e: dict) -> dict:
    """La carpeta de una entidad y su clave."""
    s = e["siembra"]
    raiz = SALIDA / e["carpeta"]
    nombre_carpeta = f"{e['id'].lower()}-{_norm(e['nombre']).replace('_', '-')}"
    docs = raiz / "tecnologia" / nombre_carpeta
    esc = e["escala"]
    esperado = []

    def esp(signal: str, key: str) -> None:
        esperado.append({"signal": signal, "key": key})

    def veces(tipo: str) -> list[int]:
        """Las veces que se siembra un defecto: ninguna en un control."""
        return list(range(1, e["veces"] + 1)) if tipo in s else []

    # ------------------------------------------------------------ 00-politica
    _pdf(f"# Política de cambios y de niveles de servicio · {e['nombre']}\n\nAprobada por el comité de tecnología el 2025-11-20.\n\n"
         "## Los cambios\n\nTodo cambio normal lo aprueba el comité de cambios antes de implementarse. Un cambio estándar está preaprobado. "
         f"Un cambio de emergencia se revisa en el comité dentro de los {METODO['emergency_review_days']} días siguientes a su implementación, "
         "y un cambio fallido o revertido se revisa siempre.\n\n"
         f"## Los incidentes\n\nTodo incidente mayor tiene su registro de problema, con su causa, dentro de los {METODO['problem_days']} días siguientes a su solución.\n\n"
         "## Los niveles de servicio\n\nEl nivel de cada servicio es el del catálogo de servicios.\n\n"
         f"## Los activos y los proveedores\n\nSe tolera hasta un {METODO['unused_license_pct']} % de licencias pagadas sin uso. "
         f"El gasto de cada cuenta de la nube no supera su presupuesto en más del {METODO['cloud_tolerance_pct']} %.\n",
         docs / "00-politica" / "politica_de_cambios_y_niveles_de_servicio.pdf")
    cat = [["Servicio", "Nombre", "Disponibilidad acordada", "Dueño"],
           ["S-01", "Banca en línea" if e["industria"] == "banca" else "Tienda en línea", 99.9, "Canales digitales"],
           ["S-02", "Pagos", 99.5, "Operaciones"], ["S-03", "Correo", 99.0, "Infraestructura"]]
    cat += [[SERVICIOS[i][0], SERVICIOS[i][1], SERVICIOS[i][2], "Canales digitales"] for i in veces("nivel")]
    _xlsx(cat, docs / "00-politica" / "catalogo_de_servicios.xlsx")

    # ------------------------------------------------------------ 10-cambios
    # Las sesiones del comité de cambios, semanales. Cada aprobación y cada revisión lleva la fecha de su sesión.
    sesiones: dict[str, dict] = {}

    def acta(fecha: str, que: str, cambio: str, texto: str) -> None:
        sesiones.setdefault(fecha, {"aprueba": [], "revisa": [], "otros": []})[que].append((cambio, texto))

    cambios = [["Cambio", "Tipo", "Fecha de implementación", "Resultado", "Servicio", "Descripción"],
               ["CHG-100", "Normal", "2026-10-05", "Exitoso", "S-01", "Actualización del certificado del portal"],
               ["CHG-101", "Estándar", "2026-10-20", "Exitoso", "S-03", "Alta de buzones del mes"],
               ["CHG-102", "Emergencia", "2026-10-10", "Exitoso", "S-02", "Corrección de la conciliación de pagos"],
               ["CHG-103", "Normal", "2026-10-08", "Exitoso", "S-01", "Ajuste del límite de sesiones"],
               ["CHG-104", "Normal", "2026-10-12", "Revertido", "S-02", "Nueva versión del motor de pagos"]]
    acta("2026-10-01", "aprueba", "CHG-100", "actualización del certificado del portal")
    acta("2026-10-08", "aprueba", "CHG-103", "ajuste del límite de sesiones")          # el mismo día en que se implementó
    acta("2026-10-08", "aprueba", "CHG-104", "nueva versión del motor de pagos")
    acta("2026-10-15", "revisa", "CHG-102", "corrección de emergencia de la conciliación de pagos")   # el último día del plazo
    acta("2026-10-15", "revisa", "CHG-104", "nueva versión del motor de pagos, revertida el 2026-10-12")
    # Sembrado: un cambio normal sin aprobación (1 y 3) o aprobado en una sesión posterior a su implementación (2).
    for i in veces("aprobacion"):
        cid, impl = f"CHG-2{i}0", {1: "2026-10-06", 2: "2026-10-16", 3: "2026-10-26"}[i]
        desc = {1: "Migración del servidor de archivos", 2: "Cambio de la regla del cortafuegos de la red interna", 3: "Nueva integración con el proveedor de mensajería"}[i]
        cambios.append([cid, "Normal", impl, "Exitoso", "S-01", desc])
        if i == 2:
            acta("2026-10-22", "aprueba", cid, desc.lower())
        elif i == 1:
            acta("2026-10-01", "otros", cid, f"{desc.lower()}: se presenta y queda pendiente de más información")
        esp("change_without_approval", f"aprobacion:{cid}")
    # Sembrado: un cambio de emergencia sin revisión (1 y 3) o revisado fuera del plazo (2).
    for i in veces("emergencia"):
        cid, impl = f"CHG-3{i}0", {1: "2026-10-03", 2: "2026-10-09", 3: "2026-10-18"}[i]
        desc = {1: "Reinicio de emergencia del clúster de base de datos", 2: "Parche de emergencia del servidor de aplicaciones", 3: "Reversión de emergencia del balanceador"}[i]
        cambios.append([cid, "Emergencia", impl, "Exitoso", "S-02", desc])
        if i == 2:
            acta("2026-10-22", "revisa", cid, desc.lower())
        esp("emergency_change_without_review", f"emergencia:{cid}")
    # Sembrado: un cambio aprobado que falló o se revirtió, sin revisión.
    for i in veces("fallido"):
        cid, impl, apr = f"CHG-4{i}0", {1: "2026-10-07", 2: "2026-10-13", 3: "2026-10-21"}[i], {1: "2026-10-01", 2: "2026-10-08", 3: "2026-10-15"}[i]
        desc = {1: "Actualización del sistema de nómina", 2: "Nueva versión de la aplicación móvil", 3: "Cambio del esquema del almacén de datos"}[i]
        cambios.append([cid, "Normal", impl, {1: "Revertido", 2: "Fallido", 3: "Revertido"}[i], "S-01", desc])
        acta(apr, "aprueba", cid, desc.lower())
        esp("failed_change_without_review", f"fallido:{cid}")
    _xlsx(cambios, docs / "10-cambios" / "cambios_2026-10.xlsx")
    desp = [["Despliegue", "Fecha", "Ambiente", "Cambio", "Sistema"],
            ["D-100", "2026-10-05", "Producción", "CHG-100", "Portal"], ["D-101", "2026-10-08", "Producción", "CHG-103", "Portal"],
            ["D-102", "2026-10-19", "Pruebas", "", "Aplicación móvil"]]                  # sin cambio, pero en pruebas
    # Sembrado: un despliegue en producción sin cambio (1 y 3) o con un cambio que no está en la exportación (2).
    for i in veces("despliegue"):
        did = f"D-5{i}0"
        desp.append([did, {1: "2026-10-14", 2: "2026-10-23", 3: "2026-10-28"}[i], "Producción", "CHG-999" if i == 2 else "",
                     {1: "Motor de reglas", 2: "Servicio de notificaciones", 3: "Tablero de ventas"}[i]])
        esp("deployment_without_change", f"despliegue:{did}")
    _xlsx(desp, docs / "10-cambios" / "despliegues_2026-10.xlsx")
    aprobaciones, revisiones = [], []
    for fecha in sorted(sesiones):
        se = sesiones[fecha]
        f = f"10-cambios/acta_comite_de_cambios_{fecha}.pdf"
        md = f"# Acta del comité de cambios · {e['nombre']}\n\nSesión del {fecha}.\n\n"
        if se["aprueba"]:
            md += "## Cambios aprobados\n\n" + "\n".join(f"- {c}, {t}: el comité lo aprueba." for c, t in se["aprueba"]) + "\n\n"
            aprobaciones += [{"change": c, "date": fecha, "authority": COMITE, "source": f} for c, _ in se["aprueba"]]
        if se["revisa"]:
            md += "## Revisiones posteriores\n\n" + "\n".join(f"- {c}, {t}: el comité revisa su implementación y su causa." for c, t in se["revisa"]) + "\n\n"
            revisiones += [{"change": c, "date": fecha, "source": f} for c, _ in se["revisa"]]
        if se["otros"]:
            md += "## Otros asuntos\n\n" + "\n".join(f"- {c}, {t}." for c, t in se["otros"]) + "\n"
        _pdf(md, docs / f)

    # ------------------------------------------------------------ 20-servicio
    inc = [["Incidente", "Prioridad", "Incidente mayor", "Servicio", "Fecha de solución"],
           ["INC-100", "P1", "Sí", "S-01", "2026-10-03"], ["INC-101", "P1", "Sí", "S-02", "2026-11-20"],   # resuelto hace menos de 10 días
           ["INC-102", "P3", "No", "S-03", "2026-10-11"]]
    pro = [["Problema", "Incidente", "Causa", "Fecha de registro"], ["PRB-100", "INC-100", "Certificado vencido en el balanceador", "2026-10-06"]]
    # Sembrado: un incidente mayor sin problema (1 y 3) o con su problema sin causa (2).
    for i in veces("problema"):
        iid = f"INC-6{i}0"
        inc.append([iid, "P1", "Sí", {1: "S-02", 2: "S-01", 3: "S-03"}[i], {1: "2026-10-04", 2: "2026-10-12", 3: "2026-10-27"}[i]])
        if i == 2:
            pro.append([f"PRB-6{i}0", iid, "", "2026-10-14"])
        esp("major_incident_without_problem", f"problema:{iid}")
    _xlsx(inc, docs / "20-servicio" / "incidentes_2026-10.xlsx")
    _xlsx(pro, docs / "20-servicio" / "problemas.xlsx")
    disp = [["Servicio", "Periodo", "Disponibilidad"], ["S-01", PERIODO, 99.95], ["S-02", PERIODO, 99.5], ["S-03", PERIODO, 99.2]]   # S-02, exactamente su nivel
    for i in veces("nivel"):
        disp.append([SERVICIOS[i][0], PERIODO, SERVICIOS[i][3]])
        esp("service_below_level", f"nivel:{SERVICIOS[i][0]}")
    _xlsx(disp, docs / "20-servicio" / "disponibilidad_2026-10.xlsx")

    # ------------------------------------------------------------ 30-activos
    inv = [["Activo", "Nombre", "Dueño", "Ambiente", "Fin de soporte"],
           ["A-100", "Sistema central", "Infraestructura", "Producción", "2028-12-31"],
           ["A-101", "Servidor de reportes", "Infraestructura", "Producción", "2026-03-31"],      # sin soporte, con su excepción vigente
           ["A-102", "Servidor del laboratorio", "Infraestructura", "Pruebas", "2024-06-30"],   # sin soporte, fuera de producción
           ["A-103", "Plataforma de correo", "Infraestructura", "Producción", "2026-12-31"]]
    for i in veces("dueno"):
        aid, nom = ACTIVOS_SIN_DUENO[i]
        inv.append([aid, nom, "", "Producción", "2029-06-30"])
        esp("asset_without_owner", f"dueno:{aid}")
    excepciones = [{"asset": "A-101", "until": "2027-03-31", "source": "30-activos/acta_comite_de_arquitectura_2026-10.pdf"}]
    antiguas = []
    # Sembrado: un activo en producción sin soporte y sin excepción (1 y 3), o con la excepción vencida (2).
    for i in veces("soporte"):
        aid, nom, fin = ACTIVOS_SIN_SOPORTE[i]
        inv.append([aid, nom, "Infraestructura", "Producción", fin])
        if i == 2:
            antiguas.append((aid, nom, "2026-09-30"))
        esp("asset_out_of_support", f"soporte:{aid}")
    _xlsx(inv, docs / "30-activos" / "inventario_de_activos.xlsx")
    _pdf(f"# Acta del comité de arquitectura · {e['nombre']}\n\nSesión del 2026-10-20.\n\n## Excepciones\n\n"
         "- A-101, servidor de reportes: su fabricante terminó el soporte el 2026-03-31. El comité aprueba que siga en producción hasta el 2027-03-31, "
         "mientras se migra a la nueva plataforma.\n\n## Otros asuntos\n\n- A-103, plataforma de correo: se evaluará su reemplazo antes del fin de su soporte.\n",
         docs / "30-activos" / "acta_comite_de_arquitectura_2026-10.pdf")
    if antiguas:
        _pdf(f"# Acta del comité de arquitectura · {e['nombre']}\n\nSesión del 2026-03-17.\n\n## Excepciones\n\n"
             + "\n".join(f"- {a}, {n.lower()}: el comité aprueba que siga en producción hasta el {h}." for a, n, h in antiguas) + "\n",
             docs / "30-activos" / "acta_comite_de_arquitectura_2026-03.pdf")
        excepciones += [{"asset": a, "until": h, "source": "30-activos/acta_comite_de_arquitectura_2026-03.pdf"} for a, _, h in antiguas]
    lic = [["Software", "Licencias compradas", "Licencias en uso"], ["Correo", 500, 480], ["Ofimática", 300, 300], ["Base de datos", 20, 18]]
    for i in veces("faltante"):
        sw, c, u = SOFTWARE_FALTA[i]
        lic.append([sw, c, u])
        esp("license_shortfall", f"faltante:{_norm(sw)}")
    for i in veces("sobrante"):
        sw, c, u = SOFTWARE_SOBRA[i]
        lic.append([sw, c, u])
        esp("license_unused", f"sobrante:{_norm(sw)}")
    _xlsx(lic, docs / "30-activos" / "licencias.xlsx")

    # ------------------------------------------------------------ 40-proveedores
    provs = [("Centro de Datos Uno", "Disponibilidad", 99.9, 99.95, 10, 120),          # cumple
             ("Mesa de Ayuda Sintética", "Casos resueltos a tiempo", 95, 94, 5, 40)]    # incumple, con su crédito en la factura
    for i in veces("credito"):
        v, m, obj, med, cred = PROVEEDORES[i]
        provs.append((v, m, obj, med, cred, {1: 90, 2: 55, 3: 35}[i]))
        esp("vendor_breach_without_credit", f"credito:{_norm(v)}")
    niveles, cum, fac = [], [["Proveedor", "Métrica", "Periodo", "Valor"]], [["Factura", "Proveedor", "Periodo", "Valor", "Crédito"]]
    for k, (v, m, obj, med, cred, valor) in enumerate(provs):
        f = f"40-proveedores/contrato_{_norm(v)}.pdf"
        _pdf(f"# Contrato de prestación de servicios · {v}\n\nEntre {e['nombre']} y {v}. Vigente desde el 2025-01-01.\n\n"
             f"## Nivel de servicio\n\n{m}: {_porc(obj)} % en cada mes. Si no se cumple, el proveedor reconoce un crédito del {cred} % "
             "de la factura de ese mes, que se descuenta en la misma factura.\n", docs / f)
        niveles.append({"vendor": v, "metric": m, "target": obj, "credit_pct": cred, "source": f})
        cum.append([v, m, PERIODO, med])
        incumple_con_credito = med < obj and k == 1
        fac.append([f"FP-{k + 1:03d}", v, PERIODO, valor * esc, round(valor * esc * cred / 100) if incumple_con_credito else 0])
    _xlsx(cum, docs / "40-proveedores" / "cumplimiento_sla_2026-10.xlsx")
    _xlsx(fac, docs / "40-proveedores" / "facturas_proveedores_2026-10.xlsx")

    # ------------------------------------------------------------ 50-nube
    nube = [["Cuenta", "Periodo", "Servicio", "Costo"], ["Producción", PERIODO, "Cómputo", 60 * esc], ["Producción", PERIODO, "Almacenamiento", 22 * esc],
            ["Desarrollo", PERIODO, "Cómputo", 9 * esc]]
    pres = [["Cuenta", "Periodo", "Presupuesto"], ["Producción", PERIODO, 80 * esc], ["Desarrollo", PERIODO, 10 * esc]]   # Producción, 2,5 % por encima
    for i in veces("nube"):
        c, b, g = CUENTAS[i]
        nube.append([c, PERIODO, "Cómputo", g * esc])
        pres.append([c, PERIODO, b * esc])
        esp("cloud_over_budget", f"nube:{c}")
    _xlsx(nube, docs / "50-nube" / "factura_de_la_nube_2026-10.xlsx")
    _xlsx(pres, docs / "50-nube" / "presupuesto_de_la_nube_2026.xlsx")

    def cfg(rol: str) -> dict:
        met = ({"emergency_review_days": METODO["emergency_review_days"], "problem_days": METODO["problem_days"]} if rol == "cambios"
               else {"unused_license_pct": METODO["unused_license_pct"], "cloud_tolerance_pct": METODO["cloud_tolerance_pct"]})
        return {"version": "0.1", "role": rol, "entity": {"id": e["id"], "name": e["nombre"], "country": e["pais"], "currency": e["moneda"]},
                "paths": {"documents": f"tecnologia/{nombre_carpeta}", "state": f"estado-tecnologia/{nombre_carpeta}"}, "period": PERIODO,
                "publish_rostrum": True, "methodology": met, "columns": {}, "report": {"language": "es"}, "execution": {"workers": 1}}

    clave = {"entidad": e["nombre"], "industria": e["industria"], "pais": e["pais"], "hoy": HOY.isoformat(), "periodo": PERIODO, "siembra": bool(s),
             "config": {"fausto": cfg("cambios"), "domingo": cfg("activos")},
             "extraccion": {"cambios": {"approvals": aprobaciones, "reviews": revisiones, "reviewed": [], "questions": []},
                            "activos": {"exceptions": excepciones, "service_levels": niveles, "reviewed": [], "questions": []}},
             "esperado": sorted(esperado, key=lambda x: (x["signal"], x["key"]))}
    (raiz / "clave.json").write_text(json.dumps(clave, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return clave


def main() -> int:
    if SALIDA.exists():
        shutil.rmtree(SALIDA)
    for e in ENTIDADES:
        c = construir(e)
        print(f"  {e['carpeta']:<15} {e['pais']}  {len(c['esperado']):>3} señales sembradas" + (" · control" if not c["siembra"] else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
