# /criterio-portfolio:change-control PRY-201 mover la salida a producción 30 días

Partí de la ficha `estado/records/PRY-201.json`. Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-16), así que no los registré de nuevo.

**Qué dice el análisis**
- **Tiempo:** la salida a producción pasa del 2027-01-04 al 2027-02-03 (+30 días). Hoy hay una sola línea base (v1), así que no hay desviación previa. El Piloto con asociados (2026-10-26) queda en el camino y la solicitud no dice si se mueve.
- **Alcance y costo:** la solicitud no declara impacto en ninguno. La proyección deja solo COP 26,2 millones de holgura sobre los COP 1.200 millones aprobados, así que un mes más de equipo probablemente la supera. No puedo cuantificarlo, porque la ficha no trae costo mensual.
- **Portafolio:** el cálculo no alcanza a ningún proyecto, pero la ficha no declara ninguna dependencia. Hay un riesgo, «dependencia del proveedor del core cooperativo», que no está enlazado a ningún proyecto. Un resultado vacío no prueba que no haya efecto.
- **Quién decide:** no se puede determinar. El acta no declara autoridad para aprobar cambios, y ese es el hallazgo de fondo. Por defecto va al Comité de Tecnología.
- **Si no se aprueba:** el proyecto se declara en verde con 74 % de avance, pero la evidencia no lo sostiene.
  - Dos hitos figuran como cerrados sin acta de recibo.
  - Hay un hallazgo de seguridad abierto sin responsable.
  - No hay minutas ni actas de comité.

**Lo que no supe y no inventé:**
- Quién pide el cambio.
- Por qué lo pide.
- Si el piloto se mueve.
- Cuántos días se mueve cada proyecto afectado, si los hay.

**Registro:** no creé una línea base nueva, porque nadie la ha aprobado. La corrida quedó registrada como `2026-10-16-change-control-1`.

El siguiente paso es completar solicitante, motivo, impacto en alcance y costo, y dónde está escrita la autoridad. Después se lleva al Comité de Tecnología. El próximo comité de la PMO es el 2026-10-30.

Archivos en `/home/claude/banco/ronda-6/cooperativas/espacio/estado/corridas/`:
- `salida-change-control.md`
- `2026-10-16-change-control.md`