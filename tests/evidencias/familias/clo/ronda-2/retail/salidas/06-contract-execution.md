# /criterio-legal:contract-execution 

Los términos (v1.2) ya estaban vigentes y aceptados, así que no hizo falta registrar nada. Corrí el reporte con `--today 2026-10-06` y dejé la corrida registrada.

# Pagos y garantías · Almacenes Caribe · al 2026-10-06

**Entidad:** Almacenes Caribe (900765432) · **Fecha de corte:** 2026-10-06 · **Procesado:** 2026-10-06 · **Agente:** Fidel, versión 0.8.0 · **Comando:** `contract-execution`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Hay pagos con fecha posterior a la terminación del contrato (`payment_after_termination`) | CTR-306: 1 pago(s) después de la terminación del 2026-07-31, por 10.000.000,00 | 10.000.000,00 | — | — | `10-registro/pagos-2026-09-30.csv` fila 20 |
| 2 | La póliza aportada vence antes de lo que exige el contrato (`guarantee_expires_early`) | CTR-301: la póliza de cumplimiento vence el 2027-05-31 y el contrato la exige hasta el 2027-07-31 | — | — | 61 | `contratos/CTR-301-logistica-caribe-s-a-s/20-garantias/poliza-cumplimiento.md` |

## El resultado

| Contrato | Valor con otrosíes | Pagado | Saldo | Último pago |
|---|---|---|---|---|
| CTR-301 | 320.000.000,00 | 96.000.000,00 | 224.000.000,00 | 2026-09-10 |
| CTR-302 | 440.000.000,00 | 132.000.000,00 | 308.000.000,00 | 2026-09-10 |
| CTR-303 | 240.000.000,00 | 72.000.000,00 | 168.000.000,00 | 2026-09-10 |
| CTR-304 | 120.000.000,00 | 36.000.000,00 | 84.000.000,00 | 2026-09-10 |
| CTR-305 | 80.000.000,00 | 24.000.000,00 | 56.000.000,00 | 2026-09-10 |
| CTR-306 | 200.000.000,00 | 70.000.000,00 | 130.000.000,00 | 2026-09-10 |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `10-registro/pagos-2026-09-30.csv`
- `contratos/CTR-301-logistica-caribe-s-a-s/20-garantias/poliza-cumplimiento.md`

---
Lo que te mostré lo guardé en `estado-legal/900765432-almacenes-caribe/corridas/salida-contract-execution.md`. El motor registró la corrida como `2026-10-06-contract-execution-1` y la cuenta con 5 hallazgos, mientras que el reporte muestra 2 señales. No sé a qué se debe la diferencia, porque la salida no lo explica.