#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El material de prueba de la familia CRO: un banco en Colombia, una aseguradora en el Perú, una
cooperativa de crédito en Brasil y dos entidades de control.

    python3 tests/criterio-cro/generar.py          escribe tests/criterio-cro/material/

Cada entidad trae su carpeta de riesgos al 25 de noviembre de 2026, con octubre como el último periodo
cerrado: la declaración de apetito, la política de riesgo operacional, la matriz de riesgos, los límites y
los indicadores clave en `00-marco/`; la exposición de octubre y los planes de acción en
`10-exposicion/`; los valores de los indicadores y sus acciones en `20-indicadores/`; la base de eventos
de pérdida en `30-eventos/`; y el acta del comité de riesgos de octubre en `40-actas/`. La cooperativa de
Brasil trae sus documentos y sus columnas en portugués.

**La clave la escribe este archivo, no el motor.** Cada defecto se siembra a propósito y su señal esperada
queda escrita en `clave.json`, junto con lo que el agente tendría que extraer de los documentos escritos
—la fecha en que la junta revisó la declaración, el exceso que aprobó el comité y la acción que acordó
sobre un indicador— y la configuración que deja el setup. El motor no la ve; `evaluar.py` compara lo que
el motor levanta contra ella, y una señal de más cuenta igual que una de menos.

**Las entidades de control no tienen ningún defecto**, y sí los casos que se parecen a uno: un límite
excedido con su plan de acción, otro excedido con el exceso aprobado en el acta, un límite mínimo que la
exposición supera por arriba, un reporte que llega el último día del plazo, un límite que se revisa el mes
que viene, un riesgo alto medido solo por un indicador, un riesgo medio sin límite, un indicador en alerta
con la acción en el acta, otro en alerta con la acción en la tabla, otro justo fuera de su alerta, un
evento registrado el último día del plazo, el mismo tipo de evento en otro proceso y dos eventos iguales
con uno fuera de la ventana. Todo es determinista: el mismo material cada vez, byte a byte. Los nombres,
las empresas y los documentos son inventados.
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
METODO = {"report_days": 10, "statement_review_months": 12, "registration_days": 30, "repeat_window_months": 12}
TODAS = {"exceso", "dueno", "revision", "tarde_reporte", "sin_limite", "declaracion",
         "alerta", "sin_reporte", "incompleto", "tarde_evento", "repetido", "sin_riesgo"}

ENTIDADES = [
    {"carpeta": "banca-co", "industria": "banca", "pais": "CO", "id": "901777333", "nombre": "Banco Andino Sintético", "moneda": "COP", "lengua": "es",
     "siembra": set(TODAS)},
    {"carpeta": "seguros-pe", "industria": "seguros", "pais": "PE", "id": "20607773331", "nombre": "Seguros del Sur Sintética", "moneda": "PEN", "lengua": "es",
     "siembra": {"exceso", "revision", "sin_limite", "alerta", "incompleto", "repetido"}},
    {"carpeta": "cooperativa-br", "industria": "cooperativa", "pais": "BR", "id": "12345678000190", "nombre": "Cooperativa Vale Sintética", "moneda": "BRL",
     "lengua": "pt", "siembra": {"dueno", "tarde_reporte", "declaracion", "sin_reporte", "tarde_evento", "sin_riesgo"}},
    {"carpeta": "control-co", "industria": "banca", "pais": "CO", "id": "901888444", "nombre": "Banco Control de Riesgos Sintético", "moneda": "COP",
     "lengua": "es", "siembra": set()},
    {"carpeta": "control-br", "industria": "cooperativa", "pais": "BR", "id": "98765432000110", "nombre": "Cooperativa Controle Sintética", "moneda": "BRL",
     "lengua": "pt", "siembra": set()},
]

