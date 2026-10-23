# /criterio-legal:contract-scan 

Corrida del 2026-10-06: 29 documentos de contratos procesados; las fichas de los seis contratos ya coincidían con sus documentos y no hubo que cambiarlas.

# Qué cambió en los contratos · Almacenes Caribe · al 2026-10-06

**Entidad:** Almacenes Caribe (900765432) · **Fecha de corte:** 2026-10-06 · **Procesado:** 2026-10-06 · **Agente:** Fidel, versión 0.8.0 · **Comando:** `contract-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Quien firmó por la entidad no tenía facultad por el tipo o el monto según la matriz de atribuciones (`signed_without_authority`) | CTR-302 · OT-1: Lucía Ortega firmó el otrosí que lleva el contrato a 440.000.000,00 sin facultad para ese monto | 280.000.000,00 | — | — | `contratos/CTR-302-empaques-del-atlantico-s-a-s/10-contrato/otrosi-1.md` |
| 2 | Un contrato vence dentro de los días configurados y no tiene una decisión registrada de renovar o terminar (`contract_expiring`) | CTR-303: vence el 2026-11-25, en 50 días, sin decisión de renovar o terminar | 240.000.000,00 | — | 50 | `contratos/CTR-303-centro-comercial-mar-s-a/10-contrato/contrato.md` |
| 3 | Hay pagos con fecha posterior a la terminación del contrato (`payment_after_termination`) | CTR-306: 1 pago(s) después de la terminación del 2026-07-31, por 10.000.000,00 | 10.000.000,00 | — | — | `10-registro/pagos-2026-09-30.csv` fila 20 |
| 4 | La póliza aportada vence antes de lo que exige el contrato (`guarantee_expires_early`) | CTR-301: la póliza de cumplimiento vence el 2027-05-31 y el contrato la exige hasta el 2027-07-31 | — | — | 61 | `contratos/CTR-301-logistica-caribe-s-a-s/20-garantias/poliza-cumplimiento.md` |
| 5 | Un contrato de la carpeta no está en el registro, o una fila del registro no tiene su documento (`register_mismatch`) | CTR-309: está en el registro y no hay documento en contratos/CTR-309…/10-contrato/ | — | — | — | `10-registro/registro-contratos.csv` fila 8 |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `10-registro/pagos-2026-09-30.csv`
- `10-registro/registro-contratos.csv`
- `contratos/CTR-301-logistica-caribe-s-a-s/20-garantias/poliza-cumplimiento.md`
- `contratos/CTR-302-empaques-del-atlantico-s-a-s/10-contrato/otrosi-1.md`
- `contratos/CTR-303-centro-comercial-mar-s-a/10-contrato/contrato.md`

La corrida quedó registrada como `2026-10-06-contract-scan-1`.