# /criterio-risk-appetite:framework-check 

Los términos están vigentes (versión 1.6), así que no hizo falta pedir aceptación. El marco tiene dos límites sin dueño y dos con la revisión vencida. La declaración de apetito no está registrada en la ficha.

# El marco y la declaración · Banco del Pichincha Sur Sintético · periodo 2026-11

**Entidad:** Banco del Pichincha Sur Sintético (1790123456001) · **Fecha de corte:** 2026-11-25 · **Agente:** Severo 1.1.0 · **Comando:** `framework-check`

## Lo que hay que atender

| # | Señal | Qué | Responsable | Días | Cita |
|---|---|---|---|---|---|
| 1 | Límite sin dueño | L-02 · Indicador de cobertura de liquidez | — | — | `00-marco/limites.xlsx` fila 3 |
| 2 | Límite sin dueño | L-22 · Concentración sectorial de la cartera | — | — | `00-marco/limites.xlsx` fila 10 |
| 3 | Revisión vencida | L-32 · Exposición en moneda extranjera: tocaba el 2026-05-31 | Tesorería | 178 | `00-marco/limites.xlsx` fila 11 |
| 4 | Revisión vencida | L-02 · Indicador de cobertura de liquidez: tocaba el 2026-06-30 | — | 148 | `00-marco/limites.xlsx` fila 3 |

## El resultado

**Declaración de apetito:** — · revisada por la junta el — · próxima revisión —. El motor no encontró la declaración en la ficha; el reporte no dice si falta el documento o solo su registro.

Los otros nueve límites (L-01, L-03, L-04, L-05, L-06, L-07, L-12, L-22 y L-42) tienen dueño y su revisión está al día. L-22 es la excepción por el dueño que le falta. Las próximas revisiones van del 2027-03-31 al 2027-06-30.

## Lo que no se pudo procesar

Los 11 límites quedaron sin exposición reportada para 2026-11: `10-exposicion/exposicion_2026-10.xlsx` solo trae el periodo anterior. Eso lo cubre `/limit-check`.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-marco/limites.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cro/FUENTES.es.md)

La corrida quedó registrada como `2026-11-25-framework-check-1` (11 hallazgos). Lo mostrado está en `corridas/salida-framework-check.md` dentro de la carpeta de estado. Esta versión del reporte está resumida: el reporte completo del motor es `apetito/2026-11/reporte-framework-check.md`, en la misma carpeta de estado.

La decisión sobre dueños, fechas de revisión y declaración es de la junta y el comité de riesgos.