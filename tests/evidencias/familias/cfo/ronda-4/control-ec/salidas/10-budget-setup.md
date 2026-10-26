# /criterio-budget:budget-setup finanzas/1790000001001-comercial-control

Quedó instalado Tomás sobre Comercial Control (presupuesto 2026, corte 2026-09). El reporte de ejecución contra lo aprobado salió sin señales.

Ajusté la salida del reporte: puse un resumen antes del encabezado y retiré la tabla de periodos individuales.

**Lo que miré:** 2 versiones del presupuesto (v1 del 2026-01-15, v2 del 2026-06-30), contabilidad de 2026-01 a 2026-09 y 3 actas.

**Versión aprobada:** la 2, que es la más reciente de `10-aprobado/`. La v1 la aprueba el acta 01 del 2026-01-20. El acta 05 del 2026-06-28 aprueba el traslado de 4,500.00 de Comercial · Publicidad a Comercial · Eventos, de julio a diciembre. No fijé `budget.approved_version` por mi cuenta.

**Términos:** aceptados para la versión 0.10.0 a nombre de José Francisco Ñáñez, con fecha 2026-10-06. Los comprobantes en Markdown y PDF están en `.criterio/terminos/`.

**Lo que decidí en lugar de la persona:**
- **Mapeo de cuentas:** usé `mapeo-presupuesto.csv` de `00-referencia/`.
- **Gastos:** el prefijo de cuentas de gasto es `51`.
- **Umbrales:** los tomé de `config.example.json`: desviación 10 %, comprometido 95 % y proyección vencida a los 45 días. Son configuración, no norma.
- **Fichas de proyectos:** encontré `estado-pmo/records/` con `PRY-310.json` y lo dejé como `pmo_records`.
- **Responsables de área:** ningún documento los dice. Los dejé vacíos y quedó anotado en las preguntas del reporte.
- **Fechas de comité:** no hay ninguna fecha futura en los documentos. La lista quedó vacía.
- **Marca de la carpeta:** no dejé `_CRITERIO_FINANZAS.txt`, porque nadie lo autorizó.

**Resultado:**

| Área | Línea | Aprobado | Al corte | Ejecutado | Comprometido | Disponible | Desviación | % |
|---|---|---|---|---|---|---|---|---|
| Administración | Mantenimiento | 36,000.00 | 27,000.00 | 26,190.00 | 900.00 | 8,910.00 | -810.00 | -3.00 |
| Administración | Servicios públicos | 54,000.00 | 40,500.00 | 39,285.00 | 1,350.00 | 13,365.00 | -1,215.00 | -3.00 |
| Comercial | Eventos | 31,500.00 | 22,500.00 | 21,825.00 | 900.00 | 8,775.00 | -675.00 | -3.00 |
| Comercial | Publicidad | 67,500.00 | 51,750.00 | 50,197.50 | 1,575.00 | 15,727.50 | -1,552.50 | -3.00 |
| Operaciones | Transporte | 63,000.00 | 47,250.00 | 45,832.50 | 1,575.00 | 15,592.50 | -1,417.50 | -3.00 |
| Tecnología | Licencias | 90,000.00 | 67,500.00 | 65,475.00 | 2,250.00 | 22,275.00 | -2,025.00 | -3.00 |
| Tecnología | PRY-310 | 108,000.00 | 81,000.00 | 78,570.00 | 2,700.00 | 26,730.00 | -2,430.00 | -3.00 |
| Personal | Nómina | 360,000.00 | 270,000.00 | 270,000.00 | 9,000.00 | 81,000.00 | 0.00 | 0.00 |

Una primera corrida de `compute` dio dos señales `transfer_without_approval`. Desaparecieron al registrar en la ficha el acta 05 con su traslado. Ya no hay señales abiertas ni documentos sin procesar.

**Compromiso abierto del comité:** el acta 06 (2026-09-10) dice que Administración revisa el contrato de vigilancia antes del próximo comité. Sigue abierto, sin evidencia.

**Dónde quedó todo:**
- Configuración: `.criterio/presupuesto/1790000001001/config.json`
- Ficha: `estado-finanzas/1790000001001-comercial-control/presupuesto/2026/ficha.json`
- Reporte: `estado-finanzas/1790000001001-comercial-control/presupuesto/2026/reporte-variance-report.md`
- Salida de la corrida: `estado-finanzas/1790000001001-comercial-control/corridas/salida-budget-setup.md`, con la corrida registrada como `2026-10-06-budget-setup-1`.

Tomás vuelve cuando llegue la contabilidad de un mes nuevo, antes de cada comité y una vez por semana por los compromisos.