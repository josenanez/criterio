# /criterio-roles:profile-language 

Cuatro señales: PT-01 (R3, apariencia), PT-03 (R4, religión) y PT-04 (R2, edad y sexo) piden lo que la política o la ley no permiten pedir. La corrección es de una persona; aquí no se reescribe ningún requisito.

# Lo que un perfil no puede pedir · Tiendas del Bajío Sintéticas · periodo 2026-11

**Entidad:** Tiendas del Bajío Sintéticas (TBA110315K21) · **Fecha de corte:** 2026-11-16 · **Procesado:** 2026-11-16 · **Agente:** Norma, versión 0.1.0 · **Comando:** `profile-language`

## Lo que hay que atender

| # | Señal | Qué | Cita |
|---|---|---|---|
| 1 | `requirement_not_allowed` | PT-01 · Cajero de tienda: el requisito R3 «Buena presencia» pide apariencia, que no se puede pedir según la política de selección de la organización | `10-perfiles/PT-01_cajero-de-tienda.docx` |
| 2 | `requirement_not_allowed` | PT-03 · Supervisor de tienda: el requisito R4 «Profesar la religión católica» pide la religión o las convicciones, que no se puede pedir según Ley Federal de Protección de Datos Personales en Posesión de los Particulares, art. 2, fr. VI (F-11) | `10-perfiles/PT-03_supervisor-de-tienda.docx` |
| 3 | `requirement_not_allowed` | PT-04 · Almacenista: el requisito R2 «Mujer entre 20 y 30 años» pide edad, que no se puede pedir según la política de selección de la organización | `10-perfiles/PT-04_almacenista.docx` |
| 4 | `requirement_not_allowed` | PT-04 · Almacenista: el requisito R2 «Mujer entre 20 y 30 años» pide sexo, que no se puede pedir según la política de selección de la organización | `10-perfiles/PT-04_almacenista.docx` |

## El resultado

| Perfil | Requisitos que piden algo que no se puede pedir |
|---|---|
| PT-01 · Cajero de tienda | R3 |
| PT-02 · Cajero de autoservicio | — |
| PT-03 · Supervisor de tienda | R4 |
| PT-04 · Almacenista | R2, R2 |

**Lo que no se puede pedir:** origen racial o étnico, salud, datos genéticos, religión o convicciones, opinión o afiliación política, vida u orientación sexual (Ley Federal de Protección de Datos Personales en Posesión de los Particulares, art. 2, fr. VI, F-11); y, según la política de la organización, edad, sexo, estado civil, fotografía y apariencia.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- Umbral de importancia de O*NET (`standard.importance_threshold`): ningún documento lo fija. Se tomó 3.0, propuesta del agente, como respuesta sugerida de la prueba.
- Equivalencia de los estudios con la CINE (`education.levels`): Secundaria = 2, Licenciatura = 6. Con O*NET la señal de estudios no se calcula.
- PT-04 Almacenista no trae código de ocupación: queda vacío y no se registra uno sin el sí de una persona.

## Fuentes

- `10-perfiles/PT-01_cajero-de-tienda.docx`
- `10-perfiles/PT-03_supervisor-de-tienda.docx`
- `10-perfiles/PT-04_almacenista.docx`
- Fuentes técnicas: F-11 (`families/criterio-chro/FUENTES.es.md`)

Los términos (versión 1.6) estaban vigentes. No volví a registrar la aceptación de José Francisco Ñáñez porque el motor ya la daba por vigente. La corrida quedó registrada como `2026-11-16-profile-language-1`.