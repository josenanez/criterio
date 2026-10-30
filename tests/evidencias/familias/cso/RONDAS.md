# criterio-cso · las rondas con el agente

<!-- generado por tests/ronda_familia.py resumen desde cada calificacion.json y defectos.json; no se edita a mano -->

Cada fila es una entidad del material corrida por los agentes con `tests/ronda_familia.py`, con un tope de tokens fijado antes de empezar. Las señales se comparan por su nombre y su clave contra la clave que el agente no ve; la extracción, campo por campo contra lo que traen los documentos escritos. En `repetidas/` están las corridas que se repitieron después de corregir un defecto, con su costo.

| Ronda | Carpeta | Material | Agentes | Señales | Extracción | Tokens |
|---|---|---|---|---|---|---|
| ronda-1 | [control-co](ronda-1/control-co/) | control · CO | augusto, valeria | 0 de 0 · 0 de más | 5 de 5 | 3.19 M |
| ronda-1 | [control-mx](ronda-1/control-mx/) | control · MX | augusto, valeria | 0 de 0 · 2 de más | 5 de 5 | 2.91 M |
| ronda-1 | [control-mx-2](ronda-1/control-mx-2/) | control · MX | augusto, valeria | 0 de 0 · 0 de más | 5 de 5 | 2.90 M |
| ronda-1 | [control-mx-3](ronda-1/control-mx-3/) | control · MX | augusto, valeria | 0 de 0 · 0 de más | 5 de 5 | 2.89 M |
| ronda-1 | [manufactura-mx](ronda-1/manufactura-mx/) | manufactura · MX | augusto, valeria | 20 de 20 · 0 de más | 5 de 5 | 3.08 M |
| ronda-1 | [retail-co](ronda-1/retail-co/) | retail · CO | augusto, valeria | 21 de 21 · 0 de más | 5 de 5 | 2.82 M |
| ronda-1 | [servicios-mx](ronda-1/servicios-mx/) | servicios · MX | augusto, valeria | 15 de 19 · 0 de más | 5 de 5 | 3.21 M |
| ronda-1 | [servicios-mx-2](ronda-1/servicios-mx-2/) | servicios · MX | augusto, valeria | 19 de 19 · 0 de más | 5 de 5 | 3.27 M |
| ronda-1 | [tecnologia-co](ronda-1/tecnologia-co/) | tecnologia · CO | augusto, valeria | 16 de 20 · 0 de más | 5 de 5 | 3.46 M |
| ronda-1 | [tecnologia-co-2](ronda-1/tecnologia-co-2/) | tecnologia · CO | augusto, valeria | 20 de 20 · 0 de más | 5 de 5 | 3.20 M |
| ronda-2 | [control-cl](ronda-2/control-cl/) | control · CL | augusto, valeria | 0 de 0 · 0 de más | 5 de 5 | 2.60 M |
| ronda-2 | [control-ec](ronda-2/control-ec/) | control · EC | augusto, valeria | 0 de 0 · 0 de más | 5 de 5 | 3.06 M |
| ronda-2 | [control-pe](ronda-2/control-pe/) | control · PE | augusto, valeria | 0 de 0 · 1 de más | 5 de 5 | 2.93 M |
| ronda-2 | [control-pe-2](ronda-2/control-pe-2/) | control · PE | augusto, valeria | 0 de 0 · 0 de más | 5 de 5 | 2.88 M |
| ronda-2 | [manufactura-pe](ronda-2/manufactura-pe/) | manufactura · PE | augusto, valeria | 20 de 20 · 0 de más | 5 de 5 | 3.20 M |
| ronda-2 | [retail-cl](ronda-2/retail-cl/) | retail · CL | augusto, valeria | 19 de 19 · 0 de más | 5 de 5 | 3.24 M |
| ronda-2 | [retail-ec](ronda-2/retail-ec/) | retail · EC | augusto, valeria | 18 de 18 · 0 de más | 5 de 5 | 3.23 M |
| ronda-2 | [servicios-pe](ronda-2/servicios-pe/) | servicios · PE | augusto, valeria | 20 de 20 · 0 de más | 5 de 5 | 3.12 M |
| ronda-2 | [tecnologia-cl](ronda-2/tecnologia-cl/) | tecnologia · CL | augusto, valeria | 20 de 20 · 0 de más | 5 de 5 | 3.01 M |
| ronda-2 | [tecnologia-ec](ronda-2/tecnologia-ec/) | tecnologia · EC | augusto, valeria | 20 de 20 · 0 de más | 5 de 5 | 3.14 M |

