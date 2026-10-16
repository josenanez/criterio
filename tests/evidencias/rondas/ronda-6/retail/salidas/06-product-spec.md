# /criterio-product:product-spec 

Escribí el borrador de especificación de PRD-302 (Autopago en tienda). Sale vacío de comportamiento: no cubre ninguno de los 12 requerimientos aceptados.

Los términos ya estaban vigentes, aceptados por José Francisco Ñáñez el 2026-10-16. No había preguntas que responder.

**Por qué no hay secciones de comportamiento.** Ningún requerimiento dice qué necesita: el título es solo el código y el campo «necesidad» no consta en ninguno de los 15. Escribir el comportamiento habría sido inventarlo, así que lo dejé como hueco.

**Criterios de aceptación.**
- Nueve de los aceptados traen el mismo criterio, «se verifica en producción». No es verificable: no dice qué se observa ni con qué umbral.
- Tres no traen ninguno: REQ-4204, 4208 y 4210.
- Ningún criterio usa el único dato que se mide hoy, `volumen_mensual`.

**Vacíos, cada uno con quien lo cierra.**
- REQ-4207 y REQ-4209 no tienen doliente; los asigna Elena Duarte.
- REQ-2028, 4203, 4207 y 4209 no tienen quién los pidió según el acta del comité.
- El supuesto «La regulación de datos lo permite» sigue sin verificar: dice «verificado» pero no cita con qué.
- Los casos borde, los otros equipos y las obligaciones normativas no aparecen en ningún documento. Los dejé señalados, sin rellenar.
- La definición no declara criterio de éxito.

**Fuera de alcance.** REQ-4201, 4206 y 4213 siguen propuestos hace 125 a 135 días, sin decisión del Comité de producto.

No ofrecí `/product-charter` porque los vacíos siguen abiertos. Hay que cerrar primero la necesidad y el criterio de aceptación y volver a correr este comando.

La corrida quedó registrada como `2026-10-16-product-spec-1` (38 s, 15 requerimientos, 25 hallazgos).

Archivos en `/home/claude/banco/ronda-6/retail/espacio/estado-producto/PRD-302/corridas/`:
- `salida-product-spec.md`