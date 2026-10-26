# /criterio-finance:close-scan 

2 archivos nuevos (los auxiliares 1305-clientes y 2205-proveedores de 2026-08), 1 cambiado (`00-referencia/politica-tesoreria.csv`) y 0 borrados. Hay 8 señales abiertas en 2026-09. Los tres son tablas que procesa el motor, así que no hubo documento escrito nuevo que extraer. Nada está fuera de su lugar.

Los términos (versión 1.2) ya estaban vigentes, así que no hubo que registrar otra aceptación.

**Lo que hay que atender en 2026-09:**
1. **Cuenta 2505:** el mayor y el balance difieren en -120.000,00.
2. **Cuenta 5195:** el mayor y el balance difieren en 120.000,00. Es el mismo monto que en 2505 con signo opuesto.
3. **Estado del cierre:** el correo del 2026-10-05 lo declara cerrado, pero hay 7 señales abiertas que ese estado no explica.
4. **Banco andino-3701:** consignación en tránsito del 2026-09-30 por 8.330.000,00 (SETP99000102 aparte, esta es SETP99000107).
5. **CUFE repetido:** SETP99000102 aparece en dos archivos, el original y el `-reenviada`, por 8.330.000,00.
6. **Factura SETP77000201:** registrada en dos asientos (C-021 y C-022) por 3.104.000,00.
7. **Factura SETP77000201:** el XML trae base 1.552.000,00 e IVA 294.880,00; los libros tienen 3.104.000,00 y 589.760,00.
8. **Cuenta 2205:** no hay auxiliar del periodo para conciliarla.

La sección "El resultado" del reporte salió vacía; la dejé tal cual. Una de las respuestas del reporte es un supuesto por confirmar: el marco contable (grupo 1) no lo dice ningún documento.

El reporte quedó en `estado-finanzas/900765432-almacenes-caribe/cierre/2026-09/reporte-close-scan.md`. Lo que te mostré lo guardé en `estado-finanzas/900765432-almacenes-caribe/corridas/salida-close-scan.md` y registré la corrida como `2026-10-06-close-scan-2`.