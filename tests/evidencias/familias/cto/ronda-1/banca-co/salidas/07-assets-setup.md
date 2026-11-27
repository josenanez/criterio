# /criterio-assets:assets-setup tecnologia/901222444-banco-meridiano-sintetico

Domingo quedó instalado sobre el Banco Meridiano Sintético (NIT 901222444), con el periodo 2026-10. La primera revisión de activos marca 6 puntos: 3 activos en producción sin soporte ni excepción vigente y 3 sin dueño.

- **Configuración:** quedó en `.criterio/activos/901222444/config.json`, con 15 % de licencias pagadas sin uso y 5 % sobre el presupuesto de la nube, ambos tomados de la política. La entidad, el periodo y la carpeta de estado coinciden con los de Fausto.
- **Términos:** los aceptó José Francisco Ñáñez el 2026-11-25. El comprobante está en `.criterio/terminos/aceptacion-criterio-assets-0.1.0-2026-11-25.md` y `.pdf`.
- **Marca:** `_CRITERIO_TECNOLOGIA.txt` quedó en la carpeta de la entidad; tomé el sí como respuesta sugerida.
- **Ficha del periodo:** procesé las 2 actas del comité de arquitectura y los 5 contratos. Pasaron a la ficha la excepción de A-320 (venció el 2026-09-30), la de A-101 (vigente hasta el 2027-03-31) y el nivel de servicio de cada uno de los 5 proveedores. A-103 solo aparece como «se evaluará su reemplazo», así que no tiene excepción.
- **Cálculo del periodo:** marcó 18 señales en total, 3 de cada tipo, entre licencias, nube y proveedores además de activos. El reporte de abajo cubre solo los activos.

# Cada activo con su dueño y su soporte · Banco Meridiano Sintético · periodo 2026-10

**Entidad:** Banco Meridiano Sintético (901222444) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Domingo, versión 0.1.0 · **Comando:** `asset-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un activo en producción pasó la fecha de fin de soporte de su fabricante sin una excepción aprobada vigente (`asset_out_of_support`) | A-310 · Servidor de la base de datos de clientes: corre en producción y su fabricante terminó el soporte el 2025-12-31; no tiene una excepción aprobada | — | — | 329 | `30-activos/inventario_de_activos.xlsx` fila 9 |
| 2 | Un activo en producción pasó la fecha de fin de soporte de su fabricante sin una excepción aprobada vigente (`asset_out_of_support`) | A-330 · Gestor de colas de mensajes: corre en producción y su fabricante terminó el soporte el 2026-04-30; no tiene una excepción aprobada | — | — | 209 | `30-activos/inventario_de_activos.xlsx` fila 11 |
| 3 | Un activo en producción pasó la fecha de fin de soporte de su fabricante sin una excepción aprobada vigente (`asset_out_of_support`) | A-320 · Sistema operativo del servidor de pagos: corre en producción y su fabricante terminó el soporte el 2026-06-30; su excepción venció el 2026-09-30 | — | — | 148 | `30-activos/inventario_de_activos.xlsx` fila 10 |
| 4 | Un activo del inventario no tiene dueño (`asset_without_owner`) | A-210 · Servidor de integración: el inventario no le asigna un dueño | — | — | — | `30-activos/inventario_de_activos.xlsx` fila 6 |
| 5 | Un activo del inventario no tiene dueño (`asset_without_owner`) | A-220 · Balanceador de carga: el inventario no le asigna un dueño | — | — | — | `30-activos/inventario_de_activos.xlsx` fila 7 |
| 6 | Un activo del inventario no tiene dueño (`asset_without_owner`) | A-230 · Repositorio de archivos: el inventario no le asigna un dueño | — | — | — | `30-activos/inventario_de_activos.xlsx` fila 8 |

## El resultado

| Activo | Dueño | Ambiente | Fin de soporte | Excepción hasta |
|---|---|---|---|---|
| A-100 · Sistema central | Infraestructura | Producción | 2028-12-31 | — |
| A-101 · Servidor de reportes | Infraestructura | Producción | 2026-03-31 | 2027-03-31 |
| A-102 · Servidor del laboratorio | Infraestructura | Pruebas | 2024-06-30 | — |
| A-103 · Plataforma de correo | Infraestructura | Producción | 2026-12-31 | — |
| A-210 · Servidor de integración | — | Producción | 2029-06-30 | — |
| A-220 · Balanceador de carga | — | Producción | 2029-06-30 | — |
| A-230 · Repositorio de archivos | — | Producción | 2029-06-30 | — |
| A-310 · Servidor de la base de datos de clientes | Infraestructura | Producción | 2025-12-31 | — |
| A-320 · Sistema operativo del servidor de pagos | Infraestructura | Producción | 2026-06-30 | 2026-09-30 |
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

**Reloj:** propuse revisar lo que toca los días hábiles a las 7:00, pero sin un sí explícito no creé la tarea. Para correrlo a mano: `/criterio-assets:assets-wake`.

**Cuándo vuelvo:** sin reloj.

La corrida quedó registrada como `2026-11-25-assets-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.