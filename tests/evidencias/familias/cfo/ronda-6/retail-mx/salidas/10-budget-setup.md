# /criterio-budget:budget-setup finanzas/TBA180912Q37-tiendas-del-bajio

## Listo — Tiendas del Bajío (TBA180912Q37) · presupuesto 2026

**Lo que miré:** 2 versiones del presupuesto, contabilidad de 2026-01 a 2026-09 (9 periodos) y 3 actas.

**Versión aprobada:** la 2, `presupuesto-2026-v2-2026-06-30.xlsx`, que es la más reciente de `10-aprobado/`. Nace del traslado del acta 05 (2026-06-28), que mueve 45,000.00 de Comercial · Publicidad a Comercial · Eventos de julio a diciembre. La v1 la aprueba el acta 01 (2026-01-20). No fijé `approved_version` a mano.

**Términos:** aceptados a nombre de José Francisco Ñáñez el 2026-10-06. Los comprobantes están en `.criterio/terminos/aceptacion-criterio-budget-0.11.0-2026-10-06.md` y `.pdf`.

**Lo que hay que atender**
1. **Gasto sin línea presupuestal:** cuenta 5135, centro ZZZ, 10,500.00 en 2026-08 (`2026-08/10-contabilidad/libro-mayor.xlsx`, fila 18).
2. **Administración · Mantenimiento:** ejecutado más comprometido es el 96.0 % de lo aprobado en el año. Quedan 14,250.00 disponibles.
3. **Proyección vencida:** la de Operaciones · Transporte es del 2026-07-15, hace 83 días. Esta señal no aparece en el reporte, solo en `resultados.json`.

**Compromiso abierto del comité:** Administración revisa el contrato de vigilancia antes del próximo comité (acta 06). El acta no da fecha.

**Ejecución al corte 2026-09:** todas las líneas están 3.00 % por debajo de lo previsto al corte, salvo Personal · Nómina, que va en 0.00 %. El reporte completo, con las ocho líneas, está en `estado-finanzas/TBA180912Q37-tiendas-del-bajio/presupuesto/2026/reporte-variance-report.md`.

**Cómo resolví las preguntas, sin nadie a quien preguntarle:**
- **Configuración:** quedó en `.criterio/presupuesto/TBA180912Q37/config.json`.
- **Datos de la entidad:** los tomé de la configuración de finanzas que ya existía.
- **Umbrales:** usé los del ejemplo: 10 % de desviación, 95 % de comprometido y 45 días para una proyección vencida.
- **Fichas PMO:** apunté a `estado-pmo/records`, que existe y trae `PRY-310.json`.
- **Fechas del comité:** quedaron vacías, porque ningún documento trae una.
- **Marca de la raíz (`_CRITERIO_FINANZAS.txt`):** no la dejé, porque nadie la autorizó.

**Cuándo vuelvo:** cuando llegue la contabilidad de un mes nuevo, antes de cada comité y una vez por semana por los compromisos.

La salida completa y el registro de la corrida están en `estado-finanzas/TBA180912Q37-tiendas-del-bajio/corridas/`.