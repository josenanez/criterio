# /criterio-finance:close-scan 

Primera corrida de close-scan: 65 archivos nuevos, ninguno cambiado ni borrado, y 6 señales abiertas. No hay corrida anterior con la que comparar.

Los términos ya estaban vigentes y aceptados a nombre de José Francisco Ñáñez el 2026-10-06, así que no volví a registrarlos. No encontré archivos fuera de lugar ni ilegibles. Convertí los documentos de `40-soportes` y `50-auditoria`. La ficha ya traía la declaración del correo de Sofía León del 2026-10-05, que dice que el cierre está cerrado. Los requerimientos R-01 a R-05 vienen en la tabla del auditor, y Paraguay no lleva facturas en la ficha, así que no extraje nada más.

Las 6 señales:
1. **Cierre declarado contra evidencia:** el correo dice «cerrado» y hay 5 señales abiertas que ese estado no explica.
2. **Banco `andino-13701`:** una consignación en tránsito del 2026-09-30 por 71.500.000,00 (001-001-0000107) sin su movimiento en el extracto.
3. **Compra sin factura electrónica:** el documento 002-001-0000202, por 33.950.000,00, está en el libro mayor pero no hay factura en `recibidas/`.
4. **Factura duplicada:** la 001-001-0000102 (27.500.000,00) aparece en dos archivos con el mismo CDC. Uno es la versión reenviada.
5. **Factura recibida fuera de su autorización:** la 002-001-0000201 (21.340.000,00) se emitió el 2026-09-07, antes de que empezara la vigencia de su timbrado el 2026-09-10. SIFEN la rechaza (validación 1103).
6. **Requerimiento sin responder:** R-05, contratos de los proveedores principales (responsable Jorge Vela), venció el 2026-10-02 y lleva 4 días vencido.

El reporte quedó en `estado-finanzas/88612904-4-distribuidora-del-ybytyruzu-sintetica/cierre/2026-09/reporte-close-scan.md`. Lo que te mostré quedó guardado en `corridas/salida-close-scan.md` de esa misma carpeta y la corrida quedó registrada como `2026-10-06-close-scan-1`.