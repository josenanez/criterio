# /criterio-talent:talent-wake 

Desde la corrida anterior no llegó ningún documento nuevo ni cambió ninguno, así que esta fue la revisión semanal. No había peticiones abiertas y los términos ya estaban aceptados.

El inventario marca `30-candidatos/VAC-31/CAN-406/diploma.jpg` como ilegible por su formato, y la ficha lo registra como fotografía excluida. Si en realidad es el soporte del título de CAN-406, la organización tendría que entregarlo en PDF.

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

Hoy solo tocaba `talent-scan`. Dejé registradas las dos corridas con el caso 2026-11: `2026-11-16-talent-scan-3` y `2026-11-16-talent-wake-2`.