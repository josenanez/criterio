# Gobierno del proyecto

[English](GOVERNANCE.md)

## Quién mantiene qué

| Parte | Responsable |
|---|---|
| El método de los skills y comandos, los esquemas de ficha, los criterios de aceptación | El mantenedor |
| Las posiciones y umbrales de cada organización | Esa organización, en su propia configuración local. No entran a este repositorio. |

**Mantenedor:** José Francisco Ñáñez ([josenanez.com](https://josenanez.com)).

## Modelo de publicación

Criterio construye y publica con un descargo explícito, y quien lo despliegue o lo ejecute acepta los términos. Cada versión pasa una validación interna antes de publicarse —las puertas del código en cada cambio y las rondas de los agentes de cada familia sobre datos de prueba sintéticos —en la PMO, construidos a partir de proyectos reales—— y queda en el registro de versiones; sobre el producto no se dice *certificado*, *verificado* ni *aprobado* (decisión 0003): se dice *probado*, siempre con enlace a su evidencia. La garantía y la responsabilidad se rigen por la licencia Apache 2.0. Ver [TERMS.es.md](TERMS.es.md) y [docs/acceptance.md](docs/acceptance.md).

Lo que sostiene la calidad no es una firma. Es que toda afirmación de una salida cargue el documento de donde salió, que la aritmética viva en código donde se puede probar, y que lo incierto o lo vencido se declare en tiempo de ejecución en vez de maquillarse.

## Verificación, plugin por plugin

Cada plugin se verifica con sus propios criterios. No hay un umbral único para el proyecto, porque leer un portafolio y revisar un contrato fallan de maneras distintas.

Cada plugin lleva, en su propia carpeta:

- Sus criterios de aceptación —qué significa "funciona" para él y qué umbral debe alcanzar—: al final de su `DISENO.es.md` en la familia PMO, y en su `ACCEPTANCE.md` en las familias CFO y CLO, cuyo diseño es de la familia (`families/criterio-<familia>/DISENO.es.md`).
- Material sintético con respuestas conocidas, en `tests/`.
- Un evaluador que califica la corrida contra esas respuestas.

Nada se publica hasta que sus propios criterios pasen, y el resultado se publica con la versión. Un evaluador que solo comprueba que se produjo un informe no es un evaluador: comprueba que se encontró cada hallazgo sembrado y que no se inventó nada.

## Versionado

`MAYOR.MENOR.PARCHE`, **uno por familia** (decisión 0017): la PMO, la CFO, la CLO, la EA y Rostrum llevan cada una su número, el mismo en todos sus plugins, y sube solo cuando ella cambia. El marketplace lleva el número del catálogo, que sube con cada entrada del registro. `scripts/registro.py verificar` hace cumplir que cada plugin esté en la versión que el registro le da a su familia.

- **Parche** — redacción, correcciones, todo lo que no cambia lo que la familia procesa; no cuenta entre las diez versiones.
- **Menor** — cada incremento de la familia: un país, una industria, un skill o un comando nuevo, o comportamiento distinto. **Diez por número entero** (decisión 0020): de x.0 a x.9.
- **Mayor** — el que sigue a la x.9. La 0.10, la 0.11 y la 0.12 son las únicas excepciones, y quien está ahí sube a la 1.0. Un cambio que rompe el esquema de una ficha se declara en la entrada del registro y en las notas de la versión; ya no lo dice el número.

**Laboratorio o estable lo dice la evidencia, no el número** (decisión 0020): una versión es estable si la corrida más reciente de cada entidad de su material tiene el piso del margen del 95 % en 95 % o más, en señales y en datos, y ningún control levanta una señal; si no, sale como laboratorio. Lo calcula `scripts/calidad.py` y el registro lo anota en cada liberación.

**Se publica desde la primera versión y se lanza en una fecha** (decisión 0021): una familia entra al marketplace y al portal con su primera liberación, y se marca «Corre hoy» la semana de su lanzamiento, que dice `lanzamiento` en su `familia.json`. Una familia lanzada sube a la 1.0.0 en su primera versión estable.

Los términos se versionan aparte. Un cambio en `TERMS.md` sube su versión y obliga a aceptar de nuevo en la siguiente corrida.

## Decisiones

Las decisiones de arquitectura se registran en `docs/decisions/` como ADR numerados: contexto, decisión, alternativas descartadas y consecuencias. Una decisión no se revierte en una conversación: se reemplaza con un ADR nuevo.
