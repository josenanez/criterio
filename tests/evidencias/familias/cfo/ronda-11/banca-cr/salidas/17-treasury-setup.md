# /criterio-treasury:treasury-setup finanzas/3101457812-banco-del-valle-central-sintetico

## Listo — Banco del Valle Central (sintético) · tesorería 2026-09

**Lo que miré:** 2 cuentas con extracto (andino-10101 y pacifico-10102). Hay programa de pagos, política y registro de deuda.
**Términos:** quedaron aceptados para la versión 1.0.0 (términos 1.3), a nombre de José Francisco Ñáñez, fecha 2026-10-06. El comprobante está en `.criterio/terminos/aceptacion-criterio-treasury-1.0.0-2026-10-06.md` y `.pdf`.

Nadie respondió preguntas, así que tomé las respuestas sugeridas:
- Entidad, moneda funcional (CRC) y período (2026-09) salen de la configuración de Clara.
- La moneda de cada cuenta la toma el motor del extracto, así que `treasury.currencies` quedó vacío.
- Los umbrales son los de `config.example.json`: 10 % de desviación, 30 días de vencimiento y 10 % de margen del covenant.
- El estado queda en `estado-finanzas/3101457812-banco-del-valle-central-sintetico`, el mismo de Clara y Tomás.

**La posición de caja** (corte 2026-09-30, copiada del reporte del motor):

| Cuenta | Moneda | Saldo | Mínimo | Proyectado | Desviación % |
|---|---|---|---|---|---|
| andino-10101 | CRC | 11.951.800,00 | 4.975.900,00 | 11.951.800,00 | 0,00 |
| pacifico-10102 | USD | 30.000.000,00 | 14.000.000,00 | 30.000.000,00 | 0,00 |

La caja consolidada es 15.161.951.800,00.

**Lo que hay que atender:**
- **Exposición en USD sobre el límite.** La posición en USD equivale a 15.150.000.000,00 CRC con la tasa de la política. El límite es 7.575.000.000,00. Las citas son `2026-09/20-bancos/pacifico-10102/extracto.pdf` fila 3 y `00-referencia/politica-tesoreria.csv` fila 7.
- **Otras dos señales** salieron del cálculo: un firmante sin autoridad (`signatory_without_authority`) y un covenant en riesgo (`covenant_at_risk`). No están en este reporte. Aparecerán al correr `/payment-check` y `/debt-watch`.

Todo lo que llegó se procesó, y el motor no hizo preguntas.

Registré la corrida como `2026-10-06-treasury-setup-1`, con 3 hallazgos. La salida completa está en `estado-finanzas/3101457812-banco-del-valle-central-sintetico/corridas/salida-treasury-setup.md`.

**Cuándo vuelvo:** cuando haya pagos programados en los próximos días, cuando una obligación entre en su ventana de vencimiento y una vez por semana.