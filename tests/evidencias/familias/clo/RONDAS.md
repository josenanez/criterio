# criterio-clo · las rondas con el agente

<!-- generado por tests/ronda_familia.py resumen desde cada calificacion.json y defectos.json; no se edita a mano -->

Cada fila es una entidad del material corrida por los agentes con `tests/ronda_familia.py`, con un tope de tokens fijado antes de empezar. Las señales se comparan por su nombre y su clave contra la clave que el agente no ve; la extracción, campo por campo contra lo que traen los documentos escritos. En `repetidas/` están las corridas que se repitieron después de corregir un defecto, con su costo.

| Ronda | Carpeta | Material | Agentes | Señales | Extracción | Tokens |
|---|---|---|---|---|---|---|
| ronda-1 | [banca](ronda-1/banca/) | banca · CO | constanza, fidel | 10 de 10 · 0 de más | 132 de 132 | 7.49 M + 0.39 M repetidos |
| ronda-1 | [control-co](ronda-1/control-co/) | control · CO | constanza, fidel | 0 de 0 · 0 de más | 126 de 132 | 7.91 M + 2.06 M repetidos |
| ronda-1 | [control-co-fidel](ronda-1/control-co-fidel/) | control · CO | fidel | 0 de 0 · 0 de más | 128 de 128 | 3.71 M |

## Los defectos que encontraron

Cada uno con su origen y el commit que lo corrige, desde `defectos.json`. Se da por verificado solo cuando una corrida posterior a la corrección da lo esperado.

| Id | Ronda | Carpeta | Origen | Qué pasó | Corrección | Commit | Estado |
|---|---|---|---|---|---|---|---|
| CLO-1 | 1 | banca | el código | Constanza no tomaba las fichas de Fidel del estado compartido cuando la configuración no las nombraba, y las rutas de las fichas no se resolvían desde la carpeta de .criterio. | Constanza las toma del estado compartido y las rutas se resuelven desde .criterio. El estado del cumplimiento se repitió en banca: 10 de 10 señales. | f80f39f | corregido y verificado |
| CLO-2 | 1 | — | el arnés de prueba | La calificación contaba señales de un periodo distinto del de la clave y las preguntas que el agente escribe de suyo. | La ronda califica solo el periodo de la clave y no las preguntas propias del agente. Se verifica en la ronda 2. | f80f39f | corregido, por verificar |
| CLO-3 | 1 | control-co | el código | Constanza usó la configuración de Fidel: el motor no rechazaba la configuración de otro agente. | El motor rechaza la configuración de otro agente y familias.py comprueba que cada carpeta sea la de familia.json. Los comandos de Constanza se repitieron en el control: ninguna señal de más. | 4df0442 | corregido y verificado |
| CLO-4 | 1 | control-co | las instrucciones del agente | Fidel dejaba fuera de la ficha las obligaciones que vencen al final del contrato, como el informe final o el acta de liquidación: faltó una en cada uno de los cinco contratos. | La skill de la ficha pide todas las obligaciones con fecha, en el orden de sus cláusulas. Fidel se corrió de nuevo sobre el control: 128 de 128 datos. | df6a04b | corregido y verificado |
| CLO-5 | 1 | control-co | el arnés de prueba | La calificación compara la cita como texto: Constanza citó «línea 5» y la clave «punto 1», que son el mismo renglón del boletín. Por eso el control da 126 de 132 y no 127. | Pendiente: que la calificación acepte la cita por línea cuando señala el mismo lugar que la clave. | — | abierto |
