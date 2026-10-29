#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El material de prueba de la familia EA: la oficina de un ejecutivo, con su clave.

    python3 tests/criterio-ea/generar.py          escribe tests/criterio-ea/material/

Cada oficina trae su agenda exportada en .ics, las sesiones de sus órganos —convocatoria,
material, notas y acta— y su correspondencia guardada en .eml, con defectos sembrados a
propósito. La clave dice qué señales tiene que levantar el motor y qué tiene que extraer la
agente a cada ficha. Las oficinas de control no traen ningún defecto: cualquier señal en ellas es
una falla.

Además de las señales, el material prueba las reglas de la operación real (ADR 0012): una
reunión semanal en otra zona horaria que solo se cruza después del cambio de hora, un evento
libre y uno cancelado que no cruzan, una agenda vieja que no da cruces, un borrador puesto en
`40-acta/` que no cuenta como acta y una carpeta excluida que no se procesa.

**El lote: la muestra que pide el piso.** Cada oficina de industria trae además un lote de las
señales que se repiten —el acuerdo sin responsable o sin fecha, el compromiso vencido o movido, la
decisión con su plazo cerca, el correo sin respuesta, el cruce de la agenda y la sesión sin acta—,
casi todas en una sesión más del comité, con su acta firmada. Así el material siembra 73 señales o
más: lo que pide un piso del 95 % sin fallas (decisión 0020).

