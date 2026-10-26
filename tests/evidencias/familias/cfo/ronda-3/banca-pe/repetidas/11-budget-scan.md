# /criterio-budget:budget-scan 

Sin archivos nuevos ni cambiados desde la corrida anterior. Extraje las 3 actas de `40-actas` a la ficha: la aprobación (versión 1), un traslado y el compromiso de vigilancia, que sigue abierto y sin evidencia. La sección «El resultado» del reporte salió vacía; así la entrega el motor.

# Qué cambió en el presupuesto · Banco Ribera · presupuesto 2026, corte 2026-09

**Entidad:** Banco Ribera (20710000019) · **Fecha de corte:** 2026-09 · **Procesado:** 2026-10-06 · **Agente:** Tomás, versión 0.9.0 · **Aprueba:** Sofía León · **Comando:** `budget-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Cita |
|---|---|---|---|---|
| 1 | Un traslado o una modificación no tiene el acta que lo aprueba (`transfer_without_approval`) | Operaciones · Transporte: cambió 19,200.00 entre la versión 1 y la 2 sin acta que lo apruebe | 19,200.00 | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` · `presupuesto-2026/10-aprobado/presupuesto-2026-v1-2026-01-15.xlsx` |
| 2 | Un traslado o una modificación no tiene el acta que lo aprueba (`transfer_without_approval`) | Tecnología · Licencias: cambió -19,200.00 entre la versión 1 y la 2 sin acta que lo apruebe | -19,200.00 | las mismas dos fuentes |
| 3 | Lo ejecutado al corte se aparta del presupuesto más del porcentaje configurado (`variance_over_threshold`) | Administración · Servicios públicos: ejecutado 124,200.00 contra 108,000.00 aprobado al corte (+15.0 %) | 16,200.00 | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` fila 2 · `2026-01/10-contabilidad/libro-mayor.xlsx` fila 2 · `2026-02/10-contabilidad/libro-mayor.xlsx` fila 2 |

Las columnas Responsable y Días venían vacías (—) y no las incluí.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `2026-01/10-contabilidad/libro-mayor.xlsx`
- `2026-02/10-contabilidad/libro-mayor.xlsx`
- `presupuesto-2026/10-aprobado/presupuesto-2026-v1-2026-01-15.xlsx`
- `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv`

La corrida quedó registrada como `2026-10-06-budget-scan-1`, con 3 hallazgos.

Antes de registrarla corregí un error mío. Un `cd` que dejé puesto hizo que el motor no encontrara la configuración. Volví a la carpeta de trabajo y el registro salió bien. La salida guardada en `corridas/salida-budget-scan.md` incluye las dos líneas del encabezado de esta respuesta y el reporte del motor. Ahí el cuadro de señales conserva las columnas Responsable y Días vacías, tal como lo emitió el motor.