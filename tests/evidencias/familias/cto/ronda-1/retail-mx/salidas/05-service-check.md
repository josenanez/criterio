# /criterio-changes:service-check 

Corrí `service-check` para el periodo 2026-11, pero el reporte salió con la tabla de servicios vacía. No hay ningún servicio con su nivel ni su disponibilidad.

El reporte tampoco trae nada que atender, y dice que todo lo que llegó se procesó. Con la tabla vacía, eso quiere decir que no se leyó ningún servicio, no que todos cumplan. Faltan datos en la carpeta de tecnología: el catálogo con los niveles acordados o la disponibilidad del periodo. Si el catálogo y la disponibilidad ya están ahí, el motor no los reconoció, y conviene correr `/criterio-changes:changes-setup` para revisarlo.

Los términos (versión 1.6) ya estaban aceptados, así que no registré una aceptación nueva con el nombre de José Francisco Ñáñez. Pasé `--today 2026-11-25` a todas las llamadas que lo aceptan.

**Archivos**
- **Reporte:** `estado-tecnologia/rgs180610qw4-retail-del-golfo-sintetico/cambios/2026-11/reporte-service-check.md`.
- **Salida registrada:** `estado-tecnologia/rgs180610qw4-retail-del-golfo-sintetico/corridas/salida-service-check.md`.
- **Corrida:** quedó registrada como `2026-11-25-service-check-1`. El motor indicó 18 hallazgos en ella; no sé de dónde salen, porque el reporte no muestra ninguno.