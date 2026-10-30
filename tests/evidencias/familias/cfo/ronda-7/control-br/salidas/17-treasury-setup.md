# /criterio-treasury:treasury-setup finanzas/40217355000151-comercial-controle-paulista

Soy Áurea. Pongo la caja, los pagos y la deuda al lado de su política, y te digo dónde no cuadran. No muevo dinero.

## Listo — Comercial Controle Paulista · tesorería 2026-09

**Lo que miré:** 2 cuentas con extracto (bandeirante-4301 y litoral-4302) · programa de pagos sí · política sí · registro de deuda sí.
**Términos:** aceptados por José Francisco Ñáñez el 2026-10-06, términos 1.3, versión 0.12.1. Los comprobantes quedaron en `.criterio/terminos/`.

**Cómo respondí las preguntas** (nadie contestó, así que tomé lo que dicen los documentos):
- **Carpeta y moneda:** usé la carpeta del argumento. La moneda funcional es BRL y quien aprueba es Sofia Leão, tomados de la configuración de Clara.
- **Otras monedas:** no hay cuentas en otra moneda, porque los dos extractos traen BRL.
- **Umbrales:** los de `config.example.json`: 10 % de desviación contra la proyección, 30 días de vencimiento y 10 % de margen del covenant. Son configuración, no norma.
- **Estado:** `estado-finanzas/40217355000151-comercial-controle-paulista`.
- **Marca de raíz:** no la creé, porque nadie la autorizó.

# La posición de caja · periodo 2026-09

**Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06

**Lo que hay que atender:** nada abierto en lo que procesa este comando.

**Caja consolidada:** 203.326,83

| Cuenta | Moneda | Saldo | Mínimo | Proyectado | Desviación % |
|---|---|---|---|---|---|
| bandeirante-4301 | BRL | 83.326,83 | 37.663,42 | 83.326,83 | 0,00 |
| litoral-4302 | BRL | 120.000,00 | 56.000,00 | 120.000,00 | 0,00 |

**Lo que no se pudo procesar:** nada. Todo lo que llegó se procesó.

**Cuándo vuelvo:** cuando haya pagos programados en los próximos días, cuando una obligación entre en su ventana de vencimiento y una vez por semana.

La configuración quedó en `.criterio/tesoreria/40217355000151/config.json`. El reporte lo escribió el motor en `estado-finanzas/…/tesoreria/2026-09/`, y la corrida quedó registrada como `2026-10-06-treasury-setup-1` en `corridas/`.