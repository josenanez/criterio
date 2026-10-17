# /criterio-portfolio:portfolio-report html

Informe de portafolio generado en HTML, con las dos vistas más una página por proyecto y por producto. Tiene 13 proyectos y 61 señales. 10 proyectos tienen hallazgos y 5 declaran verde pese a lo que muestra la evidencia.

Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-17), así que no los registré de nuevo. Las 13 fichas están en `estado/records/` y son todas del 2026-10-17. La carpeta `estado/fichas/` no existe.

**Archivos** (carpeta `reportes/`, 24 páginas):
- **`reportes/index.html`:** vista por campo, con la cadena de evidencia. Es para la PMO y los gerentes de proyecto.
- **`reportes/decisiones.html`:** vista por decisión, solo lo que excede la facultad del gerente. Es para el patrocinador y el comité.
- **PDF:** sale de imprimir el HTML.

**Qué cambió:** no hay instantánea anterior distinta de la de hoy, así que esta es la línea de partida y el diff dio 0 cambios.

**Verdes contradichos por la evidencia:**
- **PRY-211:**
  - Tiene 7 compromisos vencidos y 5 reprogramados, uno de ellos 6 veces.
  - Un proveedor facturó $1.197,9 M frente a $775,5 M aceptados.
  - Otro facturó $723,8 M sin ningún entregable aceptado.
  - La proyección de costo está +26,9 % sobre lo aprobado.
- **PRY-206:** declara 32 % de avance con 4 de 4 hitos "cumplidos", sin evidencia de ninguno. Su fecha fin (2025-12-22) ya venció y la proyección de costo está +21,4 %.
- **PRY-204:** su fecha fin (2026-08-26) ya venció y la proyección de costo está +10,8 %. Dos hitos "cumplidos" no tienen evidencia.
- **PRY-205:** se replanificó 75 días sin autorización y tiene 95,5 % comprometido.
- **PRY-207:** declara 49 % de avance cuando el plan sostiene entre 0 y 33 %.

**Otros hallazgos:**
- **PRY-209:** se corrió 55 días (24,3 %) sin autorización.
- **PRY-203:** el hito "Integración con el ERP" lleva 13 días vencido.

**Secciones vacías:**
- Contradicciones abiertas.
- Proyectos en silencio.
- Dependencias en riesgo.

**Campos inciertos:** los 13 proyectos no tienen autoridad ni fase registradas, y 6 no tienen producto. Los campos de identidad y plan de PRY-204 y PRY-206 tienen 16 meses de antigüedad, por encima del umbral de 12.

**Confirmación mensual:** no la armé, porque es la primera corrida y esta sesión no tiene a nadie que responda.

**Dos correcciones a lo guardado en `estado/corridas/salida-portfolio-report.md`:**
- Dice que PRY-211 tiene 6 compromisos vencidos. El correcto es 7, como arriba.
- Incluye una nota sobre el ERP: dice que los hitos "Integración con el ERP" de PRY-203, 204, 206 y 211 se relacionan con el corrimiento de PRY-209. Es una lectura mía, y ninguna ficha declara esa dependencia por código. Trátala como pista, no como hallazgo.

Cuando se registró la corrida (`2026-10-17-portfolio-report-1`, 37 s, 80 documentos sin relectura), el archivo ya contenía esos dos puntos, y no lo registré de nuevo.

Si hay comité próximo, puedo preparar el material de comité o entrar al detalle de PRY-211.