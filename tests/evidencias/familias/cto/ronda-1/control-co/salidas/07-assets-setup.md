# /criterio-assets:assets-setup tecnologia/901333666-banco-control-de-tecnologia-sintetico

Domingo quedó listo para Banco Control de Tecnología Sintético (NIT 901333666), y el primer reporte de activos de octubre de 2026 no tiene nada abierto.

**Qué tomé y de dónde** (nadie tuvo que contestar nada):
- **Carpeta:** solo había una y ya tenía la marca, así que no la volví a marcar. Encontré 19 documentos.
- **Entidad y país:** banco colombiano, en pesos. Los tomé de la configuración que ya había dejado Fausto, el agente de cambios.
- **Periodo:** 2026-10.
- **Licencias:** se tolera hasta un 15 % pagado sin uso. La política dice: «Se tolera hasta un 15 % de licencias pagadas sin uso».
- **Nube:** cada cuenta puede pasarse hasta un 5 % de su presupuesto. La política dice: «no supera su presupuesto en más del 5 %».
- **Publicar en Rostrum:** sí, porque la política no dice lo contrario.
- **Estado:** `estado-tecnologia/901333666-banco-control-de-tecnologia-sintetico`.
- **Términos v1.6:** los mostré tal cual y quedaron aceptados por José Francisco Ñáñez el 2026-11-25. El comprobante está en `.criterio/terminos/aceptacion-criterio-assets-0.1.0-2026-11-25.md` y en el `.pdf` del mismo nombre.

**Qué quedó en la ficha de octubre:**
- **Excepción:** el comité de arquitectura aprobó que A-101 (servidor de reportes) siga en producción sin soporte hasta el 2027-03-31.
- **A-103 (plataforma de correo):** el acta solo dice «se evaluará su reemplazo», así que no le registré excepción.
- **Niveles de servicio:**
  - Centro de Datos Uno: disponibilidad de 99,9 % al mes, con crédito del 10 % de la factura si no se cumple.
  - Mesa de Ayuda Sintética: 95 % de casos resueltos a tiempo al mes, con crédito del 5 % de la factura.

**Reporte del motor:**

# Cada activo con su dueño y su soporte · Banco Control de Tecnología Sintético · periodo 2026-10

**Entidad:** Banco Control de Tecnología Sintético (901333666) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Domingo, versión 0.1.0 · **Comando:** `asset-check`

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

**Cuándo vuelvo:** no hay revisión programada, porque nadie dio el sí explícito a la tarea diaria. Para correrlo a mano: `/criterio-assets:assets-wake`.

La corrida quedó registrada como `2026-11-25-assets-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.