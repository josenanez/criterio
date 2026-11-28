# /criterio-risk-events:events-setup riesgos/bms0907153r2-banco-mesoamericano-sintetico

Soy Casandra. Pongo cada indicador clave al lado de su umbral y cada evento de pérdida al lado de su registro y de la matriz; no califico riesgos ni cierro eventos.

Casandra quedó lista sobre el Banco Mesoamericano Sintético. En el periodo 2026-10 hay dos indicadores en alerta sin ninguna acción registrada (KRI-01 y KRI-12) y dos que no reportaron valor (KRI-03 y KRI-22).

**Carpeta:** `riesgos/bms0907153r2-banco-mesoamericano-sintetico`. Era la única candidata y ya estaba marcada con `_CRITERIO_RIESGOS.txt`, así que la confirmé.

**Respuestas que tomé** de los documentos y de la configuración que ya había dejado Severo:
- **Entidad:** Banco Mesoamericano Sintético · BMS0907153R2, México (MXN).
- **Último periodo cerrado:** 2026-10, el de `valores_indicadores_2026-10.xlsx`.
- **Plazo de registro de un evento:** 30 días calendario.
- **Ventana de eventos repetidos:** 12 meses. Este plazo y el anterior salen de `politica_de_riesgo_operacional.pdf`.
- **Publicar en Rostrum:** sí, porque el marco no dice otra cosa.
- **Dónde guardo lo que encuentro:** `estado-riesgos/bms0907153r2-banco-mesoamericano-sintetico`.
- **Marca:** no la volví a preguntar, porque la carpeta ya la tenía.

**Términos 1.6:** «Criterio entrega a la dirección análisis contrastado contra la evidencia: cada cifra, cada señal y cada vencimiento con la cita del documento del que sale. No sustituye el juicio de quien decide ni la asesoría profesional: la decisión, y su verificación, son de quien la firma. Procesa los documentos que usted le indique y dice lo que muestran; lo que se acordó fuera de ellos no lo conoce. Lo ejecuta un modelo de lenguaje (LLM), que puede equivocarse, y por eso ningún dato llega sin su fuente. Sus documentos se procesan en la infraestructura de la plataforma de IA donde lo ejecuta, no solo en su equipo. Cada versión se prueba antes de publicarse y su evidencia es pública; la garantía y la responsabilidad son las de la licencia Apache 2.0. Se acepta una vez y deja un comprobante en Markdown y PDF con su huella SHA-256; actualizar no pide aceptar de nuevo, salvo que estos términos cambien. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal»

Los aceptó José Francisco Ñáñez el 2026-11-25. El comprobante quedó en `.criterio/terminos/aceptacion-criterio-risk-events-1.0.0-2026-11-25.md` y `.pdf`.

**Configuración:** `.criterio/eventos/BMS0907153R2/config.json`.

**Ficha 2026-10:** procesé el acta del comité de riesgos y llevé a la ficha una sola acción: para KRI-06, el comité aprueba la conciliación diaria automática de las cuentas puente. Sobre KRI-01 el acta solo dice que «se revisará en la próxima sesión», y eso no es una acción acordada; por eso sale como alerta sin acción.

---

# Cada indicador contra su umbral · Banco Mesoamericano Sintético · periodo 2026-10

**Entidad:** Banco Mesoamericano Sintético (BMS0907153R2) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Casandra, versión 1.0.0 · **Comando:** `kri-check`

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

**El reloj:** no creé la tarea programada, porque esta prueba no tiene a nadie que dé el sí explícito que hace falta. Se corre a mano con `/criterio-risk-events:events-wake`.

**Cuándo vuelvo:** sin reloj.

**Registro de la corrida:** queda como `2026-11-25-events-setup-1`, con la salida en `estado-riesgos/bms0907153r2-banco-mesoamericano-sintetico/corridas/salida-events-setup.md`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.