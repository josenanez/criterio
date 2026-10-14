# /criterio-product:product-publish 

No publiqué nada. El estado de PRD-300 (Crédito de libranza) está vacío, y una ficha vacía la leería otro gerente como si fuera de hoy.

- **Estado vacío:** `estado/PRD-300/producto.json` no trae código, definición ni gerente. El cálculo devuelve código "?", y `requirements/`, `metrics/` y `snapshots/` no tienen nada. La ficha habría llevado 0 requerimientos, 0 proyectos, 0 métricas y ningún segmento.
- **Sin carpeta de publicados:** la configuración no define ninguna. Acordarla es una conversación de la organización, no algo que yo deba inventar.
- **Términos:** `terms_accepted` ya estaba en la configuración con la versión 1.0, igual que `TERMS.md`, a nombre de José Francisco Ñáñez con fecha 2026-10-14. No hubo que pedir aceptación.

Para poder publicar hay que correr antes `/criterio-product:product-setup` y `/criterio-product:product-requirements` sobre `documentos/productos/PRD-300`, y acordar la carpeta común. Después se repite este comando.

La corrida quedó registrada como `2026-10-14-product-publish-1`, con la salida guardada en `estado/PRD-300/corridas/salida-product-publish.md`.