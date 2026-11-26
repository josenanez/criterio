# /criterio-data-quality:rule-check 

Los términos están vigentes (versión 1.6). Las tres reglas que miden datos críticos corrieron en el periodo. La cuarta, de un dato no crítico, no tiene corrida.

# Las reglas de calidad · Retail Control de Datos Sintético · periodo 2026-11

**Entidad:** Retail Control de Datos Sintético (RCC200101CD2) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Ariadna, versión 0.2.0 · **Comando:** `rule-check`

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

La corrida quedó registrada como `2026-11-25-rule-check-1`, con 0 hallazgos. Dos aclaraciones sobre cómo se hizo:

- **Archivo guardado:** el texto completo está en `estado-datos/rcc200101cd2-retail-control-de-datos-sintetico/corridas/salida-rule-check.md`. El reporte del motor también queda en `calidad/2026-11/reporte-rule-check.md` dentro de esa carpeta de estado. No abrí esa ruta para comprobarlo.
- **Aceptación de términos:** el agente no mostró la aceptación pendiente, porque ya figuraba como aceptada en la versión 0.2.0. Por eso no registré a José Francisco Ñáñez.