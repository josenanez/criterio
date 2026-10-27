# /criterio-legal:contract-scan 

Los 6 contratos eran nuevos para el inventario. Sus fichas ya coincidían con los documentos, así que no las reescribí. Salieron 4 señales.

# Qué cambió en los contratos · Minera Atacama Norte · al 2026-10-06

**Entidad:** Minera Atacama Norte (76089001-4) · **Fecha de corte:** 2026-10-06 · **Procesado:** 2026-10-06 · **Agente:** Fidel, versión 0.10.0 · **Comando:** `contract-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Días | Cita |
|---|---|---|---|---|---|
| 1 | Quien firmó por la entidad no tenía facultad por el tipo o el monto según la matriz de atribuciones (`signed_without_authority`) | CTR-1101: Ignacio Pizarro firmó por 360.000.000,00 y la matriz no le da facultad para ese tipo y monto | 360.000.000,00 | — | `contratos/CTR-1101-sondajes-del-norte-spa/10-contrato/contrato.md` · `00-referencia/matriz-atribuciones.csv` fila 2 |
| 2 | Pasó la fecha límite del preaviso de un contrato con renovación automática sin una decisión registrada (`renewal_notice_missed`) | CTR-1101: el preaviso venció el 2026-10-01 sin decisión; el contrato se prorroga en sus términos el 2026-10-31 | — | 5 | `contratos/CTR-1101-sondajes-del-norte-spa/10-contrato/contrato.md` |
| 3 | El documento no tiene la firma de las dos partes y el contrato ya empezó (`unsigned_contract`) | CTR-1105: el documento no tiene la firma de las dos partes y el contrato empezó el 2026-02-01 | 90.000.000,00 | — | `contratos/CTR-1105-consultora-ambiental-ltda/10-contrato/contrato.md` |
| 4 | El contrato exige una garantía y no hay póliza aportada (`guarantee_missing`) | CTR-1103: exige la garantía de calidad y no hay póliza aportada en 20-garantias/ | — | — | `contratos/CTR-1103-campamentos-desierto-ltda/10-contrato/contrato.md, cláusula 9` |

## El resultado

(Vacío en el reporte del motor.)

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/matriz-atribuciones.csv`
- `contratos/CTR-1101-sondajes-del-norte-spa/10-contrato/contrato.md`
- `contratos/CTR-1103-campamentos-desierto-ltda/10-contrato/contrato.md, cláusula 9`
- `contratos/CTR-1105-consultora-ambiental-ltda/10-contrato/contrato.md`

La corrida quedó registrada como `2026-10-06-contract-scan-1`, con 4 hallazgos. El texto que muestro arriba, con la sección "El resultado" resumida en "(Vacío en el reporte del motor.)", es una versión editada. La salida guardada en `corridas/salida-contract-scan.md` lleva esa sección vacía, tal como la dio el motor, y no la nota que acabo de poner aquí.

El reporte completo del motor está en `estado-legal/76089001-4-minera-atacama-norte/contratos/reporte-contract-scan.md`.