# /criterio-server:server-start rato

Rostrum está corriendo en `http://127.0.0.1:8787/`, solo en este equipo y en modo «para mirarlo un rato». Lo dejé en segundo plano, con el registro en `/tmp/claude-0/-tmp-claude-0--home-claude-692b0e4d-0e89-5e8d-a391-2cabbf233557-scratchpad-r11-mineria-espacio/692b0e4d-0e89-5e8d-a391-2cabbf233557/scratchpad/rostrum.log`.

**Términos.** Ya estaban vigentes (versión 1.2, aceptada para 0.8.0) y registrados a nombre de José Francisco Ñáñez con fecha 2026-10-23. No volví a registrar nada. Los términos completos están en https://www.josenanez.com/es/agents/criterio-pmo/legal. En corto, Criterio produce borradores, no decisiones ni asesoría, y cada dato lleva la cita del documento de donde sale, así que la verificación es de quien lo usa.

**Mapa contra disco.** No hay entradas nuevas, ni desaparecidas, ni sin estado. Las tres entradas son Vera (`portafolio`), Samuel (`proyecto/PRY-204`) y Alba (`producto/PRD-309`), todas de la familia PMO.

**Qué hay y para quién:**
- **`/`**: la portada, con los tres agentes y el formulario de peticiones. Es para todos.
- **`/pmo`, `/decisiones`**: el informe de la PMO y el material del comité. Es para la PMO, el comité y el patrocinador.
- **`/proyectos`**: 13 proyectos (PRY-199 a PRY-211).
- **`/productos`**: 6 productos.
- **`/corridas`**: 33 corridas registradas, para quien audita.
- **`/estado.json`**: para un mecanismo, no para una persona.
- **`/caso/<código>`**: todo lo que los agentes hicieron sobre un caso.
- **`/vence`**: lo pendiente con fecha. No aparece en las direcciones que imprimió el servidor y no lo probé.
- **`/familia/cfo` y `/familia/clo`**: no existen aquí, porque el mapa solo tiene la familia PMO.

**Frescura.** El informe de la PMO es del 2026-10-23, 13:27 UTC. Los tres agentes aparecen con `ultimo: null` (sin corrida registrada), con 0 peticiones abiertas y sin próxima corrida programada. El portal los muestra como pendientes y no les inventa nada.

**Qué enlace pasar a quién.** Con este modo, ninguno funciona fuera de este equipo ni mañana:
- Patrocinador: `/`, o `/pmo` si solo quiere el informe.
- Comité: `/decisiones`.
- Gerencia: `/vence`, si abre.

Para tener un enlace estable hay que cambiar a «que quede corriendo». Se pide un host y un puerto dentro de la red y publicarlo detrás del control de acceso que la organización ya usa, porque el servidor no autentica. No necesita nada más. Con el servidor funcionando, se arranca con `--abierto`.

Para pararlo: `pkill -f servidor.py`.