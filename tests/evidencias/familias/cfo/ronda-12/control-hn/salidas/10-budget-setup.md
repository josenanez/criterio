# /criterio-budget:budget-setup finanzas/08010007330150-comercial-control-de-honduras

## Listo — Comercial Control de Honduras · presupuesto 2026

**Lo que miré:** 2 versiones del presupuesto, contabilidad de 2026-01 a 2026-09 y 3 actas.

**Versión aprobada:** la versión 1, con el acta 01 del 2026-01-20. La versión que rige es la 2 (2026-06-30). Nace del traslado de 90,000.00 de Comercial · Publicidad a Comercial · Eventos que aprueba el acta 05 del 2026-06-28.

**Términos:** José Francisco Ñáñez los aceptó el 2026-10-06 para la versión 1.1.0. Los comprobantes quedaron en `.criterio/terminos/`.

**Configuración:** `.criterio/presupuesto/08010007330150/config.json`. Pasó la validación sin problemas.

**Respuestas por defecto**, porque nadie podía contestar:
- **Mapeo de cuentas:** el de `00-referencia/mapeo-presupuesto.csv`.
- **Umbrales:** los de `config.example.json`, es decir desviación 10 %, comprometido 95 % y proyección vencida a los 45 días.
- **Fecha del próximo comité:** ninguna, porque no está en los documentos. El último fue el 2026-09-10.
- **Fichas del PMO:** `estado-pmo/records`.
- **Estado:** `estado-finanzas/08010007330150-comercial-control-de-honduras`.
- **Marca de la carpeta:** no dejé `_CRITERIO_FINANZAS.txt`, porque nadie la autorizó.

**Señales:** el primer `compute` dio 2 de `transfer_without_approval` y 4 documentos sin extraer, porque la ficha aún no citaba las actas. Escribí la ficha con las dos actas, el correo de Administración y el compromiso del comité. Al recalcular quedaron en 0 señales y 0 `record_issues`.

**Ejecución contra lo aprobado, corte 2026-09, versión 2:**

| Área | Línea | Aprobado | Al corte | Ejecutado | Comprometido | Disponible | Desviación | % |
|---|---|---|---|---|---|---|---|---|
| Administración | Mantenimiento | 720,000.00 | 540,000.00 | 523,800.00 | 18,000.00 | 178,200.00 | -16,200.00 | -3.00 |
| Administración | Servicios públicos | 1,080,000.00 | 810,000.00 | 785,700.00 | 27,000.00 | 267,300.00 | -24,300.00 | -3.00 |
| Comercial | Eventos | 630,000.00 | 450,000.00 | 436,500.00 | 18,000.00 | 175,500.00 | -13,500.00 | -3.00 |
| Comercial | Publicidad | 1,350,000.00 | 1,035,000.00 | 1,003,950.00 | 31,500.00 | 314,550.00 | -31,050.00 | -3.00 |
| Operaciones | Transporte | 1,260,000.00 | 945,000.00 | 916,650.00 | 31,500.00 | 311,850.00 | -28,350.00 | -3.00 |
| Tecnología | Licencias | 1,800,000.00 | 1,350,000.00 | 1,309,500.00 | 45,000.00 | 445,500.00 | -40,500.00 | -3.00 |
| Tecnología | PRY-310 | 2,160,000.00 | 1,620,000.00 | 1,571,400.00 | 54,000.00 | 534,600.00 | -48,600.00 | -3.00 |
| Personal | Nómina | 7,200,000.00 | 5,400,000.00 | 5,400,000.00 | 180,000.00 | 1,620,000.00 | 0.00 | 0.00 |

El reporte del motor dice «Nada abierto» y «Todo lo que llegó se procesó». Su sección de fuentes dice «Sin documentos citados», aunque la ficha sí cita las actas y el correo. No lo toqué.

**Cuándo vuelvo:** cuando llegue la contabilidad de un mes nuevo, antes de cada comité y una vez por semana por los compromisos.

La corrida quedó registrada como `2026-10-06-budget-setup-1`. Lo que te mostré está en `estado-finanzas/08010007330150-comercial-control-de-honduras/corridas/salida-budget-setup.md`.