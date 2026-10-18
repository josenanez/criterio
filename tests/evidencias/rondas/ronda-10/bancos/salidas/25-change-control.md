# /criterio-portfolio:change-control PRY-202 mover la salida a producción 30 días

## Solicitud de cambio — PRY-202 Migración a la nube — 2026-10-18

Salgo de la ficha de PRY-202 (corte 2026-10-11) y del acta de constitución del 2025-12-06. Los términos ya estaban vigentes (v0.5.0, aceptados por José Francisco Ñáñez el 2026-10-18), así que no los registré de nuevo. Corrí el cálculo de impacto sin ayuda de nadie y, donde faltaba un dato, lo dejé como falta en vez de inventarlo.

**Qué se pide:** mover 30 días la salida a producción. Ningún documento dice quién lo pide ni por qué. El informe del 2026-10-11 menciona dos semanas perdidas por la rotación de un desarrollador, pero son 14 días, no 30, y nadie lo liga a esta solicitud.

| Dimensión | Hoy | Con el cambio | Diferencia |
|---|---|---|---|
| Alcance | Componentes 1, 2 y 3 | Sin cambio declarado | 0 declarado |
| Tiempo | Cierre 2026-09-25 | 2026-10-25 | +30 días |
| Costo | Aprobado 3.300.000.000 COP; proyección declarada 3.241.959.414 COP | No se sabe | Sin declarar |

- **Costo:** nadie dijo cuánto cuesta un mes más. El margen de la proyección declarada es de 58.040.586 COP, el 1,8 % del aprobado.
- **Alcance:** si no cambia el alcance ni el costo, alguien absorbe el mes en horas no pagadas o en calidad. Hay que decir quién.

**La fecha ya venció.** El cierre de 2026-09-25 pasó hace 23 días y el proyecto sigue en 51 % declarado, en amarillo. Por eso esta solicitud regulariza un atraso que ya ocurrió. Con +30 días el cierre sería 2026-10-25, solo 7 días en el futuro.

**La ficha se contradice.** Marca «Salida a producción» como cumplida, igual que los otros cuatro hitos, y ninguno tiene evidencia. Eso choca con el 51 % de avance y con el criterio de éxito, que pide estar «en producción y medido».

**Efecto en el portafolio:** el cálculo no alcanza a ningún proyecto, porque el acta declara «Dependencias: Ninguna». Probablemente es una omisión: una migración a la nube de Banca Hipotecaria sin ninguna dependencia es poco creíble. Tampoco sé cuántos días se movería cada hito o actividad, porque la ficha no tiene holgura por actividad.

**Quién decide:** no se puede determinar, porque el acta no declara ninguna autoridad para cambios. Va al Comité de Arquitectura, que aprobó la línea base original, y el hallazgo de fondo es que nadie tiene un umbral escrito para decidir por menos.

**Si no se aprueba:** el proyecto sigue contra una fecha vencida, sin que el gobierno cubra el atraso.

**Si se aprueba:** sería la línea base 2, con cierre 2026-10-25. El presupuesto y el motivo quedan pendientes, porque no hay documento de aprobación. Contra la línea base original serían +30 días de atraso, y el costo no se puede calcular hoy. La línea base 1 no se toca.

**Otro hallazgo para el comité:** en el contrato CT-812 se facturaron 614.970.173 COP, frente a 534.681.656 COP de entregables aceptados. Son 80.288.517 COP sin entregable aceptado que los cubra. El licenciamiento del motor, vencido desde el 2026-03-04, sigue pendiente.

**No registré línea base nueva.** Nadie con autoridad la ha aprobado.

Dejé la corrida registrada como `2026-10-18-change-control-1`. El texto completo está en `estado/corridas/salida-change-control.md`. La corrida tardó 32 segundos.