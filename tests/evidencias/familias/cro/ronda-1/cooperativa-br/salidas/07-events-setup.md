# /criterio-risk-events:events-setup riesgos/12345678000190-cooperativa-vale-sintetica

Casandra quedó lista sobre la Cooperativa Vale Sintética (12345678000190) y la primera revisión de indicadores, para octubre de 2026, salió con una señal: **KRI-03 no tiene valor en el periodo**.

- **Configuración:** quedó en `.criterio/eventos/12345678000190/config.json`. Tomé lo que ya había fijado el setup de Severo y los dos plazos de la política de riesgo operacional: 30 días corridos para registrar un evento y 12 meses de ventana para contarlo como repetido.
- **Términos:** quedó registrada la aceptación de José Francisco Ñáñez (versión 1.6). El comprobante está en `.criterio/terminos/aceptacion-criterio-risk-events-0.1.0-2026-11-25.md` y `.pdf`.
- **Acta de octubre:** procesé el acta del comité. Trae una sola acción sobre un indicador, y la llevé a la ficha del periodo: el bloqueo preventivo de los BIN comprometidos, sobre KRI-01.
- **Las otras dos señales:** el motor también encontró un evento registrado fuera de plazo y uno que no corresponde a ningún riesgo de la matriz. No salen en este reporte, que solo cubre indicadores; las muestran `/criterio-risk-events:event-check` y `/criterio-risk-events:pattern-check`.

El reporte, tal como lo escribió el motor:

---

# Cada indicador contra su umbral · Cooperativa Vale Sintética · periodo 2026-10

**Entidad:** Cooperativa Vale Sintética (12345678000190) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Casandra, versión 0.1.0 · **Comando:** `kri-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un indicador clave no tiene valor en el periodo (`kri_not_reported`) | KRI-03 · Rotatividade da equipe de crédito: no tiene valor en 2026-10 | — | Diretoria de crédito | — | `00-marco/indicadores_chave.xlsx` fila 4 |

## El resultado

| Indicador | Sentido | Alerta | Límite | Valor del periodo | Zona | Acción |
|---|---|---|---|---|---|---|
| KRI-01 · Transações fraudulentas por milhão | mayor es peor | 40 | 60 | 52 | alerta | sí |
| KRI-02 · Disponibilidade dos canais digitais | menor es peor | 99.5 | 99 | 99.6 | normal | no |
| KRI-03 · Rotatividade da equipe de crédito | mayor es peor | 8 | 12 | — | sin valor | no |
| KRI-04 · Dias sem teste do plano de continuidade | mayor es peor | 180 | 365 | 64 | normal | no |
| KRI-05 · Concentração dos depósitos nos 20 maiores | mayor es peor | 25 | 30 | 29 | alerta | sí |

Los umbrales los fija el marco de apetito de la organización.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-marco/indicadores_chave.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cro/FUENTES.es.md)

---

**Cuándo vuelvo:** sin reloj. Nadie aceptó de forma explícita la tarea programada, así que no la creé. Para revisar a mano: `/criterio-risk-events:events-wake`.

La corrida quedó registrada como `2026-11-25-events-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.