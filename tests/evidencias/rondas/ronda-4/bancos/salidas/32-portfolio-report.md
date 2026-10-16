# /criterio-portfolio:portfolio-report html

Informe de portafolio generado y corrida registrada (`2026-10-15-portfolio-report-1`).

**Antes de producir nada**
- **Fichas:** 13, todas con barrido del 2026-10-15, así que ninguna está vieja.
- **Términos:** ya estaban vigentes (versión 1.1, aceptada por José Francisco Ñáñez el 2026-10-15), así que no hubo que registrarlos de nuevo. Resumen: Criterio produce borradores de trabajo, no decisiones ni asesoría, y la verificación de cada dato es suya. Nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

**Qué cambió:** nada. El diff contra la instantánea del 2026-10-15 dio 0 cambios.

**Lo que encontró el cruce:** 10 de 13 proyectos tienen hallazgos, 60 señales en total.
- **Verdes contradichos:** PRY-206, PRY-209, PRY-210 y PRY-211 declaran verde y la evidencia no lo sostiene.
- **PRY-210:** tiene 18 señales, entre ellas una replanificación de 41 días sin autorización. La fecha fin también se contradice: 2027-04-11 en el cronograma del PMO (más reciente) y 2027-04-24 en el acta.
- **Datacore Colombia:** atrasa entregables en PRY-204 y PRY-208. En PRY-208 hay 105.076.622 facturados sin entrega.
- **Hitos vencidos:** PRY-202 (ambiente de pruebas, 9 días) y PRY-208 (piloto, 4 días).
- **Hitos declarados cumplidos sin evidencia:** 20 señales, repartidas en 10 proyectos.
- **Vacíos:** los 13 proyectos no tienen autoridad registrada, PRY-203 no tiene línea base y PRY-202, 205, 208 y 210 no tienen producto asociado.
- **Proyectos en silencio:** ninguno.
- **Confirmación del mes:** no la hice. En el informe puse que no toca porque no hay una confirmación previa que vencer. Esa explicación es mía, no sale del script.

**Archivos:** 26 páginas en `/home/claude/banco/ronda-4/bancos/espacio/reportes/`.
- `index.html` es la vista por campo, con la cadena de evidencia, para quien va a actuar.
- `decisiones.html` es la vista por decisión, para el patrocinador en el comité del 2026-10-22.
- Hay además una página por proyecto. El PDF sale de imprimir el HTML.

**Un tropiezo:** la primera vez el informe quedó en `estado/reportes`, porque el directorio de trabajo había cambiado. Borré esa carpeta, que era de esta corrida, y lo regenerado quedó en la ruta correcta.

La salida completa de la corrida está en `estado/corridas/salida-portfolio-report.md`.