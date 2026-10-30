# /criterio-budget:budget-setup finanzas/30702173554-comercial-control-del-plata

La instalación de Tomás para Comercial Control del Plata quedó lista y la corrida quedó registrada. Falta una cosa: en este mensaje no te muestro la tabla completa, que está en el archivo de salida.

**Lo que miré:** 2 versiones del presupuesto, contabilidad de 2026-01 a 2026-09 y 3 actas.

**Versión aprobada:** la vigente es la 2, del 2026-06-30. Nace del traslado del acta 05 (2026-06-28), que mueve 3.600.000,00 de Comercial · Publicidad a Comercial · Eventos. El acta 01 (2026-01-20) aprueba la versión 1.

**Términos:** José Francisco Ñáñez los aceptó para la versión 1.0.0 (términos 1.3, fecha 2026-10-06). Los comprobantes en Markdown y PDF están en `.criterio/terminos/`.

**Ejecución al corte 2026-09:**
- Las 8 líneas quedan en 0 % o −3,00 % contra lo aprobado al corte, muy por debajo del umbral de 10 %.
- El motor no levantó ninguna señal ni `record_issues`.
- La nómina de Personal ejecuta exactamente lo previsto, con desviación 0,00.
- Administración dijo en su correo del 2026-10-01 que va dentro del presupuesto, y las cifras lo sostienen.

**Pendientes:**
- El compromiso del acta 06 (Administración revisa el contrato de vigilancia antes del próximo comité) sigue abierto, sin evidencia.
- No hay fechas de comité en los documentos, así que `committee_dates` quedó vacío.
- No dejé la marca `_CRITERIO_FINANZAS.txt` en la carpeta de documentos. Nadie autorizó escribir ahí y no había quién respondiera.
- Los umbrales (10 %, 95 %, 45 días) son los de `config.example.json`. Son configuración, no norma.

**Cómo se configuró:**
- Los datos de la entidad vienen de la configuración de finanzas que ya existía.
- La configuración quedó en `.criterio/presupuesto/30702173554/config.json`.
- Las fichas de proyectos PMO se buscan en `estado-pmo/records`, donde existe `PRY-310.json`.
- Tomé `51` como prefijo de gastos (sale de las cuentas 5135, 5145 y 5195 del mapeo).

No pregunté nada a nadie. Las cuatro respuestas de la ficha salen de los documentos y de la configuración de finanzas. No medí los minutos hasta el primer resultado, y la nota de la corrida lo dice.

Archivos en `<espacio>/estado-finanzas/30702173554-comercial-control-del-plata/`:
- `corridas/salida-budget-setup.md`: lo que te mostré, completo, con la tabla por área y línea
- `presupuesto/2026/reporte-variance-report.md`: el reporte del motor
- `presupuesto/2026/ficha.json`: la ficha con las actas, la declaración de Administración y el compromiso del comité

Tomás vuelve cuando llegue la contabilidad de un mes nuevo, antes de cada comité y una vez por semana por los compromisos.