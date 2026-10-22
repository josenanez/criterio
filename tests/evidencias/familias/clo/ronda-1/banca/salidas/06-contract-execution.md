# /criterio-legal:contract-execution 

Los términos (v1.2) ya estaban vigentes y aceptados, así que no tuve que registrar la aceptación de José Francisco Ñáñez. Corrí el reporte con corte 2026-10-06.

# Pagos y garantías · Banco Andino · al 2026-10-06

**Entidad:** Banco Andino (900123456) · **Fecha de corte:** 2026-10-06 · **Procesado:** 2026-10-06 · **Agente:** Fidel, versión 0.7.0 · **Comando:** `contract-execution`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | El contrato exige una garantía y no hay póliza aportada (`guarantee_missing`) | CTR-103: exige la garantía de calidad y no hay póliza aportada en 20-garantias/ | — | — | — | `contratos/CTR-103-inmobiliaria-centro-s-a/10-contrato/contrato.md, cláusula 9` |

## El resultado

| Contrato | Valor con otrosíes | Pagado | Saldo | Último pago |
|---|---|---|---|---|
| CTR-101 | 400.000.000,00 | 120.000.000,00 | 280.000.000,00 | 2026-09-10 |
| CTR-102 | 250.000.000,00 | 75.000.000,00 | 175.000.000,00 | 2026-09-10 |
| CTR-103 | 300.000.000,00 | 90.000.000,00 | 210.000.000,00 | 2026-09-10 |
| CTR-104 | 150.000.000,00 | 45.000.000,00 | 105.000.000,00 | 2026-09-10 |
| CTR-105 | 100.000.000,00 | 30.000.000,00 | 70.000.000,00 | 2026-09-10 |
| CTR-106 | 250.000.000,00 | 75.000.000,00 | 175.000.000,00 | 2026-07-10 |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `contratos/CTR-103-inmobiliaria-centro-s-a/10-contrato/contrato.md, cláusula 9`

La corrida quedó registrada como `2026-10-06-contract-execution-1`, con 5 hallazgos según el motor. El reporte solo muestra una señal en "Lo que hay que atender". No averigüé por qué el motor cuenta 5. La salida completa está en `estado-legal/900123456-banco-andino/corridas/salida-contract-execution.md`.