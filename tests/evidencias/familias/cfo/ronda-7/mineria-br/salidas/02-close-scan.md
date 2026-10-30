# /criterio-finance:close-scan 

Este barrido encontró 66 archivos nuevos, ninguno cambiado ni borrado, y 4 señales abiertas. El motor no entrega el conteo de la corrida anterior, así que no hay comparación de señales.

La ficha ya traía la declaración de Sofia Leão («en curso», 2026-10-05) y el requerimiento R-09 de la carta del auditor. Coinciden con los documentos, así que no agregué nada.

**Inventario:** nada está fuera de lugar ni ilegible, y todo lo que llegó se procesó.

**Términos:** estaban vigentes (v1.3, aceptados por José Francisco Ñáñez el 2026-10-06), así que no hubo que registrarlos de nuevo.

## Qué hay que atender (periodo 2026-09)

| # | Señal | Detalle | Monto | Fuente |
|---|---|---|---|---|
| 1 | `einvoice_duplicate` | La misma clave de acceso (1-102) está en dos archivos. | 39.634,15 | `emitidas/fe-1-102.xml` y `fe-1-102-reenviada.xml` |
| 2 | `recorded_without_einvoice` | El documento 2-202, registrado en compras, no tiene factura electrónica en `recibidas/`. | 33.950,00 | `livro-razao.xlsx`, filas 56 y 57 |
| 3 | `bank_unreconciled` | En bandeirante-3101 hay una nota débito del 2026-09-30 sin registrar y sin referencia. | -4.000,00 | `extrato.csv`, fila 17 |
| 4 | `audit_request_unanswered` | R-05 (contratos de los principales proveedores) está vencido desde el 2026-10-02; el responsable es Jorge Veloso. | — | `pbc-2026-09.xlsx`, fila 6 |

El reporte completo lo escribió el motor en `estado-finanzas/…/cierre/2026-09/reporte-close-scan.md`. Su sección «El resultado» salió vacía.

**Corrida registrada:** `2026-10-06-close-scan-1`, con la salida guardada en `estado-finanzas/…/corridas/salida-close-scan.md`.