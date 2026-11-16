# /criterio-talent:talent-scan 

El comando `/criterio-talent:talent-scan` no se cargó en esta sesión, aunque el plugin `criterio-talent` 0.1.0 está instalado para esta carpeta. Seguí paso a paso su definición, `commands/talent-scan.md`, y corrí su motor con `--today 2026-11-16`. Los términos ya estaban vigentes: los aceptó José Francisco Ñáñez el 2026-11-16 y no hizo falta volver a registrarlos.

---

Ninguna hoja de vida nueva ni cambiada desde la corrida anterior: las de la ficha ya estaban desde el setup. El archivo `diploma.jpg` de CAN-406 es una imagen y, por regla, se toma por fotografía y no se abre; si es el diploma, conviene que la organización lo entregue en PDF para que soporte el título.

# Qué cambió en la selección · Cooperativa Control Sintética · periodo 2026-11

**Entidad:** Cooperativa Control Sintética (900777888) · **Fecha de corte:** 2026-11-16 · **Procesado:** 2026-11-16 · **Agente:** Cándido, versión 0.1.0 · **Comando:** `talent-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | La hoja de vida afirma un título, una certificación o un empleo sin el documento que lo soporte (`claim_without_support`) | CAN-406: el título «Contador público» no tiene el documento que lo soporte | — | — | — | `30-candidatos/VAC-31/CAN-406/hoja-de-vida.pdf` |
| 2 | Llegó un dato que no se debe tratar —fotografía, edad, documento de identidad, salud—, y se excluye del análisis (`protected_data_received`) | CAN-406: llegó fotografia; se excluye del análisis y no se usa para nada | — | — | — | `30-candidatos/VAC-31/CAN-406/diploma.jpg` |
| 3 | Llegó un dato que no se debe tratar —fotografía, edad, documento de identidad, salud—, y se excluye del análisis (`protected_data_received`) | CAN-408: llegó sexo; se excluye del análisis y no se usa para nada | — | — | — | `30-candidatos/VAC-31/CAN-408/hoja-de-vida.pdf` |

## El resultado

**En la ficha:** 10 candidatos · **Vacantes en el registro:** 3 · **Perfiles de Norma:** 3 (periodo 2026-11).

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Plazo de cobertura de una vacante? → 45 días calendario desde la apertura, salvo plazo propio en el registro · 00-referencia/politica-de-seleccion.pdf, Plazos · Respuesta sugerida, tomada sin interlocutor (sesión de prueba, 2026-11-16)
- ¿Días de conservación de los datos de un candidato no seleccionado? → 180 días desde que termina su proceso · 00-referencia/politica-de-seleccion.pdf, Plazos · Respuesta sugerida, tomada sin interlocutor (sesión de prueba, 2026-11-16)
- ¿Se publican los reportes de candidatos en Rostrum? → No · Respuesta sugerida, tomada sin interlocutor (sesión de prueba, 2026-11-16)
- ¿Se marca la carpeta con _CRITERIO_TALENTO.txt? → No · Respuesta sugerida, tomada sin interlocutor (sesión de prueba, 2026-11-16)

## Fuentes

- `30-candidatos/VAC-31/CAN-406/diploma.jpg`
- `30-candidatos/VAC-31/CAN-406/hoja-de-vida.pdf`
- `30-candidatos/VAC-31/CAN-408/hoja-de-vida.pdf`

---

La corrida quedó registrada como `2026-11-16-talent-scan-1` con 3 hallazgos. La salida completa está en `estado-talento/900777888-cooperativa-control-sintetica/corridas/salida-talent-scan.md`.

Hay dos inconsistencias del motor que conviene revisar:
- **CAN-406:** el inventario marcó `diploma.jpg` como ilegible porque el formato .jpg no está soportado. Aun así, el reporte dice «Todo lo que llegó se procesó» y trata el archivo como una fotografía.
- **Registro de errores:** `.criterio/rastro-errores.log` tiene un error de una corrida anterior de esta sesión de prueba (`parar KeyError('perfiles')`).