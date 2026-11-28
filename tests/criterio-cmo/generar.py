#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El material de prueba de la familia CMO: una cadena de retail en Colombia, un banco en el Perú, una
fabricante de consumo masivo en México y dos entidades de control.

    python3 tests/criterio-cmo/generar.py          escribe tests/criterio-cmo/material/

Cada entidad trae su carpeta de mercadeo al 25 de noviembre de 2026, con octubre como el periodo que se
evalúa: la política de publicidad en `00-politica/`; el registro de piezas y cada pieza aprobada con su
texto en `10-piezas/`; los soportes de las afirmaciones en `20-soportes/`; las bases de cada promoción en
`30-promociones/`; el registro de bases de contactos en `40-bases/`; y el plan de mercadeo, las facturas
de pauta, la exportación de la plataforma y el informe de resultados de octubre en `50-campanas/`.
Ninguna trae los datos de una persona: el registro de bases dice cuántos registros tiene cada una y con
qué autorización, y nada más.

**La clave la escribe este archivo, no el motor.** Cada defecto se siembra a propósito y su señal esperada
queda escrita en `clave.json`, junto con lo que el agente tendría que extraer de los documentos escritos
—cada afirmación de una pieza con su soporte, cada promoción con sus condiciones y cada resultado del
informe— y la configuración que deja el setup. El motor no la ve; `evaluar.py` compara lo que el motor
levanta contra ella, y una señal de más cuenta igual que una de menos.

**Cuántas veces.** El retail y el banco traen cada defecto tres veces y la de consumo masivo, dos (`veces`),
cada repetición en su propia pieza, promoción, base, campaña o factura. Así la familia pasa de 73 señales
sembradas, la muestra que pide el piso del 95 % sin fallas (decisión 0020).

**Las entidades de control no tienen ningún defecto**, y sí los casos que se parecen a uno: una pieza
aprobada el mismo día en que se publicó, una pieza de un influenciador que no se le pagó, una base sin
autorización que ninguna campaña usa, una campaña que pasa su presupuesto dentro de la tolerancia, una
factura con servicio el último día de la campaña y un resultado que difiere de la plataforma dentro de la
tolerancia. Todo es determinista: el mismo material cada vez, byte a byte. Los nombres, las empresas y
los documentos son inventados.
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
METODO = {"budget_tolerance_pct": 5, "result_tolerance_pct": 2}
FUENTE_COMP = "comparativo de precios de un tercero independiente, octubre de 2026"
TODAS = {"sin_soporte", "comparativa", "promocion", "patrocinada", "aprobacion", "base",
         "presupuesto", "factura", "meta", "resultado", "fin"}

ENTIDADES = [
    {"carpeta": "retail-co", "industria": "retail", "pais": "CO", "id": "901333555", "nombre": "Almacenes del Valle Sintéticos", "moneda": "COP",
     "siembra": set(TODAS), "veces": 3},
    {"carpeta": "banca-pe", "industria": "banca", "pais": "PE", "id": "20603335551", "nombre": "Banco Altiplano Sintético", "moneda": "PEN",
     "siembra": set(TODAS), "veces": 3},
    {"carpeta": "consumo-mx", "industria": "manufactura", "pais": "MX", "id": "CMS210415XY3", "nombre": "Consumo Maya Sintético", "moneda": "MXN",
     "siembra": set(TODAS), "veces": 2},
    {"carpeta": "control-co", "industria": "retail", "pais": "CO", "id": "901444666", "nombre": "Almacenes Control de Mercadeo Sintéticos", "moneda": "COP",
     "siembra": set(), "veces": 1},
    {"carpeta": "control-mx", "industria": "manufactura", "pais": "MX", "id": "CCM220101ZZ9", "nombre": "Consumo Control de Mercadeo Sintético", "moneda": "MXN",
     "siembra": set(), "veces": 1},
    # Grupo C: Chile, con los seguros.
    {"carpeta": "seguros-cl", "industria": "seguros", "pais": "CL", "id": "96789012-3", "nombre": "Seguros Cordillera Sintéticos", "moneda": "CLP",
     "siembra": set(TODAS), "veces": 2},
    # Grupo D: Panamá, con el retail.
    {"carpeta": "retail-pa", "industria": "retail", "pais": "PA", "id": "155634567-2-2020", "nombre": "Almacenes del Canal Sintéticos", "moneda": "USD",
     "siembra": set(TODAS), "veces": 2},
]

