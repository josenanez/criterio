# /criterio-treasury:treasury-setup finanzas/76097001-8-comercial-control-andes

## Listo — Comercial Control Andes · tesorería 2026-09

**Lo que miré:** 2 cuentas con extracto (andino-9701 y pacifico-9702). Hay programa de pagos, política de tesorería y registro de deuda.

**Términos:** José Francisco Ñáñez los aceptó para la versión 0.10.0 (términos 1.2) el 2026-10-06. El comprobante quedó en `.criterio/terminos/`.

Nadie respondió preguntas en esta sesión, así que tomé estas respuestas de los documentos:
- **Entidad y moneda:** usé las de Clara, que son CL y CLP. No las deduje de la política.
- **Otras monedas:** ninguna. Las dos cuentas están en CLP.
- **Umbrales:** los de `config.example.json`, que son 10 % de desviación contra la proyección, 30 días de vencimiento y 10 % de margen del covenant. Son configuración, no norma.
- **Estado:** `estado-finanzas/76097001-8-comercial-control-andes`, el mismo de Clara y Tomás.
- **Marca de la raíz:** no la creé. Nadie la autorizó.

# La posición de caja · periodo 2026-09 (corte 2026-09-30)

**Lo que hay que atender:** nada abierto en lo que procesa este comando.

**Caja consolidada:** 13.681.800,00

| Cuenta | Moneda | Saldo | Mínimo | Proyectado | Desviación % |
|---|---|---|---|---|---|
| andino-9701 | CLP | 4.681.800,00 | 2.040.900,00 | 4.681.800,00 | 0,00 |
| pacifico-9702 | CLP | 9.000.000,00 | 4.200.000,00 | 9.000.000,00 | 0,00 |

**Lo que no se pudo procesar:** todo lo que llegó se procesó.

**Cuándo vuelvo:** cuando haya pagos programados en los próximos días, cuando una obligación entre en su ventana de vencimiento y una vez por semana.

Archivos que quedaron:
- **Configuración:** `.criterio/tesoreria/76097001-8/config.json`.
- **Reporte:** `estado-finanzas/76097001-8-comercial-control-andes/tesoreria/2026-09/reporte-cash-position.md`. No lo abrí; el texto de arriba es lo que imprimió el motor.
- **Salida de esta corrida:** `estado-finanzas/76097001-8-comercial-control-andes/corridas/salida-treasury-setup.md`. La corrida quedó registrada con 0 hallazgos.