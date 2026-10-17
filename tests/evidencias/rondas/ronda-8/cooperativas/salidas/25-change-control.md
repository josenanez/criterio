# /criterio-portfolio:change-control PRY-208 mover la salida a producción 30 días

## Solicitud de cambio — PRY-208 Motor de crédito — 2026-10-17

Parto de la ficha `estado/records/PRY-208.json`. Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-17), así que no los registré de nuevo.

**Qué se pide:** mover la salida a producción de 2027-04-20 a 2027-05-20 (+30 días). No consta quién lo pide ni por qué, así que la solicitud está incompleta.

| Dimensión | Hoy | Con el cambio |
|---|---|---|
| Alcance | Componentes 1 a 3, sin detalle | No declarado |
| Tiempo | Salida 2027-04-20 | 2027-05-20 (+30 días) |
| Costo | Aprobado 18.000 millones COP, proyección +3,0 % | No declarado |

Alcance y costo no traen impacto declarado. Si el costo no cambia, alguien absorbe el retraso en horas no pagadas o en calidad, y hay que decir quién.

**Efecto en el portafolio:**
- **Resultado del cálculo:** no alcanza a ningún proyecto. Eso solo refleja que el acta declara «Ninguna» dependencia, no que nadie dependa de PRY-208.
- **Qué no se sabe:** cuántos días se mueve cada hito intermedio, porque la ficha no tiene holgura por actividad.
- **Riesgo abierto:** el proveedor no ha confirmado la fecha de la última entrega. El contrato CT-349 no trae fecha de terminación ni vigencia, y hay que confirmar que cubra hasta 2027-05-20.

**Quién decide:**
- **Autoridad:** no se puede determinar. El acta no declara umbrales de autoridad para cambios, y ese es el hallazgo de fondo.
- **Comité:** el único nombrado es el Comité de Riesgos, así que el cambio va a comité por defecto.

**Antecedente que hay que regularizar:**
- **CC-01:** pide +117 días y 234 millones COP, y dice «Autorizada por el comité» sin decir cuál ni cuándo.
- **Cronograma v2:** movió la fecha el 2026-10-08, seis días antes de que se pidiera CC-01.
- **Línea base:** la ficha lo marca como cambio sin línea base nueva.

**Si se aprueba:**
- **Línea base 3:** cierre 2027-05-20. El presupuesto no se puede fijar, porque el último aprobado no incluye los 234 millones de CC-01 ni costo de este cambio.
- **Replanificaciones:** pasan de 1 a 2.
- **Desviación contra la línea base original:** +147 días (117 + 30), 37,2 %. Contra la vigente serían solo +30.

**Si no se aprueba:** sigue la fecha 2027-04-20 (+117 días), con el piloto vencido hace 11 días y dos hitos cumplidos sin evidencia de recibo.

No registré línea base 3, porque nadie con autoridad aprobó el cambio. Falta quién lo pide y por qué, el impacto en alcance y costo, la confirmación del proveedor, el acta que autorizó CC-01 y la autoridad de cambios en el acta. Lo siguiente es llevarlo a comité, con CC-01 regularizada primero.

La salida completa está en `estado/corridas/salida-change-control.md` y la corrida quedó registrada como `2026-10-17-change-control-1`.