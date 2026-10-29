# /criterio-portfolio:portfolio-report html

El informe HTML quedó generado en `/home/claude/r12/telecomunicaciones/espacio/reportes/` y la corrida quedó registrada como `2026-10-28-portfolio-report-1`.

**Condiciones de la corrida**
- **Términos:** ya estaban vigentes (versión 0.12.1), aceptados por José Francisco Ñáñez el 2026-10-28, así que no los registré de nuevo.
- **Fichas:** cargué las 13 fichas de `estado/records`, todas de 2026-10-28. No hay fichas viejas.
- **Cambios:** no hay instantánea previa, así que es el punto de partida y no hay delta.
- **Medición:** 92 documentos sin cambio, ninguno releído, 42 segundos.
- **Salida guardada:** el texto del informe está en `estado/corridas/salida-portfolio-report.md`.

**Qué va a quién**
- `reportes/index.html` es la vista por campo, con la cadena de evidencia. Es para quien va a actuar.
- `reportes/decisiones.html` es la vista por decisión, para el patrocinador.
- Hay una página por proyecto (`PRY-199.html` a `PRY-211.html`) y páginas por producto. En total son 23 páginas.
- El PDF sale de imprimir el HTML.

**Hallazgos principales** (10 de 13 proyectos con señales; 70 en total)
- **Verdes contradichos:** PRY-201, PRY-202 y PRY-207 declaran verde, pero tienen hitos «cumplidos» sin evidencia y un avance declarado muy por debajo de lo que dice el plan.
- **Hitos sin evidencia:** hay 20 hitos declarados cumplidos sin evidencia en 9 proyectos.
- **Replanificaciones sin autorización:** PRY-206 (93 días), PRY-210 (110) y PRY-211 (102).
- **Costo:** PRY-210 proyecta +19,7 % sobre el presupuesto aprobado.
- **Proveedores:**
  - PRY-209: se facturó 1.164.831.714 sin entrega registrada.
  - PRY-206: se facturó 80.325.470 por encima de lo aceptado.
- **PRY-211:** es el más cargado, con 21 señales. Tiene 6 compromisos vencidos y 7 reprogramados, uno de ellos 6 veces.
- **Sin señales:** PRY-199, PRY-203 y PRY-208.
- **Gobierno:** ningún proyecto tiene autoridad registrada, y 7 no tienen producto asignado.

Dos cosas que no revisé. En el resumen del informe puse que `compute` no devolvió señales de dependencia ni campos viejos, pero no lo comprobé a mano. Los campos inciertos de las fichas tampoco los conté. Tras registrar la corrida corregí en el archivo guardado el total de hitos sin evidencia, que estaba en 17 y es 20.

No hay confirmaciones pendientes este mes. Si hay comité próximo (el 2026-11-04), puedo preparar el material con `steering-pack`.