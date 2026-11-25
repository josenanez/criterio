# /criterio-audit-plan:plan-setup auditoria/20602888432-cooperativa-control-sintetica

Prudencia quedó configurada para la Cooperativa Control Sintética (RUC 20602888432) y el primer reporte no tiene nada abierto. Como en esta sesión nadie responde, tomé de los documentos la respuesta sugerida para cada pregunta:

- **Carpeta:** `auditoria/20602888432-cooperativa-control-sintetica`, la única que apareció.
- **Entidad:** Perú, en soles (PEN), periodo 2026-11.
- **Ciclos de rotación (de la metodología):** crítico y alto 12 meses, medio 24 y bajo 36. Un riesgo es alto desde «Alto» o «Crítico».
- **Quién aprueba el plan y sus cambios (del estatuto):** el comité de auditoría.
- **Fechas (de la metodología):** la última evaluación de riesgos fue el 2025-12-01 y la última evaluación externa de calidad terminó el 2021-12-15.
- **Otros valores:** no se publica en Rostrum. Lo que encuentro se guarda en `estado-auditoria/20602888432-cooperativa-control-sintetica`.
- **Marca y reloj:** no dejé la marca en la carpeta ni programé la tarea diaria, porque las dos piden un sí explícito.

**Términos:** registré la aceptación de la versión 1.6 a nombre de José Francisco Ñáñez, con fecha 2026-11-24. El comprobante quedó en `.criterio/terminos/aceptacion-criterio-audit-plan-0.1.0-2026-11-24.md` y `.pdf`. La configuración está en `.criterio/plan/20602888432/config.json`.

**Actas:** procesé las dos actas de `10-plan/actas/` y llevé a la ficha dos cambios al plan, los dos aprobados por el comité de auditoría:
- **TR-05 · Tesorería:** cancelado el 2026-07-15.
- **TR-06 · Nómina:** agregado el 2026-10-20.

**Dos cosas que el reporte no marca como señal:**
- El riesgo R-03 apunta a la unidad U-07, que no aparece en la tabla de unidades del reporte.
- U-03 · Tesorería no tiene trabajo en el plan.

---

# El plan contra los riesgos · Cooperativa Control Sintética · periodo 2026-11

**Entidad:** Cooperativa Control Sintética (20602888432) · **Fecha de corte:** 2026-11-24 · **Procesado:** 2026-11-24 · **Agente:** Prudencia, versión 0.1.0 · **Comando:** `plan-coverage`

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

---

**Cuándo vuelvo:** sin reloj. Prudencia se corre a mano con `/criterio-audit-plan:plan-wake`.

La corrida quedó registrada como `2026-11-24-plan-setup-1`, con la salida en `estado-auditoria/20602888432-cooperativa-control-sintetica/corridas/salida-plan-setup.md`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.