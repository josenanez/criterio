# /criterio-portfolio:portfolio-report html

El informe de portafolio en HTML está generado y la corrida quedó registrada como `2026-10-17-portfolio-report-1`.

Los términos ya estaban vigentes (versión 1.1), aceptados por José Francisco Ñáñez el 2026-10-17. Las 13 fichas de `estado/records/` son de hoy, así que ninguna está vencida.

**Qué encontró**
- **Cambios:** no hay delta. La única instantánea previa es de hoy, así que esta corrida es el punto de partida.
- **Alcance:** 90 señales en 11 de los 13 proyectos. PRY-199 y PRY-207 no tienen ninguna.
- **Verdes contradichos:** 9 proyectos declaran verde y las señales lo contradicen: PRY-200, 201, 202, 203, 204, 205, 206, 210 y 211.
- **PRY-203 Reposición automática:** declara verde en su informe del 2026-10-15, pero acumula 26 señales. Entre ellas, el proveedor facturó 22.377.121 COP más de lo aceptado y hay 8 compromisos vencidos.
- **Replanificaciones sin autorización:** PRY-201, 202, 209 y 211.
- **Hitos y silencio:** hay 28 hitos dados por cumplidos sin evidencia y 1 hito vencido (PRY-203). Ningún proyecto supera los 15 días de silencio.
- **Autoridad:** los 13 proyectos no tienen autoridad de aprobación identificada.

**Qué no cubre**
- El informe no calculó dependencias entre proyectos, y no detalló el hito vencido de PRY-203 en la salida.
- En la tabla de estado general, algunos proyectos quedaron con "—" en "Declarado" porque la salida resumida que leí no traía ese dato.
- No toca la confirmación mensual de campos este mes.

**Dónde están los archivos**
- Los HTML están en `/home/claude/banco/ronda-9/retail/espacio/reportes/`: 24 páginas, con una por proyecto y páginas de producto. `index.html` es para quien va a actuar; `decisiones.html` es para el patrocinador.
- El PDF sale de imprimir el HTML.
- La salida de la corrida está en `/home/claude/banco/ronda-9/retail/espacio/estado/corridas/salida-portfolio-report.md`.

Si hay comité próximo (el 2026-10-23 según la configuración), puedo preparar el material de comité o entrar al detalle de PRY-203.