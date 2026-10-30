# /criterio-sales:pipeline-scan 

Corrida de prueba sin interfaz: los términos están vigentes (aceptados por José Francisco Ñáñez). Procesé 3 exportaciones del CRM y 16 documentos escritos. La ficha del periodo ya traía esos documentos y no cambió.

# Qué cambió en el embudo · Soluciones Digitales Andinas · periodo 2026-10

**Entidad:** Soluciones Digitales Andinas (900876543) · **Fecha de corte:** 2026-11-03 · **Procesado:** 2026-11-05 · **Agente:** Augusto, versión 0.1.0 · **Comando:** `pipeline-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Días | Cita |
|---|---|---|---|---|---|
| 1 | `target_vs_closed`: lo cerrado al corte se aparta de la meta más del umbral | 2026-10: cerrado 264.000.000,00 contra 369.600.000,00 esperado al corte (100 % del periodo de una meta de 369.600.000,00): -28,6 % | -105.600.000,00 | — | `00-referencia/metas.csv` fila 3 |
| 2 | `stage_without_evidence`: falta el documento que exige la etapa | OPP-1222 · Pedido marco 22: está en «Compromiso» y la ficha no tiene la orden de compra | 80.000.000,00 | — | `10-crm/hubspot-crm-exports-deals-2026-11-03.csv` fila 11 |
| 3 | `stage_without_evidence` | OPP-1221 · Pedido marco 21: está en «Compromiso» y la ficha no tiene la orden de compra | 72.000.000,00 | — | `…2026-11-03.csv` fila 10 |
| 4 | `stage_without_evidence` | OPP-1220 · Pedido marco 20: está en «Compromiso» y la ficha no tiene la orden de compra | 64.000.000,00 | — | `…2026-11-03.csv` fila 9 |
| 5 | `close_date_slipped`: la fecha de cierre se movió más veces de las configuradas | OPP-1204 · Servicio de soporte: se corrió 2 veces, de 2026-11-15 a 2026-12-15 | 72.000.000,00 | — | `…2026-10-16.csv` fila 5 · `…2026-11-03.csv` fila 5 |
| 6 | `stalled_opportunity`: sin actividad en los días configurados | OPP-1223 · Prospecto 23: «Calificación», sin actividad desde el 2026-09-05 | 64.000.000,00 | 61 | `…2026-11-03.csv` fila 12 |
| 7 | `close_date_slipped` | OPP-1226 · Licencias adicionales 26: se corrió 2 veces, de 2026-11-20 a 2026-12-18 | 64.000.000,00 | — | `…2026-10-16.csv` fila 15 · `…2026-11-03.csv` fila 15 |
| 8 | `stalled_opportunity` | OPP-1205 · Ampliación de contrato: «Calificación», sin actividad desde el 2026-09-12 | 56.000.000,00 | 54 | `…2026-11-03.csv` fila 6 |
| 9 | `close_date_slipped` | OPP-1228 · Licencias adicionales 28: se corrió 2 veces, de 2026-11-20 a 2026-12-18 | 56.000.000,00 | — | `…2026-10-16.csv` fila 17 · `…2026-11-03.csv` fila 17 |
| 10 | `stalled_opportunity` | OPP-1225 · Prospecto 25: «Calificación», sin actividad desde el 2026-09-05 | 48.000.000,00 | 61 | `…2026-11-03.csv` fila 14 |
| 11 | `close_date_slipped` | OPP-1227 · Licencias adicionales 27: se corrió 2 veces, de 2026-11-20 a 2026-12-18 | 48.000.000,00 | — | `…2026-10-16.csv` fila 16 · `…2026-11-03.csv` fila 16 |
| 12 | `stalled_opportunity` | OPP-1224 · Prospecto 24: «Calificación», sin actividad desde el 2026-09-05 | 40.000.000,00 | 61 | `…2026-11-03.csv` fila 13 |

## El resultado

| Exportación | Fecha | Formato | Oportunidades |
|---|---|---|---|
| `10-crm/hubspot-crm-exports-deals-2026-10-01.csv` | 2026-10-01 | hubspot | 19 |
| `10-crm/hubspot-crm-exports-deals-2026-10-16.csv` | 2026-10-16 | hubspot | 19 |
| `10-crm/hubspot-crm-exports-deals-2026-11-03.csv` | 2026-11-03 | hubspot | 19 |

**Desde la exportación anterior:** 0 nuevas, 1 ganadas, 1 perdidas, 1 cambios de etapa, 0 de monto y 6 de fecha de cierre. **Evidencia en la ficha:** 15 documentos.

- **Etapa:** OPP-1203: Negociación → Compromiso
- **Fecha de cierre:** OPP-1204: 2026-12-01 → 2026-12-15; OPP-1206: 2026-10-30 → 2026-10-28; OPP-1207: 2026-11-30 → 2026-12-18; OPP-1226: 2026-12-04 → 2026-12-18; OPP-1227: 2026-12-04 → 2026-12-18; OPP-1228: 2026-12-04 → 2026-12-18

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Qué periodo abre la primera ficha? → 2026-10, el del acta del comité del 2 de octubre y la liquidación 2026-10
- ¿Se deja la marca _CRITERIO_COMERCIAL.txt en la carpeta raíz? → No; la ruta vino en el argumento

## Fuentes

- `00-referencia/metas.csv`
- `10-crm/hubspot-crm-exports-deals-2026-10-16.csv`
- `10-crm/hubspot-crm-exports-deals-2026-11-03.csv`
- Fuentes técnicas: F-04 (families/criterio-cso/FUENTES.es.md)

El reporte completo está en `comercial/2026-10/reporte-pipeline-scan.md`. La corrida quedó registrada como `2026-11-05-pipeline-scan-1`, con 12 hallazgos.

Dos aclaraciones sobre lo que mostré arriba:
- **Tabla acortada:** abrevié la tabla de señales con `…` en las rutas y quité la columna «Responsable», que estaba vacía. El archivo `salida-pipeline-scan.md` guarda el reporte con el texto íntegro del motor, no esta versión acortada.
- **Introducción:** el archivo lleva al inicio la misma introducción de dos líneas que escribí, y dice «16 documentos». El reporte del motor cuenta 15 de evidencia, más el acta del comité.