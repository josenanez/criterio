# /criterio-portfolio:portfolio-server rato

Rostrum está corriendo en modo «para mirarlo un rato» en `http://127.0.0.1:8787/`. Solo es accesible desde este equipo.

- **Términos:** ya estaban vigentes (versión 1.1, aceptada por José Francisco Ñáñez el 2026-10-17), así que no hubo que pedirlos de nuevo.
- **Modo:** no había nadie a quien preguntar, y el argumento era `rato`.
- **Servidor:** sirve la carpeta `reportes/`, que ya tenía informe, con el nombre «Cooperativa» en las páginas. Responde: `/estado.json` muestra 13 proyectos, 8 productos y 0 peticiones abiertas.
- **Corrida:** quedó registrada como `2026-10-17-portfolio-server-1`. Lo que te mostré está en `estado/corridas/salida-portfolio-server.md`.
- **Informe:** es del 2026-10-17 22:19 UTC. Si lo regeneras con `/portfolio-report html`, recarga la página para verlo.

Rutas principales:

| Ruta | Para quién |
|---|---|
| `/` (portada) | Todos |
| `/pmo` | La PMO |
| `/decisiones` | El comité y el patrocinador |
| `/proyectos` y `/p/<código>` | Todos |
| `/productos` y `/producto/<nombre>` | Quien responde por un producto |
| `/corridas` | Quien quiera ver la evidencia de cada corrida |

Lo que Rostrum no hace:
- No calcula nada: sirve lo que `informe.py` ya escribió.
- No escribe fichas: lo único que crea son las peticiones del formulario, en `estado/peticiones/`.
- No autentica y no envía nada.

**Enlace para el patrocinador:** no hay todavía, porque este enlace solo sirve en este equipo. Para dárselo hace falta el modo «que quede corriendo», que exige un host, un puerto y publicarlo detrás del control de acceso de la organización. Conviene tener esa conversación con seguridad teniendo esto funcionando delante.

El servidor sigue en segundo plano y se apaga con Ctrl-C o terminando el proceso. Su salida está en `/tmp/claude-0/-home-claude-banco-ronda-8-cooperativas-espacio/692b0e4d-0e89-5e8d-a391-2cabbf233557/scratchpad/rostrum.log`.