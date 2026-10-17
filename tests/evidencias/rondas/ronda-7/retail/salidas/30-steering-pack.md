# /criterio-portfolio:steering-pack 

Preparé el paquete de comité con 7 decisiones, 6 escalamientos sin decisión y 61 señales en 10 de los 13 proyectos. Ningún proyecto tiene registrado quién aprueba cambios o sobrecostos, así que la decisión 1 es nombrarlo.

Usé las 13 fichas (PRY-199 a PRY-211) con estado al 2026-10-17. Las cifras salen de `compute` y no las derivé a mano. Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-17), así que no los registré de nuevo. No hubo preguntas que contestar.

**Decisiones**
1. **Quién tiene la facultad de aprobar.** `identity.authority` no se encontró en ninguna ficha. La recomendación es nombrar hoy un aprobador por proyecto.
2. **PRY-205, CC-01** (+75 días, +150.000.000 COP). La línea base v2 ya se movió sin autorización. El disponible real es 147.684.786 COP, menos que lo solicitado. Recomiendo aprobar con alcance recortado o rechazar.
3. **PRY-209, CC-01** (+55 días, +110.000.000 COP). Hay fondos, pero dos hitos cumplidos sin evidencia. Recomiendo aprobar condicionado a esa evidencia.
4. **PRY-211, pagos a proveedores.**
   - **Tecnología para Tiendas:** 723.840.453 COP facturados sin ningún entregable aceptado.
   - **Datos y Demanda:** 422.462.954 COP facturados por encima de lo aceptado.
   - **Recomendación:** detener ambas facturas.
5. **PRY-211, plan y presupuesto.** La proyección es 8.631.313.230 COP contra 6.800.000.000 aprobados (26.9%). Recomiendo exigir plan v2 y solicitud de cambio formal.
6. **PRY-202** (rojo). La proyección es 26.2% sobre lo aprobado. Recomiendo recortar alcance y exigir la solicitud de cambio.
7. **Cinco proyectos en verde contradichos por su evidencia** (PRY-204, 205, 206, 207, 211). Recomiendo pasarlos a `health-check`.

**Lo que el paquete dice que no sabe**
- **Comité anterior:** no hay registro de uno, así que la sección de decisiones previas queda en blanco.
- **Quién decide:** los puntos 2 a 7 dicen "no consta" en esa casilla.
- **Alcance recortado:** los documentos no dicen qué se recortaría en las decisiones 2 y 6; no lo inventé.
- **PRY-200:** está en rojo sin causa que el cálculo marque.

La salida completa quedó en `/home/claude/banco/ronda-7/retail/espacio/estado/corridas/salida-steering-pack.md`. La corrida quedó registrada como `2026-10-17-steering-pack-1` (87 segundos). Cuando el comité sesione, puedo registrar lo que decida en las fichas para que el material del próximo parta de ahí.

Pie: criterio-portfolio 0.3.13 · 13 fichas al 2026-10-17 · términos: https://www.josenanez.com/es/agents/criterio-pmo/legal#v0.3.13