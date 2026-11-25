# /criterio-campaigns:invoice-check 

Corrí `invoice-check` sobre el periodo 2026-11, el mismo del `budget-check` anterior. Los términos están vigentes (versión 1.6, aceptados por José Francisco Ñáñez el 2026-11-25). Una factura de pauta no trae campaña ni orden de compra. El área de mercadeo con finanzas decide qué hacer con ella.

# Cada factura con su campaña · Almacenes del Valle Sintéticos · periodo 2026-11

**Entidad:** Almacenes del Valle Sintéticos (901333555) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Próspero, versión 0.1.0 · **Comando:** `invoice-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una factura de pauta no tiene campaña del plan ni orden de compra (`media_invoice_unmatched`) | F-105 · Radio Sintética: no dice a qué campaña pertenece y no tiene orden de compra | 7.000.000,00 | — | — | `50-campanas/facturas_de_pauta.xlsx` fila 6 |

## El resultado

| Factura | Proveedor | Campaña | Orden de compra | Valor | En el plan |
|---|---|---|---|---|---|
| F-101 | Televisora Sintética | C-01 | OC-301 | 60,000,000 | sí |
| F-102 | Televisora Sintética | C-01 | OC-301 | 48,000,000 | sí |
| F-103 | Redes Sintéticas | C-02 | OC-302 | 18,000,000 | sí |
| F-104 | Exteriores Sintéticos | C-03 | OC-303 | 25,000,000 | sí |
| F-105 | Radio Sintética | — | — | 7,000,000 | no |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `50-campanas/facturas_de_pauta.xlsx`
- Fuentes técnicas: F-02 (families/criterio-cmo/FUENTES.es.md)

La corrida quedó registrada como `2026-11-25-invoice-check-1`. El reporte está en `estado-mercadeo/901333555-almacenes-del-valle-sinteticos/campanas/2026-11/reporte-invoice-check.md`, y lo mostrado, en `corridas/salida-invoice-check.md`.