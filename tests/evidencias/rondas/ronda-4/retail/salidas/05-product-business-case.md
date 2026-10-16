# /criterio-product:product-business-case 

Armé el borrador del caso de negocio de PRD-300 (Venta en línea). Hoy es una propuesta, no un caso evaluable: no tiene costo de construir, ni criterio de éxito, ni una cifra con respaldo.

Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-15), así que no registré nada nuevo.

- **Cifras:** hay una sola, `volumen_mensual` = 228.369. La clasifiqué como declarada: ninguna serie la mide, no trae unidad, y la única fuente es el propio caso de negocio. La definición dice que Empresas hoy no tiene venta en línea, y nada explica de dónde sale un volumen mensual para algo que no existe.
- **Retorno:** solo dice «24 meses», sin monto. No calculé retorno ni recuperación, y no rellené nada con valores de referencia.
- **Costos:** no hay ningún costo escrito en los documentos. Es el primer vacío.
- **Requerimientos:**
  - Entran 13 aceptados; los 3 propuestos (REQ-4002, 4003 y 4005) quedan fuera.
  - 2 no tienen doliente (REQ-4004 y REQ-4009).
  - 4 no tienen criterio de aceptación.
  - 2 no tienen evidencia de demanda (REQ-4008 y REQ-4011).
  - Toda la evidencia es una frase de un solo cliente, del 2025-11-24.
- **Supuestos:** el proveedor lleva 86 días sin verificar (umbral 30), y sin proveedor no hay venta en línea. Los otros dos son implícitos: que se alcance el volumen y que haya demanda en Empresas.
- **Cómo se sabrá si funcionó:** no está declarado.
- **Otros productos:** no hay fichas publicadas (la carpeta `estado/` está vacía), así que no pude hacer el cruce de `/product-overlap`. Los casos de PRD-299 a PRD-309 traen `volumen_mensual`, pero ninguno repite 228.369. Eso no descarta que se cuenten las mismas transacciones.

Corregí un número del archivo ya guardado: decía que 5 requerimientos aceptados no tenían criterio de aceptación y son 4. La corrida quedó registrada con 25 hallazgos y 42 segundos medidos, antes de esa corrección.

Ofrezco pasar los tres supuestos a seguimiento (`assumption-tracking`), empezando por el del proveedor. `/product-charter` queda para cuando haya costo, criterio de éxito y autoridad confirmada.

El texto completo está en `/home/claude/banco/ronda-4/retail/espacio/estado-producto/PRD-300/corridas/salida-product-business-case.md`. La corrida quedó registrada como `2026-10-15-product-business-case-1`.