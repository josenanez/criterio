[English](DISENO.md) · [← La familia](README.es.md)

# criterio-cto · el diseño de la familia

**Estado: estable, en su versión 0.2.0, sin lanzar.** Los comandos, los skills y el motor de cálculo
se construyen sobre el núcleo común; el motor pasa su prueba determinista contra el material de
`tests/criterio-cto/`. El motor pasa su prueba determinista contra todo el material; en la 0.2.0, la ronda 1 en Colombia, México y Chile: 96 señales y 267 datos, con un piso del 96,1 % en las señales y del 98,5 % en los datos, y ningún control con una señal: [las rondas](../../tests/evidencias/familias/cto/RONDAS.md). Alcance en [ADR 0037](../../docs/decisions/0037-la-familia-cto.md).

**Esta es la hoja de diseño de la familia**: las señales que calcula el código, cada comando con su
entrada, su proceso y su reporte, y las decisiones tomadas. Qué hace la familia, cómo se instala, la
estructura de carpetas y la hoja de ruta están en su [página](README.es.md).

El modelo de lenguaje (LLM) extrae; el código calcula; la decisión —aprobar un cambio, exceptuar un activo,
elegir un proveedor— es siempre del comité de cambios, del comité de arquitectura, del área de tecnología y de
legal. **Los agentes procesan documentos y exportaciones**: nunca se conectan a una herramienta, a la nube ni a
un servidor, y no procesan la seguridad, que es de la familia CISO.

**De dónde sale este documento.** Las tablas de agentes, señales, comandos y cifras no se escriben aquí:
salen de [`familia.json`](familia.json), [`carpetas.json`](carpetas.json) y [`fuentes.json`](fuentes.json).

## Un agente por rol

<!-- cto:agentes · generado por scripts/familias.py; no se edita a mano -->
| Rol | Agente | Plugin | Qué hace |
|---|---|---|---|
| Los cambios y el servicio | **Fausto** — del latín *faustus*, el que trae buena fortuna: cada cambio que sale bien | `criterio-changes` | Cada cambio en producción contra su aprobación y su revisión, cada despliegue contra su cambio, cada incidente mayor contra su problema y cada servicio contra el nivel acordado: el cambio sin aprobar o aprobado después, el de emergencia sin su revisión, el despliegue sin cambio, el cambio fallido sin revisión, el incidente mayor sin causa y el servicio por debajo de su nivel |
| Los activos y los proveedores | **Domingo** — del latín *dominicus*, el del dueño: cada activo con quien responde por él | `criterio-assets` | El inventario de activos contra sus dueños y el soporte del fabricante, las licencias contra su uso, cada proveedor contra su nivel de servicio y la nube contra su presupuesto: el activo sin dueño, el que pasó su fin de soporte sin una excepción aprobada, la licencia que falta y la que sobra, el incumplimiento de un proveedor sin su crédito en la factura y la factura de la nube por encima de su presupuesto |
<!-- /cto:agentes -->

## Las señales: lo que calcula el código

<!-- cto:senales · generado por scripts/familias.py; no se edita a mano -->
**Fausto · Los cambios y el servicio**

| Señal | Se levanta cuando |
|---|---|
| `change_without_approval` | Un cambio normal se implementó sin la aprobación de su autoridad de cambio, o antes de ella |
| `emergency_change_without_review` | Un cambio de emergencia no tiene su revisión posterior en el plazo de la política |
| `deployment_without_change` | Un despliegue en producción no corresponde a ningún cambio registrado |
| `failed_change_without_review` | Un cambio fallido o revertido no tiene su revisión posterior |
| `major_incident_without_problem` | Un incidente mayor no tiene un registro de problema con su causa en el plazo de la política |
| `service_below_level` | La disponibilidad de un servicio en el periodo quedó por debajo del nivel acordado en el catálogo |

**Domingo · Los activos y los proveedores**

