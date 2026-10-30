#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El material de prueba de la familia CFO: cuatro industrias y una entidad de control por país.

    python3 tests/criterio-cfo/generar.py          escribe tests/criterio-cfo/material/

Cada entidad trae su cierre de septiembre de 2026 —balance, mayor, auxiliares, extractos,
facturas electrónicas, checklist, soportes, requerimientos del auditor— y su presupuesto del
año con dos versiones, la contabilidad de enero a septiembre, compromisos, proyecciones y
actas. Cada entidad es de un país del registro (paises.json) y trae el XML de su factura
electrónica, con el lector y la fuente de ese país.

**La clave la escribe este archivo, no el motor.** Cada defecto se siembra a propósito y su
señal esperada queda escrita en `clave.json`, junto con lo que el agente tendría que extraer
de los documentos escritos. El motor no la ve; `evaluar.py` compara lo que el motor levanta
contra ella, y una señal de más cuenta igual que una de menos.

**Los formatos son los de un área financiera real.** Parte de las tablas pasa a Excel —con números
y fechas de verdad, no texto— y parte de las actas, los soportes y las respuestas al auditor a Word
y PDF. Qué se convierte lo decide un hash del nombre y de la entidad, así que el mismo material
sale siempre igual; los hechos no cambian con el formato, y la clave cita el archivo como queda.

