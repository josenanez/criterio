# -*- coding: utf-8 -*-
"""Genera el material sintético de prueba de criterio-pmo.

Nada aquí es real. Ningún documento de cliente, de empleador ni dato personal.
Todo se construyó desde cero, como exige CONTRIBUTING.md.

    python3 tests/criterio-pmo/generar.py

Produce dos árboles:

    input/              la carpeta de documentación a la que se apunta un comando
    expected/fichas/    la extracción de referencia: lo que una lectura correcta
                        de input/ debería producir
    expected/hallazgos.json   las respuestas conocidas, escritas a mano

La fecha de referencia de todas las corridas es 2026-09-30. Es fija a propósito:
una prueba que use la fecha de hoy cambia de respuesta cada semana.

Los hallazgos esperados NO se calculan aquí. Se escriben a mano a partir de los
documentos, y el trabajo de compute es derivarlos de la ficha. Si se derivaran
con las mismas fórmulas, la prueba no probaría nada.
"""
import json
import os
import shutil
from pathlib import Path

RAIZ = Path(__file__).parent
INPUT = RAIZ / "input"
EXPECTED = RAIZ / "expected"
HOY = "2026-09-30"


def escribir(ruta: Path, texto: str):
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(texto.strip() + "\n", encoding="utf-8")


def campo(valor, fuente, fecha, estado="found", conflicto=None):
    d = {"value": valor, "source": fuente, "source_date": fecha, "state": estado}
    if conflicto:
        d["conflict"] = conflicto
    return d


# ══════════════════════════════════════════════════════════════════════════
# PRY-001 · Originación digital
# El proyecto desordenado. Declara verde y la evidencia no lo sostiene.
# Planta: hito vencido sin evidencia · verde contradicho · declaración vieja
#         presupuesto comprometido al 95% · replanificación sin autorizar
#         compromiso reprogramado tres veces · patrocinador contradicho
#         dependencia declarada y no confirmada de PRY-002
# ══════════════════════════════════════════════════════════════════════════

escribir(INPUT / "PRY-001-originacion-digital/00-gobierno/2026-01-12-acta-constitucion.md", """
# Acta de constitución · Originación digital de crédito de consumo

**Código:** PRY-001
**Área dueña:** Banca de Personas
**Patrocinador:** María Restrepo, VP de Operaciones
**Gerente de proyecto:** Andrés Lozano
**Comité:** Comité de Transformación Digital
**Fecha de aprobación:** 12 de enero de 2026

## Objetivo del negocio

Reducir el tiempo de originación de crédito de consumo de cinco días hábiles a uno,
para solicitudes de hasta 30 millones de pesos.

## Alcance

Captura digital de la solicitud, motor de decisión, desembolso automático a cuenta
propia, y notificación al cliente.

## Exclusiones explícitas

No incluye crédito hipotecario, no incluye clientes nuevos sin producto previo, y
no incluye el canal de oficina física.

## Criterio de éxito

Tiempo mediano de originación menor o igual a un día hábil, medido sobre las
solicitudes aprobadas del primer trimestre posterior a la salida a producción.

## Plan aprobado

Inicio 15 de enero de 2026. Cierre 30 de septiembre de 2026.

## Supuestos

El ambiente de pruebas integrado estará disponible en marzo. El proveedor del
motor de decisión entrega la versión certificada en abril.
""")

escribir(INPUT / "PRY-001-originacion-digital/10-plan/2026-01-15-cronograma-v1.csv", """
hito,fecha_linea_base,responsable
Diseño funcional aprobado,2026-03-02,Andrés Lozano
Ambiente integrado disponible,2026-03-31,Infraestructura
Motor de decisión certificado,2026-05-29,Proveedor
Pruebas de aceptación cerradas,2026-08-14,Calidad
Salida a producción,2026-09-30,Andrés Lozano
""")

escribir(INPUT / "PRY-001-originacion-digital/10-plan/2026-06-20-cronograma-v2.csv", """
hito,fecha_linea_base,fecha_vigente,estado,evidencia
Diseño funcional aprobado,2026-03-02,2026-03-06,cumplido,20-seguimiento/2026-03-06-acta-aprobacion-diseno.md
Ambiente integrado disponible,2026-03-31,2026-05-18,cumplido,20-seguimiento/2026-05-18-correo-ambiente.md
Motor de decisión certificado,2026-05-29,2026-07-31,pendiente,
Pruebas de aceptación cerradas,2026-08-14,2026-10-16,pendiente,
Salida a producción,2026-09-30,2026-11-30,pendiente,
""")

escribir(INPUT / "PRY-001-originacion-digital/20-seguimiento/2026-06-18-solicitud-cambio-cc-01.md", """
# Solicitud de cambio CC-01 · Originación digital

**Radicada:** 18 de junio de 2026
**Solicita:** Andrés Lozano, gerente de proyecto

## Qué se pide

Mover la fecha de cierre por el atraso en la certificación del motor de decisión.

## Impacto

- **Alcance:** sin cambio.
- **Tiempo:** 60 días.
- **Costo:** sin impacto. El proveedor absorbe el sobrecosto de la extensión de soporte.

## Decisión

**Aprobada** por el Comité de Transformación Digital el 20 de junio de 2026.
Se autoriza mover el cierre de septiembre 30 a noviembre 30 de 2026.
""")

escribir(INPUT / "PRY-001-originacion-digital/20-seguimiento/2026-08-22-informe-avance.md", """
# Informe de avance · Originación digital · agosto 2026

**Reporta:** Andrés Lozano
**Estado:** VERDE
**Avance:** 78%
**Corte:** 22 de agosto de 2026

El proyecto avanza conforme al plan replanificado. El motor de decisión está en
certificación y se espera cerrar en las próximas semanas. El equipo se mantiene
completo y no hay riesgos que requieran decisión del comité.

## Presupuesto

Aprobado 1.850.000.000. Comprometido 1.762.000.000. Ejecutado 790.000.000.
Proyección al cierre 1.910.000.000.
""")

escribir(INPUT / "PRY-001-originacion-digital/30-reuniones/2026-07-24-comite-tecnico.md", """
# Comité técnico · Originación digital · 24 de julio de 2026

**Asisten:** Andrés Lozano, Carlos Méndez (proveedor), Diana Pérez (Calidad),
Jorge Ruiz (Arquitectura)

## Temas

El motor de decisión no pasó el ciclo de certificación de julio. Carlos indica que
el hallazgo es de desempeño bajo carga y que el equipo del proveedor ya está
trabajando en él.

Carlos se compromete a enviar el informe de certificación corregido el 7 de agosto.

Jorge advierte que si el core de depósitos mueve su fecha otra vez, el desembolso
automático no tiene contra qué integrarse. Queda como riesgo.

Diana pregunta quién aprueba el cierre de pruebas dado que el acta no dice hasta
qué monto puede decidir el gerente. Nadie responde.
""")

escribir(INPUT / "PRY-001-originacion-digital/30-reuniones/2026-08-14-comite-tecnico.md", """
# Comité técnico · Originación digital · 14 de agosto de 2026

**Asisten:** Andrés Lozano, Carlos Méndez, Diana Pérez

El informe de certificación no llegó. Carlos se compromete a enviarlo el 28 de
agosto, esta vez con el resultado de las pruebas de carga incluido.

Se confirma que el proyecto depende de que el core de depósitos exponga el
servicio de abono en cuenta. Andrés indica que lo coordinará con ese proyecto.
""")

escribir(INPUT / "PRY-001-originacion-digital/30-reuniones/2026-09-11-comite-tecnico.md", """
# Comité técnico · Originación digital · 11 de septiembre de 2026

**Asisten:** Andrés Lozano, Carlos Méndez, Diana Pérez, Sandra Gil

Sandra se presenta como nueva patrocinadora del proyecto. Informa que asumió la
Vicepresidencia de Operaciones desde el 1 de septiembre.

El informe de certificación sigue pendiente. Carlos se compromete a enviarlo el 18
de septiembre.

Diana insiste en el tema de la autoridad de aprobación del cierre de pruebas. Queda
pendiente de definir.
""")