## Los defectos que encontraron

Cada uno con su origen y el commit que lo corrige, desde `defectos.json`. Se da por verificado solo cuando una corrida posterior a la corrección da lo esperado.

| Id | Ronda | Carpeta | Origen | Qué pasó | Corrección | Commit | Estado |
|---|---|---|---|---|---|---|---|
| CSO-1 | 1 | retail-co | el arnés de prueba | El arnés calificaba la evidencia de la ficha comercial como mal porque Augusto la escribió en otro orden: las diecinueve propuestas y órdenes de compra estaban todas, con su monto, su fecha y su cita. | Una lista de registros de la ficha se califica sin orden: cada registro de la clave contra uno distinto de la ficha. La primera corrida de retail se volvió a calificar con la regla nueva, sin repetir comandos, y las demás entidades se calificaron con ella. | 13b91ad2 | corregido y verificado |
| CSO-2 | 1 | servicios-mx | los datos de prueba | En servicios de México y en tecnología de Colombia, la clave esperaba que una fecha de cierre corrida dos veces se señalara, con un umbral de una vez que ningún documento de la entidad decía. Augusto tomó el umbral de omisión, dos veces, y no levantó las cuatro oportunidades de cada entidad. | Cada entidad trae su política comercial en 00-referencia/ con los dos umbrales que pregunta el setup. Se repitieron la instalación y el procesamiento de los dos agentes en las dos entidades: 19 de 19 y 20 de 20 señales, ninguna de más. | 30197756 | corregido y verificado |
| CSO-3 | 1 | control-mx | el código | En el control de México, con la exportación de HubSpot, la configuración quedó sin la columna de la empresa asociada. Sin ella Valeria no cruzó lo ganado con lo facturado, el plan dio cero y las dos liquidaciones de comisiones salieron como diferencias: dos señales de más en un control. En tecnología de Colombia, con el mismo HubSpot, sí la mapeó. | Primero el motor reconoció la columna por el nombre «Associated Company», y la corrida control-mx-2 salió limpia; pero la fuente de HubSpot (F-05) no fija ese nombre, y se retiró. La corrección que queda está en la configuración: con HubSpot, sin la columna de la empresa asociada la configuración no pasa, y el setup tiene que decir cuál es. Se repitieron la instalación y el procesamiento de los dos agentes en el control de México: Augusto dijo cuál columna trae la empresa asociada y no hubo ninguna señal, como debe ser. | 5aefad59 | corregido y verificado |
| CSO-4 | 2 | control-pe | las instrucciones del agente | En el control de Perú, con la exportación de Zoho, Augusto no mapeó la columna «Last Activity Time». La última actividad no es un campo estándar de Zoho (F-08), así que el motor tomó lo detenido de los cortes: una oportunidad que se gestionaba y no cambió de etapa, monto ni cierre salió como detenida. Fue una señal de más en un control. En Ecuador y en Chile, con el mismo Zoho, tampoco la mapeó, pero ahí esa oportunidad era la detenida sembrada. | Cuando una exportación trae una columna que parece la última actividad y no está mapeada, `exportacion` lo pregunta con la columna que propone. El setup hace esa pregunta y, con un sí, la registra en `crm.columns`. Se repitieron la instalación y el procesamiento de los dos agentes en el control de Perú: Augusto registró «Last Activity Time» como la última actividad y no hubo ninguna señal, como debe ser. | ada6141f | corregido y verificado |
