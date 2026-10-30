# /criterio-legal:contract-scan 

El motor procesó los contratos y encontró 2 señales, las dos de garantía de cumplimiento por debajo del mínimo legal. No extraje las fichas a mano: el motor las leyó de los documentos convertidos y no devolvió `record_issues`.

Los términos ya estaban vigentes, así que no registré ninguna aceptación nueva.

# Qué cambió en los contratos · Instituto Público de Occidente · al 2026-10-06

**Entidad:** Instituto Público de Occidente (08010003991010) · **Fecha de corte:** 2026-10-06 · **Agente:** Fidel, versión 1.2.0 · **Comando:** `contract-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Cita |
|---|---|---|---|---|
| 1 | `public_guarantee_below_law`: la garantía de cumplimiento de un contrato público es menor que el mínimo de la ley de su país | CTR-4301: la garantía es de 780,000.00 y la ley pide al menos el 15 % del valor del contrato, 900,000.00 | 120,000.00 | `contratos/CTR-4301-tecnologia-gubernamental-s-de-r-l/20-garantias/poliza-cumplimiento.md` |
| 2 | `public_guarantee_below_law`: la garantía de cumplimiento de un contrato público es menor que el mínimo de la ley de su país | CTR-4303: la garantía es de 585,000.00 y la ley pide al menos el 15 % del valor del contrato, 675,000.00 | 90,000.00 | `contratos/CTR-4303-edificaciones-oficiales-s-de-r-l/20-garantias/poliza-cumplimiento.md` |

## Lo que no se pudo procesar

Todo lo que llegó se procesó: 35 documentos convertidos y ninguno ilegible.

## Las preguntas que hizo

Ninguna en esta corrida.

## Otros hallazgos del inventario

- Había 64 documentos nuevos y ninguno cambiado ni borrado. Seis son contratos, del CTR-4301 al CTR-4306.
- `00-referencia/politica-contratacion.md` está fuera de lugar. El motor indica que iría en `20-politicas/`.

La salida quedó en `estado-legal/08010003991010-instituto-publico-de-occidente/corridas/salida-contract-scan.md`. La corrida quedó registrada como `2026-10-06-contract-scan-1`, con 2 hallazgos y el caso «todos».

El comando no me pidió ninguna decisión y no emití opinión jurídica sobre las garantías.