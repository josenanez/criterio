# /criterio-project:pm-plan 

El borrador de plan de PRY-207 está hecho, pero el acta de constitución casi no da material para una WBS, así que la mayoría de los nodos quedan como supuesto o sin definir. No comprometí ninguna fecha.

Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-15), así que no los registré otra vez.

**Lo que le falta al acta:**
- **Alcance:** dice «Componente 1, 2, 3» sin nombrar ningún entregable, y el «fuera de alcance» está igual de vacío.
- **Criterio de éxito:** «en producción y medido» no dice qué métrica ni qué umbral.
- **Autoridad:** no declara qué puede decidir el gerente.
- **Dependencias:** dice «Ninguna declarada», pero el informe del 2026-10-13 menciona el calendario de liberaciones del core.
- **Hueco de fechas:** entre el último hito (2027-08-10) y el cierre (2027-11-03) no hay nada nombrado.

**WBS:** solo tres entregables son citables, y vienen del cronograma v1, no del acta: diseño funcional (cerrado el 2026-09-04), ambiente de pruebas certificado (2027-02-21) e integración con el core (2027-08-10). Cuatro nodos más van como supuesto o sin definir: pruebas, salida a producción, medición y los «Componentes 1 a 3». Ningún nodo tiene quién lo acepta, porque el acta no lo dice. Las duraciones quedaron vacías.

**Orden:** va sin fechas. La integración con el core condiciona la salida a producción.

**Proyectos análogos:** ninguno. La configuración no apunta a una carpeta de fichas de la PMO, y no leí PRY-199 a PRY-211 como análogos. Sin análogos no hay referencia de duración.

**Preguntas para el equipo:** dejé siete, una por cada duración vacía. Una de ellas es si el proveedor llega con el equipo completo a la siguiente fase; salió en la reunión del 2026-10-15 y nadie la registró como riesgo.

**Para comprometer una fecha falta:** la disponibilidad del equipo y del proveedor, la ventana de cambio de operaciones, el calendario del core y la definición del alcance. Además, el informe proyecta 7.058.214.079 COP al cierre contra 6.800.000.000 aprobados.

La corrida quedó registrada como `2026-10-15-pm-plan-1`; la señal que arrojó son dos compromisos, uno reprogramado y otro sin fecha.

Archivos están en `/home/claude/banco/ronda-3/bancos/espacio/estado/PRY-207-onboarding-pyme/corridas/`:
- `salida-pm-plan.md`