# /criterio-product:product-spec 

No hay especificación de PRD-300 (Crédito de libranza): el registro de requerimientos está vacío. La carpeta `estado/PRD-300/requirements/` no tiene nada, y `producto.json` no tiene identidad ni definición. El comando solo especifica requerimientos en `aceptado` o `en_construccion`, y no hay ninguno. No inventé requerimientos desde los documentos.

- **Términos:** `terms_accepted` en la configuración es la versión 1.0, igual que `TERMS.md`. Quedó a nombre de José Francisco Ñáñez, con fecha 2026-10-14. No hubo nada que preguntar.
- **Siguiente paso:** correr `/criterio-product:product-setup` y `/criterio-product:product-requirements` para levantar el registro, y que el comité acepte requerimientos. Después se puede volver a correr `/product-spec`.
- **Corrida:** quedó registrada como `2026-10-14-product-spec-1`, con la salida en `estado/PRD-300/corridas/salida-product-spec.md`.
- **Orden de los pasos:** corrí `corrida-inicio` después de leer la configuración, no antes. La medición de 5 segundos cubre solo el final de la corrida.
- **Campo `producto`:** el registro de la corrida muestra `"producto": "?"`. Pasé el código PRD-300 solo en `--caso`.