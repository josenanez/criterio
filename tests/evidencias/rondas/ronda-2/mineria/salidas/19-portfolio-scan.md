# /criterio-portfolio:portfolio-scan 

## Barrido — 2026-10-15

Escribí 10 fichas nuevas a partir de 59 de los 74 documentos. Los 15 restantes son de PRY-201, PRY-204 y PRY-205, que no cambiaron, y no las toqué. No hubo archivos ilegibles. No hay carpeta `entrada/`, así que no moví nada. No encontré proyectos que solo aparezcan mencionados en minutas de otro.

**Términos:** ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-15), así que no los registré otra vez. Nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

Corrí el plan tal cual: un lote de 10 proyectos, uno tras otro, sin subagentes. Sellé cada ficha con sus hashes (los calculó el script). La corrida quedó registrada con el id `2026-10-15-portfolio-scan-1` y tardó 204 segundos.

**Fichas nuevas:** PRY-199, 200, 202, 203, 206, 207, 208, 209, 210 y 211. En los diez proyectos quedaron sin dato la autoridad del gerente y la fase. En PRY-202, 206, 209, 210 y 211 también falta el producto, porque el acta dice «No aplica». PRY-206 y PRY-209 no tienen cronograma, así que no hay hitos.

**Qué encontró el cálculo sobre las fichas nuevas** (31 señales en 8 de los 10 proyectos):
- **Verde con señales en contra, 5 proyectos** (203, 207, 208, 210, 211). Ejemplo: PRY-208 declara verde con 68 %, su línea base se movió 113 días y sus dos hitos cerrados no tienen acta.
- **8 hitos declarados cerrados sin acta de recibo** en 5 proyectos (200, 203, 207, 208, 210). El acta puede existir y no estar archivada. PRY-199 y PRY-211 sí tienen actas de los hitos que cerraron.
- **Cronograma v2 sin cambio aprobado.** En PRY-207 (+106 días) y PRY-211 (+65 días), la solicitud CC-01 sigue pendiente del comité y el cronograma v2 ya recorrió la fecha. En PRY-208 la CC-01 figura autorizada por «el comité», sin decir cuál.
- **Contradicción entre documentos** en PRY-207, 208 y 211: el último hito del cronograma v2 cae después del cierre comprometido en el acta. Guardé los dos valores.
- **Proveedores:**
  - Hay facturas sin ningún entregable recibido con acta en PRY-207 (CT-517, 69.251.482 COP) y en PRY-210 (CT-637, 553.602.024 COP).
  - En PRY-207, un entregable de CT-555 figura como «recibido» sin acta.
  - Hay 3 entregables vencidos sin recibo (PRY-207 y dos en PRY-210).
  - En PRY-210, la factura FV-1414 es anterior al acta de recibo de la bolsa de horas.
- **Compromisos:** uno vencido sin evidencia (PRY-202, punto 15, venció el 2026-10-01) y dos sin fecha («por definir», en PRY-207 y PRY-211).
- **PRY-206** lleva 20 días sin documentos nuevos. Su cierre comprometido (2026-09-22) ya pasó, y declara amarillo con 77 %.
- **PRY-202** declara 48 % de avance, pero su plan, sin ningún hito cerrado, sustenta entre 0 y 20 %.
- **Cifras que no cuadran:** en PRY-200, 208 y 211, el ejecutado declarado supera al comprometido. Las guardé tal cual, como declaración.

El informe completo está en `estado/corridas/salida-portfolio-scan.md`.

Con más de un proyecto con ficha, puedo generar el informe consolidado con `/criterio-portfolio:portfolio-report`. Los 13 proyectos suman 44 señales, 8 de ellas de «verde contradicho».

Criterio portfolio 0.3.8 · fichas tocadas: 10 · campos en `not_found`: autoridad y fase (10), producto (5), hitos (2). Es un borrador de trabajo con cita a cada fuente; la verificación es suya.