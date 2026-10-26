# /criterio-treasury:treasury-scan 

Terminé el scan de tesorería de Banco Ribera para 2026-09. Los términos (versión 1.2) ya estaban vigentes, así que no registré ninguna aceptación nueva.

**Inventario:** 66 archivos. Hay dos nuevos, los auxiliares `1305-clientes.csv` y `2205-proveedores.csv` de 2026-08. Hay uno cambiado, `00-referencia/politica-tesoreria.csv`.

**Señales (3):**
1. **Pago P-3 por 48,000.00:** lo aprobó Carlos Paz, que no está en la matriz de firmas (`programa-pagos.csv`, fila 4).
2. **Crédito de tesorería del Banco del Norte por 1,600,000.00:** vence el 2026-10-26, en 20 días (`registro-deuda.xlsx`, fila 2).
3. **Posición en USD:** equivale a 450,000.00 PEN y supera el límite de 225,000.00 (`extracto.csv` fila 3 y `politica-tesoreria.csv` fila 7).

La sección "El resultado" salió vacía en el reporte del motor, y no la rellené porque cualquier cifra tendría que venir del motor. No hubo nada sin procesar ni preguntas.

La salida está en `estado-finanzas/20710000019-banco-ribera/corridas/salida-treasury-scan.md`. La corrida quedó registrada como `2026-10-06-treasury-scan-2` con 3 hallazgos. Ya existía una corrida `treasury-scan-1` del mismo día, y no la toqué.