**Las entidades de control no tienen ningún defecto.** Un motor que levanta algo ahí es un
generador de ruido. Todo es determinista: la misma semilla da el mismo material, byte a byte.
"""
from __future__ import annotations

import csv
import datetime as dt
import hashlib
import json
import random
import shutil
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent.parent
sys.path.insert(0, str(RAIZ / "plugins" / "criterio-finance" / "scripts"))
import finanzas as F  # noqa: E402
sys.path.insert(0, str(RAIZ / "tests" / "sintetico"))
import formatos as FMT  # noqa: E402  (Word y PDF sin dependencias, los mismos de la familia PMO)

SALIDA = AQUI / "material"
PERIODO, ANIO, HOY = "2026-09", "2026", "2026-10-06"
# La tasa del IVA de cada país sale de su registro (paises.json), como todo lo que cambia de un país a otro.
TASA = {c: f["iva"] for c, f in F.FACTURA.items()}

def ruc(tipo: int, semilla: int, i: int) -> str:
    """Un RUC ficticio de once dígitos con su dígito verificador por módulo 11 (pesos 5 4 3 2 7 6 5 4
    3 2), para que el material tenga la forma de uno real. Ninguno corresponde a una empresa."""
    base = f"{tipo:02d}{semilla:02d}{i:06d}"
    r = 11 - sum(int(d) * w for d, w in zip(base, (5, 4, 3, 2, 7, 6, 5, 4, 3, 2))) % 11
    return base + str({10: 0, 11: 1}.get(r, r))


ENTIDADES = [
    {"carpeta": "banca", "industria": "banca", "pais": "CO", "id": "900123456", "nombre": "Banco Andino", "moneda": "COP", "escala": 1_000_000, "semilla": 11,
     "siembra": ["balance_descuadrado", "cheque_viejo", "comision_sin_registrar", "iva_distinto", "tarea_sin_soporte",
                 "desviacion", "area_declara_dentro", "traslado_sin_acta", "proyecto_distinto"]},
    {"carpeta": "cooperativas", "industria": "cooperativas", "pais": "EC", "id": "1790012345001", "nombre": "Cooperativa Sierra Alta", "moneda": "USD", "escala": 1_000, "semilla": 23,
     "siembra": ["banco_sin_extracto", "cartera_descuadrada", "factura_sin_registro", "registro_sin_factura", "requerimiento_sin_soporte",
                 "requerimiento_vencido", "tarea_vencida", "comprometido_al_limite", "proyeccion_vieja", "version_distinta"]},
    {"carpeta": "retail", "industria": "retail", "pais": "CO", "id": "900765432", "nombre": "Almacenes Caribe", "moneda": "COP", "escala": 800_000, "semilla": 37,
     "siembra": ["xml_duplicado", "registro_doble", "asiento_fuera_del_balance", "consignacion_en_transito", "cierre_declarado",
                 "gasto_sin_linea", "proyeccion_sobre_lo_aprobado", "cuenta_sin_auxiliar"]},
    {"carpeta": "mineria", "industria": "mineria", "pais": "EC", "id": "0990054321001", "nombre": "Minera Cóndor", "moneda": "USD", "escala": 2_000, "semilla": 41,
     "siembra": ["tarea_vencida", "tarea_sin_soporte", "comision_sin_registrar", "cheque_viejo", "requerimiento_vencido",
                 "desviacion", "traslado_sin_acta", "comprometido_al_limite", "factura_recibida_sin_registro", "requerimiento_en_carta"]},
    {"carpeta": "control-co", "industria": "retail", "pais": "CO", "id": "900000001", "nombre": "Distribuidora Control", "moneda": "COP", "escala": 500_000, "semilla": 53, "siembra": []},
    {"carpeta": "control-ec", "industria": "cooperativas", "pais": "EC", "id": "1790000001001", "nombre": "Comercial Control", "moneda": "USD", "escala": 1_500, "semilla": 67, "siembra": []},
    {"carpeta": "banca-pe", "industria": "banca", "pais": "PE", "id": ruc(20, 71, 1), "nombre": "Banco Ribera", "moneda": "PEN", "escala": 4_000, "semilla": 71,
     "siembra": ["iva_distinto", "xml_duplicado", "consignacion_en_transito", "cierre_declarado", "tarea_sin_soporte",
                 "desviacion", "area_declara_dentro", "traslado_sin_acta"]},
    {"carpeta": "mineria-pe", "industria": "mineria", "pais": "PE", "id": ruc(20, 73, 1), "nombre": "Minera Puna Alta", "moneda": "PEN", "escala": 6_000, "semilla": 73,
     "siembra": ["factura_sin_registro", "registro_sin_factura", "cheque_viejo", "requerimiento_en_carta", "requerimiento_vencido",
                 "comprometido_al_limite", "version_distinta", "proyeccion_vieja"]},
    {"carpeta": "control-pe", "industria": "mineria", "pais": "PE", "id": ruc(20, 79, 1), "nombre": "Comercial Control Sur", "moneda": "PEN", "escala": 3_000, "semilla": 79, "siembra": []},
    {"carpeta": "retail-cl", "industria": "retail", "pais": "CL", "id": F.rut(76083001), "nombre": "Tiendas Pacífico", "moneda": "CLP", "escala": 250_000, "semilla": 83,
     "siembra": ["iva_distinto", "xml_duplicado", "registro_doble", "consignacion_en_transito", "cierre_declarado",
                 "gasto_sin_linea", "proyeccion_sobre_lo_aprobado", "traslado_sin_acta"]},
    {"carpeta": "mineria-cl", "industria": "mineria", "pais": "CL", "id": F.rut(76089001), "nombre": "Minera Atacama Norte", "moneda": "CLP", "escala": 600_000, "semilla": 89,
     "siembra": ["factura_sin_registro", "registro_sin_factura", "cheque_viejo", "comision_sin_registrar", "requerimiento_vencido",
                 "tarea_vencida", "desviacion", "comprometido_al_limite"]},
    {"carpeta": "control-cl", "industria": "retail", "pais": "CL", "id": F.rut(76097001), "nombre": "Comercial Control Andes", "moneda": "CLP", "escala": 300_000, "semilla": 97, "siembra": []},
    {"carpeta": "banca-mx", "industria": "banca", "pais": "MX", "id": F.rfc("BVA", "150301", "K21"), "nombre": "Banco Valle de Anáhuac", "moneda": "MXN", "escala": 20_000, "semilla": 13,
     "siembra": ["balance_descuadrado", "cheque_viejo", "comision_sin_registrar", "iva_distinto", "tarea_sin_soporte",
                 "desviacion", "area_declara_dentro", "traslado_sin_acta", "factura_sin_registro"]},
    {"carpeta": "retail-mx", "industria": "retail", "pais": "MX", "id": F.rfc("TBA", "180912", "Q37"), "nombre": "Tiendas del Bajío", "moneda": "MXN", "escala": 15_000, "semilla": 17,
     "siembra": ["xml_duplicado", "registro_sin_factura", "consignacion_en_transito", "cierre_declarado", "requerimiento_vencido",
                 "gasto_sin_linea", "proyeccion_vieja", "comprometido_al_limite"]},
    {"carpeta": "control-mx", "industria": "banca", "pais": "MX", "id": F.rfc("CCM", "120615", "R59"), "nombre": "Comercial Control Centro", "moneda": "MXN", "escala": 12_000, "semilla": 19, "siembra": []},
    # Brasil: retail y minería de São Paulo, con sus documentos en portugués. Los bancos de Brasil
    # facturan sus servicios con la nota fiscal de servicios de cada municipio, no con la NF-e.
    {"carpeta": "retail-br", "industria": "retail", "pais": "BR", "id": F.cnpj(31452078), "nombre": "Lojas Paulistas", "moneda": "BRL", "escala": 5_000, "semilla": 29,
     "siembra": ["iva_distinto", "factura_sin_registro", "cheque_viejo", "cierre_declarado", "tarea_sin_soporte",
                 "desviacion", "area_declara_dentro", "comprometido_al_limite"]},
    {"carpeta": "mineria-br", "industria": "mineria", "pais": "BR", "id": F.cnpj(28903114), "nombre": "Mineração Serra Azul", "moneda": "BRL", "escala": 10_000, "semilla": 31,
     "siembra": ["registro_sin_factura", "xml_duplicado", "comision_sin_registrar", "requerimiento_en_carta", "requerimiento_vencido",
                 "traslado_sin_acta", "proyeccion_vieja", "version_distinta"]},
    {"carpeta": "control-br", "industria": "retail", "pais": "BR", "id": F.cnpj(40217355), "nombre": "Comercial Controle Paulista", "moneda": "BRL", "escala": 4_000, "semilla": 43, "siembra": []},
    # Argentina: retail y minería, con el comprobante electrónico de ARCA (F-24).
    {"carpeta": "retail-ar", "industria": "retail", "pais": "AR", "id": F.cuit(30, 71452078), "nombre": "Almacenes del Plata", "moneda": "ARS", "escala": 1_500_000, "semilla": 61,
     "siembra": ["iva_distinto", "registro_sin_factura", "cheque_viejo", "cierre_declarado", "tarea_sin_soporte",
                 "desviacion", "area_declara_dentro", "comprometido_al_limite"]},
    {"carpeta": "mineria-ar", "industria": "mineria", "pais": "AR", "id": F.cuit(30, 70903114), "nombre": "Minera Cordillera de Cuyo", "moneda": "ARS", "escala": 3_000_000, "semilla": 67,
     "siembra": ["factura_sin_registro", "xml_duplicado", "comision_sin_registrar", "requerimiento_en_carta", "requerimiento_vencido",
                 "traslado_sin_acta", "proyeccion_vieja", "version_distinta"]},
    {"carpeta": "control-ar", "industria": "retail", "pais": "AR", "id": F.cuit(30, 70217355), "nombre": "Comercial Control del Plata", "moneda": "ARS", "escala": 1_200_000, "semilla": 71, "siembra": []},
    # Panamá: banca y retail, con la factura electrónica de la DGI (F-27), en dólares.
    {"carpeta": "banca-pa", "industria": "banca", "pais": "PA", "id": F.ruc_pa(731001), "nombre": "Banco Istmeño", "moneda": "USD", "escala": 2_000, "semilla": 73,
     "siembra": ["balance_descuadrado", "cheque_viejo", "comision_sin_registrar", "iva_distinto", "tarea_sin_soporte",
                 "desviacion", "area_declara_dentro", "traslado_sin_acta", "factura_sin_registro"]},
    {"carpeta": "retail-pa", "industria": "retail", "pais": "PA", "id": F.ruc_pa(791002), "nombre": "Almacenes del Canal", "moneda": "USD", "escala": 1_500, "semilla": 79,
     "siembra": ["xml_duplicado", "registro_sin_factura", "consignacion_en_transito", "cierre_declarado", "requerimiento_vencido",
                 "gasto_sin_linea", "proyeccion_vieja", "comprometido_al_limite"]},
    {"carpeta": "control-pa", "industria": "banca", "pais": "PA", "id": F.ruc_pa(831003), "nombre": "Comercial Control del Istmo", "moneda": "USD", "escala": 1_200, "semilla": 83, "siembra": []},
    # Guatemala: retail y minería —los bancos siguen los manuales de su superintendencia, no las NIIF (F-33)—, con la FEL (F-30).
    {"carpeta": "retail-gt", "industria": "retail", "pais": "GT", "id": F.nit_gt(8714520), "nombre": "Almacenes del Altiplano", "moneda": "GTQ", "escala": 12_000, "semilla": 87,
     "siembra": ["iva_distinto", "factura_sin_registro", "cheque_viejo", "cierre_declarado", "tarea_sin_soporte",
                 "desviacion", "area_declara_dentro", "comprometido_al_limite"]},
    {"carpeta": "mineria-gt", "industria": "mineria", "pais": "GT", "id": F.nit_gt(8909031), "nombre": "Minera del Motagua", "moneda": "GTQ", "escala": 25_000, "semilla": 89,
     "siembra": ["registro_sin_factura", "xml_duplicado", "comision_sin_registrar", "requerimiento_en_carta", "requerimiento_vencido",
                 "traslado_sin_acta", "proyeccion_vieja", "version_distinta"]},
    {"carpeta": "control-gt", "industria": "retail", "pais": "GT", "id": F.nit_gt(9721735), "nombre": "Comercial Control de Guatemala", "moneda": "GTQ", "escala": 10_000, "semilla": 97, "siembra": []},
    # Costa Rica: banca y retail —las entidades del CONASSIF usan las NIIF completas (F-36)—, con el comprobante 4.4 (F-34).
    {"carpeta": "banca-cr", "industria": "banca", "pais": "CR", "id": F.cedula_cr(457812), "nombre": "Banco del Valle Central Sintético", "moneda": "CRC", "escala": 1_000_000, "semilla": 101,
     "siembra": ["balance_descuadrado", "comision_sin_registrar", "iva_distinto", "requerimiento_en_carta", "tarea_sin_soporte",
                 "desviacion", "area_declara_dentro", "traslado_sin_acta"]},
    {"carpeta": "retail-cr", "industria": "retail", "pais": "CR", "id": F.cedula_cr(612904), "nombre": "Almacenes de la Meseta", "moneda": "CRC", "escala": 750_000, "semilla": 103,
     "siembra": ["registro_sin_factura", "xml_duplicado", "cheque_viejo", "cierre_declarado", "requerimiento_vencido",
                 "gasto_sin_linea", "proyeccion_vieja", "comprometido_al_limite"]},
    {"carpeta": "control-cr", "industria": "retail", "pais": "CR", "id": F.cedula_cr(733015), "nombre": "Comercial Control de Costa Rica", "moneda": "CRC", "escala": 600_000, "semilla": 107, "siembra": []},
    # Honduras: banca —los bancos que regula la CNBS siguen las NIIF con sus normas prudenciales (F-39)— y
    # retail, con la factura como documento: su CAI, su rango autorizado y su fecha límite (F-37, decisión 0024).
    {"carpeta": "banca-hn", "industria": "banca", "pais": "HN", "id": F.rtn_hn(4578120), "nombre": "Banco de Occidente Sintético", "moneda": "HNL", "escala": 50_000, "semilla": 109,
     "siembra": ["balance_descuadrado", "comision_sin_registrar", "iva_distinto", "requerimiento_en_carta", "tarea_sin_soporte",
                 "desviacion", "area_declara_dentro", "traslado_sin_acta", "fuera_de_fecha"]},
    {"carpeta": "retail-hn", "industria": "retail", "pais": "HN", "id": F.rtn_hn(6129040), "nombre": "Almacenes del Valle de Sula", "moneda": "HNL", "escala": 40_000, "semilla": 113,
     "siembra": ["registro_sin_factura", "factura_sin_registro", "cheque_viejo", "cierre_declarado", "requerimiento_vencido",
                 "gasto_sin_linea", "proyeccion_vieja", "comprometido_al_limite", "fuera_de_rango"]},
    {"carpeta": "control-hn", "industria": "retail", "pais": "HN", "id": F.rtn_hn(7330150), "nombre": "Comercial Control de Honduras", "moneda": "HNL", "escala": 30_000, "semilla": 127, "siembra": []},
]

# Las líneas del presupuesto: área, línea, cuenta, centro de costo y el aprobado mensual en
# unidades de la escala de cada entidad.
LINEAS = [
    ("Administración", "Servicios públicos", "5135", "ADM", 3.0),
    ("Administración", "Mantenimiento", "5145", "ADM", 2.0),
    ("Comercial", "Publicidad", "5195", "COM", 4.0),
    ("Comercial", "Eventos", "5195", "EVT", 1.5),
    ("Tecnología", "Licencias", "5135", "TEC", 5.0),
    ("Tecnología", "PRY-310", "5145", "PRY", 6.0),
    ("Operaciones", "Transporte", "5135", "OPE", 3.5),
    ("Personal", "Nómina", "5105", "ADM", 20.0),
]
NOMBRES = {"11100501": "Bancos · cuenta 1", "11100502": "Bancos · cuenta 2", "1305": "Clientes", "1435": "Inventarios",
           "2205": "Proveedores", "2408": "IVA por pagar", "2505": "Salarios por pagar", "3105": "Capital", "4135": "Ventas",
           "5105": "Gastos de personal", "5135": "Servicios", "5145": "Mantenimiento", "5195": "Diversos", "5305": "Gastos financieros"}


def r2(x: float) -> float:
    return round(x + 0.0, 2)


def csv_(ruta: Path, filas: list[list]) -> None:
    ruta.parent.mkdir(parents=True, exist_ok=True)
    if LANG[0] == "pt" and filas:
        filas = [[CAB_PT.get(c, c) for c in filas[0]]] + [[tr(v) for v in f] for f in filas[1:]]
    with open(ruta, "w", newline="", encoding="utf-8") as f:
        csv.writer(f, delimiter=";", lineterminator="\n").writerows([[("" if v is None else (f"{v:.2f}" if isinstance(v, float) else v)) for v in fila] for fila in filas])


def md(ruta: Path, texto: str) -> None:
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(texto.strip() + "\n", encoding="utf-8")


# ------------------------------------------------ Brasil: el material en portugués
# Las entidades de Brasil traen sus documentos en portugués, como los tiene una empresa de allá: las
# cabeceras de las tablas, los nombres de los archivos, las cuentas, las áreas, las descripciones,
# las actas, los correos y las personas. La estructura de carpetas es la de la plataforma. El
# material se arma con el mismo código para todos los países y se traduce al escribirlo; la clave
# se traduce igual, así que lo que espera es lo que dicen los documentos.
LANG = ["es"]
CAB_PT = {"fecha": "data", "comprobante": "lancamento", "cuenta": "conta", "tercero": "cnpj", "documento": "documento",
          "debito": "debito", "credito": "credito", "centro_costo": "centro_de_custo", "descripcion": "historico",
          "nombre": "nome", "naturaleza": "natureza", "saldo_inicial": "saldo_inicial", "saldo_final": "saldo_final",
          "valor": "valor", "saldo": "saldo", "referencia": "referencia", "moneda": "moeda", "area": "area", "linea": "linha",
          "total": "total", "id": "id", "tarea": "tarefa", "responsable": "responsavel", "dia_limite": "prazo",
          "depende_de": "depende_de", "evidencia_esperada": "evidencia_esperada", "criticidad": "criticidade", "estado": "situacao",
          "solicitud": "solicitacao", "fecha_limite": "data_limite", "numero": "numero", "proveedor": "fornecedor",
          "saldo_por_ejecutar": "saldo_a_executar", "proyeccion": "projecao", "version": "versao", "concepto": "conceito",
          "monto_maximo": "valor_maximo", "cargo": "cargo", "saldo_proyectado": "saldo_projetado", "beneficiario": "beneficiario",
          "aprobado_por": "aprovado_por", "obligacion": "obrigacao", "tipo": "tipo", "contraparte": "contraparte",
          "vencimiento": "vencimento", "indicador": "indicador", "numerador": "numerador", "denominador": "denominador",
          "operador": "operador", "limite": "limite"}
CAB_PT.update(dict(zip(F.MESES, F.N.MESES_PT)))
PERSONAS_PT = [("Sofía León", "Sofia Leão"), ("Lucía Mora", "Luciana Moraes"), ("Andrés Paz", "André Pacheco"),
               ("Marta Ríos", "Marta Rios"), ("Jorge Vela", "Jorge Veloso"), ("Elena Cruz", "Helena Cruz"),
               ("Ana Ruiz", "Ana Ruas"), ("Luis Mora", "Luís Moura"), ("Carlos Paz", "Carlos Peixoto")]
FRASES_PT = PERSONAS_PT + [
    ("Administración", "Administração"), ("Tecnología", "Tecnologia"), ("Operaciones", "Operações"), ("Personal", "Pessoal"),
    ("Servicios públicos", "Serviços públicos"), ("Mantenimiento", "Manutenção"), ("Publicidad", "Publicidade"), ("Eventos", "Eventos"),
    ("Licencias", "Licenças"), ("Transporte", "Transporte"), ("Nómina", "Folha de pagamento"),
    ("Bancos · cuenta 1", "Bancos · conta 1"), ("Bancos · cuenta 2", "Bancos · conta 2"), ("Clientes", "Clientes"), ("Inventarios", "Estoques"),
    ("Proveedores", "Fornecedores"), ("IVA por pagar", "ICMS a recolher"), ("Salarios por pagar", "Salários a pagar"), ("Capital", "Capital social"),
    ("Ventas", "Vendas"), ("Gastos de personal", "Despesas com pessoal"), ("Servicios", "Serviços"), ("Diversos", "Diversos"),
    ("Gastos financieros", "Despesas financeiras"),
    ("Servicio sin centro de costo", "Serviço sem centro de custo"), ("IVA generado", "ICMS a recolher"), ("IVA descontable", "ICMS a recuperar"),
    ("Cuenta por pagar", "Conta a pagar"), ("Nómina de septiembre", "Folha de pagamento de setembro"), ("Nómina por pagar", "Folha a pagar"),
    ("Pago de nómina", "Pagamento da folha"), ("Débito nómina", "Débito folha de pagamento"), ("Traslado entre cuentas", "Transferência entre contas"),
    ("Traslado recibido", "Transferência recebida"), ("Traslado enviado", "Transferência enviada"), ("Comisión bancaria", "Tarifa bancária"),
    ("Comisión de manejo", "Tarifa de manutenção de conta"), ("Transferencia recibida", "Transferência recebida"),
    ("Ajuste registrado después del balance", "Ajuste lançado depois do balancete"), ("sin cobrar", "não compensado"), ("pagado", "compensado"),
    ("Venta", "Venda"), ("Cobro", "Recebimento"), ("Pago", "Pagamento"), ("Cheque", "Cheque"),
    ("Cobro ", "Recebimento "), ("Pago ", "Pagamento "),
    ("Cerrar los módulos de ventas, compras e inventarios", "Fechar os módulos de vendas, compras e estoques"),
    ("Conciliar cada cuenta bancaria", "Conciliar cada conta bancária"),
    ("Cruzar las facturas emitidas con las ventas", "Conferir as notas fiscais emitidas com as vendas"),
    ("Conciliar cartera contra su auxiliar", "Conciliar contas a receber com o razão auxiliar"),
    ("Registrar provisiones y causaciones", "Lançar provisões e apropriações"),
    ("Preparar los papeles de trabajo de impuestos", "Preparar os papéis de trabalho de tributos"),
    ("Cuadrar el balance de comprobación", "Fechar o balancete de verificação"),
    ("Revisar el cierre y sus soportes", "Revisar o fechamento e seus comprovantes"),
    ("Aprobar el cierre del periodo", "Aprovar o fechamento do período"),
    ("Contabilidad", "Contabilidade"), ("Tesorería", "Tesouraria"), ("Impuestos", "Tributos"), ("Contraloría", "Controladoria"),
    ("Soporte firmado", "Comprovante assinado"), ("cumplida", "concluída"), ("en curso", "em andamento"), ("pendiente", "pendente"),
    ("baja", "baixa"),
    ("Conciliaciones bancarias de septiembre", "Conciliações bancárias de setembro"),
    ("Auxiliar de cartera con antigüedad", "Razão auxiliar de contas a receber por vencimento"),
    ("Detalle de facturas emitidas", "Detalhe das notas fiscais emitidas"),
    ("Actas del comité de presupuesto", "Atas do comitê de orçamento"),
    ("Contratos de los proveedores principales", "Contratos dos principais fornecedores"),
    ("Detalle de las partidas conciliatorias de más de 90 días", "Detalhe dos itens de conciliação com mais de 90 dias"),
    ("caja_minima", "caixa_minimo"), ("aprobadores", "aprovadores"), ("limite_exposicion", "limite_exposicao"), ("tasa", "taxa"),
    ("Tesorera", "Tesoureira"), ("Gerente financiero", "Gerente financeiro"), ("Contralora", "Controller"),
    ("Proveedor de servicios", "Fornecedor de serviços"), ("Arrendador", "Locador"), ("Proveedor de tecnología", "Fornecedor de tecnologia"),
    ("Contratista de obra", "Empreiteira"), ("Crédito de tesorería", "Capital de giro"), ("Inversión a término", "CDB"),
    ("Banco del Norte", "Banco Bandeirante"), ("Banco del Sur", "Banco do Litoral"), ("deuda", "divida"), ("inversion", "investimento"),
    ("Razón corriente", "Liquidez corrente"), ("Endeudamiento", "Endividamento"),
    ("Revisar el contrato de vigilancia", "Revisar o contrato de vigilância"),
] + [(f" de {m}", f" de {n}") for m, n in zip(F.N.MESES_LARGO, F.N.MESES_LARGO_PT)]
FRASES_PT.sort(key=lambda x: -len(x[0]))
EXACTAS_PT = dict(FRASES_PT)


# Los valores de la ficha que el skill define y el agente escribe igual en cualquier idioma: la
# clave no los traduce (CFO-11).
VALORES_DE_FICHA = {"en curso", "cerrado", "pendiente", "cumplida", "dentro", "abierto"}


def tr(v):
    """Una celda o un texto en el idioma de la entidad: la frase entera si está, si no cada frase
    conocida dentro del texto, de la más larga a la más corta."""
    if LANG[0] != "pt" or not isinstance(v, str) or not v:
        return v
    if v in EXACTAS_PT:
        return EXACTAS_PT[v]
    for a, b in FRASES_PT:
        if len(a) > 4 and a in v:
            v = v.replace(a, b)
    return v


# Los archivos con su nombre en portugués; la carpeta es la de la plataforma.
ARCHIVOS_PT = [("libro-mayor", "livro-razao"), ("balance-comprobacion", "balancete"), ("auxiliar-libros", "auxiliar-livros"),
               ("extracto", "extrato"), ("2205-proveedores", "2205-fornecedores"), ("checklist-cierre", "checklist-fechamento"),
               ("correo-estado-del-cierre", "email-situacao-do-fechamento"), ("-soporte", "-suporte"), ("-respuesta", "-resposta"),
               ("presupuesto-2026-v", "orcamento-2026-v"), ("mapeo-presupuesto", "mapeamento-orcamento"), ("compromisos-", "compromissos-"),
               ("proyeccion-", "projecao-"), ("correo-administracion", "email-administracao"), ("acta-01-aprobacion", "ata-01-aprovacao"),
               ("acta-05-traslado", "ata-05-remanejamento"), ("acta-06-comite", "ata-06-comite"), ("plan-de-cuentas", "plano-de-contas"),
               ("politica-tesoreria", "politica-tesouraria"), ("matriz-firmas", "matriz-assinaturas"), ("registro-deuda", "registro-divida"),
               ("flujo-proyectado", "fluxo-projetado"), ("programa-pagos", "programa-pagamentos"),
               ("-administracion-", "-administracao-"), ("-operaciones-", "-operacoes-"), ("-personal-", "-pessoal-")]


def renombrar_pt(docs: Path) -> dict[str, str]:
    """Cada archivo con su nombre en portugués. Devuelve {ruta vieja: ruta nueva}, relativas a la
    carpeta de la entidad, para que la clave cite el archivo como queda."""
    cambios = {}
    for f in sorted(docs.rglob("*")):
        if not f.is_file():
            continue
        nombre = f.name
        for a, b in ARCHIVOS_PT:
            nombre = nombre.replace(a, b)
        if nombre != f.name:
            nuevo = f.with_name(nombre)
            f.rename(nuevo)
            cambios[f.relative_to(docs).as_posix()] = nuevo.relative_to(docs).as_posix()
    return cambios


def doc(es: str, pt: str) -> str:
    """Un documento escrito en el idioma de la entidad."""
    return pt if LANG[0] == "pt" else es


# Qué pasa a qué formato, y en qué proporción. Las tablas que una organización lleva en Excel —el
# mayor, el balance, el presupuesto, los extractos que baja del banco— y los documentos que circulan
# en Word o PDF —actas, soportes, respuestas al auditor—. Los correos quedan como texto.
FORMATOS = (
    ("libro-mayor", ".xlsx", 0.5), ("balance-comprobacion", ".xlsx", 0.6), ("extracto", ".xlsx", 0.5),
    ("extracto", ".pdf", 0.5), ("auxiliar", ".xlsx", 0.3), ("checklist-cierre", ".xlsx", 0.5), ("pbc-", ".xlsx", 0.5),
    ("presupuesto-", ".xlsx", 0.7), ("compromisos-", ".xlsx", 0.5), ("proyeccion-", ".xlsx", 0.4),
    ("programa-pagos", ".xlsx", 0.5), ("flujo-proyectado", ".xlsx", 0.5), ("matriz-firmas", ".xlsx", 0.5),
    ("registro-deuda", ".xlsx", 0.5), ("covenants", ".xlsx", 0.4),
    ("acta-", ".docx", 0.6), ("-soporte", ".pdf", 0.6), ("-respuesta", ".docx", 0.5),
)
_SERIE = dt.date(1899, 12, 30)


def _celda(ref: str, v: str) -> str:
    """Un número como número y una fecha como fecha de Excel; lo demás, texto."""
    if v.count("-") == 2 and len(v) == 10 and v[:4].isdigit():
        try:
            return f'<c r="{ref}" s="1"><v>{(dt.date.fromisoformat(v) - _SERIE).days}</v></c>'
        except ValueError:
            pass
    if v and v.lstrip("-").replace(".", "", 1).isdigit() and not (len(v) > 1 and v.lstrip("-")[0] == "0" and "." not in v):
        return f'<c r="{ref}"><v>{v}</v></c>'      # el número tal cual: Excel guarda el valor, no su formato
    return f'<c r="{ref}" t="inlineStr"><is><t>{FMT.escape(v)}</t></is></c>'


def a_excel(origen: Path, destino: Path) -> None:
    """Un CSV del material como lo guarda Excel: una hoja, números y fechas con su tipo."""
    import zipfile
    filas = list(csv.reader(origen.read_text(encoding="utf-8").splitlines(), delimiter=";"))
    hoja = "".join(f'<row r="{r}">' + "".join(_celda(f"{FMT._col(c)}{r}", v) for c, v in enumerate(fila)) + "</row>"
                   for r, fila in enumerate(filas, start=1))
    S = 'xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"'
    R = 'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"'
    rel = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
    with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr(FMT._fijo("[Content_Types].xml"),
                   '<?xml version="1.0" encoding="UTF-8"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
                   '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
                   '<Default Extension="xml" ContentType="application/xml"/>'
                   '<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>'
                   '<Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>'
                   '<Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/></Types>')
        z.writestr(FMT._fijo("_rels/.rels"), f'<?xml version="1.0" encoding="UTF-8"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
                   f'<Relationship Id="rId1" Type="{rel}/officeDocument" Target="xl/workbook.xml"/></Relationships>')
        z.writestr(FMT._fijo("xl/workbook.xml"), f'<?xml version="1.0" encoding="UTF-8"?><workbook {S} {R}><sheets>'
                   f'<sheet name="Hoja1" sheetId="1" r:id="rId1"/></sheets></workbook>')
        z.writestr(FMT._fijo("xl/_rels/workbook.xml.rels"), f'<?xml version="1.0" encoding="UTF-8"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
                   f'<Relationship Id="rId1" Type="{rel}/worksheet" Target="worksheets/sheet1.xml"/>'
                   f'<Relationship Id="rId2" Type="{rel}/styles" Target="styles.xml"/></Relationships>')
        z.writestr(FMT._fijo("xl/styles.xml"), f'<?xml version="1.0" encoding="UTF-8"?><styleSheet {S}>'
                   '<fonts count="1"><font><sz val="11"/><name val="Calibri"/></font></fonts>'
                   '<fills count="1"><fill><patternFill patternType="none"/></fill></fills>'
                   '<borders count="1"><border/></borders><cellStyleXfs count="1"><xf/></cellStyleXfs>'
                   '<cellXfs count="2"><xf/><xf numFmtId="14" applyNumberFormat="1"/></cellXfs></styleSheet>')
        z.writestr(FMT._fijo("xl/worksheets/sheet1.xml"), f'<?xml version="1.0" encoding="UTF-8"?><worksheet {S}><sheetData>{hoja}</sheetData></worksheet>')


def _cifra(v: str) -> str:
    """Una cifra como la imprime un banco de la región: punto de miles y coma decimal."""
    x = float(v)
    return f"{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def a_pdf_extracto(origen: Path, destino: Path) -> None:
    """Un extracto del material como lo entrega el banco en PDF: con texto, el título de la cuenta,
    la cabecera en cada página y las cifras alineadas a la derecha."""
    with open(origen, encoding="utf-8") as fh:
        filas = list(csv.reader(fh, delimiter=";"))
    cab = filas[0]
    num = {i for i, c in enumerate(cab) if c in ("valor", "saldo", "debito", "credito")}     # iguales en portugués
    cuerpo = [[_cifra(v) if i in num and v else v for i, v in enumerate(f)] for f in filas[1:]]
    # El ancho de cada columna sale de su texto más largo, con aire entre una y otra: un banco no
    # imprime una celda pegada a la siguiente.
    xs, x = [], 40
    for i, c in enumerate(cab):
        largo = max(sum(F.N._ANCHO.get(ch, 556) for ch in str(v)) * 8 / 1000 for v in [c] + [f[i] for f in cuerpo])
        ancho = largo + 18
        xs.append((x + largo, "d") if i in num else (x, "i"))
        x += ancho
    titulo = ([f"Extrato da conta · {origen.parent.name}", f"Período {origen.parent.parent.parent.name}"] if LANG[0] == "pt" else
              [f"Extracto de cuenta · {origen.parent.name}", f"Periodo {origen.parent.parent.parent.name}"])
    F.N._pdf_tabla(destino, titulo, [[c.capitalize() for c in cab]] + cuerpo, xs)


def formatos_reales(docs: Path, sal: str) -> dict[str, str]:
    """Convierte parte del material a Excel, Word y PDF. Devuelve {ruta vieja: ruta nueva}, relativas
    a la carpeta de la entidad, para que la clave cite el archivo como queda."""
    cambios = {}
    for f in sorted(docs.rglob("*")):
        if not f.is_file() or f.suffix not in (".csv", ".md"):
            continue
        for clave, ext, prop in FORMATOS:
            if clave not in f.name:
                continue
            tabla = f.suffix == ".csv"
            # Todos los extractos se llaman igual: el sorteo va por cuenta, no por nombre de archivo.
            quien = Path(f"{f.parent.name}-{f.name}") if clave == "extracto" else f
            if ext == ".pdf" and tabla and clave == "extracto":      # el extracto que el banco entrega en PDF
                if not FMT._toca(quien, prop, sal=sal + "-pdf"):
                    break
            elif (ext == ".xlsx") != tabla or not FMT._toca(quien, prop, sal=sal):
                if ext == ".xlsx" and clave == "extracto":
                    continue                                       # el que no pasa a Excel puede llegar en PDF
                break
            nuevo = f.with_suffix(ext)
            if ext == ".xlsx":
                a_excel(f, nuevo)
            elif tabla:
                a_pdf_extracto(f, nuevo)
            else:
                {".docx": FMT.a_docx, ".pdf": FMT.a_pdf}[ext](f.read_text(encoding="utf-8"), nuevo)
            f.unlink()
            cambios[f.relative_to(docs).as_posix()] = nuevo.relative_to(docs).as_posix()
            break
    return cambios


# La tesorería de Áurea (ADR 0016): qué se siembra en cada entidad. Las de control no llevan nada, y
# cada una de las siete señales queda sembrada al menos una vez.
TESORERIA = {
    "banca": ["caja_bajo_minimo", "pago_sin_aprobacion", "covenant_riesgo"],
    "cooperativas": ["caja_desviada", "firmante_sin_facultad", "vencimiento_cercano"],
    "retail": ["exposicion", "vencimiento_cercano"],
    "mineria": ["covenant_riesgo", "pago_sin_aprobacion", "caja_desviada"],
    "banca-pe": ["exposicion", "firmante_sin_facultad", "vencimiento_cercano"],
    "mineria-pe": ["caja_bajo_minimo", "covenant_riesgo", "caja_desviada"],
    "retail-cl": ["exposicion", "pago_sin_aprobacion", "vencimiento_cercano"],
    "mineria-cl": ["covenant_riesgo", "caja_bajo_minimo", "firmante_sin_facultad"],
    "banca-mx": ["exposicion", "caja_desviada", "pago_sin_aprobacion"],
    "retail-mx": ["vencimiento_cercano", "covenant_riesgo", "firmante_sin_facultad"],
    "retail-br": ["exposicion", "pago_sin_aprobacion", "vencimiento_cercano"],
    "mineria-br": ["covenant_riesgo", "caja_bajo_minimo", "firmante_sin_facultad"],
    "retail-ar": ["exposicion", "caja_desviada", "firmante_sin_facultad"],
    "mineria-ar": ["covenant_riesgo", "pago_sin_aprobacion", "vencimiento_cercano"],
    "banca-pa": ["caja_bajo_minimo", "firmante_sin_facultad", "covenant_riesgo"],
    "retail-pa": ["pago_sin_aprobacion", "caja_desviada", "vencimiento_cercano"],  # en dólares: sin exposición cambiaria al dólar
    "retail-gt": ["exposicion", "pago_sin_aprobacion", "vencimiento_cercano"],
    "mineria-gt": ["covenant_riesgo", "caja_bajo_minimo", "firmante_sin_facultad"],
    "banca-cr": ["exposicion", "firmante_sin_facultad", "covenant_riesgo"],
    "retail-cr": ["caja_bajo_minimo", "pago_sin_aprobacion", "vencimiento_cercano"],
    "banca-hn": ["exposicion", "firmante_sin_facultad", "covenant_riesgo"],
    "retail-hn": ["caja_bajo_minimo", "pago_sin_aprobacion", "vencimiento_cercano"],
}


def tesoreria(e: dict, docs: Path, esperado: list) -> tuple[dict, list]:
    """La política, la matriz de firmas, la deuda, los covenants, el programa de pagos y el flujo
    proyectado de la entidad, sobre los extractos y el balance que ya generó el cierre."""
    s = TESORERIA.get(e["carpeta"], [])
    esc, hoy = e["escala"], dt.date.fromisoformat(HOY)
    saldos = {}
    for sub in sorted(x for x in (docs / PERIODO / "20-bancos").iterdir() if x.is_dir()):
        ex = F.buscar(sub, "extracto")
        if ex:
            v, _, _ = F._saldo_final(ex[0])
            if v is not None:
                saldos[sub.name] = v
    cuentas = sorted(saldos)
    politica = [["concepto", "referencia", "valor"]]
    for i, c in enumerate(cuentas):
        v = saldos[c]
        minimo = v + abs(v) * 0.2 + esc if ("caja_bajo_minimo" in s and i == 0) else v - abs(v) * 0.5 - esc
        politica.append(["caja_minima", c, r2(minimo)])
        if "caja_bajo_minimo" in s and i == 0:
            esperado.append(("cash_below_minimum", f"caja:{c.lower()}"))
    politica += [["aprobadores", "0", 1], ["aprobadores", esc * 20, 2]]
    monedas = {}
    if "exposicion" in s and cuentas:
        c = cuentas[-1]
        monedas[c] = "USD"
        # Una tasa de referencia del orden de la real para la moneda funcional: con 1, la política
        # parecía decir que la funcional era el dólar (CFO-10). Es material de prueba, no una cotización.
        tasa = {"COP": 4000, "PEN": 3.75, "CLP": 950, "MXN": 18.5, "BRL": 5.4, "ARS": 1450, "GTQ": 7.7, "CRC": 505, "HNL": 26}.get(e["moneda"], 1)
        politica += [["tasa", "USD", tasa], ["limite_exposicion", "USD", r2(abs(saldos[c]) * tasa * 0.5)]]
        esperado.append(("fx_exposure_over_limit", "exposicion:USD"))
    # Cada extracto dice su moneda, como lo imprime el banco: es de donde la toma una tesorería, y el
    # agente no la puede saber si solo está en la clave (CFO-5).
    for sub in sorted(x for x in (docs / PERIODO / "20-bancos").iterdir() if x.is_dir()):
        ex = sub / "extracto.csv"
        if ex.is_file():
            with open(ex, encoding="utf-8") as fh:
                filas = list(csv.reader(fh, delimiter=";"))
            m = monedas.get(sub.name, e["moneda"])
            csv_(ex, [filas[0] + ["moneda"]] + [f + [m] for f in filas[1:]])
    csv_(docs / "00-referencia" / "politica-tesoreria.csv", politica)
    csv_(docs / "00-referencia" / "matriz-firmas.csv", [["nombre", "cargo", "monto_maximo"],
         ["Ana Ruiz", "Tesorera", esc * 25], ["Luis Mora", "Gerente financiero", esc * 100], ["Sofía León", "Contralora", esc * 100]])
    flujo = [["cuenta", "saldo_proyectado"]]
    for i, c in enumerate(cuentas):
        v = saldos[c]
        desviada = "caja_desviada" in s and i == len(cuentas) - 1 and v
        flujo.append([c, r2(v * 1.3 if desviada else v)])
        if desviada:
            esperado.append(("cash_vs_forecast", f"proyeccion:{c.lower()}"))
    csv_(docs / PERIODO / "60-tesoreria" / "flujo-proyectado.csv", flujo)
    pagos = [["id", "fecha", "beneficiario", "valor", "aprobado_por"],
             ["P-1", (hoy + dt.timedelta(days=2)).isoformat(), "Proveedor de servicios", esc * 5, "Ana Ruiz"],
             ["P-2", (hoy + dt.timedelta(days=3)).isoformat(), "Arrendador", esc * 8, "Ana Ruiz"],
             ["P-3", (hoy + dt.timedelta(days=4)).isoformat(), "Proveedor de tecnología", esc * 12,
              "Carlos Paz" if "firmante_sin_facultad" in s else "Ana Ruiz"],
             ["P-4", (hoy + dt.timedelta(days=6)).isoformat(), "Contratista de obra", esc * 30,
              "Luis Mora" if "pago_sin_aprobacion" in s else "Luis Mora; Sofía León"]]
    if "firmante_sin_facultad" in s:
        esperado.append(("signatory_without_authority", "firma:P-3:carlos_paz"))
    if "pago_sin_aprobacion" in s:
        esperado.append(("payment_without_approval", "pago:P-4"))
    csv_(docs / PERIODO / "60-tesoreria" / "programa-pagos.csv", pagos)
    credito = "Crédito de tesorería"
    deuda = [["obligacion", "tipo", "contraparte", "saldo", "moneda", "vencimiento"],
             [credito, "deuda", "Banco del Norte", esc * 400, e["moneda"],
              (hoy + dt.timedelta(days=20 if "vencimiento_cercano" in s else 90)).isoformat()],
             ["Inversión a término", "inversion", "Banco del Sur", esc * 150, e["moneda"], (hoy + dt.timedelta(days=200)).isoformat()]]
    if "vencimiento_cercano" in s:
        esperado.append(("maturity_near", f"vence:{F.norm(credito)}"))
    csv_(docs / "00-referencia" / "registro-deuda.csv", deuda)
    # Los covenants, desde el mismo balance que cierra Clara: lejos del límite, salvo el sembrado.
    cfg_b = {"_docs": docs}
    bal = F.saldos_balance(cfg_b, PERIODO)

    def suma(prefijos):
        return abs(sum(v for c, (v, _, _) in bal.items() if v is not None and any(c.startswith(p) for p in prefijos)))
    rc_num, rc_den = suma(["11", "13", "14"]), suma(["21", "22", "23", "24", "25"])
    en_num, en_den = suma(["2"]), suma(["1"])
    cov = [["obligacion", "indicador", "numerador", "denominador", "operador", "limite"]]
    if rc_den:
        rc = rc_num / rc_den
        riesgo = "covenant_riesgo" in s
        cov.append([credito, "Razón corriente", "11;13;14", "21;22;23;24;25", ">=", round(rc * (0.95 if riesgo else 0.5), 4)])
        if riesgo:
            esperado.append(("covenant_at_risk", f"covenant:{F.norm(credito)}:{F.norm('Razón corriente')}"))
    if en_den:
        cov.append([credito, "Endeudamiento", "2", "1", "<=", round(en_num / en_den * 2, 4)])
    csv_(docs / "00-referencia" / "covenants.csv", cov)
    return {"treasury": {"currencies": monedas}}, s


def factura_pdf_hn(x: dict, emisor: str, cliente: str, destino: Path) -> None:
    """La factura de Honduras como la imprime el emisor, con los requisitos de los artículos 10 y 11
    del Acuerdo 481-2017 (F-37): un PDF con texto, que el agente extrae a la ficha."""
    cifra = lambda v: f"L {v:,.2f}"  # noqa: E731
    lineas = [
        ("FACTURA", 16), (emisor, 12), (f"RTN: {x['issuer_rtn']}", 10), ("", 10),
        (f"CAI: {x['cai']}", 10),
        (f"Rango autorizado: del {x['authorized_range']['from']} al {x['authorized_range']['to']}", 10),
        (f"Fecha límite de emisión: {dt.date.fromisoformat(x['issue_deadline']).strftime('%d/%m/%Y')}", 10),
        (f"Factura N.º {x['number']}", 12),
        (f"Fecha de emisión: {dt.date.fromisoformat(x['date']).strftime('%d/%m/%Y')}", 10), ("", 10),
        (f"Cliente: {cliente}", 10), (f"RTN del cliente: {x['customer_rtn']}", 10), ("", 10),
        (f"Subtotal gravado 15 %: {cifra(x['taxable'])}", 10),
        (f"ISV 15 %: {cifra(x['isv'])}", 10),
        (f"Total: {cifra(x['total'])}", 12), ("", 10),
        ("Original: Cliente · Copia: Obligado tributario emisor", 9),
    ]
    destino.parent.mkdir(parents=True, exist_ok=True)
    FMT.pdf_de_lineas(lineas, destino)


def generar(e: dict) -> dict:
    rnd = random.Random(e["semilla"])
    s = set(e["siembra"])
    pais, esc, tasa = e["pais"], e["escala"], TASA[e["pais"]]
    LANG[0] = "pt" if pais == "BR" else "es"
    if pais == "BR":
        # El ICMS forma parte del valor de la operación (F-21, I11, p. 18): la alícuota es sobre el valor
        # con el impuesto, y sobre la base sin él es t / (1 − t).
        tasa = tasa / (1 - tasa)
    lector = F.FACTURA[pais]["lector"]
    dian = lector == "dian"
    # El nombre de cada parte en la factura impresa de Honduras; el de la entidad es el suyo.
    nombre_de = lambda rtn: e["nombre"] if rtn == e["id"] else f"Suministros Sintéticos {rtn[-4:]}, S. de R.L."  # noqa: E731
    sesion = SALIDA / e["carpeta"]
    ent_dir = f"{e['id']}-{F.norm(e['nombre']).replace('_', '-')}"
    docs = sesion / "finanzas" / ent_dir
    p = docs / PERIODO
    pr = docs / f"presupuesto-{ANIO}"
    esperado: list[tuple[str, str]] = []
    extraccion = {"cierre": {}, "presupuesto": {"minutes": [], "area_statements": [], "reports": [], "committee_commitments": []}}
    fin_sep = dt.date(2026, 9, 30)

    def tercero(i: int) -> str:
        if lector == "sunat":
            return ruc(20, e["semilla"], i)
        if lector == "sii":
            return F.rut(77000000 + e["semilla"] * 1000 + i)
        if lector == "sat":
            return F.rfc("PRV", f"{10 + e['semilla'] % 10:02d}{1 + i % 12:02d}{1 + i % 28:02d}", f"{chr(65 + i % 26)}{e['semilla'] % 10}{i % 10}")
        if lector == "nfe":
            return F.cnpj(int(f"{e['semilla']:02d}{i:06d}"))
        if lector == "wsfe":
            return F.cuit(30, int(f"{e['semilla']:02d}{i:06d}"))
        if lector == "dgipa":
            return F.ruc_pa(e["semilla"] * 1000 + i)
        if lector == "fel":
            return F.nit_gt(e["semilla"] * 100000 + i)
        if lector == "cr":
            return F.cedula_cr(e["semilla"] * 1000 + i)
        if lector == "hn":
            return F.rtn_hn(e["semilla"] * 1000 + i)
        return (f"8{e['semilla']:02d}{i:06d}" if dian else f"17{e['semilla']:02d}{i:06d}001")

    def numero_doc(prefijo: str, i: int) -> str:
        if lector == "sunat":                                  # F-13: serie de cuatro, empieza por F, y número
            return f"F{'001' if prefijo == '99' else '002'}-{i:08d}"
        if lector == "sii":                                    # F-16: el folio es numérico, hasta 10 dígitos
            return f"{1 if prefijo == '99' else 2}{i:06d}"
        if lector == "sat":                                    # F-19: serie y folio de control interno
            return f"{'A' if prefijo == '99' else 'B'}{i:06d}"
        if lector == "nfe":                                    # F-21: serie y número de la NF-e
            return f"{'1' if prefijo == '99' else '2'}-{i}"
        if lector == "wsfe":                                   # F-24: punto de venta y número del comprobante
            return f"{'00001' if prefijo == '99' else '00002'}-{i:08d}"
        if lector == "dgipa":                                  # F-27: punto de facturación y número fiscal
            return f"{'001' if prefijo == '99' else '002'}-{i:010d}"
        if lector == "fel":                                    # F-30: la serie y el número de la autorización
            return f"{'A1F0' if prefijo == '99' else 'B2E0'}{e['semilla']:02d}AB-{1000000 + i}"
        if lector == "cr":                                     # F-34: sucursal, terminal, tipo 01 y número de diez
            return f"{'001' if prefijo == '99' else '002'}0000101{i:010d}"
        if lector == "hn":                                     # F-37, art. 10: establecimiento, punto de emisión, tipo 01 y correlativo
            return f"{'000' if prefijo == '99' else '001'}-001-01-{i:08d}"
        return f"SETP{prefijo}{i:06d}" if dian else f"{'001' if prefijo == '99' else '002'}-001-{i:09d}"

    def factura_xml(numero: str, fecha: dt.date, emisor: str, receptor: str, base: float, iva: float) -> str:
        if dian:
            cufe = hashlib.sha384(f"{numero}{emisor}{base}".encode()).hexdigest()
            return F.contenedor_dian(F.factura_dian(numero, cufe, fecha.isoformat(), emisor, receptor, base, iva))
        if lector == "sunat":
            return F.factura_sunat(numero, fecha.isoformat(), emisor, receptor, base, iva)
        if lector == "sii":
            return F.factura_sii(numero, fecha.isoformat(), emisor, receptor, base, iva)
        if lector == "sat":
            return F.factura_sat(numero[0], numero[1:], fecha.isoformat(), emisor, receptor, base, iva)
        if lector == "nfe":
            serie, nnf = numero.split("-")
            vnf = base + iva
            return F.factura_nfe(serie, nnf, fecha.isoformat(), emisor, receptor, base, iva, r2(vnf * 0.0065), r2(vnf * 0.03))
        if lector == "wsfe":
            pto, nro = numero.split("-")
            return F.factura_wsfe(int(pto), int(nro), fecha.isoformat(), emisor, receptor, base, iva)
        if lector == "dgipa":
            pto, nro = numero.split("-")
            return F.factura_dgipa(pto, int(nro), fecha.isoformat(), emisor, receptor, base, iva)
        if lector == "fel":
            serie, nro = numero.split("-")
            return F.factura_fel(serie, int(nro), fecha.isoformat(), emisor, receptor, base, iva)
        if lector == "cr":
            return F.factura_cr(numero, fecha.isoformat(), emisor, receptor, base, iva)
        if lector == "hn":
            # Honduras no tiene XML (decisión 0024): la factura es un PDF con su CAI, su rango autorizado
            # y su fecha límite de emisión (F-37, art. 10), y el agente la extrae a la ficha.
            pre = numero.rsplit("-", 1)[0]
            return {"number": numero, "cai": F.cai_hn(f"{emisor}:{pre}"), "authorized_range": {"from": f"{pre}-00000001", "to": f"{pre}-00000500"},
                    "issue_deadline": "2026-12-31", "date": fecha.isoformat(), "issuer_rtn": emisor, "customer_rtn": receptor,
                    "taxable": base, "isv": iva, "total": r2(base + iva)}
        estab, pto, sec = numero.split("-")
        return F.factura_sri(fecha, emisor, estab, pto, sec, receptor, base, iva)

    mayor_sep: list[list] = []          # fecha, comprobante, cuenta, tercero, documento, debito, credito, centro_costo, descripcion
    asiento = [0]

    def asentar(fecha, lineas, prefijo="A"):
        asiento[0] += 1
        comp = f"{prefijo}-{asiento[0]:03d}"
        for cuenta, ter, doc, d, c, cc, desc in lineas:
            mayor_sep.append([fecha.isoformat(), comp, cuenta, ter, doc, r2(d), r2(c), cc, desc])
        return comp

    # ------------------------------------------------ el presupuesto y la ejecución de enero a agosto
    v1 = {(a, l): [round(m * esc, 2)] * 12 for a, l, _, _, m in LINEAS}
    v2 = {k: list(v) for k, v in v1.items()}
    T = round(0.5 * esc, 2)                                   # traslado aprobado Publicidad → Eventos, julio a diciembre
    for mes in range(6, 12):
        v2[("Comercial", "Publicidad")][mes] = r2(v2[("Comercial", "Publicidad")][mes] - T)
        v2[("Comercial", "Eventos")][mes] = r2(v2[("Comercial", "Eventos")][mes] + T)
    if "traslado_sin_acta" in s:
        U = round(0.8 * esc, 2)
        for mes in range(6, 12):
            v2[("Tecnología", "Licencias")][mes] = r2(v2[("Tecnología", "Licencias")][mes] - U)
            v2[("Operaciones", "Transporte")][mes] = r2(v2[("Operaciones", "Transporte")][mes] + U)
        esperado += [("transfer_without_approval", "traslado:2:Tecnología:Licencias"), ("transfer_without_approval", "traslado:2:Operaciones:Transporte")]
    factor = {k: 0.97 for k in v1}
    factor[("Personal", "Nómina")] = 1.0
    if "desviacion" in s:
        # Si un área declara que va dentro, la desviación cae en ella: eso es lo que la declaración no sostiene.
        k = ("Administración", "Servicios públicos") if "area_declara_dentro" in s else ("Operaciones", "Transporte")
        factor[k] = 1.15
        esperado.append(("variance_over_threshold", f"var:{k[0]}:{k[1]}"))
    real = {k: [r2(v2[k][m] * factor[k]) for m in range(9)] for k in v1}
    cab_pres = ["area", "linea", "cuenta", "centro_costo"] + F.MESES + ["total"]
    for n, v, fecha in ((1, v1, "2026-01-15"), (2, v2, "2026-06-30")):
        csv_(pr / "10-aprobado" / f"presupuesto-{ANIO}-v{n}-{fecha}.csv",
             [cab_pres] + [[a, l, c, cc] + v[(a, l)] + [r2(sum(v[(a, l)]))] for a, l, c, cc, _ in LINEAS])
    csv_(docs / "00-referencia" / "mapeo-presupuesto.csv", [["cuenta", "centro_costo", "area", "linea"]] + [[c, cc, a, l] for a, l, c, cc, _ in LINEAS])
    acumulado = {c: 0.0 for c in NOMBRES}
    for mes in range(1, 9):
        filas = [["fecha", "comprobante", "cuenta", "tercero", "documento", "debito", "credito", "centro_costo", "descripcion"]]
        for i, (a, l, c, cc, _) in enumerate(LINEAS):
            v = real[(a, l)][mes - 1]
            f = dt.date(2026, mes, 25).isoformat()
            filas += [[f, f"G-{mes:02d}{i}", c, "", "", v, 0.0, cc, f"{l} de {F.MESES_LARGO[mes - 1]}"],
                      [f, f"G-{mes:02d}{i}", "11100501", "", "", 0.0, v, "", f"Pago {l}"]]
            acumulado[c] += v
            acumulado["11100501"] -= v
        if mes == 8 and "gasto_sin_linea" in s:
            v = round(0.7 * esc, 2)
            filas += [["2026-08-28", "G-0899", "5135", "", "", v, 0.0, "ZZZ", "Servicio sin centro de costo"],
                      ["2026-08-28", "G-0899", "11100501", "", "", 0.0, v, "", "Pago"]]
            acumulado["5135"] += v
            acumulado["11100501"] -= v
            esperado.append(("spend_without_budget_line", "sinlinea:2026-08:5135:ZZZ"))
        csv_(docs / f"2026-{mes:02d}" / "10-contabilidad" / "libro-mayor.csv", filas)

    # ------------------------------------------------ saldos de apertura de septiembre
    abiertas_cxc = [(dt.date(2026, 8, 10 + i), tercero(100 + i), numero_doc("99", 90 + i), r2(rnd.randint(8, 20) * esc / 4)) for i in range(3)]
    abiertas_cxp = [(dt.date(2026, 8, 12 + i), tercero(300 + i), numero_doc("77", 50 + i), r2(rnd.randint(6, 14) * esc / 4)) for i in range(3)]
    banco_ini = {"11100501": r2(80 * esc), "11100502": r2(25 * esc)}
    cheque_viejo = None
    if "cheque_viejo" in s:
        fecha_ch = dt.date(2026, 7, 20) if e["carpeta"] == "banca" else dt.date(2026, 6, 15)
        cheque_viejo = (fecha_ch, "CH-0450", r2(-3 * esc))
    ini = dict(acumulado)
    ini["11100501"] = r2(ini["11100501"] + banco_ini["11100501"] + 9 * 30 * esc)   # lo que entró en el año, para que el banco quede positivo
    ini["11100502"] = banco_ini["11100502"]
    ini["1305"] = r2(sum(x[3] for x in abiertas_cxc))
    ini["1435"] = r2(40 * esc)
    ini["2205"] = r2(-sum(x[3] for x in abiertas_cxp))
    ini["2408"] = r2(-6 * esc)
    ini["2505"] = 0.0
    ini["4135"] = r2(-9 * 30 * esc)
    ini["5305"] = r2(0.4 * esc * 8)
    ini["3105"] = 0.0
    ini["3105"] = r2(-sum(v for k, v in ini.items() if k != "3105"))

    # ------------------------------------------------ septiembre: ventas, cobros, compras, pagos, nómina, bancos
    banco_libros = {"11100501": [], "11100502": []}            # fecha, referencia, descripción, valor
    banco_extracto = {"11100501": [], "11100502": []}
    xml_emitidas, xml_recibidas = [], []
    ext = ".pdf" if F.FACTURA[pais].get("documento") else ".xml"
    ventas = []
    for i in range(10):
        f = dt.date(2026, 9, 2 + 3 * i if 2 + 3 * i <= 28 else 28)
        base = r2(rnd.randint(10, 40) * esc / 4)
        iva = r2(base * tasa)
        num, ter = numero_doc("99", 100 + i), tercero(100 + i)
        ventas.append((f, ter, num, base, iva))
        iva_libros = iva + (round(1000 if dian else 10, 2) if ("iva_distinto" in s and i == 4) else 0)
        if not ("factura_sin_registro" in s and i == 9):
            asentar(f, [("1305", ter, num, base + iva_libros, 0, "", "Venta"), ("4135", ter, num, 0, base, "", "Venta"),
                        ("2408", ter, num, 0, iva_libros, "", "IVA generado")], "V")
        xml_emitidas.append((f"fe-{num}{ext}", factura_xml(num, f, e["id"], ter, base, iva)))
        if "iva_distinto" in s and i == 4:
            esperado.append(("einvoice_amount_mismatch", f"xml:{PERIODO}/30-facturacion/emitidas/fe-{num}{ext}"))
        if "factura_sin_registro" in s and i == 9:
            esperado.append(("einvoice_not_recorded", f"xml:{PERIODO}/30-facturacion/emitidas/fe-{num}{ext}"))
    if "xml_duplicado" in s:
        nombre, contenido = xml_emitidas[2]
        xml_emitidas.append((nombre.replace(".xml", "-reenviada.xml"), contenido))
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:        # la clave única es la que dice el lector de su país
            unica = F.leer_factura_texto(contenido, Path(tmp))["id"]
        esperado.append(("einvoice_duplicate", f"xml:{unica}"))
    # Cobros: siete facturas de septiembre y dos de agosto. La de IVA distinto y la que no se
    # registró no se cobran: quedan en la cartera.
    cobradas = [v for i, v in enumerate(ventas) if i in (0, 1, 2, 3, 5, 6, 7)] + [(x[0], x[1], x[2], x[3], 0.0) for x in abiertas_cxc[:2]]
    for j, (f, ter, num, base, iva) in enumerate(cobradas):
        total = r2(base + iva)
        fc = max(f, dt.date(2026, 9, 3)) + dt.timedelta(days=2)
        fc = min(fc, dt.date(2026, 9, 29))
        if "consignacion_en_transito" in s and j == 6:
            fc = fin_sep
        asentar(fc, [("11100501", ter, num, total, 0, "", "Cobro"), ("1305", ter, num, 0, total, "", "Cobro")], "R")
        banco_libros["11100501"].append((fc, num, f"Cobro {num}", total))
        if not ("consignacion_en_transito" in s and j == 6):
            ref = num if j % 2 == 0 else f"TRF{j:04d}"
            banco_extracto["11100501"].append((fc + dt.timedelta(days=j % 2), ref, "Transferencia recibida", total))
    if "consignacion_en_transito" in s:
        esperado.append(("bank_unreconciled", "__transito__"))
    # Compras: una factura por línea del presupuesto, salvo la nómina, que va aparte.
    compras = []
    for i, (a, l, c, cc, _) in enumerate(LINEAS):
        if l == "Nómina":
            continue
        f = dt.date(2026, 9, 5 + 2 * i)
        base = real[(a, l)][8]
        iva = r2(base * tasa)
        num, ter = numero_doc("77", 200 + i), tercero(300 + i)
        compras.append((f, ter, num, base, iva, c, cc, a, l))
        veces = 2 if ("registro_doble" in s and l == "Mantenimiento") else 1
        for _ in range(veces):
            asentar(f, [(c, ter, num, base, 0, cc, f"{l} · {num}"), ("2408", ter, num, iva, 0, "", "IVA descontable"),
                        ("2205", ter, num, 0, r2(base + iva), "", "Cuenta por pagar")], "C")
        if veces == 2:
            esperado += [("einvoice_duplicate", f"reg:recibidas:{F.ident(num)}"),
                         ("einvoice_amount_mismatch", f"xml:{PERIODO}/30-facturacion/recibidas/fr-{num}{ext}")]
            real[(a, l)][8] = r2(real[(a, l)][8] * 2)
        if "registro_sin_factura" in s and l == "Publicidad":
            esperado.append(("recorded_without_einvoice", f"reg:recibidas:{F.ident(num)}"))
            continue
        fx = factura_xml(num, f, ter, e["id"], base, iva)
        # Honduras: una factura recibida fuera de su autorización —emitida después de su fecha límite, o
        # con un número fuera de su rango autorizado— no sustenta el crédito fiscal del ISV (decisión 0024).
        if isinstance(fx, dict) and "fuera_de_fecha" in s and i == 1:
            fx["issue_deadline"] = (f - dt.timedelta(days=3)).isoformat()
            esperado.append(("invoice_outside_authorization", f"cai:{PERIODO}/30-facturacion/recibidas/fr-{num}{ext}"))
        if isinstance(fx, dict) and "fuera_de_rango" in s and i == 3:
            pre = num.rsplit("-", 1)[0]
            fx["authorized_range"] = {"from": f"{pre}-00000001", "to": f"{pre}-{int(num.rsplit('-', 1)[1]) - 5:08d}"}
            esperado.append(("invoice_outside_authorization", f"cai:{PERIODO}/30-facturacion/recibidas/fr-{num}{ext}"))
        xml_recibidas.append((f"fr-{num}{ext}", fx))
    if "factura_recibida_sin_registro" in s:
        num, ter, f = numero_doc("77", 290), tercero(390), dt.date(2026, 9, 27)
        xml_recibidas.append((f"fr-{num}{ext}", factura_xml(num, f, ter, e["id"], r2(2 * esc), r2(2 * esc * tasa))))
        esperado.append(("einvoice_not_recorded", f"xml:{PERIODO}/30-facturacion/recibidas/fr-{num}{ext}"))
    # Pagos: las tres cuentas por pagar de agosto y dos compras de septiembre, con cheque.
    pagos = [(x[0] + dt.timedelta(days=30), x[1], x[2], x[3]) for x in abiertas_cxp] + [(c[0] + dt.timedelta(days=6), c[1], c[2], r2(c[3] + c[4])) for c in compras[:2]]
    for j, (f, ter, num, total) in enumerate(pagos):
        f = min(f, dt.date(2026, 9, 26))
        ch = f"CH-{600 + j:04d}"
        asentar(f, [("2205", ter, num, total, 0, "", f"Pago {num}"), ("11100501", ter, ch, 0, total, "", f"Cheque {ch}")], "P")
        banco_libros["11100501"].append((f, ch, f"Cheque {ch}", -total))
        banco_extracto["11100501"].append((f + dt.timedelta(days=2), ch, f"Cheque {ch} pagado", -total))
    # Nómina: se causa y se paga por la segunda cuenta.
    nom = real[("Personal", "Nómina")][8]
    asentar(dt.date(2026, 9, 28), [("5105", "", "", nom, 0, "ADM", "Nómina de septiembre"), ("2505", "", "", 0, nom, "", "Nómina por pagar")], "N")
    asentar(dt.date(2026, 9, 29), [("2505", "", "", nom, 0, "", "Pago de nómina"), ("11100502", "", "NOM-09", 0, nom, "", "Pago de nómina")], "N")
    banco_libros["11100502"].append((dt.date(2026, 9, 29), "NOM-09", "Pago de nómina", -nom))
    banco_extracto["11100502"].append((dt.date(2026, 9, 29), "NOM-09", "Débito nómina", -nom))
    # Una consignación a la segunda cuenta, para que no quede negativa.
    fondeo = r2(nom + 5 * esc)
    asentar(dt.date(2026, 9, 27), [("11100502", "", "TRASLADO-09", fondeo, 0, "", "Traslado entre cuentas"), ("11100501", "", "TRASLADO-09", 0, fondeo, "", "Traslado entre cuentas")], "T")
    banco_libros["11100502"].append((dt.date(2026, 9, 27), "TRASLADO-09", "Traslado recibido", fondeo))
    banco_extracto["11100502"].append((dt.date(2026, 9, 27), "TRASLADO-09", "Traslado recibido", fondeo))
    banco_libros["11100501"].append((dt.date(2026, 9, 27), "TRASLADO-09", "Traslado enviado", -fondeo))
    banco_extracto["11100501"].append((dt.date(2026, 9, 27), "TRASLADO-09", "Traslado enviado", -fondeo))
    # La comisión bancaria del mes.
    com = r2(0.4 * esc)
    banco_extracto["11100501"].append((fin_sep, "", "Comisión de manejo", -com))
    if "comision_sin_registrar" in s:
        esperado.append(("bank_unreconciled", "__comision__"))
    else:
        asentar(fin_sep, [("5305", "", "COM-09", com, 0, "ADM", "Comisión bancaria"), ("11100501", "", "COM-09", 0, com, "", "Comisión bancaria")], "B")
        banco_libros["11100501"].append((fin_sep, "COM-09", "Comisión bancaria", -com))
    if "asiento_fuera_del_balance" in s:
        v = r2(0.15 * esc)
        mayor_extra = [[fin_sep.isoformat(), "A-999", "5195", "", "", v, 0.0, "COM", "Ajuste registrado después del balance"],
                       [fin_sep.isoformat(), "A-999", "2505", "", "", 0.0, v, "", "Ajuste registrado después del balance"]]
        esperado += [("ledger_vs_trial_balance", "mayor:5195"), ("ledger_vs_trial_balance", "mayor:2505")]
    else:
        mayor_extra = []

    # ------------------------------------------------ el balance de comprobación
    mov = {c: [0.0, 0.0] for c in NOMBRES}
    for x in mayor_sep:
        mov[x[2]][0] += x[5]
        mov[x[2]][1] += x[6]
    tb = [["cuenta", "nombre", "saldo_inicial", "debito", "credito", "saldo_final"]]
    for c in sorted(NOMBRES):
        si, d, cr = r2(ini.get(c, 0.0)), r2(mov[c][0]), r2(mov[c][1])
        sf = r2(si + d - cr)
        if c == "5305" and "balance_descuadrado" in s:
            d = r2(d + 5 * esc / 1000)
        tb.append([c, NOMBRES[c], si, d, cr, sf])
    if "balance_descuadrado" in s:
        esperado += [("trial_balance_unbalanced", "balance"), ("ledger_vs_trial_balance", "saldo:5305"), ("ledger_vs_trial_balance", "mayor:5305")]
    cont = p / "10-contabilidad"
    csv_(cont / "balance-comprobacion.csv", tb)
    csv_(cont / "libro-mayor.csv", [["fecha", "comprobante", "cuenta", "tercero", "documento", "debito", "credito", "centro_costo", "descripcion"]] + mayor_sep + mayor_extra)
    saldo_final = {r[0]: r[5] for r in tb[1:]}

    # Los auxiliares: las partidas abiertas de cartera y de proveedores al 30 de septiembre.
    cobradas_docs = {x[2] for x in cobradas}
    cxc = [(x[0], x[1], x[2], x[3]) for x in abiertas_cxc if x[2] not in cobradas_docs]
    for i, (f, ter, num, base, iva) in enumerate(ventas):
        if num in cobradas_docs or ("factura_sin_registro" in s and i == 9):
            continue
        extra = (1000 if dian else 10) if ("iva_distinto" in s and i == 4) else 0
        cxc.append((f, ter, num, r2(base + iva + extra)))
    if "cartera_descuadrada" in s:
        cxc = cxc[1:]
        esperado.append(("account_unreconciled", "cuenta:1305"))
    csv_(cont / "auxiliares" / "1305-clientes.csv", [["fecha", "tercero", "documento", "valor"]] + [[f.isoformat(), t, n, v] for f, t, n, v in cxc])
    pagados = {x[2] for x in pagos}
    cxp = [(x[0], x[1], x[2], -x[3]) for x in abiertas_cxp if x[2] not in pagados]
    for f, ter, num, base, iva, *_ in compras:
        if num not in pagados:
            cxp.append((f, ter, num, -r2(base + iva)))
    if "cuenta_sin_auxiliar" in s:
        esperado.append(("reconciliation_stale", "cuenta:2205"))
    else:
        # El registro doble sube proveedores en el mayor y no en el auxiliar, que trae cada factura
        # una vez: la cuenta no concilia, y eso también se espera.
        if "registro_doble" in s:
            esperado.append(("account_unreconciled", "cuenta:2205"))
        csv_(cont / "auxiliares" / "2205-proveedores.csv", [["fecha", "tercero", "documento", "valor"]] + [[f.isoformat(), t, n, v] for f, t, n, v in cxp])
    # Los auxiliares de agosto, con lo que quedó abierto: así sabe quien configura qué cuentas se
    # concilian cada mes, y la que no trae el de septiembre es la que falta.
    ago = docs / "2026-08" / "10-contabilidad" / "auxiliares"
    csv_(ago / "1305-clientes.csv", [["fecha", "tercero", "documento", "valor"]] + [[f.isoformat(), t, n, v] for f, t, n, v in abiertas_cxc])
    csv_(ago / "2205-proveedores.csv", [["fecha", "tercero", "documento", "valor"]] + [[f.isoformat(), t, n, -v] for f, t, n, v in abiertas_cxp])
    assert abs(sum(x[3] for x in cxc) - saldo_final["1305"]) < 0.01 or "cartera_descuadrada" in s, (e["carpeta"], "cartera")
    assert "cuenta_sin_auxiliar" in s or "registro_doble" in s or abs(sum(x[3] for x in cxp) - saldo_final["2205"]) < 0.01, (e["carpeta"], "proveedores")

    # Los bancos: el extracto y el auxiliar de libros, con su saldo corrido.
    subcarpetas = ({"11100501": f"bandeirante-{e['semilla']:02d}01", "11100502": f"litoral-{e['semilla']:02d}02"} if LANG[0] == "pt" else
                   {"11100501": f"andino-{e['semilla']:02d}01", "11100502": f"pacifico-{e['semilla']:02d}02"})
    for cta, sub in subcarpetas.items():
        lib = sorted(banco_libros[cta], key=lambda x: (x[0], x[1]))
        ext = sorted(banco_extracto[cta], key=lambda x: (x[0], x[1]))
        saldo_lib_ini = r2(ini[cta])
        filas_lib = [["fecha", "documento", "descripcion", "valor", "saldo"]]
        pendientes_ini = 0.0
        if cta == "11100501" and cheque_viejo:
            filas_lib.append([cheque_viejo[0].isoformat(), cheque_viejo[1], f"Cheque {cheque_viejo[1]} sin cobrar", cheque_viejo[2], saldo_lib_ini])
            pendientes_ini = cheque_viejo[2]
            esperado += [("bank_unreconciled", "__viejo__"), ("reconciling_item_aged", "__viejo__")]
        sl = saldo_lib_ini
        for f, ref, desc, v in lib:
            sl = r2(sl + v)
            filas_lib.append([f.isoformat(), ref, desc, v, sl])
        assert abs(sl - saldo_final[cta]) < 0.01, (e["carpeta"], cta, sl, saldo_final[cta])
        sb = r2(saldo_lib_ini - pendientes_ini)
        filas_ext = [["fecha", "referencia", "descripcion", "valor", "saldo"]]
        for f, ref, desc, v in ext:
            sb = r2(sb + v)
            filas_ext.append([f.isoformat(), ref, desc, v, sb])
        carpeta = p / "20-bancos" / sub
        csv_(carpeta / "auxiliar-libros.csv", filas_lib)
        if "banco_sin_extracto" in s and cta == "11100502":
            esperado.append(("reconciliation_stale", f"banco:{sub}"))
        else:
            csv_(carpeta / "extracto.csv", filas_ext)
        # Las claves de las partidas abiertas las pone el motor con el archivo y la fila; se
        # resuelven aquí, donde se sabe qué fila es cada una.
        rel_lib, rel_ext = f"{PERIODO}/20-bancos/{sub}/auxiliar-libros.csv", f"{PERIODO}/20-bancos/{sub}/extracto.csv"
        for k, (sig, marca) in enumerate(esperado):
            if cta != "11100501":
                continue
            if marca == "__viejo__":
                esperado[k] = (sig, f"{sub}:{rel_lib}:2")
            elif marca == "__transito__":
                fila = next(i for i, x in enumerate(filas_lib) if i and x[0] == fin_sep.isoformat() and x[3] > 0) + 1
                esperado[k] = (sig, f"{sub}:{rel_lib}:{fila}")
            elif marca == "__comision__":
                fila = next(i for i, x in enumerate(filas_ext) if i and x[2] == "Comisión de manejo") + 1
                esperado[k] = (sig, f"{sub}:{rel_ext}:{fila}")

    # Las facturas electrónicas. Las de Honduras son documentos: un PDF con texto por factura, y lo
    # que el agente extrae de cada uno va a la clave de la ficha del cierre (decisión 0024).
    for lado, lista in (("emitidas", xml_emitidas), ("recibidas", xml_recibidas)):
        for nombre, contenido in lista:
            if isinstance(contenido, dict):
                destino = p / "30-facturacion" / lado / nombre
                factura_pdf_hn(contenido, nombre_de(contenido["issuer_rtn"]), nombre_de(contenido["customer_rtn"]), destino)
                extraccion["cierre"].setdefault("invoices", {})[f"{contenido['issuer_rtn']}:{contenido['number']}"] = {
                    **contenido, "source": f"{PERIODO}/30-facturacion/{lado}/{nombre}"}
            else:
                md(p / "30-facturacion" / lado / nombre, contenido)

    # ------------------------------------------------ el checklist, los soportes y la auditoría
    md(docs / "00-referencia" / "plan-de-cuentas.csv", doc("cuenta;nombre;naturaleza\n1;Activo;D\n2;Pasivo;C\n3;Patrimonio;C\n4;Ingresos;C\n5;Gastos;D\n6;Costos;D",
                                                            "conta;nome;natureza\n1;Ativo;D\n2;Passivo;C\n3;Patrimônio líquido;C\n4;Receitas;C\n5;Despesas;D\n6;Custos;D"))
    tareas = [
        ("C-01", "Cerrar los módulos de ventas, compras e inventarios", "Contabilidad", "Lucía Mora", "D+1", "", "alta"),
        ("C-02", "Conciliar cada cuenta bancaria", "Tesorería", "Andrés Paz", "D+2", "C-01", "alta"),
        ("C-03", "Cruzar las facturas emitidas con las ventas", "Contabilidad", "Lucía Mora", "D+2", "C-01", "alta"),
        ("C-04", "Conciliar cartera contra su auxiliar", "Contabilidad", "Marta Ríos", "D+3", "C-01", "alta"),
        ("C-05", "Registrar provisiones y causaciones", "Contabilidad", "Jorge Vela", "D+3", "C-01", "media"),
        ("C-06", "Preparar los papeles de trabajo de impuestos", "Impuestos", "Elena Cruz", "D+5", "C-03", "alta"),
        ("C-07", "Cuadrar el balance de comprobación", "Contabilidad", "Lucía Mora", "D+5", "C-02 C-04 C-05", "alta"),
        ("C-08", "Revisar el cierre y sus soportes", "Contraloría", "Sofía León", "D+6", "C-07", "alta"),
        ("C-09", "Aprobar el cierre del periodo", "Contraloría", "Sofía León", "D+7", "C-08", "alta"),
    ]
    sin_soporte = {"C-02"} if "tarea_sin_soporte" in s else set()
    vencida = {"C-05"} if "tarea_vencida" in s else set()
    filas = [["id", "tarea", "area", "responsable", "dia_limite", "depende_de", "evidencia_esperada", "criticidad", "estado"]]
    for tid, t, a, r, lim, dep, cri in tareas:
        lim_d = F._limite(lim, PERIODO, set())
        vence = lim_d <= dt.date.fromisoformat(HOY)
        estado = "cumplida" if vence and tid not in vencida else ("en curso" if not vence else "pendiente")
        filas.append([tid, t, a, r, lim, dep, "Soporte firmado", cri, estado])
        if vence and tid not in vencida and tid not in sin_soporte:
            md(p / "40-soportes" / f"{tid}-soporte.md", doc(f"# {tid} · {t}\n\nFirmado por {r} el {lim_d.isoformat()}.",
                                                           f"# {tid} · {tr(t)}\n\nAssinado por {tr(r)} em {lim_d.isoformat()}."))
    csv_(docs / "00-referencia" / "checklist-cierre.csv", filas)
    esperado += [("close_task_done_without_evidence", f"tarea:{t}") for t in sorted(sin_soporte)]
    esperado += [("close_task_overdue", f"tarea:{t}") for t in sorted(vencida)]
    declarado = "cerrado" if "cierre_declarado" in s else "en curso"
    md(p / "40-soportes" / "correo-estado-del-cierre.md",
       doc(f"De: Sofía León\nPara: Gerencia financiera\nFecha: 2026-10-05\nAsunto: Cierre de septiembre\n\nEl cierre de septiembre está {declarado}.",
           f"De: Sofia Leão\nPara: Diretoria financeira\nData: 2026-10-05\nAssunto: Fechamento de setembro\n\n"
           f"O fechamento de setembro está {'fechado' if declarado == 'cerrado' else 'em andamento'}."))
    # El estado, el «dentro» de un área y el de un compromiso son valores de la ficha, los mismos en
    # cualquier idioma del documento (CFO-11): el agente los escribe así.
    extraccion["cierre"]["declared"] = {"status": declarado, "source": f"{PERIODO}/40-soportes/correo-estado-del-cierre.md", "date": "2026-10-05", "by": "Sofía León"}
    if declarado == "cerrado":
        esperado.append(("declared_close_vs_evidence", "cierre"))
    reqs = [["id", "solicitud", "fecha", "fecha_limite", "responsable", "estado"],
            ["R-01", "Conciliaciones bancarias de septiembre", "2026-10-01", "2026-10-03", "Andrés Paz", "respondido"],
            ["R-02", "Auxiliar de cartera con antigüedad", "2026-10-01", "2026-10-03", "Marta Ríos", "respondido"],
            ["R-03", "Detalle de facturas emitidas", "2026-10-01", "2026-10-03", "Lucía Mora", "respondido"],
            ["R-04", "Actas del comité de presupuesto", "2026-10-02", "2026-10-09", "Sofía León", ""],
            ["R-05", "Contratos de los proveedores principales", "2026-10-01", "2026-10-02" if "requerimiento_vencido" in s else "2026-10-08", "Jorge Vela", ""]]
    for rid in ("R-01", "R-02", "R-03"):
        if not ("requerimiento_sin_soporte" in s and rid == "R-03"):
            md(p / "50-auditoria" / "respuestas" / f"{rid}-respuesta.md", doc(f"# {rid}\n\nEntregado el 2026-10-03.", f"# {rid}\n\nEntregue em 2026-10-03."))
    csv_(p / "50-auditoria" / "requerimientos" / "pbc-2026-09.csv", reqs)
    if "requerimiento_sin_soporte" in s:
        esperado.append(("audit_request_unanswered", "req:R-03"))
    if "requerimiento_vencido" in s:
        esperado.append(("audit_request_unanswered", "req:R-05"))
    if "requerimiento_en_carta" in s:
        md(p / "50-auditoria" / "requerimientos" / "carta-auditor-2026-10-02.md",
           doc("# Carta del auditor\n\nFecha: 2026-10-02\n\nR-09 · Detalle de las partidas conciliatorias de más de 90 días. Fecha límite: 2026-10-09. Responsable: Andrés Paz.",
               "# Carta do auditor\n\nData: 2026-10-02\n\nR-09 · Detalhe dos itens de conciliação com mais de 90 dias. Prazo: 2026-10-09. Responsável: André Pacheco."))
        extraccion["cierre"]["audit_requests"] = [{"id": "R-09", "request": "Detalle de las partidas conciliatorias de más de 90 días", "date": "2026-10-02",
                                                   "due": "2026-10-09", "owner": "Andrés Paz", "status": "", "source": f"{PERIODO}/50-auditoria/requerimientos/carta-auditor-2026-10-02.md"}]

    # ------------------------------------------------ compromisos, proyecciones, actas y declaraciones
    comp = {k: r2(0.3 * v2[k][9]) for k in v1}
    if "comprometido_al_limite" in s:
        k = ("Tecnología", "Licencias") if e["carpeta"] == "cooperativas" else ("Administración", "Mantenimiento")
        ej = sum(real[k])
        comp[k] = r2(0.96 * sum(v2[k]) - ej + 0.01 * esc)
        esperado.append(("committed_near_approved", f"com:{k[0]}:{k[1]}"))
    csv_(pr / "20-compromisos" / "compromisos-2026-09-30.csv",
         [["numero", "fecha", "area", "linea", "proveedor", "valor", "saldo_por_ejecutar"]] +
         [[f"OC-{i:04d}", "2026-09-15", a, l, tercero(500 + i), r2(comp[(a, l)] * 2), comp[(a, l)]] for i, (a, l, *_ ) in enumerate(LINEAS) if comp[(a, l)]])
    areas = sorted({a for a, *_ in LINEAS})
    for area in areas:
        fecha = "2026-07-15" if ("proyeccion_vieja" in s and area == "Operaciones") else "2026-09-30"
        version = "1" if ("version_distinta" in s and area == "Comercial") else "2"
        filas = [["area", "linea", "proyeccion", "version"]]
        for a, l, *_ in LINEAS:
            if a != area:
                continue
            k = (a, l)
            proy = r2(sum(v2[k]) * (1.10 if ("proyeccion_sobre_lo_aprobado" in s and l == "PRY-310") else 0.98))
            if l == "Nómina":
                proy = r2(sum(v2[k]))
            filas.append([a, l, proy, version])
            if version == "1":
                esperado.append(("budget_version_mismatch", f"version:presupuesto-{ANIO}/30-proyecciones/proyeccion-{area.lower().replace('í', 'i').replace('ó', 'o')}-{fecha}.csv:{a}:{l}"))
            if "proyeccion_sobre_lo_aprobado" in s and l == "PRY-310":
                esperado.append(("forecast_over_approved", f"proy:{a}:{l}"))
        if fecha == "2026-07-15":
            esperado += [("forecast_stale", f"stale:{a}:{l}") for a, l, *_ in LINEAS if a == area]
        csv_(pr / "30-proyecciones" / f"proyeccion-{area.lower().replace('í', 'i').replace('ó', 'o')}-{fecha}.csv", filas)
    md(pr / "40-actas" / "acta-01-aprobacion.md", doc("# Acta 01 · Comité de presupuesto\n\nFecha: 2026-01-20\n\nSe aprueba el presupuesto 2026, versión 1.",
                                                     "# Ata 01 · Comitê de orçamento\n\nData: 2026-01-20\n\nAprovado o orçamento de 2026, versão 1."))
    md(pr / "40-actas" / "acta-05-traslado.md",
       doc(f"# Acta 05 · Comité de presupuesto\n\nFecha: 2026-06-28\n\nSe aprueba trasladar {T * 6:,.2f} de Comercial · Publicidad a Comercial · Eventos, de julio a diciembre.",
           f"# Ata 05 · Comitê de orçamento\n\nData: 2026-06-28\n\nAprovado o remanejamento de {_cifra(T * 6)} de Comercial · Publicidade para Comercial · Eventos, de julho a dezembro."))
    md(pr / "40-actas" / "acta-06-comite.md",
       doc("# Acta 06 · Comité de presupuesto\n\nFecha: 2026-09-10\n\nCompromiso: Administración revisa el contrato de vigilancia antes del próximo comité.",
           "# Ata 06 · Comitê de orçamento\n\nData: 2026-09-10\n\nCompromisso: a Administração revisa o contrato de vigilância antes do próximo comitê."))
    extraccion["presupuesto"]["minutes"] = [
        {"type": "aprobacion", "version": 1, "date": "2026-01-20", "source": f"presupuesto-{ANIO}/40-actas/acta-01-aprobacion.md"},
        {"type": "traslado", "date": "2026-06-28", "source": f"presupuesto-{ANIO}/40-actas/acta-05-traslado.md",
         "movements": [{"from": {"area": "Comercial", "line": "Publicidad"}, "to": {"area": "Comercial", "line": "Eventos"}, "amount": r2(T * 6)}]},
    ]
    extraccion["presupuesto"]["committee_commitments"] = [{"what": "Revisar el contrato de vigilancia", "owner": "Administración", "status": "abierto",
                                                          "evidence": None, "source": f"presupuesto-{ANIO}/40-actas/acta-06-comite.md"}]
    declaran = ["Administración"] if ("area_declara_dentro" in s or not e["siembra"]) else []
    for area in declaran:
        md(pr / "30-proyecciones" / f"correo-{area.lower().replace('ó', 'o')}.md",
           doc(f"De: {area}\nFecha: 2026-10-01\n\nEl área de {area} va dentro del presupuesto.",
               f"De: {tr(area)}\nData: 2026-10-01\n\nA área de {tr(area)} está dentro do orçamento."))
        extraccion["presupuesto"]["area_statements"].append({"area": area, "says": "dentro", "source": f"presupuesto-{ANIO}/30-proyecciones/correo-{area.lower().replace('ó', 'o')}.md", "date": "2026-10-01"})
    if "area_declara_dentro" in s:
        esperado.append(("declared_vs_evidence", "declara:Administración"))

    # La ficha del proyecto de la familia PMO que ejecuta la línea PRY-310.
    apr = r2(sum(v2[("Tecnología", "PRY-310")]) * (0.9 if "proyecto_distinto" in s else 1))
    ficha_pry = {"identity": {"code": {"value": "PRY-310", "source": "PRY-310/00-gobierno/acta.md", "state": "found"}},
                 "money": {"approved": {"value": apr, "source": "PRY-310/00-gobierno/acta.md", "state": "found"}}}
    (sesion / "estado-pmo" / "records").mkdir(parents=True, exist_ok=True)
    (sesion / "estado-pmo" / "records" / "PRY-310.json").write_text(json.dumps(ficha_pry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if "proyecto_distinto" in s:
        esperado.append(("project_budget_mismatch", "pry:PRY-310"))

    cfg_tesoreria, siembra_t = tesoreria(e, docs, esperado)
    entidad = {"id": e["id"], "name": e["nombre"], "country": pais, "currency": e["moneda"], "approver": "Sofía León"}
    rutas = {"documents": f"finanzas/{ent_dir}", "state": f"estado-finanzas/{ent_dir}"}
    config = {
        "clara": {"entity": entidad, "paths": rutas, "period": PERIODO,
                  "accounts": {"sales": ["4135"], "purchases": ["1435", "5135", "5145", "5195"], "vat_generated": ["2408"], "vat_deductible": ["2408"], "reconcile": ["1305", "2205"]},
                  "bank_accounts": sorted(subcarpetas.values()), "checklist": {"source": "organizacion", "approved": True}, "holidays": []},
        "tomas": {"entity": entidad, "paths": rutas, "budget": {"year": ANIO, "cut": PERIODO, "pmo_records": "estado-pmo/records", "expense_prefixes": ["51", "52"]}},
        "aurea": {"entity": entidad, "paths": rutas, "period": PERIODO, **cfg_tesoreria},
    }
    clave = {"entidad": e["nombre"], "industria": e["industria"], "pais": pais, "hoy": HOY, "siembra": e["siembra"] + siembra_t,
             "config": config, "extraccion": extraccion,
             "esperado": sorted(({"signal": a, "key": b} for a, b in set(esperado)), key=lambda x: (x["signal"], x["key"]))}
    texto = json.dumps(clave, ensure_ascii=False, indent=2)
    for viejo, nuevo in sorted(formatos_reales(docs, e["carpeta"]).items(), key=lambda x: -len(x[0])):
        texto = texto.replace(viejo, nuevo)
    if LANG[0] == "pt":
        # La clave dice lo que dicen los documentos: los archivos con su nombre en portugués, y las
        # áreas, las líneas, las personas y los conceptos como los escriben ellos, también en las
        # claves de las señales, que llevan algunos nombres normalizados.
        for viejo, nuevo in sorted(renombrar_pt(docs).items(), key=lambda x: -len(x[0])):
            texto = texto.replace(viejo, nuevo)
        for a, b in FRASES_PT:
            if len(a) > 4 and a not in VALORES_DE_FICHA:
                texto = texto.replace(f'"{a}"', f'"{b}"').replace(f":{a}:", f":{b}:").replace(f":{a}\"", f":{b}\"")
                texto = texto.replace(f":{F.norm(a)}:", f":{F.norm(b)}:").replace(f":{F.norm(a)}\"", f":{F.norm(b)}\"")
        LANG[0] = "es"
    (sesion / "clave.json").write_text(texto + "\n", encoding="utf-8")
    return json.loads(texto)


def main() -> int:
    if SALIDA.exists():
        shutil.rmtree(SALIDA)
    total = 0
    for e in ENTIDADES:
        c = generar(e)
        total += len(c["esperado"])
        print(f"  {e['carpeta']:13} {e['pais']}  {len(e['siembra']):2} defectos sembrados · {len(c['esperado']):2} señales esperadas")
    print(f"\n  {len(ENTIDADES)} entidades, {total} señales en la clave, en {SALIDA.relative_to(RAIZ)}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
