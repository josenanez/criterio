# /criterio-portfolio:change-control PRY-206 mover la salida a producción 30 días

## Solicitud de cambio: PRY-206 Red privada LTE en mina (2026-10-14)

Salgo de la ficha `estado/portafolio/records/PRY-206.json`, con informe de avance del 2026-09-27. Los términos están aceptados (v1.0, José Francisco Ñáñez, 2026-10-14). Leí «salida a producción» como el hito «Pruebas en operación», que coincide con el cierre. La ficha no tiene un hito con ese nombre; confírmalo.

**Impacto**

| Dimensión | Hoy | Con el cambio |
|---|---|---|
| Alcance | Componentes 1, 2 y 3 (sin detalle) | Sin cambio declarado |
| Tiempo | Cierre 2027-01-27 (línea base 1, la única) | 2027-02-26 (+30 días) |
| Costo | 800 M COP aprobados; proyección 833,9 M COP | Sin declarar; no se puede calcular con la ficha |

- **Quién absorbe el cambio:** si el alcance no cambia y el cierre se mueve 30 días, alguien lo absorbe en horas no pagadas o en calidad. La solicitud no lo dice.
- **Sobrecosto previo:** la proyección ya supera lo aprobado en 33,9 M COP (4,2 %) antes del cambio.
- **Hitos que pasa el cambio:** Montaje e instalación (2026-12-03) y Pruebas en operación (2027-01-27). No sé cuántos días se mueve cada uno, porque eso necesita holgura por actividad y la ficha no la tiene.
- **Proveedor CT-353:** «Calibración de sensores» vence el 2026-12-10, y el proveedor no ha confirmado la fecha de su última entrega. No leí el contrato, así que no sé si admite el corrimiento.

**Efecto en el portafolio:** el cálculo da 0 proyectos alcanzados. Eso no prueba que nadie dependa de PRY-206: la ficha tiene `dependencies: []`, o sea que no hay ninguna declarada, y una dependencia sin declarar no la veo.

**Quién decide:** no se puede determinar. El acta del 2026-04-19 no declara autoridad (`identity.authority: not_found`), y ese es el hallazgo de fondo. Por defecto va a comité, y el próximo es el 2026-10-28.

**Si no se aprueba:** el proyecto sigue con cierre 2027-01-27 y estado amarillo, con 68 % de avance al 2026-09-27. Ya arrastra un hito de permisos vencido desde el 2026-10-10 sin evidencia, diez días de montaje perdidos por lluvia y un hallazgo de seguridad sin responsable.

**Si se aprueba:** línea base 2 con cierre 2027-02-26. El presupuesto y el motivo quedan por definir. La línea base 1 no se toca, y las replanificaciones pasan de 0 a 1. La desviación acumulada contra la original sería +30 días en tiempo; en costo no hay dato.

**Lo que esta corrida no sabe:**
- Quién pide el cambio y por qué.
- Cuánto cuesta el corrimiento.
- Si hay dependientes no declarados.
- Si el contrato CT-353 permite mover fechas.
- Cuántos días se mueve cada hito intermedio.

**Siguiente paso:** llevarlo al comité del 2026-10-28 con motivo y costo escritos, o registrar la línea base 2 cuando lo apruebe quien tenga autoridad. Antes conviene que el acta declare quién decide.

Rigor: las cifras salen de la ficha y del script `impact`, sin estimaciones propias.

Corrida registrada como `2026-10-14-change-control-1`. La salida completa está en `estado/portafolio/corridas/salida-change-control.md`.