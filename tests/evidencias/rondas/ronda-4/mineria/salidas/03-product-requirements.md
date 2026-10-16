# /criterio-product:product-requirements 

El registro de PRD-300 «Monitoreo de flota» tiene 14 requerimientos, y el 100 % de los 11 aceptados sigue sin proyecto que lo construya. Los términos ya estaban vigentes (versión 0.3.10, aceptados por José Francisco Ñáñez el 2026-10-15), así que no los volví a registrar. Registré la corrida con 37 hallazgos y 35 segundos medidos.

**Estado:** 3 propuestos, 11 aceptados, ninguno en construcción, entregado ni descartado. El 81,8 % de los decididos tiene evidencia y el 0 % está trazado a un proyecto.

**En el orden de lectura de product-health:**
1. **Se va a construir y nadie lo pidió:** REQ-4002 (Camilo Beltrán) y REQ-4006 (Óscar Ramírez). Están aceptados sin evidencia y sin criterio de aceptación.
2. **Decidido y nadie lo construye:** los 11 aceptados. El más antiguo, REQ-4006, lleva 186 días.
3. **Sin doliente:** REQ-4000, 4003 y 4011 (aceptados) y REQ-4012 (propuesto).
4. **Sin criterio de aceptación:** REQ-4000, 4002, 4006 y 4011.
5. **Lleva meses sin decidirse:** REQ-4013 (175 días), REQ-4008 (120) y REQ-4012 (80). El umbral es 60 días. Quien decide es el Comité de producto.
6. **Evidencia vieja:** 12 requerimientos se apoyan en la misma entrevista del 2025-08-18, de hace 13 meses. Esa entrevista no nombra ninguno de ellos, así que es una evidencia genérica contada doce veces.

**Decisiones sin respaldo claro:** los 11 aceptados citan el acta del comité del 2026-10-14. Pero esa acta es posterior a las fechas de decisión, que van del 2026-04-12 al 2026-08-27. Las fichas que revisé tampoco dicen quién decidió; solo constan como decididas por el comité.

**En la definición del producto:**
- No hay criterio de éxito.
- El supuesto «El ahorro se sostiene sin inversión adicional» lleva 113 días sin verificar.
- La cifra de 210.767 de volumen mensual no tiene ninguna medición que la contraste.

**Datos de las fichas:** los 14 títulos son solo el código («Requerimiento REQ-40xx»), así que ninguna ficha dice de qué trata su requerimiento.

**Después:** corresponde `/product-trace` para los 11 aceptados sin proyecto. `/product-charter` no aplica todavía, porque ningún requerimiento tiene evidencia propia, criterio y doliente a la vez.

Todo está en `/home/claude/banco/ronda-4/mineria/espacio/estado-producto/PRD-300/corridas/`:
- `salida-product-requirements.md`
- `2026-10-15-product-requirements-1.md`