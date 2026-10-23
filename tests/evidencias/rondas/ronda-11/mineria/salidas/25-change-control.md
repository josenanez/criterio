# /criterio-portfolio:change-control PRY-200 mover la salida a producción 30 días

## Solicitud de cambio PRY-200: mover 30 días la salida a producción

Esta solicitud no se puede aprobar tal como está escrita. La fecha nueva que resulta de mover 30 días (2026-05-06) ya pasó, no hay quien tenga autoridad declarada para aprobarla y la solicitud no trae motivo ni solicitante.

La evaluación sale de la ficha `estado/records/PRY-200.json` y de los documentos citados. Los términos ya estaban vigentes (v1.2, aceptados por José Francisco Ñáñez), así que no hubo que aceptarlos otra vez.

La ficha no tiene un hito llamado «salida a producción». Tomé el pedido como mover el cierre de 2026-04-06 a 2026-05-06. Si se refería a otra fecha, hay que decirlo.

- **La fecha ya pasó:** hoy es 2026-10-23. El cierre vigente venció hace 200 días y el pedido, hace 170. Aprobarlo sería retroactivo y no cubriría el atraso real, que contra la línea base original es de al menos 200 días y sigue abierto.
- **Sin cambios registrados:** solo existe la línea base 1, sin cambios aprobados, y el informe del 2026-10-18 declara estado verde. Las actas de recibo de «Montaje e instalación» y de «Pruebas en operación» son 237 y 188 días posteriores a sus fechas de línea base. Ningún documento autoriza esa diferencia.
- **Impacto:**
  - **Alcance:** sin impacto declarado.
  - **Tiempo:** 30 días declarados.
  - **Costo:** sin impacto declarado. La proyección ya supera lo aprobado en 79.870.475 COP (+3,3 %).
- **Portafolio:** no alcanza a ningún otro proyecto, porque el acta dice «Ninguna declarada» en dependencias. Eso no prueba que no existan, y no tengo holgura por actividad para calcular cuántos días se movería cada uno.
- **Quién decide:** la ficha marca la autoridad como no encontrada (`identity.authority`). Por defecto el paquete va al Comité de Operaciones, que aprobó el presupuesto original. La próxima fecha de comité del portafolio es el 2026-10-29.
- **Línea base 2:** queda como borrador (cierre 2026-05-06, presupuesto sin cambio) y no la registré, porque nadie la aprobó y su fecha ya pasó. Lo coherente es pedir una fecha futura con su motivo.
- **Señales ajenas al cambio:**
  - Lo ejecutado es el 18,6 % del presupuesto, frente a un avance reportado de 77 %.
  - Lo facturado a CT-326 (551.792.512 COP) supera lo ejecutado (446.036.134 COP).
  - «Calibración de sensores» figura aceptada sin acta de recibo.

La corrida quedó registrada como `2026-10-23-change-control-1`, con la salida completa en `estado/corridas/salida-change-control.md`. Tardó 45 segundos. Las demás preguntas se resolvieron con la respuesta sugerida, como se pidió.