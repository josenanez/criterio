# /criterio-revenue:revenue-setup comercial/MBA120315KT4-manufacturas-del-bajio

Soy Valeria. Pongo cada venta al lado de su política, su contrato y su factura; no apruebo descuentos ni liquido comisiones.

**La carpeta:** usé la del argumento, `comercial/MBA120315KT4-manufacturas-del-bajio`. Procesé 33 documentos: 6 en `00-referencia/`, 3 en `10-crm/`, 1 en `20-comite/`, 17 en `30-evidencia/`, 5 en `40-cotizaciones/` y 1 en `50-comisiones/`. La carpeta sigue la estructura esperada y no hay nada fuera de lugar ni ilegible.

**Las exportaciones del CRM:** las tres son de Salesforce, no les falta ninguna columna y cada una tiene 19 filas:
- `oportunidades-2026-10-01.csv`, con fecha 2026-10-01
- `oportunidades-2026-10-16.csv`, con fecha 2026-10-16
- `oportunidades-2026-11-03.csv`, con fecha 2026-11-03

**Las respuestas.** Las tomé de los documentos y de lo que ya había fijado Augusto:
1. **Entidad y país:** Manufacturas del Bajío, RFC MBA120315KT4, México, en pesos mexicanos (MXN).
2. **Periodo:** 2026-10.
3. **Referencias:** uso la matriz de descuentos, el plan de comisiones y la tabla de cuentas de `00-referencia/`. Las 12 cuentas de `cuentas.csv` traen la identificación del cliente.
4. **CRM:** Salesforce, con las fechas en orden mes/día/año. La cuenta sale de la columna `Account ID`.
5. **Fichas de los contratos de Fidel:** `estado-legal/MBA120315KT4-manufacturas-del-bajio/contratos`. Encontré ahí 8 contratos.
6. **Fichas de la facturación de Clara:** `estado-finanzas/MBA120315KT4-manufacturas-del-bajio`. Encontré ahí los cierres de 2026-09 y 2026-10.
7. **Plazo para facturar un contrato firmado:** 30 días.
8. **Comisiones en Rostrum:** no se publican, que es la opción por omisión.
9. **Dónde guardo lo que encuentro:** `estado-comercial/MBA120315KT4-manufacturas-del-bajio`.
10. **La marca `_CRITERIO_COMERCIAL.txt`:** no la dejé, porque nadie la autorizó en esta sesión.

**Los términos:**

> Criterio entrega a la dirección análisis contrastado contra la evidencia: cada cifra, cada señal y cada vencimiento con la cita del documento del que sale. No sustituye el juicio de quien decide ni la asesoría profesional: la decisión, y su verificación, son de quien la firma. Procesa los documentos que usted le indique y dice lo que muestran; lo que se acordó fuera de ellos no lo conoce. Lo ejecuta un modelo de lenguaje (LLM), que puede equivocarse, y por eso ningún dato llega sin su fuente. Sus documentos se procesan en la infraestructura de la plataforma de IA donde lo ejecuta, no solo en su equipo. Cada versión se prueba antes de publicarse y su evidencia es pública; la garantía y la responsabilidad son las de la licencia Apache 2.0. Se acepta una vez y deja un comprobante en Markdown y PDF con su huella SHA-256; actualizar no pide aceptar de nuevo, salvo que estos términos cambien. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

José Francisco Ñáñez los aceptó el 2026-11-05 (términos 1.5, criterio-revenue 1.2.3). Los comprobantes quedaron en `.criterio/terminos/aceptacion-criterio-revenue-1.2.3-2026-11-05.md` y en el `.pdf` del mismo nombre.

**La configuración** quedó en `.criterio/ingresos/MBA120315KT4-manufacturas-del-bajio/config.json` y el motor la validó sin problemas.

El primer cruce encontró 4 contratos firmados sin factura en las fichas de Clara y 2 oportunidades ganadas sin contrato en las de Fidel.

# De lo ganado a la factura · Manufacturas del Bajío · periodo 2026-10

