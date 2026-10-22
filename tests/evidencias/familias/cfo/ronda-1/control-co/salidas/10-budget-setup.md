# /criterio-budget:budget-setup finanzas/900000001-distribuidora-control

Soy Tomás. Dejé instalado el presupuesto de Distribuidora Control, y el motor ya calculó la ejecución contra lo aprobado.

El motor marcó 2 señales `transfer_without_approval` (traslado sin acta). El reporte de ejecución no las muestra, porque las trata `/transfer-log`. Ahí hay que mirarlas.

## Listo — Distribuidora Control · presupuesto 2026

**Lo que miré:** 2 versiones (v1 de 2026-01-15 y v2 de 2026-06-30), contabilidad de 2026-01 a 2026-09 y 3 actas.

**Versión aprobada:** la 2, con el acta 05 (2026-06-28): «Se aprueba trasladar 1,500,000.00 de Comercial · Publicidad a Comercial · Eventos, de julio a diciembre.» La v2 refleja ese traslado.

**Términos:** José Francisco Ñáñez los aceptó para la versión 0.7.0 (términos 1.2). El comprobante en Markdown y PDF queda en `.criterio/terminos/aceptacion-criterio-budget-0.7.0-2026-10-06.md` y `.pdf`.

**Ejecución al corte 2026-09** (copiada del reporte del motor):

| Área | Línea | Aprobado | Al corte | Ejecutado | Comprometido | Disponible | Desviación | % |
|---|---|---|---|---|---|---|---|---|
| Administración | Mantenimiento | 12.000.000,00 | 9.000.000,00 | 8.730.000,00 | 300.000,00 | 2.970.000,00 | -270.000,00 | -3,00 |
| Administración | Servicios públicos | 18.000.000,00 | 13.500.000,00 | 13.095.000,00 | 450.000,00 | 4.455.000,00 | -405.000,00 | -3,00 |
| Comercial | Eventos | 10.500.000,00 | 7.500.000,00 | 7.275.000,00 | 300.000,00 | 2.925.000,00 | -225.000,00 | -3,00 |
| Comercial | Publicidad | 22.500.000,00 | 17.250.000,00 | 16.732.500,00 | 525.000,00 | 5.242.500,00 | -517.500,00 | -3,00 |
| Operaciones | Transporte | 21.000.000,00 | 15.750.000,00 | 15.277.500,00 | 525.000,00 | 5.197.500,00 | -472.500,00 | -3,00 |
| Tecnología | Licencias | 30.000.000,00 | 22.500.000,00 | 21.825.000,00 | 750.000,00 | 7.425.000,00 | -675.000,00 | -3,00 |
| Tecnología | PRY-310 | 36.000.000,00 | 27.000.000,00 | 26.190.000,00 | 900.000,00 | 8.910.000,00 | -810.000,00 | -3,00 |
| Personal | Nómina | 120.000.000,00 | 90.000.000,00 | 90.000.000,00 | 3.000.000,00 | 27.000.000,00 | 0,00 | 0,00 |

Todo lo que llegó se procesó. El reporte completo quedó en `estado-finanzas/900000001-distribuidora-control/presupuesto/2026/reporte-variance-report.md`.

**Respuestas tomadas de los documentos** (nadie podía contestar):
- **Configuración:** quedó en `.criterio/presupuesto/900000001/config.json`. Tomé entidad, aprobador (Sofía León) y cuentas de gasto (51 y 52) de la configuración de finanzas que ya existía.
- **Umbrales:** los de `config.example.json` (10 %, 95 %, 45 días). Son configuración, no norma.
- **Comité:** no encontré fechas en los documentos, así que dejé la lista vacía.
- **Fichas PMO:** encontré `estado-pmo/records` y lo usé como ruta.
- **Marca de la raíz:** no dejé `_CRITERIO_FINANZAS.txt`, porque nadie lo autorizó y es lo único que se escribe dentro de los documentos.

**Registro:** la corrida quedó registrada como `2026-10-06-budget-setup-1`. La salida completa está en `estado-finanzas/900000001-distribuidora-control/corridas/salida-budget-setup.md`.

**Cuándo vuelvo:** cuando llegue la contabilidad de un mes nuevo, antes de cada comité y una vez por semana por los compromisos.