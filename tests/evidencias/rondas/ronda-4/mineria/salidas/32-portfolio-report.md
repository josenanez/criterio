# /criterio-portfolio:portfolio-report html

El informe HTML está generado: 23 páginas en `/home/claude/banco/ronda-4/mineria/espacio/reportes/`, y la corrida quedó registrada como `2026-10-15-portfolio-report-1`.

Las fichas están en `estado/records/` (PRY-199 a PRY-211), no en `estado/fichas/`, así que las leí de ahí. Todas tienen fecha de hoy, 2026-10-15.

**Términos:** ya estaban vigentes (versión 1.1, aceptada por José Francisco Ñáñez el 2026-10-15), así que no registré nada nuevo.

**Qué cambió:** nada. El diff contra la instantánea anterior dio 0 cambios, porque la instantánea es de hoy.

**Hallazgos:** 10 de 13 proyectos tienen señales, 51 en total.
- **Verdes contradichos:** cuatro proyectos declarados en verde los contradice la evidencia: PRY-201, 202, 203 y 206.
- **PRY-205:** se desvió 112 días contra la línea base original y tiene una replanificación sin autorización.
- **PRY-200:** concentra 18 señales (7 compromisos vencidos, 4 hitos cumplidos sin evidencia, un entregable de proveedor atrasado y otro aceptado sin evidencia).
- **Hitos sin evidencia:** hay 21 en total, repartidos en siete proyectos.
- **Sin señales:** PRY-199, 210 y 211.
- **Vacíos:** ningún proyecto tiene autoridad registrada, y siete no tienen producto asociado.
- **Silencio:** ningún proyecto supera el umbral de 15 días; el mayor es PRY-202, con 9.

**Qué vista va a quién:**
- **`reportes/index.html`:** va por campo, con la cadena de evidencia completa, para quien va a actuar.
- **`reportes/decisiones.html`:** va por decisión, para el patrocinador.
- **PDF:** se saca imprimiendo el HTML.

No hice las preguntas de confirmación mensual, porque no hay nadie que responda. Quedan para la próxima corrida con interlocutor. El resumen que le muestro está guardado en `estado/corridas/salida-portfolio-report.md`.

**Un tropiezo:** la primera generación fue a `estado/reportes/` porque mi directorio de trabajo había cambiado. Volví al directorio de la sesión, regeneré el informe en `reportes/` y borré la copia mal ubicada.

Si hay comité próximo, puedo preparar el paquete de comité (`/criterio-portfolio:steering-pack`).