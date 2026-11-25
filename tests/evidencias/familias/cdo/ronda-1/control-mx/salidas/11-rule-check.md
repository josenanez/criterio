# /criterio-data-quality:rule-check 

Los términos 1.6 están vigentes y la aceptación de José Francisco Ñáñez, del 2026-11-25, ya estaba registrada. El motor generó el reporte del periodo 2026-11 sin hallazgos, y la corrida quedó registrada.

# Las reglas de calidad · Retail Control de Datos Sintético · periodo 2026-11

**Entidad:** Retail Control de Datos Sintético (RCC200101CD2) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Ariadna, versión 0.1.0 · **Comando:** `rule-check`

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

**Dónde quedó:** el reporte está en `calidad/2026-11/reporte-rule-check.md`. Lo mostrado está en `corridas/salida-rule-check.md`. La corrida es `2026-11-25-rule-check-1`.