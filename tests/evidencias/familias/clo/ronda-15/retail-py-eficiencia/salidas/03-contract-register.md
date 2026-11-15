# /criterio-legal:contract-register 

El registro tiene una fila sin documento, CTR-4509. Los otros seis contratos coinciden con sus documentos.

Los términos de la versión 1.5 estaban vigentes. La aceptación a nombre de José Francisco Ñáñez que pedías no se registró en esta corrida, porque `terminos` ya devolvió `vigente: true` y no pidió aceptar.

# Registro de contratos · Distribuidora del Ybytyruzú Sintética · al 2026-10-06

**Entidad:** Distribuidora del Ybytyruzú Sintética (88612904-4) · **Fecha de corte:** 2026-10-06 · **Procesado:** 2026-10-06 · **Agente:** Fidel, versión 1.6.3 · **Comando:** `contract-register`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un contrato de la carpeta no está en el registro, o una fila del registro no tiene su documento (`register_mismatch`) | CTR-4509: está en el registro y no hay documento en contratos/CTR-4509…/10-contrato/ | — | — | — | `10-registro/registro-contratos.csv` fila 8 |

## El resultado

| Contrato | Contraparte | Estado en el registro | Estado según sus fechas | Diferencias |
|---|---|---|---|---|
| CTR-4501 | Logística del Chaco Sintética S.A. | vigente | vigente | — |
| CTR-4502 | Empaques de Luque Sintética S.A. | vigente | vigente | — |
| CTR-4503 | Centro Comercial del Sur Sintética S.A. | vigente | vigente | — |
| CTR-4504 | Pagos en Línea Sintética S.A. | vigente | vigente | — |
| CTR-4505 | Mercadeo Integral Sintética S.A. | vigente | vigente | — |
| CTR-4506 | Refrigeración Comercial Sintética S.A. | terminado | terminado | — |
| CTR-4509 | Publicidad Exterior S.A.S. | vigente | — | — |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `10-registro/registro-contratos.csv`

La corrida quedó registrada con el id `2026-10-06-contract-register-1`. La salida está en `estado-legal/88612904-4-distribuidora-del-ybytyruzu-sintetica/corridas/salida-contract-register.md`.

Dos cosas más:
- **Carpeta sobrante:** creé por error `.criterio/legal/88612904-4/estado/corridas` y la borré. La carpeta de estado real es la que fija `state` en la configuración.
- **Copia del reporte:** `salida-contract-register.md` es una copia del reporte que escribió el motor. Lo que escribí encima, estas notas, no está en ese archivo.