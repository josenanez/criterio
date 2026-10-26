# /criterio-budget:budget-setup finanzas/900123456-banco-andino

## Listo — Banco Andino · presupuesto 2026

La instalación quedó terminada y vi la primera ejecución contra lo aprobado, con corte a 2026-09.

**Lo que miré:** 2 versiones del presupuesto (v1 del 2026-01-15 y v2 del 2026-06-30), contabilidad de 2026-01 a 2026-09 y 3 actas.

**Versión aprobada:** rige la v2, que es la más reciente de `10-aprobado/`.
- El acta 01 (2026-01-20) aprueba la v1.
- El acta 05 (2026-06-28) aprueba solo el traslado de Publicidad a Eventos por 3.000.000.

**Términos:** José Francisco Ñáñez los aceptó el 2026-10-06 para la versión 0.10.0. El comprobante está en `.criterio/terminos/aceptacion-criterio-budget-0.10.0-2026-10-06.md` y en el `.pdf` del mismo nombre.

**Lo que hay que atender:**
1. **Servicios públicos:** el área de Administración dice que va dentro del presupuesto (correo del 2026-10-01). Esta línea tiene ejecutado 31.050.000,00 contra 27.000.000,00 aprobado al corte, es decir +15,0 %, por encima del umbral de 10 %. Son dos señales sobre la misma línea.
2. **PRY-310:** la ficha del proyecto dice 64.800.000,00 y el área tiene asignado 72.000.000,00, una diferencia de 7.200.000,00.
3. **Dos traslados sin acta:** entre la v1 y la v2, Licencias bajó 4.800.000,00 y Transporte subió 4.800.000,00, y no hay acta que lo apruebe. El reporte no los muestra, porque son señales de traslados.
4. **Compromiso abierto del acta 06:** Administración revisa el contrato de vigilancia antes del próximo comité, que está fijado para el 2026-10-15.

Las otras 7 líneas, incluida Nómina, están dentro del umbral. Las seis con desviación van 3,0 % por debajo de lo aprobado al corte. El reporte completo, con la tabla por área y línea, está en `estado-finanzas/900123456-banco-andino/presupuesto/2026/reporte-variance-report.md`.

**Respuestas que tomé yo, sin preguntar a nadie:**
- Umbrales: 10 % de desviación, 95 % de comprometido y 45 días para una proyección vencida, los del ejemplo.
- Fecha del comité: 2026-10-15, la del ejemplo.
- Fichas PMO: `estado-pmo/records`, donde existe `PRY-310.json`.
- Estado: `estado-finanzas/900123456-banco-andino`, fuera de la carpeta de documentos.
- Aprobador: Sofía León, tomada de la configuración de la familia de cierre que ya existía.
- No fijé `budget.approved_version` por mi cuenta.

**Marca de la carpeta:** no dejé `_CRITERIO_FINANZAS.txt`, porque nadie pudo autorizarlo en esta sesión. Si quiere la marca, dígalo y la creo.

La configuración quedó en `.criterio/presupuesto/900123456/config.json`. La corrida quedó registrada como `2026-10-06-budget-setup-1`, con la salida completa en `estado-finanzas/900123456-banco-andino/corridas/salida-budget-setup.md`.

**Cuándo vuelvo:** cuando llegue la contabilidad de un mes nuevo, antes de cada comité y una vez por semana por los compromisos.