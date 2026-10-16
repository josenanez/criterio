# /criterio-portfolio:portfolio-scan 

El barrido terminó: creé las fichas de 10 proyectos, las sellé y registré la corrida.

La ficha de cada proyecto está en `estado/records/PRY-<código>.json`. Los términos ya estaban vigentes y registrados a nombre de José Francisco Ñáñez (v1.1, 2026-10-16), así que no los volví a aceptar.

- **Lectura:** leí 62 de los 95 documentos, en un solo lote de 10 proyectos, uno tras otro y sin subagentes. Los otros 33 son de PRY-200, 202 y 207 y no cambiaron. Ninguno quedó ilegible. No existe `entrada/`, así que no moví nada.
- **Fichas nuevas:** PRY-199, 201, 203, 204, 205, 206, 208, 209, 210 y 211.
- **Sin dato:** `identity.authority` y `identity.phase` en las 10 fichas, y `identity.product` en PRY-205, 208 y 210 (el acta dice «No aplica»).
- **Contradicciones entre documentos:** ninguna.

Lo más relevante:
- **Plan movido con el cambio pendiente:** en PRY-203, 204 y 206 el cronograma v2 ya mueve el último hito en la magnitud de la CC-01, y esa solicitud sigue pendiente de comité.
- **Hitos cerrados sin acta:** hay 20 en el portafolio. En las fichas nuevas son 7 proyectos: 203, 204, 205 (4 de 5 hitos), 206, 209, 210 y 211.
- **Facturas y contratos:** PRY-206 tiene una factura de 82.731.823 COP sin acta de recibo de ningún entregable. PRY-205 tiene dos contratos (CT-853 y CT-108) con los mismos 4 entregables, todos vencidos y sin acta.
- **Presupuesto:** en PRY-206 y PRY-209 el ejecutado supera al comprometido.
- **Compromiso vencido:** en PRY-208, Mauricio Pérez debía entregar el punto 28 el 2026-10-01 y no hay evidencia de entrega.

Dos cosas que no quedaron limpias:
- **Doble registro de la corrida:** la corregí tras ver que PRY-205 tenía 4 hitos sin acta y no 5, y volví a correr `corrida`. Quedó registrada dos veces; el primer registro (`2026-10-16-portfolio-scan-1`) tiene la duración medida (194 s) y el segundo no, pero este trae la salida corregida.
- **Script de apoyo:** armé las fichas con un script que dejé en el directorio temporal de la sesión. Los datos salen de lo que leí, pero la verificación sigue siendo suya.

La salida completa está en `estado/corridas/salida-portfolio-scan.md`. Hay más de un proyecto con ficha, así que puedo generar el informe consolidado con `/criterio-portfolio:portfolio-report`; no lo corrí porque no lo pidieron.

Criterio Portfolio v0.3.12 · fichas tocadas: 10 · Términos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal