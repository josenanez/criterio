# /criterio-risk-events:kri-check 

Los 7 indicadores del marco no traen valor en 2026-11, así que ninguno se pudo contrastar con su umbral. El reporte lo escribió el motor.

# Cada indicador contra su umbral · Seguros del Sur Sintética · periodo 2026-11

**Entidad:** Seguros del Sur Sintética (20607773331) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Casandra, versión 0.2.0 · **Comando:** `kri-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un indicador clave no tiene valor en el periodo (`kri_not_reported`) | KRI-01 · Transacciones fraudulentas por millón: no tiene valor en 2026-11 | — | Operaciones | — | `00-marco/indicadores_clave.xlsx` fila 2 |
| 2 | Un indicador clave no tiene valor en el periodo (`kri_not_reported`) | KRI-02 · Disponibilidad de los canales digitales: no tiene valor en 2026-11 | — | Tecnología | — | `00-marco/indicadores_clave.xlsx` fila 3 |
| 3 | Un indicador clave no tiene valor en el periodo (`kri_not_reported`) | KRI-03 · Rotación del personal de crédito: no tiene valor en 2026-11 | — | Vicepresidencia de crédito | — | `00-marco/indicadores_clave.xlsx` fila 4 |
| 4 | Un indicador clave no tiene valor en el periodo (`kri_not_reported`) | KRI-05 · Concentración de los depósitos en los 20 mayores: no tiene valor en 2026-11 | — | Tesorería | — | `00-marco/indicadores_clave.xlsx` fila 5 |
| 5 | Un indicador clave no tiene valor en el periodo (`kri_not_reported`) | KRI-06 · Partidas sin conciliar a fin de mes: no tiene valor en 2026-11 | — | Tesorería | — | `00-marco/indicadores_clave.xlsx` fila 6 |
| 6 | Un indicador clave no tiene valor en el periodo (`kri_not_reported`) | KRI-12 · Reclamos por cada 10.000 clientes: no tiene valor en 2026-11 | — | Mercadeo | — | `00-marco/indicadores_clave.xlsx` fila 7 |
| 7 | Un indicador clave no tiene valor en el periodo (`kri_not_reported`) | KRI-22 · Cancelaciones de productos en el primer mes: no tiene valor en 2026-11 | — | Mercadeo | — | `00-marco/indicadores_clave.xlsx` fila 8 |

## El resultado

| Indicador | Sentido | Alerta | Límite | Valor del periodo | Zona | Acción |
|---|---|---|---|---|---|---|
| KRI-01 · Transacciones fraudulentas por millón | mayor es peor | 40 | 60 | — | sin valor | no |
| KRI-02 · Disponibilidad de los canales digitales | menor es peor | 99.5 | 99 | — | sin valor | no |
| KRI-03 · Rotación del personal de crédito | mayor es peor | 8 | 12 | — | sin valor | no |
| KRI-05 · Concentración de los depósitos en los 20 mayores | mayor es peor | 25 | 30 | — | sin valor | no |
| KRI-06 · Partidas sin conciliar a fin de mes | mayor es peor | 5 | 10 | — | sin valor | no |
| KRI-12 · Reclamos por cada 10.000 clientes | mayor es peor | 15 | 25 | — | sin valor | no |
| KRI-22 · Cancelaciones de productos en el primer mes | mayor es peor | 10 | 15 | — | sin valor | no |

Los umbrales los fija el marco de apetito de la organización.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-marco/indicadores_clave.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cro/FUENTES.es.md)

---

- Los términos (versión 1.6) ya estaban vigentes y aceptados. No hubo que registrar la aceptación a nombre de José Francisco Ñáñez, y no la registré.
- El reporte está en `eventos/2026-11/reporte-kri-check.md`. La salida completa quedó en `corridas/salida-kri-check.md`.
- La corrida quedó registrada como `2026-11-25-kri-check-1`.