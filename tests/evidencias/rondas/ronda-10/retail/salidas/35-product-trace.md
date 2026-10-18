# /criterio-product:product-trace 

## Trazabilidad — Venta en línea (PRD-300), al 2026-10-18

La cadena se rompe entre la decisión y el proyecto. Hay 15 requerimientos decididos y ninguno tiene proyecto: en el acta del comité del 13-oct, la columna «Proyecto que lo ejecuta» es «—» en todos. Por eso ninguna traza se pudo confirmar contra una ficha, y no hay entregables.

- **Decidido y nadie lo construye:** son REQ-2028 y REQ-4000 a REQ-4013. El más antiguo es REQ-4006, decidido el 31-mar, hace más de 6 meses.
- **Lo que un proyecto construye y el registro no tiene:** la ficha de PRY-200 (Tienda en línea) dice que ejecuta «venta en línea», y ningún REQ la nombra. La coincidencia es por nombre; la ficha no trae el código PRD-300. Queda como candidato a verificar con su gerente de proyecto, no como traza confirmada.
- **Fichas que no dicen su producto:** las de PRY-203, 206, 209, 210 y 211 tienen el campo vacío. Eso es un hallazgo del lado de esas fichas, y no permite atribuirles ni descartarles relación con PRD-300.
- **Cobertura:** 9 de 15 tienen evidencia de demanda (60 %) y 0 de 15 están trazados.

La corrida quedó registrada como `2026-10-18-product-trace-1`, con 34 hallazgos en 26 s. Cada decisión que nadie construye cuenta como `requirement_untraced`, y esas son 15 de los 34.

**Términos:** ya estaban vigentes (v1.1), aceptados por José Francisco Ñáñez el 2026-10-18. No hizo falta registrarlos de nuevo.

**Siguiente paso:** si algún requerimiento ya está listo para ser proyecto, `/product-charter`. Con PRY-200 conviene hablar con su gerente de proyecto.

Archivos en `estado-producto/PRD-300/corridas/`:
- `salida-product-trace.md`
- `2026-10-18-product-trace-1.md`