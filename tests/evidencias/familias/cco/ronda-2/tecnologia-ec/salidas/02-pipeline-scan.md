# /criterio-sales:pipeline-scan 

Corrida de prueba sobre el periodo 2026-10: 3 exportaciones del CRM y 15 documentos de evidencia ya estaban en la ficha, junto con el pronóstico del acta del comité; el motor calculó las señales de abajo.

# Qué cambió en el embudo · Sistemas Integrados del Guayas · periodo 2026-10

**Entidad:** Sistemas Integrados del Guayas (0990234566001) · **Fecha de corte:** 2026-11-03 · **Procesado:** 2026-11-05 · **Agente:** Augusto, versión 0.2.0 · **Comando:** `pipeline-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Lo cerrado al corte se aparta de la meta del periodo, prorrateada por los días transcurridos, más del umbral (`target_vs_closed`) | 2026-10: cerrado 396,000.00 contra 554,400.00 esperado al corte (100 % del periodo de una meta de 554,400.00): -28.6 % | -158,400.00 | — | — | `00-referencia/metas.csv` fila 3 |
| 2 | Una oportunidad está en una etapa y no tiene el documento que esa etapa exige (`stage_without_evidence`) | OPP-1822 · Pedido marco 22: está en «Compromiso» y la ficha no tiene la orden de compra | 120,000.00 | — | — | `10-crm/Deals_2026_11_03.csv` fila 11 |
| 3 | Ídem (`stage_without_evidence`) | OPP-1821 · Pedido marco 21: está en «Compromiso» y la ficha no tiene la orden de compra | 108,000.00 | — | — | `10-crm/Deals_2026_11_03.csv` fila 10 |
| 4 | Ídem (`stage_without_evidence`) | OPP-1820 · Pedido marco 20: está en «Compromiso» y la ficha no tiene la orden de compra | 96,000.00 | — | — | `10-crm/Deals_2026_11_03.csv` fila 9 |
| 5 | La fecha de cierre se movió más veces de las configuradas (`close_date_slipped`) | OPP-1804 · Servicio de soporte: se corrió 2 veces, de 2026-11-15 a 2026-12-15 | 108,000.00 | — | — | `Deals_2026_10_16.csv` fila 5 · `Deals_2026_11_03.csv` fila 5 |
| 6 | Oportunidad abierta sin actividad en los días configurados (`stalled_opportunity`) | OPP-1823 · Prospecto 23: «Calificación», sin actividad desde 2026-10-01 | 96,000.00 | — | 35 | `Deals_2026_11_03.csv` fila 12 |
| 7 | `close_date_slipped` | OPP-1826 · Licencias adicionales 26: se corrió 2 veces, de 2026-11-20 a 2026-12-18 | 96,000.00 | — | — | `Deals_2026_10_16.csv` fila 15 · `Deals_2026_11_03.csv` fila 15 |
| 8 | `stalled_opportunity` | OPP-1805 · Ampliación de contrato: «Calificación», sin actividad desde 2026-10-01 | 84,000.00 | — | 35 | `Deals_2026_11_03.csv` fila 6 |
| 9 | `close_date_slipped` | OPP-1828 · Licencias adicionales 28: se corrió 2 veces, de 2026-11-20 a 2026-12-18 | 84,000.00 | — | — | `Deals_2026_10_16.csv` fila 17 · `Deals_2026_11_03.csv` fila 17 |
| 10 | `stalled_opportunity` | OPP-1825 · Prospecto 25: «Calificación», sin actividad desde 2026-10-01 | 72,000.00 | — | 35 | `Deals_2026_11_03.csv` fila 14 |
| 11 | `close_date_slipped` | OPP-1827 · Licencias adicionales 27: se corrió 2 veces, de 2026-11-20 a 2026-12-18 | 72,000.00 | — | — | `Deals_2026_10_16.csv` fila 16 · `Deals_2026_11_03.csv` fila 16 |
| 12 | `stalled_opportunity` | OPP-1824 · Prospecto 24: «Calificación», sin actividad desde 2026-10-01 | 60,000.00 | — | 35 | `Deals_2026_11_03.csv` fila 13 |

## El resultado

| Exportación | Fecha | Formato | Oportunidades |
|---|---|---|---|
| `10-crm/Deals_2026_10_01.csv` | 2026-10-01 | zoho | 19 |
| `10-crm/Deals_2026_10_16.csv` | 2026-10-16 | zoho | 19 |
| `10-crm/Deals_2026_11_03.csv` | 2026-11-03 | zoho | 19 |

**Desde la exportación anterior:** 0 nuevas, 1 ganadas, 1 perdidas, 1 cambios de etapa, 0 de monto y 6 de fecha de cierre. **Evidencia en la ficha:** 15 documentos.

- **Etapa:** OPP-1803: Negociación → Compromiso
- **Fecha de cierre:** OPP-1804: 2026-12-01 → 2026-12-15; OPP-1806: 2026-10-30 → 2026-10-28; OPP-1807: 2026-11-30 → 2026-12-18; OPP-1826: 2026-12-04 → 2026-12-18; OPP-1827: 2026-12-04 → 2026-12-18; OPP-1828: 2026-12-04 → 2026-12-18

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/metas.csv`
- `10-crm/Deals_2026_10_16.csv`
- `10-crm/Deals_2026_11_03.csv`
- Fuentes técnicas: F-08 (families/criterio-cso/FUENTES.es.md)

---
Dos cosas sobre lo que acabo de mostrar:
- En la tabla de señales abrevié la columna «Señal» y la «Cita» de varias filas (por ejemplo «Ídem» o `Deals_…csv` sin la carpeta). El archivo `salida-pipeline-scan.md` guarda el reporte del motor completo, con el texto sin abreviar.
- La corrida quedó registrada como `2026-11-05-pipeline-scan-1`, con 12 hallazgos.