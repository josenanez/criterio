# /criterio-budget:budget-setup finanzas/155831003-2-2013-comercial-control-del-istmo

## Listo: Comercial Control del Istmo, presupuesto 2026

**Lo que miré:** 2 versiones (v1 de 2026-01-15 y v2 de 2026-06-30), contabilidad de 2026-01 a 2026-09 y 3 actas.

**Versión aprobada:** la 2, que es la más reciente de `10-aprobado/`. No fijé `budget.approved_version` por mi cuenta. El acta 01 del 2026-01-20 aprueba la v1. El acta 05 del 2026-06-28 traslada 3,600.00 de Comercial · Publicidad a Comercial · Eventos.

**Términos:** José Francisco Ñáñez los aceptó el 2026-10-06 para la versión 1.0.0. Los comprobantes están en `.criterio/terminos/aceptacion-criterio-budget-1.0.0-2026-10-06.md` y `.pdf`.

**Marca de la carpeta:** no dejé `_CRITERIO_FINANZAS.txt`, porque nadie lo autorizó y escribe dentro de los documentos.

**Configuración:** `.criterio/presupuesto/155831003-2-2013-comercial-control-del-istmo/config.json`. Ya existía otra, creada por finance-setup, y no la toqué.

**Ejecución al corte 2026-09 (USD):**

| Área | Línea | Aprobado | Al corte | Ejecutado | Comprometido | Disponible | Desviación | % |
|---|---|---|---|---|---|---|---|---|
| Administración | Mantenimiento | 28,800.00 | 21,600.00 | 20,952.00 | 720.00 | 7,128.00 | -648.00 | -3.00 |
| Administración | Servicios públicos | 43,200.00 | 32,400.00 | 31,428.00 | 1,080.00 | 10,692.00 | -972.00 | -3.00 |
| Comercial | Eventos | 25,200.00 | 18,000.00 | 17,460.00 | 720.00 | 7,020.00 | -540.00 | -3.00 |
| Comercial | Publicidad | 54,000.00 | 41,400.00 | 40,158.00 | 1,260.00 | 12,582.00 | -1,242.00 | -3.00 |
| Operaciones | Transporte | 50,400.00 | 37,800.00 | 36,666.00 | 1,260.00 | 12,474.00 | -1,134.00 | -3.00 |
| Tecnología | Licencias | 72,000.00 | 54,000.00 | 52,380.00 | 1,800.00 | 17,820.00 | -1,620.00 | -3.00 |
| Tecnología | PRY-310 | 86,400.00 | 64,800.00 | 62,856.00 | 2,160.00 | 21,384.00 | -1,944.00 | -3.00 |
| Personal | Nómina | 288,000.00 | 216,000.00 | 216,000.00 | 7,200.00 | 64,800.00 | 0.00 | 0.00 |

- **Nada abierto:** el reporte no tiene nada que atender, y todo lo que llegó se procesó.
- **Sin señales tras corregir la ficha:** la primera corrida del motor trajo 2 señales `transfer_without_approval` y 4 documentos sin citar. Registré en la ficha las actas, el correo de Administración y el compromiso del comité (revisar el contrato de vigilancia, abierto). Con eso, al recalcular no quedó ninguna señal.
- **Umbrales:** usé los de `config.example.json` (desviación 10 %, comprometido 95 %, proyección vencida 45 días).
- **Fechas del comité:** no hay fechas futuras en los documentos, así que `committee_dates` quedó vacío.
- **Fichas PMO:** apunté a `estado-pmo/records`, donde está `PRY-310.json`.
- **Preguntas y tiempo:** nadie contestó preguntas en esta sesión sin interfaz, y no medí los minutos hasta el primer resultado.

La salida y el reporte están en `estado-finanzas/155831003-2-2013-comercial-control-del-istmo/` (`corridas/salida-budget-setup.md` y `presupuesto/2026/reporte-variance-report.md`). La corrida quedó registrada como `2026-10-06-budget-setup-1`.

**Cuándo vuelvo:** cuando llegue la contabilidad de un mes nuevo, antes de cada comité y una vez por semana por los compromisos.