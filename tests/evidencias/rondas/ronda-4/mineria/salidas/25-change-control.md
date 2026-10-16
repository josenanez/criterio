# /criterio-portfolio:change-control PRY-201 mover la salida a producción 30 días

La solicitud de cambio de PRY-201 (Ampliación de la relavera, gerente Sandra Gil) quedó evaluada, pero no se puede aprobar con lo que hay en la carpeta. Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-15), así que no los registré de nuevo.

- **Qué se mueve:** leí «salida a producción» como el hito «Pruebas en operación», que en el cronograma coincide con el cierre. Pasa del 2026-12-01 al 2026-12-31.
- **Conflicto de fechas:** el acta de constitución dice cierre 2026-12-21 y el cronograma aprobado el mismo día dice 2026-12-01. Si vale el acta, el cierre nuevo sería 2027-01-20. Hay que resolver cuál rige.
- **Falta de datos:** ningún documento dice quién pide el cambio ni por qué. El costo del cambio no está estimado, porque la ficha no trae el costo mensual del proyecto. La holgura contra el presupuesto aprobado es de 108.240.546 COP (4,5 %).
- **Efecto en el portafolio:** el cálculo dio cero proyectos alcanzados. Eso solo significa que no hay dependencias declaradas: el acta dice «Ninguna» y ninguna otra ficha apunta a PRY-201. No prueba que no existan, y la ventana de parada de planta es un riesgo abierto.
- **Quién decide:** no se puede determinar, porque el acta no declara autoridad. Lo dejé como «va a comité» por defecto, ya que la línea base la aprobó el Comité de Inversiones. Esa ausencia es el hallazgo de fondo.
- **Línea base nueva:** no la registré, porque nadie con autoridad aprobó el cambio. La v1 sigue intacta.
- **Señales que no puse en la solicitud:** el registro de la corrida marcó cuatro señales sobre PRY-201: «declared_vs_evidence», «progress_vs_plan» y dos hitos cumplidos sin evidencia. No las desarrollé en la salida. Concuerdan con que el proyecto reporte «Verde» mientras pide 30 días y tiene el montaje vencido el 2026-10-23.

La salida completa quedó en `/home/claude/banco/ronda-4/mineria/espacio/estado/corridas/salida-change-control.md`. La corrida quedó registrada con id `2026-10-15-change-control-1` (34 segundos, 13 proyectos). Si quiere llevarlo a comité, puedo preparar el paquete con `/steering-pack`.