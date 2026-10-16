# /criterio-project:pm-escalate 

## Para decisión — PRY-203 Aportes sociales en línea · 2026-10-15

Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-15), así que no los pedí de nuevo. No indicaste qué escalar y tomé lo ya marcado en la ficha: CC-01, «pendiente de presentación al comité» desde el 2026-10-04.

### Primer punto: el acta no declara la autoridad del gerente
El acta de constitución nombra a la patrocinadora (Elena Duarte), al gerente (Ricardo Salas) y al Comité de Tecnología. Dice que ese comité aprobó los 2.400.000.000 COP. **No dice qué puede decidir el gerente ni quién aprueba cambios de alcance, tiempo o costo.** Por eso no puedo afirmar que CC-01 exceda la autoridad del gerente.

### ¿Se aprueba CC-01 (+115 días, +230.000.000 COP) en el comité del 2026-10-22, o se conserva la línea base (cierre 2027-05-30, 2.400.000.000 COP)?

**Quién decide:** el acta no lo dice. Propongo llevarlo al Comité de Tecnología con Elena Duarte, porque aprobó el presupuesto original. Es una inferencia y no una cita; que el comité confirme en la misma sesión que tiene la facultad.

**Si no se decide hoy:** ningún documento fija una fecha límite y no la inventé. Lo que sí tiene fecha:
- La próxima ocasión es el comité del 2026-10-22 según la configuración. Las notas del 10-15 dicen «en dos semanas» (≈10-29); hay que confirmar cuál vale.
- El hito «Ambiente de pruebas certificado» venció el 2026-10-10 sin evidencia.

| Opción | Alcance | Tiempo | Costo |
|---|---|---|---|
| A. Aprobar CC-01 | Ampliado; la solicitud no dice qué se agrega | Cierre 2027-09-22 (+115 días) | 2.630.000.000 COP. La proyección (2.833.558.895) queda 203.558.895 por encima, salvo que ya incluya CC-01; el informe no lo dice |
| B. Rechazar | Original (3 componentes) | Cierre 2027-05-30, pero el plan v2 ya pone «Integración con el core» en 2027-07-06, después de ese cierre | 2.400.000.000 COP. La proyección ya va 433.558.895 (18,1 %) sobre lo aprobado y eso queda sin decidir |
| C. Devolver CC-01 para completarla | Se define qué se agrega | Sin cambio hasta decidir | Se separa qué parte de la proyección es CC-01 y cuál es sobrecosto previo |

**Recomiendo C.** CC-01 no describe qué alcance agrega ni si los 230.000.000 están dentro de la proyección, así que el comité decidiría a ciegas. Que se complete antes del 10-22 y que en esa sesión se confirme quién tiene la facultad.

### A quién alcanza
El cálculo con +115 días **no encontró otros proyectos alcanzados**. Eso solo refleja que este estado tiene un único proyecto. No prueba que nadie dependa de este: el acta dice «Ninguna declarada» en dependencias, pero el informe cita la dependencia del proveedor del core. Esa dependencia nunca se confirmó con el otro lado. Tampoco puedo calcular cuántos días se mueve cada proyecto alcanzado, porque falta la holgura por actividad.

### Mis hitos por los que pasa
| Hito | Fecha vigente | En cuántos días |
|---|---|---|
| Integración con el core cooperativo | 2027-07-06 (línea base 2027-03-13) | 264 días desde hoy |

**Ojo:** la fecha vigente ya está exactamente 115 días después de la línea base, lo mismo que pide CC-01, y CC-01 no está aprobada. Ningún documento dice que el cronograma v2 la incorpore. Si lo hace, el plan se movió sin decisión; si no, hay un segundo atraso de 115 días aparte. Hay que preguntarlo a Ricardo Salas antes del comité.

### Sube, pero aún no se puede formular
- **«Enviar el documento 1»** (María Restrepo): 6 reprogramaciones, última al 2026-12-11.
- **«Cerrar la prueba 2»** (Sandra Gil): 5 reprogramaciones, última al 2026-11-28.
- Pasan el umbral de 3, pero sin saber qué las bloquea no hay pregunta cerrada. Primero la llamada; si el doliente está fuera del proyecto, entonces escala.
- No escalan, son del gerente: el dueño del hallazgo de seguridad, el de la rotación del desarrollador clave y el del riesgo no registrado del equipo del proveedor.

### De dónde sale esto
- Acta (autoridad no declarada, comité, presupuesto, cierre, dependencias): `00-gobierno/2025-11-25-acta-constitucion.docx`.
- CC-01: `20-seguimiento/2026-10-04-solicitud-cambio-cc-01.md`.
- Presupuesto, proyección y riesgo del proveedor: `20-seguimiento/2026-10-12-informe-avance.pdf`.
- Hitos y fechas: `10-plan/2026-10-12-cronograma-v2.csv`.
- Comité semanal, próximo 2026-10-22: `.criterio/proyecto/PRY-203/config.json`.
- «Próxima reunión en dos semanas»: `2026-10-15-notas-reunion.txt`.
- Reprogramaciones: `30-reuniones/` y `2026-10-15-notas-reunion.txt`.
- Cálculo de impacto: `portafolio.py impact --days 115`.

Esto es solo el paquete: llevarlo al comité y llamar a quien corresponda es tuyo. La corrida quedó registrada como `2026-10-15-pm-escalate-1`, con el paquete en `estado/PRY-203-aportes-sociales-en-línea/corridas/salida-pm-escalate.md`.