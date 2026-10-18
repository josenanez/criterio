# /criterio-portfolio:portfolio-report html

# Portafolio — 2026-10-18

**13 proyectos, 10 con hallazgos (47 señales).** Cargué las 13 fichas de `estado/records/`, todas del 2026-10-18, así que ninguna tiene más de una semana sin barrido. Los términos (v1.1) ya estaban aceptados por José Francisco Ñáñez el 2026-10-18 y no los registré de nuevo.

**Qué cambió:** nada. El diff dio 0 cambios, pero la instantánea previa es del mismo día.

**Lo que muestra el informe:**
- **Verdes contradichos:** 6 proyectos declaran verde y la evidencia no lo sostiene: PRY-200, 201, 202, 203, 204 y 209.
- **Hitos sin evidencia:** 21 hitos figuran como cumplidos sin respaldo en 9 proyectos. Los más cargados son PRY-201 y PRY-210, con 4 cada uno.
- **Avance bajo el plan:** 7 proyectos declaran menos avance del que sostiene el plan. El peor es PRY-205, con 34% declarado frente a 100%.
- **PRY-205:** además está +146 días y +21,3% en costo contra la línea base original.
- **PRY-202:** +95 días contra la original.
- **PRY-208:** movió 26 días sin autorización.
- **Proveedores:** 5 entregables atrasados (PRY-201 y PRY-204), 3 aceptados sin evidencia y 1 facturación por encima de lo aceptado (PRY-201).

**Secciones vacías:**
- **Contradicciones abiertas:** ninguna.
- **Proyectos en silencio:** ninguno. El máximo es PRY-201, con 10 días, bajo el umbral de 15.
- **Dependencias en riesgo:** ninguna, porque no hay dependencias declaradas por código.

**Vacíos de información:** ningún proyecto tiene autoridad registrada (13 de 13). PRY-201, 205, 210 y 211 tienen entre 11 y 12 campos con más de 12 meses de antigüedad.

**Confirmación mensual:** no la armé porque el script no indicó que tocara. Si quieres hacerla, los candidatos son los campos viejos de PRY-201, 205, 210 y 211.

**Archivos** (en `/home/claude/banco/ronda-10/mineria/espacio/reportes/`, 23 páginas):
- `index.html`: la vista por campo, con la cadena de evidencia, para quien va a actuar.
- `decisiones.html`: la vista por decisión, para el patrocinador.
- 13 páginas de proyecto y 6 de producto. 7 proyectos no tienen producto asignado: PRY-201, 202, 205, 206, 209, 210 y 211.
- Para el PDF, imprime el HTML desde el navegador.

La corrida quedó registrada como `2026-10-18-portfolio-report-1` (80 documentos sin cambio, 35 segundos). La salida está en `estado/corridas/salida-portfolio-report.md`.

Siguiente paso posible: el material de comité del 2026-10-29 (`/criterio-portfolio:steering-pack`) o el detalle de PRY-205, PRY-208 y PRY-201.

*Pie: criterio-portfolio 0.5.0 · 13 fichas del 2026-10-18 · campos inciertos: 0 contradicciones, 2 a 4 campos faltantes por ficha · términos: https://www.josenanez.com/es/agents/criterio-pmo/legal*