# ══════════════════════════════════════════════════════════════════════════
# PRY-002 · Core de depósitos
# El proyecto del que otro depende, y que movió su fecha.
# Planta: desviación en tiempo sobre el 10% · dependencia entrante no confirmada
# ══════════════════════════════════════════════════════════════════════════

escribir(INPUT / "PRY-002-core-depositos/00-gobierno/2026-02-02-acta-constitucion.md", """
# Acta de constitución · Modernización del core de depósitos

**Código:** PRY-002
**Área dueña:** Tecnología
**Patrocinador:** Ricardo Salazar, CIO
**Gerente de proyecto:** Luisa Cárdenas
**Comité:** Comité de Tecnología
**Autoridad del gerente:** hasta 50.000.000 y sin cambios de alcance.

## Objetivo del negocio

Reemplazar el core de depósitos por una plataforma que permita exponer servicios
de abono y consulta de saldo en tiempo real a los canales digitales.

## Plan aprobado

Inicio 1 de marzo de 2026. Cierre 31 de octubre de 2026.

## Criterio de éxito

Servicios de abono y consulta expuestos con disponibilidad mensual del 99,8% durante
dos meses consecutivos.
""")

escribir(INPUT / "PRY-002-core-depositos/10-plan/2026-08-28-cronograma-v2.csv", """
hito,fecha_linea_base,fecha_vigente,estado,evidencia
Modelo de datos migrado,2026-05-29,2026-06-12,cumplido,20-seguimiento/2026-06-12-acta-migracion.md
Servicio de consulta expuesto,2026-07-31,2026-08-28,cumplido,20-seguimiento/2026-08-28-acta-servicio.md
Servicio de abono expuesto,2026-09-30,2026-12-18,pendiente,
Cierre,2026-10-31,2027-01-30,pendiente,
""")

escribir(INPUT / "PRY-002-core-depositos/20-seguimiento/2026-09-25-informe-avance.md", """
# Informe de avance · Core de depósitos · septiembre 2026

**Reporta:** Luisa Cárdenas
**Estado:** AMARILLO
**Avance:** 61%
**Corte:** 25 de septiembre de 2026

El servicio de abono se mueve a diciembre por la complejidad de la conciliación con
el mayor contable. La fecha de cierre pasa a enero de 2027. Está en trámite la
solicitud de cambio.

Advertencia a la PMO: hay al menos un proyecto que declaró dependencia del servicio
de abono y no ha coordinado con nosotros.

## Presupuesto

Aprobado 4.200.000.000. Comprometido 2.980.000.000. Ejecutado 2.410.000.000.
Proyección al cierre 4.350.000.000.
""")

escribir(INPUT / "PRY-002-core-depositos/30-reuniones/2026-09-18-comite-tecnico.md", """
# Comité técnico · Core de depósitos · 18 de septiembre de 2026

**Asisten:** Luisa Cárdenas, Ricardo Salazar, Jorge Ruiz

Se revisa el impacto de mover el servicio de abono a diciembre. Ricardo pide que se
coordine con los proyectos que dependen de ese servicio.

Luisa queda encargada de coordinar con el proyecto de originación digital. No se
define fecha para esa coordinación.
""")

# ══════════════════════════════════════════════════════════════════════════
# PRY-003 · Migración a nube
# El proyecto de proveedores.
# Planta: entregable vencido sin evidencia · aceptado sin evidencia
#         factura declarada sin entregable aceptado
# ══════════════════════════════════════════════════════════════════════════

escribir(INPUT / "PRY-003-migracion-nube/00-gobierno/2026-03-09-acta-constitucion.md", """
# Acta de constitución · Migración de cargas a nube

**Código:** PRY-003
**Área dueña:** Tecnología
**Patrocinador:** Ricardo Salazar, CIO
**Gerente de proyecto:** Felipe Naranjo
**Comité:** Comité de Tecnología
**Autoridad del gerente:** hasta 80.000.000, sin cambios de alcance.

## Plan aprobado

Inicio 16 de marzo de 2026. Cierre 18 de diciembre de 2026.

## Criterio de éxito

Cuarenta cargas migradas con ventana de indisponibilidad menor a cuatro horas cada
una, y costo de infraestructura mensual no superior al actual más 15%.
""")

escribir(INPUT / "PRY-003-migracion-nube/00-gobierno/2026-04-06-contrato-oc-2214.md", """
# Orden de compra OC-2214 · Nubetec S.A.S.

**Proveedor:** Nubetec S.A.S.
**Fecha:** 6 de abril de 2026
**Valor:** 980.000.000

## Entregables contractuales

| Entregable | Fecha comprometida | Valor |
|---|---|---|
| Landing zone certificada | 2026-05-29 | 200.000.000 |
| Migración de las primeras diez cargas | 2026-07-31 | 300.000.000 |
| Migración de las veinte cargas siguientes | 2026-09-15 | 400.000.000 |
| Tablero de costos por carga | 2026-08-29 | 80.000.000 |

## Facturación

Contra entregable aceptado por el gerente de proyecto, con acta de recibo.
""")

escribir(INPUT / "PRY-003-migracion-nube/20-seguimiento/2026-06-05-acta-recibo-landing-zone.md", """
# Acta de recibo · Landing zone certificada

**Fecha:** 5 de junio de 2026
**Entregable:** Landing zone certificada, OC-2214
**Recibe:** Felipe Naranjo, gerente de proyecto
**Entrega:** Nubetec S.A.S.

Se recibe a satisfacción. La certificación de la landing zone se valida contra el
listado de controles acordado. Se acepta el entregable.
""")

escribir(INPUT / "PRY-003-migracion-nube/20-seguimiento/2026-09-20-informe-avance.md", """
# Informe de avance · Migración a nube · septiembre 2026

**Reporta:** Felipe Naranjo
**Estado:** AMARILLO
**Avance:** 44%
**Corte:** 20 de septiembre de 2026

Las primeras diez cargas quedaron migradas en agosto. El tablero de costos por carga
se dio por entregado en la reunión del 3 de septiembre, aunque no se levantó acta de
recibo.

La migración de las veinte cargas siguientes no arrancó: la fecha del 15 de
septiembre pasó sin avance.

## Facturación

Nubetec ha facturado 620.000.000 de la orden de compra.

## Presupuesto

Aprobado 1.400.000.000. Comprometido 980.000.000. Ejecutado 640.000.000.
Proyección al cierre 1.420.000.000.
""")

escribir(INPUT / "PRY-003-migracion-nube/30-reuniones/2026-09-03-seguimiento-proveedor.md", """
# Seguimiento a proveedor · Nubetec · 3 de septiembre de 2026

**Asisten:** Felipe Naranjo, Paola Arias (Nubetec), Tomás Vélez (Finanzas)

Paola presenta el tablero de costos por carga y lo da por entregado. Felipe pide
ajustes de presentación y queda pendiente el acta de recibo.

Tomás pregunta por qué hay facturación de las veinte cargas siguientes si esa
migración no ha empezado. Paola ofrece revisarlo con su área de facturación.

Paola se compromete a entregar el cronograma de las veinte cargas el 12 de
septiembre.
""")

# ══════════════════════════════════════════════════════════════════════════
# PRY-004 · Open Banking
# El proyecto sin plan aprobado.
# Planta: sin línea base · campos ausentes · dato rancio · silencio
# ══════════════════════════════════════════════════════════════════════════

escribir(INPUT / "PRY-004-open-banking/00-gobierno/2025-02-14-memorando-inicio.md", """
# Memorando · Iniciativa de Open Banking

**Fecha:** 14 de febrero de 2025

Se instruye a la Dirección de Arquitectura iniciar el levantamiento de la
iniciativa de Open Banking, en respuesta al marco regulatorio en construcción.

**Responsable designado:** Jorge Ruiz, Director de Arquitectura
**Patrocinador:** Ricardo Salazar, CIO

No se define presupuesto ni cronograma en este memorando. El plan se presentará
al Comité de Tecnología una vez se conozca el alcance regulatorio definitivo.
""")