# Las repeticiones de cada defecto: la segunda vez (2) y la tercera (3), cada una en su propia pieza,
# promoción, base, campaña o factura.
# Pieza: (código, nombre, canal, afirmación, soporte —archivo y texto—, publicada, aprobada).
REP_PIEZAS = {
    "sin_soporte": {2: ("P-12", "Atención rápida", "Radio", "Atención en menos de 5 minutos en todas las sucursales.", None, "2026-10-05", "2026-10-01"),
                    3: ("P-13", "Cobertura", "Correo", "Más de 500 puntos de atención en el país.", None, "2026-10-09", "2026-10-06")},
    "comparativa": {2: ("P-22", "Útiles escolares", "Prensa", "Más barato que cualquier otra cadena en útiles escolares.",
                        ("comparativo_de_utiles_2026-10.pdf", "# Comparativo de precios de útiles escolares · octubre de 2026\n\nMedición propia sobre 25 productos en 4 cadenas.\n"),
                        "2026-10-07", "2026-10-03"),
                    3: ("P-23", "Envíos", "Televisión", "El envío más rápido del mercado.",
                        ("comparativo_de_envios_2026-10.pdf", "# Comparativo de tiempos de envío · octubre de 2026\n\nMedición propia sobre 300 pedidos a 3 competidores.\n"),
                        "2026-10-11", "2026-10-08")},
    "patrocinada": {2: ("P-32", "Visita de un creador", "Instagram", "La tienda abre hasta las 10 de la noche.",
                        ("horarios_de_atencion.pdf", "# Horarios de atención\n\nTodas las tiendas abren de 8 de la mañana a 10 de la noche.\n"),
                        "2026-10-14", "2026-10-13"),
                    3: ("P-33", "Reseña de cafés", "TikTok", "Tienen más de 200 referencias de café.",
                        ("catalogo_de_cafes.pdf", "# Catálogo de cafés\n\n214 referencias de café en el surtido de octubre.\n"),
                        "2026-10-16", "2026-10-15")},
    "aprobacion": {2: ("P-42", "Devoluciones", "Redes sociales", "Devoluciones en 30 días.",
                       ("politica_de_devoluciones.pdf", "# Política de devoluciones\n\nToda compra se puede devolver dentro de los 30 días siguientes.\n"),
                       "2026-10-14", "2026-10-16"),
                   3: ("P-43", "Garantía", "Exteriores", "Garantía de dos años en electrodomésticos.",
                       ("terminos_de_garantia.pdf", "# Términos de la garantía\n\nLos electrodomésticos tienen una garantía de 24 meses.\n"),
                       "2026-10-22", "2026-10-25")},
}
REP_PROMOS = {2: ("Cumpleaños", "bases_promocion_cumpleanos", "2026-10-01", "", True),
              3: ("Regreso a clases", "bases_promocion_regreso_a_clases", "2026-10-15", "2026-11-15", False)}
