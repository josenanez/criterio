# /criterio-portfolio:portfolio-scan 

Barrido terminado. Escribí y sellé 10 fichas nuevas y la corrida quedó registrada como `2026-10-15-portfolio-scan-1`.

Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-15), así que no los registré de nuevo.

- **Documentos:** de 82, leí 48 y 34 no habían cambiado. Ninguno quedó ilegible, no hay nada en `entrada/` por mover y no quedó nada diferido.
- **Fichas:** PRY-199, 200, 201, 202, 203, 204, 206, 208, 210 y 211. Las de PRY-205, 207 y 209 no se tocaron. Los lotes fueron uno tras otro, sin subagentes.
- **Hallazgos:** el cálculo levantó 68 en todo el portafolio. El detalle está en `estado/corridas/salida-portfolio-scan.md`.

Lo que conviene mirar primero:
- **PRY-202:** declara verde y acumula 8 señales. Entre ellas, +66 días y proyección 25 % sobre el presupuesto. El cronograma v2 mueve un hito más allá del cierre del acta (2026-07-15) y ningún documento da una fecha de cierre nueva. Dejé esa fecha como falta, no la inferí.
- **PRY-201:** declara verde y lleva 24 días sin documentos. Su cierre (2026-10-12) ya pasó y no hay cronograma.
- **PRY-204:** declara rojo. El contrato marca como recibida la bolsa de horas, que no tiene acta de recibo, y ya hay una factura por 1.822.428.850 COP. También tiene un hito y un entregable vencidos.
- **Hitos cerrados sin acta de recibo:** PRY-200, 202, 204, 206, 208, 210 y 211. PRY-199 es la excepción.
- **PRY-203, 206 y 211:** reportan ejecutado mayor que comprometido, lo cual no cuadra.
- **Autoridad y fase:** no aparecen en ningún documento. Quedaron en `not_found` en las 10 fichas.

El índice lista 11 campos de la ficha del gerente de PRY-207 con una cita que no resuelve contra la raíz de documentación. No lo toqué.

Puedo generar ahora el informe consolidado del portafolio, que es lo que ofrece el flujo cuando hay más de un proyecto.

Pie: criterio-portfolio 0.3.9 · 10 fichas tocadas · términos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal#v0.3.9