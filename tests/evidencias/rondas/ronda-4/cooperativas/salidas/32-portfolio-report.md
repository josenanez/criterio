# /criterio-portfolio:portfolio-report html

# Portafolio — 2026-10-15

Generé el informe en HTML. Son 13 proyectos, 9 con hallazgos y 64 señales. Usé las fichas de `estado/records/`, que son 13 con fecha 2026-10-15. Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-15), así que no los registré de nuevo.

**Dónde quedaron los archivos** (`reportes/`):
- `index.html` es la vista por campo, con la cadena de evidencia. Es para quien va a actuar.
- `decisiones.html` es la vista por decisión. Es para el patrocinador.
- También hay una página por cada uno de los 13 proyectos, una por producto, `productos.html` y `proyectos.html`.
- El PDF sale de imprimir el HTML.

**Qué cambió:** nada. Solo existe la instantánea de hoy, así que no hay una anterior con la que comparar y esta corrida es el punto de partida.

**Lo más importante:**
- **Verdes contradichos (4):** PRY-202, PRY-206, PRY-209 y PRY-210 declaran verde y la evidencia lo contradice.
- **Replanificaciones sin autorización (2):**
  - PRY-203 se corrió 115 días y PRY-210 84 días.
  - En PRY-203 el acta dice que termina el 2027-05-30 y la PMO tiene 2027-07-06.
- **Costo sobre el umbral del 10%:** PRY-203 (+18,1%) y PRY-211 (+17,3%).
- **Silencio:** PRY-206 lleva 22 días sin documentos nuevos.
- **Proveedores:**
  - PRY-211: se facturaron COP 513.489.020 sin entrega.
  - PRY-210: se facturaron COP 26.507.177 más de lo aceptado.
- **Hitos declarados cumplidos sin evidencia:** hay 21 en total, 5 de ellos en PRY-200.
- **Sin señales:** PRY-199, PRY-201, PRY-204 y PRY-205.

**Límites de esta corrida:**
- Ningún proyecto tiene autoridad registrada, 13 de 13, y 5 proyectos no tienen producto asociado.
- No cruzé a mano dependencias, cambios de gobierno ni recursos repetidos. El cálculo del script no marcó dependencias rotas.
- La confirmación mensual de cinco campos no se hizo, porque en esta sesión nadie podía responder.
- La primera vez dejé el informe en `estado/reportes` porque mi directorio de trabajo había cambiado. Lo regeneré desde la raíz del espacio y borré esa copia.
- No pegué el HTML en la conversación.

La corrida quedó registrada como `2026-10-15-portfolio-report-1`, con la salida completa en `estado/corridas/salida-portfolio-report.md`. Tardó 41 segundos y no releyó ningún documento (82 sin cambios).

Pie: criterio-portfolio 0.3.10. Términos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal#v0.3.10

Puedo preparar el material de comité para el 2026-10-22 o entrar al detalle de los proyectos con hallazgos.