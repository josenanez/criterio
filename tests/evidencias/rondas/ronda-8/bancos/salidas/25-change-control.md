# /criterio-portfolio:change-control PRY-208 mover la salida a producción 30 días

## Solicitud de cambio — PRY-208 Motor de decisión — 2026-10-17

Sale de la ficha de PRY-208 (corte 2026-10-17). Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-17), así que no hubo que registrar nada.

**Qué se pide:** mover la salida a producción 30 días, del 2026-11-08 al 2026-12-08. Ningún documento de la carpeta dice quién lo pide ni por qué.

**Impacto**

| Dimensión | Hoy | Con el cambio |
|---|---|---|
| Alcance | Componentes 1, 2 y 3 | No declarado |
| Tiempo | Cierre 2026-11-08 | Cierre 2026-12-08 (+30 días) |
| Costo | Aprobado 4.200 M COP; proyección 5.331 M (+26,9 %) | No declarado |

- **Costo:** nadie declaró cuánto cuesta un mes más. No lo calculé: sería inventarlo. Si no hay presupuesto adicional, lo absorbe una proyección que ya está sobre el aprobado.
- **Alcance:** si el corrimiento viene del cambio regulatorio que el informe de avance deja como riesgo abierto sin dueño, alcance y fecha se mueven juntos.
- **Contrato del proveedor:** no sé qué pasa con el contrato CT-190 si la salida se mueve, porque lo que leí no trae cláusula de prórroga ni de vigencia.

**Efecto en el portafolio:** el cálculo devolvió 0 proyectos alcanzados. Eso significa que no hay dependencias declaradas, no que no haya efecto. El acta dice «Ninguna declarada», pero el informe de avance menciona una dependencia con el core que no está registrada en ningún sitio. Hay que confirmarla con Gustavo Neira antes de afirmar que otros proyectos no se tocan. Tampoco sé cuántos días se mueve cada actividad, porque la ficha no tiene holgura.

**Quién decide:** la autoridad no está declarada en el acta, y ese es el hallazgo de fondo. Recomiendo llevarlo al Comité de Arquitectura del 2026-10-20 (esa fecha es la de la configuración; la recomendación es mía, no una regla del acta).

**Si no se aprueba:** el proyecto sigue en rojo y a 22 días de la fecha. Declara 57 % de avance frente a 80–100 % que sostiene el plan. Dos hitos cumplidos no tienen evidencia, y la parametrización del tarifario del proveedor lleva 91 días vencida.

**Si se aprueba:** habría una línea base 2, con cierre 2026-12-08, y la línea base 1 queda intacta. Contra la original, el corrimiento sería de 30 días y el costo estaría +26,9 % sobre el aprobado. No registré ninguna línea base nueva porque nadie ha aprobado el cambio.

La salida completa, con las señales abiertas y lo que no sé, está en `estado/corridas/salida-change-control.md`. La corrida quedó registrada como `2026-10-17-change-control-1`.

Esto es un borrador de trabajo, no una decisión. Verifique cada dato contra el documento citado. Puedo preparar el paquete para el comité del 2026-10-20 con `/steering-pack` si quiere.