escribir(INPUT / "PRY-004-open-banking/20-seguimiento/2026-04-30-nota-avance.md", """
# Nota de avance · Open Banking · abril 2026

**Reporta:** Jorge Ruiz

Se completó el inventario de APIs candidatas: 34 servicios, de los cuales 12 ya
existen con alguna forma de exposición interna.

Sigue sin plan aprobado ni presupuesto asignado. No hay cronograma, y por lo tanto
no hay fecha comprometida de cierre.

Estado reportado: VERDE, en el sentido de que no hay nada atrasado porque no hay
nada comprometido.
""")

# ══════════════════════════════════════════════════════════════════════════
# PRY-005 · Débito contactless
# CONTROL NEGATIVO. Todo en orden. No debe disparar ninguna alerta.
# Si este proyecto alerta, el agente es un generador de ruido.
# ══════════════════════════════════════════════════════════════════════════

escribir(INPUT / "PRY-005-debito-contactless/00-gobierno/2026-05-04-acta-constitucion.md", """
# Acta de constitución · Débito contactless

**Código:** PRY-005
**Área dueña:** Medios de Pago
**Patrocinador:** Sandra Gil, VP de Operaciones
**Gerente de proyecto:** Paula Betancur
**Comité:** Comité de Medios de Pago
**Autoridad del gerente:** hasta 40.000.000 y ajustes de cronograma menores a 15 días.

## Objetivo del negocio

Habilitar pago sin contacto en la tarjeta débito, para reducir el tiempo de
transacción en comercio presente y alinearse con el mandato del esquema.

## Exclusiones explícitas

No incluye tarjeta crédito, ni pago con billetera en el teléfono.

## Criterio de éxito

30% de las transacciones de débito en comercio presente hechas sin contacto, seis
meses después de la habilitación.

## Plan aprobado

Inicio 11 de mayo de 2026. Cierre 30 de noviembre de 2026.
""")

escribir(INPUT / "PRY-005-debito-contactless/10-plan/2026-05-11-cronograma-v1.csv", """
hito,fecha_linea_base,fecha_vigente,estado,evidencia
Certificación con el esquema,2026-07-31,2026-07-24,cumplido,20-seguimiento/2026-07-24-certificado-esquema.md
Piloto en 50 comercios,2026-09-11,2026-09-11,cumplido,20-seguimiento/2026-09-11-acta-cierre-piloto.md
Despliegue masivo,2026-11-13,2026-11-13,pendiente,
Cierre,2026-11-30,2026-11-30,pendiente,
""")

escribir(INPUT / "PRY-005-debito-contactless/20-seguimiento/2026-09-11-acta-cierre-piloto.md", """
# Acta de cierre del piloto · Débito contactless

**Fecha:** 11 de septiembre de 2026

El piloto en 50 comercios cierra en la fecha comprometida. 18.400 transacciones sin
contacto procesadas, sin incidentes de disponibilidad.

Se autoriza continuar al despliegue masivo según el plan.
""")

escribir(INPUT / "PRY-005-debito-contactless/20-seguimiento/2026-09-26-informe-avance.md", """
# Informe de avance · Débito contactless · septiembre 2026

**Reporta:** Paula Betancur
**Estado:** VERDE
**Avance:** 72%
**Corte:** 26 de septiembre de 2026

El piloto cerró en fecha. El despliegue masivo arranca según plan el 13 de
noviembre. No hay desviación en tiempo ni en costo, y no hay riesgos abiertos que
excedan la autoridad del gerente.

## Presupuesto

Aprobado 900.000.000. Comprometido 540.000.000. Ejecutado 498.000.000.
Proyección al cierre 880.000.000.
""")

escribir(INPUT / "PRY-005-debito-contactless/30-reuniones/2026-09-24-seguimiento-semanal.md", """
# Seguimiento semanal · Débito contactless · 24 de septiembre de 2026

**Asisten:** Paula Betancur, Mónica Salas (Riesgo), Iván Duarte (Operaciones)

Piloto cerrado y documentado. Mónica confirma que el análisis de riesgo operativo
quedó firmado el 19 de septiembre.

Iván se compromete a entregar el plan de capacitación de la red de oficinas el 15 de
octubre.

No hay decisiones pendientes para el comité.
""")

# ══════════════════════════════════════════════════════════════════════════
# PRY-006 · SARLAFT
# Planta: cambio aprobado con impacto en meses (ilegible) ·
#         cambio aprobado sin línea base nueva · declaración vieja · silencio
# ══════════════════════════════════════════════════════════════════════════

escribir(INPUT / "PRY-006-sarlaft/00-gobierno/2026-01-26-acta-constitucion.md", """
# Acta de constitución · Renovación del monitoreo SARLAFT

**Código:** PRY-006
**Área dueña:** Cumplimiento
**Patrocinador:** Beatriz Ocampo, Oficial de Cumplimiento
**Gerente de proyecto:** Nicolás Ortega
**Comité:** Comité de Riesgos
**Autoridad del gerente:** hasta 25.000.000.

## Plan aprobado

Inicio 2 de febrero de 2026. Cierre 30 de octubre de 2026.

## Criterio de éxito

Reducción del 40% en alertas falsas positivas, manteniendo la cobertura de
tipologías exigida por el supervisor.
""")

escribir(INPUT / "PRY-006-sarlaft/20-seguimiento/2026-07-08-solicitud-cambio-cc-07.md", """
# Solicitud de cambio CC-07 · SARLAFT

**Radicada:** 8 de julio de 2026
**Solicita:** Nicolás Ortega

## Qué se pide

Ampliar el alcance para incluir el monitoreo de operaciones en moneda extranjera,
por requerimiento del supervisor.

## Impacto

- **Alcance:** se suman las tipologías de moneda extranjera.
- **Tiempo:** tres meses.
- **Costo:** 180.000.000 adicionales.

## Decisión

**Aprobada** por el Comité de Riesgos el 15 de julio de 2026.
""")

escribir(INPUT / "PRY-006-sarlaft/20-seguimiento/2026-08-12-informe-avance.md", """
# Informe de avance · SARLAFT · agosto 2026

**Reporta:** Nicolás Ortega
**Estado:** VERDE
**Avance:** 55%
**Corte:** 12 de agosto de 2026

El cambio aprobado en julio se está incorporando. El cronograma se actualizará una
vez el proveedor confirme las fechas de las nuevas tipologías.

## Presupuesto

Aprobado 1.100.000.000. Comprometido 700.000.000. Ejecutado 430.000.000.
Proyección al cierre 1.290.000.000.

El presupuesto aprobado no se ha actualizado con los 180.000.000 que autorizó el
comité en julio. Se solicitará la modificación.
""")

# ══════════════════════════════════════════════════════════════════════════
# La extracción de referencia: lo que una lectura correcta produce
# ══════════════════════════════════════════════════════════════════════════

FICHAS = {}

