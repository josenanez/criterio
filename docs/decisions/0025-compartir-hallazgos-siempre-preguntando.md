# 0025 · Compartir hallazgos: un resumen sin datos, que la persona ve completo y abre ella

**Fecha:** 2026-10-30 · **Estado:** aceptada el 2026-10-30 · **Modifica:** el canal de vuelta de quien instala

## Contexto

José Francisco Ñáñez fijó la regla el 17 de octubre: la retroalimentación de quien instala se pide
siempre preguntando —«¿quieres compartir tus hallazgos para mejorar el producto?»— y nada se envía
sin un sí. La primera parte ya está en el repositorio: las plantillas de issue de defecto, de
hallazgo y de propuesta. Desde hoy su lista de familias sale de cada `familia.json`, así que una
familia nueva no se queda fuera.

Lo que falta es la segunda parte: que compartir no exija reconstruir de memoria qué corrió y qué
salió. Cada corrida ya deja su rastro local, escrito por el arnés y no por el modelo
(`.criterio/corridas/<agente>/corridas.json`): el comando, la hora, la duración y las cifras que el
comando midió.

La telemetría automática queda descartada, como se acordó.

## Propuesta

Un comando voluntario por familia, `/criterio-<plugin>:share-findings`, con el mismo motor en todos
los plugins de agente (se sincroniza como `rastro.py`):

1. **El motor arma el resumen desde el rastro local**, y solo con lo que no viene de los documentos:
   - la familia, el plugin y su versión;
   - cada comando corrido, con cuántas veces corrió y su duración mediana;
   - cada señal por su código (`invoice_outside_authorization`, `kev_overdue`…) con cuántas veces
     salió.

   No lleva el nombre de la entidad, la identificación fiscal, montos, fechas de documentos, rutas,
   nombres de archivo ni el texto de ninguna salida. El motor arma el resumen desde una lista
   cerrada de campos; el modelo de lenguaje (LLM) no redacta ni resume nada de él.
2. **La persona lo ve completo** antes de decidir, tal como iría.
3. **Pregunta, siempre:** «¿Quieres compartir este resumen para mejorar el producto?». Sin un sí,
   el comando termina ahí y no guarda nada.
4. **Con un sí, el agente no envía nada.** El motor arma el enlace a la plantilla de hallazgo, con
   la familia y el resumen ya escritos en sus campos. La persona lo abre, agrega lo que quiera con
   sus palabras y decide si lo publica.
5. **Una compuerta del repositorio** corre el motor sobre el material de prueba y falla si el
   resumen trae cualquier valor que esté en una ficha: nombres, identificaciones o cifras.

## Lo que se decidió

1. José Francisco Ñáñez aprobó el comando y su nombre, `share-findings`, el 30 de octubre de 2026.
2. El resumen lleva solo lo que midió el arnés. Lo que la persona quiera contar de Rostrum lo
   escribe ella, con sus palabras, en la plantilla.
