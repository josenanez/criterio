# /criterio-changes:change-check 

Ningún cambio ni revisión aparece aprobado en el reporte. Las actas del comité de cambios no están en la ficha del periodo, así que las señales de aprobación y revisión salen abiertas. Para llevar las actas a la ficha, corre `/criterio-changes:changes-scan`. La decisión sobre cada cambio es del comité de cambios.

# Cada cambio con su aprobación · Software Austral Sintético · periodo 2026-11

**Entidad:** Software Austral Sintético (76543210-K) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Fausto, versión 0.1.0 · **Comando:** `change-check`

## Lo que hay que atender

| # | Señal | Qué | Días | Cita |
|---|---|---|---|---|
| 1 | Cambio normal implementado sin aprobación, o antes de ella (`change_without_approval`) | CHG-100 · Actualización del certificado del portal: implementado el 2026-10-05, sin aprobación en las actas | — | `cambios_2026-10.xlsx` fila 2 |
| 2 | ídem | CHG-103 · Ajuste del límite de sesiones: 2026-10-08 | — | fila 5 |
| 3 | ídem | CHG-104 · Nueva versión del motor de pagos: 2026-10-12 | — | fila 6 |
| 4 | ídem | CHG-210 · Migración del servidor de archivos: 2026-10-06 | — | fila 7 |
| 5 | ídem | CHG-220 · Cambio de la regla del cortafuegos de la red interna: 2026-10-16 | — | fila 8 |
| 6 | ídem | CHG-410 · Actualización del sistema de nómina: 2026-10-07 | — | fila 11 |
| 7 | ídem | CHG-420 · Nueva versión de la aplicación móvil: 2026-10-13 | — | fila 12 |
| 8 | Despliegue en producción sin cambio registrado (`deployment_without_change`) | D-510 · Motor de reglas: desplegado el 2026-10-14 sin un cambio que lo autorice | — | `despliegues_2026-10.xlsx` fila 5 |
| 9 | ídem | D-520 · Servicio de notificaciones: desplegado el 2026-10-23 con CHG-999, que no está en la exportación de cambios | — | fila 6 |
| 10 | Cambio de emergencia sin revisión en el plazo (`emergency_change_without_review`) | CHG-310 · Reinicio de emergencia del clúster de base de datos: implementado el 2026-10-03; la política da 5 días y no hay revisión en las actas | 48 | `cambios_2026-10.xlsx` fila 9 |
| 11 | ídem | CHG-320 · Parche de emergencia del servidor de aplicaciones: 2026-10-09 | 42 | fila 10 |
| 12 | ídem | CHG-102 · Corrección de la conciliación de pagos: 2026-10-10 | 41 | fila 4 |
| 13 | Cambio fallido o revertido sin revisión posterior (`failed_change_without_review`) | CHG-104 · «Revertido» el 2026-10-12 | — | fila 6 |
| 14 | ídem | CHG-410 · «Revertido» el 2026-10-07 | — | fila 11 |
| 15 | ídem | CHG-420 · «Fallido» el 2026-10-13 | — | fila 12 |

## El resultado

**Días de la política para revisar un cambio de emergencia:** 5.

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

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `10-cambios/cambios_2026-10.xlsx`
- `10-cambios/despliegues_2026-10.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cto/FUENTES.es.md)

---

La corrida quedó registrada como `2026-11-25-change-check-1`. El reporte está en `estado-tecnologia/76543210-k-software-austral-sintetico/cambios/2026-11/reporte-change-check.md`.

Dos aclaraciones sobre cómo se corrió:
- **Términos:** el motor los dio por vigentes. No hizo falta registrar la aceptación de José Francisco Ñáñez y no la registré.
- **Tabla del reporte:** acorté las columnas vacías (Monto y Responsable) y escribí «ídem» en las filas repetidas. El texto completo de cada señal está en el archivo del reporte.