| Señal | Se levanta cuando |
|---|---|
| `asset_without_owner` | Un activo del inventario no tiene dueño |
| `asset_out_of_support` | Un activo en producción pasó la fecha de fin de soporte de su fabricante sin una excepción aprobada vigente |
| `license_shortfall` | Las licencias en uso de un software superan las compradas |
| `license_unused` | Las licencias pagadas sin uso de un software superan el umbral de la política |
| `vendor_breach_without_credit` | Un proveedor quedó por debajo de su nivel de servicio y su factura del periodo no trae el crédito que pacta el contrato |
| `cloud_over_budget` | La factura de la nube de una cuenta supera su presupuesto más la tolerancia de la política |
<!-- /cto:senales -->

## Los comandos de Fausto, en orden de importancia

<!-- cto:comandos-fausto · generado por scripts/familias.py; no se edita a mano -->
| # | Comando | Entrada | Proceso (lo calcula el código) | Reporte |
|---|---|---|---|---|
| 0 | `changes-setup` | La carpeta raíz. Preguntas: entidad y su identificación fiscal, país, el periodo y los plazos de la política: los días para revisar un cambio de emergencia y para registrar el problema de un incidente mayor | Inventario de lo que hay; procesa el catálogo de servicios de `00-politica/`, los cambios y los despliegues de `10-cambios/` y los incidentes, los problemas y la disponibilidad de `20-servicio/`, y dice cuántas filas reconoce; compara la carpeta con la estructura recomendada; no crea, mueve ni renombra nada | Configuración guardada; inventario por carpeta; las tablas reconocidas; la primera ficha del periodo |
| 1 | `changes-scan` | Las actas del comité de cambios de `10-cambios/`, las tablas de `10-cambios/` y `20-servicio/`, y la ficha del periodo | Lleva a la ficha cada aprobación de un cambio —su autoridad y su fecha— y cada revisión posterior que quedó en un acta, con la cita; recalcula las señales | Lo que entró a la ficha; los documentos que todavía no están en ella; las señales nuevas; lo que no se pudo procesar y por qué |
| 2 | `change-check` | La exportación de cambios y el registro de despliegues de `10-cambios/`, y la ficha —las aprobaciones y las revisiones— | Cada cambio normal implementado contra su aprobación; cada cambio de emergencia y cada cambio fallido o revertido contra su revisión en el plazo de la política; cada despliegue en producción contra el cambio que lo autoriza | Los cambios sin aprobación o aprobados después, los de emergencia y los fallidos sin revisión, y los despliegues sin cambio, con los días |
| 3 | `incident-check` | Los incidentes y los problemas de `20-servicio/` | Cada incidente mayor del periodo contra el registro de problema que lo cita y su causa, en el plazo de la política | Los incidentes mayores sin problema o con el problema sin causa, con los días |
| 4 | `service-check` | El catálogo de servicios de `00-politica/` y la disponibilidad del periodo de `20-servicio/` | La disponibilidad de cada servicio en el periodo contra el nivel acordado en el catálogo | Los servicios por debajo de su nivel, con la diferencia |
| 5 | `changes-wake` | La configuración y el registro de corridas | Decide si toca procesar los cambios —documentos nuevos o la revisión semanal— o un reporte con señales abiertas, y lo corre; si no toca nada, se calla | Lo que corrió y por qué, o nada |
| 6 | `share-findings` | El rastro de las corridas de este agente en esta carpeta | Arma un resumen sin datos —qué comandos corrieron, cuántas señales, qué no se pudo procesar— y pregunta si se comparte; nada se envía solo | El resumen y la pregunta |
<!-- /cto:comandos-fausto -->

## Los comandos de Domingo, en orden de importancia

