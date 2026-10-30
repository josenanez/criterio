# /criterio-sales:pipeline-scan 

Sesión de prueba sin interfaz: los términos estaban vigentes (aceptados por José Francisco Ñáñez el 2026-11-05). La ficha de 2026-10 ya estaba completa y coincide con los 8 documentos de evidencia y el acta del comité, así que no la modifiqué.

# Qué cambió en el embudo · Comercial Control de Chile · periodo 2026-10

**Entidad:** Comercial Control de Chile (76000002-7) · **Fecha de corte:** 2026-11-03 · **Procesado:** 2026-11-05 · **Agente:** Augusto, versión 0.2.0 · **Comando:** `pipeline-scan`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

| Exportación | Fecha | Formato | Oportunidades |
|---|---|---|---|
| `10-crm/oportunidades-2026-10-01.xlsx` | 2026-10-01 | dynamics | 7 |
| `10-crm/oportunidades-2026-10-16.xlsx` | 2026-10-16 | dynamics | 7 |
| `10-crm/oportunidades-2026-11-03.xlsx` | 2026-11-03 | dynamics | 7 |

**Desde la exportación anterior:** 0 nuevas, 1 ganadas, 1 perdidas, 1 cambios de etapa, 1 de monto y 3 de fecha de cierre. **Evidencia en la ficha:** 8 documentos.

- **Etapa:** OPP-2503: Negociación → Compromiso
- **Monto:** OPP-2505: 60.000.000,00 → 64.000.000,00
- **Fecha de cierre:** OPP-2504: 2026-12-10 → 2026-12-15; OPP-2506: 2026-10-30 → 2026-10-28; OPP-2507: 2026-11-30 → 2026-12-18

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Qué periodo se revisa? → 2026-10 (acta, metas, evidencia y liquidación son de octubre; la última exportación, del 2026-11-03, es el corte)
- ¿De qué CRM sale la exportación? → Dynamics 365 Sales (las columnas lo indican)
- ¿Umbrales de detención y de cierres corridos? → 30 días sin actividad; hasta 2 cierres corridos

## Fuentes

- Sin documentos citados.
- Fuentes técnicas: F-06 (families/criterio-cso/FUENTES.es.md)

La corrida quedó registrada como `2026-11-05-pipeline-scan-1`, con 0 hallazgos. El reporte está en `estado-comercial/76000002-7-comercial-control-de-chile/comercial/2026-10/reporte-pipeline-scan.md`.