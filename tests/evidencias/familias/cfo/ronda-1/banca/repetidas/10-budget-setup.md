# /criterio-budget:budget-setup finanzas/900123456-banco-andino

## Listo — Banco Andino (900123456) · presupuesto 2026

La instalación quedó hecha y la corrida registrada. Nadie respondió preguntas en esta sesión, así que tomé las respuestas sugeridas a partir de los documentos.

**Lo que miré:**
- Dos versiones del presupuesto: v1 del 2026-01-15 y v2 del 2026-06-30.
- Contabilidad de 2026-01 a 2026-09.
- Tres actas.

**Versión aprobada:**
- El acta 01 (2026-01-20) aprueba la versión 1.
- El acta 05 (2026-06-28) aprueba un traslado de 3.000.000 de Comercial · Publicidad a Comercial · Eventos.
- Ningún acta dice que apruebe la v2 como tal. El motor la usa como vigente porque es la más reciente.

**Términos:** aceptados a nombre de José Francisco Ñáñez para la versión 0.7.0 (términos 1.2). El comprobante está en `.criterio/terminos/aceptacion-criterio-budget-0.7.0-2026-10-06.md`.

**Lo que tomé por defecto:**
- Umbrales del ejemplo: desviación 10 %, comprometido 95 %, proyección vencida a los 45 días.
- Comité el 2026-10-15.
- Fichas PMO en `estado/records`.
- Estado en `estado-finanzas/900123456-banco-andino`.
- Aprobador: Contralor.

No dejé el archivo `_CRITERIO_FINANZAS.txt` en la carpeta, porque nadie lo autorizó.

**Lo que encontré** (corte 2026-09):
1. **Administración · Servicios públicos:** ejecutado 31.050.000,00 contra 27.000.000,00 aprobado al corte (+15,0 %, 4.050.000,00 sobre lo aprobado).
2. **Administración dice que va dentro del presupuesto** (correo del 2026-10-01), y esa línea no lo sostiene.
3. **Las demás siete líneas están en −3,0 % o 0,0 %.**
4. **Hay 2 señales de traslado sin aprobación.** El cálculo las levantó, pero el reporte no las lista. Se ven con `transfer-log`.

El reporte completo, con la tabla por área y línea, está en `estado-finanzas/900123456-banco-andino/presupuesto/2026/reporte-variance-report.md`.

Escribí la ficha del presupuesto (`ficha.json`) con las dos actas, el correo de Administración y el compromiso del acta 06: Administración revisa el contrato de vigilancia antes del próximo comité.

Lo que mostré tal cual quedó en `estado-finanzas/900123456-banco-andino/corridas/salida-budget-setup.md`, y la corrida se registró como `2026-10-06-budget-setup-1`.

**Cuándo vuelvo:** cuando llegue la contabilidad de un mes nuevo, antes de cada comité y una vez por semana por los compromisos.