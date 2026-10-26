# /criterio-budget:budget-scan 

Corte 2026-09: el inventario no trae archivos nuevos ni cambiados (63 en total). Las tres actas de `40-actas/` ya estaban en la ficha con su cita, así que no cambié nada. Aparecen dos señales: una proyección de área sobre lo aprobado y un gasto sin línea presupuestal.

Los términos (versión 1.2) ya estaban vigentes y aceptados, así que no registré ninguna aceptación nueva.

# Qué cambió en el presupuesto · Almacenes Caribe · presupuesto 2026, corte 2026-09

**Entidad:** Almacenes Caribe (900765432) · **Fecha de corte:** 2026-09 · **Procesado:** 2026-10-06 · **Agente:** Tomás, versión 0.10.0 · **Aprueba:** Sofía León · **Comando:** `budget-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | La proyección al cierre del año supera lo aprobado (`forecast_over_approved`) | Tecnología · PRY-310: la proyección al cierre, la del área, es 63.360.000,00 y lo aprobado 57.600.000,00 | 5.760.000,00 | — | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.xlsx` fila 7 · `2026-01/10-contabilidad/libro-mayor.xlsx` fila 12 · `2026-02/10-contabilidad/libro-mayor.xlsx` fila 12 |
| 2 | Hay gasto en una cuenta o centro de costo sin línea presupuestal (`spend_without_budget_line`) | cuenta 5135 · centro ZZZ: 560.000,00 en 2026-08 sin línea presupuestal | 560.000,00 | — | — | `2026-08/10-contabilidad/libro-mayor.xlsx` fila 18 |

## El resultado

(El motor dejó esta sección vacía.)

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Entidad y año presupuestal? → Almacenes Caribe (NIT 900765432), presupuesto 2026, corte 2026-09 (tomado de la carpeta y de la configuración de Clara)
- ¿Cuál es la versión aprobada y su acta? → Acta 01 del 2026-01-20 aprueba la versión 1; rige la más reciente de 10-aprobado/ (v2, 2026-06-30), que nace del traslado del acta 05 del 2026-06-28. No se fijó approved_version
- ¿Áreas y responsables? → Las que aparecen en el presupuesto y el mapeo (Administración, Comercial, Tecnología, Operaciones, Personal); responsables no declarados en los documentos
- ¿Mapeo de cuentas a líneas? → 00-referencia/mapeo-presupuesto.csv
- ¿Umbrales? → Los de config.example.json: desviación 10 %, comprometido 95 %, proyección vencida 45 días (configuración, no norma)
- ¿Fechas del comité? → No encontrado: el acta 06 (2026-09-10) no fija el próximo comité; committee_dates queda vacío
- ¿Fichas PMO? → estado-pmo/records (contiene PRY-310.json)
- ¿Dónde guardo lo que encuentro? → estado-finanzas/900765432-almacenes-caribe, fuera de la carpeta de documentos

## Fuentes

- `2026-01/10-contabilidad/libro-mayor.xlsx`
- `2026-02/10-contabilidad/libro-mayor.xlsx`
- `2026-08/10-contabilidad/libro-mayor.xlsx`
- `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.xlsx`

La corrida quedó registrada como `2026-10-06-budget-scan-1` con 2 hallazgos. El texto mostrado está en `estado-finanzas/900765432-almacenes-caribe/corridas/salida-budget-scan.md`.

Dos cosas que debe saber:
- **Sección vacía:** en el reporte del motor, «El resultado» salió sin contenido. Lo dejé tal cual, sin rellenarlo.
- **Archivo del reporte:** en el archivo de la corrida, esa sección queda sin la nota entre paréntesis que puse arriba, porque guardé el texto como lo escribió el motor.