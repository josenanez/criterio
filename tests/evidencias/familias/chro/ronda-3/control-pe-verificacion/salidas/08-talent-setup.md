# /criterio-talent:talent-setup talento/20601234567-servicios-andinos-control-sinteticos

Cándido quedó instalado sobre Servicios Andinos Control Sintéticos (RUC 20601234567, Perú), para el periodo 2026-11. No hubo que inventar nada: cada respuesta salió de los documentos o de lo que ya había dejado Norma.

**Lo que quedó configurado** (en `.criterio/seleccion/20601234567/config.json`):
- **Carpeta:** solo había una candidata y ya estaba marcada con `_CRITERIO_TALENTO.txt`, así que no la volví a marcar.
- **Plazo para cubrir una vacante:** 40 días. **Conservación de los datos de un candidato que no quedó:** 150 días. Ambos salen de `00-referencia/politica-de-seleccion.pdf`.
- **Estándar de ocupaciones:** O*NET, el mismo que usa Norma.
- **Publicar en Rostrum:** no.
- **Dónde guardo lo que encuentro:** `estado-talento/20601234567-servicios-andinos-control-sinteticos`.
- **Columnas:** reconocí todas las del registro de vacantes, el de autorizaciones y la exportación del ATS, así que no hubo nada que registrar aparte.
- **Términos v1.6:** aceptados por José Francisco Ñáñez el 2026-11-16. El comprobante está en `.criterio/terminos/aceptacion-criterio-talent-0.1.0-2026-11-16.md` y `.pdf`.

**La primera ficha:** registré las 10 hojas de vida con sus títulos, empleos, soportes y la evidencia frente a cada requisito del perfil.
- El `diploma.jpg` de CAN-506 no se pudo convertir. Lo abrí solo para confirmar que es un diploma y quedó como soporte.
- La hoja de vida de CAN-508 trae el sexo. La ficha guarda solo el tipo de dato y dónde está; el motor lo excluye del análisis y es la única señal de esta corrida.

**El reporte del motor**, tal cual:

# Las vacantes contra su plazo · Servicios Andinos Control Sintéticos · periodo 2026-11

**Entidad:** Servicios Andinos Control Sintéticos (20601234567) · **Fecha de corte:** 2026-11-16 · **Procesado:** 2026-11-16 · **Agente:** Cándido, versión 0.1.0 · **Comando:** `vacancy-status`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

| Vacante | Perfil | Apertura | Plazo | Tope | Cierre | Días | Responsable |
|---|---|---|---|---|---|---|---|
| VAC-41 | SA-01 | 2026-10-10 | 40 días | 2026-11-19 | — | 37 | Jorge Salas |
| VAC-43 | SA-02 | 2026-11-05 | 40 días | 2026-12-15 | — | 11 | Jorge Salas |
| VAC-42 | SA-02 | 2026-05-01 | 40 días | 2026-06-10 | 2026-06-19 | 49 | Jorge Salas |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- Sin documentos citados.

**Cuándo vuelvo:** sin reloj. No creé la tarea programada porque nadie dio un sí explícito. Para correrlo a mano: `/criterio-talent:talent-wake`.

La corrida quedó registrada como `2026-11-16-talent-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.