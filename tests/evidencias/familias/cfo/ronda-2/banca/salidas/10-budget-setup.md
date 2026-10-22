# /criterio-budget:budget-setup finanzas/900123456-banco-andino

Dos cosas antes del reporte.
- **Versión aprobada:** el motor tomó la versión 2 como vigente, pero el único acta que aprueba una versión es la 01, que aprueba la 1. El acta 05 solo aprueba un traslado de 3,000,000.00. La versión 2 trae otros cambios sin acta, por ejemplo en Tecnología/Licencias y Operaciones/Transporte.
- **Señales que no se ven aquí:** `compute` levantó 2 señales `transfer_without_approval`, y este reporte no las lista. Las trae `/transfer-log`.

## Listo — Banco Andino · presupuesto 2026

**Lo que miré:** 2 versiones · contabilidad de 2026-01 a 2026-09 · 3 actas
**Versión aprobada:** 1, con el acta `presupuesto-2026/40-actas/acta-01-aprobacion.md` (2026-01-20)
**Términos:** aceptados por José Francisco Ñáñez el 2026-10-06 · comprobante en `.criterio/terminos/`
**Carpeta sin marcar:** no puse `_CRITERIO_FINANZAS.txt`, porque nadie lo autorizó.

El reporte completo, con sus fuentes y las preguntas que se tomaron como respuesta sugerida, está en `estado-finanzas/900123456-banco-andino/presupuesto/2026/reporte-variance-report.md`.

**Lo que hay que atender (3 filas del reporte):**
1. **Administración se reporta dentro del presupuesto** en su correo del 2026-10-01, y la línea Servicios públicos no lo sostiene (4.050.000,00).
2. **Administración · Servicios públicos:** ejecutado 31.050.000,00 contra 27.000.000,00 aprobado al corte, +15,0 %. Es la única línea sobre el umbral.
3. **PRY-310:** la ficha del proyecto dice 64.800.000,00 y el área tiene asignado 72.000.000,00 (-7.200.000,00).

**Ejecución contra aprobado por línea (versión 2 del presupuesto):**

| Área | Línea | Aprobado | Al corte | Ejecutado | Comprometido | Disponible | Desviación | % |
|---|---|---|---|---|---|---|---|---|
| Administración | Servicios públicos | 36.000.000,00 | 27.000.000,00 | 31.050.000,00 | 900.000,00 | 4.050.000,00 | 4.050.000,00 | 15,00 |
| Administración | Mantenimiento | 24.000.000,00 | 18.000.000,00 | 17.460.000,00 | 600.000,00 | 5.940.000,00 | -540.000,00 | -3,00 |
| Comercial | Eventos | 21.000.000,00 | 15.000.000,00 | 14.550.000,00 | 600.000,00 | 5.850.000,00 | -450.000,00 | -3,00 |
| Comercial | Publicidad | 45.000.000,00 | 34.500.000,00 | 33.465.000,00 | 1.050.000,00 | 10.485.000,00 | -1.035.000,00 | -3,00 |
| Operaciones | Transporte | 46.800.000,00 | 33.900.000,00 | 32.883.000,00 | 1.290.000,00 | 12.627.000,00 | -1.017.000,00 | -3,00 |
| Tecnología | Licencias | 55.200.000,00 | 42.600.000,00 | 41.322.000,00 | 1.260.000,00 | 12.618.000,00 | -1.278.000,00 | -3,00 |
| Tecnología | PRY-310 | 72.000.000,00 | 54.000.000,00 | 52.380.000,00 | 1.800.000,00 | 17.820.000,00 | -1.620.000,00 | -3,00 |
| Personal | Nómina | 240.000.000,00 | 180.000.000,00 | 180.000.000,00 | 6.000.000,00 | 54.000.000,00 | 0,00 | 0,00 |

**Respuestas tomadas por defecto (sesión sin interfaz):**
- **Responsables por área:** no aparecen en los documentos, así que quedaron sin asignar.
- **Umbrales:** los de `config.example.json`: desviación 10 %, comprometido 95 %, proyección vencida 45 días.
- **Fecha del comité:** no hay fecha. El acta 06 dice «el próximo comité» sin fecha, así que quedó vacío.
- **Fichas PMO:** `estado-pmo/records`, donde existe `PRY-310.json`.

La salida quedó en `estado-finanzas/900123456-banco-andino/corridas/salida-budget-setup.md`, y la corrida quedó registrada como `2026-10-06-budget-setup-1`, con 5 hallazgos. No medí los minutos hasta el primer resultado.

**Cuándo vuelvo:** cuando llegue la contabilidad de un mes nuevo, antes de cada comité y una vez por semana por los compromisos.