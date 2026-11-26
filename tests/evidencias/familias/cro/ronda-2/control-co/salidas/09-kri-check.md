# /criterio-risk-events:kri-check 

Los seis indicadores clave de 2026-11 salieron sin valor, así que no hay ninguno que comparar con su umbral. Los términos 1.6 ya estaban vigentes. La configuración está en `.criterio/eventos/901888444/config.json`.

# Cada indicador contra su umbral · Banco Control de Riesgos Sintético · periodo 2026-11

**Entidad:** Banco Control de Riesgos Sintético (901888444) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Casandra, versión 0.2.0 · **Comando:** `kri-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un indicador clave no tiene valor en el periodo (`kri_not_reported`) | KRI-01 · Transacciones fraudulentas por millón: no tiene valor en 2026-11 | — | Operaciones | — | `00-marco/indicadores_clave.xlsx` fila 2 |
| 2 | Un indicador clave no tiene valor en el periodo (`kri_not_reported`) | KRI-02 · Disponibilidad de los canales digitales: no tiene valor en 2026-11 | — | Tecnología | — | `00-marco/indicadores_clave.xlsx` fila 3 |
| 3 | Un indicador clave no tiene valor en el periodo (`kri_not_reported`) | KRI-03 · Rotación del personal de crédito: no tiene valor en 2026-11 | — | Vicepresidencia de crédito | — | `00-marco/indicadores_clave.xlsx` fila 4 |
| 4 | Un indicador clave no tiene valor en el periodo (`kri_not_reported`) | KRI-04 · Días sin una prueba del plan de continuidad: no tiene valor en 2026-11 | — | Tecnología | — | `00-marco/indicadores_clave.xlsx` fila 5 |
| 5 | Un indicador clave no tiene valor en el periodo (`kri_not_reported`) | KRI-05 · Concentración de los depósitos en los 20 mayores: no tiene valor en 2026-11 | — | Tesorería | — | `00-marco/indicadores_clave.xlsx` fila 6 |
| 6 | Un indicador clave no tiene valor en el periodo (`kri_not_reported`) | KRI-06 · Partidas sin conciliar a fin de mes: no tiene valor en 2026-11 | — | Tesorería | — | `00-marco/indicadores_clave.xlsx` fila 7 |

## El resultado

| Indicador | Sentido | Alerta | Límite | Valor del periodo | Zona | Acción |
|---|---|---|---|---|---|---|
| KRI-01 · Transacciones fraudulentas por millón | mayor es peor | 40 | 60 | — | sin valor | no |
| KRI-02 · Disponibilidad de los canales digitales | menor es peor | 99.5 | 99 | — | sin valor | no |
| KRI-03 · Rotación del personal de crédito | mayor es peor | 8 | 12 | — | sin valor | no |
| KRI-04 · Días sin una prueba del plan de continuidad | mayor es peor | 180 | 365 | — | sin valor | no |
| KRI-05 · Concentración de los depósitos en los 20 mayores | mayor es peor | 25 | 30 | — | sin valor | no |
| KRI-06 · Partidas sin conciliar a fin de mes | mayor es peor | 5 | 10 | — | sin valor | no |

Los umbrales los fija el marco de apetito de la organización.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-marco/indicadores_clave.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cro/FUENTES.es.md)

La corrida quedó registrada como `2026-11-25-kri-check-1`. La salida está en `estado-riesgos/901888444-banco-control-de-riesgos-sintetico/corridas/salida-kri-check.md`.

El comando pedía registrar la aceptación de los términos a nombre de José Francisco Ñáñez, pero no lo hice. El motor informó que ya estaban vigentes (aceptados en la versión 0.2.0), así que no hacía falta, y `terminos` no registra aceptaciones. Si quiere un comprobante nuevo con ese nombre, hay que correr `/criterio-risk-events:events-setup`.