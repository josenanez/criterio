# /criterio-portfolio:portfolio-report html

Generé el informe HTML del portafolio y registré la corrida como `2026-10-16-portfolio-report-1`. Cargué 13 fichas de `estado/records/` (PRY-199 a PRY-211), todas del 2026-10-16. Los términos estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-16), así que no los registré de nuevo.

**Qué cambió:** nada. La única instantánea es la de hoy, así que este informe es el punto de partida y no hay delta que reportar.

**Hallazgos:** hay 52 señales en 10 de los 13 proyectos, y 8 de los 13 declaran verde con señales que lo contradicen.
- **PRY-210 Corresponsales rurales:** 12 señales. Tiene 3 compromisos vencidos (hasta 24 días), 2 reprogramados 4 y 5 veces, 4 sin fecha y el hito de diseño vencido. Declara 47 % de avance con 0 de 4 hitos cumplidos.
- **PRY-204 Tarjeta débito:** 10 señales.
  - La proyección de costo supera lo aprobado en 11,2 %.
  - Los dos proveedores tienen un entregable tardío (73 días).
  - Integración Financiera del Sur facturó $152.173.835 más de lo aceptado.
- **PRY-208 Motor de crédito:** movió la línea base 161 días (+48,3 %) sin autorización y tiene un compromiso vencido.
- **PRY-202 Core cooperativo:** su hito "Piloto con asociados" venció hace 7 días.
- **Hitos cumplidos sin evidencia:** hay 19, en 9 proyectos.

**Vacíos de datos:**
- **Autoridad y fase:** faltan en los 13 proyectos.
- **Producto:** falta en 5.
- **Datos viejos:** 4 proyectos tienen campos con fuente de 12 a 17 meses.
- **Evidencia:** ningún dato de las fichas está marcado como evidencia; todo es declaración o sin marcar.

Hay cuatro secciones vacías, y el informe lo dice en cada una: contradicciones, proyectos en silencio, dependencias declaradas y cambios de gobierno.

La sección "Necesito que confirmes" quedó con cinco preguntas abiertas porque nadie podía responder en esta sesión. Cuatro piden confirmar una fecha de fin o el patrocinador de proyectos con fuente de 12 a 17 meses. La quinta pregunta quién es la autoridad de PRY-208.

El formato configurado es `pptx`; usé `html` por el argumento.

El informe está en `reportes/` (25 páginas, una por proyecto y por producto). Cada vista va a una audiencia distinta:
- **`reportes/index.html`:** por campo, con la cadena de evidencia completa. Es para quien va a actuar.
- **`reportes/decisiones.html`:** por decisión, para el patrocinador. No es la anterior recortada.

Para sacar un PDF, imprime el HTML.

Lo que te mostré quedó guardado en `estado/corridas/salida-portfolio-report.md`.

Si quieres, el siguiente paso es el material de comité para el 2026-10-30, o entrar al detalle de PRY-210, PRY-204 y PRY-208.

criterio-portfolio 0.3.12 · 13 fichas del 2026-10-16 · términos: https://www.josenanez.com/es/agents/criterio-pmo/legal#v0.3.12