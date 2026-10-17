# /criterio-portfolio:portfolio-report html

# Portafolio — 2026-10-17

Generé el informe HTML y registré la corrida como `2026-10-17-portfolio-report-1`. Cubre 13 proyectos, 6 productos y 86 señales; 12 de los 13 proyectos tienen hallazgos (el único limpio es PRY-199).

**Términos:** ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-17), así que no volví a registrarlos. Texto completo: https://www.josenanez.com/es/agents/criterio-pmo/legal

**Fichas:** las 13 son de hoy, ninguna tiene más de una semana.

**Qué cambió:** nada. La única instantánea anterior es de hoy, así que no hay comparación real.

**Hallazgos principales:**
- **Verdes contradichos:** 7 proyectos se declaran en verde y la evidencia no lo sostiene: PRY-201, 202, 204, 205, 207, 209 y 210.
- **Hitos sin evidencia:** 31 hitos figuran como cumplidos sin documento que lo respalde, en 11 proyectos. PRY-203, 204 y 206 los tienen todos sin evidencia (5 de 5).
- **PRY-202 (Planta de tratamiento de agua):** atraso de 115 días (25,8%), sobrecosto proyectado de 28,9% y 5 compromisos vencidos.
- **PRY-211 (Control de polvo en vías):** sobrecosto proyectado de 20,3%.
- **Geotecnia Aplicada S.A.S.:** aparece facturando sin entrega en PRY-201, 207 y 208, y el proveedor Ingeniería Minera del Sur lo hace en PRY-204.
- **PRY-205:** corrió la línea base 75 días sin autorización.
- **Vacíos:** falta la autoridad de proyecto en los 13, y el producto asociado en 7.

**Archivos:** quedaron en `reportes/`, dentro de `/home/claude/banco/ronda-7/mineria/espacio`, 23 páginas en total.
- `index.html`: vista por campo, con la cadena de evidencia. Es para quien va a actuar.
- `decisiones.html`: vista por decisión. Es para el patrocinador.
- Hay además una página por proyecto y por producto. El PDF sale de imprimir el HTML.

**Confirmaciones del mes:** como no hay interfaz, dejé las cinco preguntas en la salida de la corrida sin respuesta. Son la autoridad de los proyectos, dos patrocinadores con datos de más de 12 meses, la aprobación del corrimiento de PRY-205 y el producto de cinco proyectos.

**Errores corregidos:**
- Al registrar la corrida, mi texto decía 26 hitos sin evidencia; el script cuenta 31. Corregí `salida-portfolio-report.md` y el registro de la corrida.
- El sistema avisó después de mis cambios que `salida-portfolio-report.md` cambió en disco; no la releí.
- No puse "último documento" en la tabla de hitos vencidos, porque no lo calculé.

Pie: criterio-portfolio 0.3.13 · fichas del 2026-10-17 · campos inciertos: autoridad, fase y evidencia de hitos.