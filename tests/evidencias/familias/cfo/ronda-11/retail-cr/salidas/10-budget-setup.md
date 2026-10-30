# /criterio-budget:budget-setup finanzas/3101612904-almacenes-de-la-meseta

## Listo: Almacenes de la Meseta, presupuesto 2026

**Lo que miré:** dos versiones aprobadas (v1 del 2026-01-15 y v2 del 2026-06-30), contabilidad de 2026-01 a 2026-09 y tres actas.

**Versión aprobada:** la 2, que es la más reciente de `10-aprobado/`.
- El acta 01 (2026-01-20) aprueba la v1.
- El acta 05 (2026-06-28) aprueba el traslado de 2.250.000,00 de Publicidad a Eventos.

**Términos:** José Francisco Ñáñez los aceptó el 2026-10-06 para la versión 1.0.0. El comprobante está en `.criterio/terminos/aceptacion-criterio-budget-1.0.0-2026-10-06.md`.

**Qué muestra el reporte:** el motor levantó tres señales. El detalle completo está en el reporte.
1. **Gasto sin línea presupuestal:** 525.000,00 en la cuenta 5135, centro de costo ZZZ, en 2026-08. Viene de la fila 18 del libro mayor de agosto.
2. **Mantenimiento sin holgura:** ejecutado más comprometido es 96,0 % de lo aprobado en el año, y quedan 712.500,00 disponibles.
3. **Proyección vencida:** la de Operaciones · Transporte es del 2026-07-15, hace 83 días. Esta señal no aparece en la tabla del reporte; la saqué de `resultados.json`.

Todas las líneas, salvo Nómina, van 3 % por debajo del aprobado al corte; Nómina va exacta. El compromiso abierto del acta 06 es que Administración revise el contrato de vigilancia antes del próximo comité, que el acta no fecha.

**Respuestas que tomé yo, porque nadie contestó:**
- **Fechas del comité:** `committee_dates` quedó vacío, porque el acta 06 dice «próximo comité» sin fecha.
- **Marca de la carpeta:** no dejé `_CRITERIO_FINANZAS.txt`. Es lo único que se escribiría dentro de los documentos y nada lo pedía.
- **Prefijo de cuentas:** usé `51` como prefijo de gasto, porque las tres cuentas del mapeo (5135, 5145, 5195) empiezan así.
- **Fichas PMO:** apunté a `estado-pmo/records`, donde existe `PRY-310.json`.
- **Umbrales:** 10 % de desviación, 95 % de comprometido y 45 días de proyección vencida, los de `config.example.json`.

**Archivos que escribí:**
- Configuración: `.criterio/presupuesto/3101612904/config.json`
- Ficha de actas: `estado-finanzas/3101612904-almacenes-de-la-meseta/presupuesto/2026/ficha.json`
- Reporte: `estado-finanzas/3101612904-almacenes-de-la-meseta/presupuesto/2026/reporte-variance-report.md`
- Salida de esta corrida: `estado-finanzas/3101612904-almacenes-de-la-meseta/corridas/salida-budget-setup.md`. La registré como `2026-10-06-budget-setup-1`.

**Cuándo vuelvo:** cuando llegue la contabilidad de un mes nuevo, antes de cada comité y una vez por semana por los compromisos.