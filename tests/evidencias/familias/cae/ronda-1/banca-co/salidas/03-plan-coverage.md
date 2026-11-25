# /criterio-audit-plan:plan-coverage 

Los términos están vigentes (versión 1.6), así que la corrida siguió. No se le preguntó nada a nadie. El reporte es del periodo 2026-11, con corte al 2026-11-24, y quedó registrado como `2026-11-24-plan-coverage-1`.

**Lo que hay que atender (5 señales)**
1. **R-06 · Pérdida de información de clientes:** está calificado Crítico y ningún trabajo del plan lo cubre.
2. **U-03 · Tesorería:** su último trabajo fue el 2023-03-10, su ciclo de 24 meses venció el 2025-03-10 y no está en el plan. Van 624 días.
3. **U-10 · Canales físicos:** no tiene ningún trabajo registrado, no está en el plan y su ciclo es de 36 meses.
4. **Evaluación de riesgos vencida:** es del 2025-09-15 y tiene 435 días. La norma 9.4 la pide al menos una vez al año, y el reporte da 70 días en la columna de días de esa señal.
5. **Riesgo de fraude:** el plan no lo considera y no dice por qué (norma 9.4). El gobierno de TI y los programas de cumplimiento y ética sí están considerados.

Los otros cinco riesgos altos o críticos (R-01 a R-04) tienen un trabajo en el plan.

**Dónde quedó**
- El reporte completo está en `estado-auditoria/901777321-banco-andino-sintetico/plan/2026-11/reporte-plan-coverage.md`.
- Copié ese reporte sin cambios como `corridas/salida-plan-coverage.md` y registré la corrida con él.
- El motor registró 10 hallazgos en la corrida.

**Dos observaciones**
- **Aceptación de términos:** no la registré a nombre de José Francisco Ñáñez. El comando de términos mostró que ya estaban vigentes y aceptados en la versión 0.1.0, así que no hizo falta aceptarlos de nuevo.
- **Fecha de corte:** pasé `--today 2026-11-24` en cada llamada que la acepta.

Qué se audita lo decide el responsable de auditoría con el consejo. El reporte solo dice qué queda sin cubrir.