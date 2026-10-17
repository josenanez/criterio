# /criterio-portfolio:portfolio-report html

El informe del portafolio en HTML está generado y la corrida quedó registrada como `2026-10-17-portfolio-report-1`. El script produjo 26 páginas en `/home/claude/banco/ronda-8/bancos/espacio/reportes/`.

Los términos v1.1 ya estaban aceptados por José Francisco Ñáñez el 2026-10-17, así que no hubo que registrarlos de nuevo. Cargué las 13 fichas, todas del barrido del 2026-10-17. Están en `estado/records/`, porque `estado/fichas/` no existe.

**Qué va a quién**
- **`index.html`:** va por campo, con la cadena de evidencia completa. Es para quien va a actuar.
- **`decisiones.html`:** va por decisión, solo lo que excede la facultad de quien gerencia. Es para el patrocinador.
- **PDF:** sale de imprimir el HTML desde el navegador.

**Qué muestra**
- **Delta:** no hay. La instantánea anterior es del mismo día, así que el diff da 0 cambios. Esto es el punto de partida.
- **Alcance:** 13 proyectos, 11 con hallazgos y 60 señales en total.
- **Verdes sin sustento:** PRY-200, 203, 209 y 211 se declaran en verde contra la evidencia.
  - PRY-200: 23 días en silencio y avance de 29% frente a 75–100% que sostiene el plan.
  - PRY-203: sobrecosto proyectado de 19,1%.
  - PRY-209: sobrecosto proyectado de 10,0%.
  - PRY-211: dos hitos declarados cumplidos sin evidencia.
- **Hitos:** hay 20 declarados cumplidos sin evidencia. PRY-210 tiene 4 y PRY-205 tiene 3, con hasta 461 días de vencimiento.
- **PRY-202:** acumula 17 hallazgos.
  - Un corrimiento de 76 días (14,7%) sin cambio autorizado.
  - Seis compromisos vencidos.
  - Dos compromisos reprogramados 5 o 6 veces.
- **Sobrecostos:** PRY-208 va en +26,9%.
- **Proveedores:** hay entregables vencidos y "bolsas de horas" aceptadas sin evidencia en PRY-202, 208 y 210.
- **Vacíos:** ninguna ficha de los 13 tiene autoridad que apruebe el proyecto, y cuatro proyectos no tienen producto asociado (PRY-202, 205, 208 y 210).

El script no reportó contradicciones entre fuentes ni dependencias rotas, y lo dejé escrito como secciones vacías. No hay preguntas de confirmación este mes, porque es la primera corrida y ningún campo supera los 12 meses de antigüedad.

El texto completo del informe está en `estado/corridas/salida-portfolio-report.md`. Queda ofrecido el material de comité (el próximo es el 2026-10-20) o entrar al detalle de PRY-202, 203 y 208.