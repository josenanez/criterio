# /criterio-legal:contract-scan 

Corrida registrada con 5 señales. Los 7 contratos se procesaron completos, sin `record_issues` y sin documentos ilegibles. Las fichas de la configuración inicial ya coincidían con los documentos, así que no hubo que corregirlas.

# Qué cambió en los contratos · Almacenes del Canal · al 2026-10-06

**Entidad:** Almacenes del Canal (155791002-2-2017) · **Fecha de corte:** 2026-10-06 · **Procesado:** 2026-10-06 · **Agente:** Fidel, versión 1.1.0 · **Comando:** `contract-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Días | Cita |
|---|---|---|---|---|---|
| 1 | Quien firmó por la entidad no tenía facultad por el tipo o el monto según la matriz de atribuciones (`signed_without_authority`) | CTR-3001: Abdiel Moreno firmó por 360,000.00 y la matriz de atribuciones no le da facultad para ese tipo y monto | 360,000.00 | — | `contratos/CTR-3001-logistica-colon-s-a/10-contrato/contrato.md` · `00-referencia/matriz-atribuciones.csv` fila 2 |
| 2 | Un contrato vence dentro de los días configurados y no tiene una decisión registrada de renovar o terminar (`contract_expiring`) | CTR-3003: vence el 2026-11-25, sin decisión de renovar o terminar | 270,000.00 | 50 | `contratos/CTR-3003-centro-comercial-albrook-s-a/10-contrato/contrato.md` |
| 3 | La póliza aportada vence antes de lo que exige el contrato (`guarantee_expires_early`) | CTR-3001: la póliza de cumplimiento vence el 2027-05-31 y el contrato la exige hasta el 2027-07-31 | — | 61 | `contratos/CTR-3001-logistica-colon-s-a/20-garantias/poliza-cumplimiento.md` |
| 4 | Un contrato de la carpeta no está en el registro, o una fila del registro no tiene su documento (`register_mismatch`) | CTR-3007: el contrato está en la carpeta y no en el registro | — | — | `contratos/CTR-3007-vigilancia-del-istmo-s-a/` |
| 5 | El valor o las fechas del registro no son los del documento (`register_differs_from_contract`) | CTR-3002: valor 270,000.00 en el registro y 225,000.00 en el documento | — | — | `10-registro/registro-contratos.csv` fila 3 · `contratos/CTR-3002-empaques-del-pacifico-s-a/10-contrato/contrato.md` |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/matriz-atribuciones.csv`
- `10-registro/registro-contratos.csv`
- `contratos/CTR-3001-logistica-colon-s-a/10-contrato/contrato.md`
- `contratos/CTR-3001-logistica-colon-s-a/20-garantias/poliza-cumplimiento.md`
- `contratos/CTR-3002-empaques-del-pacifico-s-a/10-contrato/contrato.md`
- `contratos/CTR-3003-centro-comercial-albrook-s-a/10-contrato/contrato.md`
- `contratos/CTR-3007-vigilancia-del-istmo-s-a/`

Dos cosas para saber sobre la corrida:
- **Fecha de corte:** pasé `--today 2026-10-06` al motor como pidieron. `compute` y `reporte` la aceptaron; `terminos`, `convertir` y `corrida` no mostraron ningún efecto de ella.
- **Salida guardada:** `corridas/salida-contract-scan.md` contiene el reporte tal cual, sin las líneas de introducción que podía agregar antes del encabezado.