# /criterio-portfolio:portfolio-report html

Generé el informe de portafolio en HTML: 27 páginas para 13 proyectos, en `/home/claude/banco/ronda-1/bancos/espacio/reportes`. Los términos de uso ya estaban aceptados en la versión 1.0, así que no hubo que pedirlos de nuevo.

**Qué cargué:** las 13 fichas de `estado/records/`, todas con fecha 2026-10-14. Ninguna tiene más de una semana, así que no hizo falta un barrido previo.

**Qué cambió:** nada. La instantánea anterior es de hoy, así que esta corrida no tiene un punto de comparación real.

**Qué encontró:** 10 de 13 proyectos tienen hallazgos, 54 señales en total. Lo más grave:
- **Verde contradicho:** 6 proyectos se declaran en verde y la evidencia lo contradice (PRY-201, 207, 208, 209, 210 y 211).
- **Hitos sin evidencia:** hay 23 hitos declarados como cumplidos que no tienen evidencia. El más viejo es de PRY-210, con 415 días.
- **PRY-203:** lleva +112 días de atraso contra el plan original. Además, el proveedor Datacore Colombia tiene 3 entregables atrasados y 631.036.273 facturados sin entrega.
- **PRY-205:** +101 días de atraso, y el movimiento de línea base no tiene autorización. PRY-208 también replanificó sin autorización, por 21 días.
- **PRY-207:** proyecta un costo 22,9 % por encima del aprobado, y el cambio CC-01 no tiene línea base.
- **PRY-202:** la fecha de fin tiene dos valores, 2026-09-25 en el cronograma y 2026-10-16 en el acta.
- **PRY-209:** lleva 16 días en silencio.

**Qué vista va a quién:**
- `reportes/index.html` es la vista por campo, con la cadena de evidencia. Es para quien va a actuar.
- `reportes/decisiones.html` es la vista por decisión. Es para el patrocinador, antes del comité del 2026-10-20.

Para imprimir en PDF, se imprime el HTML.

**Pendientes y límites:**
- Ninguno de los 13 proyectos tiene una autoridad de aprobación registrada.
- No hice la confirmación mensual de cinco campos porque la sesión es sin interfaz.
- Dejé guardado lo que te muestro aquí en `estado/corridas/salida-portfolio-report.md` y registré la corrida como `2026-10-14-portfolio-report-1`.