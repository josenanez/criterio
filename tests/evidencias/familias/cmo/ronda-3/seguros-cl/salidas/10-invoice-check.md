# /criterio-campaigns:invoice-check 

Términos vigentes (versión 1.6, aceptada). Se procesó el periodo 2026-10 con corte 2026-11-25; dos facturas de pauta no tienen campaña ni orden de compra.

# Cada factura con su campaña · Seguros Cordillera Sintéticos · periodo 2026-10

**Entidad:** Seguros Cordillera Sintéticos (96789012-3) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Próspero, versión 1.0.0 · **Comando:** `invoice-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una factura de pauta no tiene campaña del plan ni orden de compra (`media_invoice_unmatched`) | F-105 · Radio Sintética: no dice a qué campaña pertenece y no tiene orden de compra | 7.000.000,00 | — | — | `50-campanas/facturas_de_pauta.xlsx` fila 6 |
| 2 | Una factura de pauta no tiene campaña del plan ni orden de compra (`media_invoice_unmatched`) | F-22 · Prensa Sintética: no dice a qué campaña pertenece y no tiene orden de compra | 4.000.000,00 | — | — | `50-campanas/facturas_de_pauta.xlsx` fila 10 |

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
| F-42 | Exteriores Sintéticos | C-42 | OC-42 | 9,000,000 | sí |
| F-22 | Prensa Sintética | — | — | 4,000,000 | no |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `50-campanas/facturas_de_pauta.xlsx`
- Fuentes técnicas: F-02 (families/criterio-cmo/FUENTES.es.md)

La corrida quedó registrada como `2026-11-25-invoice-check-1`.

Dos cosas que decidí sin preguntar, porque nadie podía responder:
- **Periodo:** usé 2026-10, el que trae la configuración.
- **Aceptación de términos:** el motor ya mostraba los términos como vigentes, con aceptación registrada en la versión 1.0.0. No volví a registrar la de José Francisco Ñáñez, porque `/criterio-campaigns:campaigns-setup` es el comando que la registra y aquí no hacía falta.