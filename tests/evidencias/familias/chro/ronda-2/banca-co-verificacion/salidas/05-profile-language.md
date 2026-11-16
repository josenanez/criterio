# /criterio-roles:profile-language 

Cuatro requisitos de tres perfiles piden algo que la política de selección o la Ley 1581 no permiten pedir. La corrección es de una persona.

# Lo que un perfil no puede pedir · Banco Cordillera Sintético · periodo 2026-11

**Entidad:** Banco Cordillera Sintético (901555123) · **Fecha de corte:** 2026-11-16 · **Procesado:** 2026-11-16 · **Agente:** Norma, versión 0.1.0 · **Comando:** `profile-language`

## Lo que hay que atender

| # | Señal | Qué | Cita |
|---|---|---|---|
| 1 | `requirement_not_allowed` | PC-02 · Contador de impuestos: el requisito R5 «Hombre menor de 35 años» pide **edad**, que la política de selección no permite pedir | `10-perfiles/PC-02_contador-de-impuestos.docx` |
| 2 | `requirement_not_allowed` | PC-02 · Contador de impuestos: el requisito R5 «Hombre menor de 35 años» pide **sexo**, que la política de selección no permite pedir | `10-perfiles/PC-02_contador-de-impuestos.docx` |
| 3 | `requirement_not_allowed` | PC-04 · Analista de crédito: el requisito R4 «Gozar de buen estado de salud» pide **la salud**, que no se puede pedir según Ley 1581 de 2012, art. 5 (F-10) | `10-perfiles/PC-04_analista-de-credito.docx` |
| 4 | `requirement_not_allowed` | PC-06 · Coordinador de cobranzas: el requisito R2 «Estado civil casado» pide **estado civil**, que la política de selección no permite pedir | `10-perfiles/PC-06_coordinador-de-cobranzas.docx` |

## El resultado

**Lo que no se puede pedir:**

- Según la Ley 1581 de 2012, art. 5 (F-10):
  - el origen racial o étnico
  - la opinión o la afiliación política
  - la religión o las convicciones
  - la afiliación sindical
  - la salud
  - la vida o la orientación sexual
  - los datos biométricos
- Según la política de selección de la organización: edad, sexo, estado civil y fotografía.

| Perfil | Requisitos que piden algo que no se puede pedir |
|---|---|
| PC-01 · Contador | — |
| PC-02 · Contador de impuestos | R5, R5 |
| PC-03 · Auxiliar contable | — |
| PC-04 · Analista de crédito | R4 |
| PC-05 · Cajero | — |
| PC-06 · Coordinador de cobranzas | R2 |
| PC-07 · Director financiero | — |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- Entidad, identificación fiscal y país: Banco Cordillera Sintético · 901555123 · CO (tomada de la carpeta y de la política).
- Periodo: 2026-11.
- Estándar de ocupaciones: CUOC · `00-referencia/estandar/PerfilesOcupacionales-Excel-CUOC-2026-sintetico.xlsx`.
- Equivalencia de estudios con la CINE: Bachiller 3 · Tecnólogo 5 · Profesional 6 (propuesta desde los perfiles).
- Cada cuántos meses se revisa un perfil: 12 (`00-referencia/politica-de-seleccion.pdf`, Plazos).
- Lo que la política prohíbe pedir: edad, sexo, estado civil, fotografía (`00-referencia/politica-de-seleccion.pdf`, Lo que no se pide).
- Dónde se guarda el estado: `estado-talento/901555123-banco-cordillera-sintetico`.
- Términos: aceptados por José Francisco Ñáñez, 2026-11-16.
- Marca `_CRITERIO_TALENTO.txt`: sin marca, porque no hubo un sí explícito.

## Fuentes

- `10-perfiles/PC-02_contador-de-impuestos.docx`
- `10-perfiles/PC-04_analista-de-credito.docx`
- `10-perfiles/PC-06_coordinador-de-cobranzas.docx`
- Fuentes técnicas: F-10 (`families/criterio-chro/FUENTES.es.md`)

---

**Corrida registrada:** `2026-11-16-profile-language-1`, con 14 hallazgos según el motor. La salida quedó en `estado-talento/901555123-banco-cordillera-sintetico/corridas/salida-profile-language.md`.

**Lo que ajusté al mostrar el reporte.** Reordené la lista de lo que no se puede pedir para agrupar cada fuente, y quité de la tabla de señales las columnas que venían vacías (Monto, Responsable, Días). Los hallazgos son los mismos. El archivo con el reporte tal como lo escribió el motor está en `perfiles/2026-11/reporte-profile-language.md`, en la misma carpeta de estado.

**Lo que no pude hacer.** Los términos ya estaban vigentes (versión 1.5), así que no hizo falta registrar la aceptación de nuevo. La salida de la corrida que guardé lleva la línea inicial y el reporte tal como lo escribió el motor, no esta versión reordenada.