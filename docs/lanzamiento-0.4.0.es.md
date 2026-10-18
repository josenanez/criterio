# Criterio PMO · versión 0.4.0 · 19 de octubre de 2026

La primera versión pública de la familia de gobierno de proyectos de Criterio: tres agentes y un servidor que procesan lo que la oficina de proyectos ya escribió, preparan su trabajo y dicen qué cambió, qué se contradice y qué ningún documento sostiene. Código abierto bajo Apache 2.0.

## Qué trae

| | Para quién | Comandos | Qué hace |
|---|---|---:|---|
| **Vera** · `criterio-portfolio` | La PMO | 17 | Una ficha por proyecto con la cita de cada dato, desviaciones y alertas de todo el portafolio, el informe y el material del comité |
| **Samuel** · `criterio-project` | Cada gerente de proyecto | 9 | Los compromisos de cada reunión con su fecha, sus reprogramaciones y si están cumplidos; agenda, acta, informe y la ficha que publica a la PMO |
| **Alba** · `criterio-product` | Cada gerente de producto | 11 | La definición contra la evidencia de demanda, el registro de requerimientos y el acta con la que nace el proyecto |
| **Rostrum** · dentro de `criterio-portfolio` | Quien no abre una carpeta | — | Publica el informe y recibe peticiones; no escribe nunca la ficha |

Los 37 comandos, uno por uno, en el [manual](manual.es.md).

## Lo que está medido

Ronda 9, sobre la versión 0.4.0, el 17 de octubre de 2026: cuatro industrias —entidades financieras (bancos y cooperativas), retail y minería de Suramérica—, 52 proyectos, los 37 comandos en el orden de una PMO, con los plugins instalados desde cero y una clave que ningún agente ve.

| | Resultado | Margen del 95 % |
|---|---|---|
| Comandos que terminaron y cumplieron su contrato | 148 de 148 | — |
| Vera · alertas encontradas de las que había | 266 de 266 | 98,6–100 % |
| Vera · alertas correctas de las emitidas | 266 de 267 | 97,9–99,9 % |
| Samuel · compromisos y fecha de cierre correctos | 108 de 108 | 96,6–100 % |
| Alba · alertas de su producto, encontradas y correctas | 128 de 128 | 97,1–100 % |
| Rostrum · comprobaciones de lo que muestra | 2170 de 2170 | 99,8–100 % |

La alerta de más de Vera es un defecto de código que encontró esta misma ronda: cuando el gerente escribe «No aplica» como producto, el contraste entre las dos fichas lo leía como un producto (D056, corregido después de la 0.4.0).

Nueve rondas desde el 14 de octubre, 57 defectos registrados con su origen, el commit que los corrige y la ronda que los verificó. Todo publicado en [`tests/evidencias/`](../tests/evidencias/).

## Lo que todavía no se sabe

- **Nada se ha corrido sobre la documentación real de una organización.** Los datos de prueba los escribe el repositorio.
- **Cada industria tiene una docena de proyectos:** los márgenes son anchos, y así se publican.
- **Contra una clave se califican** las alertas de Vera, los compromisos y la fecha de cierre de Samuel y las alertas del producto de Alba. Los demás comandos se revisan contra su contrato —qué deben escribir y qué no—, no contra una clave.
- **La redacción del modelo** —actas, informes, síntesis de entrevistas— no la mide un calificador determinista.
- **La comparación campo por campo de la ficha entera** (`grade.py --fichas` y `--registros`) todavía no se ha ejecutado sobre lo que producen las rondas.

## Antes de usarla

Cada versión se acepta de nuevo: el agente muestra los términos, pide un sí explícito y deja un comprobante en Markdown y PDF con la huella SHA-256 de los términos. Produce borradores de trabajo, no decisiones, y ningún agente escribe el estado declarado de un proyecto.

Instalación: `/plugin marketplace add josenanez/criterio`, o en Claude Cowork, Personalizar → Explorar plugins → Personal → + → `josenanez/criterio`.
