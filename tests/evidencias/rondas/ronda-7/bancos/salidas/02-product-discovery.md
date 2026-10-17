# /criterio-product:product-discovery 

No hay descubrimiento nuevo en PRD-302 (Crédito hipotecario digital). Los 4 documentos del producto no han cambiado desde la última lectura y no leí ninguno. El script `plan-lectura` dijo "nada que leer", así que solo recalculé.

- **Términos:** ya estaban vigentes, aceptados por José Francisco Ñáñez el 2026-10-17 para la versión 0.3.13. No los volví a registrar.
- **Pregunta sin respuesta:** no verifiqué si las entrevistas de 2025-09-12 tienen temas sin requerimiento, porque no las releí. El script `producto.py` solo señala los requerimientos con evidencia vencida o sin evidencia. La corrida lo deja anotado.
- **Registro:** hay 14 requerimientos, 9 aceptados y 5 propuestos. El recálculo dio 31 hallazgos:
  - 10 con evidencia vencida (la entrevista tiene 13 meses).
  - 9 aceptados sin proyecto que los trace.
  - 4 propuestos sin decisión (el más antiguo, REQ-4212, lleva 115 días).
  - 3 sin doliente.
  - 3 aceptados sin evidencia.
  - 1 aceptado sin criterio de aceptación.
  - 1 supuesto sin verificar desde hace 113 días: «La demanda declarada se sostiene sin campaña».
- **Brecha en la definición:** el criterio de éxito no está definido y la cifra de volumen mensual (130.646) no tiene serie medida que la contraste.
- **Corrida registrada:** `2026-10-17-product-discovery-1`. La salida quedó en `estado-producto/PRD-302/corridas/salida-product-discovery.md`.