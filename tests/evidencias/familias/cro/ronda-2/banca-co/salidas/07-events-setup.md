# /criterio-risk-events:events-setup riesgos/901777333-banco-andino-sintetico

Soy Casandra. Pongo cada indicador clave al lado de su umbral y cada evento de pérdida al lado de su registro y de la matriz; no califico riesgos ni cierro eventos.

Casandra quedó configurada para Banco Andino Sintético. No hizo falta preguntar nada: todas las respuestas salieron de los documentos o del setup de Severo.

**Configuración**
- **Carpeta:** `riesgos/901777333-banco-andino-sintetico`. Es la única candidata y ya estaba marcada con `_CRITERIO_RIESGOS.txt`, así que no la volví a marcar. Procesé 11 documentos; ninguno quedó fuera de lugar ni ilegible.
- **Entidad:** Banco Andino Sintético, NIT 901777333, Colombia (COP).
- **Último periodo cerrado:** 2026-10, el de los valores de los indicadores.
- **Plazos de la política de riesgo operacional:** 30 días calendario para registrar un evento desde que se descubre, y 12 meses de ventana para contar dos eventos como repetidos.
- **Publicar en Rostrum:** sí, porque el marco no dice otra cosa.
- **Dónde guardo lo que encuentro:** `estado-riesgos/901777333-banco-andino-sintetico`, fuera de los documentos.
- **Términos 1.6:** se mostraron y José Francisco Ñáñez los aceptó el 2026-11-25. El comprobante quedó en `.criterio/terminos/aceptacion-criterio-risk-events-0.2.0-2026-11-25.md` y en el `.pdf` del mismo nombre.
- **Archivo de configuración:** `.criterio/eventos/901777333/config.json`.

**La primera ficha.** Procesé el acta del comité de riesgos de octubre y registré una acción sobre KRI-06: la conciliación diaria automática de las cuentas puente. Sobre KRI-01, el acta solo dice que «se revisará en la próxima sesión». Eso no es una acción acordada, así que no la registré.

# Cada indicador contra su umbral · Banco Andino Sintético · periodo 2026-10

**Entidad:** Banco Andino Sintético (901777333) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Casandra, versión 0.2.0 · **Comando:** `kri-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un indicador clave está en su umbral de alerta o de límite y no tiene acción registrada (`kri_alert_without_action`) | KRI-01 · Transacciones fraudulentas por millón: dio 52 en 2026-10, en su zona de alerta (40), y no hay una acción registrada en la tabla de acciones ni en un acta | — | Operaciones | — | `00-marco/indicadores_clave.xlsx` fila 2 · `20-indicadores/valores_indicadores_2026-10.xlsx` fila 2 |
| 2 | Un indicador clave está en su umbral de alerta o de límite y no tiene acción registrada (`kri_alert_without_action`) | KRI-12 · Reclamos por cada 10.000 clientes: dio 19 en 2026-10, en su zona de alerta (15), y no hay una acción registrada en la tabla de acciones ni en un acta | — | Mercadeo | — | `00-marco/indicadores_clave.xlsx` fila 7 · `20-indicadores/valores_indicadores_2026-10.xlsx` fila 6 |
| 3 | Un indicador clave está en su umbral de alerta o de límite y no tiene acción registrada (`kri_alert_without_action`) | KRI-13 · Incidentes de seguridad por mes: dio 4 en 2026-10, en su zona de alerta (3), y no hay una acción registrada en la tabla de acciones ni en un acta | — | Operaciones | — | `00-marco/indicadores_clave.xlsx` fila 8 · `20-indicadores/valores_indicadores_2026-10.xlsx` fila 7 |
| 4 | Un indicador clave no tiene valor en el periodo (`kri_not_reported`) | KRI-03 · Rotación del personal de crédito: no tiene valor en 2026-10 | — | Vicepresidencia de crédito | — | `00-marco/indicadores_clave.xlsx` fila 4 |
| 5 | Un indicador clave no tiene valor en el periodo (`kri_not_reported`) | KRI-22 · Cancelaciones de productos en el primer mes: no tiene valor en 2026-10 | — | Mercadeo | — | `00-marco/indicadores_clave.xlsx` fila 9 |
| 6 | Un indicador clave no tiene valor en el periodo (`kri_not_reported`) | KRI-23 · Operaciones con errores de digitación: no tiene valor en 2026-10 | — | Vicepresidencia de crédito | — | `00-marco/indicadores_clave.xlsx` fila 10 |

## El resultado

| Indicador | Sentido | Alerta | Límite | Valor del periodo | Zona | Acción |
|---|---|---|---|---|---|---|
| KRI-01 · Transacciones fraudulentas por millón | mayor es peor | 40 | 60 | 52 | alerta | no |
| KRI-02 · Disponibilidad de los canales digitales | menor es peor | 99.5 | 99 | 99.6 | normal | no |
| KRI-03 · Rotación del personal de crédito | mayor es peor | 8 | 12 | — | sin valor | no |
| KRI-05 · Concentración de los depósitos en los 20 mayores | mayor es peor | 25 | 30 | 29 | alerta | sí |
| KRI-06 · Partidas sin conciliar a fin de mes | mayor es peor | 5 | 10 | 7 | alerta | sí |
| KRI-12 · Reclamos por cada 10.000 clientes | mayor es peor | 15 | 25 | 19 | alerta | no |
| KRI-13 · Incidentes de seguridad por mes | mayor es peor | 3 | 6 | 4 | alerta | no |
| KRI-22 · Cancelaciones de productos en el primer mes | mayor es peor | 10 | 15 | — | sin valor | no |
| KRI-23 · Operaciones con errores de digitación | mayor es peor | 20 | 40 | — | sin valor | no |

Los umbrales los fija el marco de apetito de la organización.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-marco/indicadores_clave.xlsx`
- `20-indicadores/valores_indicadores_2026-10.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cro/FUENTES.es.md)

**Cuándo vuelvo:** sin reloj. En esta prueba nadie confirmó una tarea programada, así que no la creé. Para correrlo a mano: `/criterio-risk-events:events-wake`.

El motor también encontró señales sobre la base de eventos: eventos repetidos, registrados tarde, incompletos y sin riesgo en la matriz. No forman parte de este reporte; se ven con `/criterio-risk-events:event-check` y `/criterio-risk-events:pattern-check`.

La corrida quedó registrada como `2026-11-25-events-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.