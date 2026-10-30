# /criterio-sales:sales-setup comercial/900000002-comercial-control-andina

Soy Augusto. Dejé la instalación lista para Comercial Control Andina (900000002) y corrí el primer pipeline-check de octubre. No encontró nada que atender: ninguna oportunidad le falta evidencia, está detenida o corrió su cierre de más.

- **Carpeta:** `comercial/900000002-comercial-control-andina` vino en el argumento. Tiene 21 documentos, ninguno fuera de lugar ni ilegible. No marqué la raíz con `_CRITERIO_COMERCIAL.txt`, porque nadie lo autorizó.
- **Exportaciones del CRM:**
  - Las tres de `10-crm/` (2026-10-01, 2026-10-16 y 2026-11-03) se reconocieron como CRM distinto de Salesforce y HubSpot. Tienen 7 filas cada una y no les falta ninguna columna.
  - Registré qué columna trae cada dato: monto = «Valor estimado», cierre = «Fecha estimada de cierre» y última actividad = «Última gestión».
  - Las fechas van día/mes, porque hay una como 22/10/2026.
- **Términos (versión 1.3):** José Francisco Ñáñez los aceptó el 2026-11-05. Mostré el `en_corto` tal cual en la salida guardada. El comprobante quedó en `.criterio/terminos/` en Markdown y PDF.
- **Preguntas que respondí yo, por ser una sesión sin interfaz:**
  - Periodo 2026-10, porque el acta del comité compromete el pronóstico de octubre.
  - Umbrales de 30 días sin actividad y 2 cierres corridos. Son los valores por omisión: ningún documento dice otros.
  - Entidad, país y moneda: Colombia, COP.
- **Ficha de 2026-10:**
  - Lleva 8 documentos de evidencia: las propuestas de OPP-1301, 1302, 1303, 1304 y 1307, y las órdenes de compra de OPP-1301, 1302 y 1303.
  - Lleva también el pronóstico comprometido por el comité el 2026-10-02: $ 189.000.000. El mejor escenario del acta, $ 288.000.000, no se compromete y no va a la ficha.
  - Los correos y teléfonos que traen las propuestas no entraron.
- **Dónde quedó todo:**
  - Configuración: `.criterio/comercial/900000002-comercial-control-andina/config.json`.
  - Reporte: `estado-comercial/900000002-comercial-control-andina/comercial/2026-10/reporte-pipeline-check.md`.
  - Salida de esta sesión: `estado-comercial/900000002-comercial-control-andina/corridas/salida-sales-setup.md`.
  - La corrida quedó registrada como `2026-11-05-sales-setup-1`.

# El embudo contra su evidencia · Comercial Control Andina · periodo 2026-10

**Entidad:** Comercial Control Andina (900000002) · **Fecha de corte:** 2026-11-03 · **Procesado:** 2026-11-05 · **Agente:** Augusto, versión 0.1.0 · **Comando:** `pipeline-check`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

| Oportunidad | Etapa | Monto | Cierre | Falta | Días sin actividad | Veces corrido |
|---|---|---|---|---|---|---|
| OPP-1301 · Renovación de licencias | Ganada | 72.000.000,00 | 2026-10-10 | — | 26 | 0 |
| OPP-1302 · Proyecto de expansión | Ganada | 108.000.000,00 | 2026-10-22 | — | 14 | 0 |
| OPP-1303 · Suministro anual | Compromiso | 150.000.000,00 | 2026-11-20 | — | 6 | 0 |
| OPP-1304 · Servicio de soporte | Propuesta | 54.000.000,00 | 2026-12-15 | — | 7 | 1 |
| OPP-1305 · Ampliación de contrato | Calificación | 42.000.000,00 | 2026-12-20 | — | 9 | 0 |
| OPP-1307 · Implementación por fases | Negociación | 66.000.000,00 | 2026-12-18 | — | 5 | 1 |

Sin calificar a quien lleva cada oportunidad: la señal es de la oportunidad, no de la persona.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿De qué CRM sale la exportación y qué columna trae cada dato? → Un CRM distinto de Salesforce y HubSpot, con cabeceras en español; se registró el mapeo de monto (Valor estimado), cierre (Fecha estimada de cierre) y última actividad (Última gestión).
- ¿Las fechas van día/mes o mes/día? → Día/mes: hay fechas con el día mayor que 12, como 22/10/2026.
- ¿Qué periodo se revisa? → 2026-10: el acta del comité compromete el pronóstico de octubre.
- ¿Cuántos días sin actividad detienen una oportunidad y cuántas veces puede correrse un cierre? → 30 días y 2 veces, los valores por omisión de la configuración de ejemplo; ningún documento dice otros.

## Fuentes

- Sin documentos citados.