# /criterio-portfolio:steering-pack 

Armé el material del comité de PRY-199 a PRY-211. Tiene 6 decisiones y 3 escalamientos sin decisión asociada, y 11 de los 13 proyectos tienen hallazgos. Lo escribí a mano, no lo generó el script, y no volví a leer el archivo completo después de corregirlo.

Los términos ya estaban vigentes (v1.2), aceptados por José Francisco Ñáñez el 2026-10-23, así que no hizo falta registrarlos otra vez. Las cifras vienen de `compute`, que dio 71 señales en total. El diferencial de costo de PRY-201 (412.334.652 COP) lo copié de la corrida de control de cambios de hoy. Corregí a mano un par de errores de redacción y cifras mal atribuidas; no verifiqué línea por línea el archivo final contra la salida de `compute`.

**Decisiones de hoy**
1. Quién aprueba cambios de fecha y de presupuesto. La autoridad no consta en ninguna de las 13 fichas, y esto condiciona los puntos 2 y 3.
2. CC-01 de PRY-202: piloto +69 días, sin aprobar y ya reflejado en un cronograma v2 que no tiene aprobación. Recomiendo devolverlo hasta que haya sustento.
3. PRY-201: mover la salida +30 días, del 2026-10-30 al 2026-11-29. No consta quién lo pide ni por qué. Recomiendo aplazar con tope el 2026-10-30.
4. PRY-209: lo facturado por Núcleo Financiero supera lo aceptado en 949.911.814 COP. Recomiendo retener nuevos pagos.
5. Quién es la contraparte del calendario de liberaciones del core. Afecta a cinco proyectos: 203, 207, 209, 208 y 211.
6. Quién es el dueño del hallazgo de seguridad y de la disponibilidad del equipo de seguridad. Aparece en ocho proyectos.

**Escalamientos sin decisión asociada**
- PRY-206 está en verde con 16 señales abiertas.
- PRY-207 lleva 20 días en silencio.
- PRY-205, 208, 210 y 211 tienen la fecha de cierre vencida y ninguna solicitud de cambio.

**Lo que no sé**
- **Comité anterior:** no hay registro de uno, así que no pude cerrar ese ciclo.
- **PRY-201:** no sé quién pide el cambio, cuánto cuesta el mes extra ni hasta cuándo cubre el contrato CT-600.
- **Fichas:** faltan la autoridad de aprobación y la fase en las 13, y el dueño de los 41 ítems del registro de riesgos, supuestos, incidencias y dependencias.
- **Costos:** no hay costo por opción en los puntos 2, 5 y 6.

La corrida quedó registrada como `2026-10-23-steering-pack-1` y dice que tardó 88 segundos.

Archivos en `estado/corridas/` (dentro de la carpeta de trabajo de la sesión):
- `salida-steering-pack.md`