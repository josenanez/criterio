# /criterio-budget:budget-wake 

Hoy tocaban `budget-scan`, `variance-report` y `forecast`, y los tres corrieron con corte 2026-09. Había contabilidad nueva (2026-01 a 2026-08) y ninguna petición abierta. Los términos de la versión 1.2 ya estaban vigentes, aceptados a nombre de José Francisco Ñáñez el 2026-10-06.

**Barrido (`budget-scan`):** encontró 2 archivos nuevos fuera de la estructura de carpetas: `reporte-budget-committee-pack.md` y `resultados.json`. El `.json` no se pudo leer porque el formato no está soportado. Nada más cambió ni se borró.

**Ejecución contra aprobado (`variance-report`):**
- **Servicios públicos (Administración):** se pasa del presupuesto. Lleva 31.050.000,00 ejecutados contra 27.000.000,00 aprobados al corte, 4.050.000,00 por encima (+15,0 %). Supera el umbral configurado del 10 %.
- **Declaración del área:** Administración se reporta dentro del presupuesto en su correo, pero esa línea no lo sostiene.
- **Resto de líneas:** todas están entre 0 % y -3 % de desviación.
- **Versión aprobada:** el acta 01 aprueba la versión 1. El acta 05 aprueba un traslado y existe la versión 2 del 2026-06-30, pero ningún acta la aprueba como tal. Esa es la respuesta sugerida que tomé de los documentos para la única pregunta que hizo el motor.

**Proyección al cierre (`forecast`):** no deja nada abierto. En Servicios públicos, la proyección al ritmo da 41.400.000,00 y la proyección al plan 40.050.000,00. Ambas superan los 36.000.000,00 aprobados. La proyección de Administración para esa línea es de 35.280.000,00.

**Registro:** dejé lo mostrado completo en `estado-finanzas/900123456-banco-andino/corridas/salida-budget-wake.md`. Registré las cuatro corridas (`budget-wake`, `budget-scan`, `variance-report` y `forecast`) con `--caso 2026-09`.