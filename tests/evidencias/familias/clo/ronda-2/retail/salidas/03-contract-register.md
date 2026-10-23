# /criterio-legal:contract-register 

Los términos (versión 1.2) ya estaban vigentes y aceptados, así que no hizo falta registrar la aceptación. El registro tiene una fila sin documento: CTR-309.

# Registro de contratos · Almacenes Caribe · al 2026-10-06

## Lo que hay que atender

| # | Señal | Qué | Cita |
|---|---|---|---|
| 1 | Fila del registro sin documento (`register_mismatch`) | CTR-309 está en el registro y no hay documento en `contratos/CTR-309…/10-contrato/` | `10-registro/registro-contratos.csv` fila 8 |

## El resultado

| Contrato | Contraparte | Estado en el registro | Estado según sus fechas | Diferencias |
|---|---|---|---|---|
| CTR-301 | Logística Caribe S.A.S. | vigente | vigente | — |
| CTR-302 | Empaques del Atlántico S.A.S. | vigente | vigente | — |
| CTR-303 | Centro Comercial Mar S.A. | vigente | vigente | — |
| CTR-304 | Punto de Venta Digital S.A.S. | vigente | vigente | — |
| CTR-305 | Mercadeo Integral S.A.S. | vigente | vigente | — |
| CTR-306 | Refrigeración Industrial S.A.S. | terminado | terminado | — |
| CTR-309 | Publicidad Exterior S.A.S. | vigente | — | — |

Todo lo que llegó se procesó. El agente no hizo preguntas en esta corrida. La única fuente fue `10-registro/registro-contratos.csv`.

La salida quedó en `estado-legal/900765432-almacenes-caribe/corridas/salida-contract-register.md`. La corrida quedó registrada como `2026-10-06-contract-register-1`, con caso «todos».

El motor devolvió `"hallazgos": 5` al registrar la corrida. El reporte solo lista una señal, y no sé de dónde sale la diferencia.