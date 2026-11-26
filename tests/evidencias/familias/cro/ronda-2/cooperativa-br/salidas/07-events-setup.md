# /criterio-risk-events:events-setup riesgos/12345678000190-cooperativa-vale-sintetica

Soy Casandra. Pongo cada indicador clave al lado de su umbral y cada evento de pérdida al lado de su registro y de la matriz; no califico riesgos ni cierro eventos.

Casandra quedó lista sobre la Cooperativa Vale Sintética. El primer resultado muestra dos indicadores en alerta sin ninguna acción y dos indicadores sin valor en octubre de 2026. No te hice ninguna pregunta: las respuestas salieron de los documentos y de la configuración de Severo, el otro agente, que ya había corrido en esta carpeta.

**Carpeta:** solo encontré una, y ya tenía la marca `_CRITERIO_RIESGOS.txt`: `riesgos/12345678000190-cooperativa-vale-sintetica`. Tiene 00-marco/, 10-exposicion/, 20-indicadores/, 30-eventos/ y 40-actas/. Respuesta sugerida: sí, esa. No pido marcarla porque ya lo está. Procesé 11 documentos, todos en su lugar y ninguno ilegible.

**Respuestas tomadas:**
- **Entidad:** Cooperativa Vale Sintética, CNPJ 12345678000190, Brasil (BRL).
- **Último periodo cerrado:** 2026-10, el de `valores_indicadores_2026-10.xlsx`.
- **Plazo para registrar un evento:** 30 días. La política dice «em até 30 dias corridos desde sua descoberta» (`00-marco/politica_de_risco_operacional.pdf`).
- **Ventana para contar eventos repetidos:** 12 meses. La misma política dice «dentro de 12 meses são tratados como recorrentes».
- **Publicar en Rostrum:** sí, porque el marco no dice otra cosa.
- **Dónde guardo lo que encuentro:** `estado-riesgos/12345678000190-cooperativa-vale-sintetica`.

**Términos (versión 1.6, del 2026-11-16):**
> Criterio entrega a la dirección análisis contrastado contra la evidencia: cada cifra, cada señal y cada vencimiento con la cita del documento del que sale. No sustituye el juicio de quien decide ni la asesoría profesional: la decisión, y su verificación, son de quien la firma. Procesa los documentos que usted le indique y dice lo que muestran; lo que se acordó fuera de ellos no lo conoce. Lo ejecuta un modelo de lenguaje (LLM), que puede equivocarse, y por eso ningún dato llega sin su fuente. Sus documentos se procesan en la infraestructura de la plataforma de IA donde lo ejecuta, no solo en su equipo. Cada versión se prueba antes de publicarse y su evidencia es pública; la garantía y la responsabilidad son las de la licencia Apache 2.0. Se acepta una vez y deja un comprobante en Markdown y PDF con su huella SHA-256; actualizar no pide aceptar de nuevo, salvo que estos términos cambien. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

Quedaron aceptados por José Francisco Ñáñez el 2026-11-25. El comprobante está en `.criterio/terminos/aceptacion-criterio-risk-events-0.2.0-2026-11-25.md` y en el `.pdf` del mismo nombre. La configuración quedó en `.criterio/eventos/12345678000190/config.json`.

**Ficha de 2026-10:** procesé el acta del comité y llevé a la ficha una sola acción, sobre KRI-06: «O comitê aprova a conciliação diária automática das contas transitórias». KRI-01 aparece en el acta, pero solo con «Será revisado na próxima sessão», y eso no es una acción acordada.

---

# Cada indicador contra su umbral · Cooperativa Vale Sintética · periodo 2026-10

**Entidad:** Cooperativa Vale Sintética (12345678000190) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Casandra, versión 0.2.0 · **Comando:** `kri-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un indicador clave está en su umbral de alerta o de límite y no tiene acción registrada (`kri_alert_without_action`) | KRI-01 · Transações fraudulentas por milhão: dio 52 en 2026-10, en su zona de alerta (40), y no hay una acción registrada en la tabla de acciones ni en un acta | — | Operações | — | `00-marco/indicadores_chave.xlsx` fila 2 · `20-indicadores/valores_indicadores_2026-10.xlsx` fila 2 |
| 2 | Un indicador clave está en su umbral de alerta o de límite y no tiene acción registrada (`kri_alert_without_action`) | KRI-12 · Reclamações por 10.000 clientes: dio 19 en 2026-10, en su zona de alerta (15), y no hay una acción registrada en la tabla de acciones ni en un acta | — | Marketing | — | `00-marco/indicadores_chave.xlsx` fila 7 · `20-indicadores/valores_indicadores_2026-10.xlsx` fila 6 |
| 3 | Un indicador clave no tiene valor en el periodo (`kri_not_reported`) | KRI-03 · Rotatividade da equipe de crédito: no tiene valor en 2026-10 | — | Diretoria de crédito | — | `00-marco/indicadores_chave.xlsx` fila 4 |
| 4 | Un indicador clave no tiene valor en el periodo (`kri_not_reported`) | KRI-22 · Cancelamentos de produtos no primeiro mês: no tiene valor en 2026-10 | — | Marketing | — | `00-marco/indicadores_chave.xlsx` fila 8 |

## El resultado

| Indicador | Sentido | Alerta | Límite | Valor del periodo | Zona | Acción |
|---|---|---|---|---|---|---|
| KRI-01 · Transações fraudulentas por milhão | mayor es peor | 40 | 60 | 52 | alerta | no |
| KRI-02 · Disponibilidade dos canais digitais | menor es peor | 99.5 | 99 | 99.6 | normal | no |
| KRI-03 · Rotatividade da equipe de crédito | mayor es peor | 8 | 12 | — | sin valor | no |
| KRI-05 · Concentração dos depósitos nos 20 maiores | mayor es peor | 25 | 30 | 29 | alerta | sí |
| KRI-06 · Itens sem conciliar no fim do mês | mayor es peor | 5 | 10 | 7 | alerta | sí |
| KRI-12 · Reclamações por 10.000 clientes | mayor es peor | 15 | 25 | 19 | alerta | no |
| KRI-22 · Cancelamentos de produtos no primeiro mês | mayor es peor | 10 | 15 | — | sin valor | no |

Los umbrales los fija el marco de apetito de la organización.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-marco/indicadores_chave.xlsx`
- `20-indicadores/valores_indicadores_2026-10.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cro/FUENTES.es.md)

---

**Revisión diaria automática:** te propongo una tarea programada los días hábiles a las 7:00 para que Casandra revise sola lo que toca. Solo procesaría y escribiría en el estado de Criterio, sin enviar nada. No la creé porque necesita un sí explícito y en esta prueba no lo hubo. Para correrlo a mano: `/criterio-risk-events:events-wake`.

**Cuándo vuelvo:** no hay tarea programada, así que no vuelvo sola.

La corrida quedó registrada como `2026-11-25-events-setup-1`. El motor también encontró señales sobre los eventos de pérdida: dos registrados tarde, dos incompletos, dos repetidos y dos que no están en la matriz. Este reporte cubre solo los indicadores; esas ocho señales las detallan `/criterio-risk-events:event-check` y `/criterio-risk-events:pattern-check`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.