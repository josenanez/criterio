# /criterio-server:server-setup 

El mapa de Rostrum quedó escrito en `.criterio/rostrum/config.json`, con la organización "Telecomunicaciones". Tiene 3 entradas de la familia pmo: Vera (portafolio), Samuel (proyecto PRY-211) y Alba (producto PRD-306). No dejé nada fuera. La revisión final no encontró entradas nuevas ni desaparecidas, y todas tienen su estado.

Los términos 1.3 quedaron aceptados a nombre de José Francisco Ñáñez, con fecha 2026-10-28. El comprobante, en Markdown y PDF, está en `.criterio/terminos/aceptacion-criterio-server-0.12.1-2026-10-28.*`.

Cambié el orden de dos pasos. Los términos se guardan dentro de `rostrum/config.json`, que no existía, así que guardé el mapa antes de consultarlos y aceptarlos. Tomé las respuestas sugeridas: la carpeta de la sesión como carpeta de trabajo y ninguna exclusión. Como la configuración de la PMO no traía el nombre de la organización, usé el de la entrada de portafolio.

Para levantar el portal: `/criterio-server:server-start`.