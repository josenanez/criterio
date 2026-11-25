# /criterio-risk-appetite:coverage-check 

Cobertura de la matriz, periodo 2026-10: de los cinco riesgos altos o críticos, R-04 no tiene límite y R-06 no tiene indicador. Si necesitan uno lo decide el comité de riesgos.

# Cada riesgo alto con su límite · Cooperativa Controle Sintética · periodo 2026-10

**Entidad:** Cooperativa Controle Sintética (98765432000110) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Severo, versión 0.1.0 · **Comando:** `coverage-check`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

| Riesgo | Calificación | Con límite | Con indicador |
|---|---|---|---|
| R-01 · Risco de crédito pessoal | Alto | sí | sí |
| R-02 · Risco de liquidez | Crítico | sí | sí |
| R-03 · Fraude externa nos canais | Alto | sí | sí |
| R-04 · Continuidade de negócios | Alto | no | sí |
| R-06 · Risco de contraparte | Alto | sí | no |

Si un riesgo necesita un límite o un indicador lo decide el comité de riesgos.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- Sin documentos citados.
- Fuentes técnicas: F-01 (families/criterio-cro/FUENTES.es.md)

---
Notas de la sesión, que no están en el reporte:
- Los términos ya estaban aceptados (versión 1.6, el 2026-11-25, por José Francisco Ñáñez), así que no volví a registrarlos.
- No se dio periodo. Tomé 2026-10, que es el de la configuración y el de la exposición y los indicadores.
- La sección "Lo que hay que atender" sale vacía aunque R-04 y R-06 tienen huecos. El motor reporta 0 hallazgos en esta corrida. Lo dejo tal cual, sin corregirlo.
- La corrida quedó registrada como `2026-11-25-coverage-check-1`.