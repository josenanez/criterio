# /criterio-risk-events:kri-check 

Los nueve indicadores del marco salen sin valor en 2026-11, así que ninguno se pudo medir contra su umbral de alerta ni de límite. No hay ninguno en alerta; lo que falta es el dato del periodo.

Los términos (versión 1.6) estaban vigentes y ya aceptados, así que no hizo falta registrar nada. No hubo preguntas en esta corrida.

# Cada indicador contra su umbral · Banco Andino Sintético · periodo 2026-11

**Entidad:** Banco Andino Sintético (901777333) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Casandra, versión 0.2.0 · **Comando:** `kri-check`

## Lo que hay que atender

| # | Señal | Qué | Responsable | Cita |
|---|---|---|---|---|
| 1 | `kri_not_reported` | KRI-01 · Transacciones fraudulentas por millón | Operaciones | `00-marco/indicadores_clave.xlsx` fila 2 |
| 2 | `kri_not_reported` | KRI-02 · Disponibilidad de los canales digitales | Tecnología | fila 3 |
| 3 | `kri_not_reported` | KRI-03 · Rotación del personal de crédito | Vicepresidencia de crédito | fila 4 |
| 4 | `kri_not_reported` | KRI-05 · Concentración de los depósitos en los 20 mayores | Tesorería | fila 5 |
| 5 | `kri_not_reported` | KRI-06 · Partidas sin conciliar a fin de mes | Tesorería | fila 6 |
| 6 | `kri_not_reported` | KRI-12 · Reclamos por cada 10.000 clientes | Mercadeo | fila 7 |
| 7 | `kri_not_reported` | KRI-13 · Incidentes de seguridad por mes | Operaciones | fila 8 |
| 8 | `kri_not_reported` | KRI-22 · Cancelaciones de productos en el primer mes | Mercadeo | fila 9 |
| 9 | `kri_not_reported` | KRI-23 · Operaciones con errores de digitación | Vicepresidencia de crédito | fila 10 |

## El resultado

| Indicador | Sentido | Alerta | Límite | Valor del periodo | Zona | Acción |
|---|---|---|---|---|---|---|
| KRI-01 | mayor es peor | 40 | 60 | — | sin valor | no |
| KRI-02 | menor es peor | 99.5 | 99 | — | sin valor | no |
| KRI-03 | mayor es peor | 8 | 12 | — | sin valor | no |
| KRI-05 | mayor es peor | 25 | 30 | — | sin valor | no |
| KRI-06 | mayor es peor | 5 | 10 | — | sin valor | no |
| KRI-12 | mayor es peor | 15 | 25 | — | sin valor | no |
| KRI-13 | mayor es peor | 3 | 6 | — | sin valor | no |
| KRI-22 | mayor es peor | 10 | 15 | — | sin valor | no |
| KRI-23 | mayor es peor | 20 | 40 | — | sin valor | no |

Los umbrales los fija el marco de apetito de la organización.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-marco/indicadores_clave.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cro/FUENTES.es.md)

La corrida quedó registrada como `2026-11-25-kri-check-1`. El reporte completo está en `estado-riesgos/901777333-banco-andino-sintetico/eventos/2026-11/reporte-kri-check.md`. Lo que le mostré está en `corridas/salida-kri-check.md`, en la misma carpeta de estado.