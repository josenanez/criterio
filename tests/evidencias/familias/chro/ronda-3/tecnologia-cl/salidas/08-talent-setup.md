# /criterio-talent:talent-setup talento/76543210k-nube-austral-software-sintetica

Cándido quedó listo sobre Nube Austral Software Sintética (RUT 76543210-K). Las dos vacantes VAC-21 y VAC-24 siguen abiertas después del plazo que da la política.

- **Configuración:** está en `.criterio/seleccion/76543210k/config.json` y el motor la validó sin problemas. Las respuestas salieron de los documentos:
  - Plazo para cubrir una vacante: 60 días, de la política de selección. VAC-24 trae en el registro su propio plazo de 45 días, y ese manda.
  - Conservación de los datos de un candidato: 90 días, también de la política.
  - Estándar: O*NET, el mismo que usa Norma.
  - Los reportes de candidatos no se publican en Rostrum.
  - El estado se guarda en `estado-talento/76543210k-nube-austral-software-sintetica`.
- **Términos:** quedaron aceptados por José Francisco Ñáñez el 2026-11-16. El comprobante está en `.criterio/terminos/aceptacion-criterio-talent-0.1.0-2026-11-16.md` y en `.pdf`.
- **Marca de la carpeta:** ya existía, así que no la toqué.
- **Columnas:** el motor reconoció todas las de los registros de vacantes y autorizaciones, de la exportación del ATS y de la base interna. Por eso `columns` queda vacío.
- **Ficha de 2026-11:** registra los 10 candidatos de `30-candidatos/`, solo por su identificador.
  - Dos fotografías (CAN-302 y CAN-306) y una fecha de nacimiento (CAN-306) quedan anotadas solo por tipo y lugar, y no se usan para nada.
  - El cálculo dejó 13 señales en total. Las de candidatos y datos se ven con `/criterio-talent:cv-check` y `/criterio-talent:privacy-check`.

# Las vacantes contra su plazo · Nube Austral Software Sintética · periodo 2026-11

**Entidad:** Nube Austral Software Sintética (76543210k) · **Fecha de corte:** 2026-11-16 · **Procesado:** 2026-11-16 · **Agente:** Cándido, versión 0.1.0 · **Comando:** `vacancy-status`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una vacante sigue abierta después del plazo de cobertura de la política (`vacancy_past_target`) | VAC-21 · TI-01: abierta desde el 2026-08-10; la política da 60 días y el plazo venció el 2026-10-09 | — | Tomás Vidal | 38 | `20-vacantes/registro-vacantes.xlsx` fila 2 |
| 2 | Una vacante sigue abierta después del plazo de cobertura de la política (`vacancy_past_target`) | VAC-24 · TI-05: abierta desde el 2026-09-01; la política da 45 días y el plazo venció el 2026-10-16 | — | Tomás Vidal | 31 | `20-vacantes/registro-vacantes.xlsx` fila 5 |

## El resultado

| Vacante | Perfil | Apertura | Plazo | Tope | Cierre | Días | Responsable |
|---|---|---|---|---|---|---|---|
| VAC-21 | TI-01 | 2026-08-10 | 60 días | 2026-10-09 | — | 98 | Tomás Vidal |
| VAC-22 | TI-03 | 2026-10-30 | 60 días | 2026-12-29 | — | 17 | Tomás Vidal |
| VAC-23 | TI-02 | 2026-06-01 | 60 días | 2026-07-31 | 2026-07-20 | 49 | Tomás Vidal |
| VAC-24 | TI-05 | 2026-09-01 | 45 días | 2026-10-16 | — | 76 | Tomás Vidal |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `20-vacantes/registro-vacantes.xlsx`

---

No creé la tarea programada diaria porque nadie dio un sí explícito en esta sesión de prueba. Para revisar lo que toca, se corre a mano `/criterio-talent:talent-wake`.

**Cuándo vuelvo:** sin reloj.

La corrida quedó registrada como `2026-11-16-talent-setup-1`. Lo que se mostró está en `estado-talento/76543210k-nube-austral-software-sintetica/corridas/salida-talent-setup.md`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.