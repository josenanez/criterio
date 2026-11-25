# /criterio-risk-events:kri-check 

Revisé los indicadores clave de 2026-10 contra los umbrales del marco. Hay uno en alerta sin acción registrada.

# Cada indicador contra su umbral · Seguros del Sur Sintética · periodo 2026-10

**Entidad:** Seguros del Sur Sintética (20607773331) · **Fecha de corte:** 2026-11-25 · **Agente:** Casandra, versión 0.1.0 · **Comando:** `kri-check`

## Lo que hay que atender

| # | Señal | Qué | Responsable | Cita |
|---|---|---|---|---|
| 1 | Indicador en alerta sin acción registrada (`kri_alert_without_action`) | KRI-01 · Transacciones fraudulentas por millón: dio 52 en 2026-10, en su zona de alerta (40), y no hay acción registrada en la tabla de acciones ni en un acta | Operaciones | `00-marco/indicadores_clave.xlsx` fila 2 · `20-indicadores/valores_indicadores_2026-10.xlsx` fila 2 |

## El resultado

| Indicador | Sentido | Alerta | Límite | Valor | Zona | Acción |
|---|---|---|---|---|---|---|
| KRI-01 · Transacciones fraudulentas por millón | mayor es peor | 40 | 60 | 52 | alerta | no |
| KRI-02 · Disponibilidad de los canales digitales | menor es peor | 99.5 | 99 | 99.6 | normal | no |
| KRI-03 · Rotación del personal de crédito | mayor es peor | 8 | 12 | 6.5 | normal | no |
| KRI-05 · Concentración de los depósitos en los 20 mayores | mayor es peor | 25 | 30 | 29 | alerta | sí |

Los umbrales los fija el marco de apetito de la organización. Todo lo que llegó se procesó, y el motor no hizo preguntas en esta corrida.

**Fuentes:** `00-marco/indicadores_clave.xlsx`, `20-indicadores/valores_indicadores_2026-10.xlsx`, F-01 (families/criterio-cro/FUENTES.es.md).

El reporte completo está en `estado-riesgos/20607773331-seguros-del-sur-sintetica/eventos/2026-10/reporte-kri-check.md`. La corrida quedó registrada como `2026-11-25-kri-check-1`.

Dos aclaraciones sobre cómo la corrí:
- **Términos:** ya estaban vigentes (versión 1.6, aceptación registrada en 0.1.0), así que no hubo nada que registrar a nombre de José Francisco Ñáñez.
- **Periodo:** no venía en el argumento. Usé 2026-10, que es el que tiene valores cargados, y lo dejo anotado como supuesto.