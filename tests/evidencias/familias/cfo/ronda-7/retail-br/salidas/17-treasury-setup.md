# /criterio-treasury:treasury-setup finanzas/31452078000170-lojas-paulistas

## Listo — Lojas Paulistas · tesorería 2026-09

**Lo que miré:** 2 cuentas con extracto (bandeirante-2901, litoral-2902) · programa de pagos sí · política sí · registro de deuda sí
**Términos:** José Francisco Ñáñez los aceptó el 2026-10-06 para la versión 0.12.1. El comprobante está en `.criterio/terminos/aceptacion-criterio-treasury-0.12.1-2026-10-06.md`.

Todo esto lo tomé de los documentos y lo dejé así, porque nadie podía responder:
- Usé la carpeta del argumento y no busqué la raíz.
- La moneda funcional es BRL, como en la configuración de Clara.
- litoral-2902 va en USD; lo dice su extracto y también lo puse en la configuración.
- Los umbrales son los de `config.example.json` (10 %, 30 días, 10 %). Son configuración, no norma.
- El estado queda en `estado-finanzas/31452078000170-lojas-paulistas`.
- No marqué la raíz, porque nadie la autorizó.

# La posición de caja · Lojas Paulistas · periodo 2026-09

**Entidad:** Lojas Paulistas (31452078000170) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Áurea, versión 0.12.1 · **Aprueba:** Sofia Leão · **Comando:** `cash-position`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | La posición en otra moneda, convertida con la tasa de la política, supera su límite (`fx_exposure_over_limit`) | la posición en USD equivale a 810.000,00 BRL, sobre el límite de 405.000,00 | 405.000,00 | — | — | `2026-09/20-bancos/litoral-2902/extrato.csv` fila 3 · `00-referencia/politica-tesouraria.csv` fila 7 |

## El resultado

**Caja consolidada:** 869.082,93

| Cuenta | Moneda | Saldo | Mínimo | Proyectado | Desviación % |
|---|---|---|---|---|---|
| bandeirante-2901 | BRL | 59.082,93 | 24.541,47 | 59.082,93 | 0,00 |
| litoral-2902 | USD | 150.000,00 | 70.000,00 | 150.000,00 | 0,00 |

| Moneda | Posición en moneda funcional | Límite |
|---|---|---|
| USD | 810.000,00 | 405.000,00 |

Áurea no mueve dinero ni entra a un portal bancario: procesa las exportaciones.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/politica-tesouraria.csv`
- `2026-09/20-bancos/litoral-2902/extrato.csv`

**Cuándo vuelvo:** cuando haya pagos programados en los próximos días, cuando una obligación entre en su ventana de vencimiento y una vez por semana.

---
Dos notas mías, fuera del reporte:
- `compute` encontró otras dos señales además de la de exposición: `payment_without_approval` y `maturity_near`. Este reporte no las trae. Las verás en `/payment-check` y `/debt-watch`.
- Las fuentes del reporte no incluyen el `extrato.pdf` de bandeirante-2901. Su saldo coincide con el proyectado, así que conviene confirmar de dónde salió ese saldo.

La corrida quedó registrada como `2026-10-06-treasury-setup-1`. Hice 0 preguntas, el primer resultado salió en una sola pasada y la corrida tuvo 3 hallazgos.