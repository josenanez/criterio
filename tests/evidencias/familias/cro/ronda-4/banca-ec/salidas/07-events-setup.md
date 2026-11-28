# /criterio-risk-events:events-setup riesgos/1790123456001-banco-del-pichincha-sur-sintetico

Casandra quedó lista para Banco del Pichincha Sur Sintético (1790123456001), con el periodo 2026-10. La primera revisión encontró dos indicadores en alerta sin ninguna acción registrada (KRI-01 y KRI-12) y dos sin valor en el periodo (KRI-03 y KRI-22).

- **Configuración:** quedó en `.criterio/eventos/1790123456001/config.json`. La entidad y el periodo coinciden con los que ya usa Severo. Los dos plazos salen de la política de riesgo operacional (`00-marco/politica_de_riesgo_operacional.pdf`): 30 días para registrar un evento y 12 meses para contar dos eventos como repetidos.
- **Términos:** quedan aceptados a nombre de José Francisco Ñáñez con fecha 2026-11-25. El comprobante está en `.criterio/terminos/aceptacion-criterio-risk-events-1.1.0-2026-11-25.md` y `.pdf`.
- **Marca:** la carpeta ya tenía `_CRITERIO_RIESGOS.txt`, así que no la volví a marcar.
- **Acta de octubre:** registra una sola acción sobre un indicador, la conciliación diaria automática de las cuentas puente (KRI-06). El acta solo dice que KRI-01 «subió… se revisará», y eso no cuenta como acción, por eso sigue en la lista.

# Cada indicador contra su umbral · Banco del Pichincha Sur Sintético · periodo 2026-10

**Entidad:** Banco del Pichincha Sur Sintético (1790123456001) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Casandra, versión 1.1.0 · **Comando:** `kri-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un indicador clave está en su umbral de alerta o de límite y no tiene acción registrada (`kri_alert_without_action`) | KRI-01 · Transacciones fraudulentas por millón: dio 52 en 2026-10, en su zona de alerta (40), y no hay una acción registrada en la tabla de acciones ni en un acta | — | Operaciones | — | `00-marco/indicadores_clave.xlsx` fila 2 · `20-indicadores/valores_indicadores_2026-10.xlsx` fila 2 |
| 2 | Un indicador clave está en su umbral de alerta o de límite y no tiene acción registrada (`kri_alert_without_action`) | KRI-12 · Reclamos por cada 10.000 clientes: dio 19 en 2026-10, en su zona de alerta (15), y no hay una acción registrada en la tabla de acciones ni en un acta | — | Mercadeo | — | `00-marco/indicadores_clave.xlsx` fila 7 · `20-indicadores/valores_indicadores_2026-10.xlsx` fila 6 |
| 3 | Un indicador clave no tiene valor en el periodo (`kri_not_reported`) | KRI-03 · Rotación del personal de crédito: no tiene valor en 2026-10 | — | Vicepresidencia de crédito | — | `00-marco/indicadores_clave.xlsx` fila 4 |
| 4 | Un indicador clave no tiene valor en el periodo (`kri_not_reported`) | KRI-22 · Cancelaciones de productos en el primer mes: no tiene valor en 2026-10 | — | Mercadeo | — | `00-marco/indicadores_clave.xlsx` fila 8 |

## El resultado

| Indicador | Sentido | Alerta | Límite | Valor del periodo | Zona | Acción |
|---|---|---|---|---|---|---|
| KRI-01 · Transacciones fraudulentas por millón | mayor es peor | 40 | 60 | 52 | alerta | no |
| KRI-02 · Disponibilidad de los canales digitales | menor es peor | 99.5 | 99 | 99.6 | normal | no |
| KRI-03 · Rotación del personal de crédito | mayor es peor | 8 | 12 | — | sin valor | no |
| KRI-05 · Concentración de los depósitos en los 20 mayores | mayor es peor | 25 | 30 | 29 | alerta | sí |
| KRI-06 · Partidas sin conciliar a fin de mes | mayor es peor | 5 | 10 | 7 | alerta | sí |
| KRI-12 · Reclamos por cada 10.000 clientes | mayor es peor | 15 | 25 | 19 | alerta | no |
| KRI-22 · Cancelaciones de productos en el primer mes | mayor es peor | 10 | 15 | — | sin valor | no |

Los umbrales los fija el marco de apetito de la organización.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-marco/indicadores_clave.xlsx`
- `20-indicadores/valores_indicadores_2026-10.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cro/FUENTES.es.md)

---

El motor también encontró 8 señales sobre los eventos de pérdida: eventos repetidos, registrados fuera de plazo, incompletos o que no corresponden a ningún riesgo de la matriz. Este reporte no las incluye; salen con `/criterio-risk-events:event-check` y `/criterio-risk-events:pattern-check`.

**Revisión diaria:** te proponía una tarea los días hábiles a las 7:00, pero la tarea programada necesita un sí explícito y en esta sesión nadie lo dio, así que no la creé. A mano se corre con `/criterio-risk-events:events-wake`.

**Cuándo vuelvo:** sin reloj.

La corrida quedó registrada como `2026-11-25-events-setup-1`, y lo que mostré está en `estado-riesgos/1790123456001-banco-del-pichincha-sur-sintetico/corridas/salida-events-setup.md`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.