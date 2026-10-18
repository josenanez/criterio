# /criterio-product:product-definition 

## Definición: Monitoreo de flota (PRD-300), contrastada al 2026-10-17

**Términos:** ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-17), así que no los registré de nuevo.

**Documento:** `2025-12-15-definicion-producto.docx` y `2025-12-15-caso-de-negocio.md`, del 2025-12-15. Saqué 7 afirmaciones.

**Lo que la evidencia contradice:** nada. Ninguna fuente dice lo contrario de lo que afirma la definición.

**El negocio y los datos:**

| Métrica | Declarado | Medido | Diferencia |
|---|---|---|---|
| volumen_mensual | 236.725 (caso de negocio, 2025-12-15) | 201.743 (tablero de métricas, corte 2026-10-15) | −14,8 % |

La diferencia queda bajo el umbral de 20 % de la configuración, así que es imprecisión y no contradicción. Hay dos reservas:
- La serie tiene un solo punto, así que no se ve tendencia.
- El tablero no define qué cuenta como «volumen».

**Afirmaciones numéricas que nadie mide:** «Retorno esperado en 24 meses». No trae cifra ni base de cálculo, y ninguna métrica la sigue.

**No está dicho en ninguna parte:**
- El criterio de éxito.
- El contenido de la propuesta: la sección dice solo «Propuesta principal».
- Que el segmento Mantenimiento sea quien tiene el problema. La entrevista no nombra el segmento.
- Qué cuenta como «volumen mensual».
- Cuál es «el plan» que el comité del 2026-10-15 decidió mantener.
- Qué datos recoge el monitoreo.

**Sostenida por un supuesto:** «El proveedor cumple el tiempo pactado» figura como verificado el 2026-07-13, 116 días después de declararse. Se verificó con el documento técnico del propio proveedor, que no está en la carpeta (solo la nota de verificación). Para sostenerlo hace falta traer ese documento y contrastarlo con una fuente que el proveedor no controle, como una entrega recibida o un acta de aceptación. No hay supuestos sin verificar.

**Sostenida por evidencia:** el problema del segmento descansa en una sola entrevista del 2025-10-08: «Lo necesito y hoy no lo tengo.» Es evidencia débil: alguien dijo que lo necesita, pero nadie pagó ni pidió algo concreto.

**Evidencia que ya envejeció:** esa entrevista tiene 12 meses, justo en el umbral. Es lo único que sostiene el problema y 11 de los 16 requerimientos. Además, 3 requerimientos aceptados (REQ-4003, REQ-4004, REQ-4009) no tienen ninguna evidencia de demanda.

**Lo normativo que toca:** no nombré ninguna norma. La definición no menciona datos personales, pagos ni retención. Un monitoreo de flota podría recoger ubicación de conductores, pero el documento no dice qué recoge, así que no puedo establecer si aplica algo ni si se cumple. No tengo país ni norma a la vista. Esto va a revisión jurídica.

**Lo que falta para cerrar la definición:**
- **Criterio de éxito:** falta, y sin él el producto no se puede cerrar.
- **Problema y para quién:** declarados.
- **Quién decide:** el Comité de producto, pero a la reunión del 2026-10-15 asistió solo el gerente de producto.
- Ningún proyecto construye el producto («Ninguno declarado») y 0 de los 11 requerimientos aceptados tienen trazabilidad a un proyecto.

**Después:** no hay supuestos sin verificar que convertir en riesgo, y la definición no puede cerrarse sin criterio de éxito, así que no ofrezco `/product-charter`.

La corrida quedó registrada como `2026-10-17-product-definition-1`. Escribí el resultado completo en `estado-producto/PRD-300/corridas/salida-product-definition.md`.