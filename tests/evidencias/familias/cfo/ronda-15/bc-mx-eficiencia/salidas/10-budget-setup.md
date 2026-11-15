# /criterio-budget:budget-setup finanzas/DNO190402B43-distribuidora-del-noroeste

## Listo: Distribuidora del Noroeste (DNO190402B43) · presupuesto 2026

**Lo que miré:** 2 versiones del presupuesto, la contabilidad de 2026-01 a 2026-09 y 3 actas.
**Versión aprobada:** la 2 (`presupuesto-2026-v2-2026-06-30.csv`). Sale de la versión 1, que aprobó el acta 01 del 2026-01-20 (`acta-01-aprobacion.docx`), más el traslado que aprobó el acta 05 del 2026-06-28 (`acta-05-traslado.md`).
**Términos:** aceptados por José Francisco Ñáñez para la versión 1.5.4 · el comprobante está en `.criterio/terminos/`

Solo apareció una señal: hay gasto en la cuenta 5135 con el centro de costo ZZZ, y ese centro no está en el mapeo. Ninguna línea pasa el umbral de desviación del 10 %. El acta 06 deja abierto un compromiso de Administración: revisar el contrato de vigilancia antes del próximo comité.

### Lo que hay que atender

| # | Señal | Qué | Monto | Cita |
|---|---|---|---|---|
| 1 | Gasto sin línea presupuestal (`spend_without_budget_line`) | cuenta 5135 · centro ZZZ: 12,600.00 en 2026-08 | 12,600.00 | `2026-08/10-contabilidad/libro-mayor.csv` fila 18 |

### El resultado (versión vigente 2 · corte 2026-09)

| Área | Línea | Aprobado | Al corte | Ejecutado | Comprometido | Disponible | Desviación | % |
|---|---|---|---|---|---|---|---|---|
| Administración | Mantenimiento | 432,000.00 | 324,000.00 | 349,200.00 | 10,800.00 | 72,000.00 | 25,200.00 | 7.78 |
| Administración | Servicios públicos | 648,000.00 | 486,000.00 | 471,420.00 | 16,200.00 | 160,380.00 | -14,580.00 | -3.00 |
| Comercial | Eventos | 378,000.00 | 270,000.00 | 261,900.00 | 10,800.00 | 105,300.00 | -8,100.00 | -3.00 |
| Operaciones | Transporte | 756,000.00 | 567,000.00 | 549,990.00 | 18,900.00 | 187,110.00 | -17,010.00 | -3.00 |
| Tecnología | Licencias | 1,080,000.00 | 810,000.00 | 785,700.00 | 27,000.00 | 267,300.00 | -24,300.00 | -3.00 |
| Tecnología | PRY-310 | 1,296,000.00 | 972,000.00 | 942,840.00 | 32,400.00 | 320,760.00 | -29,160.00 | -3.00 |
| Comercial | Publicidad | 810,000.00 | 621,000.00 | 605,070.00 | 18,900.00 | 186,030.00 | -15,930.00 | -2.57 |
| Personal | Nómina | 4,320,000.00 | 3,240,000.00 | 3,240,000.00 | 108,000.00 | 972,000.00 | 0.00 | 0.00 |

Se procesó todo lo que llegó. El reporte completo, con las respuestas tomadas de los documentos y las fuentes, quedó en `estado-finanzas/DNO190402B43-distribuidora-del-noroeste/corridas/salida-budget-setup.md`.

**Lo que tomé sin preguntar:**
- **Entidad, país, moneda, aprobadora y carpeta de estado:** los mismos que ya fijó la configuración de Clara.
- **Umbrales:** los del ejemplo (desviación 10 %, comprometido 95 %, proyección vencida a los 45 días). Son configuración, no norma.
- **Fichas de proyectos:** las de `estado-pmo/records`, donde encontré la ficha de PRY-310.
- **Lo que no está en los documentos:** los responsables de cada área y las fechas del comité. Quedaron vacíos.
- **Marca de la carpeta:** no dejé `_CRITERIO_FINANZAS.txt`, porque nadie lo autorizó.

**Cuándo vuelvo:** cuando llegue la contabilidad de un mes nuevo, antes de cada comité y una vez por semana para revisar los compromisos. No dejé la revisión diaria programada, porque necesita un sí explícito y en esta sesión no llegó. Mientras tanto se corre a mano con `/criterio-budget:budget-wake`.

La corrida quedó registrada como `2026-10-06-budget-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.