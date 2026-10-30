# /criterio-budget:budget-setup finanzas/97217352-comercial-control-de-guatemala

## Listo — Comercial Control de Guatemala · presupuesto 2026

**Lo que miré:** 2 versiones (v1 de 2026-01-15 y v2 de 2026-06-30), contabilidad de 2026-01 a 2026-09 y 3 actas.

**Versión aprobada:** la 2, porque es la más reciente de `10-aprobado/`. Nace del traslado del acta 05 (`acta-05-traslado.docx`, 2026-06-28). El acta 01 (2026-01-20) aprobó la v1.

**Términos:** José Francisco Ñáñez los aceptó el 2026-10-06 para la versión 1.0.0. El comprobante en Markdown y PDF quedó en `.criterio/terminos/`.

La sesión no tenía interfaz, así que tomé cada respuesta de los documentos:
- **Configuración:** `.criterio/presupuesto/97217352/config.json`, con los umbrales de `config.example.json` (desviación 10 %, comprometido 95 %, proyección vencida 45 días).
- **Fichas del PMO:** `estado-pmo/records`, donde existe `PRY-310.json`.
- **Estado:** `estado-finanzas/97217352-comercial-control-de-guatemala`.
- **Fechas de comité:** ninguna, porque ningún documento trae una.
- **Marca de la carpeta:** no dejé `_CRITERIO_FINANZAS.txt`, porque nadie lo autorizó.
- **Ficha del presupuesto:**
  - Administración dice que va dentro del presupuesto (correo del 2026-10-01).
  - El acta 06 deja un compromiso abierto: revisar el contrato de vigilancia antes del próximo comité.

**Ejecución contra lo aprobado, corte 2026-09.** El motor no encontró señales ni documentos sin procesar. El reporte completo está en `estado-finanzas/97217352-comercial-control-de-guatemala/presupuesto/2026/reporte-variance-report.md`.

| Área | Línea | Aprobado | Al corte | Ejecutado | Comprometido | Disponible | Desviación | % |
|---|---|---|---|---|---|---|---|---|
| Administración | Mantenimiento | 240,000.00 | 180,000.00 | 174,600.00 | 6,000.00 | 59,400.00 | -5,400.00 | -3.00 |
| Administración | Servicios públicos | 360,000.00 | 270,000.00 | 261,900.00 | 9,000.00 | 89,100.00 | -8,100.00 | -3.00 |
| Comercial | Eventos | 210,000.00 | 150,000.00 | 145,500.00 | 6,000.00 | 58,500.00 | -4,500.00 | -3.00 |
| Comercial | Publicidad | 450,000.00 | 345,000.00 | 334,650.00 | 10,500.00 | 104,850.00 | -10,350.00 | -3.00 |
| Operaciones | Transporte | 420,000.00 | 315,000.00 | 305,550.00 | 10,500.00 | 103,950.00 | -9,450.00 | -3.00 |
| Tecnología | Licencias | 600,000.00 | 450,000.00 | 436,500.00 | 15,000.00 | 148,500.00 | -13,500.00 | -3.00 |
| Tecnología | PRY-310 | 720,000.00 | 540,000.00 | 523,800.00 | 18,000.00 | 178,200.00 | -16,200.00 | -3.00 |
| Personal | Nómina | 2,400,000.00 | 1,800,000.00 | 1,800,000.00 | 60,000.00 | 540,000.00 | 0.00 | 0.00 |

**Cuándo vuelvo:** cuando llegue la contabilidad de un mes nuevo, antes de cada comité y una vez por semana por los compromisos.

La corrida quedó registrada como `2026-10-06-budget-setup-1`, con lo que te mostré en `corridas/salida-budget-setup.md`.