# /criterio-portfolio:portfolio-server rato

Rostrum está corriendo en **http://127.0.0.1:8788/**, no en el 8787. Ese puerto ya lo ocupaba otro proceso con un informe distinto: 9 productos, contra los 8 de `reportes/`. No lo toqué.

Los términos ya estaban vigentes (versión 1.1, aceptada por José Francisco Ñáñez el 2026-10-15), así que no hubo que registrar nada. Había informe HTML en `reportes/`, con 13 proyectos y 8 productos. Elegí la forma «para mirarlo un rato» porque el argumento fue `rato`.

| Ruta | Qué es | Para quién |
|---|---|---|
| `/` | Portada con las secciones y el formulario de peticiones | Todos |
| `/pmo` | Cómo va el portafolio: verdes sin sustento, silencios, patrocinadores repetidos | La PMO |
| `/decisiones` | Lo que necesita decisión, con la consecuencia de no decidir | Comité y patrocinador |
| `/proyectos` | Listado ordenado por lo que más pide atención | Todos |
| `/p/<código>` | Informe de un proyecto, con enlace a su producto | Quien gerencia |
| `/productos` | Listado de productos y proyectos sin producto declarado | Quien responde por un producto |
| `/producto/<nombre>` | Informe de un producto, con enlace a sus proyectos | Quien responde por un producto |
| `/estado.json` | Fecha del informe y peticiones abiertas | Un mecanismo |

El arranque también imprimió `/corridas` (31), una ruta que no está en la guía del comando.

- **Alcance:** solo escucha en este equipo, así que el enlace no sirve para un patrocinador. Se apaga con Ctrl-C o matando el proceso.
- **Qué no hace:** no calcula, no escribe fichas, no autentica y no manda correos. El formulario solo deja una petición en `estado/peticiones/`, que por ahora tiene 0 abiertas.
- **Frescura del informe:** es del 2026-10-15 y queda desactualizado cuando cambien las fichas o los documentos. Para refrescarlo hay que correr `/portfolio-report html`.
- **Para un enlace estable:** haría falta la segunda forma, «que quede corriendo». Habría que pedirle a la organización un host y puerto internos, y publicarlo detrás de su control de acceso.

La corrida quedó registrada como `2026-10-15-portfolio-server-1`, con la salida en `estado/corridas/salida-portfolio-server.md`. El proceso del servidor sigue vivo y su registro está en `/tmp/claude-0/-home-claude-banco-ronda-2-cooperativas-espacio/692b0e4d-0e89-5e8d-a391-2cabbf233557/scratchpad/rostrum.log`.

La nota de la corrida y el archivo de salida dicen puerto 8787, porque los escribí antes de ver que estaba ocupado. El puerto real es el 8788.