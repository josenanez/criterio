# Criterio PMO · versión 0.5.0 · 19 de octubre de 2026

La versión de lanzamiento de la familia de gobierno de proyectos de Criterio: tres agentes y un servidor que procesan lo que la oficina de proyectos ya escribió, preparan su trabajo y dicen qué cambió, qué se contradice y qué ningún documento sostiene. Código abierto bajo Apache 2.0.

## Qué trae

| | Para quién | Comandos | Qué hace |
|---|---|---:|---|
| **Vera** · `criterio-portfolio` | La PMO | 17 | Una ficha por proyecto con la cita de cada dato, desviaciones y alertas de todo el portafolio, el informe y el material del comité |
| **Samuel** · `criterio-project` | Cada gerente de proyecto | 9 | Los compromisos de cada reunión con su fecha, sus reprogramaciones y si están cumplidos; agenda, acta, informe y la ficha que publica a la PMO |
| **Alba** · `criterio-product` | Cada gerente de producto | 11 | La definición contra la evidencia de demanda, el registro de requerimientos y el acta con la que nace el proyecto |
| **Rostrum** · dentro de `criterio-portfolio` | Quien no abre una carpeta | — | Publica el informe y recibe peticiones; no escribe nunca la ficha |

Los 37 comandos, uno por uno, en el [manual](manual.es.md).

## Lo que está medido

Diez rondas desde el 14 de octubre, sobre datos de prueba de cuatro industrias —entidades financieras (bancos y cooperativas), retail y minería de Suramérica— construidos para ser más exigentes que la documentación habitual de esas organizaciones: más de 500 documentos por ronda en Markdown, Word, PDF, Excel y CSV, contradicciones entre documentos, compromisos movidos hasta seis veces, hitos cumplidos sin acta, proyectos en silencio, entregas de proveedor sin evidencia, y en cada industria un proyecto sano que no debe levantar ninguna alerta. Cada ronda trae material nuevo y una clave que ningún agente ve.

Ronda 10, sobre la versión 0.5.0, el 18 de octubre de 2026: 52 proyectos y los 37 comandos en el orden de una PMO, con los plugins instalados desde cero.

| | Resultado | Margen del 95 % |
|---|---|---|
| Comandos que terminaron y cumplieron su contrato | 148 de 148 | — |
| Vera · alertas correctas de las emitidas | 242 de 242 | 98,4–100 % |
| Vera · alertas encontradas de las que había | 242 de 249 | 90,4–100 % |
| Samuel · compromisos y fecha de cierre correctos | 108 de 108 | 96,6–100 % |
| Alba · alertas encontradas de las que había | 131 de 131 | 97,2–100 % |
| Alba · alertas correctas de las emitidas | 131 de 132 | 95,8–99,9 % |
| Rostrum · comprobaciones de lo que muestra | 2175 de 2175 | 99,8–100 % |

Ninguna alerta falsa de Vera. Las siete que le faltaron son una sola falla, en un proyecto de minería: al configurarse dejó ese proyecto sin compromisos porque estaban en la ficha que publicó su gerente (D059). La alerta de más de Alba tenía razón: los datos de prueba citaban una entrevista que la carpeta no traía (D058). Las dos están corregidas después de la 0.5.0.

60 defectos registrados con su origen, el commit que los corrige y la ronda que los verificó, todos en [`tests/evidencias/`](../tests/evidencias/). Las preguntas frecuentes, en [`families/criterio-pmo/PREGUNTAS.es.md`](../families/criterio-pmo/PREGUNTAS.es.md).

## Lo que sigue

- **El primer uso sobre la documentación de una organización concreta.** Es el paso que decide la versión 1.0, cuando el esquema de la ficha sobreviva a ese uso.
- **Lo que se califica contra una clave:** las alertas de Vera, los compromisos y la fecha de cierre de Samuel y las alertas del producto de Alba. Los demás comandos se revisan en cada corrida contra su contrato —qué deben escribir y qué no—.
- **La redacción del modelo** —actas, informes, síntesis de entrevistas— se verifica en la aritmética de la que salen sus cifras, no con un calificador determinista.
- **La comparación campo por campo de la ficha entera** (`grade.py --fichas` y `--registros`) es la siguiente prueba por agregar a las rondas.

## Antes de usarla

Cada versión se acepta de nuevo: el agente muestra los términos, pide un sí explícito y deja un comprobante en Markdown y PDF con la huella SHA-256 de los términos. Produce borradores de trabajo, no decisiones, y ningún agente escribe el estado declarado de un proyecto.

Instalación: `/plugin marketplace add josenanez/criterio`, o en Claude Cowork, Personalizar → Explorar plugins → Personal → + → `josenanez/criterio`.
