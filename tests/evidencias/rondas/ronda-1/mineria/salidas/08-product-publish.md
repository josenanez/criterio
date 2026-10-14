# /criterio-product:product-publish 

No publiqué la ficha de PRD-303 (Gemelo digital), porque no hay nada que publicar y tampoco hay dónde hacerlo.

- **Términos:** quedaron aceptados (v1.0, vigente), con la aceptación de José Francisco Ñáñez del 2026-10-14 que ya estaba en la configuración.
- **Estado vacío:** `estado/producto.json` no tiene código, nombre, gerente, segmento ni métricas. `estado/requirements/` y `estado/metrics/` no tienen archivos.
- **Lo que saldría:** el script de publicación daría una ficha con `code: "?"`, sin segmento, métricas, proyectos ni requerimientos. Otros productos la leerían como si fuera de hoy.
- **Sin carpeta de publicados:** `config.json` no define ninguna ruta para la carpeta de productos publicados. Acordarla es una conversación de la organización, así que no la creé ni inventé una.
- **Qué falta:** correr `product-setup` y `product-requirements` (o `product-definition`) para llenar el estado, y acordar la carpeta `publicados/`. Después se repite `/product-publish`.

Dejé registrada la corrida `2026-10-14-product-publish-1`, con 0 hallazgos y 25 segundos. Lo que te mostré está en `estado/corridas/salida-product-publish.md`.