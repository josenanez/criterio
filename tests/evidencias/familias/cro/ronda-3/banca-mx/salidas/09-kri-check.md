# /criterio-risk-events:kri-check 

Periodo procesado: 2026-10, el mes anterior a la fecha de la prueba (2026-11-25). El comando no indicaba periodo, así que lo elegí yo. Los términos (v1.6) ya estaban vigentes, así que no pedí aceptarlos de nuevo. Cuatro indicadores piden atención. Los umbrales los fija el marco.

# Cada indicador contra su umbral · Banco Mesoamericano Sintético · periodo 2026-10

**Entidad:** Banco Mesoamericano Sintético (BMS0907153R2) · **Fecha de corte:** 2026-11-25 · **Agente:** Casandra 1.0.0 · **Comando:** `kri-check`

## Lo que hay que atender

| # | Señal | Qué | Responsable | Cita |
|---|---|---|---|---|
| 1 | En alerta, sin acción registrada | KRI-01 · Transacciones fraudulentas por millón: dio 52, en su zona de alerta (40); no hay acción en la tabla de acciones ni en un acta | Operaciones | `00-marco/indicadores_clave.xlsx` fila 2 · `20-indicadores/valores_indicadores_2026-10.xlsx` fila 2 |
| 2 | En alerta, sin acción registrada | KRI-12 · Reclamos por cada 10.000 clientes: dio 19, en su zona de alerta (15); no hay acción registrada | Mercadeo | `00-marco/indicadores_clave.xlsx` fila 7 · `20-indicadores/valores_indicadores_2026-10.xlsx` fila 6 |
| 3 | Sin valor en el periodo | KRI-03 · Rotación del personal de crédito | Vicepresidencia de crédito | `00-marco/indicadores_clave.xlsx` fila 4 |
| 4 | Sin valor en el periodo | KRI-22 · Cancelaciones de productos en el primer mes | Mercadeo | `00-marco/indicadores_clave.xlsx` fila 8 |

## El resultado

| Indicador | Sentido | Alerta | Límite | Valor | Zona | Acción |
|---|---|---|---|---|---|---|
| KRI-01 · Transacciones fraudulentas por millón | mayor es peor | 40 | 60 | 52 | alerta | no |
| KRI-02 · Disponibilidad de los canales digitales | menor es peor | 99.5 | 99 | 99.6 | normal | no |
| KRI-03 · Rotación del personal de crédito | mayor es peor | 8 | 12 | — | sin valor | no |
| KRI-05 · Concentración de los depósitos en los 20 mayores | mayor es peor | 25 | 30 | 29 | alerta | sí |
| KRI-06 · Partidas sin conciliar a fin de mes | mayor es peor | 5 | 10 | 7 | alerta | sí |
| KRI-12 · Reclamos por cada 10.000 clientes | mayor es peor | 15 | 25 | 19 | alerta | no |
| KRI-22 · Cancelaciones de productos en el primer mes | mayor es peor | 10 | 15 | — | sin valor | no |

## Lo que no se pudo procesar
Todo lo que llegó se procesó.

## Las preguntas que hizo
Ninguna en esta corrida.

## Fuentes
- `00-marco/indicadores_clave.xlsx`
- `20-indicadores/valores_indicadores_2026-10.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cro/FUENTES.es.md)

---
Corrida registrada como `2026-11-25-kri-check-1`. La salida completa está en `estado-riesgos/bms0907153r2-banco-mesoamericano-sintetico/corridas/salida-kri-check.md`. El reporte del motor está en `estado-riesgos/bms0907153r2-banco-mesoamericano-sintetico/eventos/2026-10/reporte-kri-check.md`.