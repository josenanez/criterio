# /criterio-portfolio:portfolio-report html

Generé el informe HTML del portafolio y dejé la corrida registrada. Los términos v1.2 ya estaban vigentes, aceptados por José Francisco Ñáñez el 2026-10-23, así que no los registré de nuevo.

**Base:** 13 fichas, todas barridas el 2026-10-23. El mayor silencio es de 11 días, por debajo del umbral de 15.

**Qué cambió:** nada. El diff se calculó contra la instantánea del mismo día y dio 0 cambios, así que hoy no hay delta.

**Hallazgos:** 10 de los 13 proyectos tienen señales, 58 en total.
- **Contradicciones:** PRY-200 y PRY-207 declaran verde, pero tienen hitos "cumplidos" sin acta de recibo.
- **Hitos sin evidencia:** 23 hitos declarados cumplidos, sobre todo en PRY-204, 205, 209 y 211.
- **Avance bajo:** en PRY-204, 205, 209 y 211 el avance declarado queda muy por debajo de lo que sostiene el plan, con brechas de 42 a 75 puntos. Puede ser que el avance esté subdeclarado o que los hitos estén sobredeclarados.
- **PRY-209 (Migración del ERP):** lleva +95 días (48,2 %) por una replanificación sin ningún cambio autorizado. Además tiene dos entregables aceptados sin evidencia.
- **PRY-205 (Pago con QR):** el cambio CC-01 de 42 días se aplicó sin línea base nueva.
- **PRY-206 (Precios dinámicos):** el costo proyectado supera lo aprobado en 17,5 %.
- **PRY-202 (Centro de distribución norte):** tiene 6 compromisos vencidos, 2 sin fecha y 3 reprogramados entre 3 y 6 veces.
- **Proveedores:** Sistemas Comerciales del Norte tiene entregables atrasados en PRY-201, 209 y 210. El licenciamiento de PRY-201 lleva más de 250 días vencido con dos proveedores.
- **Vacíos:** ningún proyecto tiene autoridad registrada, y 6 no tienen producto asociado.

**Confirmación mensual:** toca, pero en esta sesión sin interfaz las cinco preguntas cerradas quedan sin responder. Están al final de la salida guardada.

**Dónde quedó, en `reportes/`:**
- `index.html`: vista por campo con la cadena de evidencia. Es para quien va a actuar.
- `decisiones.html`: vista por decisión. Es para el patrocinador y el comité del 2026-11-06.
- Una página por proyecto y páginas por producto, 24 en total.
- Para sacar el PDF, imprime el HTML desde el navegador.

**Salida y registro de la corrida:**
- La salida completa está en `estado/corridas/salida-portfolio-report.md`.
- La corrida quedó registrada como `2026-10-23-portfolio-report-1` y tardó 113 segundos.

**Una discrepancia:** sumando las señales de mi tabla por proyecto me salen 57, y el script cuenta 58. No encontré la diferencia. El total de 58 y el conteo por señal vienen del script.

**Pie:** criterio-portfolio v0.8.0. Fichas aplicadas: 13, del 2026-10-23. Campos inciertos: autoridad sin registrar en los 13 proyectos y 6 sin producto. Términos: https://www.josenanez.com/es/agents/criterio-pmo/legal#v0.8.0

Puedo preparar el material del comité del 2026-11-06 con `/steering-pack`, o entrar al detalle de PRY-202, PRY-209 o PRY-201.