FICHAS["PRY-001"] = {
    "schema_version": "0.1",
    "identity": {
        "code": campo("PRY-001", "00-gobierno/2026-01-12-acta-constitucion.md", "2026-01-12"),
        "name": campo("Originación digital de crédito de consumo",
                      "00-gobierno/2026-01-12-acta-constitucion.md", "2026-01-12"),
        "business_area": campo("Banca de Personas", "00-gobierno/2026-01-12-acta-constitucion.md", "2026-01-12"),
        "product": campo("Crédito de consumo", "00-gobierno/2026-01-12-acta-constitucion.md", "2026-01-12"),
        # el acta dice María Restrepo; la minuta de septiembre dice Sandra Gil
        "sponsor": campo("Sandra Gil, VP de Operaciones",
                         "30-reuniones/2026-09-11-comite-tecnico.md", "2026-09-11", "ambiguous",
                         {"value": "María Restrepo, VP de Operaciones",
                          "source": "00-gobierno/2026-01-12-acta-constitucion.md",
                          "source_date": "2026-01-12"}),
        "manager": campo("Andrés Lozano", "00-gobierno/2026-01-12-acta-constitucion.md", "2026-01-12"),
        "committee": campo("Comité de Transformación Digital",
                           "00-gobierno/2026-01-12-acta-constitucion.md", "2026-01-12"),
        "authority": {"value": None, "source": None, "source_date": None, "state": "not_found"},
    },
    "declared": {
        "status": campo("verde", "20-seguimiento/2026-08-22-informe-avance.md", "2026-08-22"),
        "progress_pct": campo(78, "20-seguimiento/2026-08-22-informe-avance.md", "2026-08-22"),
        "as_of": campo("2026-08-22", "20-seguimiento/2026-08-22-informe-avance.md", "2026-08-22"),
    },
    "plan": {
        "start_date": campo("2026-01-15", "00-gobierno/2026-01-12-acta-constitucion.md", "2026-01-12"),
        "end_date": campo("2026-11-30", "10-plan/2026-06-20-cronograma-v2.csv", "2026-06-20"),
        "baseline": [
            {"version": 1, "approved_on": "2026-01-12", "start_date": "2026-01-15",
             "end_date": "2026-09-30", "reason": "inicial",
             "source": "00-gobierno/2026-01-12-acta-constitucion.md"},
            {"version": 2, "approved_on": "2026-06-20", "start_date": "2026-01-15",
             "end_date": "2026-11-30", "reason": "atraso en certificación del motor",
             "source": "20-seguimiento/2026-06-18-solicitud-cambio-cc-01.md"},
        ],
        "milestones": [
            {"name": campo("Diseño funcional aprobado", "10-plan/2026-06-20-cronograma-v2.csv", "2026-06-20"),
             "baseline_date": campo("2026-03-02", "10-plan/2026-01-15-cronograma-v1.csv", "2026-01-15"),
             "current_date": campo("2026-03-06", "10-plan/2026-06-20-cronograma-v2.csv", "2026-06-20"),
             "state": campo("met", "10-plan/2026-06-20-cronograma-v2.csv", "2026-06-20"),
             "evidence": campo("20-seguimiento/2026-03-06-acta-aprobacion-diseno.md",
                               "10-plan/2026-06-20-cronograma-v2.csv", "2026-06-20")},
            {"name": campo("Motor de decisión certificado", "10-plan/2026-06-20-cronograma-v2.csv", "2026-06-20"),
             "baseline_date": campo("2026-05-29", "10-plan/2026-01-15-cronograma-v1.csv", "2026-01-15"),
             "current_date": campo("2026-07-31", "10-plan/2026-06-20-cronograma-v2.csv", "2026-06-20"),
             "state": campo("pending", "10-plan/2026-06-20-cronograma-v2.csv", "2026-06-20"),
             "evidence": {"value": None, "source": None, "source_date": None, "state": "not_found"}},
            {"name": campo("Salida a producción", "10-plan/2026-06-20-cronograma-v2.csv", "2026-06-20"),
             "baseline_date": campo("2026-09-30", "10-plan/2026-01-15-cronograma-v1.csv", "2026-01-15"),
             "current_date": campo("2026-11-30", "10-plan/2026-06-20-cronograma-v2.csv", "2026-06-20"),
             "state": campo("pending", "10-plan/2026-06-20-cronograma-v2.csv", "2026-06-20"),
             "evidence": {"value": None, "source": None, "source_date": None, "state": "not_found"}},
        ],
    },
    "money": {
        "currency": campo("COP", "20-seguimiento/2026-08-22-informe-avance.md", "2026-08-22"),
        "approved": campo(1850000000, "20-seguimiento/2026-08-22-informe-avance.md", "2026-08-22"),
        "committed": campo(1762000000, "20-seguimiento/2026-08-22-informe-avance.md", "2026-08-22"),
        "executed": campo(790000000, "20-seguimiento/2026-08-22-informe-avance.md", "2026-08-22"),
        "projection": campo(1910000000, "20-seguimiento/2026-08-22-informe-avance.md", "2026-08-22"),
    },
    "changes": [
        {"ref": campo("CC-01", "20-seguimiento/2026-06-18-solicitud-cambio-cc-01.md", "2026-06-18"),
         "requested_on": campo("2026-06-18", "20-seguimiento/2026-06-18-solicitud-cambio-cc-01.md", "2026-06-18"),
         "scope_impact": campo("sin cambio", "20-seguimiento/2026-06-18-solicitud-cambio-cc-01.md", "2026-06-18"),
         "time_impact": campo("60 días", "20-seguimiento/2026-06-18-solicitud-cambio-cc-01.md", "2026-06-18"),
         "cost_impact": campo("sin impacto", "20-seguimiento/2026-06-18-solicitud-cambio-cc-01.md", "2026-06-18"),
         "decision": campo("approved", "20-seguimiento/2026-06-18-solicitud-cambio-cc-01.md", "2026-06-18"),
         "decided_by": campo("Comité de Transformación Digital",
                             "20-seguimiento/2026-06-18-solicitud-cambio-cc-01.md", "2026-06-18")},
    ],
    "raid": {
        "risks": [
            {"what": campo("Si el core de depósitos mueve su fecha otra vez, el desembolso automático no tiene contra qué integrarse",
                           "30-reuniones/2026-07-24-comite-tecnico.md", "2026-07-24"),
             "owner": {"value": None, "source": None, "source_date": None, "state": "not_found"},
             "formally_registered": campo(False, "30-reuniones/2026-07-24-comite-tecnico.md", "2026-07-24")},
        ],
        "issues": [
            {"what": campo("El acta no declara la autoridad de aprobación del cierre de pruebas",
                           "30-reuniones/2026-09-11-comite-tecnico.md", "2026-09-11"),
             "since": campo("2026-07-24", "30-reuniones/2026-07-24-comite-tecnico.md", "2026-07-24")},
        ],
        "dependencies": [
            {"on_project": campo("PRY-002", "30-reuniones/2026-08-14-comite-tecnico.md", "2026-08-14"),
             "what": campo("Servicio de abono en cuenta expuesto por el core de depósitos",
                           "30-reuniones/2026-08-14-comite-tecnico.md", "2026-08-14"),
             "confirmed": campo(False, "30-reuniones/2026-08-14-comite-tecnico.md", "2026-08-14")},
        ],
    },
    "commitments": [
        {"who": campo("Carlos Méndez", "30-reuniones/2026-09-11-comite-tecnico.md", "2026-09-11"),
         "what": campo("Enviar el informe de certificación del motor de decisión",
                       "30-reuniones/2026-09-11-comite-tecnico.md", "2026-09-11"),
         "due_date": campo("2026-09-18", "30-reuniones/2026-09-11-comite-tecnico.md", "2026-09-11"),
         "stated_on": campo("2026-09-11", "30-reuniones/2026-09-11-comite-tecnico.md", "2026-09-11"),
         "state": campo("open", "30-reuniones/2026-09-11-comite-tecnico.md", "2026-09-11"),
         "reschedules": [
             {"due_date": "2026-08-07", "stated_on": "2026-07-24",
              "source": "30-reuniones/2026-07-24-comite-tecnico.md"},
             {"due_date": "2026-08-28", "stated_on": "2026-08-14",
              "source": "30-reuniones/2026-08-14-comite-tecnico.md"},
             {"due_date": "2026-09-18", "stated_on": "2026-09-11",
              "source": "30-reuniones/2026-09-11-comite-tecnico.md"},
         ]},
    ],
    "activity": {
        "last_document_date": campo("2026-09-11", "30-reuniones/2026-09-11-comite-tecnico.md", "2026-09-11"),
        "last_meeting_date": campo("2026-09-11", "30-reuniones/2026-09-11-comite-tecnico.md", "2026-09-11"),
    },
}

