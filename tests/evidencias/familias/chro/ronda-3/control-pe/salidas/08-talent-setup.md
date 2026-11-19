# /criterio-talent:talent-setup talento/20601234567-servicios-andinos-control-sinteticos

Cándido ya está configurado sobre Servicios Andinos Control Sintéticos (RUC 20601234567, Perú). El reporte de vacantes de 2026-11 salió, pero ningún candidato se pudo comparar todavía requisito por requisito con su perfil, porque Norma no ha procesado los perfiles SA-01 y SA-02. Eso se resuelve con `/criterio-roles:roles-scan`.

**Lo que reconocí en los registros:**
- **Vacantes:** Vacante, Perfil, Apertura, Cierre, Estado, Plazo días y Responsable.
- **Autorizaciones:** candidato, fecha y finalidad.
- **Exportación del ATS:** Candidate ID, Requisition ID, Applied Date, Stage y Last Activity. No hubo que registrar ninguna columna en `columns`.

**Las respuestas que tomé (la sugerida en cada caso):**
- **Entidad, país y estándar:** los mismos que dejó Norma; el estándar es O*NET (`00-referencia/onet-31-0-sintetico`).
- **Periodo:** 2026-11.
- **Plazo para cubrir una vacante:** 40 días. La política dice: «Una vacante se cubre en un máximo de 40 días calendario desde su apertura» (`00-referencia/politica-de-seleccion.pdf`, Plazos).
- **Conservación de los datos de un candidato:** 150 días. La política dice: «se conservan 150 días desde que termina su proceso» (misma página).
- **Publicar reportes de candidatos en Rostrum:** no.
- **Dónde guardo lo que encuentro:** `estado-talento/20601234567-servicios-andinos-control-sinteticos`.
- **Marcar la carpeta con `_CRITERIO_TALENTO.txt`:** no, porque nadie lo autorizó.
- **Términos 1.6:** los acepta José Francisco Ñáñez con fecha 2026-11-16. El comprobante quedó en `.criterio/terminos/aceptacion-criterio-talent-0.1.0-2026-11-16.md` y `.pdf`.

**La configuración** quedó en `.criterio/seleccion/20601234567/config.json` y el motor la validó sin problemas.

**La ficha de 2026-11** recoge las hojas de vida y los soportes de `30-candidatos/`:
- El motor no procesa el `diploma.jpg` de CAN-506. Lo abrí solo para confirmar que es el diploma escaneado, y quedó como soporte.
- La hoja de vida de CAN-508 trae el sexo de la persona. La ficha registra solo qué tipo de dato es y dónde está, y el motor lo deja fuera del análisis.

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

- `20-vacantes`: la vacante VAC-41 no tiene un perfil procesado por Norma: sus candidatos no se contrastan requisito por requisito
- `20-vacantes`: la vacante VAC-42 no tiene un perfil procesado por Norma: sus candidatos no se contrastan requisito por requisito
- `20-vacantes`: la vacante VAC-43 no tiene un perfil procesado por Norma: sus candidatos no se contrastan requisito por requisito

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- Sin documentos citados.

---

**Revisión diaria:** no creé la tarea programada, porque nadie dio un sí explícito. Para correrlo a mano: `/criterio-talent:talent-wake`.

**Cuándo vuelvo:** sin reloj.

La corrida quedó registrada como `2026-11-16-talent-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.