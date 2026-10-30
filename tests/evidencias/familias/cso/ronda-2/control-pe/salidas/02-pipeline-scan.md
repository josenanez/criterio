# /criterio-sales:pipeline-scan 

Los términos 1.3 están vigentes. Los 8 documentos de evidencia y el acta ya estaban en la ficha del periodo, con los mismos datos que el texto convertido, así que no la modifiqué.

# Qué cambió en el embudo · Comercial Control del Perú · periodo 2026-10

**Entidad:** Comercial Control del Perú (20210047035) · **Fecha de corte:** 2026-11-03 · **Procesado:** 2026-11-05 · **Agente:** Augusto, versión 0.2.0 · **Comando:** `pipeline-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una oportunidad abierta no tiene actividad registrada en los días configurados (`stalled_opportunity`) | OPP-2205 · Ampliación de contrato: abierta en «Calificación», sin actividad desde el 2026-10-01 (35 días) | 175,000.00 | — | 35 | `10-crm/Deals_2026_11_03.csv` fila 6 |

## El resultado

| Exportación | Fecha | Formato | Oportunidades |
|---|---|---|---|
| `10-crm/Deals_2026_10_01.csv` | 2026-10-01 | zoho | 7 |
| `10-crm/Deals_2026_10_16.csv` | 2026-10-16 | zoho | 7 |
| `10-crm/Deals_2026_11_03.csv` | 2026-11-03 | zoho | 7 |

**Desde la exportación anterior:** 0 nuevas, 1 ganadas, 1 perdidas, 1 cambios de etapa, 0 de monto y 3 de fecha de cierre. **Evidencia en la ficha:** 8 documentos.

- **Etapa:** OPP-2203: Negociación → Compromiso
- **Fecha de cierre:** OPP-2204: 2026-12-10 → 2026-12-15; OPP-2206: 2026-10-30 → 2026-10-28; OPP-2207: 2026-11-30 → 2026-12-18

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿De qué CRM salen las exportaciones de 10-crm/? → Zoho CRM (propuesto por las columnas Record ID, Deal Name y Last Activity Time; el motor lo reconoció sin columnas faltantes)
- ¿Las fechas de las exportaciones van día/mes o mes/día? → Día/mes (28/09/2026, 22/10/2026)

## Fuentes

- `10-crm/Deals_2026_11_03.csv`
- Fuentes técnicas: F-08 (families/criterio-cso/FUENTES.es.md)

La corrida quedó registrada como `2026-11-05-pipeline-scan-1`, con 1 hallazgo.