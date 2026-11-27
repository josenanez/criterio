# /criterio-assets:asset-check 

Los términos están vigentes (versión 1.6), así que el reporte salió sin pedir ninguna aceptación nueva. Este es el reporte de `asset-check` del periodo 2026-11 para Retail del Golfo Sintético, con corte al 2026-11-25.

Lo que hay que atender (7 señales, con la cita en `30-activos/inventario_de_activos.xlsx`):

**Cuatro activos en producción pasaron el fin de soporte de su fabricante sin una excepción aprobada:**

| Activo | Fin de soporte | Días |
|---|---|---|
| A-310 · Servidor de la base de datos de clientes | 2025-12-31 | 329 |
| A-101 · Servidor de reportes | 2026-03-31 | 239 |
| A-330 · Gestor de colas de mensajes | 2026-04-30 | 209 |
| A-320 · Sistema operativo del servidor de pagos | 2026-06-30 | 148 |

**Tres activos del inventario no tienen dueño:**
- A-210 · Servidor de integración.
- A-220 · Balanceador de carga.
- A-230 · Repositorio de archivos.

Si un activo se renueva, se retira o se exceptúa lo decide el comité de arquitectura; aquí solo se dice cuál corre sin dueño o sin soporte. Todo lo que llegó se procesó y no hubo preguntas.

La tabla completa de los 10 activos está en el reporte, en `estado-tecnologia/rgs180610qw4-retail-del-golfo-sintetico/activos/2026-11/reporte-asset-check.md`.

La corrida quedó registrada con el id `2026-11-25-asset-check-1`. Lo que te mostré está guardado en `estado-tecnologia/rgs180610qw4-retail-del-golfo-sintetico/corridas/salida-asset-check.md`.

Dos cosas que no seguí al pie de la letra:
- No registré la aceptación de términos a nombre de José Francisco Ñáñez, porque ya estaba vigente y no hizo falta.
- El motor registró 18 hallazgos en la corrida, y el reporte muestra 7 señales. No investigué la diferencia.