FICHAS["PRY-002"] = {
    "schema_version": "0.1",
    "identity": {
        "code": campo("PRY-002", "00-gobierno/2026-02-02-acta-constitucion.md", "2026-02-02"),
        "name": campo("Modernización del core de depósitos",
                      "00-gobierno/2026-02-02-acta-constitucion.md", "2026-02-02"),
        "business_area": campo("Tecnología", "00-gobierno/2026-02-02-acta-constitucion.md", "2026-02-02"),
        "sponsor": campo("Ricardo Salazar, CIO", "00-gobierno/2026-02-02-acta-constitucion.md", "2026-02-02"),
        "manager": campo("Luisa Cárdenas", "00-gobierno/2026-02-02-acta-constitucion.md", "2026-02-02"),
        "committee": campo("Comité de Tecnología", "00-gobierno/2026-02-02-acta-constitucion.md", "2026-02-02"),
        "authority": campo("hasta 50.000.000 y sin cambios de alcance",
                           "00-gobierno/2026-02-02-acta-constitucion.md", "2026-02-02"),
    },
    "declared": {
        "status": campo("amarillo", "20-seguimiento/2026-09-25-informe-avance.md", "2026-09-25"),
        "progress_pct": campo(61, "20-seguimiento/2026-09-25-informe-avance.md", "2026-09-25"),
        "as_of": campo("2026-09-25", "20-seguimiento/2026-09-25-informe-avance.md", "2026-09-25"),
    },
    "plan": {
        "start_date": campo("2026-03-01", "00-gobierno/2026-02-02-acta-constitucion.md", "2026-02-02"),
        "end_date": campo("2027-01-30", "10-plan/2026-08-28-cronograma-v2.csv", "2026-08-28"),
        "baseline": [
            {"version": 1, "approved_on": "2026-02-02", "start_date": "2026-03-01",
             "end_date": "2026-10-31", "reason": "inicial",
             "source": "00-gobierno/2026-02-02-acta-constitucion.md"},
        ],
        "milestones": [
            {"name": campo("Servicio de abono expuesto", "10-plan/2026-08-28-cronograma-v2.csv", "2026-08-28"),
             "baseline_date": campo("2026-09-30", "10-plan/2026-08-28-cronograma-v2.csv", "2026-08-28"),
             "current_date": campo("2026-12-18", "10-plan/2026-08-28-cronograma-v2.csv", "2026-08-28"),
             "state": campo("pending", "10-plan/2026-08-28-cronograma-v2.csv", "2026-08-28"),
             "evidence": {"value": None, "source": None, "source_date": None, "state": "not_found"}},
        ],
    },
    "money": {
        "currency": campo("COP", "20-seguimiento/2026-09-25-informe-avance.md", "2026-09-25"),
        "approved": campo(4200000000, "20-seguimiento/2026-09-25-informe-avance.md", "2026-09-25"),
        "committed": campo(2980000000, "20-seguimiento/2026-09-25-informe-avance.md", "2026-09-25"),
        "executed": campo(2410000000, "20-seguimiento/2026-09-25-informe-avance.md", "2026-09-25"),
        "projection": campo(4350000000, "20-seguimiento/2026-09-25-informe-avance.md", "2026-09-25"),
    },
    "commitments": [
        # sin fecha: el skill lo registra como `no_declarada`. No puede estar vencido,
        # y hasta ahora tampoco se contaba.
        {"who": campo("Luisa Cárdenas", "30-reuniones/2026-09-18-comite-tecnico.md", "2026-09-18"),
         "what": campo("Coordinar con el proyecto de originación digital el cambio de fecha del abono",
                       "30-reuniones/2026-09-18-comite-tecnico.md", "2026-09-18"),
         "due_date": {"value": "no_declarada", "source": "30-reuniones/2026-09-18-comite-tecnico.md",
                      "source_date": "2026-09-18", "state": "found"},
         "stated_on": campo("2026-09-18", "30-reuniones/2026-09-18-comite-tecnico.md", "2026-09-18"),
         "state": campo("open", "30-reuniones/2026-09-18-comite-tecnico.md", "2026-09-18")},
    ],
    "activity": {
        "last_document_date": campo("2026-09-25", "20-seguimiento/2026-09-25-informe-avance.md", "2026-09-25"),
        "last_meeting_date": campo("2026-09-18", "30-reuniones/2026-09-18-comite-tecnico.md", "2026-09-18"),
    },
}

FICHAS["PRY-003"] = {
    "schema_version": "0.1",
    "identity": {
        "code": campo("PRY-003", "00-gobierno/2026-03-09-acta-constitucion.md", "2026-03-09"),
        "name": campo("Migración de cargas a nube", "00-gobierno/2026-03-09-acta-constitucion.md", "2026-03-09"),
        "business_area": campo("Tecnología", "00-gobierno/2026-03-09-acta-constitucion.md", "2026-03-09"),
        "sponsor": campo("Ricardo Salazar, CIO", "00-gobierno/2026-03-09-acta-constitucion.md", "2026-03-09"),
        "manager": campo("Felipe Naranjo", "00-gobierno/2026-03-09-acta-constitucion.md", "2026-03-09"),
        "committee": campo("Comité de Tecnología", "00-gobierno/2026-03-09-acta-constitucion.md", "2026-03-09"),
        "authority": campo("hasta 80.000.000, sin cambios de alcance",
                           "00-gobierno/2026-03-09-acta-constitucion.md", "2026-03-09"),
    },
    "declared": {
        "status": campo("amarillo", "20-seguimiento/2026-09-20-informe-avance.md", "2026-09-20"),
        "progress_pct": campo(44, "20-seguimiento/2026-09-20-informe-avance.md", "2026-09-20"),
        "as_of": campo("2026-09-20", "20-seguimiento/2026-09-20-informe-avance.md", "2026-09-20"),
    },
    "plan": {
        "start_date": campo("2026-03-16", "00-gobierno/2026-03-09-acta-constitucion.md", "2026-03-09"),
        "end_date": campo("2026-12-18", "00-gobierno/2026-03-09-acta-constitucion.md", "2026-03-09"),
        "baseline": [
            {"version": 1, "approved_on": "2026-03-09", "start_date": "2026-03-16",
             "end_date": "2026-12-18", "reason": "inicial",
             "source": "00-gobierno/2026-03-09-acta-constitucion.md"},
        ],
        "milestones": [],
    },
    "money": {
        "currency": campo("COP", "20-seguimiento/2026-09-20-informe-avance.md", "2026-09-20"),
        "approved": campo(1400000000, "20-seguimiento/2026-09-20-informe-avance.md", "2026-09-20"),
        "committed": campo(980000000, "20-seguimiento/2026-09-20-informe-avance.md", "2026-09-20"),
        "executed": campo(640000000, "20-seguimiento/2026-09-20-informe-avance.md", "2026-09-20"),
        "projection": campo(1420000000, "20-seguimiento/2026-09-20-informe-avance.md", "2026-09-20"),
    },
    "vendors": [
        {"name": campo("Nubetec S.A.S.", "00-gobierno/2026-04-06-contrato-oc-2214.md", "2026-04-06"),
         "contract_ref": campo("OC-2214", "00-gobierno/2026-04-06-contrato-oc-2214.md", "2026-04-06"),
         "invoiced": campo(620000000, "20-seguimiento/2026-09-20-informe-avance.md", "2026-09-20"),
         "deliverables": [
             {"name": campo("Landing zone certificada", "00-gobierno/2026-04-06-contrato-oc-2214.md", "2026-04-06"),
              "due_date": campo("2026-05-29", "00-gobierno/2026-04-06-contrato-oc-2214.md", "2026-04-06"),
              "amount": campo(200000000, "00-gobierno/2026-04-06-contrato-oc-2214.md", "2026-04-06"),
              "state": campo("accepted", "20-seguimiento/2026-06-05-acta-recibo-landing-zone.md", "2026-06-05"),
              "evidence": campo("20-seguimiento/2026-06-05-acta-recibo-landing-zone.md",
                                "20-seguimiento/2026-06-05-acta-recibo-landing-zone.md", "2026-06-05")},
             {"name": campo("Migración de las primeras diez cargas",
                            "00-gobierno/2026-04-06-contrato-oc-2214.md", "2026-04-06"),
              "due_date": campo("2026-07-31", "00-gobierno/2026-04-06-contrato-oc-2214.md", "2026-04-06"),
              "amount": campo(300000000, "00-gobierno/2026-04-06-contrato-oc-2214.md", "2026-04-06"),
              "state": campo("delivered", "20-seguimiento/2026-09-20-informe-avance.md", "2026-09-20"),
              "evidence": {"value": None, "source": None, "source_date": None, "state": "not_found"}},
             {"name": campo("Migración de las veinte cargas siguientes",
                            "00-gobierno/2026-04-06-contrato-oc-2214.md", "2026-04-06"),
              "due_date": campo("2026-09-15", "00-gobierno/2026-04-06-contrato-oc-2214.md", "2026-04-06"),
              "amount": campo(400000000, "00-gobierno/2026-04-06-contrato-oc-2214.md", "2026-04-06"),
              "state": campo("pending", "20-seguimiento/2026-09-20-informe-avance.md", "2026-09-20"),
              "evidence": {"value": None, "source": None, "source_date": None, "state": "not_found"}},
             {"name": campo("Tablero de costos por carga",
                            "00-gobierno/2026-04-06-contrato-oc-2214.md", "2026-04-06"),
              "due_date": campo("2026-08-29", "00-gobierno/2026-04-06-contrato-oc-2214.md", "2026-04-06"),
              "amount": campo(80000000, "00-gobierno/2026-04-06-contrato-oc-2214.md", "2026-04-06"),
              "state": campo("delivered", "30-reuniones/2026-09-03-seguimiento-proveedor.md", "2026-09-03"),
              "evidence": {"value": None, "source": None, "source_date": None, "state": "not_found"}},
         ]},
    ],
    "commitments": [
        {"who": campo("Paola Arias", "30-reuniones/2026-09-03-seguimiento-proveedor.md", "2026-09-03"),
         "what": campo("Entregar el cronograma de las veinte cargas siguientes",
                       "30-reuniones/2026-09-03-seguimiento-proveedor.md", "2026-09-03"),
         "due_date": campo("2026-09-12", "30-reuniones/2026-09-03-seguimiento-proveedor.md", "2026-09-03"),
         "stated_on": campo("2026-09-03", "30-reuniones/2026-09-03-seguimiento-proveedor.md", "2026-09-03"),
         "state": campo("open", "30-reuniones/2026-09-03-seguimiento-proveedor.md", "2026-09-03")},
    ],
    "activity": {
        "last_document_date": campo("2026-09-20", "20-seguimiento/2026-09-20-informe-avance.md", "2026-09-20"),
        "last_meeting_date": campo("2026-09-03", "30-reuniones/2026-09-03-seguimiento-proveedor.md", "2026-09-03"),
    },
}

