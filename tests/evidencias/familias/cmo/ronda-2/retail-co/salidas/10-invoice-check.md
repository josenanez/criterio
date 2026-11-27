# /criterio-campaigns:invoice-check 

Términos vigentes (versión 1.6, aceptados por José Francisco Ñáñez). Periodo 2026-10, el de la configuración.

# Cada factura con su campaña · Almacenes del Valle Sintéticos · periodo 2026-10

**Entidad:** Almacenes del Valle Sintéticos (901333555) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Próspero, versión 0.2.0 · **Comando:** `invoice-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una factura de pauta no tiene campaña del plan ni orden de compra (`media_invoice_unmatched`) | F-23 · Vallas Sintéticas: no dice a qué campaña pertenece y no tiene orden de compra | 9.000.000,00 | — | — | `50-campanas/facturas_de_pauta.xlsx` fila 14 |
| 2 | Una factura de pauta no tiene campaña del plan ni orden de compra (`media_invoice_unmatched`) | F-105 · Radio Sintética: no dice a qué campaña pertenece y no tiene orden de compra | 7.000.000,00 | — | — | `50-campanas/facturas_de_pauta.xlsx` fila 6 |
| 3 | Una factura de pauta no tiene campaña del plan ni orden de compra (`media_invoice_unmatched`) | F-22 · Prensa Sintética: no dice a qué campaña pertenece y no tiene orden de compra | 4.000.000,00 | — | — | `50-campanas/facturas_de_pauta.xlsx` fila 13 |

## El resultado

| Factura | Proveedor | Campaña | Orden de compra | Valor | En el plan |
|---|---|---|---|---|---|
| F-101 | Televisora Sintética | C-01 | OC-301 | 60,000,000 | sí |
| F-102 | Televisora Sintética | C-01 | OC-301 | 48,000,000 | sí |
| F-103 | Redes Sintéticas | C-02 | OC-302 | 18,000,000 | sí |
| F-104 | Exteriores Sintéticos | C-03 | OC-303 | 25,000,000 | sí |
| F-105 | Radio Sintética | — | — | 7,000,000 | no |
| F-321 | Digital Sintética | C-32 | OC-32 | 12,000,000 | sí |
| F-322 | Digital Sintética | C-32 | OC-32 | 11,000,000 | sí |
| F-331 | Digital Sintética | C-33 | OC-33 | 30,000,000 | sí |
| F-332 | Digital Sintética | C-33 | OC-33 | 24,000,000 | sí |
| F-42 | Exteriores Sintéticos | C-42 | OC-42 | 9,000,000 | sí |
| F-43 | Exteriores Sintéticos | C-43 | OC-43 | 11,000,000 | sí |
| F-22 | Prensa Sintética | — | — | 4,000,000 | no |
| F-23 | Vallas Sintéticas | — | — | 9,000,000 | no |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `50-campanas/facturas_de_pauta.xlsx`
- Fuentes técnicas: F-02 (families/criterio-cmo/FUENTES.es.md)

La corrida quedó registrada como `2026-11-25-invoice-check-1`.