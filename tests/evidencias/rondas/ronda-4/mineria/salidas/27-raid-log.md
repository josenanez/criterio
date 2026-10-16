# /criterio-portfolio:raid-log portafolio

El registro RAID del portafolio está hecho y la corrida quedó registrada como `2026-10-15-raid-log-1`. El texto completo está en `estado/corridas/salida-raid-log.md`, con los dos límites de abajo.

Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-15), así que no los registré de nuevo.

**Resultado**
- **Lo registrado:** 20 riesgos, 24 incidencias, 0 supuestos y 0 dependencias en los 13 proyectos (PRY-199 a PRY-211).
- **Doliente y fecha:** ninguno de los 44 ítems tiene doliente y ninguno de los 20 riesgos tiene fecha. Lo reporto como hallazgo y no lo relleno.
- **Riesgo no registrado:** encontré uno, en PRY-200. En las notas del 2026-10-15 se dijo que el proveedor podría no llegar con el equipo completo para la siguiente fase y nadie lo anotó. Ese mismo día quedó una "revisión con el proveedor" para el 2026-10-25 a cargo de Óscar Ramírez, a quien propongo como candidato a doliente, pero ninguna acta lo nombra responsable del riesgo.
- **Reclasificaciones que propongo:** pasar 7 riesgos a dependencia, sin tocar las fichas.
  - **"Ventana de parada de planta definida por operaciones"** (PRY-201, 202, 203, 205 y 210). Depende de Operaciones. PRY-199 y PRY-207 además dicen que la parada se reprogramó. Son 7 proyectos con la misma dependencia y conviene un solo interlocutor.
  - **"El proveedor no ha confirmado la fecha de la última entrega"** (PRY-204 y 206).
- **Riesgo que ya ocurrió:** en PRY-200 y PRY-205, "concentración del conocimiento en una sola persona" sigue abierto como riesgo, pero el mismo informe cuenta que el equipo perdió dos semanas por la rotación de un ingeniero clave.
- **Dudosas:** marqué 6 incidencias porque son hechos del periodo y el informe no dice qué daño causan: equipos entregados pendientes de aceptación, presupuesto actualizado con compras y parada reprogramada.

**Límites**
- No pude medir qué lleva más de dos períodos sin movimiento. Hay un solo informe por proyecto y `last_moved` está vacío en todos los riesgos.
- Ningún documento declara una dependencia de otro proyecto. Busqué códigos PRY ajenos en todo el caché y no hay ninguno, así que no hay dependencias para cruzar. Eso no prueba que no existan, solo que nadie las escribió.

Puedo subir a comité tres cosas: la dependencia compartida con Operaciones, el riesgo ya materializado de PRY-200 y PRY-205, y el riesgo de proveedor de PRY-200. Si quiere, redacto la decisión formulada de cada una; no asigné ningún doliente.