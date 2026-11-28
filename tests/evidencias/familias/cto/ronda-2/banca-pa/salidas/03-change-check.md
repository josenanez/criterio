# /criterio-changes:change-check 

Términos vigentes (versión 1.6). Constan como aceptados por José Francisco Ñáñez, con fecha 2026-11-25, para esta prueba.

**Aviso:** en el resultado, las columnas «Aprobado» y «Revisado» salen vacías en los 11 cambios. Parece que las actas del comité de cambios todavía no se han llevado a la ficha del periodo, y eso lo hace `/criterio-changes:changes-scan`. Lea las señales de falta de aprobación y de falta de revisión con esa reserva.

# Cada cambio con su aprobación · Banco del Istmo Sintético · periodo 2026-11

**Entidad:** Banco del Istmo Sintético (155612345-2-2019) · **Fecha de corte:** 2026-11-25 · **Agente:** Fausto 0.2.0

## Lo que hay que atender (15 señales)

**Cambios normales sin aprobación en las actas** (`change_without_approval`), todos en `10-cambios/cambios_2026-10.xlsx`:
- CHG-100, Actualización del certificado del portal, implementado el 2026-10-05 (fila 2).
- CHG-103, Ajuste del límite de sesiones, implementado el 2026-10-08 (fila 5).
- CHG-104, Nueva versión del motor de pagos, implementado el 2026-10-12 (fila 6).
- CHG-210, Migración del servidor de archivos, implementado el 2026-10-06 (fila 7).
- CHG-220, Cambio de la regla del cortafuegos de la red interna, implementado el 2026-10-16 (fila 8).
- CHG-410, Actualización del sistema de nómina, implementado el 2026-10-07 (fila 11).
- CHG-420, Nueva versión de la aplicación móvil, implementado el 2026-10-13 (fila 12).

**Despliegues sin cambio que los autorice** (`deployment_without_change`), en `10-cambios/despliegues_2026-10.xlsx`:
- D-510, Motor de reglas, desplegado el 2026-10-14 sin ningún cambio (fila 5).
- D-520, Servicio de notificaciones, desplegado el 2026-10-23 con el cambio CHG-999, que no está en la exportación de cambios (fila 6).

**Cambios de emergencia sin revisión posterior** (`emergency_change_without_review`). La política da 5 días para revisarlos. Los días son los que informa el motor.
- CHG-310, Reinicio de emergencia del clúster de base de datos, implementado el 2026-10-03, 48 días (fila 9).
- CHG-320, Parche de emergencia del servidor de aplicaciones, implementado el 2026-10-09, 42 días (fila 10).
- CHG-102, Corrección de la conciliación de pagos, implementado el 2026-10-10, 41 días (fila 4).

**Cambios fallidos o revertidos sin revisión** (`failed_change_without_review`):
- CHG-104, Revertido el 2026-10-12.
- CHG-410, Revertido el 2026-10-07.
- CHG-420, Fallido el 2026-10-13.

## El resultado

| Cambio | Tipo | Implementado | Resultado | Aprobado | Revisado |
|---|---|---|---|---|---|
| CHG-100 | Normal | 2026-10-05 | Exitoso | — | — |
| CHG-101 | Estándar | 2026-10-20 | Exitoso | — | — |
| CHG-102 | Emergencia | 2026-10-10 | Exitoso | — | — |
| CHG-103 | Normal | 2026-10-08 | Exitoso | — | — |
| CHG-104 | Normal | 2026-10-12 | Revertido | — | — |
| CHG-210 | Normal | 2026-10-06 | Exitoso | — | — |
| CHG-220 | Normal | 2026-10-16 | Exitoso | — | — |
| CHG-310 | Emergencia | 2026-10-03 | Exitoso | — | — |
| CHG-320 | Emergencia | 2026-10-09 | Exitoso | — | — |
| CHG-410 | Normal | 2026-10-07 | Revertido | — | — |
| CHG-420 | Normal | 2026-10-13 | Fallido | — | — |

| Despliegue | Fecha | Sistema | Cambio | En la exportación |
|---|---|---|---|---|
| D-100 | 2026-10-05 | Portal | CHG-100 | sí |
| D-101 | 2026-10-08 | Portal | CHG-103 | sí |
| D-510 | 2026-10-14 | Motor de reglas | — | no |
| D-520 | 2026-10-23 | Servicio de notificaciones | CHG-999 | no |

Si un cambio se aprueba lo decide el comité de cambios: aquí se dice cuál llegó a producción sin su aprobación o sin su revisión.

**Lo que no se pudo procesar:** nada, todo lo que llegó se procesó. **Preguntas que hizo:** ninguna.

**Fuentes:** `10-cambios/cambios_2026-10.xlsx`, `10-cambios/despliegues_2026-10.xlsx`, F-01 (families/criterio-cto/FUENTES.es.md).

La corrida quedó registrada como `2026-11-25-change-check-1` con 12 hallazgos. La salida completa está en `estado-tecnologia/155612345-2-2019-banco-del-istmo-sintetico/corridas/salida-change-check.md`, y el reporte del motor está en `…/cambios/2026-11/reporte-change-check.md`.

El reporte tiene 15 señales y la corrida registró 12 hallazgos. No sé a qué se debe la diferencia: el motor no la explica. Una posibilidad es que CHG-104 y CHG-410 cuenten cada uno una vez en vez de dos, pero no lo verifiqué.