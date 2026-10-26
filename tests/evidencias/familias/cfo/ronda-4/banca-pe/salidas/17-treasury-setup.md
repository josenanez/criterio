# /criterio-treasury:treasury-setup finanzas/20710000019-banco-ribera

## Listo — Banco Ribera · tesorería 2026-09

**Lo que miré:** 2 cuentas con extracto · programa de pagos sí · política sí · registro de deuda sí
**Términos:** aceptados para la versión 0.10.0 (términos 1.2) por José Francisco Ñáñez · comprobante en `.criterio/terminos/aceptacion-criterio-treasury-0.10.0-2026-10-06-2.md`

La moneda funcional es PEN, tomada de la configuración de Clara. pacifico-7102 está en USD porque así lo dice su extracto. Usé los umbrales de `config.example.json` (10 % / 30 días / 10 %) y guardé el estado en `estado-finanzas/20710000019-banco-ribera`.

No marqué la raíz con `_CRITERIO_FINANZAS.txt` porque nadie lo autorizó.

# La posición de caja · Banco Ribera · periodo 2026-09

**Entidad:** Banco Ribera (20710000019) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Áurea, versión 0.10.0 · **Aprueba:** Sofía León · **Comando:** `cash-position`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | La posición en otra moneda, convertida con la tasa de la política, supera su límite (`fx_exposure_over_limit`) | la posición en USD equivale a 450,000.00 PEN, sobre el límite de 225,000.00 | 225,000.00 | — | — | `2026-09/20-bancos/pacifico-7102/extracto.csv` fila 3 · `00-referencia/politica-tesoreria.csv` fila 7 |

## El resultado

**Caja consolidada:** 466,959.20

| Cuenta | Moneda | Saldo | Mínimo | Proyectado | Desviación % |
|---|---|---|---|---|---|
| andino-7101 | PEN | 16,959.20 | 4,479.60 | 16,959.20 | 0.00 |
| pacifico-7102 | USD | 120,000.00 | 56,000.00 | 120,000.00 | 0.00 |

| Moneda | Posición en moneda funcional | Límite |
|---|---|---|
| USD | 450,000.00 | 225,000.00 |

Áurea no mueve dinero ni entra a un portal bancario: procesa las exportaciones.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/politica-tesoreria.csv`
- `2026-09/20-bancos/pacifico-7102/extracto.csv`

**Cuándo vuelvo:** cuando haya pagos programados en los próximos días, cuando una obligación entre en su ventana de vencimiento y una vez por semana.

La corrida quedó registrada como `2026-10-06-treasury-setup-2`. El motor detectó 3 señales, pero el reporte de caja solo muestra la de exposición cambiaria. Las otras dos, `signatory_without_authority` y `maturity_near`, son de pagos y de deuda. Salen con `/criterio-treasury:payment-check` y `/criterio-treasury:debt-watch`.