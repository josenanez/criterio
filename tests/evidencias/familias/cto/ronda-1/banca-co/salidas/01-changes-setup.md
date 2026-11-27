# /criterio-changes:changes-setup tecnologia/901222444-banco-meridiano-sintetico

Fausto quedó configurado para Banco Meridiano Sintético (901222444), periodo 2026-10. La configuración está en `.criterio/cambios/901222444/config.json` y el comprobante de los términos en `.criterio/terminos/aceptacion-criterio-changes-0.1.0-2026-11-25.md` (y su PDF).

Procesé las cuatro actas del comité de cambios de octubre y llevé sus aprobaciones y revisiones posteriores a la ficha. CHG-210 no cuenta como aprobado: en el acta del 2026-10-01 quedó «pendiente de más información». En este reporte solo están los cambios y los despliegues. Las señales de incidentes y de niveles de servicio que encontró el cálculo salen con `/criterio-changes:incident-check` y `/criterio-changes:service-check`.

# Cada cambio con su aprobación · Banco Meridiano Sintético · periodo 2026-10

**Entidad:** Banco Meridiano Sintético (901222444) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Fausto, versión 0.1.0 · **Comando:** `change-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un cambio normal se implementó sin la aprobación de su autoridad de cambio, o antes de ella (`change_without_approval`) | CHG-220 · Cambio de la regla del cortafuegos de la red interna: se implementó el 2026-10-16 y el comité lo aprobó el 2026-10-22, después | — | — | 6 | `10-cambios/cambios_2026-10.xlsx` fila 8 |
| 2 | Un cambio normal se implementó sin la aprobación de su autoridad de cambio, o antes de ella (`change_without_approval`) | CHG-210 · Migración del servidor de archivos: se implementó el 2026-10-06 sin una aprobación en las actas del comité de cambios | — | — | — | `10-cambios/cambios_2026-10.xlsx` fila 7 |
| 3 | Un cambio normal se implementó sin la aprobación de su autoridad de cambio, o antes de ella (`change_without_approval`) | CHG-230 · Nueva integración con el proveedor de mensajería: se implementó el 2026-10-26 sin una aprobación en las actas del comité de cambios | — | — | — | `10-cambios/cambios_2026-10.xlsx` fila 9 |
| 4 | Un despliegue en producción no corresponde a ningún cambio registrado (`deployment_without_change`) | D-510 · Motor de reglas: desplegado en producción el 2026-10-14 sin un cambio que lo autorice | — | — | — | `10-cambios/despliegues_2026-10.xlsx` fila 5 |
| 5 | Un despliegue en producción no corresponde a ningún cambio registrado (`deployment_without_change`) | D-520 · Servicio de notificaciones: desplegado en producción el 2026-10-23 con el cambio CHG-999, que no está en la exportación de cambios | — | — | — | `10-cambios/despliegues_2026-10.xlsx` fila 6 |
| 6 | Un despliegue en producción no corresponde a ningún cambio registrado (`deployment_without_change`) | D-530 · Tablero de ventas: desplegado en producción el 2026-10-28 sin un cambio que lo autorice | — | — | — | `10-cambios/despliegues_2026-10.xlsx` fila 7 |
| 7 | Un cambio de emergencia no tiene su revisión posterior en el plazo de la política (`emergency_change_without_review`) | CHG-310 · Reinicio de emergencia del clúster de base de datos: cambio de emergencia implementado el 2026-10-03; la política da 5 días para su revisión posterior y no tiene revisión en las actas | — | — | 48 | `10-cambios/cambios_2026-10.xlsx` fila 10 |
| 8 | Un cambio de emergencia no tiene su revisión posterior en el plazo de la política (`emergency_change_without_review`) | CHG-320 · Parche de emergencia del servidor de aplicaciones: cambio de emergencia implementado el 2026-10-09; la política da 5 días para su revisión posterior y se revisó el 2026-10-22, tarde | — | — | 42 | `10-cambios/cambios_2026-10.xlsx` fila 11 |
| 9 | Un cambio de emergencia no tiene su revisión posterior en el plazo de la política (`emergency_change_without_review`) | CHG-330 · Reversión de emergencia del balanceador: cambio de emergencia implementado el 2026-10-18; la política da 5 días para su revisión posterior y no tiene revisión en las actas | — | — | 33 | `10-cambios/cambios_2026-10.xlsx` fila 12 |
| 10 | Un cambio fallido o revertido no tiene su revisión posterior (`failed_change_without_review`) | CHG-410 · Actualización del sistema de nómina: terminó como «Revertido» el 2026-10-07 y no tiene revisión posterior en las actas | — | — | — | `10-cambios/cambios_2026-10.xlsx` fila 13 |
| 11 | Un cambio fallido o revertido no tiene su revisión posterior (`failed_change_without_review`) | CHG-420 · Nueva versión de la aplicación móvil: terminó como «Fallido» el 2026-10-13 y no tiene revisión posterior en las actas | — | — | — | `10-cambios/cambios_2026-10.xlsx` fila 14 |
| 12 | Un cambio fallido o revertido no tiene su revisión posterior (`failed_change_without_review`) | CHG-430 · Cambio del esquema del almacén de datos: terminó como «Revertido» el 2026-10-21 y no tiene revisión posterior en las actas | — | — | — | `10-cambios/cambios_2026-10.xlsx` fila 15 |

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
| CHG-230 | Normal | 2026-10-26 | Exitoso | — | — |
| CHG-310 | Emergencia | 2026-10-03 | Exitoso | — | — |
| CHG-320 | Emergencia | 2026-10-09 | Exitoso | — | 2026-10-22 |
| CHG-330 | Emergencia | 2026-10-18 | Exitoso | — | — |
| CHG-410 | Normal | 2026-10-07 | Revertido | 2026-10-01 | — |
| CHG-420 | Normal | 2026-10-13 | Fallido | 2026-10-08 | — |
| CHG-430 | Normal | 2026-10-21 | Revertido | 2026-10-15 | — |

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

**Cuándo vuelvo:** sin reloj. En esta sesión de prueba nadie dio un sí explícito a la tarea programada. Para correrlo a mano: `/criterio-changes:changes-wake`.

La carpeta quedó sin la marca `_CRITERIO_TECNOLOGIA.txt`, porque nadie la autorizó.

La corrida quedó registrada como `2026-11-25-changes-setup-1`, y lo que se mostró está en `estado-tecnologia/901222444-banco-meridiano-sintetico/corridas/salida-changes-setup.md`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.