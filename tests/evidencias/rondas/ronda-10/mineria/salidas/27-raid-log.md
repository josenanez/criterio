# /criterio-portfolio:raid-log portafolio

## RAID del portafolio al 2026-10-18

El registro de los 13 proyectos tiene 12 riesgos, 13 incidencias y 9 dependencias, más 1 dependencia sin registrar que salió de las notas de PRY-203. No hay ningún supuesto. Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-18), así que no los registré de nuevo.

Salió de las 13 fichas, las 13 actas de constitución y 14 documentos de reunión. No releí los informes de avance enteros: usé lo que recogen las fichas. PRY-201, 205, 206, 207 y 210 no tienen minutas en la carpeta, así que en esos cinco no pude buscar riesgos dichos en reunión.

- **Reclasificados:** 9 de los 21 «riesgos» eran dependencias, porque dependen de alguien fuera del proyecto. Son 6 de «ventana de parada de planta» (Operaciones) y 3 de «proveedor sin fecha» (PRY-201, 208 y 211).
- **Sin doliente ni fecha:** ninguno de los 35 ítems trae doliente, fecha, probabilidad ni impacto. Lo reporto como hallazgo y no lo rellené.
- **No registrado formalmente:** en las notas de PRY-203 del 2026-10-18 se dijo que el proveedor podría no llegar con el equipo completo. Es el único hallazgo de reuniones; en las otras 13 minutas solo hay compromisos.
- **Las decisiones que subo:**
  - Operaciones debe fijar una ventana de parada única. La misma frase aparece en 10 de los 13 proyectos, pero los documentos no dicen si es la misma parada.
  - PRY-208 (en rojo) necesita fecha del proveedor antes de resolver su CC-01.
  - PRY-211 y PRY-201 necesitan que el proveedor confirme fecha. En PRY-201 el montaje figura cumplido pero la última entrega sigue sin fecha.
  - PRY-200 perdió dos semanas por la rotación de un ingeniero clave y sigue llevando ese riesgo como abierto.
  - PRY-205 (en rojo) tiene una incidencia sin doliente y dos cambios aprobados en una semana (+146 días y 292 millones de COP).
- **Lo que no pude medir:** no sé si hay ítems sin movimiento en dos períodos, porque no hay historial. Tampoco pude cruzar dependencias por código, porque ninguna cita un proyecto PRY.

Al final, en las tablas, hay textos repetidos que no cuadran con la fase del proyecto (PRY-199, 204, 206 y 207). Los dejo señalados para verificar con cada gerente, no como errores.

**Después:** puedo subir al comité 201-D2, 208-D1 y 211-D2 junto con el CC-01 de PRY-208, y proponer dolientes. Propondría al gerente de cada proyecto para sus ítems. Para la parada de planta no hay nombre en los documentos. No asigné nada.

La corrida quedó registrada como `2026-10-18-raid-log-1`. Duró 117 segundos y la salida está guardada tal cual. Tiene una limitación: el conteo de 47 hallazgos de señales que devolvió el script viene de las señales de portafolio ya abiertas, no del RAID de esta corrida.

Archivos en `/home/claude/banco/ronda-10/mineria/espacio/estado/corridas/`:
- `salida-raid-log.md`