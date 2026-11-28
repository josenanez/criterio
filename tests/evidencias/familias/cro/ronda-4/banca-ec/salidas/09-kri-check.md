# /criterio-risk-events:kri-check 

Hay dos indicadores en alerta sin acción registrada y dos sin valor en el periodo. La decisión es del comité de riesgos y de las áreas.

# Cada indicador contra su umbral · Banco del Pichincha Sur Sintético · periodo 2026-10

**Entidad:** Banco del Pichincha Sur Sintético (1790123456001) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Casandra, versión 1.1.0 · **Comando:** `kri-check`

## Lo que hay que atender

| # | Señal | Qué | Responsable | Cita |
|---|---|---|---|---|
| 1 | Indicador en alerta sin acción registrada (`kri_alert_without_action`) | KRI-01 · Transacciones fraudulentas por millón: dio 52 en 2026-10, en su zona de alerta (40), y no hay una acción registrada en la tabla de acciones ni en un acta | Operaciones | `00-marco/indicadores_clave.xlsx` fila 2 · `20-indicadores/valores_indicadores_2026-10.xlsx` fila 2 |
| 2 | Indicador en alerta sin acción registrada (`kri_alert_without_action`) | KRI-12 · Reclamos por cada 10.000 clientes: dio 19 en 2026-10, en su zona de alerta (15), y no hay una acción registrada en la tabla de acciones ni en un acta | Mercadeo | `00-marco/indicadores_clave.xlsx` fila 7 · `20-indicadores/valores_indicadores_2026-10.xlsx` fila 6 |
| 3 | Indicador sin valor en el periodo (`kri_not_reported`) | KRI-03 · Rotación del personal de crédito: no tiene valor en 2026-10 | Vicepresidencia de crédito | `00-marco/indicadores_clave.xlsx` fila 4 |
| 4 | Indicador sin valor en el periodo (`kri_not_reported`) | KRI-22 · Cancelaciones de productos en el primer mes: no tiene valor en 2026-10 | Mercadeo | `00-marco/indicadores_clave.xlsx` fila 8 |

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

Los umbrales los fija el marco de apetito de la organización.

**No se pudo procesar:** nada, todo lo que llegó se procesó. **Preguntas que hizo:** ninguna.

**Fuentes:** `00-marco/indicadores_clave.xlsx`, `20-indicadores/valores_indicadores_2026-10.xlsx`, F-01 (families/criterio-cro/FUENTES.es.md).

---
Notas de la corrida:
- Los términos ya estaban vigentes (versión 1.6, aceptada en la instalación 1.1.0), así que no registré una aceptación nueva a nombre de José Francisco Ñáñez.
- El periodo (2026-10) salió de la configuración.
- Para mostrar el reporte resumí algunas columnas de la tabla «Lo que hay que atender». El reporte completo del motor está en `estado-riesgos/1790123456001-banco-del-pichincha-sur-sintetico/eventos/2026-10/reporte-kri-check.md`.
- La corrida quedó registrada como `2026-11-25-kri-check-1`, en `corridas/salida-kri-check.md`. Ese archivo contiene el reporte completo del motor, no la versión resumida que muestro aquí.