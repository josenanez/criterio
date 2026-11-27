# /criterio-changes:changes-wake 

Esta fue la revisión semanal de Software Austral Sintético. No llegaron documentos nuevos, cambiados ni borrados, y nadie dejó peticiones. Los términos ya estaban aceptados, así que no hubo que registrar nada. Lo único pendiente hoy era `changes-scan`. En la ficha de 2026-10 no faltaba ningún documento, y el motor escribió este reporte:

# Qué cambió en los cambios · Software Austral Sintético · periodo 2026-10

**Entidad:** Software Austral Sintético (76543210-K) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Fausto, versión 0.1.0 · **Comando:** `changes-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un cambio normal se implementó sin la aprobación de su autoridad de cambio, o antes de ella (`change_without_approval`) | CHG-220 · Cambio de la regla del cortafuegos de la red interna: se implementó el 2026-10-16 y el comité lo aprobó el 2026-10-22, después | — | — | 6 | `10-cambios/cambios_2026-10.xlsx` fila 8 |
| 2 | Un cambio normal se implementó sin la aprobación de su autoridad de cambio, o antes de ella (`change_without_approval`) | CHG-210 · Migración del servidor de archivos: se implementó el 2026-10-06 sin una aprobación en las actas del comité de cambios | — | — | — | `10-cambios/cambios_2026-10.xlsx` fila 7 |
| 3 | Un despliegue en producción no corresponde a ningún cambio registrado (`deployment_without_change`) | D-510 · Motor de reglas: desplegado en producción el 2026-10-14 sin un cambio que lo autorice | — | — | — | `10-cambios/despliegues_2026-10.xlsx` fila 5 |
| 4 | Un despliegue en producción no corresponde a ningún cambio registrado (`deployment_without_change`) | D-520 · Servicio de notificaciones: desplegado en producción el 2026-10-23 con el cambio CHG-999, que no está en la exportación de cambios | — | — | — | `10-cambios/despliegues_2026-10.xlsx` fila 6 |
| 5 | Un cambio de emergencia no tiene su revisión posterior en el plazo de la política (`emergency_change_without_review`) | CHG-310 · Reinicio de emergencia del clúster de base de datos: cambio de emergencia implementado el 2026-10-03; la política da 5 días para su revisión posterior y no tiene revisión en las actas | — | — | 48 | `10-cambios/cambios_2026-10.xlsx` fila 9 |
| 6 | Un cambio de emergencia no tiene su revisión posterior en el plazo de la política (`emergency_change_without_review`) | CHG-320 · Parche de emergencia del servidor de aplicaciones: cambio de emergencia implementado el 2026-10-09; la política da 5 días para su revisión posterior y se revisó el 2026-10-22, tarde | — | — | 42 | `10-cambios/cambios_2026-10.xlsx` fila 10 |
| 7 | Un incidente mayor no tiene un registro de problema con su causa en el plazo de la política (`major_incident_without_problem`) | INC-610 · S-02: incidente mayor resuelto el 2026-10-04; no tiene un registro de problema, y la política da 10 días | — | — | 42 | `20-servicio/incidentes_2026-10.xlsx` fila 5 |
| 8 | Un incidente mayor no tiene un registro de problema con su causa en el plazo de la política (`major_incident_without_problem`) | INC-620 · S-01: incidente mayor resuelto el 2026-10-12; su problema, PRB-620, no tiene causa, y la política da 10 días | — | — | 34 | `20-servicio/incidentes_2026-10.xlsx` fila 6 · `20-servicio/problemas.xlsx` fila 3 |
| 9 | Un cambio fallido o revertido no tiene su revisión posterior (`failed_change_without_review`) | CHG-410 · Actualización del sistema de nómina: terminó como «Revertido» el 2026-10-07 y no tiene revisión posterior en las actas | — | — | — | `10-cambios/cambios_2026-10.xlsx` fila 11 |
| 10 | Un cambio fallido o revertido no tiene su revisión posterior (`failed_change_without_review`) | CHG-420 · Nueva versión de la aplicación móvil: terminó como «Fallido» el 2026-10-13 y no tiene revisión posterior en las actas | — | — | — | `10-cambios/cambios_2026-10.xlsx` fila 12 |
| 11 | La disponibilidad de un servicio en el periodo quedó por debajo del nivel acordado en el catálogo (`service_below_level`) | S-11 · Pagos en línea: dio 99.4 % de disponibilidad en 2026-10 y el catálogo acuerda 99.9 % | — | — | — | `20-servicio/disponibilidad_2026-10.xlsx` fila 5 · `00-politica/catalogo_de_servicios.xlsx` fila 5 |
| 12 | La disponibilidad de un servicio en el periodo quedó por debajo del nivel acordado en el catálogo (`service_below_level`) | S-12 · Aplicación móvil: dio 98.7 % de disponibilidad en 2026-10 y el catálogo acuerda 99.5 % | — | — | — | `20-servicio/disponibilidad_2026-10.xlsx` fila 6 · `00-politica/catalogo_de_servicios.xlsx` fila 6 |

## El resultado

**Cambios en la exportación:** 11 · **Despliegues en producción:** 4 · **Incidentes mayores:** 4 · **Servicios medidos:** 5 · **Aprobaciones y revisiones en la ficha:** 6 y 3.

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

---

Las dos corridas quedaron registradas con el periodo 2026-10: `2026-11-25-changes-scan-2` y `2026-11-25-changes-wake-1`. Lo que mostré está guardado en `<espacio>/estado-tecnologia/76543210-k-software-austral-sintetico/corridas/salida-changes-wake.md`. Las decisiones sobre estas señales les tocan al comité de cambios y al área de tecnología.