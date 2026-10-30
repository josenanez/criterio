# criterio-ciso · las rondas con el agente

<!-- generado por tests/ronda_familia.py resumen desde cada calificacion.json y defectos.json; no se edita a mano -->

Cada fila es una entidad del material corrida por los agentes con `tests/ronda_familia.py`, con un tope de tokens fijado antes de empezar. Las señales se comparan por su nombre y su clave contra la clave que el agente no ve; la extracción, campo por campo contra lo que traen los documentos escritos. En `repetidas/` están las corridas que se repitieron después de corregir un defecto, con su costo.

| Ronda | Carpeta | Material | Agentes | Señales | Extracción | Tokens |
|---|---|---|---|---|---|---|
| ronda-1 | [banca-co](ronda-1/banca-co/) | banca · CO | alexis, amparo, guillermo | 25 de 25 · 0 de más | 8 de 8 | 5.28 M |
| ronda-1 | [control-co](ronda-1/control-co/) | control · CO | alexis, amparo, guillermo | 0 de 0 · 0 de más | 8 de 8 | 5.31 M |
| ronda-1 | [control-mx](ronda-1/control-mx/) | control · MX | alexis, amparo, guillermo | 0 de 0 · 0 de más | 8 de 8 | 5.19 M |
| ronda-1 | [retail-mx](ronda-1/retail-mx/) | retail · MX | alexis, amparo, guillermo | 25 de 25 · 0 de más | 8 de 8 | 5.09 M |
| ronda-1 | [salud-pe](ronda-1/salud-pe/) | salud · PE | alexis, amparo, guillermo | 25 de 25 · 0 de más | 8 de 8 | 6.05 M |
| ronda-1 | [tecnologia-cl](ronda-1/tecnologia-cl/) | tecnologia · CL | alexis, amparo, guillermo | 25 de 25 · 0 de más | 8 de 8 | 5.01 M |

## Los defectos que encontraron

Cada uno con su origen y el commit que lo corrige, desde `defectos.json`. Se da por verificado solo cuando una corrida posterior a la corrección da lo esperado.

| Id | Ronda | Carpeta | Origen | Qué pasó | Corrección | Commit | Estado |
|---|---|---|---|---|---|---|---|
| CISO-1 | 1 | banca-co | el arnés de prueba | La clave esperaba en la ficha de Amparo la lista de lo revisado vacía, y Amparo no escribió el campo porque no revisó nada que descartar. El arnés lo calificó como mal, aunque las dos formas dicen lo mismo. | El arnés da por buena una lista que la clave espera vacía cuando la ficha no la trae. Se volvió a calificar la corrida de banca de Colombia, sin repetir comandos: 8 de 8 datos. | 2777ad04 | corregido y verificado |
| CISO-2 | 1 | banca-co | el código | Las corridas de Alexis, Guillermo y Amparo no dejaban su página ni su registro en `.criterio/corridas/`: el hook se disparaba, pero el rastro no sabía cuál era el área de los plugins de la CISO, ni de los de la CCO. No cambiaba ninguna señal ni ningún dato; Rostrum no tenía qué mostrar de esas corridas. | El rastro conoce el área y el nombre de los cinco plugins, con su prueba, y la sincronización falla si un plugin con el hook no está en el rastro. La entidad de control de Colombia, armada después de la corrección, dejó sus corridas. | 2777ad04 | corregido y verificado |
| CISO-3 | 1 | control-co | las instrucciones del agente | En las dos entidades de control, Alexis anotó en la lista de lo revisado las credenciales, la llave y el respaldo que el motor excluye. No los abrió —su motivo dice «no se abre»—, pero la lista dejó de ser lo que se miró y se descartó, y el dato se calificó como mal. | El skill de la ficha de Alexis, y el de la de Amparo, dicen que lo que el motor excluye no va a esa lista: ya lo lista `seguridad.py excluidos`, que es lo que cita el reporte. Se repitieron la instalación y el barrido de Alexis en los dos controles: 8 de 8 datos en cada uno. | 3bd3af0e | corregido y verificado |
| CISO-4 | 1 | banca-co | el código | Guillermo lo reportó en su instalación: `convertir` dejó en el caché una copia en texto de un archivo de credenciales que el motor ya había excluido. El agente no la abrió, pero la exclusión de credenciales, llaves y respaldos tiene que valer también para la conversión. | `convertir` recibe del motor de la CISO la lista de excluidos y no abre ni copia ninguno: van al manifiesto como no convertidos, con su motivo. La prueba del motor lo exige. Se verificó con el motor instalado después de la corrección, sobre el control de Colombia: la credencial quedó en el manifiesto como excluida y sin copia. | 21363181 | corregido y verificado |