# Lo que cambia entre el español y el portugués: los nombres de los archivos, las columnas y los valores.
T = {
    "es": {
        "matriz": ("matriz_de_riesgos.xlsx", ["Riesgo", "Nombre", "Calificación", "Proceso", "Dueño"]),
        "limites": ("limites.xlsx", ["Límite", "Riesgo", "Métrica", "Valor del límite", "Sentido", "Dueño", "Próxima revisión", "Unidad"]),
        "indicadores": ("indicadores_clave.xlsx", ["Indicador", "Nombre", "Riesgo", "Umbral de alerta", "Umbral de límite", "Sentido", "Dueño"]),
        "exposicion": ("exposicion_2026-10.xlsx", ["Límite", "Exposición", "Periodo", "Fecha de reporte", "Área"]),
        "planes": ("planes_de_accion.xlsx", ["Límite", "Plan de acción", "Responsable", "Fecha compromiso"]),
        "valores": ("valores_indicadores_2026-10.xlsx", ["Indicador", "Periodo", "Valor"]),
        "acciones": ("acciones_indicadores.xlsx", ["Indicador", "Periodo", "Acción", "Responsable"]),
        "eventos": ("base_de_eventos.xlsx", ["Evento", "Fecha de ocurrencia", "Fecha de descubrimiento", "Fecha de registro", "Proceso", "Tipo",
                                             "Causa", "Monto", "Riesgo"]),
        "declaracion": "declaracion_de_apetito.pdf", "politica": "politica_de_riesgo_operacional.pdf", "acta": "acta_comite_riesgos_2026-10.pdf",
        "alto": "Alto", "critico": "Crítico", "medio": "Medio", "max": "Máximo", "min": "Mínimo", "mayor": "Mayor", "menor": "Menor",
        "riesgos": {"R-01": ("Riesgo de crédito de consumo", "Crédito", "Vicepresidencia de crédito"), "R-02": ("Riesgo de liquidez", "Tesorería", "Tesorería"),
                    "R-03": ("Fraude externo en canales", "Canales", "Operaciones"), "R-04": ("Continuidad del negocio", "Tecnología", "Tecnología"),
                    "R-05": ("Riesgo reputacional", "Mercadeo", "Mercadeo"), "R-06": ("Riesgo de contraparte", "Tesorería", "Tesorería")},
        "metricas": {"L-01": "Cartera vencida de consumo", "L-02": "Indicador de cobertura de liquidez", "L-03": "Concentración en el mayor deudor",
                     "L-04": "Pérdidas por fraude externo sobre ingresos", "L-05": "Exposición a contrapartes sin calificación"},
        "kri": {"KRI-01": "Transacciones fraudulentas por millón", "KRI-02": "Disponibilidad de los canales digitales",
                "KRI-03": "Rotación del personal de crédito", "KRI-04": "Días sin una prueba del plan de continuidad",
                "KRI-05": "Concentración de los depósitos en los 20 mayores"},
        "procesos": {"canales": "Canales", "sucursales": "Sucursales", "tesoreria": "Tesorería", "mercadeo": "Mercadeo", "tecnologia": "Tecnología",
                     "credito": "Crédito"},
        "tipos": {"fraude": "Fraude con tarjeta", "liquidacion": "Error de liquidación", "multa": "Multa por publicidad", "caida": "Caída del canal digital",
                  "desembolso": "Error de desembolso"},
        "causas": {"fraude": "Clonación de tarjetas", "liquidacion": "Digitación de la tasa", "multa": "Pieza publicada sin revisión",
                   "caida": "Falla del proveedor de nube", "desembolso": "Cuenta de destino errada"},
        "areas": {"L-01": "Crédito", "L-02": "Tesorería", "L-03": "Crédito", "L-04": "Operaciones", "L-05": "Tesorería"},
        "planes_txt": ("Venta de cartera del mayor deudor y cupo congelado", "Vicepresidencia de crédito"),
        "accion_tabla": "Campaña de captación de depósitos minoristas",
    },
    "pt": {
        "matriz": ("matriz_de_riscos.xlsx", ["Risco", "Nome", "Classificação", "Processo", "Responsável"]),
        "limites": ("limites.xlsx", ["Limite", "Risco", "Métrica", "Valor do limite", "Sentido", "Responsável", "Próxima revisão", "Unidade"]),
        "indicadores": ("indicadores_chave.xlsx", ["Indicador", "Nome", "Risco", "Limiar de alerta", "Limiar de limite", "Sentido", "Responsável"]),
        "exposicion": ("exposicao_2026-10.xlsx", ["Limite", "Exposição", "Período", "Data do reporte", "Área"]),
        "planes": ("planos_de_acao.xlsx", ["Limite", "Plano de ação", "Responsável", "Data compromisso"]),
        "valores": ("valores_indicadores_2026-10.xlsx", ["Indicador", "Período", "Valor"]),
        "acciones": ("acoes_indicadores.xlsx", ["Indicador", "Período", "Ação", "Responsável"]),
        "eventos": ("base_de_eventos.xlsx", ["Evento", "Data de ocorrência", "Data de descoberta", "Data de registro", "Processo", "Tipo",
                                             "Causa", "Valor da perda", "Risco"]),
        "declaracion": "declaracao_de_apetite.pdf", "politica": "politica_de_risco_operacional.pdf", "acta": "ata_comite_riscos_2026-10.pdf",
        "alto": "Alto", "critico": "Crítico", "medio": "Médio", "max": "Máximo", "min": "Mínimo", "mayor": "Maior", "menor": "Menor",
        "riesgos": {"R-01": ("Risco de crédito pessoal", "Crédito", "Diretoria de crédito"), "R-02": ("Risco de liquidez", "Tesouraria", "Tesouraria"),
                    "R-03": ("Fraude externa nos canais", "Canais", "Operações"), "R-04": ("Continuidade de negócios", "Tecnologia", "Tecnologia"),
                    "R-05": ("Risco reputacional", "Marketing", "Marketing"), "R-06": ("Risco de contraparte", "Tesouraria", "Tesouraria")},
        "metricas": {"L-01": "Carteira vencida de crédito pessoal", "L-02": "Índice de liquidez de curto prazo", "L-03": "Concentração no maior devedor",
                     "L-04": "Perdas por fraude externa sobre receitas", "L-05": "Exposição a contrapartes sem rating"},
        "kri": {"KRI-01": "Transações fraudulentas por milhão", "KRI-02": "Disponibilidade dos canais digitais",
                "KRI-03": "Rotatividade da equipe de crédito", "KRI-04": "Dias sem teste do plano de continuidade",
                "KRI-05": "Concentração dos depósitos nos 20 maiores"},
        "procesos": {"canales": "Canais", "sucursales": "Agências", "tesoreria": "Tesouraria", "mercadeo": "Marketing", "tecnologia": "Tecnologia",
                     "credito": "Crédito"},
        "tipos": {"fraude": "Fraude com cartão", "liquidacion": "Erro de liquidação", "multa": "Multa por publicidade", "caida": "Queda do canal digital",
                  "desembolso": "Erro de desembolso"},
        "causas": {"fraude": "Clonagem de cartões", "liquidacion": "Digitação da taxa", "multa": "Peça publicada sem revisão",
                   "caida": "Falha do provedor de nuvem", "desembolso": "Conta de destino errada"},
        "areas": {"L-01": "Crédito", "L-02": "Tesouraria", "L-03": "Crédito", "L-04": "Operações", "L-05": "Tesouraria"},
        "planes_txt": ("Cessão da carteira do maior devedor e limite congelado", "Diretoria de crédito"),
        "accion_tabla": "Campanha de captação de depósitos de varejo",
    },
}


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


