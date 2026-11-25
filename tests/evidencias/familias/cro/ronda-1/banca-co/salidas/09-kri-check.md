# /criterio-risk-events:kri-check 

Los términos (v1.6) ya estaban vigentes, así que no registré ninguna aceptación nueva. Corrí el periodo 2026-10, que tiene los valores de indicadores más recientes.

# Cada indicador contra su umbral · Banco Andino Sintético · periodo 2026-10

**Entidad:** Banco Andino Sintético (901777333) · **Fecha de corte:** 2026-11-25 · **Agente:** Casandra, versión 0.1.0 · **Comando:** `kri-check`

## Lo que hay que atender

| # | Señal | Qué | Responsable | Cita |
|---|---|---|---|---|
| 1 | Indicador en alerta sin acción registrada (`kri_alert_without_action`) | KRI-01 · Transacciones fraudulentas por millón: dio 52 en 2026-10, en su zona de alerta (40). No hay acción en la tabla de acciones ni en un acta. | Operaciones | `00-marco/indicadores_clave.xlsx` fila 2 · `20-indicadores/valores_indicadores_2026-10.xlsx` fila 2 |
| 2 | Indicador sin valor en el periodo (`kri_not_reported`) | KRI-03 · Rotación del personal de crédito: no tiene valor en 2026-10. | Vicepresidencia de crédito | `00-marco/indicadores_clave.xlsx` fila 4 |

## El resultado

| Indicador | Sentido | Alerta | Límite | Valor | Zona | Acción |
|---|---|---|---|---|---|---|
| KRI-01 · Transacciones fraudulentas por millón | mayor es peor | 40 | 60 | 52 | alerta | no |
| KRI-02 · Disponibilidad de los canales digitales | menor es peor | 99.5 | 99 | 99.6 | normal | no |
| KRI-03 · Rotación del personal de crédito | mayor es peor | 8 | 12 | — | sin valor | no |
| KRI-05 · Concentración de los depósitos en los 20 mayores | mayor es peor | 25 | 30 | 29 | alerta | sí |

Los umbrales los fija el marco de apetito de la organización. Todo lo que llegó se procesó, y en esta corrida no hubo preguntas.

**Fuentes:** `00-marco/indicadores_clave.xlsx`, `20-indicadores/valores_indicadores_2026-10.xlsx`, F-01.

El reporte completo está en `estado-riesgos/901777333-banco-andino-sintetico/eventos/2026-10/reporte-kri-check.md`. La corrida quedó registrada como `2026-11-25-kri-check-1`, con la salida en `corridas/salida-kri-check.md`. Esa salida lleva al inicio una nota con el periodo y el estado de los términos, que no estaba en el reporte.