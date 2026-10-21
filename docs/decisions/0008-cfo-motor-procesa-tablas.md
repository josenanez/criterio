# 0008 · En la familia CFO, el motor procesa las tablas y las facturas; el agente extrae lo escrito

**Fecha:** 2026-10-20 · **Estado:** aceptada

## Contexto

En la familia PMO casi todo lo que importa llega en texto: actas, minutas, informes de avance.
El agente lo extrae a la ficha y el código calcula sobre la ficha. En la función financiera la
mayoría de los documentos son tablas —balance, mayor, auxiliares, extractos, presupuesto,
compromisos— y XML con una estructura oficial. Pasarlos por la extracción del modelo agregaría
un paso que puede equivocarse donde no hace falta ninguno.

## Decisión

**El motor (`finanzas.py`) procesa directamente las tablas en CSV o Excel y las facturas
electrónicas de la DIAN y del SRI**, cada dato con su archivo y su fila como cita. **El agente
extrae a la ficha solo lo que únicamente trae un documento escrito**: el estado que alguien
declara, las actas de aprobación y de traslado, lo que un área dice de su presupuesto, un
requerimiento que llegó por correo.

Dos archivos por periodo, un escritor cada uno: `ficha.json` la escribe el agente y
`resultados.json` el motor. Los reportes los escribe el motor en el formato común, y el agente
los muestra tal cual.

Las columnas de cada exportación se reconocen por su nombre y sus variantes; la que no se
reconoce se pregunta y queda en la configuración. Cada campo de factura que se procesa cita su
identificador en la fuente oficial (`families/criterio-cfo/fuentes.json`), y una puerta falla si
el motor usa uno que no está verificado.

## Alternativas descartadas

**Que el agente extraiga también las tablas, como en la PMO.** Un balance de quinientas filas
transcrito por el modelo es una fuente de error y de costo sin ganancia: el código lo lee
exacto.

**Un formato de exportación por ERP.** Ata el producto a una lista de sistemas; la detección por
nombre de columna, con la configuración para lo que no se detecta, sirve a cualquiera.

## Consecuencias

- El motor es determinista y se prueba sin el modelo: `tests/criterio-cfo/evaluar.py` lo corre
  sobre el material sintético con la extracción correcta y compara cada señal contra la clave.
- La extracción del agente se prueba aparte, en la ronda, sobre el mismo material.
- Un ERP con columnas que no se detectan se resuelve con una pregunta, no con código nuevo.
