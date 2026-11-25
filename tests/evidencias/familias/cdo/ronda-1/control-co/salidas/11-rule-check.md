# /criterio-data-quality:rule-check 

Los términos están vigentes (versión 1.6), así que no hizo falta registrar la aceptación.

Debajo está el reporte tal cual lo escribió el motor. El motor no marca nada como pendiente, pero RQ-04 (Proveedor.correo, dato no crítico) aparece sin corrida en el periodo.

# Las reglas de calidad · Banco Control de Datos Sintético · periodo 2026-11

**Entidad:** Banco Control de Datos Sintético (901666888) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Ariadna, versión 0.1.0 · **Comando:** `rule-check`

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

La corrida quedó registrada como `2026-11-25-rule-check-1`, con 0 hallazgos. La salida mostrada está en `estado-datos/901666888-banco-control-de-datos-sintetico/corridas/salida-rule-check.md`.