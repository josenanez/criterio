# /criterio-changes:changes-setup tecnologia/76543210-k-software-austral-sintetico

Fausto quedó instalado para Software Austral Sintético (RUT 76543210-K, Chile, periodo 2026-10), y el primer reporte de cambios trae 8 señales.

Como nadie podía contestar, saqué cada respuesta de los documentos:
- **Carpeta:** `tecnologia/76543210-k-software-austral-sintetico`. Era la única candidata.
- **Plazos:** 5 días para revisar un cambio de emergencia y 10 días para registrar el problema de un incidente mayor. Los dos salen de la política aprobada el 2025-11-20.
- **Rostrum:** lo que encuentro se publica ahí. La política no dice otra cosa.
- **Dónde guardo el estado:** `estado-tecnologia/76543210-k-software-austral-sintetico`.
- **Marca:** dejé `_CRITERIO_TECNOLOGIA.txt` en la carpeta de la entidad.
- **Términos v1.6:** los aceptó José Francisco Ñáñez el 2026-11-25. El comprobante está en `.criterio/terminos/aceptacion-criterio-changes-0.1.0-2026-11-25.md` y su `.pdf`.
- **Configuración:** `.criterio/cambios/76543210-K/config.json`.

Procesé las 4 actas del comité de cambios de octubre y pasé a la ficha 6 aprobaciones y 3 revisiones posteriores. El reporte, tal como lo escribió el motor:

# Cada cambio con su aprobación · Software Austral Sintético · periodo 2026-10

**Entidad:** Software Austral Sintético (76543210-K) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Fausto, versión 0.1.0 · **Comando:** `change-check`

## Lo que hay que atender

| # | Señal | Qué | Días | Cita |
|---|---|---|---|---|
| 1 | `change_without_approval` | CHG-220 · Cambio de la regla del cortafuegos de la red interna: se implementó el 2026-10-16 y el comité lo aprobó el 2026-10-22, después | 6 | `10-cambios/cambios_2026-10.xlsx` fila 8 |
| 2 | `change_without_approval` | CHG-210 · Migración del servidor de archivos: se implementó el 2026-10-06 sin una aprobación en las actas del comité de cambios | — | `10-cambios/cambios_2026-10.xlsx` fila 7 |
| 3 | `deployment_without_change` | D-510 · Motor de reglas: desplegado en producción el 2026-10-14 sin un cambio que lo autorice | — | `10-cambios/despliegues_2026-10.xlsx` fila 5 |
| 4 | `deployment_without_change` | D-520 · Servicio de notificaciones: desplegado en producción el 2026-10-23 con el cambio CHG-999, que no está en la exportación de cambios | — | `10-cambios/despliegues_2026-10.xlsx` fila 6 |
| 5 | `emergency_change_without_review` | CHG-310 · Reinicio de emergencia del clúster de base de datos: implementado el 2026-10-03; la política da 5 días para su revisión posterior y no tiene revisión en las actas | 48 | `10-cambios/cambios_2026-10.xlsx` fila 9 |
| 6 | `emergency_change_without_review` | CHG-320 · Parche de emergencia del servidor de aplicaciones: implementado el 2026-10-09; la política da 5 días para su revisión posterior y se revisó el 2026-10-22, tarde | 42 | `10-cambios/cambios_2026-10.xlsx` fila 10 |
| 7 | `failed_change_without_review` | CHG-410 · Actualización del sistema de nómina: terminó como «Revertido» el 2026-10-07 y no tiene revisión posterior en las actas | — | `10-cambios/cambios_2026-10.xlsx` fila 11 |
| 8 | `failed_change_without_review` | CHG-420 · Nueva versión de la aplicación móvil: terminó como «Fallido» el 2026-10-13 y no tiene revisión posterior en las actas | — | `10-cambios/cambios_2026-10.xlsx` fila 12 |

## El resultado

**Días de la política para revisar un cambio de emergencia:** 5.

| Cambio | Tipo | Implementado | Resultado | Aprobado | Revisado |
|---|---|---|---|---|---|
| CHG-100 | Normal | 2026-10-05 | Exitoso | 2026-10-01 | — |
| CHG-101 | Estándar | 2026-10-20 | Exitoso | — | — |
| CHG-102 | Emergencia | 2026-10-10 | Exitoso | — | 2026-10-15 |
| CHG-103 | Normal | 2026-10-08 | Exitoso | 2026-10-08 | — |
| CHG-104 | Normal | 2026-10-12 | Revertido | 2026-10-08 | 2026-10-15 |
| CHG-210 | Normal | 2026-10-06 | Exitoso | — | — |
| CHG-220 | Normal | 2026-10-16 | Exitoso | 2026-10-22 | — |
| CHG-310 | Emergencia | 2026-10-03 | Exitoso | — | — |
| CHG-320 | Emergencia | 2026-10-09 | Exitoso | — | 2026-10-22 |
| CHG-410 | Normal | 2026-10-07 | Revertido | 2026-10-01 | — |
| CHG-420 | Normal | 2026-10-13 | Fallido | 2026-10-08 | — |

| Despliegue | Fecha | Sistema | Cambio | En la exportación |
|---|---|---|---|---|
| D-100 | 2026-10-05 | Portal | CHG-100 | sí |
| D-101 | 2026-10-08 | Portal | CHG-103 | sí |
| D-510 | 2026-10-14 | Motor de reglas | — | no |
| D-520 | 2026-10-23 | Servicio de notificaciones | CHG-999 | no |

Si un cambio se aprueba lo decide el comité de cambios: aquí se dice cuál llegó a producción sin su aprobación o sin su revisión.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `10-cambios/cambios_2026-10.xlsx`
- `10-cambios/despliegues_2026-10.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cto/FUENTES.es.md)

---

En la tabla de señales quité las columnas Monto y Responsable porque el motor las dejó vacías. El reporte completo está en `estado-tecnologia/76543210-k-software-austral-sintetico/cambios/2026-10/reporte-change-check.md`.

El cruce del periodo encontró 12 señales en total. Las 4 que no aparecen aquí son de incidentes mayores sin su problema y de servicios por debajo de su nivel; se ven con `/criterio-changes:incident-check` y `/criterio-changes:service-check`.

**Cuándo vuelvo:** sin reloj. La tarea programada necesita un sí explícito y en esta sesión nadie podía darlo. Se corre a mano con `/criterio-changes:changes-wake`.

La corrida quedó registrada como `2026-11-25-changes-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.