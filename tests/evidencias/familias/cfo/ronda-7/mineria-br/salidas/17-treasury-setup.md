# /criterio-treasury:treasury-setup finanzas/28903114000160-mineracao-serra-azul

## Listo: Mineração Serra Azul · tesorería 2026-09

**Lo que miré:** 2 cuentas con extracto, y también el programa de pagos, la política y el registro de deuda.
**Términos:** quedaron aceptados para la versión 0.12.1 a nombre de José Francisco Ñáñez, con fecha 2026-10-06. El comprobante está en `.criterio/terminos/aceptacion-criterio-treasury-0.12.1-2026-10-06.md`.

Estas son las respuestas que tomé de los documentos:
- **Carpeta raíz:** `finanzas/28903114000160-mineracao-serra-azul`, la única candidata.
- **Moneda funcional:** BRL, según la configuración de Clara.
- **Otras monedas:** no hay cuentas en otra moneda. Los extractos traen la columna `moeda` y todo es BRL.
- **Umbrales:** los de `config.example.json`: 10 % de desviación, 30 días de vencimiento y 10 % de margen del covenant.
- **Estado:** `estado-finanzas/28903114000160-mineracao-serra-azul`.

No marqué la raíz con `_CRITERIO_FINANZAS.txt`, porque nadie lo autorizó en esta prueba.

El motor levantó 3 señales: caja bajo el mínimo, un firmante sin autoridad y un covenant en riesgo. Este reporte cubre la primera. Las otras dos las muestran `/criterio-treasury:payment-check` y `/criterio-treasury:debt-watch`.

# La posición de caja · Mineração Serra Azul · periodo 2026-09

**Entidad:** Mineração Serra Azul (28903114000160) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Áurea, versión 0.12.1 · **Aprueba:** Sofia Leão

## Lo que hay que atender

| # | Señal | Qué | Monto | Cita |
|---|---|---|---|---|
| 1 | Saldo bajo el mínimo de la política (`cash_below_minimum`) | bandeirante-3101: saldo 169.841,48 BRL, bajo el mínimo de 213.809,78 | 43.968,30 | `2026-09/20-bancos/bandeirante-3101/extrato.csv` fila 17 · `00-referencia/politica-tesouraria.csv` fila 2 |

## El resultado

**Caja consolidada:** 469.841,48

| Cuenta | Moneda | Saldo | Mínimo | Proyectado | Desviación % |
|---|---|---|---|---|---|
| bandeirante-3101 | BRL | 169.841,48 | 213.809,78 | 169.841,48 | 0,00 |
| litoral-3102 | BRL | 300.000,00 | 140.000,00 | 300.000,00 | 0,00 |

Áurea no mueve dinero ni entra a un portal bancario: procesa las exportaciones.

**Lo que no se pudo procesar:** todo lo que llegó se procesó.
**Las preguntas que hizo:** ninguna en esta corrida.
**Fuentes:** `00-referencia/politica-tesouraria.csv` y `2026-09/20-bancos/bandeirante-3101/extrato.csv`

**Cuándo vuelvo:** cuando haya pagos programados en los próximos días, cuando una obligación entre en su ventana de vencimiento y una vez por semana.

La corrida quedó registrada como `2026-10-06-treasury-setup-1`, con 0 preguntas a la persona. En esta sesión de prueba no medí los minutos hasta el primer resultado. La configuración está en `.criterio/tesoreria/28903114000160/config.json`, y la salida completa en `estado-finanzas/28903114000160-mineracao-serra-azul/corridas/salida-treasury-setup.md`.