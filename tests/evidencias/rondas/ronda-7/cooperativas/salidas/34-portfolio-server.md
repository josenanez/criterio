# /criterio-portfolio:portfolio-server rato

Rostrum está corriendo en `http://127.0.0.1:8787/`, en modo «para mirarlo un rato». Lo abrí con `curl` a `/estado.json` y respondió. No miré las otras páginas ni abrí ningún navegador.

- **Pregunta del modo:** nadie podía responder, así que tomé la sugerida (empezar por «rato»).
- **Términos:** ya estaban vigentes (versión 1.1, aceptada por José Francisco Ñáñez el 2026-10-17), así que no los volví a pedir.
- **Quién lo ve:** solo este equipo (`127.0.0.1`). El proceso quedó en segundo plano y su salida va a `/tmp/claude-0/rostrum.log`. Para pararlo, termina el proceso de `servidor.py`.
- **Qué sirve:** la carpeta `reportes/` con los 13 proyectos (PRY-199 a PRY-211) y 8 productos. Lo marca como «Cooperativa» porque le pasé la configuración.
- **Rutas:** `/`, `/pmo`, `/decisiones`, `/proyectos`, `/productos`, `/corridas` (32) y `/estado.json`.
- **Peticiones:** hay 0 abiertas.
- **Registro:** la salida está en `estado/corridas/salida-portfolio-server.md` y la corrida quedó como `2026-10-17-portfolio-server-1`.

**Qué enlace a quién:** `http://127.0.0.1:8787/` solo sirve a quien lo levantó. Si el patrocinador necesita un enlace que funcione mañana, hace falta el modo «que quede corriendo». Eso requiere un host y un puerto internos, publicados detrás del control de acceso de la organización, porque el servidor no autentica. Conviene tener esa conversación con seguridad después de haberlo visto funcionar.

**Cuándo se desactualiza:** el informe es del 2026-10-17 a las 20:16 UTC. Regenéralo con `/portfolio-report html` antes del comité del 2026-10-24, con 2 días de antelación según la configuración.