def _monto(x: float, lengua: str) -> str:
    return f"{x:,.0f}".replace(",", ".")


def construir(e: dict) -> dict:
    """La carpeta de una entidad y su clave."""
    s, t, pt = e["siembra"], T[e["lengua"]], e["lengua"] == "pt"
    raiz = SALIDA / e["carpeta"]
    nombre_carpeta = f"{e['id'].lower()}-{_norm(e['nombre']).replace('_', '-')}"
    docs = raiz / "riesgos" / nombre_carpeta
    esperado = []

    def esp(signal: str, key: str) -> None:
        esperado.append({"signal": signal, "key": key})

    # ------------------------------------------------------------ 00-marco · la declaración y la política
    revisada = "2025-08-28" if "declaracion" in s else "2026-02-26"      # hace 15 meses, o hace 9 (control)
    if "declaracion" in s:
        esp("appetite_statement_outdated", "declaracion:")
    decl = f"00-marco/{t['declaracion']}"
    if pt:
        _pdf(f"# Declaração de apetite por riscos · {e['nombre']}\n\nRevisada e aprovada pelo conselho de administração na sessão de {revisada}.\n\n"
             "O conselho revisa esta declaração pelo menos a cada 12 meses.\n\n"
             "As áreas reportam sua exposição contra cada limite nos 10 dias corridos seguintes ao fechamento de cada mês.\n\n"
             "Os limites, seu sentido e seu responsável estão na tabela de limites, que faz parte desta declaração.\n", docs / decl)
        _pdf(f"# Política de risco operacional · {e['nombre']}\n\nTodo evento de perda é registrado na base de eventos em até 30 dias corridos desde sua descoberta.\n\n"
             "Dois eventos do mesmo tipo no mesmo processo dentro de 12 meses são tratados como recorrentes.\n", docs / "00-marco" / t["politica"])
    else:
        _pdf(f"# Declaración de apetito por riesgo · {e['nombre']}\n\nRevisada y aprobada por la junta directiva en su sesión del {revisada}.\n\n"
             "La junta revisa esta declaración al menos cada 12 meses.\n\n"
             "Las áreas reportan su exposición contra cada límite dentro de los 10 días calendario siguientes al cierre de cada mes.\n\n"
             "Los límites, su sentido y su dueño están en la tabla de límites, que hace parte de esta declaración.\n", docs / decl)
        _pdf(f"# Política de riesgo operacional · {e['nombre']}\n\nTodo evento de pérdida se registra en la base de eventos dentro de los 30 días calendario "
             "siguientes a su descubrimiento.\n\nDos eventos del mismo tipo en el mismo proceso dentro de 12 meses se tratan como recurrentes.\n",
             docs / "00-marco" / t["politica"])

    # ------------------------------------------------------------ 00-marco · la matriz, los límites y los indicadores
    rs = t["riesgos"]
    calif = {"R-01": t["alto"], "R-02": t["critico"], "R-03": t["alto"], "R-04": t["alto"], "R-05": t["medio"], "R-06": t["alto"]}
    _xlsx([t["matriz"][1]] + [[r, rs[r][0], calif[r], rs[r][1], rs[r][2]] for r in sorted(rs)], docs / "00-marco" / t["matriz"][0])
    # R-04 solo lo mide KRI-04. Sembrado: KRI-04 no existe y R-04, alto, no tiene con qué medirse.
    # R-05 es medio y no tiene límite ni indicador: no es una señal.
    if "sin_limite" in s:
        esp("risk_without_limit", "riesgo:R-04")
    m = t["metricas"]
    rev_l02 = "2026-06-30" if "revision" in s else "2026-12-15"
    if "revision" in s:
        esp("limit_review_overdue", "revision:L-02")
    if "dueno" in s:
        esp("limit_without_owner", "dueno:L-02")
    lim = [t["limites"][1],
           ["L-01", "R-01", m["L-01"], 6, t["max"], rs["R-01"][2], "2027-03-31", "%"],
           ["L-02", "R-02", m["L-02"], 120, t["min"], "" if "dueno" in s else rs["R-02"][2], rev_l02, "%"],
           ["L-03", "R-01", m["L-03"], 10, t["max"], rs["R-01"][2], "2027-03-31", "%"],
           ["L-04", "R-03", m["L-04"], 0.5, t["max"], rs["R-03"][2], "2027-06-30", "%"],
           ["L-05", "R-06", m["L-05"], 15, t["max"], rs["R-06"][2], "2027-06-30", "%"]]
    _xlsx(lim, docs / "00-marco" / t["limites"][0])
    k = t["kri"]
    kri = [t["indicadores"][1],
           ["KRI-01", k["KRI-01"], "R-03", 40, 60, t["mayor"], rs["R-03"][2]],
           ["KRI-02", k["KRI-02"], "R-03", 99.5, 99, t["menor"], rs["R-04"][2]],
           ["KRI-03", k["KRI-03"], "R-01", 8, 12, t["mayor"], rs["R-01"][2]],
           ["KRI-05", k["KRI-05"], "R-02", 25, 30, t["mayor"], rs["R-02"][2]]]
    if "sin_limite" not in s:
        kri.insert(4, ["KRI-04", k["KRI-04"], "R-04", 180, 365, t["mayor"], rs["R-04"][2]])
    _xlsx(kri, docs / "00-marco" / t["indicadores"][0])

    # ------------------------------------------------------------ 10-exposicion
    # Plazo: 10 días después del 31 de octubre, el 10 de noviembre. L-02 reporta el 18 (sembrado) o el 10 (control: el último día).
    rep_l02 = "2026-11-18" if "tarde_reporte" in s else "2026-11-10"
    if "tarde_reporte" in s:
        esp("exposure_report_late", "reporte:L-02")
    if "exceso" in s:
        esp("limit_breached_without_plan", "limite:L-01")
    a = t["areas"]
    _xlsx([t["exposicion"][1],
           ["L-01", 6.4 if "exceso" in s else 5.8, PERIODO, "2026-11-06", a["L-01"]],
           ["L-02", 131, PERIODO, rep_l02, a["L-02"]],                                   # mínimo 120: 131 está dentro
           ["L-03", 11.2, PERIODO, "2026-11-05", a["L-03"]],                              # excedido, con su plan
           ["L-04", 0.62, PERIODO, "2026-11-07", a["L-04"]],                              # excedido, con el exceso aprobado en el acta
           ["L-05", 12, PERIODO, "2026-11-09", a["L-05"]]], docs / "10-exposicion" / t["exposicion"][0])
    _xlsx([t["planes"][1], ["L-03", t["planes_txt"][0], t["planes_txt"][1], "2027-01-31"]], docs / "10-exposicion" / t["planes"][0])

    # ------------------------------------------------------------ 20-indicadores
    # KRI-01 da 52, en su zona de alerta (40): la acción está en el acta, salvo donde se siembra la falta.
    # KRI-02 da 99,6, justo fuera de su alerta (99,5, menor es peor). KRI-05 da 29, en alerta, con la acción en la tabla.
    if "alerta" in s:
        esp("kri_alert_without_action", "alerta:KRI-01")
    if "sin_reporte" in s:
        esp("kri_not_reported", "reporte:KRI-03")
    val = [t["valores"][1], ["KRI-01", PERIODO, 52], ["KRI-02", PERIODO, 99.6], ["KRI-05", PERIODO, 29]]
    if "sin_reporte" not in s:
        val.insert(3, ["KRI-03", PERIODO, 6.5])
    if "sin_limite" not in s:
        val.append(["KRI-04", PERIODO, 64])
    _xlsx(val, docs / "20-indicadores" / t["valores"][0])
    _xlsx([t["acciones"][1], ["KRI-05", PERIODO, t["accion_tabla"], rs["R-02"][2]]], docs / "20-indicadores" / t["acciones"][0])

    # ------------------------------------------------------------ 30-eventos
    p, ti, ca = t["procesos"], t["tipos"], t["causas"]
    ev2 = "2026-08-02" if "repetido" in s else "2024-08-02"                 # dentro de la ventana de 12 meses, o fuera (control)
    if "repetido" in s:
        esp("loss_event_repeated", f"repetido:{_norm(p['canales'])}:{_norm(ti['fraude'])}")
    reg5 = "2026-08-20" if "tarde_evento" in s else "2026-07-31"            # 50 días, o exactamente 30 (control)
    if "tarde_evento" in s:
        esp("loss_event_registered_late", "tarde:EV-05")
    if "incompleto" in s:
        esp("loss_event_incomplete", "incompleto:EV-03")
    if "sin_riesgo" in s:
        esp("loss_event_risk_unmapped", "sin_riesgo:EV-04")
    d2 = dt.date.fromisoformat(ev2)
    ev = [t["eventos"][1],
          ["EV-01", "2026-03-10", "2026-03-12", "2026-03-20", p["canales"], ti["fraude"], ca["fraude"], 18_500_000, "R-03"],
          ["EV-02", ev2, (d2 + dt.timedelta(days=2)).isoformat(), (d2 + dt.timedelta(days=9)).isoformat(), p["canales"], ti["fraude"], ca["fraude"], 22_100_000, "R-03"],
          ["EV-03", "2026-09-14", "2026-09-14", "2026-09-30", p["tesoreria"], ti["liquidacion"], "" if "incompleto" in s else ca["liquidacion"], 4_300_000, "R-02"],
          ["EV-04", "2026-10-03", "2026-10-03", "2026-10-10", p["mercadeo"], ti["multa"], ca["multa"], 9_800_000, "R-09" if "sin_riesgo" in s else "R-05"],
          ["EV-05", "2026-07-01", "2026-07-01", reg5, p["tecnologia"], ti["caida"], ca["caida"], 31_000_000, "R-04"],
          ["EV-06", "2026-05-04", "2026-05-05", "2026-05-15", p["sucursales"], ti["fraude"], ca["fraude"], 6_200_000, "R-03"],   # el mismo tipo, en otro proceso
          ["EV-07", "2025-06-01", "2025-06-02", "2025-06-10", p["credito"], ti["desembolso"], ca["desembolso"], 1_200_000, "R-01"],  # fuera de la ventana
          ["EV-08", "2026-02-01", "2026-02-02", "2026-02-10", p["credito"], ti["desembolso"], ca["desembolso"], 900_000, "R-01"]]
    _xlsx(ev, docs / "30-eventos" / t["eventos"][0])

    # ------------------------------------------------------------ 40-actas
    acta = f"40-actas/{t['acta']}"
    con_accion = "alerta" not in s
    if pt:
        texto = (f"# Ata do comitê de riscos · outubro de 2026\n\n{e['nombre']}. Sessão de 2026-11-12.\n\n## Limites\n\n"
                 f"O comitê aprova o excesso do limite L-04, {m['L-04'].lower()}, até 2027-01-31, enquanto se reforça o monitoramento de transações.\n\n"
                 "O comitê toma conhecimento do plano de ação do limite L-03.\n\n## Indicadores-chave\n\n"
                 + ("O indicador KRI-01 está em alerta. O comitê aprova o bloqueio preventivo dos BIN comprometidos.\n" if con_accion else
                    "O indicador KRI-01 subiu no mês. Será revisado na próxima sessão.\n"))
    else:
        texto = (f"# Acta del comité de riesgos · octubre de 2026\n\n{e['nombre']}. Sesión del 2026-11-12.\n\n## Límites\n\n"
                 f"El comité aprueba el exceso del límite L-04, {m['L-04'].lower()}, hasta el 2027-01-31, mientras se refuerza el monitoreo transaccional.\n\n"
                 "El comité toma nota del plan de acción del límite L-03.\n\n## Indicadores clave\n\n"
                 + ("El indicador KRI-01 está en alerta. El comité aprueba el bloqueo preventivo de los BIN comprometidos.\n" if con_accion else
                    "El indicador KRI-01 subió en el mes. Se revisará en la próxima sesión.\n"))
    _pdf(texto, docs / acta)

    def cfg(rol: str) -> dict:
        return {"version": "0.1", "role": rol, "entity": {"id": e["id"], "name": e["nombre"], "country": e["pais"], "currency": e["moneda"]},
                "paths": {"documents": f"riesgos/{nombre_carpeta}", "state": f"estado-riesgos/{nombre_carpeta}"}, "period": PERIODO, "publish_rostrum": True,
                "methodology": dict(METODO), "columns": {}, "report": {"language": "es"}, "execution": {"workers": 1}}

    accion = ("Bloqueio preventivo dos BIN comprometidos" if pt else "Bloqueo preventivo de los BIN comprometidos")
    clave = {"entidad": e["nombre"], "industria": e["industria"], "pais": e["pais"], "hoy": HOY.isoformat(), "periodo": PERIODO, "siembra": bool(s),
             "config": {"severo": cfg("apetito"), "casandra": cfg("eventos")},
             "extraccion": {
                 "apetito": {"statement": {"name": "Declaração de apetite por riscos" if pt else "Declaración de apetito por riesgo", "board_review": revisada,
                                           "source": decl},
                             "approvals": [{"limit": "L-04", "until": "2027-01-31", "source": acta}],
                             "reviewed": [f"00-marco/{t['politica']}"], "questions": []},
                 "eventos": {"actions": [{"indicator": "KRI-01", "action": accion, "source": acta}] if con_accion else [],
                             "reviewed": [] if con_accion else [acta], "questions": []}},
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
