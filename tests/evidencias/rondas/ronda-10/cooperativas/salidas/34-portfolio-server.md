# /criterio-portfolio:portfolio-server rato

Rostrum está corriendo en modo «para mirarlo un rato» en **http://127.0.0.1:8787/**, y solo se ve desde este equipo. La portada responde 200 y `/estado.json` muestra 13 proyectos, 8 productos y 0 peticiones abiertas.

- **Términos:** ya estaban vigentes (versión 1.1, aceptados por José Francisco Ñáñez el 2026-10-18), así que no los volví a mostrar ni a registrar.
- **Modo:** elegí «para mirarlo un rato», la respuesta sugerida, porque nadie podía contestar.
- **Informe:** ya existía en `reportes/`, así que no hizo falta correr `/portfolio-report html`.
- **Secciones:**
  - `/pmo`: cómo va el portafolio.
  - `/decisiones`: lo que necesita una decisión.
  - `/proyectos` y `/p/<código>`: el listado y el informe de cada proyecto.
  - `/productos` y `/producto/<nombre>`: el listado y el informe de cada producto.
  - `/corridas`: las corridas registradas (32).
  - `/estado.json`: la frescura del informe.
- **Qué no hace:** no calcula, no escribe fichas, no autentica y no manda nada. Lo único que escribe son las peticiones del formulario, en `estado/peticiones/`.
- **Corrida registrada:** `2026-10-18-portfolio-server-1`. Lo que le mostré a la persona está en `estado/corridas/salida-portfolio-server.md`. La corrida dice «informe: null», y no entendí por qué, porque `reportes/` sí tiene informe.
- **Qué enlace pasar:** ninguno todavía. Con `127.0.0.1` el patrocinador no puede abrirlo; solo funciona en este equipo. Para un enlace estable hay que pasar a «que quede corriendo» (`--abierto`) y pedir un host y puerto internos, publicarlo detrás del control de acceso de la organización y mantener el equipo encendido.
- **Cuándo queda desactualizado:** el informe es del 2026-10-18 a las 13:26 UTC. La próxima corrida no está programada (`proxima_corrida: null`); si hace falta algo más reciente, corre `/portfolio-report html`.
- **Cómo parar:** el servidor sigue en segundo plano. Se apaga con `pkill -f servidor.py`, y su log está en `/tmp/claude-0/-home-claude-banco-ronda-10-cooperativas-espacio/692b0e4d-0e89-5e8d-a391-2cabbf233557/scratchpad/rostrum.log`.