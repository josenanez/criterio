# /criterio-budget:budget-setup finanzas/1790012345001-cooperativa-sierra-alta

## Listo — Cooperativa Sierra Alta · presupuesto 2026

La instalación quedó terminada y la corrida registrada (`2026-10-06-budget-setup-1`, 4 hallazgos). La configuración está en `.criterio/presupuesto/1790012345001/config.json`.

**Lo que miré:** 2 versiones (v1 del 2026-01-15, v2 del 2026-06-30) · contabilidad de 2026-01 a 2026-09 · 3 actas.

**Versión aprobada:** el motor toma la 2 como vigente, pero ningún acta la nombra.
- El acta 01 (2026-01-20) aprueba la v1.
- El acta 05 (2026-06-28) aprueba un traslado de 3,000.00 de Publicidad a Eventos. Eso coincide con la diferencia entre v1 y v2.
- Alguien debería confirmar que la v2 es la aprobada.

**Términos:** José Francisco Ñáñez los aceptó el 2026-10-06 (términos 1.2, versión 0.8.0). El comprobante está en `.criterio/terminos/` en Markdown y PDF.

**Las preguntas:** nadie respondió, así que tomé la respuesta sugerida por los documentos.
- **Responsables de las áreas:** no aparecen en ningún documento.
- **Fechas del comité:** tampoco aparecen, así que quedó vacío.
- **Umbrales:** usé los de `config.example.json`.
- **Fichas PMO:** `estado-pmo/records`, donde existe `PRY-310.json`.
- **Moneda y marco contable:** puse USD y NIIF por ser un RUC de Ecuador. Es un supuesto mío; ningún documento lo dice.
- **Archivo `_CRITERIO_FINANZAS.txt`:** no lo dejé en la carpeta de documentos, porque nadie lo autorizó.

**Lo que muestra la ejecución al corte 2026-09** (cifras tal como las da el motor):
- Todas las líneas están 3.00 % por debajo de lo previsto al corte, salvo Personal · Nómina, que está en 0.00.
- Tecnología · Licencias tiene ejecutado más comprometido en el 96.0 % de lo aprobado del año. Quedan disponibles 2,390.00. Es la única señal que el reporte lista.

**Otras señales que calculó el motor:** el reporte no las incluye, así que las agregué a mano arriba de la tabla en la salida guardada.
- **Versión desactualizada:** `proyeccion-comercial-2026-09-30.csv` usa la v1 para Publicidad y Eventos, y la vigente es la 2.
- **Proyección vencida:** la de Operaciones · Transporte es del 2026-07-15, hace 83 días.
- **Compromiso abierto:** el acta 06 encarga a Administración revisar el contrato de vigilancia antes del próximo comité. No hay evidencia de que se haya hecho.

El reporte completo está en `estado-finanzas/1790012345001-cooperativa-sierra-alta/presupuesto/2026/reporte-variance-report.md`. Lo que te mostré aquí está guardado en `corridas/salida-budget-setup.md` de la misma carpeta de estado.

**Cuándo vuelvo:** cuando llegue la contabilidad de un mes nuevo, antes de cada comité y una vez por semana por los compromisos.