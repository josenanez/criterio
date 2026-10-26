# /criterio-budget:budget-scan 

Términos vigentes (versión 1.2, aceptados por José Francisco Ñáñez el 2026-10-06). El inventario no trae archivos nuevos, cambiados ni borrados. Las tres actas de `40-actas/` ya estaban en la ficha y coinciden con su texto.

# Qué cambió en el presupuesto · Comercial Control Sur · presupuesto 2026, corte 2026-09

**Entidad:** Comercial Control Sur (20790000014) · **Fecha de corte:** 2026-09 · **Procesado:** 2026-10-06 · **Agente:** Tomás, versión 0.10.0 · **Aprueba:** Sofía León · **Comando:** `budget-scan`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la entidad y el año presupuestal? → Comercial Control Sur (RUC 20790000014), presupuesto 2026, corte 2026-09 (tomado de la carpeta y de la configuración de finanzas)
- ¿Cuál es la versión aprobada y su acta? → Acta 01 del 2026-01-20 aprueba la versión 1; la vigente es la más reciente de 10-aprobado (v2 del 2026-06-30), que nace del traslado del acta 05 del 2026-06-28. No se fijó approved_version
- ¿Áreas y responsables? → No encontrado en los documentos; se toman las áreas del presupuesto y no se asignan responsables
- ¿Mapeo de cuentas a líneas? → 00-referencia/mapeo-presupuesto.csv
- ¿Umbrales? → Los de config.example.json: desviación 10 %, comprometido 95 %, proyección vencida 45 días (configuración, no norma)
- ¿Fechas del comité de presupuesto? → No encontrado: las actas traen fechas de sesiones pasadas, no la del próximo comité; committee_dates queda vacío
- ¿Fichas PMO? → estado-pmo/records (contiene PRY-310.json)
- ¿Dónde se guarda el estado? → estado-finanzas/20790000014-comercial-control-sur, fuera de la carpeta de documentos

## Fuentes

- Sin documentos citados.

La corrida quedó registrada como `2026-10-06-budget-scan-1` (0 hallazgos). Antes de escribir `salida-budget-scan.md` ejecuté `compute`, que no devolvió señales. Tampoco devolvió `record_issues`, así que la ficha no necesitó cambios.

Dos observaciones sobre lo que me pasó:
- El reporte sale con "El resultado" vacío y "Fuentes: Sin documentos citados", aunque la ficha cita las actas. Lo dejé tal como lo escribió el motor.
- La nota de la corrida dice "3 actas ya en la ficha". Es mi lectura del inventario y de la ficha, no una cifra del motor.