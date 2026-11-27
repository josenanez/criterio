# /criterio-assets:cloud-check 

El comando no traía periodo y la única factura de la nube es la de 2026-10, así que corrí el reporte sobre 2026-10. Con 2026-11 el reporte sale sin cuentas. Los términos estaban vigentes (versión 1.6), y no hizo falta registrar una aceptación nueva.

# La nube contra su presupuesto · Banco Meridiano Sintético · periodo 2026-10

**Entidad:** Banco Meridiano Sintético (901222444) · **Fecha de corte:** 2026-11-25 · **Agente:** Domingo, versión 0.1.0

## Lo que hay que atender

Tres cuentas superan su presupuesto más la tolerancia del 5 % de la política (`cloud_over_budget`):

| # | Cuenta | Facturado | Presupuesto | Exceso | Cita |
|---|---|---|---|---|---|
| 1 | Analítica | 36,000,000 | 30,000,000 | 6.000.000,00 | `50-nube/factura_de_la_nube_2026-10.xlsx` fila 5 · `50-nube/presupuesto_de_la_nube_2026.xlsx` fila 4 |
| 2 | Canales digitales | 51,000,000 | 45,000,000 | 6.000.000,00 | `50-nube/factura_de_la_nube_2026-10.xlsx` fila 6 · `50-nube/presupuesto_de_la_nube_2026.xlsx` fila 5 |
| 3 | Respaldo | 14,000,000 | 12,000,000 | 2.000.000,00 | `50-nube/factura_de_la_nube_2026-10.xlsx` fila 7 · `50-nube/presupuesto_de_la_nube_2026.xlsx` fila 6 |

## El resultado

| Cuenta | Facturado | Presupuesto |
|---|---|---|
| Analítica | 36,000,000 | 30,000,000 |
| Canales digitales | 51,000,000 | 45,000,000 |
| Desarrollo | 9,000,000 | 10,000,000 |
| Producción | 82,000,000 | 80,000,000 |
| Respaldo | 14,000,000 | 12,000,000 |

Producción pasa su presupuesto en 2,000,000, que queda dentro de la tolerancia, y Desarrollo queda por debajo.

**Lo que no se pudo procesar:** nada, todo lo que llegó se procesó. **Preguntas que hizo el agente:** ninguna.

**Fuentes:** `50-nube/factura_de_la_nube_2026-10.xlsx`, `50-nube/presupuesto_de_la_nube_2026.xlsx`.

Si se amplía algún presupuesto, lo decide el área de tecnología con finanzas.

La corrida quedó registrada como `2026-11-25-cloud-check-1`. La salida mostrada está en `estado-tecnologia/901222444-banco-meridiano-sintetico/corridas/salida-cloud-check.md`.