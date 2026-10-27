# criterio-ea · las rondas con el agente

<!-- generado por tests/ronda_familia.py resumen desde cada calificacion.json y defectos.json; no se edita a mano -->

Cada fila es una entidad del material corrida por los agentes con `tests/ronda_familia.py`, con un tope de tokens fijado antes de empezar. Las señales se comparan por su nombre y su clave contra la clave que el agente no ve; la extracción, campo por campo contra lo que traen los documentos escritos. En `repetidas/` están las corridas que se repitieron después de corregir un defecto, con su costo.

| Ronda | Carpeta | Material | Agentes | Señales | Extracción | Tokens |
|---|---|---|---|---|---|---|
| ronda-1 | [banca](ronda-1/banca/) | banca · CO | ofelia | 10 de 10 · 0 de más | 17 de 17 | 1.43 M + 1.20 M repetidos |
| ronda-1 | [control-co](ronda-1/control-co/) | control · CO | ofelia | 0 de 0 · 1 de más | 21 de 22 | 1.25 M |
| ronda-1 | [control-co-ofelia](ronda-1/control-co-ofelia/) | control · CO | ofelia | 0 de 0 · 0 de más | 21 de 22 | 1.51 M |
| ronda-1 | [control-co-ofelia-2](ronda-1/control-co-ofelia-2/) | control · CO | ofelia | 0 de 0 · 0 de más | 22 de 22 | 2.08 M |
| ronda-1 | [control-ec](ronda-1/control-ec/) | control · EC | ofelia | 0 de 0 · 0 de más | 22 de 22 | 1.48 M |
| ronda-1 | [cooperativas](ronda-1/cooperativas/) | cooperativas · EC | ofelia | 4 de 4 · 0 de más | 16 de 17 | 1.67 M |
| ronda-1 | [cooperativas-ofelia](ronda-1/cooperativas-ofelia/) | cooperativas · EC | ofelia | 4 de 4 · 0 de más | 17 de 17 | 1.84 M |

## Los defectos que encontraron

Cada uno con su origen y el commit que lo corrige, desde `defectos.json`. Se da por verificado solo cuando una corrida posterior a la corrección da lo esperado.

| Id | Ronda | Carpeta | Origen | Qué pasó | Corrección | Commit | Estado |
|---|---|---|---|---|---|---|---|
| EA-1 | 1 | banca | el código | El setup se detuvo: el motor exigía la identificación fiscal de la entidad, y ningún documento de la oficina la trae. Ofelia no la inventó y dejó la configuración sin validar. | La oficina se identifica por su ejecutivo: el motor ya no pide la identificación fiscal y el encabezado del reporte no la muestra si falta. Los dos comandos se repitieron en banca: 10 de 10 señales y 17 de 17 datos. | d11470ea | corregido y verificado |
| EA-2 | 1 | banca | el código | El inventario marcó la agenda .ics como «formato no soportado», aunque el motor de Ofelia la procesa. | El inventario toma como legibles los formatos que la estructura de la familia declara como suyos por su extensión. Verificado en la repetición de banca. | d11470ea | corregido y verificado |
| EA-3 | 1 | banca | las instrucciones del agente | Las citas de los acuerdos y los compromisos nombraban la sección y no el renglón: «Compromisos, primer punto». | Las skills dicen que cada cita señala un renglón —`línea N` o `punto N`— y que el texto citado entre « » la acompaña, no la reemplaza. Verificado en la repetición de banca. | d11470ea | corregido y verificado |
| EA-4 | 1 | banca | la clave de respuestas | La clave contradecía dos skills: citaba la decisión en el acta que la aplaza, cuando decision-brief la cita donde la escribe el material, y daba por rutinario pedir una reunión con el ejecutivo, cuando correspondence-record solo da por rutinaria una cita ya aprobada. | La clave sigue ahora a las skills. Ofelia había hecho las dos cosas bien. | d11470ea | corregido y verificado |
| EA-5 | 1 | banca | el arnés de prueba | El arnés no reconocía como la misma cita una que nombra la sección antes del punto —«Acuerdos, punto 1»— ni una que cita el texto del renglón entre « ». | `tests/ronda_familia.py` resuelve el renglón por «línea N», por «punto N» aunque venga tras la sección, o por el texto citado, y lo aplica también a la cita del plazo. | d11470ea | corregido y verificado |
| EA-6 | 1 | cooperativas | las instrucciones del agente | Las citas de los acuerdos llevaban delante la carpeta de la oficina —`direccion/gerencia-general/organos/…`—, así que no se abrían desde la oficina. | La skill dice que cada cita va relativa a la carpeta de la oficina, y el motor dice como problema de la ficha una cita que no está ahí, para que se corrija antes de calcular. Ofelia se corrió de nuevo sobre la cooperativa: 17 de 17 datos. | d11470ea | corregido y verificado |
| EA-7 | 1 | control-co | las instrucciones del agente | En el control de Colombia, Ofelia dejó abierto un compromiso cuyo cumplimiento estaba en el material de la sesión, y el motor levantó un compromiso vencido que no lo era. | La skill de la ficha dice que, antes de dejar abierto un compromiso vencido, se busca su evidencia en el material de las sesiones del órgano, y `ea-scan` lo repite. Ofelia se corrió de nuevo sobre el control de Colombia: ninguna señal de más y el compromiso, cumplido con su evidencia. | d11470ea | corregido y verificado |
| EA-8 | 1 | control-co-ofelia | las instrucciones del agente | En la corrida que verificó EA-7, Ofelia agregó a lo que falta saber de una decisión un hecho que el acta ya dice: que se decide en la próxima sesión. | La skill de la decisión dice que en `missing` va solo lo que el material no responde, no lo que los documentos ya dicen. Ofelia se corrió de nuevo sobre el control de Colombia: ninguna señal de más y 22 de 22 datos. | d11470ea | corregido y verificado |
