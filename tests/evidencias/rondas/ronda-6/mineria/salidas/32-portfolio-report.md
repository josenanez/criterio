# /criterio-portfolio:portfolio-report html

# Portafolio — 2026-10-16

13 proyectos, 9 con hallazgos. Cargué las 13 fichas, todas del 2026-10-16, así que no hay fichas viejas. Los términos ya estaban vigentes (versión 1.1, aceptados por José Francisco Ñáñez el 2026-10-16). No los registré de nuevo.

**Qué cambió:** no hay delta. Solo existe la instantánea de hoy, así que esta corrida es el punto de partida.

**Hallazgos principales (60 alertas en total):**
- **Verdes que la evidencia no sostiene:** PRY-201, PRY-203, PRY-205 y PRY-207.
  - PRY-203 lleva 120 días de atraso (50,6 %) y una replanificación no autorizada.
  - PRY-205 tiene 7 compromisos vencidos. Uno se reprogramó 6 veces.
  - PRY-207 tiene facturado por encima de lo aceptado y termina el 2026-10-19.
- **Hitos sin sustento:** 20 hitos declarados como cumplidos no tienen evidencia. Además, el hito «Pruebas en operación» de PRY-204 venció hace 4 días sin cumplirse.
- **Sobrecosto proyectado:** PRY-209 en 24,9 % y PRY-211 en 17,9 %.
- **Sin hallazgos:** PRY-199, PRY-200, PRY-206 y PRY-208.
- **Secciones vacías:** no hay proyectos en silencio (el máximo es PRY-211 con 8 días). Tampoco hay contradicciones entre documentos ni dependencias declaradas. Lo comprobé en las fichas.
- **Campos inciertos:** ningún proyecto tiene autoridad ni fase registradas. Siete proyectos no tienen producto asociado: PRY-201, 202, 205, 206, 209, 210 y 211.

**Dónde quedó el informe:** `/home/claude/banco/ronda-6/mineria/espacio/reportes/` (23 páginas).
- **`index.html`:** vista por campo, con la cadena de evidencia. Es para el gerente de PMO.
- **`decisiones.html`:** vista por decisión. Es para el patrocinador y el comité.
- **Páginas por proyecto:** una por proyecto, de `PRY-199.html` a `PRY-211.html`.
- **PDF:** sale de imprimir el HTML.

**Dos avisos:**
- La primera vez generé el informe sin querer en `estado/reportes`, porque la carpeta de trabajo había cambiado. Borré esa copia y lo regeneré en `reportes/`.
- El formato configurado es `pptx`. Esta corrida usó `html` por el argumento.

**Confirmaciones del mes:** las cinco preguntas cerradas quedaron pendientes, porque nadie podía responder. Son sobre la identidad y el patrocinador de PRY-203 y el patrocinador de PRY-210.

**Corrida registrada:** `estado/corridas/2026-10-16-portfolio-report-1.md`. Lo que mostré está en `estado/corridas/salida-portfolio-report.md`.

Pie: criterio-portfolio 0.3.12. Fichas aplicadas: 13, del 2026-10-16. Términos: https://www.josenanez.com/es/agents/criterio-pmo/legal

Puedo preparar el material de comité para el 2026-10-19, o entrar al detalle de PRY-203, PRY-205 y PRY-207.