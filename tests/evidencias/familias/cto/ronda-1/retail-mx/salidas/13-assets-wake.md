# /criterio-assets:assets-wake 

Hoy solo tocaba `assets-scan`, por la revisión semanal, y no había peticiones en Rostrum. No llegaron documentos nuevos, cambiados ni borrados. La ficha del periodo 2026-10 ya tenía las excepciones de las dos actas del comité de arquitectura y los niveles de servicio de los cinco contratos, así que no hubo nada que agregar. Decidir sobre cada señal le toca al área de tecnología, al comité de arquitectura y a legal.

# Qué cambió en los activos · Retail del Golfo Sintético · periodo 2026-10

**Entidad:** Retail del Golfo Sintético (RGS180610QW4) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Domingo, versión 0.1.0 · **Comando:** `assets-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Las licencias en uso de un software superan las compradas (`license_shortfall`) | Herramienta de analítica: 131 en uso y 120 compradas | 11.00 | — | — | `30-activos/licencias.xlsx` fila 6 |
| 2 | Las licencias en uso de un software superan las compradas (`license_shortfall`) | Diseño gráfico: 46 en uso y 40 compradas | 6.00 | — | — | `30-activos/licencias.xlsx` fila 5 |
| 3 | Las licencias en uso de un software superan las compradas (`license_shortfall`) | Gestor de proyectos: 80 en uso y 75 compradas | 5.00 | — | — | `30-activos/licencias.xlsx` fila 7 |
| 4 | Un activo en producción pasó la fecha de fin de soporte de su fabricante sin una excepción aprobada vigente (`asset_out_of_support`) | A-310 · Servidor de la base de datos de clientes: corre en producción y su fabricante terminó el soporte el 2025-12-31; no tiene una excepción aprobada | — | — | 329 | `30-activos/inventario_de_activos.xlsx` fila 9 |
| 5 | Un activo en producción pasó la fecha de fin de soporte de su fabricante sin una excepción aprobada vigente (`asset_out_of_support`) | A-330 · Gestor de colas de mensajes: corre en producción y su fabricante terminó el soporte el 2026-04-30; no tiene una excepción aprobada | — | — | 209 | `30-activos/inventario_de_activos.xlsx` fila 11 |
| 6 | Un activo en producción pasó la fecha de fin de soporte de su fabricante sin una excepción aprobada vigente (`asset_out_of_support`) | A-320 · Sistema operativo del servidor de pagos: corre en producción y su fabricante terminó el soporte el 2026-06-30; su excepción venció el 2026-09-30 | — | — | 148 | `30-activos/inventario_de_activos.xlsx` fila 10 |
| 7 | Un proveedor quedó por debajo de su nivel de servicio y su factura del periodo no trae el crédito que pacta el contrato (`vendor_breach_without_credit`) | Nube Andina · Disponibilidad: dio 99.7 en 2026-10 y el contrato pacta 99.95, con un crédito del 10 %; su factura FP-003 no trae el crédito | 450,000.00 | — | — | `40-proveedores/contrato_nube_andina.pdf` · `40-proveedores/cumplimiento_sla_2026-10.xlsx` fila 4 · `40-proveedores/facturas_proveedores_2026-10.xlsx` fila 4 |
| 8 | Un proveedor quedó por debajo de su nivel de servicio y su factura del periodo no trae el crédito que pacta el contrato (`vendor_breach_without_credit`) | Enlaces del Pacífico · Disponibilidad: dio 99.2 en 2026-10 y el contrato pacta 99.8, con un crédito del 8 %; su factura FP-004 no trae el crédito | 275,000.00 | — | — | `40-proveedores/contrato_enlaces_del_pacifico.pdf` · `40-proveedores/cumplimiento_sla_2026-10.xlsx` fila 5 · `40-proveedores/facturas_proveedores_2026-10.xlsx` fila 5 |
| 9 | Un proveedor quedó por debajo de su nivel de servicio y su factura del periodo no trae el crédito que pacta el contrato (`vendor_breach_without_credit`) | Soporte Integral · Casos resueltos a tiempo: dio 89 en 2026-10 y el contrato pacta 95, con un crédito del 5 %; su factura FP-005 no trae el crédito | 175,000.00 | — | — | `40-proveedores/contrato_soporte_integral.pdf` · `40-proveedores/cumplimiento_sla_2026-10.xlsx` fila 6 · `40-proveedores/facturas_proveedores_2026-10.xlsx` fila 6 |
| 10 | La factura de la nube de una cuenta supera su presupuesto más la tolerancia de la política (`cloud_over_budget`) | Analítica: la nube facturó 180,000 en 2026-10 y el presupuesto es 150,000; la política tolera un 5 % más | 30,000.00 | — | — | `50-nube/factura_de_la_nube_2026-10.xlsx` fila 5 · `50-nube/presupuesto_de_la_nube_2026.xlsx` fila 4 |
| 11 | La factura de la nube de una cuenta supera su presupuesto más la tolerancia de la política (`cloud_over_budget`) | Canales digitales: la nube facturó 255,000 en 2026-10 y el presupuesto es 225,000; la política tolera un 5 % más | 30,000.00 | — | — | `50-nube/factura_de_la_nube_2026-10.xlsx` fila 6 · `50-nube/presupuesto_de_la_nube_2026.xlsx` fila 5 |
| 12 | La factura de la nube de una cuenta supera su presupuesto más la tolerancia de la política (`cloud_over_budget`) | Respaldo: la nube facturó 70,000 en 2026-10 y el presupuesto es 60,000; la política tolera un 5 % más | 10,000.00 | — | — | `50-nube/factura_de_la_nube_2026-10.xlsx` fila 7 · `50-nube/presupuesto_de_la_nube_2026.xlsx` fila 6 |
| 13 | Las licencias pagadas sin uso de un software superan el umbral de la política (`license_unused`) | Antivirus de escritorio: 200 de 900 licencias pagadas sin uso, el 22.2 %; la política tolera un 15 % | 200.00 | — | — | `30-activos/licencias.xlsx` fila 10 |
| 14 | Las licencias pagadas sin uso de un software superan el umbral de la política (`license_unused`) | Videoconferencia: 190 de 600 licencias pagadas sin uso, el 31.7 %; la política tolera un 15 % | 190.00 | — | — | `30-activos/licencias.xlsx` fila 8 |
| 15 | Las licencias pagadas sin uso de un software superan el umbral de la política (`license_unused`) | Firma electrónica: 80 de 200 licencias pagadas sin uso, el 40 %; la política tolera un 15 % | 80.00 | — | — | `30-activos/licencias.xlsx` fila 9 |
| 16 | Un activo del inventario no tiene dueño (`asset_without_owner`) | A-210 · Servidor de integración: el inventario no le asigna un dueño | — | — | — | `30-activos/inventario_de_activos.xlsx` fila 6 |
| 17 | Un activo del inventario no tiene dueño (`asset_without_owner`) | A-220 · Balanceador de carga: el inventario no le asigna un dueño | — | — | — | `30-activos/inventario_de_activos.xlsx` fila 7 |
| 18 | Un activo del inventario no tiene dueño (`asset_without_owner`) | A-230 · Repositorio de archivos: el inventario no le asigna un dueño | — | — | — | `30-activos/inventario_de_activos.xlsx` fila 8 |

## El resultado

**Activos en el inventario:** 10 · **Software con licencias:** 9 · **Proveedores con nivel en la ficha:** 5 · **Cuentas de la nube:** 5 · **Excepciones en la ficha:** 2.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `30-activos/inventario_de_activos.xlsx`
- `30-activos/licencias.xlsx`
- `40-proveedores/contrato_enlaces_del_pacifico.pdf`
- `40-proveedores/contrato_nube_andina.pdf`
- `40-proveedores/contrato_soporte_integral.pdf`
- `40-proveedores/cumplimiento_sla_2026-10.xlsx`
- `40-proveedores/facturas_proveedores_2026-10.xlsx`
- `50-nube/factura_de_la_nube_2026-10.xlsx`
- `50-nube/presupuesto_de_la_nube_2026.xlsx`
- Fuentes técnicas: F-02 (families/criterio-cto/FUENTES.es.md)

---

Las dos corridas quedaron registradas, `2026-11-25-assets-scan-2` y `2026-11-25-assets-wake-1`, ambas con el caso 2026-10. La aceptación de los términos (versión 1.6) ya estaba vigente, así que no hubo que registrarla otra vez.

Usé el periodo 2026-10 que dice la configuración, porque los documentos son de ese mes. Las corridas anteriores de `asset-check`, `license-check` y `vendor-check` quedaron en una carpeta 2026-11 que no tiene ficha. Por eso esos reportes no ven las excepciones aprobadas.