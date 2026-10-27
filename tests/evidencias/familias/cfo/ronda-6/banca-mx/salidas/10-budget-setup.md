# /criterio-budget:budget-setup finanzas/BVA150301K21-banco-valle-de-anahuac

## Listo — Banco Valle de Anáhuac (BVA150301K21) · presupuesto 2026

**Lo que miré:** 2 versiones del presupuesto · contabilidad de 2026-01 a 2026-09 (9 periodos) · 3 actas · 5 proyecciones de área · 1 archivo de compromisos
**Versión aprobada:** la 2 (`presupuesto-2026-v2-2026-06-30.csv`). La v1 la aprueba el acta 01 del 2026-01-20. La v2 nace del traslado del acta 05 del 2026-06-28, que solo cubre Comercial · Publicidad → Eventos.
**Términos:** aceptados por José Francisco Ñáñez el 2026-10-06 (versión 0.11.0, términos 1.2). El comprobante está en `.criterio/terminos/aceptacion-criterio-budget-0.11.0-2026-10-06.md` y `.pdf`.

**Los términos, tal cual:** Criterio produce borradores de trabajo, no decisiones ni asesoría. Procesa los documentos que usted le indique y dice lo que muestran; no sabe lo que se habló fuera de ellos. Puede equivocarse, y por eso cada dato viene con la cita del documento de donde salió: la verificación es suya. Sus documentos se procesan en la infraestructura de la plataforma de IA, no solo en su equipo. Cada versión se prueba antes de publicarse; garantía y responsabilidad: licencia Apache 2.0. Cada versión se acepta de nuevo y deja un comprobante en Markdown y PDF con su huella SHA-256. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

**Lo que hay que atender (4 señales):**
- **Servicios públicos:** Administración dice en su correo del 2026-10-01 que va dentro del presupuesto, y esta línea no lo sostiene (`declared_vs_evidence`).
- **Servicios públicos:** se ejecutaron 621,000.00 contra 540,000.00 aprobados al corte, es decir +15.0 %, sobre el umbral de 10 % (`variance_over_threshold`).
- **Cambios sin acta entre la v1 y la v2** (`transfer_without_approval`): Operaciones · Transporte +96,000.00 y Tecnología · Licencias -96,000.00. Salen en el registro de traslados, no en el reporte de ejecución.

| Área | Línea | Aprobado | Al corte | Ejecutado | Comprometido | Disponible | Desviación | % |
|---|---|---|---|---|---|---|---|---|
| Administración | Servicios públicos | 720,000.00 | 540,000.00 | 621,000.00 | 18,000.00 | 81,000.00 | 81,000.00 | 15.00 |
| Administración | Mantenimiento | 480,000.00 | 360,000.00 | 349,200.00 | 12,000.00 | 118,800.00 | -10,800.00 | -3.00 |
| Comercial | Eventos | 420,000.00 | 300,000.00 | 291,000.00 | 12,000.00 | 117,000.00 | -9,000.00 | -3.00 |
| Comercial | Publicidad | 900,000.00 | 690,000.00 | 669,300.00 | 21,000.00 | 209,700.00 | -20,700.00 | -3.00 |
| Operaciones | Transporte | 936,000.00 | 678,000.00 | 657,660.00 | 25,800.00 | 252,540.00 | -20,340.00 | -3.00 |
| Tecnología | Licencias | 1,104,000.00 | 852,000.00 | 826,440.00 | 25,200.00 | 252,360.00 | -25,560.00 | -3.00 |
| Tecnología | PRY-310 | 1,440,000.00 | 1,080,000.00 | 1,047,600.00 | 36,000.00 | 356,400.00 | -32,400.00 | -3.00 |
| Personal | Nómina | 4,800,000.00 | 3,600,000.00 | 3,600,000.00 | 120,000.00 | 1,080,000.00 | 0.00 | 0.00 |

**Lo que decidí porque nadie contestó:**
- **Datos de la entidad:** entidad, país, moneda, marco y aprobador salieron de la configuración de finanzas que ya existía.
- **Umbrales:** desviación 10 %, comprometido 95 % y proyección vencida a 45 días, los de `config.example.json`. Son configuración, no norma.
- **Comité:** no encontré fechas de comité, así que quedan vacías. La última acta de comité es del 2026-09-10. Dejé abierto su compromiso: Administración revisa el contrato de vigilancia antes del próximo comité.
- **Fichas PMO:** `estado-pmo/records`, que existe y trae `PRY-310.json`.
- **Marca de la carpeta:** no dejé `_CRITERIO_FINANZAS.txt` porque nadie lo autorizó.

**Lo que no se pudo procesar:** todo lo que llegó se procesó.

La configuración quedó en `.criterio/presupuesto/BVA150301K21/config.json` y la corrida quedó registrada como `2026-10-06-budget-setup-1`. El reporte completo está en `estado-finanzas/BVA150301K21-banco-valle-de-anahuac/presupuesto/2026/reporte-variance-report.md`.

**Cuándo vuelvo:** cuando llegue la contabilidad de un mes nuevo, antes de cada comité y una vez por semana por los compromisos.