# /criterio-portfolio:change-control PRY-205 mover la salida a producción 30 días

Evalué el cambio de PRY-205 y dejé la corrida registrada. No se puede decidir todavía: la solicitud llegó sin solicitante, sin motivo y sin impacto en costo, y el acta no dice quién puede aprobar un cambio de fecha. Los términos (v1.1) ya estaban vigentes a nombre de José Francisco Ñáñez, fecha 2026-10-17, y no hubo preguntas que contestar.

## Solicitud de cambio — PRY-205 Prevención de lavado de activos — 2026-10-17

**Qué se pide:** mover la salida a producción 30 días, del 2027-06-28 al 2027-07-28.
**Quién lo pide:** no consta en ningún documento de la carpeta.
**Por qué:** no consta. Dos hechos del informe del 2026-10-14 podrían explicarlo, pero es lectura mía: la prueba de carga no alcanzó el umbral y se repite, y dos historias quedaron fuera del sprint por dependencia con el core.

**Línea base de la que parte:** una sola, v1, aprobada el 2026-05-29 por el Comité de Transformación Digital. Cierre 2027-06-28 y 800.000.000 COP. No hay replanificaciones ni cambios aprobados, así que hoy no hay días sin autorizar.

### Impacto
| Dimensión | Hoy | Con el cambio | Diferencia |
|---|---|---|---|
| Alcance | Componentes 1, 2 y 3 (el acta no los nombra) | No declarado | No se puede medir |
| Tiempo | Salida a producción 2027-06-28 | 2027-07-28 | +30 días en ese hito. No está dicho si los otros tres hitos pendientes se mueven. |
| Costo | Aprobado 800.000.000 COP; proyección 762.502.965 COP | No declarado | No se puede calcular: ningún documento dice cuánto cuesta un mes más. |

**Quién absorbe lo que no está declarado:** alguien lo absorbe en horas del equipo no presupuestadas, en el contrato CT-172 con Núcleo Financiero o en los 37.497.035 COP entre la proyección y lo aprobado. Nadie lo ha dicho, así que el costo queda abierto, no en cero.

- **Hito cercano:** "Ambiente de pruebas certificado" vence el 2026-11-09, en 23 días, y la prueba de carga acaba de fallar. Si ese hito se mueve, el 2027-07-28 puede no alcanzar.
- **Brecha entre fechas:** entre el piloto (2027-04-12) y la salida hay 77 días. Es distancia entre fechas, no holgura; la ficha no tiene holgura por actividad.

### Efecto en el portafolio
`impact` no alcanza a ningún proyecto, directo ni indirecto: 0 que no puedan sostener su fecha y 0 dependencias sin confirmar. Eso no significa que no haya efecto. El acta dice "Ninguna declarada", pero el informe habla de una "dependencia con el core" y hay un hito "Integración con el core" (2027-01-25). Si el core es otro proyecto del portafolio, el cálculo no lo ve. Tampoco puedo decir cuántos días se movería cada proyecto afectado.

### Quién decide
- **Autoridad requerida:** no determinable. Ni el acta ni otro documento dicen quién aprueba un cambio de fecha ni hasta qué umbral. Es el hallazgo de fondo.
- **Va a comité:** sí, por defecto y no por una cláusula. El Comité de Transformación Digital aprobó la línea base y el presupuesto. Próximo comité: 2026-10-24. Si la facultad es de otra persona, decide esa persona.

### Si no se aprueba
El cierre sigue en 2027-06-28, pero la fecha ya tiene señales de que no se sostiene. El informe declara verde y 82 %, y la evidencia no lo respalda:
- Solo 1 de 5 hitos tiene acta de recibo. Diseño funcional, comprometido para el 2026-08-24, se recibió el 2026-10-08, 45 días tarde y sin mover la fecha vigente.
- Se ejecutó el 19,6 % del presupuesto (156.431.890 de 800.000.000 COP).
- El licenciamiento del motor (CT-172, 2026-09-22) sigue pendiente, sin evidencia, 25 días después.
- Hay un riesgo de concentración del conocimiento y un compromiso vencido: Laura Vélez, "punto 31", para el 2026-10-11.

### Si se aprueba
- **Línea base 2:** cierre 2027-07-28. El presupuesto no está declarado (800.000.000 COP si no cambia) y el motivo está pendiente.
- **Desviación acumulada contra la original:** +30 días en tiempo y sin dato en costo. La v1 no se toca.
- **El atraso previo no está incluido:** los 45 días del hito de diseño funcional no están dentro de los 30 de esta solicitud.

### Lo que falta para poder decidir
1. Quién pide el cambio y el motivo, por escrito.
2. Si los hitos de ambiente de pruebas, integración con el core y piloto se mueven, y cuánto.
3. Cuánto cuesta un mes más (equipo y CT-172) y quién lo paga.
4. Quién tiene la autoridad para aprobar un cambio de fecha en PRY-205.
5. Si la "dependencia con el core" es de otro proyecto del portafolio, y cuál.

Puedo preparar el punto para el comité del 2026-10-24 con esas cinco preguntas, o registrar la línea base 2 cuando la apruebe quien pueda. No registro nada hasta entonces.

**Pie de rigor:** borrador de trabajo, no decisión ni asesoría. Se basa solo en los 6 documentos de la carpeta de PRY-205; no sabe lo que se habló fuera de ellos. Los días de propagación salen de `portafolio.py impact` al 2026-10-17; las demás cifras se copian de los documentos o son resta simple de sus fechas y montos. La verificación de cada cita es suya.

La corrida quedó registrada con id `2026-10-17-change-control-1`. La salida completa está en `estado/corridas/salida-change-control.md`.