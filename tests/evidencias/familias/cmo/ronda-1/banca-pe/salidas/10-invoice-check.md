# /criterio-campaigns:invoice-check 

Corrí `invoice-check` para Banco Altiplano Sintético (20603335551), periodo 2026-10, con fecha 2026-11-25. Los términos ya estaban vigentes, en la versión 1.6 con aceptación 0.1.0. No hizo falta registrar la aceptación de nuevo.

De las 5 facturas de pauta, 4 tienen campaña del plan y orden de compra. Una no las tiene.

## Lo que hay que atender

| # | Señal | Qué | Monto | Cita |
|---|---|---|---|---|
| 1 | Una factura de pauta no tiene campaña del plan ni orden de compra (`media_invoice_unmatched`) | F-105 · Radio Sintética: no dice a qué campaña pertenece y no tiene orden de compra | 7,000,000.00 | `50-campanas/facturas_de_pauta.xlsx` fila 6 |

## El resultado

| Factura | Proveedor | Campaña | Orden de compra | Valor | En el plan |
|---|---|---|---|---|---|
| F-101 | Televisora Sintética | C-01 | OC-301 | 60,000,000 | sí |
| F-102 | Televisora Sintética | C-01 | OC-301 | 48,000,000 | sí |
| F-103 | Redes Sintéticas | C-02 | OC-302 | 18,000,000 | sí |
| F-104 | Exteriores Sintéticos | C-03 | OC-303 | 25,000,000 | sí |
| F-105 | Radio Sintética | — | — | 7,000,000 | no |

Todo lo que llegó se procesó, y la corrida no hizo preguntas. La fuente es `50-campanas/facturas_de_pauta.xlsx`.

Qué se paga con F-105 lo decide el área de mercadeo con finanzas. El agente no lo decide.

El reporte quedó en `estado-mercadeo/20603335551-banco-altiplano-sintetico/campanas/2026-10/reporte-invoice-check.md`. La salida que te mostré está en `estado-mercadeo/20603335551-banco-altiplano-sintetico/corridas/salida-invoice-check.md`. La corrida quedó registrada como `2026-11-25-invoice-check-1`.