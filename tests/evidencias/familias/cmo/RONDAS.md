# criterio-cmo · las rondas con el agente

<!-- generado por tests/ronda_familia.py resumen desde cada calificacion.json y defectos.json; no se edita a mano -->

Cada fila es una entidad del material corrida por los agentes con `tests/ronda_familia.py`, con un tope de tokens fijado antes de empezar. Las señales se comparan por su nombre y su clave contra la clave que el agente no ve; la extracción, campo por campo contra lo que traen los documentos escritos. En `repetidas/` están las corridas que se repitieron después de corregir un defecto, con su costo.

| Ronda | Carpeta | Material | Agentes | Señales | Extracción | Tokens |
|---|---|---|---|---|---|---|
| ronda-1 | [banca-pe](ronda-1/banca-pe/) | banca · PE | lucia, prospero | 6 de 6 · 0 de más | 5 de 5 | 6.30 M |
| ronda-1 | [consumo-mx](ronda-1/consumo-mx/) | manufactura · MX | lucia, prospero | 5 de 5 · 0 de más | 5 de 5 | 6.42 M |
| ronda-1 | [control-co](ronda-1/control-co/) | control · CO | lucia, prospero | 0 de 0 · 0 de más | 5 de 5 | 6.72 M |
| ronda-1 | [control-mx](ronda-1/control-mx/) | control · MX | lucia, prospero | 0 de 0 · 0 de más | 5 de 5 | 6.67 M + 7.01 M repetidos |
| ronda-1 | [retail-co](ronda-1/retail-co/) | retail · CO | lucia, prospero | 11 de 11 · 0 de más | 5 de 5 | 6.81 M |
| ronda-2 | [banca-pe](ronda-2/banca-pe/) | banca · PE | lucia, prospero | 33 de 33 · 0 de más | 99 de 99 | 6.68 M |
| ronda-2 | [consumo-mx](ronda-2/consumo-mx/) | manufactura · MX | lucia, prospero | 22 de 22 · 0 de más | 76 de 76 | 6.97 M |
| ronda-2 | [control-co](ronda-2/control-co/) | control · CO | lucia, prospero | 0 de 0 · 0 de más | 53 de 53 | 6.58 M |
| ronda-2 | [control-mx](ronda-2/control-mx/) | control · MX | lucia, prospero | 0 de 0 · 0 de más | 53 de 53 | 7.18 M |
| ronda-2 | [retail-co](ronda-2/retail-co/) | retail · CO | lucia, prospero | 33 de 33 · 0 de más | 99 de 99 | 7.18 M |
| ronda-3 | [seguros-cl](ronda-3/seguros-cl/) | seguros · CL | lucia, prospero | 22 de 22 · 0 de más | 76 de 76 | 6.26 M |

## Los defectos que encontraron

Cada uno con su origen y el commit que lo corrige, desde `defectos.json`. Se da por verificado solo cuando una corrida posterior a la corrección da lo esperado.

| Id | Ronda | Carpeta | Origen | Qué pasó | Corrección | Commit | Estado |
|---|---|---|---|---|---|---|---|
| CMO-1 | 1 | banca-pe | la clave de respuestas | La clave guardaba la fuente de la comparativa con la etiqueta «Fuente:» y el punto final de la pieza. Lucía la llevó a la ficha sin ellos, como lo pide claim-record, y la calificación la contó como mal: el dato estaba bien. | La clave guarda solo la fuente. La misma salida de Lucía, calificada otra vez con la clave corregida, da los cinco datos bien; los controles se corrieron después con la clave corregida. | 46d4a7d0 | corregido y verificado |
| CMO-2 | 1 | control-mx | las instrucciones del agente | Lucía dejó la reseña pagada a la creadora —«mi pedido llegó al día siguiente»— como revisada sin afirmaciones: claim-record decía que una opinión no es una afirmación y no decía nada de los testimonios. En las otras cuatro entidades la llevó a la ficha con su soporte. | claim-record dice que un testimonio que dice un hecho comprobable es una afirmación y va con su soporte; «me encantó» no lo es. El control de México, corrido otra vez, da los cinco datos bien; la primera corrida está en repetidas/. | 95cef028 | corregido y verificado |
