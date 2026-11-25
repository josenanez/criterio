# /criterio-risk-events:kri-check 

Términos vigentes (ya aceptados en 0.1.0, no hizo falta registrar de nuevo). Periodo 2026-10: dos indicadores en zona de alerta, KRI-01 y KRI-05; ambos con acción registrada.

# Cada indicador contra su umbral · Banco Control de Riesgos Sintético · periodo 2026-10

**Entidad:** Banco Control de Riesgos Sintético (901888444) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Casandra, versión 0.1.0 · **Comando:** `kri-check`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

| Indicador | Sentido | Alerta | Límite | Valor del periodo | Zona | Acción |
|---|---|---|---|---|---|---|
| KRI-01 · Transacciones fraudulentas por millón | mayor es peor | 40 | 60 | 52 | alerta | sí |
| KRI-02 · Disponibilidad de los canales digitales | menor es peor | 99.5 | 99 | 99.6 | normal | no |
| KRI-03 · Rotación del personal de crédito | mayor es peor | 8 | 12 | 6.5 | normal | no |
| KRI-04 · Días sin una prueba del plan de continuidad | mayor es peor | 180 | 365 | 64 | normal | no |
| KRI-05 · Concentración de los depósitos en los 20 mayores | mayor es peor | 25 | 30 | 29 | alerta | sí |

Los umbrales los fija el marco de apetito de la organización.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- Sin documentos citados.
- Fuentes técnicas: F-01 (families/criterio-cro/FUENTES.es.md)

La corrida quedó registrada como `2026-11-25-kri-check-1`, con 0 hallazgos.