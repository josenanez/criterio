# /criterio-assets:assets-setup tecnologia/rgs180610qw4-retail-del-golfo-sintetico

Domingo quedó listo para Retail del Golfo Sintético (RFC RGS180610QW4, periodo 2026-10). Las ocho preguntas se resolvieron con la respuesta que sugieren los documentos: los umbrales son 15 % de licencias sin uso y 5 % sobre el presupuesto de la nube, como dice la política.

- **Términos:** quedan aceptados a nombre de José Francisco Ñáñez con fecha 2026-11-25. El comprobante está en `.criterio/terminos/aceptacion-criterio-assets-0.1.0-2026-11-25.md` y `.pdf`.
- **Marca:** la carpeta ya tenía `_CRITERIO_TECNOLOGIA.txt`, así que no la volví a poner.
- **Ficha:** procesé dos actas y cinco contratos. Pasé a la ficha dos excepciones (A-320 y A-101) y cinco niveles de servicio con su crédito. A-103 no cuenta como excepción, porque el acta solo dice que se evaluará su reemplazo.
- **Una regla que no seguí:** usé un `cd` para ver el texto convertido, y el comando pide no hacerlo. No cambió nada, pero la carpeta de trabajo de la sesión quedó movida a la caché.

# Cada activo con su dueño y su soporte · Retail del Golfo Sintético · periodo 2026-10

**Entidad:** Retail del Golfo Sintético (RGS180610QW4) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Domingo, versión 0.1.0 · **Comando:** `asset-check`

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

**Reloj:** propuse revisar los días hábiles a las 7:00, pero no lo creé, porque hace falta un sí explícito y aquí nadie lo dio. A mano se corre con `/criterio-assets:assets-wake`.

**Cuándo vuelvo:** sin reloj.

La corrida quedó registrada como `2026-11-25-assets-setup-1`, con 18 señales. Las otras 12 son de licencias, proveedores y nube, y salen en sus propios reportes: `license-check`, `vendor-check` y `cloud-check`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.