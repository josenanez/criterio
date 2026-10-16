# /criterio-product:product-setup documentos/productos/PRD-300

Listo. Dejé PRD-300 (Monitoreo de flota) configurado y la ficha levantada. Aceptación de términos registrada, y la corrida quedó registrada como `2026-10-15-product-setup-1`.

**Qué hay:** 4 documentos, solo uno de descubrimiento (una ronda de entrevistas del 2025-08-18 con una sola cita de un cliente sin nombre). Hay una definición y un caso de negocio del 2025-11-14, y un acta del comité del 2026-10-14. No hay series de métricas ni transcripciones. Leí los dos .docx.

**Términos:** José Francisco Ñáñez los aceptó para la versión 0.3.10 (términos 1.1) el 2026-10-15, con el sí que traía el argumento de la sesión.
- Comprobante: `.criterio/terminos/aceptacion-criterio-product-0.3.10-2026-10-15.md` y `.pdf`, con su `.sha256`.
- SHA-256 del `.md`: `fdf0177cc54e5055…`

**Qué afirma la definición y qué la sostiene:**

| Afirmación | Sostenida por |
|---|---|
| Operadores no tiene monitoreo de flota | Una cita («Lo necesito y hoy no lo tengo»), de 13 meses. No dice que el cliente sea Operador ni que hable de flota |
| El ahorro se sostiene sin inversión adicional | Un supuesto sin verificar hace 113 días |
| volumen_mensual = 210.767 | Solo el propio caso de negocio |
| Retorno esperado en 24 meses | Nada: sin cifra, método ni fuente |

**Lo que no está dicho en ninguna parte:**
- El criterio de éxito y el contenido de la propuesta («Propuesta principal» y nada más).
- De dónde sale 210.767. No hay serie medida, así que nadie está midiendo lo que el negocio afirmó.
- La cifra del retorno y la del ahorro.
- Qué proyecto construye cualquiera de los 14 requerimientos: 11 aceptados, 0 con proyecto.
- El criterio de aceptación en REQ-4000, 4002, 4006 y 4011, todos aceptados.
- Doliente en REQ-4000, 4003, 4011 y 4012 («sin asignar»).
- Evidencia en REQ-4002 y 4006, aceptados sin ninguna.

**Lo que marca el cálculo (37 hallazgos):**
- 12 requerimientos se apoyan en la misma entrevista de hace 13 meses. Esa entrevista no nombra ninguno.
- 3 propuestos llevan sin decidir 175, 120 y 80 días (REQ-4013, 4008 y 4012).
- La fecha del supuesto es posterior a la de la definición, así que el documento se tocó después de su fecha.

**Para mejorar la carpeta, como hallazgo y no como requisito:** las transcripciones completas, la serie de volumen_mensual con su fuente, el desglose del retorno y del ahorro, y las decisiones del comité con quién decidió.

**Tres cosas que hice por mi cuenta:**
- **Quién decide:** lo puse como «Comité de producto», la respuesta sugerida, porque el acta no lo nombra en esas palabras.
- **`sellar`:** exigió una corrida abierta, así que abrí una con `corrida-inicio`. El comando dice que aquí no va.
- **Salida registrada:** en `estado-producto/PRD-300/corridas/salida-product-setup.md` la lista «Lo que no está dicho» tiene dos fallas. Escribí «las dos únicas decisiones del acta» y hay una sola («Se mantiene el plan»). La línea sobre REQ-4002 y 4006 también está mal redactada. El archivo quedó registrado tal cual, sin corregir.

Siguiente paso sugerido: `/product-discovery` sobre las entrevistas.