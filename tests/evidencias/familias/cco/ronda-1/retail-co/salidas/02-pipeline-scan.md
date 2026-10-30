# /criterio-sales:pipeline-scan 

Los términos vigentes (versión 1.3) ya estaban aceptados a nombre de José Francisco Ñáñez, así que no hizo falta registrar nada. Los 19 documentos de evidencia y el pronóstico del acta ya estaban en la ficha y coinciden con los originales. Corrí el motor con `--today 2026-11-05`.

---

# Qué cambió en el embudo · Almacenes del Valle · periodo 2026-10

**Entidad:** Almacenes del Valle (901234567) · **Fecha de corte:** 2026-11-03 · **Procesado:** 2026-11-05 · **Agente:** Augusto, versión 0.1.0 · **Comando:** `pipeline-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Lo comprometido supera lo que suman las oportunidades con evidencia, ponderadas por su etapa, más de la tolerancia configurada (`forecast_unsupported`) | 2026-10: se comprometieron 630.000.000,00 y lo cerrado más lo ponderado con evidencia suma 420.000.000,00; la tolerancia es 10 % | 210.000.000,00 | — | — | `20-comite/acta-comite-2026-10-02.docx, sección «Pronóstico de octubre»` · `10-crm/oportunidades-2026-11-03.csv` |
| 2 | Etapa sin el documento que exige (`stage_without_evidence`) | OPP-1103 · Suministro anual: está en «Compromiso» y la ficha no tiene la orden de compra | 250.000.000,00 | — | — | `10-crm/oportunidades-2026-11-03.csv` fila 4 |
| 3 | Etapa sin el documento que exige (`stage_without_evidence`) | OPP-1123 · Pedido marco 23: está en «Compromiso» y la ficha no tiene la orden de compra | 110.000.000,00 | — | — | `10-crm/oportunidades-2026-11-03.csv` fila 13 |
| 4 | Etapa sin el documento que exige (`stage_without_evidence`) | OPP-1122 · Pedido marco 22: está en «Compromiso» y la ficha no tiene la orden de compra | 100.000.000,00 | — | — | `10-crm/oportunidades-2026-11-03.csv` fila 12 |
| 5 | Etapa sin el documento que exige (`stage_without_evidence`) | OPP-1121 · Pedido marco 21: está en «Compromiso» y la ficha no tiene la orden de compra | 90.000.000,00 | — | — | `10-crm/oportunidades-2026-11-03.csv` fila 11 |
| 6 | Etapa sin el documento que exige (`stage_without_evidence`) | OPP-1120 · Pedido marco 20: está en «Compromiso» y la ficha no tiene la orden de compra | 80.000.000,00 | — | — | `10-crm/oportunidades-2026-11-03.csv` fila 10 |
| 7 | Fecha de cierre movida más veces de las configuradas (`close_date_slipped`) | OPP-1107 · Implementación por fases: se corrió 3 veces, de 2026-10-31 a 2026-12-18 | 110.000.000,00 | — | — | `10-crm/historial-2026-11-03.csv` filas 2, 3 y 4 |
| 8 | Fecha de cierre movida más veces de las configuradas (`close_date_slipped`) | OPP-1129 · Renovación anual 29: se corrió 3 veces, de 2026-11-08 a 2026-12-20 | 80.000.000,00 | — | — | `10-crm/historial-2026-11-03.csv` filas 11, 12 y 13 |
| 9 | Oportunidad abierta sin actividad (`stalled_opportunity`) | OPP-1126 · Prospecto 26: en «Calificación», sin actividad desde el 2026-09-05 | 70.000.000,00 | — | 61 | `10-crm/oportunidades-2026-11-03.csv` fila 16 |
| 10 | Fecha de cierre movida más veces de las configuradas (`close_date_slipped`) | OPP-1128 · Renovación anual 28: se corrió 3 veces, de 2026-11-08 a 2026-12-20 | 70.000.000,00 | — | — | `10-crm/historial-2026-11-03.csv` filas 8, 9 y 10 |
| 11 | Oportunidad abierta sin actividad (`stalled_opportunity`) | OPP-1125 · Prospecto 25: en «Calificación», sin actividad desde el 2026-09-05 | 60.000.000,00 | — | 61 | `10-crm/oportunidades-2026-11-03.csv` fila 15 |
| 12 | Fecha de cierre movida más veces de las configuradas (`close_date_slipped`) | OPP-1127 · Renovación anual 27: se corrió 3 veces, de 2026-11-08 a 2026-12-20 | 60.000.000,00 | — | — | `10-crm/historial-2026-11-03.csv` filas 5, 6 y 7 |
| 13 | Oportunidad abierta sin actividad (`stalled_opportunity`) | OPP-1124 · Prospecto 24: en «Calificación», sin actividad desde el 2026-09-05 | 50.000.000,00 | — | 61 | `10-crm/oportunidades-2026-11-03.csv` fila 14 |

## El resultado

| Exportación | Fecha | Formato | Oportunidades |
|---|---|---|---|
| `10-crm/oportunidades-2026-10-01.csv` | 2026-10-01 | salesforce | 22 |
| `10-crm/oportunidades-2026-10-16.csv` | 2026-10-16 | salesforce | 22 |
| `10-crm/oportunidades-2026-11-03.csv` | 2026-11-03 | salesforce | 22 |

**Desde la exportación anterior:** 0 nuevas, 1 ganadas, 1 perdidas, 1 cambios de etapa, 0 de monto y 6 de fecha de cierre. **Evidencia en la ficha:** 19 documentos.

- **Etapa:** OPP-1103: Negociación → Compromiso
- **Fecha de cierre:** OPP-1104: 2026-12-10 → 2026-12-15; OPP-1106: 2026-10-30 → 2026-10-28; OPP-1107: 2026-11-30 → 2026-12-18; OPP-1127: 2026-12-01 → 2026-12-20; OPP-1128: 2026-12-01 → 2026-12-20; OPP-1129: 2026-12-01 → 2026-12-20

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Dejo la marca _CRITERIO_COMERCIAL.txt en la carpeta raíz? → No (sesión de prueba sin interfaz; no se escribió nada en la carpeta de documentos)

## Fuentes

- `10-crm/historial-2026-11-03.csv`
- `10-crm/oportunidades-2026-11-03.csv`
- `20-comite/acta-comite-2026-10-02.docx, sección «Pronóstico de octubre»`
- Fuentes técnicas: F-02 (families/criterio-cso/FUENTES.es.md)

---

Dos aclaraciones sobre esta presentación:
- En las filas 2 a 13 abrevié el texto de la columna «Señal». El reporte completo, con la descripción larga, está en `estado-comercial/901234567-almacenes-del-valle/comercial/2026-10/reporte-pipeline-scan.md`.
- `corridas/salida-pipeline-scan.md` guarda el reporte completo que escribió el motor, con una nota inicial. No guarda esta versión abreviada.

La corrida quedó registrada como `2026-11-05-pipeline-scan-1`, con 13 hallazgos.