Nada de esto pertenece a una organización: los nombres, las cifras y las personas los escribe
este archivo. El material sale igual byte a byte cada vez.
"""
from __future__ import annotations

import datetime as dt
import json
import shutil
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent.parent
SALIDA = AQUI / "material"
HOY = dt.date(2026, 10, 26)

CABECERA_ICS = "BEGIN:VCALENDAR\r\nVERSION:2.0\r\nPRODID:-//Criterio//Material de prueba//ES\r\nCALSCALE:GREGORIAN\r\n"


def vevent(uid, resumen, ini, fin, tz=None, extra=""):
    p = f";TZID={tz}" if tz else ""
    return (f"BEGIN:VEVENT\r\nUID:{uid}\r\nDTSTAMP:20261025T120000Z\r\nSUMMARY:{resumen}\r\n"
            f"DTSTART{p}:{ini}\r\nDTEND{p}:{fin}\r\n{extra}END:VEVENT\r\n")


def eml(mid, de, para, fecha, asunto, cuerpo, responde=None):
    r = f"In-Reply-To: {responde}\nReferences: {responde}\n" if responde else ""
    return (f"Message-ID: {mid}\n{r}From: {de}\nTo: {para}\nDate: {fecha}\nSubject: {asunto}\n"
            "MIME-Version: 1.0\nContent-Type: text/plain; charset=utf-8\nContent-Transfer-Encoding: 8bit\n\n" + cuerpo + "\n")


def escribir(p: Path, texto: str) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(texto.encode("utf-8"))


def oficina(o: dict) -> dict:
    """Una oficina: escribe sus documentos y devuelve su clave."""
    base = SALIDA / o["carpeta"]
    docs_rel = f"direccion/{o['ejecutivo_slug']}"
    docs = base / docs_rel
    s = set(o["siembra"])
    esperado: list[tuple[str, str]] = []
    reuniones, correspondencia = {}, {}
    tz = o["tz"]
    dom = o["dominio"]

    # La referencia: los órganos que se siguen.
    escribir(docs / "00-referencia" / "organos.csv",
             "organo;integrantes;calendario\n" + "".join(f"{x};{y};{z}\n" for x, y, z in o["organos"]))

    # La ficha de la oficina: lo que el setup propone a partir de los documentos.
    excl = "\nNo se procesa: 20-correspondencia/personal (asuntos personales del ejecutivo).\n" if "carpeta_excluida" in s else ""
    escribir(docs / "00-referencia" / "oficina.md",
             f"# La oficina de {o['ejecutivo'].lower()} · {o['nombre']}\n\nEjecutivo: {o['ejecutivo']}.\n"
             f"Asiste: {o['personas'][4]}.\nCorreo de la oficina: presidencia@{dom}\nZona horaria de la agenda: {tz}\n{excl}")

    # La agenda exportada.
    ev = [
        vevent(f"comite-{o['n']}", "Comité de presidencia", "20261019T080000", "20261019T093000", tz, "RRULE:FREQ=WEEKLY;COUNT=10\r\n"),
        vevent(f"bloque-{o['n']}", "Bloque de concentración", "20261027T080000", "20261027T120000", tz, "TRANSP:TRANSPARENT\r\n"),
        vevent(f"feriado-{o['n']}", "Día sin reuniones", "20261102", "20261103", None, ""),
        vevent(f"cancelada-{o['n']}", "Visita al centro de datos", "20261028T100000", "20261028T113000", tz, "STATUS:CANCELLED\r\n"),
        vevent(f"junta-{o['n']}", "Sesión de la junta", "20261029T140000", "20261029T170000", tz),
        vevent(f"almuerzo-{o['n']}", "Almuerzo con el comité de auditoría", "20261030T123000", "20261030T140000", tz),
    ]
    if "cruce_directo" in s:
        ev.append(vevent(f"regulador-{o['n']}", "Visita del supervisor", "20261029T153000", "20261029T163000", tz))
        a, b = sorted([f"junta-{o['n']}", f"regulador-{o['n']}"])
        esperado.append(("meeting_conflict", f"cruce:2026-10-29:{a}|{b}"))
    if "cruce_cambio_de_hora" in s:
        # 9:00 en Nueva York: 8:00 en Bogotá antes del 1 de noviembre y 9:00 después. Solo cruza
        # la revisión de las 9:00 del martes 3 de noviembre.
        ev.append(vevent(f"matriz-{o['n']}", "Llamada con la casa matriz", "20261020T090000", "20261020T100000", "America/New_York",
                         "RRULE:FREQ=WEEKLY;COUNT=6\r\n"))
        ev.append(vevent(f"tesoreria-{o['n']}", "Revisión con tesorería", "20261020T090000", "20261020T093000", tz, "RRULE:FREQ=WEEKLY;COUNT=6\r\n"))
        a, b = sorted([f"matriz-{o['n']}", f"tesoreria-{o['n']}"])
        esperado.append(("meeting_conflict", f"cruce:2026-11-03:{a}|{b}"))
    for j in range((o.get("lote") or {}).get("cruce", 0)):   # el lote: dos reuniones que se cruzan, un día distinto cada una
        dia = ["20261104", "20261105", "20261106", "20261103"][j]
        x, y = f"cruce-a{j + 1}-{o['n']}", f"cruce-b{j + 1}-{o['n']}"
        ev.append(vevent(x, f"Reunión con la firma auditora {j + 1}", f"{dia}T150000", f"{dia}T160000", tz))
        ev.append(vevent(y, f"Visita del cliente {j + 1}", f"{dia}T153000", f"{dia}T163000", tz))
        a, b = sorted([x, y])
        esperado.append(("meeting_conflict", f"cruce:{dia[:4]}-{dia[4:6]}-{dia[6:]}:{a}|{b}"))
    fecha_exp = "2026-10-12" if "agenda_vieja" in s else "2026-10-25"
    if "agenda_vieja" in s:
        # Una agenda vieja con un cruce: el motor avisa y no lo cuenta.
        ev.append(vevent(f"viejo-{o['n']}", "Reunión que se cruza en la agenda vieja", "20261029T150000", "20261029T160000", tz))
    escribir(docs / "10-agenda" / f"agenda-{fecha_exp}.ics", CABECERA_ICS + "".join(ev) + "END:VCALENDAR\r\n")

    def sesion(organo, fecha, convocatoria=True, material=True, notas=None, acta=None, borrador_en_acta=False):
        d = docs / "organos" / organo / fecha
        if convocatoria:
            escribir(d / "10-convocatoria" / "orden-del-dia.md",
                     f"# {organo.replace('-', ' ').capitalize()} · sesión del {fecha}\n\n1. Verificación del quórum.\n2. Informe de la presidencia.\n3. Asuntos que piden decisión.\n4. Proposiciones y varios.\n")
        if material:
            escribir(d / "20-material" / "informe-de-gestion.md", f"# Informe de gestión para la sesión del {fecha}\n\nResultados del periodo y avance de los proyectos.\n")
        if notas:
            escribir(d / "30-notas" / "notas.md", notas)
        if acta:
            escribir(d / "40-acta" / "acta-firmada.md", acta)
        if borrador_en_acta:
            escribir(d / "40-acta" / "acta-BORRADOR.md", "BORRADOR — no es el acta\n\nAcuerdos por confirmar.\n")
        return f"organos/{organo}/{fecha}"

    # La junta pasada: el acta firmada con sus acuerdos, compromisos y decisiones.
    org = o["organos"][0][0]
    f_ant = "2026-09-24"
    ruta_acta = f"organos/{org}/{f_ant}/40-acta/acta-firmada.md"
    p = o["personas"]
    acuerdos = [
        {"id": "A-1", "what": "Aprobar los estados financieros de agosto", "who": p[1], "due": "2026-10-15", "source": f"{ruta_acta}, línea 9"},
        {"id": "A-2", "what": "Actualizar la política de viajes", "who": None if "acuerdo_sin_responsable" in s else p[2],
         "due": "2026-11-30", "source": f"{ruta_acta}, línea 10"},
        {"id": "A-3", "what": "Contratar la auditoría del sistema de pagos", "who": p[1],
         "due": None if "acuerdo_sin_fecha" in s else "2026-12-15", "source": f"{ruta_acta}, línea 11"},
    ]
    k_ant = f"{org}:{f_ant}"
    if "acuerdo_sin_responsable" in s:
        esperado.append(("agreement_without_owner", f"acuerdo-responsable:{k_ant}:A-2"))
    if "acuerdo_sin_fecha" in s:
        esperado.append(("agreement_without_date", f"acuerdo-fecha:{k_ant}:A-3"))
    compromisos = [
        {"id": "C-1", "who": p[3], "what": "Presentar el informe de cartera vencida", "due_date": "2026-10-15",
         "original_due_date": "2026-10-15", "reschedules": [], "state": "open" if "compromiso_vencido" in s else "met",
         "evidence": None if "compromiso_vencido" in s else f"organos/{org}/{f_ant}/20-material/informe-de-gestion.md",
         "source": f"{ruta_acta}, línea 14"},
        {"id": "C-2", "who": p[1], "what": "Entregar el plan de continuidad del negocio", "due_date": "2026-11-20",
         "original_due_date": "2026-09-30",
         "reschedules": ([{"due_date": "2026-10-15", "source": f"{ruta_acta}, línea 15"},
                          {"due_date": "2026-10-30", "source": f"{ruta_acta}, línea 15"},
                          {"due_date": "2026-11-20", "source": f"{ruta_acta}, línea 15"}] if "compromiso_movido" in s else
                         [{"due_date": "2026-11-20", "source": f"{ruta_acta}, línea 15"}]),
         "state": "open", "evidence": None, "source": f"{ruta_acta}, línea 15"},
    ]
    if "compromiso_vencido" in s:
        esperado.append(("commitment_overdue", f"compromiso:{k_ant}:C-1"))
    if "compromiso_movido" in s:
        esperado.append(("commitment_rescheduled", f"reprogramado:{k_ant}:C-2"))
    plazo_d1 = "2026-11-02" if "decision_con_plazo" in s else "2026-12-18"
    if "decision_con_plazo" in s:
        esperado.append(("decision_deadline", f"decision:{k_ant}:D-1"))
    mat = f"organos/{org}/{f_ant}/20-material"
    decisiones = [
        # La decisión como la escribe el material (decision-brief), no el acta que la aplaza (EA-4).
        {"id": "D-1", "decision": "Proveedor del centro de datos alterno", "source": f"{mat}/propuesta-centro-de-datos.md",
         "options": [{"option": "Renovar con el proveedor actual", "evidence": [{"archivo": f"{mat}/propuesta-centro-de-datos.md"}]},
                     {"option": "Abrir una licitación", "evidence": [{"archivo": f"{mat}/propuesta-centro-de-datos.md"}]}],
         "missing": ["La oferta económica de la licitación"],
         "deadline": plazo_d1, "deadline_source": f"{mat}/propuesta-centro-de-datos.md, línea 3", "status": "pending"},
    ]
    nombre_r = lambda x: x or "sin responsable en el acta"  # noqa: E731
    acta = "\n".join([
        f"# Acta de la sesión de {org.replace('-', ' ')} del {f_ant}",
        "",
        f"Asistentes: {', '.join(p[:4])}.",
        "Quórum verificado.",
        "",
        "## Acuerdos",
        "",
        "Se aprobó, por unanimidad:",
        f"1. Aprobar los estados financieros de agosto. Responsable: {nombre_r(acuerdos[0]['who'])}. Fecha: {acuerdos[0]['due']}.",
        f"2. Actualizar la política de viajes. Responsable: {nombre_r(acuerdos[1]['who'])}. Fecha: {acuerdos[1]['due']}.",
        f"3. Contratar la auditoría del sistema de pagos. Responsable: {nombre_r(acuerdos[2]['who'])}. Fecha: {acuerdos[2]['due'] or 'por definir'}.",
        "",
        "## Compromisos",
        f"- {p[3]} presentará el informe de cartera vencida el 2026-10-15.",
        (f"- {p[1]} entregará el plan de continuidad del negocio. Comprometido para el 2026-09-30, se movió al 2026-10-15, luego al 2026-10-30 y hoy queda para el 2026-11-20."
         if "compromiso_movido" in s else f"- {p[1]} entregará el plan de continuidad del negocio. Comprometido para el 2026-09-30, queda para el 2026-11-20."),
        "",
        "## Decisiones pendientes",
        "- Proveedor del centro de datos alterno: el material plantea renovar con el proveedor actual o abrir una licitación. Se decide en la próxima sesión.",
        "",
        f"Firmada por {p[0]}, presidente de la sesión, y {p[4]}, secretaria.",
        "",
    ])
    sesion(org, f_ant, acta=acta)
    escribir(docs / mat / "propuesta-centro-de-datos.md",
             "# Propuesta: proveedor del centro de datos alterno\n\n"
             f"La oferta del proveedor actual vence el {plazo_d1}.\n\n"
             "Opción 1 · Renovar con el proveedor actual, por tres años.\n"
             "Opción 2 · Abrir una licitación con al menos tres oferentes.\n\n"
             "La oferta económica de la licitación no está disponible todavía.\n")
    if "compromiso_vencido" not in s:
        escribir(docs / f"organos/{org}/{f_ant}/20-material/informe-de-gestion.md",
                 f"# Informe de gestión para la sesión del {f_ant}\n\nIncluye el informe de cartera vencida presentado por {p[3]} el 2026-10-14.\n")
    reuniones[f"{org}-{f_ant}"] = {"organ": org, "date": f_ant, "agreements": acuerdos, "commitments": compromisos, "decisions": decisiones}

    # La próxima junta: el material a tres días.
    f_prox = "2026-10-29"
    sesion(org, f_prox, material="sin_material" not in s)
    if "sin_material" in s:
        esperado.append(("meeting_without_material", f"material:{org}:{f_prox}"))

    # El comité: una sesión vieja sin acta y una reciente que todavía está en plazo.
    com = o["organos"][1][0]
    notas = f"Notas de la sesión.\n\n- {p[2]} revisará los indicadores de servicio para el 2026-11-06.\n"
    f_vieja = "2026-09-21"
    if "sin_acta" in s or "borrador_en_acta" in s:
        sesion(com, f_vieja, notas=notas, borrador_en_acta="borrador_en_acta" in s)
        esperado.append(("meeting_without_minutes", f"acta:{com}:{f_vieja}"))
    else:
        acta_c = (f"# Acta de la sesión de {com.replace('-', ' ')} del {f_vieja}\n\nAsistentes: {', '.join(p[:3])}.\n\n## Acuerdos\n\n"
                  f"1. Publicar el calendario de comités de 2027. Responsable: {p[2]}. Fecha: 2026-12-01.\n\nFirmada por {p[0]}.\n")
        sesion(com, f_vieja, notas=notas, acta=acta_c)
        reuniones[f"{com}-{f_vieja}"] = {"organ": com, "date": f_vieja, "agreements": [
            {"id": "A-1", "what": "Publicar el calendario de comités de 2027", "who": p[2], "due": "2026-12-01",
             "source": f"organos/{com}/{f_vieja}/40-acta/acta-firmada.md, línea 7"}], "commitments": [], "decisions": []}
    sesion(com, "2026-10-19", notas=notas)

    # La correspondencia.
    corr = docs / "20-correspondencia"
    oficina_mail = f"presidencia@{dom}"
    def guardar(nombre, texto):
        escribir(corr / nombre, texto)

    # El lote: una sesión más del comité, con su acta firmada, y lo que se repite en ella.
    lote = o.get("lote") or {}
    if lote:
        f_l = "2026-10-05"
        k_l = f"{com}:{f_l}"
        ruta_l = f"organos/{com}/{f_l}/40-acta/acta-firmada.md"
        mat_l = f"organos/{com}/{f_l}/20-material"
        temas = ["Renovar las pólizas de la sede", "Publicar el informe de sostenibilidad", "Actualizar el manual de compras",
                 "Revisar el tablero de indicadores", "Cerrar el proyecto de nómina", "Definir el plan de capacitación",
                 "Ajustar el presupuesto de mercadeo", "Contratar la consultoría de procesos", "Migrar el archivo documental"]
        lineas = [f"# Acta de la sesión de {com.replace('-', ' ')} del {f_l}", "", f"Asistentes: {', '.join(p[:4])}.", "Quórum verificado.",
                  "", "## Acuerdos", ""]
        ag, cm, dc = [], [], []
        n = 0
        for tipo in ("sin_responsable", "sin_fecha"):
            for j in range(lote.get(f"acuerdo_{tipo}", 0)):
                n += 1
                qu, quien, cuando = temas[(n - 1) % len(temas)], None if tipo == "sin_responsable" else p[1 + n % 3], None if tipo == "sin_fecha" else "2026-12-10"
                lineas.append(f"{n}. {qu}. Responsable: {quien or 'sin responsable en el acta'}. Fecha: {cuando or 'por definir'}.")
                ag.append({"id": f"A-{n}", "what": qu, "who": quien, "due": cuando, "source": f"{ruta_l}, línea {len(lineas)}"})
                esperado.append(("agreement_without_owner" if tipo == "sin_responsable" else "agreement_without_date",
                                 f"acuerdo-{'responsable' if tipo == 'sin_responsable' else 'fecha'}:{k_l}:A-{n}"))
        lineas += ["", "## Compromisos"]
        c = 0
        for j in range(lote.get("compromiso_vencido", 0)):
            c += 1
            due = f"2026-10-{12 + j:02d}"
            quien, qu = p[1 + c % 4], f"Entregar el informe {c} de seguimiento"
            lineas.append(f"- {quien} se compromete a {qu.lower()} el {due}.")
            cm.append({"id": f"C-{c}", "who": quien, "what": qu, "due_date": due, "original_due_date": due, "reschedules": [],
                       "state": "open", "evidence": None, "source": f"{ruta_l}, línea {len(lineas)}"})
            esperado.append(("commitment_overdue", f"compromiso:{k_l}:C-{c}"))
        for j in range(lote.get("compromiso_movido", 0)):
            c += 1
            quien, qu = p[1 + c % 4], f"Presentar el plan {c} de mejora"
            lineas.append(f"- {quien} presentará {qu[9:].lower()}. Comprometido para el 2026-09-15, se movió al 2026-09-30, luego al "
                          f"2026-10-20 y hoy queda para el 2026-12-{4 + j:02d}.")
            fuente = f"{ruta_l}, línea {len(lineas)}"
            cm.append({"id": f"C-{c}", "who": quien, "what": qu, "due_date": f"2026-12-{4 + j:02d}", "original_due_date": "2026-09-15",
                       "reschedules": [{"due_date": "2026-09-30", "source": fuente}, {"due_date": "2026-10-20", "source": fuente},
                                       {"due_date": f"2026-12-{4 + j:02d}", "source": fuente}],
                       "state": "open", "evidence": None, "source": fuente})
            esperado.append(("commitment_rescheduled", f"reprogramado:{k_l}:C-{c}"))
        lineas += ["", "## Decisiones pendientes"]
        for j in range(lote.get("decision_con_plazo", 0)):
            plazo, doc = f"2026-11-{3 + j:02d}", f"{mat_l}/propuesta-{j + 1}.md"
            asunto = ["Proveedor de la mesa de ayuda", "Sede de la oficina regional", "Aseguradora de la flota"][j % 3]
            lineas.append(f"- {asunto}: el material plantea dos opciones. Se decide antes del {plazo}.")
            escribir(docs / doc, f"# Propuesta: {asunto.lower()}\n\nLa decisión vence el {plazo}.\n\nOpción 1 · Continuar como hoy.\n"
                                 "Opción 2 · Cambiar de proveedor.\n")
            dc.append({"id": f"D-{j + 1}", "decision": asunto, "source": doc,
                       "options": [{"option": "Continuar como hoy", "evidence": [{"archivo": doc}]},
                                   {"option": "Cambiar de proveedor", "evidence": [{"archivo": doc}]}],
                       "missing": [], "deadline": plazo, "deadline_source": f"{doc}, línea 3", "status": "pending"})
            esperado.append(("decision_deadline", f"decision:{k_l}:D-{j + 1}"))
        lineas += ["", f"Firmada por {p[0]}, presidente de la sesión, y {p[4]}, secretaria.", ""]
        sesion(com, f_l, acta="\n".join(lineas))
        reuniones[f"{com}-{f_l}"] = {"organ": com, "date": f_l, "agreements": ag, "commitments": cm, "decisions": dc}
        # Las sesiones extraordinarias del comité que no tienen acta firmada pasados quince días.
        for j in range(lote.get("sin_acta", 0)):
            f_s = f"2026-09-{25 + j * 2:02d}"
            sesion(com, f_s, notas=f"Notas de la sesión extraordinaria del {f_s}.\n")
            esperado.append(("meeting_without_minutes", f"acta:{com}:{f_s}"))
        # Los correos que piden respuesta, con el plazo vencido y sin respuesta.
        for j in range(lote.get("correo_sin_respuesta", 0)):
            stem = f"2026-10-{14 + j:02d}-solicitud-{j + 1}"
            guardar(f"{stem}.eml", eml(f"<sol{j + 1}@proveedor.test>", "Proveedor <ventas@proveedor.test>", oficina_mail,
                    f"Wed, {14 + j:02d} Oct 2026 09:00:00 -0500", f"Solicitud {j + 1}: confirmación de condiciones",
                    f"Buenos días:\n\nLes agradecemos confirmar las condiciones del contrato {j + 1} antes del 2026-10-{20 + j:02d}.\n\nGracias."))
            correspondencia[stem] = {"file": f"20-correspondencia/{stem}.eml", "asks_reply": True, "due": f"2026-10-{20 + j:02d}", "routine": False}
            esperado.append(("correspondence_unanswered", f"correo:{stem}"))
    guardar("2026-10-08-supervisor.eml", eml(f"<req45@supervisor.test>", "Oficios <oficios@supervisor.test>", oficina_mail,
            "Thu, 08 Oct 2026 09:00:00 -0500", "Requerimiento 45: cartera reestructurada",
            "Señor presidente:\n\nSolicitamos el detalle de la cartera reestructurada del tercer trimestre.\n"
            "La respuesta debe llegar a más tardar el 2026-10-20.\n\nAtentamente,\nDirección de supervisión"))
    correspondencia["2026-10-08-supervisor"] = {"file": "20-correspondencia/2026-10-08-supervisor.eml", "asks_reply": True,
                                               "due": "2026-10-20", "routine": False}
    if "correo_sin_respuesta" not in s:
        guardar("2026-10-19-respuesta-supervisor.eml", eml(f"<r-req45@{dom}>", oficina_mail, "oficios@supervisor.test",
                "Mon, 19 Oct 2026 16:00:00 -0500", "Re: Requerimiento 45: cartera reestructurada",
                "Adjuntamos el detalle solicitado.", responde="<req45@supervisor.test>"))
    else:
        esperado.append(("correspondence_unanswered", "correo:2026-10-08-supervisor"))
    guardar("2026-10-12-cliente.eml", eml("<cita1@cliente.test>", "Gerencia <gerencia@cliente.test>", oficina_mail,
            "Mon, 12 Oct 2026 10:00:00 -0500", "Solicitud de reunión",
            "Buenos días:\n\nQuisiéramos una reunión con el presidente. Les agradecemos confirmar antes del 2026-10-16.\n\nGracias."))
    guardar("2026-10-13-respuesta-cliente.eml", eml(f"<r-cita1@{dom}>", oficina_mail, "gerencia@cliente.test",
            "Tue, 13 Oct 2026 09:00:00 -0500", "Re: Solicitud de reunión", "Con gusto. Les proponemos el 2026-10-22 a las 10:00.",
            responde="<cita1@cliente.test>"))
    # Pedir una reunión con el ejecutivo no es una cita ya aprobada: no es rutinario (EA-4).
    correspondencia["2026-10-12-cliente"] = {"file": "20-correspondencia/2026-10-12-cliente.eml", "asks_reply": True,
                                            "due": "2026-10-16", "routine": False}
    guardar("2026-10-21-boletin.eml", eml("<bol88@gremio.test>", "Boletín <boletin@gremio.test>", oficina_mail,
            "Wed, 21 Oct 2026 07:00:00 -0500", "Boletín semanal del gremio", "Para su conocimiento: las cifras del sector de septiembre."))
    correspondencia["2026-10-21-boletin"] = {"file": "20-correspondencia/2026-10-21-boletin.eml", "asks_reply": False, "due": None, "routine": False}
    if "carpeta_excluida" in s:
        # Lo personal del ejecutivo: excluido, aunque pida respuesta con el plazo vencido.
        escribir(corr / "personal" / "2026-10-01-colegio.eml", eml("<col1@colegio.test>", "colegio@colegio.test", oficina_mail,
                 "Thu, 01 Oct 2026 08:00:00 -0500", "Reunión de padres", "Por favor confirmar antes del 2026-10-05."))
    (docs / "90-borradores").mkdir(parents=True, exist_ok=True)
    escribir(docs / "90-borradores" / "LEEME.txt", "Aquí deja Ofelia sus borradores, con BORRADOR en el nombre.\n")

    cfg = {"entity": {"name": o["nombre"], "country": o["pais"]},
           "executive": {"name": o["ejecutivo"]}, "timezone": tz, "office_emails": [oficina_mail],
           "excluded_folders": ["20-correspondencia/personal"] if "carpeta_excluida" in s else [],
           "publish_rostrum": False,
           "paths": {"documents": docs_rel, "state": f"estado-direccion/{o['ejecutivo_slug']}"}}
    # La extracción esperada: lo que la agente lleva a cada ficha. Sin el orden del día ni el
    # texto de las opciones más allá de lo que el documento dice tal cual.
    clave = {"entidad": o["nombre"], "industria": o["industria"], "pais": o["pais"], "hoy": HOY.isoformat(),
             "siembra": sorted(s), "config": {"ofelia": cfg},
             "extraccion": {"reuniones": reuniones, "correspondencia": correspondencia},
             "esperado": [{"signal": a, "key": b} for a, b in sorted(esperado)]}
    (base / "clave.json").write_text(json.dumps(clave, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return clave


OFICINAS = [
    {"carpeta": "banca", "industria": "banca", "pais": "CO", "id": "900123456", "nombre": "Banco Andino", "n": 1,
     "ejecutivo": "Presidencia", "ejecutivo_slug": "presidencia", "tz": "America/Bogota", "dominio": "bancoandino.test",
     "organos": [("junta-directiva", "Nueve miembros", "último jueves de cada mes"), ("comite-de-presidencia", "Los vicepresidentes", "lunes")],
     "personas": ("Marta Ríos", "Andrés Vela", "Diana Cruz", "Felipe Duarte", "Laura Gómez"),
     "siembra": ["cruce_directo", "cruce_cambio_de_hora", "sin_material", "sin_acta", "acuerdo_sin_responsable", "acuerdo_sin_fecha",
                 "compromiso_vencido", "compromiso_movido", "decision_con_plazo", "correo_sin_respuesta"],
     "lote": {"acuerdo_sin_responsable": 6, "acuerdo_sin_fecha": 5, "compromiso_vencido": 6, "compromiso_movido": 3,
              "decision_con_plazo": 2, "correo_sin_respuesta": 5, "cruce": 4}},
    {"carpeta": "cooperativas", "industria": "cooperativas", "pais": "EC", "id": "1790012345001", "nombre": "Cooperativa Sierra Alta", "n": 2,
     "ejecutivo": "Gerencia general", "ejecutivo_slug": "gerencia-general", "tz": "America/Guayaquil", "dominio": "sierraalta.test",
     "organos": [("consejo-de-administracion", "Siete vocales", "tercer jueves de cada mes"), ("comite-de-gerencia", "Las jefaturas", "lunes")],
     "personas": ("Patricio Andrade", "Gabriela Mora", "Esteban Jácome", "Verónica Paz", "Rosa Quishpe"),
     "siembra": ["agenda_vieja", "borrador_en_acta", "acuerdo_sin_responsable", "compromiso_vencido", "correo_sin_respuesta", "carpeta_excluida"],
     "lote": {"acuerdo_sin_responsable": 6, "acuerdo_sin_fecha": 6, "compromiso_vencido": 6, "compromiso_movido": 3,
              "decision_con_plazo": 2, "correo_sin_respuesta": 5, "sin_acta": 3}},
    {"carpeta": "control-co", "industria": "retail", "pais": "CO", "id": "900000001", "nombre": "Distribuidora Control", "n": 3,
     "ejecutivo": "Gerencia general", "ejecutivo_slug": "gerencia-general", "tz": "America/Bogota", "dominio": "control.test",
     "organos": [("junta-directiva", "Cinco miembros", "último jueves de cada mes"), ("comite-de-gerencia", "Las direcciones", "lunes")],
     "personas": ("Elena Duarte", "Jorge Silva", "Natalia Rincón", "Camilo Prieto", "Sara León"), "siembra": []},
    {"carpeta": "control-ec", "industria": "cooperativas", "pais": "EC", "id": "1790000001001", "nombre": "Comercial Control", "n": 4,
     "ejecutivo": "Presidencia", "ejecutivo_slug": "presidencia", "tz": "America/Guayaquil", "dominio": "controlec.test",
     "organos": [("directorio", "Cinco directores", "último jueves de cada mes"), ("comite-ejecutivo", "Las gerencias", "lunes")],
     "personas": ("Fernanda Vaca", "Diego Herrera", "Paola Cevallos", "Iván Torres", "Mónica Ruiz"), "siembra": []},
]


def main() -> int:
    if SALIDA.exists():
        shutil.rmtree(SALIDA)
    total = 0
    for o in OFICINAS:
        c = oficina(o)
        total += len(c["esperado"])
        print(f"  {o['carpeta']:13} {o['pais']}  {len(o['siembra']):2} defectos sembrados · {len(c['esperado']):2} señales esperadas")
    print(f"\n  {len(OFICINAS)} oficinas, {total} señales en la clave, en {SALIDA.relative_to(RAIZ)}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
