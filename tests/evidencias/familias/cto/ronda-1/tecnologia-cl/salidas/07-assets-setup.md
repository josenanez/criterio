# /criterio-assets:assets-setup tecnologia/76543210-k-software-austral-sintetico

Domingo quedó instalado sobre Software Austral Sintético (RUT 76543210-K) y ya hizo la primera revisión del periodo 2026-10. Encontró 12 señales; 4 son de activos y van abajo.

**Cómo quedó el setup.** Todas las respuestas salieron de los documentos:
- **Carpeta:** había una sola y ya estaba marcada con `_CRITERIO_TECNOLOGIA.txt`. Tiene sus 23 documentos en su lugar, así que no la volví a marcar.
- **Entidad:** Chile, en pesos chilenos. Coincide con lo que ya había fijado el setup de Fausto.
- **Umbrales:** se toleran hasta 15 % de licencias pagadas sin uso y hasta 5 % sobre el presupuesto de cada cuenta de la nube. Los dos vienen de la política aprobada el 2025-11-20.
- **Rostrum:** sí se publica, porque la política no dice otra cosa.
- **Estado:** queda en `estado-tecnologia/76543210-k-software-austral-sintetico`.
- **Configuración:** `.criterio/activos/76543210-K/config.json`.
- **Términos v1.6:** se registró la aceptación de José Francisco Ñáñez con fecha 2026-11-25. El comprobante está en `.criterio/terminos/aceptacion-criterio-assets-0.1.0-2026-11-25.md` y `.pdf`.

**La ficha de 2026-10:**
- **Excepciones:** dos. A-320 tiene excepción hasta 2026-09-30, según el acta de marzo, y A-101 hasta 2027-03-31, según el acta de octubre. El acta de octubre solo menciona A-103 («se evaluará su reemplazo»), así que no lo cuento como excepción.
- **Niveles de servicio:** cuatro, uno por contrato: Centro de Datos Uno, Enlaces del Pacífico, Mesa de Ayuda Sintética y Nube Andina.

**Las 12 señales,** de a dos por tipo:
- activos sin soporte;
- activos sin dueño;
- licencias en uso sin comprar;
- licencias pagadas sin uso;
- proveedores que no cumplieron su nivel y no tienen el crédito en la factura;
- cuentas de la nube por encima de su presupuesto.

Este es el reporte de activos que escribió el motor. Las demás señales salen con `/criterio-assets:license-check`, `/criterio-assets:vendor-check` y `/criterio-assets:cloud-check`.

# Cada activo con su dueño y su soporte · Software Austral Sintético · periodo 2026-10

**Entidad:** Software Austral Sintético (76543210-K) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Domingo, versión 0.1.0 · **Comando:** `asset-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un activo en producción pasó la fecha de fin de soporte de su fabricante sin una excepción aprobada vigente (`asset_out_of_support`) | A-310 · Servidor de la base de datos de clientes: corre en producción y su fabricante terminó el soporte el 2025-12-31; no tiene una excepción aprobada | — | — | 329 | `30-activos/inventario_de_activos.xlsx` fila 8 |
| 2 | Un activo en producción pasó la fecha de fin de soporte de su fabricante sin una excepción aprobada vigente (`asset_out_of_support`) | A-320 · Sistema operativo del servidor de pagos: corre en producción y su fabricante terminó el soporte el 2026-06-30; su excepción venció el 2026-09-30 | — | — | 148 | `30-activos/inventario_de_activos.xlsx` fila 9 |
| 3 | Un activo del inventario no tiene dueño (`asset_without_owner`) | A-210 · Servidor de integración: el inventario no le asigna un dueño | — | — | — | `30-activos/inventario_de_activos.xlsx` fila 6 |
| 4 | Un activo del inventario no tiene dueño (`asset_without_owner`) | A-220 · Balanceador de carga: el inventario no le asigna un dueño | — | — | — | `30-activos/inventario_de_activos.xlsx` fila 7 |

## El resultado

| Activo | Dueño | Ambiente | Fin de soporte | Excepción hasta |
|---|---|---|---|---|
| A-100 · Sistema central | Infraestructura | Producción | 2028-12-31 | — |
| A-101 · Servidor de reportes | Infraestructura | Producción | 2026-03-31 | 2027-03-31 |
| A-102 · Servidor del laboratorio | Infraestructura | Pruebas | 2024-06-30 | — |
| A-103 · Plataforma de correo | Infraestructura | Producción | 2026-12-31 | — |
| A-210 · Servidor de integración | — | Producción | 2029-06-30 | — |
| A-220 · Balanceador de carga | — | Producción | 2029-06-30 | — |
| A-310 · Servidor de la base de datos de clientes | Infraestructura | Producción | 2025-12-31 | — |
| A-320 · Sistema operativo del servidor de pagos | Infraestructura | Producción | 2026-06-30 | 2026-09-30 |

Si un activo se renueva, se retira o se exceptúa lo decide el comité de arquitectura: aquí se dice cuál corre sin dueño o sin soporte.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `30-activos/inventario_de_activos.xlsx`
- Fuentes técnicas: F-02 (families/criterio-cto/FUENTES.es.md)

**Cuándo vuelvo:** sin reloj. Crear la tarea programada necesita un sí explícito, y en esta prueba nadie lo dio. Para correrlo a mano: `/criterio-assets:assets-wake`.

Lo que mostré quedó guardado en `estado-tecnologia/76543210-k-software-austral-sintetico/corridas/salida-assets-setup.md`, y la corrida quedó registrada como `2026-11-25-assets-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.