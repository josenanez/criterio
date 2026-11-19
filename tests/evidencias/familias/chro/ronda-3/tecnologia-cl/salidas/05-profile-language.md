# /criterio-roles:profile-language 

Dos perfiles piden algo que no se puede pedir: TI-02 (R4) y TI-03 (R3). La corrección es de una persona; Norma no reescribe el perfil.

Los términos ya estaban vigentes (versión 1.6, aceptación registrada), así que no hizo falta registrarlos de nuevo. Lo corrí con `--today 2026-11-16`.

# Lo que un perfil no puede pedir · Nube Austral Software Sintética · periodo 2026-11

**Entidad:** Nube Austral Software Sintética (76543210k) · **Fecha de corte:** 2026-11-16 · **Procesado:** 2026-11-16 · **Agente:** Norma, versión 0.1.0 · **Comando:** `profile-language`

## Lo que hay que atender

| # | Señal | Qué | Cita |
|---|---|---|---|
| 1 | `requirement_not_allowed` | TI-02 · Analista de soporte: el requisito R4 «Nivel socioeconómico medio alto» pide la situación socioeconómica, que no se puede pedir según Ley 19.628, modificada por la Ley 21.719, art. 2, letra g) (F-13) | `10-perfiles/TI-02_analista-de-soporte.docx` |
| 2 | `requirement_not_allowed` | TI-03 · Analista de seguridad: el requisito R3 «No pertenecer a ningún sindicato» pide la afiliación sindical, que no se puede pedir según Ley 19.628, modificada por la Ley 21.719, art. 2, letra g) (F-13) | `10-perfiles/TI-03_analista-de-seguridad.docx` |

## El resultado

**Lo que no se puede pedir** (Ley 19.628, modificada por la Ley 21.719, art. 2, letra g) (F-13)):
origen racial o étnico, opinión o afiliación política, afiliación sindical, situación socioeconómica, religión o convicciones, salud, datos biométricos, datos genéticos, vida u orientación sexual e identidad de género.
**Por la política de selección de la organización:** edad, sexo, estado civil y fotografía.

| Perfil | Requisitos que piden algo que no se puede pedir |
|---|---|
| TI-01 · Desarrollador de software | — |
| TI-02 · Analista de soporte | R4 |
| TI-03 · Analista de seguridad | R3 |
| TI-04 · Desarrollador backend | — |
| TI-05 · Líder técnico | — |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Desde qué importancia de O*NET una destreza es exigible? → 3, propuesta de Norma; la política de selección no lo fija.
- ¿Qué nivel de la CINE corresponde a cada forma de nombrar los estudios? → Técnico = 5, Ingeniería = 6, propuesta desde los perfiles.

## Fuentes

- `10-perfiles/TI-02_analista-de-soporte.docx`
- `10-perfiles/TI-03_analista-de-seguridad.docx`
- Fuentes técnicas: F-13 (families/criterio-chro/FUENTES.es.md)

El reporte completo está en `perfiles/2026-11/reporte-profile-language.md`, dentro de la carpeta de estado. Lo que te mostré quedó en `corridas/salida-profile-language.md`, y el motor registró la corrida como `2026-11-16-profile-language-1`.

Por la instrucción de sesión sin interfaz, tomé las respuestas sugeridas a las dos preguntas del motor sin consultarlas. La importancia 3 de O*NET y los niveles CINE son propuestas de Norma, no valores fijados por la política.