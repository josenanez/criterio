# /criterio-portfolio:portfolio-scan 

## Barrido — 2026-10-17

Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-17), así que no hubo que registrarlos de nuevo. Escribí 10 fichas, selladas una a una, y dejé la corrida registrada.

**Documentos:** 89 en la carpeta, 59 leídos, 30 sin cambio y 0 ilegibles. Un solo lote de 10 proyectos, uno tras otro y sin subagentes.
**Proyectos:** 13 con ficha. 10 son nuevos (PRY-199, 201, 202, 203, 204, 205, 206, 208, 209 y 211). PRY-200, 207 y 210 no cambiaron y no se releyeron. Ninguno quedó sin carpeta propia.
**Movidos y pendientes:** nada. La carpeta no tiene `entrada/`.

**Campos sin dato:** `authority` y `phase` faltan en las 10 fichas. `product` falta además en PRY-202, 205, 208 y 209, porque su acta dice «No aplica». PRY-205 no tiene cronograma, así que su ficha no tiene hitos.

### Lo que hay que mirar

- **Línea base movida sin autorización:**
  - PRY-204: el cronograma v2 mueve el piloto 116 días. La solicitud CC-01 que pide esos días es posterior y sigue pendiente del comité.
  - PRY-208: el v2 mueve el piloto 59 días. Su CC-01 también está pendiente.
  - PRY-206: este sí está en regla. Su CC-01 (+36 días) figura autorizada, aunque el documento no nombra qué comité.
- **Factura sin entrega:** PRY-206 tiene la factura FV-1399 por 96.483.298 COP contra CT-399. Ninguno de sus tres entregables tiene acta de recibo y los tres están vencidos.
- **Entregables de proveedor vencidos:** hay 9 en total, sin acta de recibo. 4 son de PRY-202 y 2 de PRY-201. Los otros 3 son de PRY-206, los mismos tres del caso anterior.
- **Hitos declarados cerrados sin acta que lo pruebe:**
  - Los hay en PRY-201, 202, 203, 204, 206 y 208.
  - En PRY-209 el diseño funcional venció el 2026-10-09 y sigue abierto y sin acta.
- **Estado declarado frente a los documentos:**
  - PRY-203 está en verde con 28%, y su acta fijaba el cierre al 2026-01-17.
  - PRY-202 está en rojo con 46%, mientras su cronograma declara cerrada la salida a producción del 2026-05-23.
  - PRY-211 reporta 74% sin ningún hito cerrado.
  - Seis informes dicen «se reprogramó la salida», y solo PRY-206 tiene un cronograma que lo registre.
- **Dinero según los informes:** en PRY-201, 202, 203, 205 y 209 el ejecutado supera al comprometido. La proyección al cierre pasa el aprobado en PRY-201, 205, 206 y 211.
- **Compromisos de minutas:** el de Jorge Medina en PRY-203 (punto 13, para el 2026-10-14) está vencido, sin evidencia de entrega. PRY-202 y PRY-211 tienen compromisos «por definir». En los cinco compromisos, quien se compromete no figura entre los asistentes.
- **PRY-200:** 15 citas de su `ficha-pm` no resuelven desde la raíz de documentación, porque les falta el prefijo de la carpeta del proyecto. No toqué su ficha.

La corrida registró 66 hallazgos en los 13 proyectos, en 255 segundos. El detalle completo, con tablas, está en `estado/corridas/salida-portfolio-scan.md`.

**Siguiente paso:** como hay más de un proyecto, puedo generar el informe consolidado con `/criterio-portfolio:portfolio-report`.

---
criterio-portfolio 0.3.13 · términos v1.1: https://www.josenanez.com/es/agents/criterio-pmo/legal#v0.3.13
Fichas tocadas: 10. Campos en `not_found`: `authority` y `phase` en las 10, `product` en 4.