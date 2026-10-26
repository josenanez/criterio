# /criterio-finance:close-scan 

El barrido de 2026-09 de Banco Ribera dio 5 señales abiertas. La más importante es que el correo del 2026-10-05 declara el cierre como cerrado y hay 4 señales que ese estado no explica.

El inventario encontró 64 archivos nuevos y ninguno cambiado, borrado o fuera de su lugar. Los términos de la versión 0.10.0 ya estaban vigentes, así que no hubo nada que registrar. Convertí los soportes C-01, C-03, C-04 y C-05, las respuestas R-01 a R-03, el requerimiento del auditor y el correo. La ficha ya traía la declaración de Sofía León y los requerimientos R-01 a R-05 vienen en la tabla del auditor, así que no la modifiqué.

| # | Señal | Detalle |
|---|---|---|
| 1 | Tarea cumplida sin soporte | C-02 (conciliar cada cuenta bancaria, a cargo de Andrés Paz) figura cumplida y no hay un soporte C-02 en `2026-09/40-soportes/`. |
| 2 | Cierre declarado contra evidencia | El correo dice «cerrado» y hay 4 señales abiertas. |
| 3 | Factura duplicada | F001-00000102 aparece en dos archivos (la original y la reenviada), por 18,880.00. |
| 4 | Banco sin conciliar | andino-7101 tiene una consignación en tránsito del 2026-09-30 por 12,980.00 (F001-00000107). |
| 5 | Diferencia de IGV | F001-00000104 tiene IGV 2,160.00 en el XML y 2,170.00 en libros, una diferencia de 10.00. |

Todo lo que llegó se procesó. El motor no da una comparación de señales contra la corrida anterior, así que no puedo decir cuántas de las 5 son nuevas.

Guardé todo lo mostrado en `estado-finanzas/20710000019-banco-ribera/corridas/salida-close-scan.md` y la corrida quedó registrada como `2026-10-06-close-scan-1`. El reporte completo está en `estado-finanzas/20710000019-banco-ribera/cierre/2026-09/reporte-close-scan.md`.