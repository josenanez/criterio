# /criterio-roles:roles-setup talento/900777888-cooperativa-control-sintetica

Norma quedó instalada sobre la Cooperativa Control Sintética (NIT 900777888). Procesé y crucé contra la CUOC los tres perfiles de cargo, y el primer reporte no dejó nada abierto.

La revisión del perfil del contador (PC-11) está fijada para el 2026-11-17, mañana. No sale como señal porque la política no dice cada cuántos meses se revisa un perfil.

- **Configuración:** `.criterio/perfiles/900777888/config.json`, con la CUOC como estándar. Equivalencia con la CINE: Técnico laboral → 4, Tecnólogo → 5, Profesional → 6. La política prohíbe pedir edad, sexo, estado civil y fotografía. Los meses entre revisiones quedaron sin valor porque la política no los da.
- **Términos:** quedaron aceptados a nombre de José Francisco Ñáñez el 2026-11-16 (v1.5). El comprobante está en `.criterio/terminos/aceptacion-criterio-roles-0.1.0-2026-11-16.md` y en su `.pdf`.
- **Lo que no hice:** no dejé la marca `_CRITERIO_TALENTO.txt` ni creé la tarea diaria, porque nadie dio un sí explícito. A mano se corre con `/criterio-roles:roles-wake`.
- **Un tropiezo con el motor:** la primera vez rechazó la ficha porque esperaba cada pregunta con su respuesta. La corregí y el cálculo corrió bien.

---

# Los perfiles contra su ocupación · Cooperativa Control Sintética · periodo 2026-11

**Entidad:** Cooperativa Control Sintética (900777888) · **Fecha de corte:** 2026-11-16 · **Procesado:** 2026-11-16 · **Agente:** Norma, versión 0.1.0 · **Comando:** `profile-check`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

| Perfil | Ocupación | Nivel | Estudios | Requisitos | Tareas | Del estándar sin recoger | Revisión |
|---|---|---|---|---|---|---|---|
| PC-11 · Contador | 24111 · Contadores sintéticos | 4 | Profesional | 5 | 2 | 0 | 2026-11-17 |
| PC-12 · Auxiliar contable | 43111 · Auxiliares contables sintéticos | 2 | Técnico laboral | 2 | 1 | 0 | 2027-01-01 |
| PC-13 · Desarrollador de software | 25120 · Desarrolladores de software sintéticos | 4 | Tecnólogo | 3 | 1 | 0 | 2027-01-01 |

El perfil lo aprueba una persona: aquí se dice qué le falta frente a su ocupación y qué requisito no se apoya en una tarea.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Entidad, identificación fiscal y país? → Cooperativa Control Sintética, NIT 900777888, CO — de la carpeta y la política de selección
- ¿Periodo? → 2026-11
- ¿Estándar de ocupaciones y su descarga? → CUOC; 00-referencia/estandar/PerfilesOcupacionales-Excel-CUOC-2026-sintetico.xlsx
- ¿Equivalencia de los niveles de estudio con la CINE? → Técnico laboral 4, Tecnólogo 5, Profesional 6 — propuesta desde los perfiles
- ¿Cada cuántos meses se revisa un perfil? → La política no lo dice; queda sin valor
- ¿Qué prohíbe pedir la política? → Edad, sexo, estado civil, fotografía — politica-de-seleccion.pdf, «Lo que no se pide»
- ¿Dónde se guarda el estado? → estado-talento/900777888-cooperativa-control-sintetica
- ¿Se acepta los términos? → Sí, José Francisco Ñáñez, v1.5, 2026-11-16
- ¿Se deja la marca _CRITERIO_TALENTO.txt? → No; nadie la autorizó en esta sesión

## Fuentes

- Sin documentos citados.
- Fuentes técnicas: F-03 (families/criterio-chro/FUENTES.es.md)

---

**Cuándo vuelvo:** sin reloj. La corrida quedó registrada como `2026-11-16-roles-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.