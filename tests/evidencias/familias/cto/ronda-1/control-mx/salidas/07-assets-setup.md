# /criterio-assets:assets-setup tecnologia/rct190101ab2-retail-control-de-tecnologia-sintetico

Soy Domingo. Pongo cada activo al lado de su dueño y su soporte, y cada proveedor al lado de su nivel; no elijo proveedores ni interpreto contratos.

Domingo quedó listo para Retail Control de Tecnología Sintético (RCT190101AB2). La primera revisión de activos no encontró nada abierto.

**La carpeta.** Encontré una sola candidata: `tecnologia/rct190101ab2-retail-control-de-tecnologia-sintetico`. Ya estaba marcada con `_CRITERIO_TECNOLOGIA.txt` y tiene las seis subcarpetas, de `00-politica/` a `50-nube/`. Tomé esa. Trae 19 documentos; ninguno está fuera de lugar ni es ilegible.

**Las respuestas.** No pregunté lo que el setup de Fausto ya había fijado, y lo demás lo tomé de los documentos:
- **Entidad:** RCT190101AB2, México, en pesos mexicanos.
- **Periodo:** 2026-10.
- **Licencias pagadas sin uso:** se tolera hasta el 15 %. **Cuentas de la nube:** hasta un 5 % sobre su presupuesto. Ambas cifras están en la política aprobada el 2025-11-20.
- **Publicar en Rostrum:** sí, porque la política no dice otra cosa.
- **Dónde guardo lo que encuentro:** `estado-tecnologia/rct190101ab2-retail-control-de-tecnologia-sintetico`, el mismo de Fausto.
- **Marca:** no hacía falta otra.

**Términos.** José Francisco Ñáñez aceptó la versión 1.6 el 2026-11-25. El comprobante quedó en `.criterio/terminos/aceptacion-criterio-assets-0.1.0-2026-11-25.md` y su `.pdf`.

**Configuración:** `.criterio/activos/RCT190101AB2/config.json`.

**La ficha de 2026-10.**
- **Excepción:** el acta del comité de arquitectura aprueba que A-101 siga en producción hasta el 2027-03-31.
- **Centro de Datos Uno:** disponibilidad del 99,9 %, con crédito del 10 % si no se cumple.
- **Mesa de Ayuda Sintética:** 95 % de casos resueltos a tiempo, con crédito del 5 %.
- **A-103:** el acta solo dice que se evaluará su reemplazo, así que no lo registré como excepción.

Una cosa del reporte: la sección de fuentes dice «Sin documentos citados», aunque la excepción de A-101 sale del acta del comité de arquitectura. La ficha sí la cita. Parece una falla del motor.

# Cada activo con su dueño y su soporte · Retail Control de Tecnología Sintético · periodo 2026-10

**Entidad:** Retail Control de Tecnología Sintético (RCT190101AB2) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Domingo, versión 0.1.0 · **Comando:** `asset-check`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

| Activo | Dueño | Ambiente | Fin de soporte | Excepción hasta |
|---|---|---|---|---|
| A-100 · Sistema central | Infraestructura | Producción | 2028-12-31 | — |
| A-101 · Servidor de reportes | Infraestructura | Producción | 2026-03-31 | 2027-03-31 |
| A-102 · Servidor del laboratorio | Infraestructura | Pruebas | 2024-06-30 | — |
| A-103 · Plataforma de correo | Infraestructura | Producción | 2026-12-31 | — |

Si un activo se renueva, se retira o se exceptúa lo decide el comité de arquitectura: aquí se dice cuál corre sin dueño o sin soporte.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- Sin documentos citados.
- Fuentes técnicas: F-02 (families/criterio-cto/FUENTES.es.md)

**El reloj.** No creé la tarea programada de los días hábiles a las 7:00 porque nadie dio un sí explícito. A mano se corre con `/criterio-assets:assets-wake`.

**Cuándo vuelvo:** sin reloj.

La corrida quedó registrada como `2026-11-25-assets-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.