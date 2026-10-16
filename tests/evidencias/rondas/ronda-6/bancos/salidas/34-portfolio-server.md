# /criterio-portfolio:portfolio-server rato

Rostrum está corriendo en modo «para mirarlo un rato», con una salvedad: usa el puerto **8788**, no el 8787. El 8787 ya estaba ocupado.

**Términos:** ya estaban vigentes, así que no hubo que registrarlos de nuevo. Son la versión 1.1, aceptados por José Francisco Ñáñez el 2026-10-16. El comprobante en Markdown y PDF está en `.criterio/terminos/`.

**Enlaces** (solo funcionan en este equipo):
- Portada: http://127.0.0.1:8788/
- Cómo va el portafolio, para la PMO: http://127.0.0.1:8788/pmo
- Decisiones, para el comité y el patrocinador: http://127.0.0.1:8788/decisiones
- Proyectos (13): http://127.0.0.1:8788/proyectos
- Productos (9): http://127.0.0.1:8788/productos
- Corridas (35): http://127.0.0.1:8788/corridas
- Frescura del informe: http://127.0.0.1:8788/estado.json

**Qué hay:**
- Sirve el informe que ya existe en `reportes/`; no calcula nada.
- El enlace entre proyecto y producto va en los dos sentidos.
- No escribe fichas, no autentica y no manda correos.
- El único archivo que crea es una petición, en `estado/peticiones/`. Hoy no hay ninguna abierta.
- El informe es del 2026-10-16 y queda desactualizado en cuanto cambie un documento o se corra un nuevo barrido. La portada muestra su fecha.

**Qué enlace pasar a quién:** el de la portada sirve para quien esté en este equipo. Un patrocinador remoto no puede abrirlo. Para eso hace falta la otra forma, «que quede corriendo», con `--abierto`. Eso exige pedirle a la organización un host y un puerto, y publicarlo detrás de su control de acceso, porque el servidor no autentica.

**Para apagarlo:** el servidor corre en segundo plano, así que hay que cerrar ese proceso. Su registro está en `/tmp/claude-0/-home-claude-banco-ronda-6-bancos-espacio/692b0e4d-0e89-5e8d-a391-2cabbf233557/scratchpad/rostrum.log`.

**Corrida registrada:** `2026-10-16-portfolio-server-1`, con la salida en `estado/corridas/salida-portfolio-server.md`. Registré la corrida antes de saber que el puerto 8787 estaba ocupado. La nota dice 8787 y el puerto real es 8788.