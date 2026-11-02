# /criterio-budget:budget-setup finanzas/88457812-7-banco-del-tebicuary-sintetico

## Listo — Banco del Tebicuary (sintético) · presupuesto 2026

**Lo que miré:**
- Dos versiones del presupuesto: v1 del 2026-01-15 y v2 del 2026-06-30.
- Contabilidad de 2026-01 a 2026-09.
- Tres actas.

**Versión aprobada:** rige la v2, la más reciente de `10-aprobado/`.
- El acta 01 (2026-01-20) aprueba la v1.
- El acta 05 (2026-06-28) traslada 45,000,000.00 de Comercial · Publicidad a Comercial · Eventos.

**Términos:** ya estaban aceptados para la versión 1.2.0 por José Francisco Ñáñez el 2026-10-06, así que no registré una aceptación nueva. El comprobante está en `.criterio/terminos/`.

**Configuración:** ya existía en `.criterio/presupuesto/88457812-7/config.json` y valida sin problemas, así que no la reescribí. En cada pregunta usé la respuesta sugerida a partir de los documentos:
- Los umbrales son los del ejemplo: 10 %, 95 % y 45 días.
- No hay fechas de comité en los documentos, y las dejé vacías.
- Las fichas PMO están en `estado-pmo/records` (`PRY-310.json`).
- No marqué la carpeta con `_CRITERIO_FINANZAS.txt`, porque nadie dio un sí.

**Lo que atender, al corte 2026-09:**
- **Administración · Servicios públicos:** se aparta del presupuesto +15,0 %. Se ejecutaron 465.750.000,00 contra 405.000.000,00 aprobados al corte.
- **El correo de Administración:** dice que el área está dentro del presupuesto, y los números no lo sostienen en esa línea (60.750.000,00).
- **El resto de las líneas:** quedan 3,0 % por debajo de lo aprobado al corte, salvo Nómina, que queda exacta.

**Señales sin mostrar:** el motor calculó 4 señales, pero el reporte muestra solo 2. Las 2 de `transfer_without_approval` no aparecen en él. No las revisé, y `transfer-log` es el comando que las muestra.

El reporte completo está en `estado-finanzas/88457812-7-banco-del-tebicuary-sintetico/presupuesto/2026/reporte-variance-report.md`. Lo que te mostré quedó en `corridas/salida-budget-setup.md` y la corrida quedó registrada.

**Cuándo vuelvo:** cuando llegue la contabilidad de un mes nuevo, antes de cada comité y una vez por semana por los compromisos.