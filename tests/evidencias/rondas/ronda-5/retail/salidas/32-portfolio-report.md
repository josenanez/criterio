# /criterio-portfolio:portfolio-report html

Generé el informe de portafolio en HTML: 13 proyectos, 11 con hallazgos y 54 señales. Cargué las fichas de `estado/records/` (la carpeta `estado/fichas/` no existe), todas con barrido de hoy, 2026-10-16.

Los términos ya estaban vigentes (versión 1.1, aceptados por José Francisco Ñáñez el 2026-10-16), así que no volví a registrarlos.

**Qué cambió:** nada. Solo hay una instantánea, la de hoy, y el diff dio 0 cambios.

**Hallazgos principales:**
- **Verdes contradichos (7):** PRY-200, 206, 207, 208, 209, 210 y 211 declaran verde y la evidencia lo contradice. Por ejemplo, PRY-200 declara 79% de avance con 0 de 3 hitos cumplidos y movió su línea base 27 días sin autorización.
- **PRY-209:**
  - Tiene 6 compromisos vencidos, el más viejo con 22 días.
  - Dos compromisos llevan 5 y 6 reprogramaciones.
  - Tiene dos fechas de fin: 2027-09-28 en el cronograma y 2027-12-02 en el acta.
- **Silencio:** PRY-210 lleva 20 días sin documentos, sobre el umbral de 15.
- **Hitos:** 2 vencidos sin evidencia (PRY-203 y PRY-204) y 13 declarados cumplidos sin respaldo.
- **Costo:** 5 proyectos superan el 10% de desviación (PRY-200, 202, 206, 208 y 211, entre +20,6% y +26,8%).
- **Atraso:** PRY-207 acumula 72 días contra la línea base original.
- **Vacíos:** los 13 proyectos no tienen patrocinador o decisor registrado, y 6 no tienen producto asociado.
- **Dependencias en riesgo:** ninguna detectada.

**Confirmación del mes:** dejé una sola pregunta cerrada, la de la fecha de fin de PRY-209. El script no eligió los cinco campos más viejos en esta corrida, así que no inventé el resto.

Los archivos están en `reportes/` (24 páginas):
- **`index.html`:** vista por campo, con la cadena de evidencia completa. Es para quien va a actuar.
- **`decisiones.html`:** vista por decisión. Es para el patrocinador.
- **Resto:** una página por proyecto y por producto. Para sacar PDF, imprime el HTML.

La corrida quedó registrada como `2026-10-16-portfolio-report-1`; el texto completo está en `estado/corridas/salida-portfolio-report.md`.

Pie: criterio-portfolio 0.3.11, fichas con barrido 2026-10-16, campo incierto: la fecha de fin de PRY-209. Términos: https://www.josenanez.com/es/agents/criterio-pmo/legal#v0.3.11

Si quieres, preparo el material de comité para el 2026-10-23 o entro al detalle de PRY-209.