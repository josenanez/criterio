# /criterio-assets:asset-check 

Los términos ya estaban vigentes (versión 1.6), así que no hizo falta registrar la aceptación. Un activo en producción corre sin soporte del fabricante y sin excepción.

# Cada activo con su dueño y su soporte · Retail Control de Tecnología Sintético · periodo 2026-11

**Entidad:** Retail Control de Tecnología Sintético (RCT190101AB2) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Domingo, versión 0.1.0 · **Comando:** `asset-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un activo en producción pasó la fecha de fin de soporte de su fabricante sin una excepción aprobada vigente (`asset_out_of_support`) | A-101 · Servidor de reportes: corre en producción y su fabricante terminó el soporte el 2026-03-31; no tiene una excepción aprobada | — | — | 239 | `30-activos/inventario_de_activos.xlsx` fila 3 |

## El resultado

| Activo | Dueño | Ambiente | Fin de soporte | Excepción hasta |
|---|---|---|---|---|
| A-100 · Sistema central | Infraestructura | Producción | 2028-12-31 | — |
| A-101 · Servidor de reportes | Infraestructura | Producción | 2026-03-31 | — |
| A-102 · Servidor del laboratorio | Infraestructura | Pruebas | 2024-06-30 | — |
| A-103 · Plataforma de correo | Infraestructura | Producción | 2026-12-31 | — |

Si un activo se renueva, se retira o se exceptúa lo decide el comité de arquitectura: aquí se dice cuál corre sin dueño o sin soporte.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `30-activos/inventario_de_activos.xlsx`
- Fuentes técnicas: F-02 (families/criterio-cto/FUENTES.es.md)

---
La corrida quedó registrada como `2026-11-25-asset-check-1`. El registro dice `hallazgos: 0`, aunque el reporte trae una señal. Es una discrepancia del motor que no revisé.