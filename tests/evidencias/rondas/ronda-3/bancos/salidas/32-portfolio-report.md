# /criterio-portfolio:portfolio-report html

El informe de portafolio está generado en HTML y la corrida quedó registrada como `2026-10-15-portfolio-report-1`. Cargué 13 fichas del barrido del 2026-10-15, y ninguna tiene más de una semana.

**Términos:** ya estaban vigentes (versión 1.1, aceptados por José Francisco Ñáñez el 2026-10-15), así que no los volví a registrar.

**Qué cambió:** nada que comparar. La única instantánea es la de hoy, así que esta corrida es el punto de partida y no hay delta.

**Hallazgos:** 11 de los 13 proyectos tienen hallazgos, 68 señales en total. Solo PRY-199 y PRY-203 salen limpios.
- **Verdes contradichos:** 7 proyectos se declaran en verde y las señales lo desmienten (PRY-201, 202, 206, 208, 209, 210 y 211).
- **Hitos sin evidencia:** 25 hitos figuran como cumplidos sin documento que lo respalde. Además, el hito "Integración con el core" de PRY-204 venció hace 7 días.
- **PRY-209:** corrió su línea base 32 días sin ninguna autorización. Declara verde, tiene "Salida a producción" sin evidencia y dos entregables de proveedor vencidos.
- **PRY-202:** lleva 66 días de atraso contra el plan original y +25,1% de costo, y también declara verde.
- **PRY-207:** tiene 12 señales, sobre todo compromisos: 6 vencidos, 2 sin fecha y 2 reprogramadas 4 y 6 veces. Además, el cronograma da fin 2027-08-10 y el acta 2027-11-03, ambos del mismo día.
- **PRY-201:** lleva 24 días en silencio, con +13,5% de costo proyectado.
- **Proveedor compartido:** Redes del Norte tiene entregables vencidos en PRY-204 y PRY-209.
- **Vacíos:** ningún proyecto tiene autoridad de aprobación identificada, y cuatro no tienen producto asociado.
- **Dependencias entre proyectos:** no hay ninguna declarada en las fichas, así que no pude cruzarlas.

**Confirmaciones del mes:** nadie respondió en esta sesión, así que dejé tres preguntas cerradas para el comité del 2026-10-21 en lugar de cinco campos. Son las fechas de fin de PRY-207, la autorización del corrimiento de PRY-209 y la evidencia de su salida a producción.

**Archivos** (en `/home/claude/banco/ronda-3/bancos/espacio/reportes`, 26 páginas):
- `index.html` — vista por campo, con la cadena de evidencia completa. Es para quien va a actuar.
- `decisiones.html` — vista por decisión, para el patrocinador y el comité.
- Para sacar el PDF se imprime el HTML.
- Lo que te mostré está guardado en `estado/corridas/salida-portfolio-report.md`.

El pie del informe lleva la versión 0.3.9, las 13 fichas aplicadas, los campos inciertos y el enlace a los términos.

Si hay comité próximo, puedo armar el material con `steering-pack`, o entrar al detalle de PRY-209 o PRY-207.