FICHAS["PRY-004"] = {
    "schema_version": "0.1",
    "identity": {
        "code": campo("PRY-004", "00-gobierno/2025-02-14-memorando-inicio.md", "2025-02-14"),
        "name": campo("Iniciativa de Open Banking", "00-gobierno/2025-02-14-memorando-inicio.md", "2025-02-14"),
        "business_area": campo("Arquitectura", "00-gobierno/2025-02-14-memorando-inicio.md", "2025-02-14"),
        "sponsor": campo("Ricardo Salazar, CIO", "00-gobierno/2025-02-14-memorando-inicio.md", "2025-02-14"),
        "manager": campo("Jorge Ruiz", "00-gobierno/2025-02-14-memorando-inicio.md", "2025-02-14"),
        "committee": campo("Comité de Tecnología", "00-gobierno/2025-02-14-memorando-inicio.md", "2025-02-14"),
        "authority": {"value": None, "source": None, "source_date": None, "state": "not_found"},
    },
    "declared": {
        "status": campo("verde", "20-seguimiento/2026-04-30-nota-avance.md", "2026-04-30"),
        "as_of": campo("2026-04-30", "20-seguimiento/2026-04-30-nota-avance.md", "2026-04-30"),
    },
    "plan": {
        "start_date": {"value": None, "source": None, "source_date": None, "state": "not_found"},
        "end_date": {"value": None, "source": None, "source_date": None, "state": "not_found"},
        "baseline": [],
        "milestones": [],
    },
    "money": {
        "currency": {"value": None, "source": None, "source_date": None, "state": "not_found"},
        "approved": {"value": None, "source": None, "source_date": None, "state": "not_found"},
    },
    "activity": {
        "last_document_date": campo("2026-04-30", "20-seguimiento/2026-04-30-nota-avance.md", "2026-04-30"),
    },
}

FICHAS["PRY-005"] = {
    "schema_version": "0.1",
    "identity": {
        "code": campo("PRY-005", "00-gobierno/2026-05-04-acta-constitucion.md", "2026-05-04"),
        "name": campo("Débito contactless", "00-gobierno/2026-05-04-acta-constitucion.md", "2026-05-04"),
        "business_area": campo("Medios de Pago", "00-gobierno/2026-05-04-acta-constitucion.md", "2026-05-04"),
        "product": campo("Tarjeta débito", "00-gobierno/2026-05-04-acta-constitucion.md", "2026-05-04"),
        "sponsor": campo("Sandra Gil, VP de Operaciones",
                         "00-gobierno/2026-05-04-acta-constitucion.md", "2026-05-04"),
        "manager": campo("Paula Betancur", "00-gobierno/2026-05-04-acta-constitucion.md", "2026-05-04"),
        "committee": campo("Comité de Medios de Pago", "00-gobierno/2026-05-04-acta-constitucion.md", "2026-05-04"),
        "authority": campo("hasta 40.000.000 y ajustes de cronograma menores a 15 días",
                           "00-gobierno/2026-05-04-acta-constitucion.md", "2026-05-04"),
    },
    "declared": {
        "status": campo("verde", "20-seguimiento/2026-09-26-informe-avance.md", "2026-09-26"),
        "progress_pct": campo(72, "20-seguimiento/2026-09-26-informe-avance.md", "2026-09-26"),
        "as_of": campo("2026-09-26", "20-seguimiento/2026-09-26-informe-avance.md", "2026-09-26"),
    },
    "plan": {
        "start_date": campo("2026-05-11", "00-gobierno/2026-05-04-acta-constitucion.md", "2026-05-04"),
        "end_date": campo("2026-11-30", "10-plan/2026-05-11-cronograma-v1.csv", "2026-05-11"),
        "baseline": [
            {"version": 1, "approved_on": "2026-05-04", "start_date": "2026-05-11",
             "end_date": "2026-11-30", "reason": "inicial",
             "source": "00-gobierno/2026-05-04-acta-constitucion.md"},
        ],
        "milestones": [
            {"name": campo("Certificación con el esquema", "10-plan/2026-05-11-cronograma-v1.csv", "2026-05-11"),
             "baseline_date": campo("2026-07-31", "10-plan/2026-05-11-cronograma-v1.csv", "2026-05-11"),
             "current_date": campo("2026-07-24", "10-plan/2026-05-11-cronograma-v1.csv", "2026-05-11"),
             "state": campo("met", "10-plan/2026-05-11-cronograma-v1.csv", "2026-05-11"),
             "evidence": campo("20-seguimiento/2026-07-24-certificado-esquema.md",
                               "10-plan/2026-05-11-cronograma-v1.csv", "2026-05-11")},
            {"name": campo("Piloto en 50 comercios", "10-plan/2026-05-11-cronograma-v1.csv", "2026-05-11"),
             "baseline_date": campo("2026-09-11", "10-plan/2026-05-11-cronograma-v1.csv", "2026-05-11"),
             "current_date": campo("2026-09-11", "10-plan/2026-05-11-cronograma-v1.csv", "2026-05-11"),
             "state": campo("met", "20-seguimiento/2026-09-11-acta-cierre-piloto.md", "2026-09-11"),
             "evidence": campo("20-seguimiento/2026-09-11-acta-cierre-piloto.md",
                               "20-seguimiento/2026-09-11-acta-cierre-piloto.md", "2026-09-11")},
            {"name": campo("Despliegue masivo", "10-plan/2026-05-11-cronograma-v1.csv", "2026-05-11"),
             "baseline_date": campo("2026-11-13", "10-plan/2026-05-11-cronograma-v1.csv", "2026-05-11"),
             "current_date": campo("2026-11-13", "10-plan/2026-05-11-cronograma-v1.csv", "2026-05-11"),
             "state": campo("pending", "10-plan/2026-05-11-cronograma-v1.csv", "2026-05-11"),
             "evidence": {"value": None, "source": None, "source_date": None, "state": "not_found"}},
        ],
    },
    "money": {
        "currency": campo("COP", "20-seguimiento/2026-09-26-informe-avance.md", "2026-09-26"),
        "approved": campo(900000000, "20-seguimiento/2026-09-26-informe-avance.md", "2026-09-26"),
        "committed": campo(540000000, "20-seguimiento/2026-09-26-informe-avance.md", "2026-09-26"),
        "executed": campo(498000000, "20-seguimiento/2026-09-26-informe-avance.md", "2026-09-26"),
        "projection": campo(880000000, "20-seguimiento/2026-09-26-informe-avance.md", "2026-09-26"),
    },
    "commitments": [
        {"who": campo("Iván Duarte", "30-reuniones/2026-09-24-seguimiento-semanal.md", "2026-09-24"),
         "what": campo("Entregar el plan de capacitación de la red de oficinas",
                       "30-reuniones/2026-09-24-seguimiento-semanal.md", "2026-09-24"),
         "due_date": campo("2026-10-15", "30-reuniones/2026-09-24-seguimiento-semanal.md", "2026-09-24"),
         "stated_on": campo("2026-09-24", "30-reuniones/2026-09-24-seguimiento-semanal.md", "2026-09-24"),
         "state": campo("open", "30-reuniones/2026-09-24-seguimiento-semanal.md", "2026-09-24")},
    ],
    "activity": {
        "last_document_date": campo("2026-09-26", "20-seguimiento/2026-09-26-informe-avance.md", "2026-09-26"),
        "last_meeting_date": campo("2026-09-24", "30-reuniones/2026-09-24-seguimiento-semanal.md", "2026-09-24"),
    },
}

