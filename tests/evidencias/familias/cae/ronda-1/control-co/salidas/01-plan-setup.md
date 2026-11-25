# /criterio-audit-plan:plan-setup auditoria/901888432-banco-control-sintetico

Soy Prudencia. Pongo el plan de auditoría al lado de la matriz de riesgos y del universo auditable; no decido qué se audita.

Prudencia quedó configurada para Banco Control Sintético. No hay riesgos altos sin trabajo y el plan cubre las tres áreas que exige la norma 9.4.

**Carpeta:** `auditoria/901888432-banco-control-sintetico`. Era la única candidata y tiene 00-referencia/, 10-plan/, 20-trabajos/ y 30-seguimiento/. No dejé el archivo `_CRITERIO_AUDITORIA.txt` porque nadie lo autorizó.

**Respuestas tomadas de los documentos:**
- **Entidad:** Banco Control Sintético, NIT 901888432, Colombia (COP). Periodo 2026-11.
- **Ciclos:** Crítico 12 meses, Alto 12, Medio 24 y Bajo 36. Un riesgo es alto desde «Alto» y «Crítico». Sale de la metodología, sección «Ciclos de rotación».
- **Quién aprueba el plan y sus cambios:** el Comité de auditoría, según el estatuto.
- **Evaluaciones:** la última de riesgos es del 2025-12-01 y la última externa de calidad, del 2021-12-15. Sale de la metodología, sección «Evaluaciones».
- **Rostrum:** no se publica.
- **Estado:** `estado-auditoria/901888432-banco-control-sintetico`.
- **Términos:** versión 1.6, aceptados por José Francisco Ñáñez el 2026-11-24. El comprobante está en `.criterio/terminos/aceptacion-criterio-audit-plan-0.1.0-2026-11-24.md` y en su `.pdf`.

**Archivos fuera de su lugar sugerido** (no moví nada):
- `30-seguimiento/informe_revisor_fiscal_2026.pdf` iría en `20-trabajos/`.
- `30-seguimiento/riesgos_aceptados.xlsx` iría en `10-plan/`.

**Actas:** procesé las dos de `10-plan/actas/` y las llevé a la ficha. El acta 07-2026 cancela TR-05 y el acta 10-2026 agrega TR-06; las dos las aprobó el Comité de auditoría.

# El plan contra los riesgos · Banco Control Sintético · periodo 2026-11

**Entidad:** Banco Control Sintético (901888432) · **Fecha de corte:** 2026-11-24 · **Procesado:** 2026-11-24 · **Agente:** Prudencia, versión 0.1.0 · **Comando:** `plan-coverage`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

| Riesgo | Calificación | Unidad | Alto | Trabajos que lo cubren |
|---|---|---|---|---|
| R-01 · Pérdida por riesgo de crédito | Alto | U-01 | sí | TR-01 |
| R-02 · Ataque a los canales digitales | Crítico | U-02 | sí | TR-02 |
| R-03 · Fraude en pagos a proveedores | Alto | U-07 | sí | TR-04 |
| R-04 · Lavado de activos | Crítico | U-05 | sí | TR-03 |
| R-05 · Error en la liquidación de nómina | Medio | U-04 | no | TR-06 |

| Unidad | Nivel | Último trabajo | Ciclo | Vence | En el plan |
|---|---|---|---|---|---|
| U-01 · Crédito | Alto | 2025-10-15 | 12 meses | 2026-10-15 | TR-01 |
| U-02 · Tecnología | Alto | 2025-10-01 | 12 meses | 2026-10-01 | TR-02 |
| U-03 · Tesorería | Medio | 2024-12-20 | 24 meses | 2026-12-20 | — |
| U-04 · Nómina | Bajo | 2024-05-01 | 36 meses | 2027-05-01 | TR-06 |
| U-05 · Cumplimiento | Alto | 2025-12-01 | 12 meses | 2026-12-01 | TR-03 |
| U-06 · Proveedores | Medio | 2025-01-15 | 24 meses | 2027-01-15 | — |
| U-10 · Canales físicos | Bajo | 2024-05-01 | 36 meses | 2027-05-01 | — |

| Lo que el plan tiene que considerar (norma 9.4) | Considerado | Por qué no |
|---|---|---|
| el gobierno de TI | sí | — |
| el riesgo de fraude | sí | — |
| los programas de cumplimiento y ética | sí | — |

**Última evaluación de riesgos:** 2025-12-01.

Qué se audita lo decide el responsable de auditoría con el consejo: aquí se dice qué queda sin cubrir.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- Sin documentos citados.
- Fuentes técnicas: F-01 (families/criterio-cae/FUENTES.es.md)

## Cuándo vuelvo

Sin reloj: nadie dio un sí a la tarea programada. Para correrlo a mano: `/criterio-audit-plan:plan-wake`.

La corrida quedó registrada como `2026-11-24-plan-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.