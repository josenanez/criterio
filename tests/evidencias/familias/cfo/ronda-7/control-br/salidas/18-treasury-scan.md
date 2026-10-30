# /criterio-treasury:treasury-scan 

Corrí el escaneo de tesorería de Comercial Controle Paulista (40217355000151) para el periodo 2026-09, y no hay nada nuevo que atender. No cargué ni leí ningún documento fuente; todo lo calculó el motor. Los términos (versión 1.3) ya estaban vigentes, así que no hizo falta registrar una aceptación.

- **Inventario:** hay 66 archivos y ninguno es nuevo, cambiado, borrado, ilegible ni está fuera de lugar. El inventario no distingue qué archivos son extractos, programa de pagos o flujo, así que no puedo decir cuáles revisó el cálculo.
- **Cálculo:** el motor no encontró señales (total 0). Lo que no pudo procesar es 0.
- **Reporte:** el motor lo generó con las secciones "Lo que hay que atender" y "Lo que no se pudo procesar" vacías. "El resultado" y "Fuentes" salieron sin contenido ("Sin documentos citados"). No puedo asegurar si eso significa que no había nada que reportar o que el motor no leyó los archivos de `60-tesoreria` (hay 2); esa parte conviene que la revise quien aprueba (Sofia Leão).
- **Corrida registrada:** quedó como `2026-10-06-treasury-scan-1`, con 0 hallazgos. Copié el reporte tal cual a `corridas/salida-treasury-scan.md`, dentro de la carpeta de estado de la entidad.

Usé `--today 2026-10-06` en cada llamada y tomé 2026-09 como último periodo con datos. El reporte quedó en `tesoreria/2026-09/reporte-treasury-scan.md`, también dentro de esa carpeta de estado.