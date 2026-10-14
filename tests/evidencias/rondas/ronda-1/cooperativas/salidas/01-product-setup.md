# /criterio-product:product-setup documentos/productos/PRD-300

## Listo — Crédito de libranza (PRD-300)

**Lo que miré:** 4 documentos, 1 de descubrimiento (la entrevista del 2025-10-11). También leí la definición y el caso de negocio del 2026-05-09 y el acta del comité del 2026-10-13. Pude leer todos los formatos.

**Configuración:** como nadie respondió, tomé las respuestas sugeridas.
- **Producto:** Crédito de libranza, gerente Laura Vélez (sale del caso de negocio).
- **Quién decide:** el Comité de producto (sale del acta).
- **Estado:** `estado/PRD-300`, fuera de la carpeta de documentación.
- **Términos:** TERMS.md v1.0, aceptados por José Francisco Ñáñez el 2026-10-14.
- **Archivo:** `.criterio/producto/PRD-300/config.json`.

La persona que aceptó los términos no es la gerente que firma el caso. Queda registrado tal cual.

### Lo que tu definición afirma, y qué lo sostiene
| Afirmación | Sostenida por |
|---|---|
| «Asociados urbanos no tiene libranza» | Una entrevista de un cliente sin nombre: «Lo necesito y hoy no lo tengo». Sostiene su necesidad, no la falta de oferta en el segmento. |
| «El proveedor cumple el tiempo pactado» | Está marcado «verificado» (declarado el 2026-09-03), pero ningún documento muestra la verificación. |
| volumen_mensual 211.347 | Solo el propio caso de negocio, que se cita a sí mismo. |
| «Retorno esperado en 24 meses» | Nada: no hay cifra ni base de cálculo. |

### Lo que no está dicho en ninguna parte
- De dónde sale 211.347 al mes.
- Qué retorno es el esperado, y con qué supuestos.
- Qué es la «Propuesta principal»: la definición solo pone el título.
- Quién es el segmento, cuántos son, y qué es el éxito.
- Quién es el proveedor y cuál es el tiempo pactado.
- El criterio de aceptación de REQ-2023: está vacío, y aun así el comité lo aceptó.
- Qué proyecto ejecuta REQ-1000, REQ-1001 y REQ-2023: los tres figuran «—», y la definición dice «Ninguno declarado».
- Quién pidió cada requerimiento. El acta pone «Cliente entrevistado» en los tres, pero hay una sola entrevista y no se vincula con ninguno.
- Por qué «Se mantiene el plan».

### Sin serie medida
No hay ninguna serie medida a la vista. Nadie está midiendo lo que el negocio afirmó, así que no puedo decir cuánto se desvía 211.347.

El comando `compute` salió vacío porque el registro de requerimientos aún no existe. Por eso no calculé días ni porcentajes. La entrevista del 2025-10-11 está en el borde de los 12 meses del umbral de evidencia vieja. Eso queda sin verificar.

### Qué le falta a tu carpeta
- Las transcripciones de las entrevistas.
- La serie del volumen mensual con su fuente.
- Las decisiones del comité con su motivo.

La corrida quedó registrada como `2026-10-14-product-setup-1`, con la salida completa en `estado/PRD-300/corridas/salida-product-setup.md`.

**Siguiente paso:** `/product-discovery` sobre las entrevistas.