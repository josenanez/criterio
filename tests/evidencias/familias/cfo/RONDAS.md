# criterio-cfo · las rondas con el agente

<!-- generado por tests/ronda_familia.py resumen desde cada calificacion.json y defectos.json; no se edita a mano -->

Cada fila es una entidad del material corrida por los agentes con `tests/ronda_familia.py`, con un tope de tokens fijado antes de empezar. Las señales se comparan por su nombre y su clave contra la clave que el agente no ve; la extracción, campo por campo contra lo que traen los documentos escritos. En `repetidas/` están las corridas que se repitieron después de corregir un defecto, con su costo.

| Ronda | Carpeta | Material | Agentes | Señales | Extracción | Tokens |
|---|---|---|---|---|---|---|
| ronda-1 | [banca](ronda-1/banca/) | banca · CO | clara, tomas | 13 de 13 · 0 de más | 8 de 8 | 8.78 M + 0.82 M repetidos |
| ronda-1 | [control-co](ronda-1/control-co/) | control · CO | clara, tomas | 0 de 0 · 0 de más | 8 de 8 | 8.54 M |
| ronda-2 | [banca](ronda-2/banca/) | banca · CO | clara, tomas | 13 de 13 · 0 de más | 8 de 8 | 8.40 M |
| ronda-2 | [control-co](ronda-2/control-co/) | control · CO | clara, tomas | 0 de 0 · 0 de más | 8 de 8 | 8.39 M |
| ronda-2 | [control-ec](ronda-2/control-ec/) | control · EC | clara, tomas | 0 de 0 · 0 de más | 8 de 8 | 8.52 M |
| ronda-2 | [cooperativas](ronda-2/cooperativas/) | cooperativas · EC | clara, tomas | 11 de 11 · 0 de más | 8 de 8 | 9.17 M |
| ronda-2 | [mineria](ronda-2/mineria/) | mineria · EC | clara, tomas | 11 de 11 · 0 de más | 8 de 9 | 9.70 M |
| ronda-2 | [retail](ronda-2/retail/) | retail · CO | clara, tomas | 10 de 10 · 0 de más | 8 de 8 | 8.82 M |

## Los defectos que encontraron

Cada uno con su origen y el commit que lo corrige, desde `defectos.json`. Se da por verificado solo cuando una corrida posterior a la corrección da lo esperado.

| Id | Ronda | Carpeta | Origen | Qué pasó | Corrección | Commit | Estado |
|---|---|---|---|---|---|---|---|
| CFO-1 | 1 | banca | las instrucciones del agente | Tomás proponía la ruta de las fichas de la PMO sin buscarlas antes, y el motor no avisaba cuando no encontraba ninguna. | Tomás busca las fichas antes de proponer la ruta y el motor dice cuando no hay ninguna. La instalación se repitió en banca y dio lo esperado. | 7ba9570 | corregido y verificado |
| CFO-2 | 1 | banca | el arnés de prueba | La calificación no igualaba una cifra escrita de otra forma y rechazaba un texto correcto con más detalle que la clave. | La calificación iguala las cifras y acepta el texto que contiene lo que pide la clave. Verificado en la ronda 2: 48 de 49 datos en las seis entidades. | 7ba9570 | corregido y verificado |
| CFO-3 | 1 | control-co | el código | Un cambio de carpeta del agente hacía que el motor escribiera el estado y las señales en otra parte: resolvía las rutas desde la sesión y no desde la carpeta de .criterio. | El motor resuelve las rutas desde la carpeta de .criterio y la calificación solo toma el estado que dice la configuración. Verificado en la ronda 2: ninguna señal de más en los dos controles. | 39e892d | corregido y verificado |
| CFO-4 | 2 | mineria | el arnés de prueba | La calificación compara el compromiso del comité como texto: la clave dice «Revisar el contrato de vigilancia» y Tomás escribió «Administración revisa el contrato de vigilancia antes del próximo comité», el mismo compromiso con el mismo responsable y la misma acta. Por eso minería da 8 de 9 y no 9. | Pendiente: decidir cómo la calificación reconoce el mismo compromiso dicho con otras palabras sin volverse permisiva. | — | abierto |