<!-- cto:comandos-domingo · generado por scripts/familias.py; no se edita a mano -->
| # | Comando | Entrada | Proceso (lo calcula el código) | Reporte |
|---|---|---|---|---|
| 0 | `assets-setup` | La carpeta raíz. Preguntas: entidad y su identificación fiscal, país, el periodo y los umbrales de la política: el porcentaje de licencias sin uso que tolera y la tolerancia sobre el presupuesto de la nube | Inventario de lo que hay; procesa el inventario y las licencias de `30-activos/`, el cumplimiento y las facturas de los proveedores de `40-proveedores/` y la factura y el presupuesto de `50-nube/`, y dice cuántas filas reconoce; compara la carpeta con la estructura recomendada; no crea, mueve ni renombra nada | Configuración guardada; inventario por carpeta; las tablas reconocidas; la primera ficha del periodo |
| 1 | `assets-scan` | Las actas del comité de arquitectura de `30-activos/`, los contratos de `40-proveedores/`, las tablas de `30-activos/`, `40-proveedores/` y `50-nube/`, y la ficha del periodo | Lleva a la ficha cada excepción aprobada sobre un activo sin soporte y cada nivel de servicio de un contrato, con su crédito, con la cita; recalcula las señales | Lo que entró a la ficha; los documentos que todavía no están en ella; las señales nuevas; lo que no se pudo procesar y por qué |
| 2 | `asset-check` | El inventario de activos de `30-activos/` y la ficha —las excepciones aprobadas— | Cada activo contra su dueño, y cada activo en producción contra la fecha de fin de soporte de su fabricante y la excepción que lo cubre | Los activos sin dueño y los que pasaron su fin de soporte sin excepción, con los días |
| 3 | `license-check` | Las licencias de `30-activos/` | Las licencias compradas de cada software contra las que están en uso, y las que sobran contra el umbral de la política | El software con menos licencias que uso y el que tiene licencias pagadas sin uso por encima del umbral, con la diferencia |
| 4 | `vendor-check` | La ficha —los niveles de servicio de cada contrato—, y el cumplimiento y las facturas de `40-proveedores/` | El cumplimiento de cada proveedor en el periodo contra el nivel de su contrato; el incumplimiento, contra el crédito en su factura | Los proveedores que incumplieron sin el crédito en la factura, con el nivel, lo medido y el valor |
| 5 | `cloud-check` | La factura y el presupuesto de `50-nube/` | La factura de la nube del periodo, por cuenta, contra su presupuesto y la tolerancia de la política | Las cuentas de la nube por encima de su presupuesto, con la diferencia |
| 6 | `assets-wake` | La configuración y el registro de corridas | Decide si toca procesar los activos —documentos nuevos o la revisión semanal— o un reporte con señales abiertas, y lo corre; si no toca nada, se calla | Lo que corrió y por qué, o nada |
| 7 | `share-findings` | El rastro de las corridas de este agente en esta carpeta | Arma un resumen sin datos —qué comandos corrieron, cuántas señales, qué no se pudo procesar— y pregunta si se comparte; nada se envía solo | El resumen y la pregunta |
<!-- /cto:comandos-domingo -->

## Cifras de terceros

<!-- cto:cifras · generado por scripts/familias.py; no se edita a mano -->
Solo entran las verificadas, con fuente, año y muestra, y están en [`FUENTES.es.md`](FUENTES.es.md). Verificadas: C-01 (Flexera), C-02 (Uptime Institute), C-03 (Uptime Institute).
<!-- /cto:cifras -->

## Decisiones cerradas

- Los nombres, Fausto y Domingo, y la estructura: dos agentes, sus doce señales y sus comandos (decisión 0037).
- La tecnología entra por lo que vive en documentos —los cambios y el servicio, los activos y los proveedores—; las herramientas de gestión del servicio, de inventario y de la nube, solo por sus exportaciones.
- La seguridad no es de esta familia: las vulnerabilidades, los controles y los incidentes de seguridad son de la CISO (decisión 0023).
- Un cambio estándar está preaprobado y no se le pide una aprobación por cambio; uno de emergencia se revisa después, en el plazo de la política.
- La disponibilidad se compara con el nivel acordado en el catálogo de servicios: mayor es mejor. El cumplimiento de un proveedor, con el nivel de su contrato, en el mismo sentido.
- La Circular Externa 005 de 2019 de la Superintendencia Financiera (F-10) se cita solo en una entidad de Colombia con niveles de servicio pactados; ITIL 4, COBIT 2019 y la norma del Perú y de Brasil quedan fuera de la 0.1.0 hasta verificarse.
- Cada defecto se siembra más de una vez desde la primera versión del material, para que la familia pase de 73 señales (decisión 0020).
