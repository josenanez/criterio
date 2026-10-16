# /criterio-portfolio:portfolio-scan 

Barrido terminado. Creé 10 fichas nuevas, todas selladas, y los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-16), así que no los registré de nuevo.

**Documentos:** 77 en la carpeta, 50 leídos, 27 sin cambio y 0 ilegibles. Los 27 sin cambio son los de PRY-200, PRY-202 y PRY-210, que ya tenían ficha. El plan cabía en un solo lote de 10 proyectos, leído en esta conversación sin subagentes.

**Fichas nuevas:** PRY-199, 201, 203, 204, 205, 206, 207, 208, 209 y 211.

**Campos en `not_found`:**
- La facultad del gerente y la etapa faltan en los 10.
- El producto falta en PRY-201, 205, 206, 209 y 211, porque sus actas dicen «No aplica».

**Señales del cálculo:** son 32 en los 10 proyectos nuevos.
- **Verdes contradichos:** PRY-205, 206, 208 y 211.
- **Fechas movidas sin autorización:** PRY-203 (66 días) y PRY-211 (70 días), ambos con la solicitud de cambio CC-01 pendiente de comité.
- **PRY-204:** tiene un compromiso vencido.
- **PRY-207:**
  - Un hito vencido, «Licencia y permisos obtenidos».
  - Un entregable de proveedor atrasado 33 días (contrato CT-858).
- **PRY-199 y PRY-209:** no tienen señales. PRY-209 no tiene cronograma, así que no hay contra qué medir atraso.
- **Hitos cerrados sin acta de recibo:** aparecen en 8 de los 10 proyectos.

**Cosas que registré tal cual, con nota:**
- En PRY-203 y PRY-205 el informe declara comprometido menor que ejecutado.
- En PRY-204 el compromiso vencido lleva una fecha anterior a la reunión donde se dijo.
- La fecha de cierre calculada es la del último hito, no la del acta, y difieren en 8 proyectos. Conviene confirmar cuál cuenta.

**Movidos o pendientes:** no existe carpeta `entrada/`, así que no moví nada. Sigue pendiente el archivo suelto de PRY-200 (`2026-10-16-notas-reunion.txt`), que no toqué.

Fallos de la corrida:
- En una llamada junté dos comandos con `&&` (al escribir y sellar PRY-201), lo que el comando pedía evitar. No cambió el resultado.
- El registro de la corrida dice `sin_cambio: 77, releidos: 0`, que no refleja los 50 que sí leí. Lo dejo como lo midió el script.
- La corrida midió 261 segundos. La estimación de 25 a 30 minutos que di en el arranque quedó muy por encima.

La salida completa quedó en `estado/corridas/salida-portfolio-scan.md`, y la corrida en `estado/corridas/` con el id `2026-10-16-portfolio-scan-1`. Hay más de un proyecto, así que el siguiente paso sería `/criterio-portfolio:portfolio-report`.

*criterio-portfolio 0.3.11 · fichas tocadas: 10 · Términos: https://www.josenanez.com/es/agents/criterio-pmo/legal#v0.3.11*