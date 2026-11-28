# /criterio-revenue:revenue-setup comercial/155622222-2-2017-almacenes-del-istmo

Valeria quedó instalada sobre Almacenes del Istmo (RUC 155622222-2-2017), y el primer cruce de lo ganado a la factura de 2026-10 está abajo. Encontró tres oportunidades ganadas sin contrato firmado y dos contratos firmados sin factura con el plazo vencido. Los descuentos de las cinco cotizaciones ya están en la ficha. Su cruce contra la matriz sale con `/criterio-revenue:discount-check`.

Cómo quedó la instalación:
- **Configuración:** en `.criterio/ingresos/155622222-2-2017-almacenes-del-istmo/config.json`. Tomé la entidad, el país, la moneda, el periodo y el CRM del setup de Augusto.
- **Exportaciones:** las tres de `10-crm/` son de HubSpot, sin columnas faltantes. Todas las cuentas de `00-referencia/` tienen su identificación.
- **Respuestas:** tomé la sugerida a partir de los documentos en cada pregunta. Un contrato firmado se factura en 30 días, las comisiones no se publican en Rostrum y el estado se guarda en `estado-comercial/155622222-2-2017-almacenes-del-istmo`. La carpeta ya estaba marcada, así que no volví a pedir la marca.
- **Términos:** quedó registrada la aceptación de la versión 1.6 a nombre de José Francisco Ñáñez, con fecha 2026-11-05. El comprobante está en `.criterio/terminos/aceptacion-criterio-revenue-1.4.2-2026-11-05.md` y `.pdf`.
- **Cotizaciones:** procesé las cinco de `40-cotizaciones/` y las llevé a `ingresos/2026-10/ficha.json`, con su oportunidad, su descuento, quién lo aprobó y la cita de cada una.

---

# De lo ganado a la factura · Almacenes del Istmo · periodo 2026-10

**Entidad:** Almacenes del Istmo (155622222-2-2017) · **Fecha de corte:** 2026-10-31 · **Procesado:** 2026-11-05 · **Agente:** Valeria, versión 1.4.2 · **Comando:** `won-to-invoice`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una oportunidad ganada no tiene su contrato firmado en la ficha de Fidel (`won_without_contract`) | OPP-2608 · Venta de equipos: ganada el 2026-10-05 por 75,000.00 y las fichas de Fidel no tienen un contrato firmado con el cliente 830026002 | 75,000.00 | — | 31 | `10-crm/hubspot-crm-exports-deals-2026-11-03.csv` fila 9 |
| 2 | Una oportunidad ganada no tiene su contrato firmado en la ficha de Fidel (`won_without_contract`) | OPP-2630 · Venta directa 30: ganada el 2026-10-07 por 60,000.00 y las fichas de Fidel no tienen un contrato firmado con el cliente 830026008 | 60,000.00 | — | 29 | `10-crm/hubspot-crm-exports-deals-2026-11-03.csv` fila 20 |
| 3 | Un contrato firmado no tiene su factura en la ficha de Clara dentro del plazo de facturación (`signed_without_invoice`) | CTR-2631: firmado con el cliente 830026010 el 2026-09-09 y las fichas de Clara no tienen una factura emitida a ese cliente hasta el 2026-10-09 | 60,000.00 | — | 27 | `contratos/CTR-2631.json` |
| 4 | Una oportunidad ganada no tiene su contrato firmado en la ficha de Fidel (`won_without_contract`) | OPP-2629 · Venta directa 29: ganada el 2026-10-06 por 45,000.00 y las fichas de Fidel no tienen un contrato firmado con el cliente 830026007 | 45,000.00 | — | 30 | `10-crm/hubspot-crm-exports-deals-2026-11-03.csv` fila 19 |
| 5 | Un contrato firmado no tiene su factura en la ficha de Clara dentro del plazo de facturación (`signed_without_invoice`) | CTR-2630: firmado con el cliente 830026009 el 2026-09-08 y las fichas de Clara no tienen una factura emitida a ese cliente hasta el 2026-10-08 | 45,000.00 | — | 28 | `contratos/CTR-2630.json` |

## El resultado

| Oportunidad ganada | Cuenta | Monto | Ganada | Contrato (Fidel) | Factura (Clara) |
|---|---|---|---|---|---|
| OPP-2601 · Renovación de licencias | Supermercados Bahía S.A. | 180,000.00 | 2026-10-10 | CTR-2601 | FE-2601 |
| OPP-2602 · Proyecto de expansión | Distribuidora Colón S.A. | 270,000.00 | 2026-10-22 | CTR-2602 | FE-2602 |
| OPP-2608 · Venta de equipos | Farmacias Chiriquí S.A. | 75,000.00 | 2026-10-05 | — | — |
| OPP-2629 · Venta directa 29 | Cliente Comercial 2650 S.A. | 45,000.00 | 2026-10-06 | — | — |
| OPP-2630 · Venta directa 30 | Cliente Comercial 2651 S.A. | 60,000.00 | 2026-10-07 | — | — |

| Contrato | Cliente | Firmado | Plazo de facturación | Factura | Estado |
|---|---|---|---|---|---|
| CTR-2601 | 830026000 | 2026-10-13 | 2026-11-12 | FE-2601 | facturado |
| CTR-2602 | 830026001 | 2026-10-24 | 2026-11-23 | FE-2602 | facturado |
| CTR-2603 | 830026004 | 2026-10-20 | 2026-11-19 | — | en plazo |
| CTR-2630 | 830026009 | 2026-09-08 | 2026-10-08 | — | vencido |
| CTR-2631 | 830026010 | 2026-09-09 | 2026-10-09 | — | vencido |

Plazo de facturación configurado: 30 días. Los contratos y las facturas son los de las fichas de Fidel y de Clara: no se vuelven a procesar.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `10-crm/hubspot-crm-exports-deals-2026-11-03.csv`
- `contratos/CTR-2630.json`
- `contratos/CTR-2631.json`

---

**Cuándo vuelvo:** sin reloj, porque en esta prueba nadie dio un sí explícito a la tarea programada. Para correrlo a mano: `/criterio-revenue:revenue-wake`.

La corrida quedó registrada como `2026-11-05-revenue-setup-1`, y lo que se mostró está en `estado-comercial/155622222-2-2017-almacenes-del-istmo/corridas/salida-revenue-setup.md`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.