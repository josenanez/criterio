# /criterio-risk-events:events-setup riesgos/901777333-banco-andino-sintetico

Soy Casandra. Pongo cada indicador clave al lado de su umbral y cada evento de pérdida al lado de su registro y de la matriz. No califico riesgos ni cierro eventos.

**Carpeta:** solo encontré una, `riesgos/901777333-banco-andino-sintetico`, así que la tomé. Ya está marcada con `_CRITERIO_RIESGOS.txt` (Banco Andino Sintético, 901777333) y tiene 00-marco/, 10-exposicion/, 20-indicadores/, 30-eventos/ y 40-actas/. Procesé sus 11 documentos: todos estaban en su carpeta y se pudieron leer.

**Respuestas tomadas** (sesión de prueba, una línea por cada una):
- **Entidad, periodo y estado:** los fijó el setup de Severo. Banco Andino Sintético, 901777333, CO, COP. Último periodo cerrado 2026-10. El estado se guarda en `estado-riesgos/901777333-banco-andino-sintetico`.
- **Plazos:** salen de `00-marco/politica_de_riesgo_operacional.pdf`. Un evento se registra dentro de 30 días calendario desde que se descubre. Dos eventos del mismo tipo en el mismo proceso dentro de 12 meses cuentan como repetidos.
- **Rostrum:** sí, porque el marco no dice otra cosa.
- **Marca:** la carpeta ya estaba marcada, así que no la volví a marcar.

**Términos (versión 1.6, 2026-11-16):**
> Criterio entrega a la dirección análisis contrastado contra la evidencia: cada cifra, cada señal y cada vencimiento con la cita del documento del que sale. No sustituye el juicio de quien decide ni la asesoría profesional: la decisión, y su verificación, son de quien la firma. Procesa los documentos que usted le indique y dice lo que muestran; lo que se acordó fuera de ellos no lo conoce. Lo ejecuta un modelo de lenguaje (LLM), que puede equivocarse, y por eso ningún dato llega sin su fuente. Sus documentos se procesan en la infraestructura de la plataforma de IA donde lo ejecuta, no solo en su equipo. Cada versión se prueba antes de publicarse y su evidencia es pública; la garantía y la responsabilidad son las de la licencia Apache 2.0. Se acepta una vez y deja un comprobante en Markdown y PDF con su huella SHA-256; actualizar no pide aceptar de nuevo, salvo que estos términos cambien. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

Los aceptó José Francisco Ñáñez el 2026-11-25. El comprobante quedó en `.criterio/terminos/aceptacion-criterio-risk-events-0.1.0-2026-11-25.md` y `.pdf`. La configuración quedó en `.criterio/eventos/901777333/config.json` y se validó sin problemas.

**Acta:** según el acta de octubre, KRI-01 subió y «se revisará en la próxima sesión». Eso es una mención, no una acción acordada, así que en la ficha el acta quedó como procesada y sin acciones.

---

# Cada indicador contra su umbral · Banco Andino Sintético · periodo 2026-10

**Entidad:** Banco Andino Sintético (901777333) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Casandra, versión 0.1.0 · **Comando:** `kri-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un indicador clave está en su umbral de alerta o de límite y no tiene acción registrada (`kri_alert_without_action`) | KRI-01 · Transacciones fraudulentas por millón: dio 52 en 2026-10, en su zona de alerta (40), y no hay una acción registrada en la tabla de acciones ni en un acta | — | Operaciones | — | `00-marco/indicadores_clave.xlsx` fila 2 · `20-indicadores/valores_indicadores_2026-10.xlsx` fila 2 |
| 2 | Un indicador clave no tiene valor en el periodo (`kri_not_reported`) | KRI-03 · Rotación del personal de crédito: no tiene valor en 2026-10 | — | Vicepresidencia de crédito | — | `00-marco/indicadores_clave.xlsx` fila 4 |

## El resultado

| Indicador | Sentido | Alerta | Límite | Valor del periodo | Zona | Acción |
|---|---|---|---|---|---|---|
| KRI-01 · Transacciones fraudulentas por millón | mayor es peor | 40 | 60 | 52 | alerta | no |
| KRI-02 · Disponibilidad de los canales digitales | menor es peor | 99.5 | 99 | 99.6 | normal | no |
| KRI-03 · Rotación del personal de crédito | mayor es peor | 8 | 12 | — | sin valor | no |
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

**Cuándo vuelvo:** sin reloj, porque en esta sesión de prueba nadie dio un sí explícito. Para correrlo a mano: `/criterio-risk-events:events-wake`.

El motor también encontró señales sobre la base de eventos de 2026-10: uno incompleto, uno registrado tarde, uno repetido y uno que no está en la matriz. Las detallan `/criterio-risk-events:event-check` y `/criterio-risk-events:pattern-check`.

La corrida quedó registrada como `2026-11-25-events-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.