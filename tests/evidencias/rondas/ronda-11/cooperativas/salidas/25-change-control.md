# /criterio-portfolio:change-control PRY-201 mover la salida a producción 30 días

La solicitud de cambio de PRY-201 está evaluada y la corrida quedó registrada como `2026-10-23-change-control-1`. Los términos ya estaban vigentes (v1.2, aceptados por José Francisco Ñáñez el 2026-10-23), así que no hubo que registrarlos de nuevo.

## Solicitud de cambio: PRY-201 Apertura de ahorro en línea (2026-10-23)

Sale de la ficha PRY-201, la línea base v1 y el cálculo de impacto del portafolio.

**Qué se pide:** mover la salida a producción de 2027-03-24 a 2027-04-23 (30 días). Ningún documento dice quién lo pide ni por qué.

| Dimensión | Hoy | Con el cambio |
|---|---|---|
| Alcance | Componentes 1, 2 y 3 (el acta no los detalla) | No declarado |
| Tiempo | Cierre 2027-03-24 | 2027-04-23 (+30 días) |
| Costo | 18.000.000.000 COP aprobados; proyección 18.824.193.276 | No declarado |

- **Alcance y costo:** la solicitud no declara impacto en ninguno de los dos. Si no cambian, alguien absorbe el mes en calidad, en horas no pagadas o en costo. La proyección ya supera lo aprobado en 824 millones COP (4,6 %), por debajo del umbral de 10 %.
- **Contrato CT-967:** la solicitud no dice qué pasa con sus entregables (2026-11-20 y 2027-02-04). La ficha no trae la vigencia del contrato.
- **Efecto en el portafolio:** el cálculo no alcanza a ningún proyecto, ni directa ni indirectamente. Eso solo refleja que el acta declara «Ninguna dependencia», no que no existan. Conviene confirmar con PRY-202 (core cooperativo), porque PRY-201 tiene un hito de integración con el core.
- **Hitos por los que pasa el cambio:** integración con el core (2026-12-04), piloto (2027-01-28) y salida (2027-03-24). Cuántos días se mueve cada uno no se puede calcular, porque la ficha no tiene holgura por actividad.
- **Quién decide:** el acta no declara autoridad para aprobar cambios. Por defecto va al Comité de Tecnología; el próximo es el 2026-10-30. Que falte esa autoridad es el hallazgo de fondo.
- **Si no se aprueba:** el cierre sigue en 2027-03-24, pero esa fecha no tiene sustento. Con la prueba de carga repetida, el hallazgo de seguridad sin responsable y el 33 % de avance, el estado «verde» no lo respalda la evidencia.
- **Si se aprueba:** línea base 2 con cierre 2027-04-23. La v1 no se toca y las replanificaciones pasan de 0 a 1. La desviación acumulada contra la original sería +30 días. En costo sería +0 hasta que se declare otro presupuesto. No hay ningún cambio aprobado registrado que autorice esos 30 días.

**Lo que no sé:** quién lo pide y por qué, cuántos días se mueven el piloto y la integración, cuánto cuesta un mes más, y si hay dependencias reales que nadie declaró.

Es un borrador de trabajo, no una decisión; la verificación es suya.

El texto completo está en `estado/corridas/salida-change-control.md`, dentro de la carpeta de trabajo.

**Siguiente paso:** puedo preparar el paquete para el comité del 2026-10-30. Si alguien con autoridad ya lo aprobó, indíqueme quién y en qué documento, y registro la línea base 2.