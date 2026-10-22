# /criterio-budget:budget-scan 

Corte 2026-09: el inventario no trae archivos nuevos ni cambiados. Las tres actas ya estaban en la ficha y coinciden con lo que dicen, así que no la modifiqué. Salen 4 señales.

# Qué cambió en el presupuesto · Banco Andino · presupuesto 2026, corte 2026-09

**Entidad:** Banco Andino (900123456) · **Fecha de corte:** 2026-09 · **Procesado:** 2026-10-06 · **Agente:** Tomás, versión 0.7.0 · **Aprueba:** Contralor · **Comando:** `budget-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Cita |
|---|---|---|---|---|
| 1 | El área se reporta dentro del presupuesto y los números no lo sostienen (`declared_vs_evidence`) | Administración se reporta dentro del presupuesto y 1 línea no lo sostiene: Servicios públicos | 4.050.000,00 | `presupuesto-2026/30-proyecciones/correo-administracion.md` |
| 2 | Traslado o modificación sin acta que lo apruebe (`transfer_without_approval`) | Operaciones · Transporte: cambió 4.800.000,00 entre la versión 1 y la 2 sin acta | 4.800.000,00 | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` · `presupuesto-2026/10-aprobado/presupuesto-2026-v1-2026-01-15.csv` |
| 3 | Traslado o modificación sin acta que lo apruebe (`transfer_without_approval`) | Tecnología · Licencias: cambió -4.800.000,00 entre la versión 1 y la 2 sin acta | -4.800.000,00 | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` · `presupuesto-2026/10-aprobado/presupuesto-2026-v1-2026-01-15.csv` |
| 4 | Ejecutado se aparta del presupuesto más del umbral (`variance_over_threshold`) | Administración · Servicios públicos: ejecutado 31.050.000,00 contra 27.000.000,00 aprobado al corte (+15,0 %) | 4.050.000,00 | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` fila 2 · `2026-01/10-contabilidad/libro-mayor.csv` fila 2 · `2026-02/10-contabilidad/libro-mayor.csv` fila 2 |

## El resultado

(El motor no trae contenido en esta sección.)

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la versión aprobada y su acta? → Sesión sin interfaz: respuesta sugerida. El acta 01 (2026-01-20) aprueba la versión 1. El acta 05 (2026-06-28) aprueba un traslado, y existe la versión 2 del 2026-06-30. Ningún acta dice que apruebe la versión 2 como tal.

## Fuentes

- `2026-01/10-contabilidad/libro-mayor.csv`
- `2026-02/10-contabilidad/libro-mayor.csv`
- `presupuesto-2026/10-aprobado/presupuesto-2026-v1-2026-01-15.csv`
- `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv`
- `presupuesto-2026/30-proyecciones/correo-administracion.md`

La corrida quedó registrada como `2026-10-06-budget-scan-1`, con 4 hallazgos. La salida está en `estado-finanzas/900123456-banco-andino/corridas/salida-budget-scan.md`.

Dos cosas de esta sesión:
- Los términos (versión 1.2) ya estaban vigentes, así que no registré ninguna aceptación nueva a nombre de José Francisco Ñáñez.
- En el archivo de salida, la sección «El resultado» quedó vacía igual que en el reporte del motor. Añadí la línea entre paréntesis solo en este mensaje, no en el archivo.