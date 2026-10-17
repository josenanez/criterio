# /criterio-portfolio:portfolio-report html

# Portafolio — 2026-10-17

13 proyectos, 11 con hallazgos (67 señales). Usé las 13 fichas de `estado/records/`, de la instantánea de hoy. Ninguna está en silencio: el mayor silencio son 8 días (PRY-203), y el umbral es 15.

Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-17), así que no los registré de nuevo. Resumen: Criterio produce borradores de trabajo, no decisiones ni asesoría. La verificación de cada dato es suya. Términos: https://www.josenanez.com/es/agents/criterio-pmo/legal

**Dónde quedó el informe (26 páginas, en `reportes/`):**
- `reportes/index.html` es la vista por campo, con la cadena de evidencia. Es para quien va a actuar.
- `reportes/decisiones.html` es la vista por decisión, con preguntas cerradas. Es para el patrocinador.
- También hay una página por proyecto (`PRY-199.html` a `PRY-211.html`) y una por producto.
- El PDF sale de imprimir el HTML.

**Qué cambió:** nada. La única instantánea previa es la de hoy, así que este es el punto de partida y no hay delta.

**Hallazgos principales:**
- **Verdes sin sustento:** 8 proyectos declaran verde y la evidencia no lo sostiene: PRY-200, 201, 202, 204, 205, 207, 210 y 211.
- **Hitos declarados cumplidos sin documento que lo respalde:** 20 hitos, repartidos en 8 proyectos. PRY-205 declara los 5 hitos cumplidos y solo un 27 % de avance.
- **Hito vencido:** PRY-202, "Piloto con usuarios internos", venció hace 4 días.
- **Desviación contra la línea base original:** PRY-201 va +107 días y +24,2 % en costo, PRY-205 +80 días, PRY-207 +58 días y PRY-208 +57 días. En PRY-201, 205 y 207 la línea base se movió sin autorización.
- **Costo por encima del aprobado:** PRY-204 (+23,5 %), PRY-209 (+20,6 %) y PRY-207 (+18,4 %), además de PRY-201.
- **Proveedor:** en PRY-209, Integra Sistemas Ltda. facturó COP 365.708.982 más de lo aceptado.
- **Compromisos:** 10 vencidos, 8 de ellos en PRY-205. Tres compromisos de PRY-205 se han reprogramado entre 3 y 6 veces.
- **Vacíos:** ninguno de los 13 proyectos tiene autoridad aprobadora registrada, y PRY-202, 205, 208 y 210 no tienen producto asociado.

**Limitaciones:**
- La sección de dependencias en riesgo queda vacía porque el cálculo no emitió ninguna señal de dependencia.
- No hay preguntas de confirmación mensual: ningún comando de este flujo elige los 5 campos y no los inventé. Queda pendiente para la próxima corrida.
- En la tabla de estado general, "—" significa que el cálculo no contrastó un semáforo verde en ese proyecto. No afirmo qué declara.

La corrida quedó registrada como `2026-10-17-portfolio-report-1`, con el texto completo en `estado/corridas/salida-portfolio-report.md`.

Si quiere, preparo el material de comité para el 2026-10-24 o entro al detalle de PRY-205, PRY-201 y PRY-209, que son los que más conviene mirar primero.