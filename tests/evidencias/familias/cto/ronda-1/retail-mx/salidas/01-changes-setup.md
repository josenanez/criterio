# /criterio-changes:changes-setup tecnologia/rgs180610qw4-retail-del-golfo-sintetico

Soy Fausto. Pongo cada cambio al lado de su aprobación y cada servicio al lado de su nivel; no apruebo cambios ni califico incidentes.

Usé esta carpeta: 1. `tecnologia/rgs180610qw4-retail-del-golfo-sintetico`. Es la única candidata y tiene 00-politica/, 10-cambios/, 20-servicio/, 30-activos/, 40-proveedores/ y 50-nube/. Procesé 24 documentos; ninguno estaba fuera de lugar ni era ilegible.

**Respuestas tomadas de los documentos, una por pregunta:**
1. **Entidad:** Retail del Golfo Sintético, RFC RGS180610QW4, México (MXN).
2. **Periodo:** 2026-10, que es el que traen las tablas.
3. **Revisión de un cambio de emergencia:** 5 días, según la política aprobada el 2025-11-20.
4. **Problema de un incidente mayor:** 10 días, según la misma política.
5. **Publicar en Rostrum:** sí. Es la opción por omisión y la política no dice otra cosa.
6. **Estado:** `estado-tecnologia/rgs180610qw4-retail-del-golfo-sintetico`.
7. **Términos (v1.6):** «Criterio entrega a la dirección análisis contrastado contra la evidencia: cada cifra, cada señal y cada vencimiento con la cita del documento del que sale. No sustituye el juicio de quien decide ni la asesoría profesional: la decisión, y su verificación, son de quien la firma. Procesa los documentos que usted le indique y dice lo que muestran; lo que se acordó fuera de ellos no lo conoce. Lo ejecuta un modelo de lenguaje (LLM), que puede equivocarse, y por eso ningún dato llega sin su fuente. Sus documentos se procesan en la infraestructura de la plataforma de IA donde lo ejecuta, no solo en su equipo. Cada versión se prueba antes de publicarse y su evidencia es pública; la garantía y la responsabilidad son las de la licencia Apache 2.0. Se acepta una vez y deja un comprobante en Markdown y PDF con su huella SHA-256; actualizar no pide aceptar de nuevo, salvo que estos términos cambien. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal». Acepta José Francisco Ñáñez, el 2026-11-25.
8. **Marca de la carpeta:** sí. Quedó `_CRITERIO_TECNOLOGIA.txt`.

**Dónde quedó todo:**
- **Configuración:** `.criterio/cambios/RGS180610QW4/config.json`
- **Comprobante de los términos:** `.criterio/terminos/aceptacion-criterio-changes-0.1.0-2026-11-25.md` y `.pdf`

**Ficha:** pasé a la ficha las 4 actas del comité de cambios, con 7 aprobaciones y 3 revisiones posteriores. CHG-210 no entró como aprobado: el acta del 2026-10-01 lo deja «pendiente de más información».

---

# Cada cambio con su aprobación · Retail del Golfo Sintético · periodo 2026-10

**Entidad:** Retail del Golfo Sintético (RGS180610QW4) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Fausto, versión 0.1.0 · **Comando:** `change-check`

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

**Cuándo vuelvo:** sin reloj. En esta sesión de prueba nadie dio el sí para una tarea programada. Se corre a mano con `/criterio-changes:changes-wake`.

La corrida quedó registrada como `2026-11-25-changes-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.