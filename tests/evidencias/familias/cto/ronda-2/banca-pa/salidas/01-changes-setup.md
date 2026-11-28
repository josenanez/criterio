# /criterio-changes:changes-setup tecnologia/155612345-2-2019-banco-del-istmo-sintetico

Fausto ya está configurado para el Banco del Istmo Sintético, y el primer reporte de octubre de 2026 muestra 8 cambios y despliegues que llegaron a producción sin la aprobación o la revisión que pide la política.

- **Configuración:** `.criterio/cambios/155612345-2-2019/config.json`. Las respuestas que no estaban en los documentos son las sugeridas: país PA y moneda USD. Los plazos salen de la política: 5 días para revisar un cambio de emergencia y 10 para registrar el problema de un incidente mayor.
- **Términos v1.6:** aceptados por José Francisco Ñáñez el 2026-11-25. El comprobante quedó en `.criterio/terminos/aceptacion-criterio-changes-0.2.0-2026-11-25.md` y `.pdf`.
- **Sin marca y sin tarea programada:** nadie podía decir que sí. Para correrlo a mano: `/criterio-changes:changes-wake`.
- **Ficha:** procesé las cuatro actas del comité de cambios. La ficha registra 6 aprobaciones y 3 revisiones posteriores.
- **Lo que falta mirar:** el cálculo dio 12 señales. Las 4 de incidentes y servicios salen en `/criterio-changes:incident-check` y `/criterio-changes:service-check`; todavía no las he revisado.

# Cada cambio con su aprobación · Banco del Istmo Sintético · periodo 2026-10

**Entidad:** Banco del Istmo Sintético (155612345-2-2019) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Fausto, versión 0.2.0 · **Comando:** `change-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un cambio normal se implementó sin la aprobación de su autoridad de cambio, o antes de ella (`change_without_approval`) | CHG-220 · Cambio de la regla del cortafuegos de la red interna: se implementó el 2026-10-16 y el comité lo aprobó el 2026-10-22, después | — | — | 6 | `10-cambios/cambios_2026-10.xlsx` fila 8 |
| 2 | Un cambio normal se implementó sin la aprobación de su autoridad de cambio, o antes de ella (`change_without_approval`) | CHG-210 · Migración del servidor de archivos: se implementó el 2026-10-06 sin una aprobación en las actas del comité de cambios | — | — | — | `10-cambios/cambios_2026-10.xlsx` fila 7 |
| 3 | Un despliegue en producción no corresponde a ningún cambio registrado (`deployment_without_change`) | D-510 · Motor de reglas: desplegado en producción el 2026-10-14 sin un cambio que lo autorice | — | — | — | `10-cambios/despliegues_2026-10.xlsx` fila 5 |
| 4 | Un despliegue en producción no corresponde a ningún cambio registrado (`deployment_without_change`) | D-520 · Servicio de notificaciones: desplegado en producción el 2026-10-23 con el cambio CHG-999, que no está en la exportación de cambios | — | — | — | `10-cambios/despliegues_2026-10.xlsx` fila 6 |
| 5 | Un cambio de emergencia no tiene su revisión posterior en el plazo de la política (`emergency_change_without_review`) | CHG-310 · Reinicio de emergencia del clúster de base de datos: cambio de emergencia implementado el 2026-10-03; la política da 5 días para su revisión posterior y no tiene revisión en las actas | — | — | 48 | `10-cambios/cambios_2026-10.xlsx` fila 9 |
| 6 | Un cambio de emergencia no tiene su revisión posterior en el plazo de la política (`emergency_change_without_review`) | CHG-320 · Parche de emergencia del servidor de aplicaciones: cambio de emergencia implementado el 2026-10-09; la política da 5 días para su revisión posterior y se revisó el 2026-10-22, tarde | — | — | 42 | `10-cambios/cambios_2026-10.xlsx` fila 10 |
| 7 | Un cambio fallido o revertido no tiene su revisión posterior (`failed_change_without_review`) | CHG-410 · Actualización del sistema de nómina: terminó como «Revertido» el 2026-10-07 y no tiene revisión posterior en las actas | — | — | — | `10-cambios/cambios_2026-10.xlsx` fila 11 |
| 8 | Un cambio fallido o revertido no tiene su revisión posterior (`failed_change_without_review`) | CHG-420 · Nueva versión de la aplicación móvil: terminó como «Fallido» el 2026-10-13 y no tiene revisión posterior en las actas | — | — | — | `10-cambios/cambios_2026-10.xlsx` fila 12 |

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

La corrida quedó registrada como `2026-11-25-changes-setup-1` con 12 hallazgos. La salida está en `estado-tecnologia/155612345-2-2019-banco-del-istmo-sintetico/corridas/salida-changes-setup.md`. **Cuándo vuelvo:** sin reloj.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.