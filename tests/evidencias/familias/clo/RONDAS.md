# criterio-clo · las rondas con el agente

<!-- generado por tests/ronda_familia.py resumen desde cada calificacion.json y defectos.json; no se edita a mano -->

Cada fila es una entidad del material corrida por los agentes con `tests/ronda_familia.py`, con un tope de tokens fijado antes de empezar. Las señales se comparan por su nombre y su clave contra la clave que el agente no ve; la extracción, campo por campo contra lo que traen los documentos escritos. En `repetidas/` están las corridas que se repitieron después de corregir un defecto, con su costo.

| Ronda | Carpeta | Material | Agentes | Señales | Extracción | Tokens |
|---|---|---|---|---|---|---|
| ronda-1 | [banca](ronda-1/banca/) | banca · CO | constanza, fidel | 10 de 10 · 0 de más | 132 de 132 | 7.49 M + 0.39 M repetidos |
| ronda-1 | [control-co](ronda-1/control-co/) | control · CO | constanza, fidel | 0 de 0 · 0 de más | 126 de 132 | 7.91 M + 2.06 M repetidos |
| ronda-1 | [control-co-fidel](ronda-1/control-co-fidel/) | control · CO | fidel | 0 de 0 · 0 de más | 128 de 128 | 3.71 M |
| ronda-2 | [banca](ronda-2/banca/) | banca · CO | constanza, fidel | 10 de 10 · 0 de más | 131 de 132 | 7.93 M |
| ronda-2 | [control-co](ronda-2/control-co/) | control · CO | constanza, fidel | 0 de 0 · 0 de más | 128 de 132 | 5.30 M |
| ronda-2 | [control-ec](ronda-2/control-ec/) | control · EC | constanza, fidel | 0 de 0 · 0 de más | 134 de 134 | 7.72 M |
| ronda-2 | [cooperativas](ronda-2/cooperativas/) | cooperativas · EC | constanza, fidel | 9 de 9 · 0 de más | 153 de 153 | 7.83 M |
| ronda-2 | [mineria](ronda-2/mineria/) | mineria · EC | constanza, fidel | 9 de 9 · 0 de más | 130 de 132 | 7.72 M |
| ronda-2 | [retail](ronda-2/retail/) | retail · CO | constanza, fidel | 9 de 9 · 0 de más | 132 de 132 | 7.22 M |
| ronda-3 | [control-co-verificacion](ronda-3/control-co-verificacion/) | control · CO | constanza, fidel | 0 de 0 · 0 de más | 131 de 132 | 7.52 M |
| ronda-3 | [mineria-fidel](ronda-3/mineria-fidel/) | mineria · EC | fidel | 4 de 4 · 0 de más | 128 de 128 | 3.47 M |

## Los defectos que encontraron

Cada uno con su origen y el commit que lo corrige, desde `defectos.json`. Se da por verificado solo cuando una corrida posterior a la corrección da lo esperado.

| Id | Ronda | Carpeta | Origen | Qué pasó | Corrección | Commit | Estado |
|---|---|---|---|---|---|---|---|
| CLO-1 | 1 | banca | el código | Constanza no tomaba las fichas de Fidel del estado compartido cuando la configuración no las nombraba, y las rutas de las fichas no se resolvían desde la carpeta de .criterio. | Constanza las toma del estado compartido y las rutas se resuelven desde .criterio. El estado del cumplimiento se repitió en banca: 10 de 10 señales. | f80f39f | corregido y verificado |
| CLO-2 | 1 | — | el arnés de prueba | La calificación contaba señales de un periodo distinto del de la clave y las preguntas que el agente escribe de suyo. | La ronda califica solo el periodo de la clave y no las preguntas propias del agente. Verificado en la ronda 2: ninguna señal de más en las seis entidades. | f80f39f | corregido y verificado |
| CLO-3 | 1 | control-co | el código | Constanza usó la configuración de Fidel: el motor no rechazaba la configuración de otro agente. | El motor rechaza la configuración de otro agente y familias.py comprueba que cada carpeta sea la de familia.json. Verificado en la ronda 2: Constanza trabajó con la suya en cinco entidades. | 4df0442 | corregido y verificado |
| CLO-4 | 1 | control-co | las instrucciones del agente | Fidel dejaba fuera de la ficha las obligaciones que vencen al final del contrato, como el informe final o el acta de liquidación: faltó una en cada uno de los cinco contratos. | La skill de la ficha pide todas las obligaciones con fecha, en el orden de sus cláusulas. Fidel se corrió de nuevo sobre el control: 128 de 128 datos; en la ronda 2, todas las obligaciones de los seis materiales están en las fichas. | df6a04b | corregido y verificado |
| CLO-5 | 1 | control-co | el arnés de prueba | La calificación compara la cita como texto: Constanza citó «línea 5» y la clave «punto 1», que son el mismo renglón del boletín. Por eso el control da 126 de 132 y no 127. | La calificación acepta la cita que señala el mismo renglón del mismo archivo que la clave. Verificado volviendo a calificar la salida original del control de Colombia de la ronda 1 con la calificación corregida: la cita «línea 5» cuenta como bien y el resultado pasa de 126 a 127 de 132. En la ronda 3, Constanza citó «punto 1». | db293b9 | corregido y verificado |
| CLO-6 | 2 | control-co | las instrucciones del agente | En el control de Colombia, Constanza no escribió su configuración: el setup decía «deja la configuración escrita» sin decir que la escribe el agente, y ella paró porque ningún comando del motor la crea. Sin configuración, sus comandos no calcularon nada: los 4 datos de la ficha del periodo faltan, y ese control no prueba sus falsas alarmas en esta ronda. | Los cuatro setup (Clara, Tomás, Fidel y Constanza) dicen que la configuración la escribe el agente con la forma de config.example.json, que init prepara el estado y config la valida. Verificado en la ronda 3: Constanza escribió su configuración en el control de Colombia y su ficha del periodo trae los 4 datos. | f075160 | corregido y verificado |
| CLO-7 | 2 | mineria | la clave de respuestas | La clave de un contrato sin la firma de la contraparte seguía listando a la contraparte como firmante. Fidel, con razón, listó solo a quien firmó. | El generador deja en la clave solo a quien firmó; cambia únicamente la clave de minería. Verificado en la ronda 3: Fidel sobre minería, 128 de 128 datos. | f075160 | corregido y verificado |
| CLO-8 | 2 | mineria | las instrucciones del agente | En ese mismo contrato, Fidel dejó vacía la fecha de firma: la skill no decía qué fecha va cuando solo firmó una parte. | La skill de la ficha dice que la fecha es la de la firma que trae el documento, aunque sea de una sola parte, y que signed_by_both dice que falta la otra. Verificado en la ronda 3: Fidel sobre minería, 128 de 128 datos. | f075160 | corregido y verificado |
| CLO-9 | 2 | banca | el arnés de prueba | El mismo caso que CFO-4: la clave dice «Reporte de operaciones al oficial de cumplimiento» y Fidel escribió «Reporte de operaciones del periodo al oficial de cumplimiento». La calificación lo cuenta como error porque compara el texto contenido, no el sentido. Se repitió en la ronda 3, en el control de Colombia: es el único dato que falló ahí (131 de 132). | Pendiente, junto con CFO-4: decidir cómo la calificación reconoce el mismo dato dicho con otras palabras sin volverse permisiva. | — | abierto |
