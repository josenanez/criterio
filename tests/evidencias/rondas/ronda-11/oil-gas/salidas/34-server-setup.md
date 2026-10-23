# /criterio-server:server-setup 

El mapa de Rostrum quedó escrito con 3 agentes de la familia pmo: Vera (portafolio), Samuel (PRY-200) y Alba (PRD-302). No dejé ninguno fuera. El comando para levantar el portal es `/criterio-server:server-start`.

- **Términos:** la versión 1.2 quedó aceptada a nombre de José Francisco Ñáñez. Los comprobantes están en `.criterio/terminos/aceptacion-criterio-server-0.8.0-2026-10-23.md` y `.pdf`, y llevan la fecha 2026-10-23, la del sistema, no la 2026-10-22 de la instrucción.
- **Orden del flujo:** guardé el mapa antes de revisar los términos, al revés de lo previsto. `terminos` exige el `config.json` de Rostrum, que solo crea `guardar`.
- **Nombre de la organización:** no pasé `--organizacion`, y no sé si la configuración de la PMO lo trae. Si falta, `guardar` se puede repetir con ese dato.
- **Carpetas sin marca:** las de PRY-200 y PRD-302 siguen sin marca. Se marcan con `/criterio-project:pm-setup` y `/criterio-product:product-setup`.