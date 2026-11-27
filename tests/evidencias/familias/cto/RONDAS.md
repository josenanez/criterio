# criterio-cto · las rondas con el agente

<!-- generado por tests/ronda_familia.py resumen desde cada calificacion.json y defectos.json; no se edita a mano -->

Cada fila es una entidad del material corrida por los agentes con `tests/ronda_familia.py`, con un tope de tokens fijado antes de empezar. Las señales se comparan por su nombre y su clave contra la clave que el agente no ve; la extracción, campo por campo contra lo que traen los documentos escritos. En `repetidas/` están las corridas que se repitieron después de corregir un defecto, con su costo.

| Ronda | Carpeta | Material | Agentes | Señales | Extracción | Tokens |
|---|---|---|---|---|---|---|
| ronda-1 | [banca-co](ronda-1/banca-co/) | banca · CO | domingo, fausto | 36 de 36 · 0 de más | 70 de 70 | 7.01 M |
| ronda-1 | [control-co](ronda-1/control-co/) | control · CO | domingo, fausto | 0 de 0 · 0 de más | 33 de 33 | 6.43 M |
| ronda-1 | [control-mx](ronda-1/control-mx/) | control · MX | domingo, fausto | 0 de 0 · 0 de más | 33 de 33 | 6.51 M |
| ronda-1 | [retail-mx](ronda-1/retail-mx/) | retail · MX | domingo, fausto | 36 de 36 · 0 de más | 70 de 70 | 7.33 M |
| ronda-1 | [tecnologia-cl](ronda-1/tecnologia-cl/) | tecnologia · CL | domingo, fausto | 24 de 24 · 0 de más | 61 de 61 | 7.23 M |

## Los defectos que encontraron

Cada uno con su origen y el commit que lo corrige, desde `defectos.json`. Se da por verificado solo cuando una corrida posterior a la corrección da lo esperado.

| Id | Ronda | Carpeta | Origen | Qué pasó | Corrección | Commit | Estado |
|---|---|---|---|---|---|---|---|
| CTO-1 | 1 | control-co | las instrucciones del agente | El acta del comité de cambios decía «el comité lo aprueba», y change-record pedía la autoridad «en las palabras del acta»: Fausto la registró como «el comité» en tres aprobaciones, en lugar de «Comité de cambios». | change-record pide la autoridad por su nombre: si el acta dice «el comité», es el comité del título del acta. El escaneo de cambios, corrido otra vez con la instrucción corregida, da los 33 datos bien. | 7c512b56 | corregido y verificado |
