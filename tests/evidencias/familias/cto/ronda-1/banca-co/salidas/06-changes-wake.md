# /criterio-changes:changes-wake 

Hoy tocaba la revisión semanal de changes-scan para Banco Meridiano Sintético (901222444). No había peticiones abiertas y los términos están vigentes. No llegaron documentos nuevos, modificados ni borrados desde la corrida anterior. La ficha del periodo ya tenía las aprobaciones y revisiones de las actas de `10-cambios/`, y no faltaba ningún documento en ella. Las dos corridas quedaron registradas: `2026-11-25-changes-scan-2` y `2026-11-25-changes-wake-1`.

# Qué cambió en los cambios · Banco Meridiano Sintético · periodo 2026-10

**Entidad:** Banco Meridiano Sintético (901222444) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Fausto, versión 0.1.0 · **Comando:** `changes-scan`

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
| 9 | Un incidente mayor no tiene un registro de problema con su causa en el plazo de la política (`major_incident_without_problem`) | INC-610 · S-02: incidente mayor resuelto el 2026-10-04; no tiene un registro de problema, y la política da 10 días | — | — | 42 | `20-servicio/incidentes_2026-10.xlsx` fila 5 |
| 10 | Un incidente mayor no tiene un registro de problema con su causa en el plazo de la política (`major_incident_without_problem`) | INC-620 · S-01: incidente mayor resuelto el 2026-10-12; su problema, PRB-620, no tiene causa, y la política da 10 días | — | — | 34 | `20-servicio/incidentes_2026-10.xlsx` fila 6 · `20-servicio/problemas.xlsx` fila 3 |
| 11 | Un cambio de emergencia no tiene su revisión posterior en el plazo de la política (`emergency_change_without_review`) | CHG-330 · Reversión de emergencia del balanceador: cambio de emergencia implementado el 2026-10-18; la política da 5 días para su revisión posterior y no tiene revisión en las actas | — | — | 33 | `10-cambios/cambios_2026-10.xlsx` fila 12 |
| 12 | Un incidente mayor no tiene un registro de problema con su causa en el plazo de la política (`major_incident_without_problem`) | INC-630 · S-03: incidente mayor resuelto el 2026-10-27; no tiene un registro de problema, y la política da 10 días | — | — | 19 | `20-servicio/incidentes_2026-10.xlsx` fila 7 |
| 13 | Un cambio fallido o revertido no tiene su revisión posterior (`failed_change_without_review`) | CHG-410 · Actualización del sistema de nómina: terminó como «Revertido» el 2026-10-07 y no tiene revisión posterior en las actas | — | — | — | `10-cambios/cambios_2026-10.xlsx` fila 13 |
| 14 | Un cambio fallido o revertido no tiene su revisión posterior (`failed_change_without_review`) | CHG-420 · Nueva versión de la aplicación móvil: terminó como «Fallido» el 2026-10-13 y no tiene revisión posterior en las actas | — | — | — | `10-cambios/cambios_2026-10.xlsx` fila 14 |
| 15 | Un cambio fallido o revertido no tiene su revisión posterior (`failed_change_without_review`) | CHG-430 · Cambio del esquema del almacén de datos: terminó como «Revertido» el 2026-10-21 y no tiene revisión posterior en las actas | — | — | — | `10-cambios/cambios_2026-10.xlsx` fila 15 |
| 16 | La disponibilidad de un servicio en el periodo quedó por debajo del nivel acordado en el catálogo (`service_below_level`) | S-11 · Pagos en línea: dio 99.4 % de disponibilidad en 2026-10 y el catálogo acuerda 99.9 % | — | — | — | `20-servicio/disponibilidad_2026-10.xlsx` fila 5 · `00-politica/catalogo_de_servicios.xlsx` fila 5 |
| 17 | La disponibilidad de un servicio en el periodo quedó por debajo del nivel acordado en el catálogo (`service_below_level`) | S-12 · Aplicación móvil: dio 98.7 % de disponibilidad en 2026-10 y el catálogo acuerda 99.5 % | — | — | — | `20-servicio/disponibilidad_2026-10.xlsx` fila 6 · `00-politica/catalogo_de_servicios.xlsx` fila 6 |
| 18 | La disponibilidad de un servicio en el periodo quedó por debajo del nivel acordado en el catálogo (`service_below_level`) | S-13 · Portal de proveedores: dio 97.9 % de disponibilidad en 2026-10 y el catálogo acuerda 99 % | — | — | — | `20-servicio/disponibilidad_2026-10.xlsx` fila 7 · `00-politica/catalogo_de_servicios.xlsx` fila 7 |

## El resultado

**Cambios en la exportación:** 14 · **Despliegues en producción:** 5 · **Incidentes mayores:** 5 · **Servicios medidos:** 6 · **Aprobaciones y revisiones en la ficha:** 7 y 3.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-politica/catalogo_de_servicios.xlsx`
- `10-cambios/cambios_2026-10.xlsx`
- `10-cambios/despliegues_2026-10.xlsx`
- `20-servicio/disponibilidad_2026-10.xlsx`
- `20-servicio/incidentes_2026-10.xlsx`
- `20-servicio/problemas.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cto/FUENTES.es.md)