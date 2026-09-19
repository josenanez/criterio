# Gobierno del proyecto

[English](GOVERNANCE.md)

## Quién mantiene qué

| Parte | Responsable |
|---|---|
| El método de los skills y comandos, los esquemas de ficha, los criterios de aceptación | El mantenedor |
| Las posiciones y umbrales de cada organización | Esa organización, en su propia configuración local. No entran a este repositorio. |

**Mantenedor:** José Francisco Ñáñez ([josenanez.com](https://josenanez.com)).

## Modelo de publicación

Criterio construye y publica con un descargo explícito, y quien lo despliegue o lo ejecute acepta los términos. No se afirma certificación alguna, y las palabras *verificado*, *certificado* y *aprobado* no se usan sobre nada de aquí. Ver [TERMS.es.md](TERMS.es.md) y [docs/acceptance.md](docs/acceptance.md).

Lo que sostiene la calidad no es una firma. Es que toda afirmación de una salida cargue el documento de donde salió, que la aritmética viva en código donde se puede probar, y que lo incierto o lo vencido se declare en tiempo de ejecución en vez de maquillarse.

## Verificación, plugin por plugin

Cada plugin se verifica con sus propios criterios. No hay un umbral único para el proyecto, porque leer un portafolio y revisar un contrato fallan de maneras distintas.

Cada plugin lleva, en su propia carpeta:

- `ACCEPTANCE.md` — qué significa "funciona" para él y qué umbral debe alcanzar.
- Material sintético con respuestas conocidas, en `tests/`.
- Un evaluador que califica la corrida contra esas respuestas.

Nada se publica hasta que sus propios criterios pasen, y el resultado se publica con la versión. Un evaluador que solo comprueba que se produjo un informe no es un evaluador: comprueba que se encontró cada hallazgo sembrado y que no se inventó nada.

## Versionado

`MAYOR.MENOR.PARCHE`, compartido entre el marketplace y todos los plugins — no hay versionado independiente por plugin, y el validador lo hace cumplir.

- **Parche** — redacción, todo lo que no cambia la salida.
- **Menor** — un skill o comando nuevo, o comportamiento distinto.
- **Mayor** — cambia el esquema de una ficha, o se reestructura el repositorio.

Los términos se versionan aparte. Un cambio en `TERMS.md` sube su versión y obliga a aceptar de nuevo en la siguiente corrida.

## Decisiones

Las decisiones de arquitectura se registran en `docs/decisions/` como ADR numerados: contexto, decisión, alternativas descartadas y consecuencias. Una decisión no se revierte en una conversación: se reemplaza con un ADR nuevo.
