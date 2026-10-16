# /criterio-portfolio:portfolio-report html

El informe HTML del portafolio quedó generado en `/home/claude/banco/ronda-5/bancos/espacio/reportes/`, y la corrida quedó registrada como `2026-10-16-portfolio-report-1`. Cubre los 13 proyectos con fichas del 2026-10-16: 10 tienen hallazgos y suman 50 señales. La corrida midió 50 segundos y 72 documentos, ninguno releído.

**Qué cambió.** Nada. La única instantánea previa es la de hoy, así que este informe es el punto de partida y no hay delta histórico.

**Seis proyectos declaran verde y las señales lo contradicen:**
- **PRY-202:** declara 24% de avance cuando el plan sostiene entre 50% y 75%. Además tiene un hito vencido y otro marcado como cumplido sin evidencia.
- **PRY-204:** declara 71% cuando el plan sostiene 100%. Va 31 días atrasado, tiene 3 hitos cumplidos sin evidencia y un compromiso vencido.
- **PRY-206:** declara 62% cuando el plan sostiene 100%. Tiene 3 hitos cumplidos sin evidencia, el más viejo de hace 373 días.
- **PRY-207:** lleva 22 días en silencio, con el umbral en 15.
- **PRY-210:** tiene "Diseño funcional aprobado" marcado como cumplido hace 115 días y sin documento que lo respalde.
- **PRY-211:** tiene 7 compromisos vencidos, dos reprogramados 4 y 6 veces, y el costo proyectado va 15,5% por encima del aprobado.

**Otros hallazgos:**
- **PRY-200:** la línea base se movió 139 días sin autorización registrada. El tiempo va 36% por encima del original y el costo 10,6%.
- **PRY-211:** el cronograma dice que termina el 2026-12-25 y el acta dice 2027-03-01, ambos con fecha 2025-07-08. No se puede saber cuál manda.
- **Costo:** PRY-203 va 26,8% por encima y PRY-208 va 23%.
- **Sin señales:** PRY-199, PRY-205 y PRY-209.

**Dos vacíos de datos.** Los 13 proyectos no tienen autoridad registrada, y cuatro (PRY-202, 205, 208 y 210) no tienen producto asociado.

**Qué vista va a quién.** `index.html` es por campo, con la cadena de evidencia completa, para quien va a actuar. `decisiones.html` es por decisión, para el patrocinador. El PDF sale de imprimir el HTML.

**Otros puntos:**
- **Términos:** ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-16), así que no los registré de nuevo.
- **Carpeta de fichas:** la configuración apunta a `estado/fichas/`, que no existe; leí las fichas de `estado/records/`.
- **Formato:** la configuración dice `presentation` y usé `html` porque lo pediste.
- **Confirmación mensual:** no la hice, porque la sesión no tiene interfaz y nadie podía responder.

El comité próximo es el 2026-10-21. Puedo preparar el material con `/criterio-portfolio:steering-pack` o entrar al detalle de PRY-211, PRY-200 y PRY-204.

El texto completo de la salida quedó en `/home/claude/banco/ronda-5/bancos/espacio/estado/corridas/salida-portfolio-report.md`. Pie: criterio-portfolio 0.3.11; términos en https://www.josenanez.com/es/agents/criterio-pmo/legal#v0.3.11.