# /criterio-portfolio:portfolio-report html

# Portafolio — 2026-10-15

Cargué las 13 fichas de `estado/records/`, todas del barrido de hoy. Ninguna tiene más de una semana, así que no hizo falta un `/portfolio-scan` antes.

Los términos ya estaban vigentes (versión 0.3.10, aceptados por José Francisco Ñáñez el 2026-10-15), así que no los volví a registrar. En corto: Criterio produce borradores de trabajo, no decisiones. La verificación de cada dato es suya, con la cita del documento. Términos: https://www.josenanez.com/es/agents/criterio-pmo/legal#v0.3.10

**Qué cambió:** nada. Es la única instantánea (la de hoy), así que esto es el punto de partida y no hay delta.

**Lo que muestra el cálculo:** 56 alertas en 9 de los 13 proyectos.

- **Cinco proyectos declaran verde y las señales lo contradicen:**
  - **PRY-200:** declara 76% de avance, pero 3 hitos cumplidos no tienen evidencia.
  - **PRY-203:** 5 hitos sin evidencia, 4 entregables del proveedor atrasados y 459.463.652 facturados sin entrega.
  - **PRY-204:** sobrecosto proyectado de 11,8% y un compromiso vencido.
  - **PRY-205:** sobrecosto de 15,7%, un entregable del proveedor con 66 días de atraso y un compromiso vencido.
  - **PRY-211:** sobrecosto de 13,7% y un compromiso vencido hace 20 días.
- **Contradicción abierta:** PRY-209 tiene dos fechas de fin, 2027-02-03 en el cronograma y 2027-03-06 en el acta. Ambos documentos son del 2026-05-28, así que no se puede saber cuál es la vigente.
- **PRY-209, además:** tiene un hito vencido hace 10 días y 4 compromisos vencidos. Dos compromisos se han reprogramado 6 y 5 veces.
- **Proyectos en silencio:** ninguno. El más callado es PRY-206, con 12 días.
- **Vacíos:** ningún proyecto tiene autoridad identificada, y 6 no están asociados a un producto (PRY-202, 203, 206, 209, 210, 211).

**Dónde quedó el informe** (24 páginas en `/home/claude/banco/ronda-4/retail/espacio/reportes/`):
- `index.html` es la vista por campo, con la cadena de evidencia. Va para quien va a actuar, que es el gerente de PMO y los gerentes de proyecto.
- `decisiones.html` es la vista por decisión, solo con lo que excede la facultad del gerente. Va para el patrocinador y el comité del 2026-10-29.
- Además hay una página por proyecto y por producto. Para sacar un PDF, imprima el HTML desde el navegador.

La primera vez el informe cayó en `estado/reportes` porque corrí el script desde otro directorio. Lo regeneré en la carpeta configurada y borré la copia mal ubicada.

**Necesito que confirmes:** este mes no toca confirmación, así que no hay preguntas.

La corrida quedó registrada como `2026-10-15-portfolio-report-1`, con el detalle en `estado/corridas/salida-portfolio-report.md`. Tardó 46 segundos y se leyeron 66 documentos sin cambios.

Pie: criterio-portfolio 0.3.10 · fichas del 2026-10-15 · campo incierto: fecha de fin de PRY-209.

Siguiente paso: puedo armar el material para el comité del 29 de octubre con `/steering-pack`, o entrar al detalle de los cinco verdes contradichos.