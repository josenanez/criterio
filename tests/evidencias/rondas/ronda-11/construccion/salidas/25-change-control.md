# /criterio-portfolio:change-control PRY-206 mover la salida a producción 30 días

## Solicitud de cambio — PRY-206 Modelado BIM de proyectos — 2026-10-22

Sale de la ficha PRY-206 (actualizada el 2026-10-22). Los términos v1.2 ya estaban vigentes, aceptados por José Francisco Ñáñez el 2026-10-22, así que no hubo que registrarlos de nuevo.

**Supuesto que tomé (respuesta sugerida):** «salida a producción» es el cierre del proyecto. El criterio de éxito del acta es «en producción y medido» y el cierre comprometido es 2027-07-31. Si te referías a otro hito, el cálculo cambia.

**Qué se pide:** mover la salida a producción 30 días. Ni la solicitud ni la carpeta dicen quién lo pide ni por qué.

### Impacto
| Dimensión | Hoy | Con el cambio | Diferencia |
|---|---|---|---|
| Alcance | Componentes 1, 2 y 3 | Sin cambio declarado | 0 declarado |
| Tiempo | Cierre 2027-07-31 | 2027-08-30 | +30 días |
| Costo | Aprobado COP 6.800.000.000; proyección COP 7.897.229.155 | No declarado | No declarado |

- **Quién absorbe lo que no se declaró:** con alcance y costo sin cambio y 30 días más de plazo, alguien lo absorbe en horas no pagadas o en calidad.
- **El costo ya viene mal sin este cambio:** la proyección supera lo aprobado en COP 1.097.229.155 (+16,1 %), con un umbral de 10 %. El costo de los 30 días no está en ningún documento y no lo invento.
- **Presupuesto y avance no cuadran:** lo ejecutado es el 47 % del presupuesto aprobado, frente a un 69 % de avance declarado.
- **Comprometido menor que ejecutado:** COP 2.410.717.775 contra COP 3.198.959.008. Una de las dos cifras está mal.
- **Hito en riesgo:** «Licencias y permisos obtenidos» vence el 2026-10-24, en 2 días, y está pendiente y sin evidencia. Si se corre, el cierre ya no se mueve solo 30 días.
- **Cronograma sospechoso:** sus hitos (cimentación, estructura, entrega de obra) son de construcción, no de modelado BIM. Conviene confirmar que sea el cronograma de este proyecto.

### Efecto en el portafolio
`impact` no alcanza a ningún proyecto, directo ni indirecto. Eso es ausencia de dependencias declaradas, no de efecto: el acta dice «Ninguna declarada». Tampoco sé cuántos días se mueve cada hito intermedio, porque la ficha no tiene holgura por actividad.

### Quién decide
- **Autoridad requerida:** no se puede determinar. El acta no declara autoridad de cambios ni umbrales.
- **Va a comité:** sí, por defecto. Solo consta el Comité de Seguridad, que aprobó el presupuesto el 2026-04-11. Que sea el órgano de un proyecto BIM también hay que confirmarlo.
- **Hallazgo de fondo:** el proyecto no tiene autoridad de cambios declarada.

### Si no se aprueba
El proyecto sigue con cierre 2027-07-31, con la proyección 16,1 % sobre el presupuesto. Todavía no hay desviación de tiempo registrada contra la línea base 1.

### Si se aprueba
- **Línea base 2:** cierre 2027-08-30, presupuesto sin cambio declarado y motivo sin constar. La línea base 1 no se toca.
- **Desviación contra la original:** +30 días, y +COP 1.097.229.155 (+16,1 %) de proyección sobre lo aprobado, sin sumar el costo de esos 30 días.
- **Replanificaciones:** pasarían de 0 a 1.

### Lo que no sé
Quién pide el cambio y por qué; el costo de 30 días más; qué hito es la «salida a producción»; quién puede aprobarlo; y qué otros proyectos dependen de este.

### Después
Puedo llevarlo a comité con el paquete de decisión (`/steering-pack`) o, si ya lo aprobó quien podía, registrar la línea base 2.

La corrida quedó registrada (`2026-10-22-change-control-1`, 40 s). La salida completa está en `estado/corridas/salida-change-control.md`.

*Pie de rigor: borrador de trabajo, no decisión ni asesoría. Cada dato sale de la ficha PRY-206 y de sus documentos citados (acta 2026-04-11, cronograma v1, informe de avance 2026-10-15, comité 2026-10-17). La verificación es de quien lo lea.*