# /criterio-finance:close-scan 

Primera corrida de close-scan: 66 archivos nuevos, 0 cambiados y 0 borrados, con 6 señales. Todas son nuevas porque no había una corrida anterior de este comando.

Los términos 1.3 estaban vigentes, aceptados por José Francisco Ñáñez el 2026-10-06. Convertí los 10 documentos escritos de `40-soportes` y `50-auditoria`. La ficha ya traía el estado declarado ("en curso", Sofía León, 2026-10-05) y el requerimiento R-09 de la carta del auditor, así que no hubo nada nuevo que extraer.

Las 6 señales del periodo 2026-09:

1. **Cuenta 5305 (dos señales):** el mayor no coincide con el balance de comprobación. El mayor suma 0,00 en débitos y créditos, y el balance dice 5.000,00 en débitos.
2. **Balance de comprobación:** los débitos suman 241.863.410,00 y los créditos 241.858.410,00, con una diferencia de 5.000,00. Es la misma diferencia de la cuenta 5305.
3. **Checklist:** la tarea C-02 (conciliar cada cuenta bancaria) figura cumplida, pero no hay soporte que empiece por C-02. El responsable es Andrés Paz.
4. **Banco andino-10101:** hay una nota débito del 2026-09-30 por -400.000,00 en el extracto, sin registro en libros.
5. **Factura 00100001010000000104:** el IVA es 552.500,00 en el XML y 552.510,00 en libros, una diferencia de 10,00.

La sección "El resultado" salió vacía del motor y la dejé así, sin completarla. El reporte completo está en `cierre/2026-09/reporte-close-scan.md`.

La corrida quedó registrada con el id `2026-10-06-close-scan-1`. Lo que te mostré está guardado en `corridas/salida-close-scan.md`.