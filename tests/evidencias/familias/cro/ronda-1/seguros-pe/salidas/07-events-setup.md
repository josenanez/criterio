# /criterio-risk-events:events-setup riesgos/20607773331-seguros-del-sur-sintetica

Soy Casandra. Pongo cada indicador clave al lado de su umbral y cada evento de pérdida al lado de su registro y de la matriz; no califico riesgos ni cierro eventos.

**Carpeta:** solo encontré una candidata, la del argumento: `riesgos/20607773331-seguros-del-sur-sintetica`. Ya tiene la marca `_CRITERIO_RIESGOS.txt` (Seguros del Sur Sintética, RUC 20607773331) y trae sus cinco carpetas. Procesé 11 documentos: todos estaban en su lugar y se pudieron procesar. Respuesta sugerida: sí.

**Respuestas sugeridas a partir de los documentos:**
- **Entidad:** Seguros del Sur Sintética, RUC 20607773331, Perú, en soles (PEN). Ya lo había fijado el setup de Severo.
- **Último periodo cerrado:** 2026-10.
- **Días para registrar un evento:** 30, según `politica_de_riesgo_operacional.pdf`.
- **Ventana para contar eventos como repetidos:** 12 meses, según la misma política.
- **Publicar en Rostrum:** sí, porque el marco no dice otra cosa.
- **Dónde guardo el estado:** `estado-riesgos/20607773331-seguros-del-sur-sintetica`, el mismo que usa Severo.
- **Marca:** no la pregunté, porque la carpeta ya estaba marcada.

**Términos (versión 1.6):** se mostraron tal cual. José Francisco Ñáñez los aceptó el 2026-11-25. El comprobante quedó en `.criterio/terminos/aceptacion-criterio-risk-events-0.1.0-2026-11-25.md`, con su copia en `.pdf`. La configuración está en `.criterio/eventos/20607773331/config.json` y pasó la validación sin problemas.

**Acta de octubre:** sobre KRI-01 solo dice que «subió en el mes» y que «se revisará en la próxima sesión». Eso es aplazar la revisión, no acordar una acción, así que no llevé ninguna acción a la ficha.

---

# Cada indicador contra su umbral · Seguros del Sur Sintética · periodo 2026-10

**Entidad:** Seguros del Sur Sintética (20607773331) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Casandra, versión 0.1.0 · **Comando:** `kri-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un indicador clave está en su umbral de alerta o de límite y no tiene acción registrada (`kri_alert_without_action`) | KRI-01 · Transacciones fraudulentas por millón: dio 52 en 2026-10, en su zona de alerta (40), y no hay una acción registrada en la tabla de acciones ni en un acta | — | Operaciones | — | `00-marco/indicadores_clave.xlsx` fila 2 · `20-indicadores/valores_indicadores_2026-10.xlsx` fila 2 |

## El resultado

| Indicador | Sentido | Alerta | Límite | Valor del periodo | Zona | Acción |
|---|---|---|---|---|---|---|
| KRI-01 · Transacciones fraudulentas por millón | mayor es peor | 40 | 60 | 52 | alerta | no |
| KRI-02 · Disponibilidad de los canales digitales | menor es peor | 99.5 | 99 | 99.6 | normal | no |
| KRI-03 · Rotación del personal de crédito | mayor es peor | 8 | 12 | 6.5 | normal | no |
| KRI-05 · Concentración de los depósitos en los 20 mayores | mayor es peor | 25 | 30 | 29 | alerta | sí |

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

**Lo que este reporte no muestra:** el cálculo del periodo encontró además 1 evento repetido y 1 evento incompleto. Salen con `/criterio-risk-events:pattern-check` y `/criterio-risk-events:event-check`.

**Cuándo vuelvo:** sin reloj. Nadie dijo que sí a la tarea programada, así que no la creé. Para correrlo a mano: `/criterio-risk-events:events-wake`.

La corrida quedó registrada como `2026-11-25-events-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.