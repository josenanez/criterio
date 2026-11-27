# /criterio-audit-plan:plan-coverage 

Términos vigentes (versión 1.6). El reporte salió y la corrida quedó registrada como `2026-11-24-plan-coverage-1`, con 0 hallazgos. Dejo el reporte tal cual lo escribió el motor.

# El plan contra los riesgos · Cooperativa Control Sintética · periodo 2026-11

**Entidad:** Cooperativa Control Sintética (20602888432) · **Fecha de corte:** 2026-11-24 · **Agente:** Prudencia 0.2.2

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

| Lo que el plan tiene que considerar (norma 9.4) | Considerado |
|---|---|
| el gobierno de TI | sí |
| el riesgo de fraude | sí |
| los programas de cumplimiento y ética | sí |

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

**Dos correcciones:**
- **Nota previa en la salida registrada:** escribí que "el reporte señala las unidades que no están en el plan". Es inexacto, porque el reporte no marca nada como abierto. Las unidades U-03, U-06 y U-10 aparecen con "—" en la columna "En el plan", pero el motor no las señala como pendientes. La salida registrada en `salida-plan-coverage.md` conserva esa frase.
- **Términos:** el motor los dio por vigentes con aceptación previa (0.2.2), así que no corrí un registro nuevo a nombre de José Francisco Ñáñez. Si quieres ese registro con fecha 2026-11-24, hay que correr `/criterio-audit-plan:plan-setup`.