# /criterio-portfolio:change-control PRY-203 mover la salida a producción 30 días

## Solicitud de cambio — PRY-203 Reposición automática — 2026-10-15

Salgo de la ficha `estado/records/PRY-203.json`, con corte del informe al 2026-10-07. Los términos v1.1 ya estaban vigentes a nombre de José Francisco Ñáñez (2026-10-15), así que no los registré de nuevo.

**La fecha que se quiere mover ya venció.**
- La línea base v1 pone el despliegue en la cadena el 2026-01-15, hace 273 días.
- Sumarle 30 días da 2026-02-14, que también quedó 243 días atrás.
- Tomé «salida a producción» como ese hito de despliegue, que además es el criterio de éxito del acta. Es una suposición mía.

**Los documentos no coinciden.**
- El acta dice cierre el 2026-02-04 y el cronograma dice despliegue el 2026-01-15. Son 20 días de diferencia que ningún documento explica.
- El cronograma da los 5 hitos por cerrados, sin evidencia de cierre en ninguno. El informe declara 47% de avance y estado verde.
- El script reporta 0 días de atraso contra la original. Ese cero sale de los hitos sin evidencia, así que no debe citarse como «sin atraso».

| Dimensión | Hoy | Con el cambio |
|---|---|---|
| Alcance | Componentes 1, 2 y 3 | Sin cambio declarado |
| Tiempo | Vencida hace 273 días (cronograma) | +30 días sobre una fecha ya vencida; no cubre el atraso real |
| Costo | 6.800 M COP aprobados; 3.563 M ejecutados | Sin estimación, y no la invento |

- **Quién absorbe la ausencia de impacto en alcance y costo:** el equipo, que ya perdió dos semanas por una rotación y concentra el conocimiento en una persona. También las pruebas.
- **Cifras de costo que no cuadran:**
  - Lo ejecutado (3.563 M) supera lo comprometido (3.051 M).
  - El gasto lleva 52,4% del aprobado con 47% de avance. Una extrapolación lineal mía da unos 7.580 M, por encima del aprobado y de la proyección de 6.284 M.
- **Proveedor CT-345 (Retail Andino Consultores):** tiene 4 entregables vencidos, entre 296 y 425 días, y 459 M facturados sin entrega.

**Efecto en el portafolio:** `impact` no alcanza a ningún proyecto. Ninguna ficha declara dependencia con PRY-203, y el acta dice «Ninguna declarada». Eso no prueba que no haya efecto: PRY-209 (migración del ERP) podría tocarlo y ningún documento lo dice. Tampoco hay holgura por actividad, así que no puedo decir cuántos días se movería cada proyecto.

**Quién decide:** no se puede determinar. El acta no declara autoridad para cambios, y ese vacío es el hallazgo de fondo. Recomiendo llevarlo al Comité Comercial (comité del proyecto y quien aprobó el presupuesto), próxima sesión el 2026-10-29, como rebaseline y no como «+30 días».

**Si no se aprueba:** el proyecto sigue con la fecha vencida y un verde que los documentos no sostienen.

**Si se aprueba:** no registré línea base 2, porque faltan fecha fundamentada, presupuesto, motivo y quien apruebe. La desviación contra la original hoy es de 273 días (253 si se usa la fecha del acta).

**Lo que no sé:**
- Quién pide el cambio y por qué.
- Cuál de las dos fechas es la comprometida.
- Si los hitos realmente se cerraron.
- La fecha real de salida a producción y su costo.
- Si PRY-209 depende de este proyecto.

La salida completa está en `estado/corridas/salida-change-control.md`, y la corrida quedó registrada como `2026-10-15-change-control-1`.