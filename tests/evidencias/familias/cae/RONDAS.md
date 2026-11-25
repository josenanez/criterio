# criterio-cae · las rondas con el agente

<!-- generado por tests/ronda_familia.py resumen desde cada calificacion.json y defectos.json; no se edita a mano -->

Cada fila es una entidad del material corrida por los agentes con `tests/ronda_familia.py`, con un tope de tokens fijado antes de empezar. Las señales se comparan por su nombre y su clave contra la clave que el agente no ve; la extracción, campo por campo contra lo que traen los documentos escritos. En `repetidas/` están las corridas que se repitieron después de corregir un defecto, con su costo.

| Ronda | Carpeta | Material | Agentes | Señales | Extracción | Tokens |
|---|---|---|---|---|---|---|
| ronda-1 | [banca-co](ronda-1/banca-co/) | banca · CO | justo, prudencia, remedios | 22 de 25 · 2 de más | 35 de 72 | 11.28 M |

## Los defectos que encontraron

Cada uno con su origen y el commit que lo corrige, desde `defectos.json`. Se da por verificado solo cuando una corrida posterior a la corrección da lo esperado.

| Id | Ronda | Carpeta | Origen | Qué pasó | Corrección | Commit | Estado |
|---|---|---|---|---|---|---|---|
| CAE-1 | 1 | banca-co | los datos de prueba | Los papeles de trabajo traían solo su encabezado: el criterio, la condición, la causa, el efecto, la calificación y la cifra de cada hallazgo estaban en la clave y no en ningún documento, y el informe no decía sus cifras. Justo no registró hallazgos, con razón, y por eso faltaron tres señales y sobraron dos: los hallazgos del informe quedaron sin su papel. | Cada hallazgo se escribe en el papel que la clave cita como su fuente, con cada elemento en su renglón; el que falta no se escribe, y la razón por la que no se identificó la causa, sí. El informe dice la cifra de cada hallazgo. | — | corregido, por verificar |
| CAE-2 | 1 | banca-co | los datos de prueba | La evidencia de implementación y la explicación del atraso no traían su fecha ni su título: la fecha estaba solo en la clave. Remedios dejó la fecha vacía. | Cada evidencia y cada explicación dicen su fecha y su título; la instrucción de Remedios pide los dos, en las palabras del documento. | — | corregido, por verificar |
| CAE-3 | 1 | banca-co | la clave de respuestas | La clave esperaba el título del hallazgo del revisor fiscal acortado, «Horas extra sin aprobación»; el informe dice «horas extra pagadas sin aprobación», y así lo registró Remedios. | La clave toma el título como lo dice el informe. | — | corregido, por verificar |
| CAE-4 | 1 | banca-co | las instrucciones del agente | Las instrucciones de Justo y de Remedios no decían qué va en `reviewed`, y los dos listaron ahí todos los documentos que procesaron, también los citados en otro campo. | Las dos instrucciones dicen que `reviewed` lleva solo los documentos procesados que no traen nada para la ficha, y que un documento citado en otro campo no va ahí. | — | corregido, por verificar |
