# /criterio-budget:budget-wake 

Hoy tocaban `budget-scan`, `variance-report` y `forecast`, porque hay contabilidad nueva de 2026-01 a 2026-08. No había peticiones abiertas.

**Términos:** el motor los dio por vigentes (versión 1.2, aceptada en 0.8.0). No llamé a `/budget-setup` para registrar la aceptación a nombre de José Francisco Ñáñez, así que el registro con ese nombre no se hizo.

**Barrido:** 57 documentos, sin nuevos, cambiados, borrados, fuera de lugar ni ilegibles.

## Ejecución contra aprobado, corte 2026-08 (versión 2 del presupuesto)
- Cada línea va un 3,00 % por debajo de lo previsto al corte, salvo Nómina, que está en 0,00 %.
- **Señal:** hay 560.000,00 de gasto en la cuenta 5135, centro ZZZ, sin línea presupuestal (`2026-08/10-contabilidad/libro-mayor.csv`, fila 18).

## Proyección al cierre
- **Señal:** Tecnología · PRY-310. La proyección del área es 63.360.000,00 y lo aprobado es 57.600.000,00, una diferencia de 5.760.000,00.
- Las proyecciones calculadas por el motor no superan lo aprobado: 55.872.000,00 al ritmo y 56.448.000,00 al plan.
- Las demás líneas quedan dentro de lo aprobado.

**Preguntas sin respuesta:** nadie las contestó, así que quedaron las respuestas sugeridas.
- Se propuso la versión 2 del presupuesto, porque ningún acta dice «versión 2».
- Entran como gasto las cuentas con prefijo 51.
- El acta 06 no fija fecha del próximo comité.

El reporte completo, con tablas y fuentes, está en `estado-finanzas/900765432-almacenes-caribe/corridas/salida-budget-wake.md`.

Registré las cuatro corridas (`budget-wake`, `budget-scan`, `variance-report`, `forecast`) con el caso 2026-08.