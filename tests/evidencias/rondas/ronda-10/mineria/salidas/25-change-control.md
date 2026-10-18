# /criterio-portfolio:change-control PRY-201 mover la salida a producción 30 días

## Solicitud de cambio — PRY-201 Ampliación de la relavera — 2026-10-18

**Ficha de origen:** `estado/records/PRY-201.json` (corte del informe 2026-10-08) y el cálculo `portafolio.py impact`. Los términos ya estaban vigentes (v0.5.0, aceptados por José Francisco Ñáñez el 2026-10-18), así que no los registré de nuevo.

**Qué se pide:** mover la salida a producción 30 días.
**Quién lo pide:** no consta en ningún documento de la carpeta.
**Por qué:** no consta. El informe del 2026-10-08 dice «se reprogramó la parada de planta por la ventana de mantenimiento», pero no la liga a este cambio ni da fecha nueva. Es una pista, no un motivo sustentado.

**Supuesto que hay que confirmar:** el plan no tiene un hito llamado «salida a producción». Lo más cercano es «Pruebas en operación» (2026-12-15), que coincide con el cierre. Evalué el cambio como mover ese hito y el cierre de 2026-12-15 a 2027-01-14.

### Impacto
| Dimensión | Hoy | Con el cambio | Diferencia |
|---|---|---|---|
| Alcance | Componentes 1, 2 y 3 | No declarado | Sin impacto declarado |
| Tiempo | Cierre 2026-12-15 (línea base 1) | 2027-01-14 | +30 días |
| Costo | Aprobado 18.000.000.000 COP; proyección 18.496.508.384 COP | No declarado | Sin impacto declarado |

**Quién absorbe lo que no se declaró:** nadie lo dice. Mover 30 días sin tocar costo ni alcance significa que alguien lo absorbe en horas no pagadas o en calidad, o que el costo existe y no se escribió. No lo estimo: ninguna ficha trae tarifa ni holgura.

La proyección ya supera lo aprobado en 496.508.384 COP (2,8 %), y el estado declarado sigue en verde. Se ha ejecutado el 57,1 % del presupuesto con un avance declarado del 48 %. Eso no cruza el umbral de 10 % de la PMO, pero es el margen que queda.

### Efecto en el portafolio
Ninguno calculado: 0 proyectos alcanzados, 0 que no puedan sostener su fecha, 0 dependencias sin confirmar.

**Esto no equivale a «no afecta a nadie».** El acta declara «Ninguna declarada» como dependencia, y el cálculo solo recorre lo declarado. Hay dos señales de efecto que nadie escribió:
- «Ventana de parada de planta definida por operaciones» es un riesgo abierto y la parada ya se reprogramó. Operaciones depende de esta fecha y no figura como dependencia.
- «El proveedor no ha confirmado la fecha de la última entrega» es un riesgo abierto, sin dueño.

El cambio pasa por el hito «Pruebas en operación», 2026-12-15, a 58 días. Cuántos días se mueve cada actividad no se puede decir, porque la ficha no tiene holgura por actividad.

### Quién decide
- **Autoridad requerida:** no se puede determinar. La autoridad de cambio de PRY-201 no aparece en ningún documento. Ese es el hallazgo de fondo.
- **Según:** el acta de 2025-09-12 solo dice que el Comité de Seguridad aprobó el presupuesto. No fija umbrales de tiempo ni de costo ni quién aprueba cambios. El patrocinador es Natalia Ospina y el gerente es Mauricio Pérez.
- **Va a comité:** sí, por defecto. Propongo el Comité de Seguridad, que aprobó el presupuesto. El próximo comité de la PMO es el 2026-10-29.

### Si no se aprueba
El proyecto sigue con cierre el 2026-12-15, que es lo único aprobado. El informe ya declara una parada de planta reprogramada y un proveedor sin fecha de última entrega, y aun así reporta verde. Si la fecha real ya es otra, el plan vigente está desactualizado y la desviación se acumula sin registro.

### Si se aprueba
- **Línea base 2:** cierre 2027-01-14. El presupuesto sigue en 18.000.000.000 COP, porque no se pidió otro monto. El motivo está por documentar y hoy no consta.
- **Línea base 1:** no se toca (2025-09-12, cierre 2026-12-15). Replanificaciones: de 0 a 1.
- **Desviación acumulada contra la línea base original:** tiempo +30 días. Costo +496.508.384 COP (+2,8 %), que es la proyección actual contra lo aprobado. El cambio no declara costo propio.

### Otros hallazgos para el comité
- La carpeta no contiene solicitud de cambio ni acta que autorice un movimiento. `changes` está vacío, así que no hay desviación de línea base sin autorizar que reconciliar.
- Cuatro hitos figuran «cumplidos» sin evidencia de recibo propia. El cumplimiento sale del cronograma v1, no de un acta.
- El licenciamiento del software sigue pendiente en CT-546 (vencía 2026-03-05) y en CT-852 (vencía 2026-01-23). No revisé la vigencia de los contratos. Si vencen antes de 2027-01-14, el cambio los alcanza.

### Después
- Si se lleva a comité, el paquete es esta solicitud más la pregunta de quién tiene autoridad sobre PRY-201.
- Si ya lo aprobó quien podía, pásame el documento y registro la línea base 2.

**Pie de rigor.** No sé quién pidió el cambio ni por qué, qué se habló fuera de los documentos, la holgura por actividad ni el costo de 30 días. Las cifras son las que declara el informe del gerente. La verificación es suya.

La corrida quedó registrada como `2026-10-18-change-control-1`, con esta salida guardada en `estado/corridas/salida-change-control.md`.