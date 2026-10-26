# /criterio-treasury:treasury-setup finanzas/20730000015-minera-puna-alta

## Listo — Minera Puna Alta (20730000015) · tesorería 2026-09

**Lo que miré:** 2 cuentas con extracto (andino-7301 y pacifico-7302) · programa de pagos sí · política sí · registro de deuda sí
**Términos:** José Francisco Ñáñez los aceptó para la versión 0.10.0 (términos 1.2). El comprobante está en `.criterio/terminos/aceptacion-criterio-treasury-0.10.0-2026-10-06.md`.

Nadie respondió preguntas en esta sesión y no hice ninguna. Usé los datos de la entidad que ya tiene la configuración de Clara.

- **Cuentas en otra moneda:** no puse ninguna. Las dos cuentas están en PEN, que es la moneda de la entidad.
- **Umbrales:** usé los de `config.example.json`: 10 % de desviación contra la proyección, 30 días de vencimiento y 10 % de margen de covenant. Son configuración, no norma.
- **Estado:** `estado-finanzas/20730000015-minera-puna-alta`, fuera de la carpeta de documentos.
- **Marca de la raíz:** no la puse, porque nadie la autorizó.

Además de las dos señales de caja, el cálculo marcó un covenant en riesgo (`covenant_at_risk`). No sale en el reporte de posición de caja. Lo detalla `/debt-watch`, que no he corrido.

# La posición de caja · Minera Puna Alta · periodo 2026-09

**Entidad:** Minera Puna Alta (20730000015) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Áurea, versión 0.10.0 · **Aprueba:** Sofía León

## Lo que hay que atender

| # | Señal | Qué | Monto | Cita |
|---|---|---|---|---|
| 1 | Saldo bajo el mínimo de la política (`cash_below_minimum`) | andino-7301: saldo 56,802.00 PEN, bajo el mínimo de 74,162.40 | 17,360.40 | `2026-09/20-bancos/andino-7301/extracto.xlsx` fila 17 · `00-referencia/politica-tesoreria.csv` fila 2 |
| 2 | Saldo real lejos de la proyección (`cash_vs_forecast`) | pacifico-7302: saldo 180,000.00 contra 234,000.00 proyectado (-23.1) | 54,000.00 | `2026-09/20-bancos/pacifico-7302/extracto.xlsx` fila 3 · `2026-09/60-tesoreria/flujo-proyectado.csv` fila 3 |

## El resultado

**Caja consolidada:** 236,802.00

| Cuenta | Moneda | Saldo | Mínimo | Proyectado | Desviación % |
|---|---|---|---|---|---|
| andino-7301 | PEN | 56,802.00 | 74,162.40 | 56,802.00 | 0.00 |
| pacifico-7302 | PEN | 180,000.00 | 84,000.00 | 234,000.00 | -23.08 |

Áurea no mueve dinero ni entra a un portal bancario: procesa las exportaciones.

**Lo que no se pudo procesar:** todo lo que llegó se procesó.
**Preguntas que hizo:** ninguna en esta corrida.

**Fuentes:** `00-referencia/politica-tesoreria.csv`, los dos extractos de `2026-09/20-bancos/` y `2026-09/60-tesoreria/flujo-proyectado.csv`.

**Cuándo vuelvo:** cuando haya pagos programados en los próximos días, cuando una obligación entre en su ventana de vencimiento y una vez por semana.

La corrida quedó registrada como `2026-10-06-treasury-setup-1`. Lo que te mostré está en `estado-finanzas/20730000015-minera-puna-alta/corridas/salida-treasury-setup.md`.