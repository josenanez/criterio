# /criterio-finance:close-scan 

El barrido del cierre de 2026-09 de Almacenes Caribe quedó hecho y registrado como `2026-10-06-close-scan-1`. Encontró 9 señales abiertas.

El inventario trajo 63 archivos nuevos y ninguno cambiado ni borrado. No dejó nada fuera de lugar ni ilegible.

El único documento escrito que declara el estado del cierre es el correo de Sofía León del 2026-10-05, que dice «cerrado». Ya estaba en la ficha del cierre, así que no la toqué. Los soportes C-01 a C-05 se convirtieron a texto sin problemas.

Las señales abiertas son estas:
- **Mayor contra balance (cuentas 2505 y 5195):** difieren en 120.000,00 de crédito en 2505 y 120.000,00 de débito en 5195.
- **Cierre declarado contra evidencia:** el correo dice «cerrado», pero hay 8 señales abiertas que ese estado no explica.
- **Banco andino-3701:** una consignación en tránsito del 2026-09-30 por 8.330.000,00 (SETP99000102 y SETP99000107 aparecen en las señales; la consignación es la de SETP99000107).
- **Facturas duplicadas:** la factura emitida SETP99000102 llegó en dos archivos con el mismo CUFE (8.330.000,00), y la recibida SETP77000201 está registrada en dos asientos (3.104.000,00).
- **Factura SETP77000201:** en libros figura con base 3.104.000,00 e IVA 589.760,00; el XML dice base 1.552.000,00 e IVA 294.880,00.
- **Conciliaciones sin actualizar:** las cuentas 1435 y 2205 no tienen auxiliar del periodo.

Dos cosas no pude cerrar:
- El motor dejó vacía la sección «El resultado» del reporte; la mostré tal cual, sin rellenarla.
- El marco contable sigue por confirmar, porque ningún documento lo declara.

Archivos en `estado-finanzas/900765432-almacenes-caribe/` (la carpeta del estado):
- `cierre/2026-09/reporte-close-scan.md`
- `corridas/salida-close-scan.md`