**Entidad:** Manufacturas del Bajío (MBA120315KT4) · **Fecha de corte:** 2026-10-31 · **Procesado:** 2026-11-05 · **Agente:** Valeria, versión 1.2.3 · **Comando:** `won-to-invoice`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un contrato firmado no tiene su factura en la ficha de Clara dentro del plazo de facturación (`signed_without_invoice`) | CTR-1405: firmado con el cliente CMA150606F55 el 2026-09-10 y las fichas de Clara no tienen una factura emitida a ese cliente hasta el 2026-10-10 | 960,000.00 | — | 26 | `contratos/CTR-1405.json` |
| 2 | Un contrato firmado no tiene su factura en la ficha de Clara dentro del plazo de facturación (`signed_without_invoice`) | CTR-1432: firmado con el cliente CMA210312L114 el 2026-09-10 y las fichas de Clara no tienen una factura emitida a ese cliente hasta el 2026-10-10 | 600,000.00 | — | 26 | `contratos/CTR-1432.json` |
| 3 | Una oportunidad ganada no tiene su contrato firmado en la ficha de Fidel (`won_without_contract`) | OPP-1431 · Venta directa 31: ganada el 2026-10-07 por 480,000.00 y las fichas de Fidel no tienen un contrato firmado con el cliente CMA180909I81 | 480,000.00 | — | 29 | `10-crm/oportunidades-2026-11-03.csv` fila 20 |
| 4 | Un contrato firmado no tiene su factura en la ficha de Clara dentro del plazo de facturación (`signed_without_invoice`) | CTR-1431: firmado con el cliente CMA200211K103 el 2026-09-09 y las fichas de Clara no tienen una factura emitida a ese cliente hasta el 2026-10-09 | 480,000.00 | — | 27 | `contratos/CTR-1431.json` |
| 5 | Una oportunidad ganada no tiene su contrato firmado en la ficha de Fidel (`won_without_contract`) | OPP-1430 · Venta directa 30: ganada el 2026-10-06 por 360,000.00 y las fichas de Fidel no tienen un contrato firmado con el cliente CMA170808H70 | 360,000.00 | — | 30 | `10-crm/oportunidades-2026-11-03.csv` fila 19 |
| 6 | Un contrato firmado no tiene su factura en la ficha de Clara dentro del plazo de facturación (`signed_without_invoice`) | CTR-1430: firmado con el cliente CMA190110J92 el 2026-09-08 y las fichas de Clara no tienen una factura emitida a ese cliente hasta el 2026-10-08 | 360,000.00 | — | 28 | `contratos/CTR-1430.json` |

## El resultado

| Oportunidad ganada | Cuenta | Monto | Ganada | Contrato (Fidel) | Factura (Clara) |
|---|---|---|---|---|---|
| OPP-1401 · Renovación de licencias | 001A0000140000AaQZ | 1,440,000.00 | 2026-10-10 | CTR-1401 | FE-1401 |
| OPP-1402 · Proyecto de expansión | 001A0000140001AaQZ | 2,160,000.00 | 2026-10-22 | CTR-1402 | FE-1402 |
| OPP-1430 · Venta directa 30 | 001A0000140007AaQZ | 360,000.00 | 2026-10-06 | — | — |
| OPP-1431 · Venta directa 31 | 001A0000140008AaQZ | 480,000.00 | 2026-10-07 | — | — |

| Contrato | Cliente | Firmado | Plazo de facturación | Factura | Estado |
|---|---|---|---|---|---|
| CTR-1401 | CMA100101A00 | 2026-10-13 | 2026-11-12 | FE-1401 | facturado |
| CTR-1402 | CMA110202B11 | 2026-10-24 | 2026-11-23 | FE-1402 | facturado |
| CTR-1403 | CMA140505E44 | 2026-10-20 | 2026-11-19 | — | en plazo |
| CTR-1405 | CMA150606F55 | 2026-09-10 | 2026-10-10 | — | vencido |
| CTR-1430 | CMA190110J92 | 2026-09-08 | 2026-10-08 | — | vencido |
| CTR-1431 | CMA200211K103 | 2026-09-09 | 2026-10-09 | — | vencido |
| CTR-1432 | CMA210312L114 | 2026-09-10 | 2026-10-10 | — | vencido |

Plazo de facturación configurado: 30 días. Los contratos y las facturas son los de las fichas de Fidel y de Clara: no se vuelven a procesar.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `10-crm/oportunidades-2026-11-03.csv`
- `contratos/CTR-1405.json`
- `contratos/CTR-1430.json`
- `contratos/CTR-1431.json`
- `contratos/CTR-1432.json`

**Cuándo vuelvo:** sin reloj, porque nadie confirmó la tarea programada. Para correrlo a mano: `/criterio-revenue:revenue-wake`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.