FICHAS["PRY-006"] = {
    "schema_version": "0.1",
    "identity": {
        "code": campo("PRY-006", "00-gobierno/2026-01-26-acta-constitucion.md", "2026-01-26"),
        "name": campo("Renovación del monitoreo SARLAFT",
                      "00-gobierno/2026-01-26-acta-constitucion.md", "2026-01-26"),
        "business_area": campo("Cumplimiento", "00-gobierno/2026-01-26-acta-constitucion.md", "2026-01-26"),
        "sponsor": campo("Beatriz Ocampo, Oficial de Cumplimiento",
                         "00-gobierno/2026-01-26-acta-constitucion.md", "2026-01-26"),
        "manager": campo("Nicolás Ortega", "00-gobierno/2026-01-26-acta-constitucion.md", "2026-01-26"),
        "committee": campo("Comité de Riesgos", "00-gobierno/2026-01-26-acta-constitucion.md", "2026-01-26"),
        "authority": campo("hasta 25.000.000", "00-gobierno/2026-01-26-acta-constitucion.md", "2026-01-26"),
    },
    "declared": {
        "status": campo("verde", "20-seguimiento/2026-08-12-informe-avance.md", "2026-08-12"),
        "progress_pct": campo(55, "20-seguimiento/2026-08-12-informe-avance.md", "2026-08-12"),
        "as_of": campo("2026-08-12", "20-seguimiento/2026-08-12-informe-avance.md", "2026-08-12"),
    },
    "plan": {
        "start_date": campo("2026-02-02", "00-gobierno/2026-01-26-acta-constitucion.md", "2026-01-26"),
        "end_date": campo("2026-10-30", "00-gobierno/2026-01-26-acta-constitucion.md", "2026-01-26"),
        "baseline": [
            {"version": 1, "approved_on": "2026-01-26", "start_date": "2026-02-02",
             "end_date": "2026-10-30", "reason": "inicial",
             "source": "00-gobierno/2026-01-26-acta-constitucion.md"},
        ],
        "milestones": [],
    },
    "money": {
        "currency": campo("COP", "20-seguimiento/2026-08-12-informe-avance.md", "2026-08-12"),
        "approved": campo(1100000000, "20-seguimiento/2026-08-12-informe-avance.md", "2026-08-12"),
        "committed": campo(700000000, "20-seguimiento/2026-08-12-informe-avance.md", "2026-08-12"),
        "executed": campo(430000000, "20-seguimiento/2026-08-12-informe-avance.md", "2026-08-12"),
        "projection": campo(1290000000, "20-seguimiento/2026-08-12-informe-avance.md", "2026-08-12"),
    },
    "changes": [
        {"ref": campo("CC-07", "20-seguimiento/2026-07-08-solicitud-cambio-cc-07.md", "2026-07-08"),
         "requested_on": campo("2026-07-08", "20-seguimiento/2026-07-08-solicitud-cambio-cc-07.md", "2026-07-08"),
         "scope_impact": campo("se suman las tipologías de moneda extranjera",
                               "20-seguimiento/2026-07-08-solicitud-cambio-cc-07.md", "2026-07-08"),
         "time_impact": campo("tres meses", "20-seguimiento/2026-07-08-solicitud-cambio-cc-07.md", "2026-07-08"),
         "cost_impact": campo("180.000.000 adicionales",
                              "20-seguimiento/2026-07-08-solicitud-cambio-cc-07.md", "2026-07-08"),
         "decision": campo("approved", "20-seguimiento/2026-07-08-solicitud-cambio-cc-07.md", "2026-07-08"),
         "decided_by": campo("Comité de Riesgos",
                             "20-seguimiento/2026-07-08-solicitud-cambio-cc-07.md", "2026-07-08")},
    ],
    "activity": {
        "last_document_date": campo("2026-08-12", "20-seguimiento/2026-08-12-informe-avance.md", "2026-08-12"),
    },
}

# ══════════════════════════════════════════════════════════════════════════
# Las respuestas conocidas. Escritas a mano leyendo los documentos.
# ══════════════════════════════════════════════════════════════════════════

