# /criterio-portfolio:raid-log portafolio

Levanté el RAID del portafolio: 35 ítems en 13 proyectos, y ninguno tiene doliente ni fecha de resolución.

Salió de las 13 fichas y de las 13 actas o notas de reunión que pude leer. Los informes en PDF los tomé de las fichas, no los releí. Los términos ya estaban vigentes (v1.1), aceptados por José Francisco Ñáñez el 2026-10-15. La corrida quedó registrada como `2026-10-15-raid-log-1`, con el registro completo en `estado/corridas/salida-raid-log.md`.

| Tipo | Cantidad |
|---|---|
| Riesgos | 16 |
| Incidencias | 15 |
| Dependencias | 4 |
| Supuestos | 0 |

- **Reclasificados:** las 4 dependencias eran riesgos en la ficha. Tres son "el proveedor no ha confirmado la fecha de la última entrega" (PRY-199, 201, 203). La cuarta es el proveedor de PRY-205, que podría no llegar con el equipo completo. Todas son declaradas, no acordadas, y ninguna depende de otro proyecto del portafolio.
- **Incidencia añadida:** el informe de PRY-201 dice que el despliegue se reprogramó por el congelamiento de fin de año, pero la ficha no lo tenía. Lo añadí.
- **Riesgos ya materializados:** "congelamiento de cambios en temporada alta" sigue como riesgo en PRY-201 y PRY-209, pero el mismo informe dice que el despliegue ya se reprogramó. Hay que pasarlos a incidencia.
- **No registrado formalmente:** solo uno. En la reunión de PRY-205 del 2026-10-15 se comentó que el proveedor podría no llegar con el equipo completo, y nadie lo anotó. Las otras actas solo traen compromisos; no inventé más.

Esto es lo que propongo subir al comité del 2026-10-22, con un doliente propuesto (no asignado) por proyecto:
1. **Hallazgo de seguridad en los medios de pago:** aparece en PRY-201 y PRY-206, sin doliente. PRY-206 lo reporta en verde. El texto es idéntico en ambos y no sé si es el mismo hallazgo.
2. **Prueba de carga de temporada que no alcanzó el umbral:** PRY-199 (declarado verde con 20% de avance), PRY-204 y PRY-208.
3. **Congelamiento de cambios:** pasar a incidencia el riesgo de PRY-201 y PRY-209.

Lo que no sé:
- Si algún ítem lleva dos períodos sin movimiento, porque las fichas no guardan esa fecha.
- Si varias frases repetidas palabra por palabra entre proyectos (por ejemplo la validación con dos tiendas) son hechos distintos o texto copiado.
- Si existen dependencias entre proyectos: ningún documento declara ninguna.

Fuera del RAID, de pasada: hay compromisos vencidos (PRY-204, 207, 208 y el de Beatriz Cuéllar en PRY-211). Las solicitudes de cambio de PRY-208 y PRY-211 siguen pendientes de comité.