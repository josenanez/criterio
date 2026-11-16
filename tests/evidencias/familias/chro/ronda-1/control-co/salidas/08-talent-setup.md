# /criterio-talent:talent-setup talento/900777888-cooperativa-control-sintetica

Cándido quedó configurado para la Cooperativa Control Sintética (NIT 900777888) y generó el primer reporte del estado de las vacantes. El comando `/criterio-talent:talent-setup` no está cargado en esta sesión, aunque el plugin está activado en `.claude/settings.json`. Por eso seguí su definición, que está en la copia local del plugin (versión 0.1.0), y corrí su motor `talento.py` con `--today 2026-11-16`.

**Respuestas que tomé de los documentos:**
- **Carpeta:** `talento/900777888-cooperativa-control-sintetica`, la única que se encontró.
- **Entidad y periodo:** Colombia, periodo 2026-11.
- **Plazo para cubrir una vacante:** 45 días, según la política de selección.
- **Conservación de los datos de un candidato:** 180 días, según la misma política.
- **Estándar:** el CUOC sintético que ya usa Norma.
- **Publicar en Rostrum:** no.
- **Marca `_CRITERIO_TALENTO.txt` en la carpeta:** no.
- **Tarea diaria programada:** no; se corre a mano con `/criterio-talent:talent-wake`.
- **Términos 1.5:** aceptados a nombre de José Francisco Ñáñez. El comprobante quedó en `.criterio/terminos/aceptacion-criterio-talent-0.1.0-2026-11-16.md` y `.pdf`.

La configuración está en `.criterio/seleccion/900777888/config.json`.

**Lo que encontró el motor en las 10 hojas de vida de las 3 vacantes:**
- **Una afirmación sin soporte:** el título de CAN-406. Su diploma llegó en `.jpg` y el motor no procesa ese formato.
- **Dos datos que no se deben tratar:** uno es el campo «Sexo» en la hoja de vida de CAN-408. En la ficha solo quedó el tipo de dato y dónde está, no su valor.

En la ficha no quedaron nombres ni correos de los candidatos.

---

# Las vacantes contra su plazo · Cooperativa Control Sintética · periodo 2026-11

**Entidad:** Cooperativa Control Sintética (900777888) · **Fecha de corte:** 2026-11-16 · **Procesado:** 2026-11-16 · **Agente:** Cándido, versión 0.1.0 · **Comando:** `vacancy-status`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

| Vacante | Perfil | Apertura | Plazo | Tope | Cierre | Días | Responsable |
|---|---|---|---|---|---|---|---|
| VAC-31 | PC-11 | 2026-10-05 | 45 días | 2026-11-19 | — | 42 | Rosa Díaz |
| VAC-32 | PC-13 | 2026-08-01 | 120 días | 2026-11-29 | — | 107 | Rosa Díaz |
| VAC-33 | PC-12 | 2026-04-01 | 45 días | 2026-05-16 | 2026-05-20 | 49 | Rosa Díaz |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Plazo de cobertura de una vacante? → 45 días calendario desde la apertura, salvo plazo propio en el registro · 00-referencia/politica-de-seleccion.pdf, Plazos · Respuesta sugerida, tomada sin interlocutor (sesión de prueba, 2026-11-16)
- ¿Días de conservación de los datos de un candidato no seleccionado? → 180 días desde que termina su proceso · 00-referencia/politica-de-seleccion.pdf, Plazos · Respuesta sugerida, tomada sin interlocutor (sesión de prueba, 2026-11-16)
- ¿Se publican los reportes de candidatos en Rostrum? → No · Respuesta sugerida, tomada sin interlocutor (sesión de prueba, 2026-11-16)
- ¿Se marca la carpeta con _CRITERIO_TALENTO.txt? → No · Respuesta sugerida, tomada sin interlocutor (sesión de prueba, 2026-11-16)

## Fuentes

- Sin documentos citados.

---

**Fallas del motor que conviene revisar en esta versión:**
- **VAC-33 cerró después de su tope.** El reporte dice «nada que atender» aunque la tabla muestra el cierre después del tope.
- **«Fuentes» sale vacía.** El registro de vacantes no aparece citado.
- **«Lo que no se pudo procesar» queda incompleto.** Dice que todo se procesó, pero el `.jpg` de CAN-406 no se procesó.
- **Fechas al revés en el sistema de selección.** En la exportación, CAN-410 tiene la última actividad (2026-10-01) antes de su postulación (2026-11-01).
- **Hubo que reescribir las preguntas de la ficha.** El motor rechazó la primera ficha porque cada pregunta pide una respuesta. Dejé como preguntas las del setup, con las respuestas que tomé.

La salida quedó guardada en `estado-talento/900777888-cooperativa-control-sintetica/corridas/salida-talent-setup.md`, y la corrida quedó registrada como `2026-11-16-talent-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.