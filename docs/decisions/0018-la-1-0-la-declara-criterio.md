# 0018 · La 1.0 de cada familia la declara Criterio

**Fecha:** 2026-10-28 · **Estado:** reemplazada el 2026-10-28 por la [0020](0020-laboratorio-estable-y-diez-versiones.md) · **Modifica:** la hoja de ruta de cada familia y 0017

> **Reemplazada.** La 1.0 ya no es «la versión estable»: si una versión es estable o de laboratorio lo
> dice su evidencia, con el piso del margen del 95 %, y cada número entero tiene diez versiones
> (decisión 0020). Se conserva como se escribió.

## Contexto

Hasta hoy, la hoja de ruta de cada familia reservaba la versión 1.0 para «el despliegue en una
organización»: el primer uso sobre la documentación de una empresa concreta. Eso dejaba la 1.0 en
manos de un tercero —que alguien la desplegara— y no de lo que Criterio prueba.

Criterio es un proyecto autónomo: desarrolla, prueba y libera. Quien quiera la instala, la prueba
sobre sus documentos y comparte lo que encuentra; eso mejora los incrementos siguientes, pero no es
una condición para que una familia sea estable.

## Decisión

**La 1.0 de una familia es su versión estable, y la declara Criterio** cuando la familia cumple las
tres condiciones, todas verificables en el repositorio:

1. **Su alcance planeado está liberado.** Cada incremento que su hoja de ruta pone antes de la 1.0
   tiene su versión liberada.
2. **Dos rondas completas seguidas sin defectos nuevos.** Sus agentes corren todos sus comandos sobre
   todo su material en dos rondas consecutivas, sin un defecto nuevo de código ni de instrucciones,
   sin señales de más en las entidades de control, y con el piso del margen de confianza del 95 % en
   95 % o más para las señales encontradas y para los datos extraídos.
3. **El esquema de la ficha queda fijo.** Desde la 1.0, un cambio que rompa el esquema de la ficha es
   una versión 2.0.

La primera liberación de cada familia sigue siendo su versión de laboratorio: probada sobre
material sintético y lista para usar. La 1.0 no cambia eso; dice que la familia cerró su alcance
planeado y que su prueba se sostuvo dos veces seguidas.

**El uso en una organización es una invitación, no una puerta.** Quien despliegue una familia sobre
sus documentos y comparta lo que encontró abre un issue; lo que traiga entra en un incremento con su
prueba, como cualquier otro cambio.

## Consecuencias

- El incremento reservado de cada hoja de ruta pasa a ser la 1.0.0, «La versión estable», con las
  tres condiciones.
- Las preguntas frecuentes, la evidencia y el análisis estadístico dejan de decir que la 1.0 depende
  de una organización.
- Cada familia llega a su 1.0 por su cuenta (decisión 0017).
