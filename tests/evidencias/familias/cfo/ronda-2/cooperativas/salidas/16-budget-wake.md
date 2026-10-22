# /criterio-budget:budget-wake 

Hoy tocaban `budget-scan`, `variance-report` y `forecast`, porque llegó contabilidad nueva de 2026-01 a 2026-08. No había peticiones abiertas, y los términos (versión 1.2) estaban vigentes.

El barrido de `inventario` revisó 53 archivos y no encontró nuevos, cambiados, borrados ni fuera de lugar. El cierre de ese barrido es de 2026-08 y no mira 2026-09.

**Ejecución contra aprobado, corte 2026-08, versión 2 del presupuesto**
- El reporte no tiene nada abierto.
- Siete de las ocho líneas van un 3,00 % por debajo de lo aprobado al corte.
- Nómina va exacta, con desviación 0,00.

**Proyección al cierre**
El reporte marca tres señales:
- **Comercial · Eventos:** la proyección del área usa la versión 1 del presupuesto y la aprobada es la 2 (fila 3 de `proyeccion-comercial-2026-09-30.csv`).
- **Comercial · Publicidad:** misma diferencia de versión, en la fila 2 del mismo archivo.
- **Operaciones · Transporte:** la proyección del área es del 2026-07-15, hace 83 días, y el umbral configurado es de 45.

**Preguntas sin documento:** nadie respondió, así que el motor dejó vacías las fechas del comité y los responsables de las áreas (ningún documento los trae).

El acta 05 (2026-06-28) aprueba un traslado de 3,000.00 que coincide con la versión 2, pero ningún acta nombra esa versión.

`budget-committee-pack` no tocaba hoy. Los reportes completos están en `reporte-variance-report.md` y `reporte-forecast.md`, y dejé la salida entera en `estado-finanzas/1790012345001-cooperativa-sierra-alta/corridas/salida-budget-wake.md`.

Registré la corrida de `budget-wake` y las de `budget-scan`, `variance-report` y `forecast`, todas con `--caso 2026-08`.