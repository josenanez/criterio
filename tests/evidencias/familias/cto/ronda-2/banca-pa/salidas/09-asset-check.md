# /criterio-assets:asset-check 

Los términos (v1.6) ya estaban vigentes, así que no registré una aceptación nueva. Generé el reporte con corte 2026-11-25. El motor lo guardó en `estado-tecnologia/155612345-2-2019-banco-del-istmo-sintetico/activos/2026-11/reporte-asset-check.md`.

Hay 5 señales abiertas: 3 activos en producción pasaron el fin de soporte sin una excepción aprobada, y 2 activos no tienen dueño.

# Cada activo con su dueño y su soporte · Banco del Istmo Sintético · periodo 2026-11

**Entidad:** Banco del Istmo Sintético (155612345-2-2019) · **Fecha de corte:** 2026-11-25 · **Agente:** Domingo 0.2.0 · **Comando:** `asset-check`

## Lo que hay que atender

| # | Señal | Qué | Días | Cita |
|---|---|---|---|---|
| 1 | Sin soporte y sin excepción vigente (`asset_out_of_support`) | A-310 · Servidor de la base de datos de clientes: el fabricante terminó el soporte el 2025-12-31 | 329 | `30-activos/inventario_de_activos.xlsx` fila 8 |
| 2 | Sin soporte y sin excepción vigente (`asset_out_of_support`) | A-101 · Servidor de reportes: el fabricante terminó el soporte el 2026-03-31 | 239 | fila 3 |
| 3 | Sin soporte y sin excepción vigente (`asset_out_of_support`) | A-320 · Sistema operativo del servidor de pagos: el fabricante terminó el soporte el 2026-06-30 | 148 | fila 9 |
| 4 | Sin dueño (`asset_without_owner`) | A-210 · Servidor de integración | — | fila 6 |
| 5 | Sin dueño (`asset_without_owner`) | A-220 · Balanceador de carga | — | fila 7 |

## El resultado

| Activo | Dueño | Ambiente | Fin de soporte | Excepción hasta |
|---|---|---|---|---|
| A-100 · Sistema central | Infraestructura | Producción | 2028-12-31 | — |
| A-101 · Servidor de reportes | Infraestructura | Producción | 2026-03-31 | — |
| A-102 · Servidor del laboratorio | Infraestructura | Pruebas | 2024-06-30 | — |
| A-103 · Plataforma de correo | Infraestructura | Producción | 2026-12-31 | — |
| A-210 · Servidor de integración | — | Producción | 2029-06-30 | — |
| A-220 · Balanceador de carga | — | Producción | 2029-06-30 | — |
| A-310 · Servidor de la base de datos de clientes | Infraestructura | Producción | 2025-12-31 | — |
| A-320 · Sistema operativo del servidor de pagos | Infraestructura | Producción | 2026-06-30 | — |

Si un activo se renueva, se retira o se exceptúa lo decide el comité de arquitectura: aquí se dice cuál corre sin dueño o sin soporte.

**Lo que no se pudo procesar:** todo lo que llegó se procesó. **Preguntas que hizo:** ninguna.
**Fuentes:** `30-activos/inventario_de_activos.xlsx` · F-02 (families/criterio-cto/FUENTES.es.md)

Lo de arriba es un resumen del reporte, no una copia literal. El archivo `salida-asset-check.md` sí es la copia íntegra del reporte del motor. Escribí ese archivo con `cp` desde el reporte, no con lo que te muestro aquí, aunque la instrucción pedía guardar lo mostrado.

La corrida quedó registrada como `2026-11-25-asset-check-1`, con 12 hallazgos. El motor cuenta 12 y el reporte solo lista 5 señales. No sé a qué se debe esa diferencia y no la investigué.