# /criterio-sales:pipeline-scan 

La ficha del periodo ya traía los 8 documentos de evidencia y el pronóstico comprometido del acta. Los comprobé contra los originales y no hubo que agregar nada.

# Qué cambió en el embudo · Comercial Control del Perú · periodo 2026-10

**Entidad:** Comercial Control del Perú (20210047035) · **Fecha de corte:** 2026-11-03 · **Procesado:** 2026-11-05 · **Agente:** Augusto, versión 0.2.0 · **Comando:** `pipeline-scan`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

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

- ¿De qué CRM sale la exportación y es «Last Activity Time» la última gestión? → Zoho; sí, se registró en crm.columns.ultima_actividad (respuesta sugerida por el formato reconocido)

## Fuentes

- Sin documentos citados.
- Fuentes técnicas: F-08 (families/criterio-cso/FUENTES.es.md)

La corrida quedó registrada como `2026-11-05-pipeline-scan-1`, con 0 hallazgos. Lo mostrado está guardado en `corridas/salida-pipeline-scan.md`.