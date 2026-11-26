# /criterio-data-quality:rule-check 

Los términos (versión 1.6) ya estaban vigentes y aceptados, así que no hizo falta registrar una aceptación nueva. La corrida quedó registrada.

# Las reglas de calidad · Banco Control de Datos Sintético · periodo 2026-11

**Entidad:** Banco Control de Datos Sintético (901666888) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Ariadna, versión 0.2.0 · **Comando:** `rule-check`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

| Regla | Dato | Crítico | Umbral | Resultado del periodo |
|---|---|---|---|---|
| RQ-01 | Cliente.documento | sí | 99 | 99.6 |
| RQ-02 | Movimiento.valor | sí | 98 | 98 |
| RQ-03 | Crédito.fecha_desembolso | sí | 97 | 97.4 |
| RQ-04 | Proveedor.correo | no | 90 | sin corrida |

Los umbrales los fija la política de datos de la organización.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- Sin documentos citados.
- Fuentes técnicas: F-01, F-03 (families/criterio-cdo/FUENTES.es.md)

El reporte está en `estado-datos/901666888-banco-control-de-datos-sintetico/calidad/2026-11/reporte-rule-check.md`. Copié lo mostrado en `…/corridas/salida-rule-check.md` y la corrida quedó registrada como `2026-11-25-rule-check-1`, sin hallazgos.