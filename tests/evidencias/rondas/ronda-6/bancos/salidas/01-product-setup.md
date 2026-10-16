# /criterio-product:product-setup documentos/productos/PRD-306

## Listo — Microseguros (PRD-306)

**Lo que miré:** 4 documentos (2 .docx y 2 .md), todos legibles. Solo uno es de descubrimiento: una entrevista del 2025-10-05. La definición y el caso de negocio son del 2025-12-25, y lo más reciente es el acta del comité del 2026-10-14. No hay serie medida de ninguna métrica.

**Términos:** José Francisco Ñáñez los aceptó el 2026-10-16 para la versión 0.3.12 (términos 1.1). Lo registré con el sí que venía en el argumento de la prueba.
- Comprobante en `.criterio/terminos/aceptacion-criterio-product-0.3.12-2026-10-16.md` y `.pdf`.
- SHA-256 del .md: bbc944aafa669a5067d0a907591a89f40c0b0d00c37cb1e1b054d8f9862c5919.

**Respuestas por defecto** (nadie respondió):
- **Gerente:** Jorge Medina, según la definición.
- **Quien decide:** Comité de producto. Es una propuesta mía; el acta no lo dice.
- **Estado:** `estado-producto/PRD-306`.

### Lo que tu definición afirma, y qué lo sostiene
| Afirmación | Sostenida por | De cuándo |
|---|---|---|
| «El segmento Personas no tiene microseguros» | Nada que lo diga del segmento. Lo más cercano: un cliente sin nombre dijo «Lo necesito y hoy no lo tengo», sin decir qué es «lo» | 2025-10-05 |
| Volumen mensual de 204.945 | Solo el propio caso de negocio; no hay serie medida | 2025-12-25 |
| «Retorno esperado en 24 meses» | Nada: no hay cifra ni base | 2025-12-25 |
| «El proveedor cumple el tiempo pactado» | Un supuesto sin verificar (110 días) | declarado 2026-06-28 |

### Lo que no está dicho en ninguna parte
- Que el segmento Personas necesite microseguros. La única entrevista no los menciona.
- El criterio de éxito del producto.
- En qué consiste la propuesta: el documento dice «Propuesta principal» y nada más.
- De dónde sale el 204.945 mensual y cuánto se mide hoy. Nadie está midiendo lo que el caso de negocio afirmó.
- Cuánto es el retorno esperado y cómo se calculó.
- Quién decidió cada aceptación: el acta solo lista como asistente a Jorge Medina.
- Qué problema resuelve cada requerimiento: los 16 del acta (REQ-4600 a REQ-4615) solo traen el número.
- Qué proyecto ejecuta cada requerimiento aceptado: 0 de 12.

### Supuestos sobre los que está escrita
Uno declarado: «El proveedor cumple el tiempo pactado», sin verificar. El documento es de 2025-12-25 pero el supuesto dice «declarado el 2026-06-28», así que se editó después de su fecha.

### Qué le falta a tu carpeta
- Más entrevistas, con nombre de quien habla y qué pide. Hoy hay una.
- La serie del volumen mensual con su fuente.
- Las decisiones del comité, con quién decidió cada una.
- El proyecto que ejecuta cada requerimiento aceptado.

### Lo que ya muestra el registro (cifras de `compute`)
Son 16 requerimientos: 12 aceptados y 4 propuestos.
- **Evidencia:** 9 de los 12 aceptados tienen alguna (75.0 %). Toda es esa entrevista de hace 12 meses, que no nombra ningún requerimiento, así que `evidence_stale` sale 12 veces (incluye 3 propuestos).
- **Sin ninguna evidencia:** REQ-4603, REQ-4614 y REQ-4615.
- **Sin criterio de aceptación:** REQ-4606, REQ-4613, REQ-4614 y REQ-4615. En los demás el criterio es «se verifica en producción», que no dice qué se mide.
- **Sin doliente:** REQ-4602.
- **Propuestos sin decidir:** REQ-4609 (197 días), REQ-4601 (154), REQ-4607 (143) y REQ-4611 (111).
- **Sin proyecto que los ejecute:** 12 aceptados (0.0 % con traza).

**Archivos:**
- `estado-producto/PRD-306/producto.json` y `requirements/` con los 16 registros.
- `estado-producto/PRD-306/corridas/salida-product-setup.md` con esta salida.
- La corrida quedó registrada como `2026-10-16-product-setup-1` (0 preguntas, 38 segundos).
- La configuración quedó en `.criterio/producto/PRD-306/config.json`.

**Siguiente paso:** `/product-discovery` sobre las entrevistas.