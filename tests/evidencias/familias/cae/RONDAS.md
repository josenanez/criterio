# criterio-cae · las rondas con el agente

<!-- generado por tests/ronda_familia.py resumen desde cada calificacion.json y defectos.json; no se edita a mano -->

Cada fila es una entidad del material corrida por los agentes con `tests/ronda_familia.py`, con un tope de tokens fijado antes de empezar. Las señales se comparan por su nombre y su clave contra la clave que el agente no ve; la extracción, campo por campo contra lo que traen los documentos escritos. En `repetidas/` están las corridas que se repitieron después de corregir un defecto, con su costo.

| Ronda | Carpeta | Material | Agentes | Señales | Extracción | Tokens |
|---|---|---|---|---|---|---|
| ronda-1 | [banca-co](ronda-1/banca-co/) | banca · CO | justo, prudencia, remedios | 22 de 25 · 2 de más | 35 de 72 | 11.28 M |
| ronda-1 | [control-co](ronda-1/control-co/) | control · CO | justo, prudencia, remedios | 0 de 0 · 0 de más | 68 de 68 | 10.37 M |
| ronda-1 | [control-pe](ronda-1/control-pe/) | control · PE | justo, prudencia, remedios | 0 de 0 · 0 de más | 68 de 68 | 10.91 M |
| ronda-1 | [cooperativa-pe](ronda-1/cooperativa-pe/) | cooperativas · PE | justo, prudencia, remedios | 14 de 14 · 0 de más | 72 de 72 | 11.50 M |
| ronda-1 | [seguros-br](ronda-1/seguros-br/) | seguros · BR | justo, prudencia, remedios | 12 de 12 · 0 de más | 67 de 68 | 11.12 M |
| ronda-2 | [banca-co](ronda-2/banca-co/) | banca · CO | justo, prudencia, remedios | 25 de 25 · 0 de más | 72 de 72 | 10.73 M |
| ronda-2 | [control-co](ronda-2/control-co/) | control · CO | justo, prudencia, remedios | 0 de 0 · 0 de más | 68 de 68 | 11.08 M |
| ronda-2 | [control-pe](ronda-2/control-pe/) | control · PE | justo, prudencia, remedios | 0 de 0 · 0 de más | 68 de 68 | 10.57 M |
| ronda-2 | [cooperativa-pe](ronda-2/cooperativa-pe/) | cooperativas · PE | justo, prudencia, remedios | 26 de 26 · 0 de más | 72 de 72 | 10.42 M |
| ronda-2 | [seguros-br](ronda-2/seguros-br/) | seguros · BR | justo, prudencia, remedios | 25 de 25 · 0 de más | 72 de 72 | 10.77 M |
| ronda-3 | [banca-mx](ronda-3/banca-mx/) | banca · MX | justo, prudencia, remedios | 26 de 26 · 0 de más | 72 de 72 | 10.98 M |

## Los defectos que encontraron

Cada uno con su origen y el commit que lo corrige, desde `defectos.json`. Se da por verificado solo cuando una corrida posterior a la corrección da lo esperado.

| Id | Ronda | Carpeta | Origen | Qué pasó | Corrección | Commit | Estado |
|---|---|---|---|---|---|---|---|
| CAE-1 | 1 | banca-co | los datos de prueba | Los papeles de trabajo traían solo su encabezado: el criterio, la condición, la causa, el efecto, la calificación y la cifra de cada hallazgo estaban en la clave y no en ningún documento, y el informe no decía sus cifras. Justo no registró hallazgos, con razón, y por eso faltaron tres señales y sobraron dos: los hallazgos del informe quedaron sin su papel. | Cada hallazgo se escribe en el papel que la clave cita como su fuente, con cada elemento en su renglón; el que falta no se escribe, y la razón por la que no se identificó la causa, sí. El informe dice la cifra de cada hallazgo. | 4d4b99a1 | corregido y verificado |
| CAE-2 | 1 | banca-co | los datos de prueba | La evidencia de implementación y la explicación del atraso no traían su fecha ni su título: la fecha estaba solo en la clave. Remedios dejó la fecha vacía. | Cada evidencia y cada explicación dicen su fecha y su título; la instrucción de Remedios pide los dos, en las palabras del documento. | 4d4b99a1 | corregido y verificado |
| CAE-3 | 1 | banca-co | la clave de respuestas | La clave esperaba el título del hallazgo del revisor fiscal acortado, «Horas extra sin aprobación»; el informe dice «horas extra pagadas sin aprobación», y así lo registró Remedios. | La clave toma el título como lo dice el informe. | 4d4b99a1 | corregido y verificado |
| CAE-4 | 1 | banca-co | las instrucciones del agente | Las instrucciones de Justo y de Remedios no decían qué va en `reviewed`, y los dos listaron ahí todos los documentos que procesaron, también los citados en otro campo. | Las dos instrucciones dicen que `reviewed` lleva solo los documentos procesados que no traen nada para la ficha, y que un documento citado en otro campo no va ahí. | 4d4b99a1 | corregido y verificado |
| CAE-5 | 1 | seguros-br | las instrucciones del agente | Prudencia listó en `reviewed` las tablas del plan —el universo, la matriz de riesgos y el plan anual—, que procesa el motor y no pasan por la ficha. La instrucción decía «los documentos que se procesaron» sin distinguirlas. | La instrucción de cada uno de los tres agentes nombra las tablas que procesa el motor y dice que no van en `reviewed`. | 24f39616 | corregido y verificado |
