# /criterio-finance:close-scan 

Terminé el barrido del cierre 2026-09. Quedaron 5 señales abiertas y la corrida está registrada.

Los términos estaban vigentes (versión 1.3, aceptada en 1.0.0), así que no registré una aceptación nueva. Corrí el motor con `--today 2026-10-06`.

65 archivos nuevos, 0 cambiados, 0 borrados. Convertí los documentos escritos (correo del estado, soportes y respuestas del auditor). La ficha ya traía el estado declarado "cerrado", así que no la modifiqué. No pude comparar contra la corrida anterior, porque el motor no da ese conteo. Las 5 señales son el total del periodo.

# Qué cambió en el cierre · Almacenes del Canal · periodo 2026-09

**Entidad:** Almacenes del Canal (155791002-2-2017) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 1.0.0 · **Aprueba:** Contralor

| # | Señal | Qué | Monto | Responsable | Días |
|---|---|---|---|---|---|
| 1 | `declared_close_vs_evidence` | Sofía León reportó el cierre como cerrado el 2026-10-05 (`correo-estado-del-cierre.md`), pero hay 4 señales abiertas que ese estado no explica | — | — | — |
| 2 | `einvoice_duplicate` | El mismo CUFE aparece en 2 archivos (001-0000000102): `fe-001-0000000102.xml` y `fe-001-0000000102-reenviada.xml` | 10,031.25 | — | — |
| 3 | `bank_unreconciled` | andino-7901: consignación en tránsito del 2026-09-30 por 6,420.00 (001-0000000107), `auxiliar-libros.csv` fila 16 | 6,420.00 | — | 0 |
| 4 | `recorded_without_einvoice` | Documento 002-0000000202 en las cuentas de compras, sin factura electrónica en `recibidas/` (`libro-mayor.xlsx` filas 56 y 57) | 5,092.50 | — | — |
| 5 | `audit_request_unanswered` | R-05, contratos de los proveedores principales: venció el 2026-10-02 (`pbc-2026-09.csv` fila 6) | — | Jorge Vela | 4 |

- **Sección vacía:** "El resultado" salió vacía en el reporte del motor. No agregué nada ahí.
- **Procesamiento:** todo lo que llegó se procesó.
- **Pendiente:** el aprobador del cierre no aparece en los documentos y quedó "Contralor" por defecto.

El reporte completo está en `estado-finanzas/155791002-2-2017-almacenes-del-canal/cierre/2026-09/reporte-close-scan.md`. La salida mostrada quedó en `corridas/salida-close-scan.md`, con id de corrida `2026-10-06-close-scan-1`.