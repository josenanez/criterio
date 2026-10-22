# /criterio-budget:budget-setup finanzas/0990054321001-minera-condor

## Listo — Minera Cóndor · presupuesto 2026

Instalé el presupuesto de Minera Cóndor y calculé la ejecución al corte 2026-09. El resultado quedó con tres puntos que revisar antes del comité.

**Lo que miré:** 2 versiones del presupuesto (v1 del 2026-01-15 y v2 del 2026-06-30), contabilidad de 2026-01 a 2026-09 y 3 actas.

**Versión aprobada:** la 1, con el acta 01 del 2026-01-20. El motor tomó como vigente la 2, que no tiene acta que la apruebe. El acta 05 solo aprueba un traslado de 6,000.00 de Publicidad a Eventos.

**Términos:** José Francisco Ñáñez los aceptó el 2026-10-06 (versión 0.8.0, términos 1.2). Los comprobantes quedaron en `.criterio/terminos/aceptacion-criterio-budget-0.8.0-2026-10-06.md` y `.pdf`.

**Lo que hay que atender:**
1. **Operaciones · Transporte** va 15.0 % por encima de lo aprobado al corte: 77,970.00 ejecutado contra 67,800.00, una diferencia de 10,170.00.
2. **Administración · Mantenimiento** tiene ejecutado más comprometido en 96.0 % de lo aprobado del año; le quedan 1,900.00 disponibles.
3. **Dos traslados entre v1 y v2 no tienen acta:** Transporte +9,600.00 y Licencias −9,600.00. El reporte `variance-report` no los muestra en su tabla de atención. Salen en el resultado del motor y en la salida de esta sesión.

Las demás líneas van 3 % por debajo del aprobado al corte, salvo Nómina, que está exactamente en lo aprobado.

**Lo que decidí sin preguntar a nadie (sesión sin interfaz):**
- Usé los umbrales de `config.example.json` (desviación 10 %, comprometido 95 %, proyección vencida 45 días). Son configuración, no norma.
- Tomé a Sofía León como quien aprueba, de la configuración de Clara.
- Las fichas PMO están en `estado-pmo/records` (solo `PRY-310.json`).
- No hay fechas de comité en los documentos, así que ese campo quedó vacío.
- No dejé el archivo `_CRITERIO_FINANZAS.txt` en la carpeta de documentos, porque nadie lo autorizó.

**Lo que no hice:** no medí los minutos hasta el primer resultado.

**Dónde quedó todo:**
- Configuración: `.criterio/presupuesto/0990054321001/config.json`
- Ficha con las actas: `estado-finanzas/0990054321001-minera-condor/presupuesto/2026/ficha.json`
- Reporte: `estado-finanzas/0990054321001-minera-condor/presupuesto/2026/reporte-variance-report.md`
- Salida de la sesión: `estado-finanzas/0990054321001-minera-condor/corridas/salida-budget-setup.md`
- Corrida registrada como `2026-10-06-budget-setup-1`.

Vuelvo cuando llegue la contabilidad de un mes nuevo, antes de cada comité y una vez por semana por los compromisos.