# Campaña: (código, nombre, presupuesto, inicio, fin, meta, indicador, base)
REP_CAMP = {
    "base": {2: ("C-12", "Reactivación", 15_000_000, "2026-10-01", "2026-11-30", "800 clientes reactivados", "Clientes reactivados", "B-12"),
             3: ("C-13", "Referidos", 12_000_000, "2026-10-01", "2026-12-15", "500 referidos", "Referidos", "B-13")},
    "meta": {2: ("C-22", "Aniversario", 25_000_000, "2026-10-01", "2026-11-15", "", "", ""),
             3: ("C-23", "Gran venta de noviembre", 35_000_000, "2026-10-15", "2026-11-30", "", "", "")},
    "presupuesto": {2: ("C-32", "Día de la familia", 20_000_000, "2026-09-01", "2026-10-31", "900 ventas", "Ventas atribuidas", ""),
                    3: ("C-33", "Hogar", 50_000_000, "2026-09-01", "2026-10-31", "1500 ventas", "Ventas atribuidas", "")},
    "fin": {2: ("C-42", "Verano", 18_000_000, "2026-08-01", "2026-09-30", "1000 visitas a la tienda", "Visitas a la tienda", ""),
            3: ("C-43", "Feria escolar", 22_000_000, "2026-09-01", "2026-10-10", "1200 visitas a la tienda", "Visitas a la tienda", "")},
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


def _miles(x: float) -> str:
    return f"{x:,.0f}".replace(",", ".")


def construir(e: dict) -> dict:
    """La carpeta de una entidad y su clave."""
    s = e["siembra"]

    def veces(tipo: str) -> list[int]:
        """Las repeticiones de un defecto sembrado, cada una en su propia fila."""
        return list(range(2, e["veces"] + 1)) if tipo in s else []

    raiz = SALIDA / e["carpeta"]
    nombre_carpeta = f"{e['id'].lower()}-{_norm(e['nombre']).replace('_', '-')}"
    docs = raiz / "mercadeo" / nombre_carpeta
    esperado = []

    def esp(signal: str, key: str) -> None:
        esperado.append({"signal": signal, "key": key})

    # ------------------------------------------------------------ 00-politica
    _pdf(f"# Política de publicidad · {e['nombre']}\n\nAprobada por la junta directiva el 2025-03-01.\n\n"
         "Toda pieza la aprueba el área legal antes de publicarse, y toda afirmación objetiva tiene su soporte en la carpeta de soportes. "
         "Una comparación con la competencia cita su fuente y su fecha en la misma pieza.\n\n"
         "Toda pieza pagada a un creador de contenido se identifica como publicidad.\n\n"
         f"La pauta facturada de una campaña no puede pasar su presupuesto en más del {METODO['budget_tolerance_pct']} %. "
         f"Un resultado reportado no puede diferir de la plataforma en más del {METODO['result_tolerance_pct']} % al mismo corte.\n",
         docs / "00-politica" / "politica_de_publicidad.pdf")

    # ------------------------------------------------------------ 20-soportes
    soportes = {"entrega": "20-soportes/tiempos_de_entrega.xlsx", "precios": "20-soportes/comparativo_de_precios_2026-10.pdf",
                "encuesta": "20-soportes/encuesta_de_satisfaccion_2026.pdf", "origen": "20-soportes/certificado_de_origen.pdf",
                "coleccion": "20-soportes/catalogo_de_la_coleccion.pdf"}
    _xlsx([["Ciudad", "Pedidos", "Entregados en 24 horas"], ["Principal 1", 12000, 11650], ["Principal 2", 8000, 7810]], docs / soportes["entrega"])
    _pdf("# Comparativo de precios de la canasta básica · octubre de 2026\n\nMedición de un tercero independiente sobre 40 productos en 5 cadenas.\n",
         docs / soportes["precios"])
    if "sin_soporte" not in s:
        _pdf("# Encuesta de satisfacción 2026\n\nMuestra de 2.400 clientes. El 90 % recomendaría la marca.\n", docs / soportes["encuesta"])
    _pdf("# Certificado de origen\n\nLa línea de productos se fabrica en el país.\n", docs / soportes["origen"])
    _pdf("# Catálogo de la colección\n\nTres colores disponibles.\n", docs / soportes["coleccion"])

    # ------------------------------------------------------------ 10-piezas
    fuente_comp = "" if "comparativa" in s else f"Fuente: {FUENTE_COMP}."
    piezas = [
        ("P-01", "Entrega en un día", "Televisión", "Entrega en 24 horas en las ciudades principales.", soportes["entrega"], False, ""),
        ("P-02", "Precio bajo", "Prensa", "El precio más bajo del mercado en la canasta básica.", soportes["precios"], True, fuente_comp),
        ("P-03", "Recomendación", "Redes sociales", "9 de cada 10 clientes nos recomiendan.", "" if "sin_soporte" in s else soportes["encuesta"], False, ""),
        ("P-04", "Reseña de una creadora", "Instagram", "Mi pedido llegó al día siguiente.", soportes["entrega"], False, ""),
        ("P-05", "Hecho en casa", "Exteriores", "Fabricado en el país.", soportes["origen"], False, ""),
        ("P-06", "La nueva colección", "TikTok", "La colección llega en tres colores.", soportes["coleccion"], False, ""),
    ]
    # Las repeticiones: cada una, una pieza más, con su soporte si lo tiene.
    reg_extra = []
    for tipo in ("sin_soporte", "comparativa", "patrocinada", "aprobacion"):
        for i in veces(tipo):
            pid, nom, canal, texto, sop, pub, apr = REP_PIEZAS[tipo][i]
            ruta = ""
            if sop:
                ruta = f"20-soportes/{sop[0]}"
                _pdf(sop[1], docs / ruta)
            piezas.append((pid, nom, canal, texto, ruta, tipo == "comparativa", ""))
            pagada = tipo == "patrocinada"
            reg_extra.append([pid, nom, canal, pub, apr, "Legal", "Sí" if pagada else "No", "No" if pagada else "",
                              "@creador_invitado_sintetico" if pagada else ""])
            esp({"sin_soporte": "claim_without_substantiation", "comparativa": "comparative_claim_without_source",
                 "patrocinada": "sponsored_content_unidentified", "aprobacion": "piece_published_unapproved"}[tipo],
                f"{ {'sin_soporte': 'soporte', 'comparativa': 'comparativa', 'patrocinada': 'patrocinada', 'aprobacion': 'aprobacion'}[tipo] }:{pid}")
    claims = []
    for pid, nom, canal, texto, sop, comp, fuente in piezas:
        f = f"10-piezas/pieza_{pid}.pdf"
        extra = ""
        if pid == "P-04":
            extra = "\n\n#Publicidad · Contenido pagado por la marca." if "patrocinada" not in s else "\n\n@creadora_sintetica"
        elif pid.startswith("P-3"):
            extra = "\n\n@creador_invitado_sintetico"
        _pdf(f"# {nom} · {e['nombre']}\n\nCanal: {canal}.\n\n«{texto}»" + (f"\n\n{fuente}" if fuente else "") + extra + "\n", docs / f)
        c = {"piece": pid, "claim": texto, "support": sop, "source": f}
        if comp:
            c["comparative"] = True
            # La fuente que la pieza cita, sin la etiqueta «Fuente:» ni el punto final: es lo que el
            # agente lleva a la ficha, y la calificación busca este texto dentro del suyo (CMO-1).
            c["comparative_source"] = FUENTE_COMP if fuente else ""
        claims.append(c)
    if "sin_soporte" in s:
        esp("claim_without_substantiation", "soporte:P-03")
    if "comparativa" in s:
        esp("comparative_claim_without_source", "comparativa:P-02")
    apr_p05 = "2026-10-15" if "aprobacion" in s else "2026-10-12"         # después de publicada, o el mismo día (control)
    if "aprobacion" in s:
        esp("piece_published_unapproved", "aprobacion:P-05")
    if "patrocinada" in s:
        esp("sponsored_content_unidentified", "patrocinada:P-04")
    _xlsx([["Pieza", "Nombre", "Canal", "Fecha de publicación", "Fecha de aprobación", "Aprobado por", "Pagada a influenciador",
            "Identificada como publicidad", "Influenciador"],
           ["P-01", "Entrega en un día", "Televisión", "2026-10-03", "2026-09-28", "Legal", "No", "", ""],
           ["P-02", "Precio bajo", "Prensa", "2026-10-06", "2026-10-02", "Legal", "No", "", ""],
           ["P-03", "Recomendación", "Redes sociales", "2026-10-08", "2026-10-07", "Legal", "No", "", ""],
           ["P-04", "Reseña de una creadora", "Instagram", "2026-10-10", "2026-10-09", "Legal", "Sí", "No" if "patrocinada" in s else "Sí", "@creadora_sintetica"],
           ["P-05", "Hecho en casa", "Exteriores", "2026-10-12", apr_p05, "Legal", "No", "", ""],
           ["P-06", "La nueva colección", "TikTok", "2026-10-20", "2026-10-18", "Legal", "No", "No", "@creador_sintetico"]] + reg_extra,
          docs / "10-piezas" / "registro_de_piezas.xlsx")

    # ------------------------------------------------------------ 30-promociones
    fin_puntos = "" if "promocion" in s else "2026-11-30"
    if "promocion" in s:
        esp("promotion_terms_missing", "promocion:bases_promocion_puntos_dobles")
    _pdf(f"# Bases de la promoción Navidad · {e['nombre']}\n\nVigencia: del 2026-12-01 al 2026-12-24.\n\n"
         "Modo: un cupón por cada compra superior al monto mínimo. Lugar: todas las tiendas y la tienda en línea.\n",
         docs / "30-promociones" / "bases_promocion_navidad.pdf")
    _pdf(f"# Bases de la promoción Puntos dobles · {e['nombre']}\n\nVigencia: desde el 2026-11-01" + (f" hasta el {fin_puntos}" if fin_puntos else "") + ".\n\n"
         "Modo: puntos dobles en cada compra con la tarjeta de la marca. Lugar: todas las tiendas.\n",
         docs / "30-promociones" / "bases_promocion_puntos_dobles.pdf")
    promos = [{"name": "Navidad", "start": "2026-12-01", "end": "2026-12-24", "conditions": True, "source": "30-promociones/bases_promocion_navidad.pdf"},
              {"name": "Puntos dobles", "start": "2026-11-01", "end": fin_puntos, "conditions": True, "source": "30-promociones/bases_promocion_puntos_dobles.pdf"}]
    for i in veces("promocion"):                      # la segunda sin su fin; la tercera, sin el modo ni el lugar
        nom, stem, ini, fin, cond = REP_PROMOS[i]
        _pdf(f"# Bases de la promoción {nom} · {e['nombre']}\n\nVigencia: desde el {ini}" + (f" hasta el {fin}" if fin else "") + ".\n\n"
             + ("Modo: un bono en el mes de cumpleaños del cliente. Lugar: todas las tiendas.\n" if cond else "Descuentos especiales en la temporada.\n"),
             docs / "30-promociones" / f"{stem}.pdf")
        promos.append({"name": nom, "start": ini, "end": fin, "conditions": cond, "source": f"30-promociones/{stem}.pdf"})
        esp("promotion_terms_missing", f"promocion:{stem}")

    # ------------------------------------------------------------ 40-bases
    # B-02 la usa C-02: sin autorización donde se siembra. B-03 no tiene autorización y ninguna campaña la usa: no es una señal.
    if "base" in s:
        esp("contact_base_without_consent", "base:B-02")
    _xlsx([["Base", "Registros", "Autorización para mercadeo", "Fecha de autorización", "Finalidad"],
           ["B-01", 120000, "Sí", "2024-03-01", "Mercadeo y servicio"],
           ["B-02", 45000, "No" if "base" in s else "Sí", "" if "base" in s else "2025-06-15", "Servicio" if "base" in s else "Mercadeo"],
           ["B-03", 8000, "No", "", "Servicio"]]
          + [[f"B-1{i}", {2: 15000, 3: 6000}[i], "No", "", "Servicio"] for i in veces("base")],
          docs / "40-bases" / "registro_de_bases_de_contactos.xlsx")
    for i in veces("base"):
        esp("contact_base_without_consent", f"base:B-1{i}")

    # ------------------------------------------------------------ 50-campanas
    if "meta" in s:
        esp("campaign_without_goal", "meta:C-02")
    _xlsx([["Campaña", "Nombre", "Presupuesto", "Inicio", "Fin", "Meta", "Indicador", "Base de contactos"],
           ["C-01", "Temporada de fin de año", 100_000_000, "2026-09-01", "2026-10-31", "5000 ventas", "Ventas atribuidas", "B-01"],
           ["C-02", "Clientes recurrentes", 40_000_000, "2026-09-15", "2026-11-30", "" if "meta" in s else "1200 recompras",
            "" if "meta" in s else "Recompras", "B-02"],
           ["C-03", "Lanzamiento de la colección", 60_000_000, "2026-09-01", "2026-10-15", "3000 visitas a la tienda", "Visitas a la tienda", ""],
           ["C-04", "Marca", 30_000_000, "2026-08-01", "2026-12-31", "2 millones de impresiones", "Impresiones", ""]]
          + [list(REP_CAMP[tipo][i]) for tipo in ("base", "meta", "presupuesto", "fin") for i in veces(tipo)],
          docs / "50-campanas" / "plan_de_mercadeo.xlsx")
    for i in veces("meta"):
        esp("campaign_without_goal", f"meta:{REP_CAMP['meta'][i][0]}")
    for i in veces("presupuesto"):
        esp("campaign_over_budget", f"presupuesto:{REP_CAMP['presupuesto'][i][0]}")
    for i in veces("fin"):
        esp("campaign_ran_past_end", f"fin:{REP_CAMP['fin'][i][0]}")
    for i in veces("factura"):
        esp("media_invoice_unmatched", f"factura:F-2{i}")
    # Las facturas de las repeticiones: la pauta que pasa el presupuesto, la que sigue después del fin y la que no tiene campaña.
    fac_extra = []
    for i in veces("presupuesto"):
        cid, _, pres = REP_CAMP["presupuesto"][i][:3]
        fac_extra += [[f"F-3{i}1", "Digital Sintética", cid, f"OC-3{i}", "2026-09-30", "2026-09-30", round(pres * 0.6)],
                      [f"F-3{i}2", "Digital Sintética", cid, f"OC-3{i}", "2026-10-31", "2026-10-31", round(pres * {2: 0.55, 3: 0.48}[i])]]
    for i in veces("fin"):
        cid, _, pres, _, fin_c = REP_CAMP["fin"][i][:5]
        fac_extra.append([f"F-4{i}", "Exteriores Sintéticos", cid, f"OC-4{i}", "2026-10-31", {2: "2026-10-20", 3: "2026-10-25"}[i], round(pres * 0.5)])
    for i in veces("factura"):
        fac_extra.append([f"F-2{i}", {2: "Prensa Sintética", 3: "Vallas Sintéticas"}[i], "", "", "2026-10-31", "2026-10-31", {2: 4_000_000, 3: 9_000_000}[i]])
    if "presupuesto" in s:
        esp("campaign_over_budget", "presupuesto:C-01")
    if "fin" in s:
        esp("campaign_ran_past_end", "fin:C-03")
    if "factura" in s:
        esp("media_invoice_unmatched", "factura:F-105")
    _xlsx([["Factura", "Proveedor", "Campaña", "Orden de compra", "Fecha", "Pauta hasta", "Valor"],
           ["F-101", "Televisora Sintética", "C-01", "OC-301", "2026-09-30", "2026-09-30", 60_000_000],
           ["F-102", "Televisora Sintética", "C-01", "OC-301", "2026-10-31", "2026-10-31", 48_000_000 if "presupuesto" in s else 44_000_000],
           ["F-103", "Redes Sintéticas", "C-02", "OC-302", "2026-10-31", "2026-10-31", 18_000_000],
           ["F-104", "Exteriores Sintéticos", "C-03", "OC-303", "2026-10-31", "2026-10-31" if "fin" in s else "2026-10-15", 25_000_000],
           ["F-105", "Radio Sintética", "" if "factura" in s else "C-04", "" if "factura" in s else "OC-304", "2026-10-31", "2026-10-31", 7_000_000]] + fac_extra,
          docs / "50-campanas" / "facturas_de_pauta.xlsx")
    corte = "2026-10-31"
    plataforma = {("C-01", "Ventas atribuidas"): 4100, ("C-03", "Visitas a la tienda"): 2850, ("C-04", "Impresiones"): 1_840_000}
    _xlsx([["Campaña", "Indicador", "Corte", "Valor"]] + [[c, i, corte, v] for (c, i), v in plataforma.items()],
          docs / "50-campanas" / "resultados_plataforma.xlsx")
    rep_c01 = 4600 if "resultado" in s else 4150                                  # 12 % por encima, o 1,2 % (control: dentro de la tolerancia)
    if "resultado" in s:
        esp("result_differs_from_platform", "resultado:C-01:ventas_atribuidas")
    rep_c03 = 3100 if 2 in veces("resultado") else 2850                       # 8,8 % por encima, o igual
    rep_c04 = 1_990_000 if 3 in veces("resultado") else 1_840_000             # 8,2 % por encima, o igual
    for i, (c, ind) in ((2, ("C-03", "visitas_a_la_tienda")), (3, ("C-04", "impresiones"))):
        if i in veces("resultado"):
            esp("result_differs_from_platform", f"resultado:{c}:{ind}")
    reportados = [("C-01", "Ventas atribuidas", rep_c01), ("C-03", "Visitas a la tienda", rep_c03), ("C-04", "Impresiones", rep_c04)]
    inf = "50-campanas/informe_de_resultados_2026-10.pdf"
    _pdf(f"# Informe de resultados de mercadeo · octubre de 2026\n\n{e['nombre']}. Resultados con corte al 31 de octubre de 2026.\n\n"
         "| Campaña | Indicador | Resultado |\n|---|---|---|\n" + "\n".join(f"| {c} | {i} | {_miles(v)} |" for c, i, v in reportados) + "\n", docs / inf)

    def cfg(rol: str) -> dict:
        return {"version": "0.1", "role": rol, "entity": {"id": e["id"], "name": e["nombre"], "country": e["pais"], "currency": e["moneda"]},
                "paths": {"documents": f"mercadeo/{nombre_carpeta}", "state": f"estado-mercadeo/{nombre_carpeta}"}, "period": PERIODO,
                "publish_rostrum": True, "methodology": dict(METODO), "columns": {}, "report": {"language": "es"}, "execution": {"workers": 1}}

    clave = {"entidad": e["nombre"], "industria": e["industria"], "pais": e["pais"], "hoy": HOY.isoformat(), "periodo": PERIODO, "siembra": bool(s),
             "config": {"lucia": cfg("piezas"), "prospero": cfg("campanas")},
             "extraccion": {"piezas": {"claims": claims, "promotions": promos, "reviewed": [], "questions": []},
                            "campanas": {"reported": [{"campaign": c, "indicator": i, "cutoff": corte, "value": v, "source": inf} for c, i, v in reportados],
                                         "reviewed": [], "questions": []}},
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
