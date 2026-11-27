# /criterio-assets:asset-check 

Siete señales en los activos: cuatro corren en producción sin soporte de su fabricante ni excepción aprobada, y tres no tienen dueño en el inventario.

# Cada activo con su dueño y su soporte · Banco Meridiano Sintético · periodo 2026-11

**Entidad:** Banco Meridiano Sintético (901222444) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Domingo, versión 0.1.0 · **Comando:** `asset-check`

## Lo que hay que atender

| # | Señal | Qué | Días | Cita |
|---|---|---|---|---|
| 1 | Sin soporte y sin excepción (`asset_out_of_support`) | A-310 · Servidor de la base de datos de clientes: el fabricante terminó el soporte el 2025-12-31 | 329 | `30-activos/inventario_de_activos.xlsx` fila 9 |
| 2 | Sin soporte y sin excepción (`asset_out_of_support`) | A-101 · Servidor de reportes: soporte terminado el 2026-03-31 | 239 | fila 3 |
| 3 | Sin soporte y sin excepción (`asset_out_of_support`) | A-330 · Gestor de colas de mensajes: soporte terminado el 2026-04-30 | 209 | fila 11 |
| 4 | Sin soporte y sin excepción (`asset_out_of_support`) | A-320 · Sistema operativo del servidor de pagos: soporte terminado el 2026-06-30 | 148 | fila 10 |
| 5 | Sin dueño (`asset_without_owner`) | A-210 · Servidor de integración | — | fila 6 |
| 6 | Sin dueño (`asset_without_owner`) | A-220 · Balanceador de carga | — | fila 7 |
| 7 | Sin dueño (`asset_without_owner`) | A-230 · Repositorio de archivos | — | fila 8 |

## El resultado

| Activo | Dueño | Ambiente | Fin de soporte | Excepción hasta |
|---|---|---|---|---|
| A-100 · Sistema central | Infraestructura | Producción | 2028-12-31 | — |
| A-101 · Servidor de reportes | Infraestructura | Producción | 2026-03-31 | — |
| A-102 · Servidor del laboratorio | Infraestructura | Pruebas | 2024-06-30 | — |
| A-103 · Plataforma de correo | Infraestructura | Producción | 2026-12-31 | — |
| A-210 · Servidor de integración | — | Producción | 2029-06-30 | — |
| A-220 · Balanceador de carga | — | Producción | 2029-06-30 | — |
| A-230 · Repositorio de archivos | — | Producción | 2029-06-30 | — |
| A-310 · Servidor de la base de datos de clientes | Infraestructura | Producción | 2025-12-31 | — |
| A-320 · Sistema operativo del servidor de pagos | Infraestructura | Producción | 2026-06-30 | — |
| A-330 · Gestor de colas de mensajes | Infraestructura | Producción | 2026-04-30 | — |

Si un activo se renueva, se retira o se exceptúa lo decide el comité de arquitectura: aquí se dice cuál corre sin dueño o sin soporte.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `30-activos/inventario_de_activos.xlsx`
- Fuentes técnicas: F-02 (families/criterio-cto/FUENTES.es.md)

---
Los términos ya estaban vigentes, así que no hizo falta registrar una aceptación nueva. Dejé la corrida registrada como `2026-11-25-asset-check-1`. Usé `--today 2026-11-25` en las llamadas que lo aceptan. El comando `terminos` no lo aceptaba, así que lo corrí sin esa opción.