# /criterio-treasury:treasury-setup finanzas/900000001-distribuidora-control

Soy Áurea. Pongo la caja, los pagos y la deuda al lado de su política, y te digo dónde no cuadran. No muevo dinero.

## Listo — Distribuidora Control · tesorería 2026-09

**Lo que miré:**
- 2 cuentas con extracto: andino-5301 y pacifico-5302.
- Programa de pagos: sí.
- Política: sí, en `politica-tesoreria.csv`.
- Registro de deuda: sí, en `registro-deuda.xlsx` y `covenants.csv`.

**Términos:** José Francisco Ñáñez los aceptó para la versión 0.10.0 (términos 1.2). Los comprobantes están en `.criterio/terminos/aceptacion-criterio-treasury-0.10.0-2026-10-06.md` y `.pdf`.

**Respuestas por defecto:** nadie podía contestar, así que tomé las respuestas de los documentos:
- Aprobador: Sofía León.
- Cuentas: todas en COP.
- Umbrales: los de `config.example.json`.
- Estado: `estado-finanzas/900000001-distribuidora-control`.

# La posición de caja · Distribuidora Control · periodo 2026-09

**Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Aprueba:** Sofía León

**Lo que hay que atender:** nada abierto en lo que procesa este comando.

**Caja consolidada:** 25.241.750,00

| Cuenta | Moneda | Saldo | Mínimo | Proyectado | Desviación % |
|---|---|---|---|---|---|
| andino-5301 | COP | 10.241.750,00 | 4.620.875,00 | 10.241.750,00 | 0,00 |
| pacifico-5302 | COP | 15.000.000,00 | 7.000.000,00 | 15.000.000,00 | 0,00 |

**Lo que no se pudo procesar:** todo lo que llegó se procesó.

**Preguntas que hizo el agente:** ninguna.

**Fuentes:** el reporte no cita documentos.

**Cuándo vuelvo:** cuando haya pagos programados en los próximos días, cuando una obligación entre en su ventana de vencimiento y una vez por semana.

Las dos cuentas están por encima de su mínimo y el proyectado coincide con el saldo. Esa coincidencia puede ser real o puede venir de un flujo proyectado que repite el saldo; no lo verifiqué.

La configuración quedó en `.criterio/tesoreria/900000001/config.json` y valida sin problemas. El reporte está en `estado-finanzas/900000001-distribuidora-control/tesoreria/2026-09/reporte-cash-position.md`. Esta salida está en `estado-finanzas/900000001-distribuidora-control/corridas/salida-treasury-setup.md` y la corrida quedó registrada como `2026-10-06-treasury-setup-1`.