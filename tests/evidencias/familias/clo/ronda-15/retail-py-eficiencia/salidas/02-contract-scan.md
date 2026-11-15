# /criterio-legal:contract-scan 

El inventario marcó todos los documentos como nuevos porque no había un inventario guardado de la corrida anterior. Revisé las fichas que dejó `legal-setup` contra cada contrato, el otrosí, las pólizas, los certificados y el acta, y coinciden, así que no cambié ninguna. El motor no reportó `record_issues`. Las señales son las mismas que encontró `legal-setup`; no hay ninguna nueva.

# Qué cambió en los contratos · Distribuidora del Ybytyruzú Sintética · al 2026-10-06

**Entidad:** Distribuidora del Ybytyruzú Sintética (88612904-4) · **Fecha de corte:** 2026-10-06 · **Procesado:** 2026-10-06 · **Agente:** Fidel, versión 1.6.3 · **Comando:** `contract-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Quien firmó por la entidad no tenía facultad por el tipo o el monto según la matriz de atribuciones (`signed_without_authority`) | CTR-4501: Celeste Villalba firmó por 2.640.000.000,00 y la matriz de atribuciones no le da facultad para ese tipo y monto | 2.640.000.000,00 | — | — | `contratos/CTR-4501-logistica-del-chaco-sintetica-s-a/10-contrato/contrato.md` · `00-referencia/matriz-atribuciones.csv` fila 2 |
| 2 | Un contrato vence dentro de los días configurados y no tiene una decisión registrada de renovar o terminar (`contract_expiring`) | CTR-4503: vence el 2026-11-25, en 50 días, sin decisión de renovar o terminar | 1.980.000.000,00 | — | 50 | `contratos/CTR-4503-centro-comercial-del-sur-sintetica-s-a/10-contrato/contrato.md` |
| 3 | Hay pagos con fecha posterior a la terminación del contrato (`payment_after_termination`) | CTR-4506: 1 pago(s) después de la terminación del 2026-07-31, por 82.500.000,00 | 82.500.000,00 | — | — | `10-registro/pagos-2026-09-30.csv` fila 20 |
| 4 | La póliza aportada vence antes de lo que exige el contrato (`guarantee_expires_early`) | CTR-4501: la póliza de cumplimiento vence el 2027-05-31 y el contrato la exige hasta el 2027-07-31 | — | — | 61 | `contratos/CTR-4501-logistica-del-chaco-sintetica-s-a/20-garantias/poliza-cumplimiento.md` |
| 5 | Un contrato de la carpeta no está en el registro, o una fila del registro no tiene su documento (`register_mismatch`) | CTR-4509: está en el registro y no hay documento en contratos/CTR-4509…/10-contrato/ | — | — | — | `10-registro/registro-contratos.csv` fila 8 |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/matriz-atribuciones.csv`
- `10-registro/pagos-2026-09-30.csv`
- `10-registro/registro-contratos.csv`
- `contratos/CTR-4501-logistica-del-chaco-sintetica-s-a/10-contrato/contrato.md`
- `contratos/CTR-4501-logistica-del-chaco-sintetica-s-a/20-garantias/poliza-cumplimiento.md`
- `contratos/CTR-4503-centro-comercial-del-sur-sintetica-s-a/10-contrato/contrato.md`

---

Corrida registrada como `2026-10-06-contract-scan-1`. Lo mostrado quedó guardado en `estado-legal/88612904-4-distribuidora-del-ybytyruzu-sintetica/corridas/salida-contract-scan.md`. La sección «El resultado» sale vacía porque así la generó el motor.