# /criterio-budget:budget-setup finanzas/0990054321001-minera-condor

## Listo — Minera Cóndor · presupuesto 2026

**Lo que miré:** 2 versiones (v1 de 2026-01-15, v2 de 2026-06-30), contabilidad de 2026-01 a 2026-09 y 3 actas.

**Versión aprobada:** rige la v2, que es la más reciente de `10-aprobado/`. No fijé `approved_version` por mi cuenta.
- El acta 01 (2026-01-20) aprueba la v1.
- El acta 05 (2026-06-28) traslada 6,000.00 de Comercial · Publicidad a Comercial · Eventos.

**Términos:** José Francisco Ñáñez los aceptó el 2026-10-06 para la versión 0.10.0. Los comprobantes están en `.criterio/terminos/aceptacion-criterio-budget-0.10.0-2026-10-06.md` y `.pdf`.

**Lo que atender (de 8 líneas, 2 señales):**
- **Operaciones · Transporte** va +15.0 % sobre lo aprobado al corte: ejecutado 77,970.00 contra 67,800.00, una desviación de 10,170.00.
- **Administración · Mantenimiento** tiene ejecutado más comprometido en 96.0 % de lo aprobado del año, con 1,900.00 disponibles.
- Las otras seis líneas están entre 0 % y -3.0 % de desviación.

**Dos traslados sin acta:** entre la v1 y la v2, Operaciones · Transporte subió 9,600.00 y Tecnología · Licencias bajó 9,600.00. Ningún acta los aprueba. El reporte del motor no los lista en «Lo que hay que atender», así que los tomé de `resultados.json` y los puse aparte en mi salida.

**Respuestas por defecto (nadie contestó en esta prueba):**
- **Umbrales:** los de `config.example.json`: 10 %, 95 % y 45 días.
- **Comité:** sin fechas, porque el acta 06 dice «próximo comité» sin fecha.
- **Responsables de área:** no aparecen en los documentos.
- **Fichas PMO:** en `estado-pmo/records` (existe `PRY-310.json`).
- **Estado:** guardado en `estado-finanzas/0990054321001-minera-condor`.
- **Marca de la raíz:** no dejé `_CRITERIO_FINANZAS.txt`, porque nadie lo autorizó.

**Compromiso abierto:** el acta 06 encarga a Administración revisar el contrato de vigilancia antes del próximo comité.

El reporte completo está en `estado-finanzas/0990054321001-minera-condor/presupuesto/2026/reporte-variance-report.md`. La salida y la corrida quedaron registradas en `corridas/salida-budget-setup.md` (corrida `2026-10-06-budget-setup-1`).

**Cuándo vuelvo:** cuando llegue la contabilidad de un mes nuevo, antes de cada comité y una vez por semana por los compromisos.