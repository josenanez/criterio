# /criterio-assets:assets-scan 

No llegó ningún documento nuevo desde la corrida anterior. Las excepciones de las actas del comité de arquitectura y los niveles de servicio de los contratos ya estaban en la ficha del periodo. Los revisé contra los documentos y no hubo que agregar nada.

# Qué cambió en los activos · Software Austral Sintético · periodo 2026-10

**Entidad:** Software Austral Sintético (76543210-K) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Domingo, versión 0.1.0 · **Comando:** `assets-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Las licencias en uso de un software superan las compradas (`license_shortfall`) | Herramienta de analítica: 131 en uso y 120 compradas | 11,00 | — | — | `30-activos/licencias.xlsx` fila 6 |
| 2 | Las licencias en uso de un software superan las compradas (`license_shortfall`) | Diseño gráfico: 46 en uso y 40 compradas | 6,00 | — | — | `30-activos/licencias.xlsx` fila 5 |
| 3 | Un activo en producción pasó la fecha de fin de soporte de su fabricante sin una excepción aprobada vigente (`asset_out_of_support`) | A-310 · Servidor de la base de datos de clientes: corre en producción y su fabricante terminó el soporte el 2025-12-31; no tiene una excepción aprobada | — | — | 329 | `30-activos/inventario_de_activos.xlsx` fila 8 |
| 4 | Un activo en producción pasó la fecha de fin de soporte de su fabricante sin una excepción aprobada vigente (`asset_out_of_support`) | A-320 · Sistema operativo del servidor de pagos: corre en producción y su fabricante terminó el soporte el 2026-06-30; su excepción venció el 2026-09-30 | — | — | 148 | `30-activos/inventario_de_activos.xlsx` fila 9 |
| 5 | Un proveedor quedó por debajo de su nivel de servicio y su factura del periodo no trae el crédito que pacta el contrato (`vendor_breach_without_credit`) | Nube Andina · Disponibilidad: dio 99.7 en 2026-10 y el contrato pacta 99.95, con un crédito del 10 %; su factura FP-003 no trae el crédito | 22.500.000,00 | — | — | `40-proveedores/contrato_nube_andina.pdf` · `40-proveedores/cumplimiento_sla_2026-10.xlsx` fila 4 · `40-proveedores/facturas_proveedores_2026-10.xlsx` fila 4 |
| 6 | Un proveedor quedó por debajo de su nivel de servicio y su factura del periodo no trae el crédito que pacta el contrato (`vendor_breach_without_credit`) | Enlaces del Pacífico · Disponibilidad: dio 99.2 en 2026-10 y el contrato pacta 99.8, con un crédito del 8 %; su factura FP-004 no trae el crédito | 13.750.000,00 | — | — | `40-proveedores/contrato_enlaces_del_pacifico.pdf` · `40-proveedores/cumplimiento_sla_2026-10.xlsx` fila 5 · `40-proveedores/facturas_proveedores_2026-10.xlsx` fila 5 |
| 7 | La factura de la nube de una cuenta supera su presupuesto más la tolerancia de la política (`cloud_over_budget`) | Analítica: la nube facturó 9,000,000 en 2026-10 y el presupuesto es 7,500,000; la política tolera un 5 % más | 1.500.000,00 | — | — | `50-nube/factura_de_la_nube_2026-10.xlsx` fila 5 · `50-nube/presupuesto_de_la_nube_2026.xlsx` fila 4 |
| 8 | La factura de la nube de una cuenta supera su presupuesto más la tolerancia de la política (`cloud_over_budget`) | Canales digitales: la nube facturó 12,750,000 en 2026-10 y el presupuesto es 11,250,000; la política tolera un 5 % más | 1.500.000,00 | — | — | `50-nube/factura_de_la_nube_2026-10.xlsx` fila 6 · `50-nube/presupuesto_de_la_nube_2026.xlsx` fila 5 |
| 9 | Las licencias pagadas sin uso de un software superan el umbral de la política (`license_unused`) | Videoconferencia: 190 de 600 licencias pagadas sin uso, el 31.7 %; la política tolera un 15 % | 190,00 | — | — | `30-activos/licencias.xlsx` fila 7 |
| 10 | Las licencias pagadas sin uso de un software superan el umbral de la política (`license_unused`) | Firma electrónica: 80 de 200 licencias pagadas sin uso, el 40 %; la política tolera un 15 % | 80,00 | — | — | `30-activos/licencias.xlsx` fila 8 |
| 11 | Un activo del inventario no tiene dueño (`asset_without_owner`) | A-210 · Servidor de integración: el inventario no le asigna un dueño | — | — | — | `30-activos/inventario_de_activos.xlsx` fila 6 |
| 12 | Un activo del inventario no tiene dueño (`asset_without_owner`) | A-220 · Balanceador de carga: el inventario no le asigna un dueño | — | — | — | `30-activos/inventario_de_activos.xlsx` fila 7 |

## El resultado

**Activos en el inventario:** 8 · **Software con licencias:** 7 · **Proveedores con nivel en la ficha:** 4 · **Cuentas de la nube:** 4 · **Excepciones en la ficha:** 2.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `30-activos/inventario_de_activos.xlsx`
- `30-activos/licencias.xlsx`
- `40-proveedores/contrato_enlaces_del_pacifico.pdf`
- `40-proveedores/contrato_nube_andina.pdf`
- `40-proveedores/cumplimiento_sla_2026-10.xlsx`
- `40-proveedores/facturas_proveedores_2026-10.xlsx`
- `50-nube/factura_de_la_nube_2026-10.xlsx`
- `50-nube/presupuesto_de_la_nube_2026.xlsx`
- Fuentes técnicas: F-02 (families/criterio-cto/FUENTES.es.md)

---

**La corrida quedó registrada** como `2026-11-25-assets-scan-1`. La salida está en `<espacio>/estado-tecnologia/76543210-k-software-austral-sintetico/corridas/salida-assets-scan.md`.

**Dos cosas del reporte del motor, por si las corriges:**
- En las filas 5 y 6, la columna «Monto» trae la factura completa del proveedor, no el crédito que faltó.
- En las filas 1, 2, 9 y 10, «Monto» trae un número de licencias, pero tiene formato de dinero.

El reporte lo dejé tal como lo escribió el motor.