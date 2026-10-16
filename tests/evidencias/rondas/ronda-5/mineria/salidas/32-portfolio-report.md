# /criterio-portfolio:portfolio-report html

Generé el informe HTML del portafolio y registré la corrida como `2026-10-16-portfolio-report-1`. Los términos ya estaban vigentes (versión 0.3.11, aceptados por José Francisco Ñáñez el 2026-10-16), así que no hubo que aceptarlos otra vez.

Cargué las 13 fichas (PRY-199 a PRY-211), todas del barrido de hoy. La instantánea anterior también es de hoy, así que el diff dio 0 cambios y el informe no tiene delta. Hay 58 señales en 11 de los 13 proyectos. Solo PRY-199 y PRY-209 no tienen ninguna.

- **Verdes contradichos:** seis proyectos declaran verde y la evidencia no lo sostiene (PRY-202, 205, 206, 208, 210 y 211).
- **Líneas base movidas sin autorización:** PRY-203 (66 días), PRY-210 (33) y PRY-211 (70).
- **Hitos declarados cumplidos sin evidencia:** 19 en total. PRY-200 tiene sus 4 hitos en esa situación.
- **Contradicción abierta:** la fecha de fin de PRY-200 es 2026-08-08 en el cronograma y 2026-09-30 en el acta. Ambos documentos son del 2025-06-03, así que no hay forma de desempatar.
- **Compromisos de PRY-200:** tiene 6 vencidos sin evidencia, no 4 como dice el informe. La salida ya quedó registrada con "4+", que es impreciso.
- **Vacíos de datos:** los 13 proyectos no tienen autoridad ni fase. PRY-206 y PRY-209 no tienen línea base, y siete proyectos no tienen producto asociado.
- **Dependencias entre proyectos:** el cálculo no devolvió ninguna señal. En PRY-207 hay un entregable de proveedor atrasado 33 días.
- **Confirmaciones del mes:** las cinco preguntas quedaron redactadas en el informe, sin respuesta porque nadie contesta en esta prueba.

Los archivos quedaron en `reportes/`, con 23 páginas. Cada audiencia tiene su vista:
- **`index.html`:** para quien va a actuar. Va por campo, con la cadena de evidencia completa.
- **`decisiones.html`:** para el patrocinador. Va por decisión, con pregunta cerrada y la consecuencia de no decidir.

También hay una página por proyecto y por producto, más `productos.html` y `proyectos.html`. El PDF sale de imprimir el HTML.

La salida completa está en `estado/corridas/salida-portfolio-report.md` y el registro de la corrida en `estado/corridas/2026-10-16-portfolio-report-1.md`. La corrida tardó 64 segundos y leyó 77 documentos sin cambios (0 releídos).

Si hay comité próximo, puedo preparar el material con `steering-pack`. También puedo entrar al detalle de PRY-200, que concentra 18 de las 58 señales.