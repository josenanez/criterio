# /criterio-changes:change-check 

Ninguna aprobación ni revisión aparece en las actas procesadas para este periodo, así que todos los cambios figuran sin ellas. Si las actas de `10-cambios/` aún no se han procesado, `/criterio-changes:changes-scan` las lleva a la ficha.

# Cada cambio con su aprobación · Banco Meridiano Sintético · periodo 2026-11

**Entidad:** Banco Meridiano Sintético (901222444) · **Fecha de corte:** 2026-11-25 · **Agente:** Fausto 0.1.0 · **Comando:** `change-check`

## Lo que hay que atender

**Cambios normales sin aprobación en las actas (9):**
- CHG-100, CHG-103, CHG-104, CHG-210, CHG-220, CHG-230, CHG-410, CHG-420 y CHG-430.
- Fuente: `10-cambios/cambios_2026-10.xlsx`.

**Despliegues en producción sin cambio que los autorice (3):**
- D-510, Motor de reglas, 2026-10-14: sin cambio.
- D-520, Servicio de notificaciones, 2026-10-23: apunta a CHG-999, que no está en la exportación de cambios.
- D-530, Tablero de ventas, 2026-10-28: sin cambio.
- Fuente: `10-cambios/despliegues_2026-10.xlsx`.

**Cambios de emergencia sin revisión posterior (4).** La política da 5 días.

| Cambio | Implementado | Días |
|---|---|---|
| CHG-310 | 2026-10-03 | 48 |
| CHG-320 | 2026-10-09 | 42 |
| CHG-102 | 2026-10-10 | 41 |
| CHG-330 | 2026-10-18 | 33 |

**Cambios fallidos o revertidos sin revisión (4):**
- CHG-104, revertido.
- CHG-410, revertido.
- CHG-420, fallido.
- CHG-430, revertido.

## Lo que no se pudo procesar
Todo lo que llegó se procesó.

## Las preguntas que hizo
Ninguna en esta corrida.

## Fuentes
`10-cambios/cambios_2026-10.xlsx`, `10-cambios/despliegues_2026-10.xlsx`.

El reporte completo, con la tabla de los 14 cambios y los 5 despliegues, está en `estado-tecnologia/901222444-banco-meridiano-sintetico/cambios/2026-11/reporte-change-check.md`. Lo de arriba lo resumí yo a partir de ese reporte. La salida guardada en `corridas/salida-change-check.md` lleva el texto completo del motor, no este resumen.

La corrida quedó registrada como `2026-11-25-change-check-1`, con 18 hallazgos. Tiene 18 y no 20 porque CHG-104 y CHG-410 aparecen dos veces entre las señales. Los términos ya estaban vigentes, así que no registré ninguna aceptación nueva.