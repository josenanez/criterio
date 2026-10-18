# /criterio-portfolio:portfolio-server rato

Rostrum está corriendo en modo «para mirarlo un rato» y la portada responde 200.

- **Términos:** ya estaban vigentes para la versión 0.4.0, aceptados por José Francisco Ñáñez el 2026-10-17. No hubo que registrar nada.
- **Modo:** nadie podía responder, así que tomé la respuesta sugerida y empecé por «para mirarlo un rato».
- **Dónde:** `http://127.0.0.1:8787/`, solo en este equipo. Se para con Ctrl-C y no tiene autenticación. Está levantado en segundo plano y el registro de arranque está en `/tmp/claude-0/rostrum.log`.
- **Qué hay:**
  - Las rutas son `/`, `/pmo`, `/decisiones`, `/proyectos`, `/productos` y `/corridas`.
  - Sirve el informe de `reportes/`: 13 proyectos (PRY-199 a PRY-211) y 9 productos.
  - No escribe fichas. Solo crea peticiones en `estado/peticiones/`, y hoy hay 0 abiertas.
- **Cuándo se desactualiza:** el informe se generó el 2026-10-18 a las 01:50 UTC, según `/estado.json`. Regenéralo con `/portfolio-report html` antes de pasarle el enlace al patrocinador.
- **Para que quede corriendo:** hay que pedir `--abierto`, que no trae autenticación. La organización pone un host y un puerto internos, el control de acceso que ya usa y un equipo que no se apague. No hace falta nada más.
- **Registro de la corrida:** lo que te mostré está en `estado/corridas/salida-portfolio-server.md` y la corrida quedó como `2026-10-17-portfolio-server-1`.

El enlace `127.0.0.1` solo funciona para quien lo levantó. Un patrocinador necesita el modo «que quede corriendo».