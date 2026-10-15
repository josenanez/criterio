# /criterio-product:product-wake 

## Almacén de repuestos (PRD-306) · 2026-10-15

Esta fue la primera revisión del registro. No había corte anterior, así que las 31 señales abiertas cuentan como nuevas. Desde la próxima corrida solo se reportará lo que cruce un umbral después de hoy.

**Términos:** ya estaban vigentes (v1.1), aceptados por José Francisco Ñáñez el 2026-10-15. No hubo nada que registrar.

### Cruzó un umbral sin que nadie hiciera nada
- **Tres requerimientos sin decidir** (umbral 60 días). La facultad de decidirlos es del Comité de producto, que se reúne el 2026-11-12.
  - REQ-4606 lleva 195 días (Óscar Ramírez).
  - REQ-4612 lleva 192 días (Mauricio Pérez).
  - REQ-4613 lleva 176 días (Ricardo Salas).
- **Supuesto «El proveedor cumple el tiempo pactado»:** lleva 205 días sin verificar (umbral 30). Verificarlo exige el historial de entregas del proveedor contra el plazo pactado. Ya pasó el punto en que conviene registrarlo como riesgo.
- **Evidencia vencida en 11 requerimientos:** todos se apoyan en la misma entrevista, de un cliente sin nombre, del 2025-10-14. Esa evidencia cumplió 12 meses ayer, así que todos se quedan sin sustento a la vez.

### Contradicción entre lo declarado y lo medido
El caso de negocio declara un volumen mensual de 249.273. El tablero de producto mide 153.324. La declaración queda 38,5 % por encima (umbral 20 %).

### Aceptado sin que nadie lo construya
- **Sin traza:** los 10 requerimientos aceptados no tienen proyecto.
- **REQ-4609:** se aceptó sin evidencia de que alguien lo pidiera.
- **Sin criterio de aceptación:** REQ-4603, 4605, 4607 y 4611.
- **Sin doliente:** REQ-4601.

### Las trazas
Ninguna traza estaba declarada, así que no hay nada que confirmar. La configuración no indica dónde están las fichas de proyecto. Leí `estado/records` (13 fichas) por mi cuenta, y ninguna dice ejecutar PRD-306.

### Del descubrimiento
No releí documentos de descubrimiento ni de definición en esta corrida, así que no sé si hay material nuevo. Hay que revisarlo a mano con `/product-discovery`.

Tras registrar la corrida corregí «29» por «31» señales en el archivo de salida. La cifra inicial estaba mal y la del script es la correcta. El archivo ya había quedado registrado como evidencia de la corrida, así que ese registro puede no coincidir con su contenido final.

Registré la revisión, tomé el corte (`snapshots/2026-10-15.json`) y guardé la corrida `2026-10-15-product-wake-1` (46 segundos). La salida completa está en `estado-producto/PRD-306/corridas/salida-product-wake.md`.

**Vuelvo el 2026-11-10.**