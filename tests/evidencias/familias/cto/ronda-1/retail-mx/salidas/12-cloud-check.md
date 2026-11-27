# /criterio-assets:cloud-check 

Tres cuentas de la nube superaron su presupuesto más la tolerancia en el periodo 2026-10; el reporte las detalla.

# La nube contra su presupuesto · Retail del Golfo Sintético · periodo 2026-10

**Entidad:** Retail del Golfo Sintético (RGS180610QW4) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Domingo, versión 0.1.0 · **Comando:** `cloud-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | La factura de la nube de una cuenta supera su presupuesto más la tolerancia de la política (`cloud_over_budget`) | Analítica: la nube facturó 180,000 en 2026-10 y el presupuesto es 150,000; la política tolera un 5 % más | 30,000.00 | — | — | `50-nube/factura_de_la_nube_2026-10.xlsx` fila 5 · `50-nube/presupuesto_de_la_nube_2026.xlsx` fila 4 |
| 2 | La factura de la nube de una cuenta supera su presupuesto más la tolerancia de la política (`cloud_over_budget`) | Canales digitales: la nube facturó 255,000 en 2026-10 y el presupuesto es 225,000; la política tolera un 5 % más | 30,000.00 | — | — | `50-nube/factura_de_la_nube_2026-10.xlsx` fila 6 · `50-nube/presupuesto_de_la_nube_2026.xlsx` fila 5 |
| 3 | La factura de la nube de una cuenta supera su presupuesto más la tolerancia de la política (`cloud_over_budget`) | Respaldo: la nube facturó 70,000 en 2026-10 y el presupuesto es 60,000; la política tolera un 5 % más | 10,000.00 | — | — | `50-nube/factura_de_la_nube_2026-10.xlsx` fila 7 · `50-nube/presupuesto_de_la_nube_2026.xlsx` fila 6 |

## El resultado

**Tolerancia de la política sobre el presupuesto de cada cuenta:** 5 %.

| Cuenta | Facturado | Presupuesto |
|---|---|---|
| Analítica | 180,000 | 150,000 |
| Canales digitales | 255,000 | 225,000 |
| Desarrollo | 45,000 | 50,000 |
| Producción | 410,000 | 400,000 |
| Respaldo | 70,000 | 60,000 |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `50-nube/factura_de_la_nube_2026-10.xlsx`
- `50-nube/presupuesto_de_la_nube_2026.xlsx`
- Fuentes técnicas: F-02 (families/criterio-cto/FUENTES.es.md)

---

Corrida registrada como `2026-11-25-cloud-check-1`. La salida quedó en `corridas/salida-cloud-check.md`.

Los términos (versión 1.6) ya estaban vigentes y no hubo que mostrarlos ni registrar una aceptación nueva. Por eso no registré a José Francisco Ñáñez como aceptante. Pasé `--today 2026-11-25` en todas las llamadas.

Las 3 cuentas pasadas son Analítica, Canales digitales y Respaldo. Si se amplía algún presupuesto lo decide el área con finanzas.