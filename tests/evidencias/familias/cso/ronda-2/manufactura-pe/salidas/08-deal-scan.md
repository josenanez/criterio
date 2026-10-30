# /criterio-revenue:deal-scan 

Cinco cotizaciones de `40-cotizaciones/` quedaron en la ficha de 2026-10. El inventario no trajo documentos nuevos. El reporte trae 8 señales. Los términos ya estaban vigentes (versión 1.3, aceptada por José Francisco Ñáñez el 2026-11-05).

# Qué cambió en lo vendido · Industrias del Rímac · periodo 2026-10

**Entidad:** Industrias del Rímac (20210045016) · **Fecha de corte:** 2026-10-31 · **Procesado:** 2026-11-05 · **Agente:** Valeria, versión 0.2.0 · **Comando:** `deal-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Días | Cita |
|---|---|---|---|---|---|
| 1 | Ganada sin contrato firmado en la ficha de Fidel (`won_without_contract`) | OPP-2008: ganada el 2026-10-05 por 200,000.00; sin contrato firmado con el cliente 20200001029 | 200,000.00 | 31 | `10-crm/oportunidades-2026-11-03.csv` fila 9 |
| 2 | Ganada sin contrato firmado (`won_without_contract`) | OPP-2032: ganada el 2026-10-07 por 160,000.00; sin contrato firmado con el cliente 20200001088 | 160,000.00 | 29 | `10-crm/oportunidades-2026-11-03.csv` fila 22 |
| 3 | Contrato firmado sin factura en la ficha de Clara (`signed_without_invoice`) | CTR-2031: firmado con el cliente 20200001100 el 2026-09-09; sin factura emitida hasta el 2026-10-09 | 160,000.00 | 27 | `contratos/CTR-2031.json` |
| 4 | Ganada sin contrato firmado (`won_without_contract`) | OPP-2031: ganada el 2026-10-06 por 120,000.00; sin contrato firmado con el cliente 20200001070 | 120,000.00 | 30 | `10-crm/oportunidades-2026-11-03.csv` fila 21 |
| 5 | Contrato firmado sin factura (`signed_without_invoice`) | CTR-2030: firmado con el cliente 20200001096 el 2026-09-08; sin factura emitida hasta el 2026-10-08 | 120,000.00 | 28 | `contratos/CTR-2030.json` |
| 6 | Descuento fuera de la matriz (`discount_outside_policy`) | COT-2003 · OPP-2003: ningún nivel de la matriz cubre un descuento de 35 % | 406,000.00 | — | `40-cotizaciones/COT-2003_cotizacion.pdf` |
| 7 | Descuento fuera de la matriz (`discount_outside_policy`) | COT-2005 · OPP-2030: ningún nivel de la matriz cubre un descuento de 35 % | 168,000.00 | — | `40-cotizaciones/COT-2005_cotizacion.pdf` |
| 8 | Descuento fuera de la matriz (`discount_outside_policy`) | COT-2004 · OPP-2029: ningún nivel de la matriz cubre un descuento de 35 % | 154,000.00 | — | `40-cotizaciones/COT-2004_cotizacion.pdf` |

## El resultado

**Cotizaciones en la ficha:** 5 · **Exportación:** `10-crm/oportunidades-2026-11-03.csv`

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- COT-2001 dice "Descuento dentro del nivel sin aprobación": ¿se deja la aprobación vacía? → Sí: nadie la firmó. La matriz decide si el 10 % la exigía.

## Fuentes

- `10-crm/oportunidades-2026-11-03.csv`
- `40-cotizaciones/COT-2003_cotizacion.pdf`, `COT-2004_cotizacion.pdf` y `COT-2005_cotizacion.pdf`
- `contratos/CTR-2030.json` y `contratos/CTR-2031.json`

La corrida quedó registrada como `2026-11-05-deal-scan-1`, con la salida guardada en `estado-comercial/20210045016-industrias-del-rimac/corridas/salida-deal-scan.md`.

Escribí a mano la ficha `ingresos/2026-10/ficha.json`, porque no existía. Mi primera versión de la pregunta de COT-2001 tenía un formato que el motor rechazó con un error. Lo corregí y el cálculo corrió bien.