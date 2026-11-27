# /criterio-changes:change-check 

Los términos de esta versión están vigentes. En la tabla del reporte ningún cambio trae aprobación ni revisión. Si las actas del comité de cambios no se han procesado, conviene correr primero `/criterio-changes:changes-scan`.

# Cada cambio con su aprobación · Retail del Golfo Sintético · periodo 2026-11

**Entidad:** Retail del Golfo Sintético (RGS180610QW4) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Fausto, versión 0.1.0 · **Comando:** `change-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un cambio normal se implementó sin la aprobación de su autoridad de cambio, o antes de ella (`change_without_approval`) | CHG-100 · Actualización del certificado del portal: se implementó el 2026-10-05 sin una aprobación en las actas del comité de cambios | — | — | — | `10-cambios/cambios_2026-10.xlsx` fila 2 |
| 2 | Un cambio normal se implementó sin la aprobación de su autoridad de cambio, o antes de ella (`change_without_approval`) | CHG-103 · Ajuste del límite de sesiones: se implementó el 2026-10-08 sin una aprobación en las actas del comité de cambios | — | — | — | `10-cambios/cambios_2026-10.xlsx` fila 5 |
| 3 | Un cambio normal se implementó sin la aprobación de su autoridad de cambio, o antes de ella (`change_without_approval`) | CHG-104 · Nueva versión del motor de pagos: se implementó el 2026-10-12 sin una aprobación en las actas del comité de cambios | — | — | — | `10-cambios/cambios_2026-10.xlsx` fila 6 |
| 4 | Un cambio normal se implementó sin la aprobación de su autoridad de cambio, o antes de ella (`change_without_approval`) | CHG-210 · Migración del servidor de archivos: se implementó el 2026-10-06 sin una aprobación en las actas del comité de cambios | — | — | — | `10-cambios/cambios_2026-10.xlsx` fila 7 |
| 5 | Un cambio normal se implementó sin la aprobación de su autoridad de cambio, o antes de ella (`change_without_approval`) | CHG-220 · Cambio de la regla del cortafuegos de la red interna: se implementó el 2026-10-16 sin una aprobación en las actas del comité de cambios | — | — | — | `10-cambios/cambios_2026-10.xlsx` fila 8 |
| 6 | Un cambio normal se implementó sin la aprobación de su autoridad de cambio, o antes de ella (`change_without_approval`) | CHG-230 · Nueva integración con el proveedor de mensajería: se implementó el 2026-10-26 sin una aprobación en las actas del comité de cambios | — | — | — | `10-cambios/cambios_2026-10.xlsx` fila 9 |
| 7 | Un cambio normal se implementó sin la aprobación de su autoridad de cambio, o antes de ella (`change_without_approval`) | CHG-410 · Actualización del sistema de nómina: se implementó el 2026-10-07 sin una aprobación en las actas del comité de cambios | — | — | — | `10-cambios/cambios_2026-10.xlsx` fila 13 |
| 8 | Un cambio normal se implementó sin la aprobación de su autoridad de cambio, o antes de ella (`change_without_approval`) | CHG-420 · Nueva versión de la aplicación móvil: se implementó el 2026-10-13 sin una aprobación en las actas del comité de cambios | — | — | — | `10-cambios/cambios_2026-10.xlsx` fila 14 |
| 9 | Un cambio normal se implementó sin la aprobación de su autoridad de cambio, o antes de ella (`change_without_approval`) | CHG-430 · Cambio del esquema del almacén de datos: se implementó el 2026-10-21 sin una aprobación en las actas del comité de cambios | — | — | — | `10-cambios/cambios_2026-10.xlsx` fila 15 |
| 10 | Un despliegue en producción no corresponde a ningún cambio registrado (`deployment_without_change`) | D-510 · Motor de reglas: desplegado en producción el 2026-10-14 sin un cambio que lo autorice | — | — | — | `10-cambios/despliegues_2026-10.xlsx` fila 5 |
| 11 | Un despliegue en producción no corresponde a ningún cambio registrado (`deployment_without_change`) | D-520 · Servicio de notificaciones: desplegado en producción el 2026-10-23 con el cambio CHG-999, que no está en la exportación de cambios | — | — | — | `10-cambios/despliegues_2026-10.xlsx` fila 6 |
| 12 | Un despliegue en producción no corresponde a ningún cambio registrado (`deployment_without_change`) | D-530 · Tablero de ventas: desplegado en producción el 2026-10-28 sin un cambio que lo autorice | — | — | — | `10-cambios/despliegues_2026-10.xlsx` fila 7 |
| 13 | Un cambio de emergencia no tiene su revisión posterior en el plazo de la política (`emergency_change_without_review`) | CHG-310 · Reinicio de emergencia del clúster de base de datos: cambio de emergencia implementado el 2026-10-03; la política da 5 días para su revisión posterior y no tiene revisión en las actas | — | — | 48 | `10-cambios/cambios_2026-10.xlsx` fila 10 |
| 14 | Un cambio de emergencia no tiene su revisión posterior en el plazo de la política (`emergency_change_without_review`) | CHG-320 · Parche de emergencia del servidor de aplicaciones: cambio de emergencia implementado el 2026-10-09; la política da 5 días para su revisión posterior y no tiene revisión en las actas | — | — | 42 | `10-cambios/cambios_2026-10.xlsx` fila 11 |
| 15 | Un cambio de emergencia no tiene su revisión posterior en el plazo de la política (`emergency_change_without_review`) | CHG-102 · Corrección de la conciliación de pagos: cambio de emergencia implementado el 2026-10-10; la política da 5 días para su revisión posterior y no tiene revisión en las actas | — | — | 41 | `10-cambios/cambios_2026-10.xlsx` fila 4 |
| 16 | Un cambio de emergencia no tiene su revisión posterior en el plazo de la política (`emergency_change_without_review`) | CHG-330 · Reversión de emergencia del balanceador: cambio de emergencia implementado el 2026-10-18; la política da 5 días para su revisión posterior y no tiene revisión en las actas | — | — | 33 | `10-cambios/cambios_2026-10.xlsx` fila 12 |
| 17 | Un cambio fallido o revertido no tiene su revisión posterior (`failed_change_without_review`) | CHG-104 · Nueva versión del motor de pagos: terminó como «Revertido» el 2026-10-12 y no tiene revisión posterior en las actas | — | — | — | `10-cambios/cambios_2026-10.xlsx` fila 6 |
| 18 | Un cambio fallido o revertido no tiene su revisión posterior (`failed_change_without_review`) | CHG-410 · Actualización del sistema de nómina: terminó como «Revertido» el 2026-10-07 y no tiene revisión posterior en las actas | — | — | — | `10-cambios/cambios_2026-10.xlsx` fila 13 |
| 19 | Un cambio fallido o revertido no tiene su revisión posterior (`failed_change_without_review`) | CHG-420 · Nueva versión de la aplicación móvil: terminó como «Fallido» el 2026-10-13 y no tiene revisión posterior en las actas | — | — | — | `10-cambios/cambios_2026-10.xlsx` fila 14 |
| 20 | Un cambio fallido o revertido no tiene su revisión posterior (`failed_change_without_review`) | CHG-430 · Cambio del esquema del almacén de datos: terminó como «Revertido» el 2026-10-21 y no tiene revisión posterior en las actas | — | — | — | `10-cambios/cambios_2026-10.xlsx` fila 15 |

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
| CHG-230 | Normal | 2026-10-26 | Exitoso | — | — |
| CHG-310 | Emergencia | 2026-10-03 | Exitoso | — | — |
| CHG-320 | Emergencia | 2026-10-09 | Exitoso | — | — |
| CHG-330 | Emergencia | 2026-10-18 | Exitoso | — | — |
| CHG-410 | Normal | 2026-10-07 | Revertido | — | — |
| CHG-420 | Normal | 2026-10-13 | Fallido | — | — |
| CHG-430 | Normal | 2026-10-21 | Revertido | — | — |

| Despliegue | Fecha | Sistema | Cambio | En la exportación |
|---|---|---|---|---|
| D-100 | 2026-10-05 | Portal | CHG-100 | sí |
| D-101 | 2026-10-08 | Portal | CHG-103 | sí |
| D-510 | 2026-10-14 | Motor de reglas | — | no |
| D-520 | 2026-10-23 | Servicio de notificaciones | CHG-999 | no |
| D-530 | 2026-10-28 | Tablero de ventas | — | no |

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

La corrida quedó registrada como `2026-11-25-change-check-1`. El motor la cuenta con 18 hallazgos. El reporte lista 20 filas, y no sé explicar la diferencia, así que no la he forzado. La salida completa está en `estado-tecnologia/rgs180610qw4-retail-del-golfo-sintetico/corridas/salida-change-check.md`.

Esta sesión de prueba no tuvo que registrar la aceptación de términos, porque el motor ya la daba por vigente (versión instalada 0.1.0).