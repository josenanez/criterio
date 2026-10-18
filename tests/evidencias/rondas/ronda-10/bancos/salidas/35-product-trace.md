# /criterio-product:product-trace 

## Trazabilidad — Tarjeta de crédito digital (PRD-304) · al 2026-10-18

Hay 17 requerimientos decididos y ninguno tiene proyecto. Tampoco hay trazas confirmadas ni entregados.

**Dos puntos de la corrida:**
- Los términos ya estaban vigentes, aceptados por José Francisco Ñáñez el 2026-10-18, así que no se pidió nada.
- La configuración apunta a `estado` como carpeta de fichas, y con esa ruta `compute` falla: `estado/corridas.json` es una lista y el script espera fichas. Las fichas reales están en `estado/records/`, y con esa carpeta se calculó. Si esa no es la carpeta que corresponde, hay que corregir `paths.fichas`.

**Decidido y nadie lo está construyendo:** los 17 aceptados tienen `project: null`. El más antiguo es REQ-4410, decidido el 2026-03-20 y sin proyecto desde hace 212 días. La decisión está citada en `30-decisiones/2026-10-18-comite-producto.docx`. Ese documento no dice quién decidió, así que «por quién» quedó como «no figura» y no lo supuse. REQ-4401 sigue «propuesto», con 65 días sin decidir, y no cuenta como brecha de construcción.

**La traza no se confirma:** no hay ninguna, porque ningún requerimiento nombra un proyecto y no hay nada que cruzar con las fichas.

**Lo que un proyecto construye y el registro no tiene:** ninguno. De las 13 fichas leídas, ninguna dice ejecutar PRD-304.
- Nueve declaran otro producto.
- PRY-202, PRY-205, PRY-208 y PRY-210 tienen vacío el campo de producto. Es un hallazgo del lado de esas fichas, y no infiero que alguna construya la tarjeta.

Con 41 hallazgos en total, `requirement_untraced` es el más frecuente, 17, y `evidence_stale` le sigue con 13. La corrida quedó registrada como `2026-10-18-product-trace-1`, con la salida en `estado-producto/PRD-304/corridas/salida-product-trace.md`.

**Después:** como hay decididos sin proyecto, el siguiente paso sería `/criterio-product:product-charter` para el que ya esté listo. No decidí cuál es.