HALLAZGOS = {
    "as_of": HOY,
    "nota": ("Respuestas conocidas para la corrida con --today 2026-09-30. Escritas a mano "
             "desde los documentos de input/, no calculadas. `senales` es el conjunto exacto: "
             "el grader falla igual si falta una o si aparece una que no está."),
    "proyectos": {
        "PRY-001": {
            "por_que": "Declara verde en agosto y la evidencia no lo sostiene. Es el caso central.",
            "senales": ["budget_committed", "commitment_overdue", "contradiction",
                        "declaration_stale", "declared_vs_evidence", "milestone_overdue",
                        "commitment_rescheduled", "rebaseline_unauthorized", "silent",
                        "variance_time"],
            "valores": {
                "days_silent": 19,
                "replans": 1,
                "slip_vs_original_days": 61,
                "slip_vs_current_days": 0,
                "milestones_overdue": 1,
                "commitments_overdue": 1,
                "commitments_rescheduled": 1,
                "commitments_undated": 0,
                "money.pct_committed": 95.2,
                "money.available_real": 88000000,
                # la proyección se pasa del aprobado, pero solo 3,2%: bajo el umbral
                "money.projection_over_pct": 3.2,
                "changes.baseline_moved_days": 61,
                "changes.approved_time_days": 60,
                "changes.unauthorized_days": 1,
                "declared.age_days": 39,
            },
            "comentario": ("La replanificación movió 61 días y el comité autorizó 60. Un día de "
                           "diferencia es un caso a propósito: el hallazgo no es el tamaño, es "
                           "que ningún documento autoriza la diferencia."),
        },
        "PRY-002": {
            "por_que": "Declara amarillo, y se movió mucho. El amarillo no dispara la alerta de brecha.",
            "senales": ["commitment_undated", "variance_time"],
            "valores": {
                "commitments_undated": 1,
                "commitments_overdue": 0,
                "days_silent": 5,
                "replans": 0,
                "slip_vs_original_days": 91,
                "milestones_overdue": 0,
                "declared.age_days": 5,
            },
            "comentario": ("Dos controles en un proyecto. Primero, el amarillo: hay señales y "
                           "`declared_vs_evidence` NO debe aparecer, porque quien ya reportó "
                           "problema no está escondiendo nada. Segundo, el hito que se movió: su "
                           "fecha de línea base ya pasó, pero su fecha vigente es de diciembre, "
                           "así que NO es un hito vencido. El atraso sale como desviación contra "
                           "la línea base, que es donde corresponde. Confundir las dos cosas "
                           "sería contar el mismo atraso dos veces."),
        },
        "PRY-003": {
            "por_que": "El proyecto de proveedores.",
            "senales": ["commitment_overdue", "vendor_accepted_without_evidence",
                        "vendor_deliverable_late", "vendor_invoiced_over_accepted"],
            "valores": {
                "days_silent": 10,
                "commitments_overdue": 1,
                "vendors.0.late": 1,
                "vendors.0.accepted_without_evidence": 2,
                "vendors.0.accepted": 3,
                "vendors.0.amount_accepted": 580000000,
                "vendors.0.amounts_declared": 4,
            },
            "comentario": ("`vendor_invoiced_without_delivery` NO aparece, y está bien: hay "
                           "facturación y también entregables aceptados. Lo que sí aparece es "
                           "`vendor_invoiced_over_accepted`, que es la pregunta que Finanzas hace "
                           "en la minuta: se facturaron 620 millones contra 580 de entregables "
                           "aceptados. Ese hallazgo no existía hasta que el esquema tuvo monto por "
                           "entregable, y el monto entró porque esta misma prueba mostró el hueco."),
        },
        "PRY-004": {
            "por_que": "El proyecto sin plan aprobado, que es el caso más común en una PMO real.",
            "senales": ["declaration_stale", "declared_vs_evidence", "silent"],
            "valores": {
                "days_silent": 153,
                "has_baseline": False,
                "declared.age_days": 153,
            },
            "comentario": ("Declara verde y tiene señales, así que `declared_vs_evidence` SÍ aparece: "
                           "el silencio de cinco meses es una señal que ese verde no explica. "
                           "Sin línea base no hay desviación medible, y eso se reporta como vacío."),
        },
        "PRY-005": {
            "por_que": "CONTROL NEGATIVO. Todo en orden. Ninguna alerta.",
            "senales": [],
            "valores": {
                "days_silent": 4,
                "replans": 0,
                "slip_vs_original_days": 0,
                "milestones_overdue": 0,
                "commitments_overdue": 0,
                "money.pct_committed": 60.0,
                "declared.age_days": 4,
            },
            "comentario": ("Si este proyecto alerta, el agente es un generador de ruido y no sirve. "
                           "Es la prueba más importante del conjunto."),
        },
        "PRY-006": {
            "por_que": "El cambio aprobado que nadie bajó al plan, con impacto escrito en meses.",
            "senales": ["declaration_stale", "declared_vs_evidence", "silent", "variance_cost"],
            "valores": {
                "days_silent": 49,
                "replans": 0,
                "changes.time_impact_unreadable": 1,
                "changes.approved_time_days": 0,
                "changes.approved_without_new_baseline": 0,
                "money.projection_over_pct": 17.3,
                "declared.age_days": 49,
            },
            "comentario": ("«Tres meses» queda ilegible en vez de convertirse en 90 días inventados, "
                           "y por eso mismo el cambio no suma a `approved_time_days` ni entra en "
                           "`approved_without_new_baseline`: el impacto no se pudo leer. Ese "
                           "encadenamiento es un límite conocido del diseño, no del proyecto: un "
                           "cambio aprobado que movió fechas y quedó ilegible desaparece del control "
                           "de replanificación, y solo se ve en la lista de ilegibles. "
                           "El sobrecosto sí se ve: el comité autorizó 180.000.000 y el presupuesto "
                           "aprobado nunca se actualizó, así que la proyección se pasa 17,3%."),
        },
    },
    "totales": {
        "projects": 6,
        "no_baseline": 1,
        "green_contradicted": 3,
        "products": 2,
        "no_authority": 2,
    },
}

# ══════════════════════════════════════════════════════════════════════════

# ══════════════════════════════════════════════════════════════════════════
# Las citas y el registro de documentos leídos
#
# Una cita tiene que ser resoluble desde la raíz de documentación, no desde la
# carpeta del proyecto: es lo que permite que `index` cruce lo que hay en disco
# contra lo que las fichas dicen haber leído, con un solo join. Aquí se le pone el
# prefijo de la carpeta a cada `source`, y de ahí sale `meta.documents_seen` con el
# hash de bytes y el hash del texto de cada documento citado.
# ══════════════════════════════════════════════════════════════════════════

CARPETAS = {
    "PRY-001": "PRY-001-originacion-digital",
    "PRY-002": "PRY-002-core-depositos",
    "PRY-003": "PRY-003-migracion-nube",
    "PRY-004": "PRY-004-open-banking",
    "PRY-005": "PRY-005-debito-contactless",
    "PRY-006": "PRY-006-sarlaft",
}


def prefijar(nodo, carpeta):
    """Vuelve toda cita relativa a la raíz de documentación."""
    if isinstance(nodo, dict):
        for clave in ("source", "evidence"):
            v = nodo.get(clave)
            if isinstance(v, str) and v and not v.startswith(carpeta) and "/" in v:
                nodo[clave] = f"{carpeta}/{v}"
        for v in nodo.values():
            prefijar(v, carpeta)
    elif isinstance(nodo, list):
        for v in nodo:
            prefijar(v, carpeta)


def documentos_leidos(ficha, carpeta):
    """El registro de lo leído, con los dos hashes. Sale de las citas de la ficha."""
    import importlib.util
    ruta_pmo = RAIZ.parent.parent / "plugins" / "criterio-pmo" / "scripts" / "pmo.py"
    spec = importlib.util.spec_from_file_location("pmo", ruta_pmo)
    pmo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(pmo)

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
        salida.append({
            "path": cita,
            "hash": pmo.hash_bytes(archivo),
            "text_hash": pmo.hash_texto(archivo),
            "date": archivo.name[:10] if archivo.name[:4].isdigit() else None,
        })
    return salida


if __name__ == "__main__":
    for carpeta in (EXPECTED / "fichas",):
        if carpeta.exists():
            shutil.rmtree(carpeta)
    for codigo, ficha in FICHAS.items():
        carpeta = CARPETAS[codigo]
        prefijar(ficha, carpeta)
        ficha["meta"] = {"record_updated": HOY,
                         "documents_seen": documentos_leidos(ficha, carpeta)}
        escribir(EXPECTED / "fichas" / f"{codigo}.json",
                 json.dumps(ficha, ensure_ascii=False, indent=2))
    escribir(EXPECTED / "hallazgos.json", json.dumps(HALLAZGOS, ensure_ascii=False, indent=2))

    docs = sum(len(f) for _, _, f in os.walk(INPUT))
    print(f"input/     {docs} documentos en {len(FICHAS)} proyectos")
    print(f"expected/  {len(FICHAS)} fichas de referencia y las respuestas conocidas")
    print(f"corrida:   --today {HOY}")
