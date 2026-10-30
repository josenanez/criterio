# /criterio-legal:contract-scan 

Revisé los 6 contratos: las fichas que ya existían coinciden con sus documentos y el motor no reporta `record_issues`. Salieron 3 señales, todas sobre garantías.

# Qué cambió en los contratos · Instituto Público de la Meseta · al 2026-10-06

**Entidad:** Instituto Público de la Meseta (3101399101) · **Fecha de corte:** 2026-10-06 · **Procesado:** 2026-10-06 · **Agente:** Fidel, versión 1.1.0 · **Comando:** `contract-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | La garantía de cumplimiento de un contrato público es menor que el mínimo de la ley de su país (`public_guarantee_below_law`) | CTR-3901: la garantía de cumplimiento es de 3.600.000,00 y la ley pide al menos el 5 % del valor del contrato, 6.000.000,00 | 2.400.000,00 | — | — | `contratos/CTR-3901-tecnologia-gubernamental-s-a/20-garantias/poliza-cumplimiento.md` |
| 2 | La garantía de cumplimiento de un contrato público es menor que el mínimo de la ley de su país (`public_guarantee_below_law`) | CTR-3903: la garantía de cumplimiento es de 2.700.000,00 y la ley pide al menos el 5 % del valor del contrato, 4.500.000,00 | 1.800.000,00 | — | — | `contratos/CTR-3903-edificaciones-oficiales-s-a/20-garantias/poliza-cumplimiento.md` |
| 3 | La garantía exigida en un contrato público supera el tope de la ley de su país (`public_guarantee_over_cap`) | CTR-3906: la garantía exigida es de 9.000.000,00 y la ley la limita a 7.500.000,00, sin una justificación por la complejidad y los riesgos | 1.500.000,00 | — | — | `contratos/CTR-3906-mantenimiento-publico-s-a/20-garantias/poliza-cumplimiento.md` |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `contratos/CTR-3901-tecnologia-gubernamental-s-a/20-garantias/poliza-cumplimiento.md`
- `contratos/CTR-3903-edificaciones-oficiales-s-a/20-garantias/poliza-cumplimiento.md`
- `contratos/CTR-3906-mantenimiento-publico-s-a/20-garantias/poliza-cumplimiento.md`

La corrida quedó registrada como `2026-10-06-contract-scan-1`, y el texto de arriba está guardado en `corridas/salida-contract-scan.md`.

Los términos ya estaban aceptados en la configuración por José Francisco Ñáñez (versión 1.3, 2026-10-06), así que no volví a registrarlos.