# /criterio-finance:close-scan 

Hay 64 archivos nuevos, ninguno cambiado, borrado ni fuera de su lugar. Hay 5 señales abiertas en 2026-09. El estado del cierre no coincide con la evidencia: el correo de Sofía León del 2026-10-05 lo declara cerrado y hay otras 4 señales abiertas. No hay una corrida anterior de close-scan, así que no pude decir cuáles señales son nuevas.

Convertí los 9 documentos escritos de `40-soportes` y `50-auditoria`. La ficha ya traía la declaración del correo. Los requerimientos R-01 a R-05 vienen en la tabla del auditor, así que no agregué ninguno.

## Qué cambió en el cierre · Banco Ribera · periodo 2026-09

| # | Señal | Qué | Monto |
|---|---|---|---|
| 1 | Tarea cumplida sin soporte | C-02, conciliar cada cuenta bancaria: figura cumplida y no hay soporte que empiece por C-02 en `2026-09/40-soportes/` (responsable Andrés Paz; `00-referencia/checklist-cierre.csv` fila 3) | — |
| 2 | Cierre declarado contra evidencia | El cierre se reporta cerrado y hay 4 señales abiertas que ese estado no explica | — |
| 3 | Factura duplicada | F001-00000102 aparece en 2 archivos: `fe-F001-00000102.xml` y `fe-F001-00000102-reenviada.xml` | 18,880.00 |
| 4 | Banco sin conciliar | andino-7101: consignación en tránsito del 2026-09-30 (F001-00000107), `auxiliar-libros.csv` fila 17 | 12,980.00 |
| 5 | Diferencia de IGV | F001-00000104: 2,160.00 en el XML y 2,170.00 en libros (`libro-mayor.xlsx` filas 15 y 16) | 10.00 |

**Lo que no se pudo procesar:** nada, todo se procesó.

**Observación:** la sección «El resultado» del reporte salió vacía. Es como la entregó el motor y no la completé.

Las 11 preguntas de la configuración inicial, con las respuestas tomadas, están en el reporte, en la sección «Las preguntas que hizo». El reporte quedó en `estado-finanzas/20710000019-banco-ribera/cierre/2026-09/reporte-close-scan.md`. La corrida quedó registrada como `2026-10-06-close-scan-1`, con su salida en `corridas/salida-close-scan.md`.