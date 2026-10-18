# /criterio-portfolio:portfolio-server rato

Rostrum ya estaba corriendo en `http://127.0.0.1:8787/` cuando intenté levantarlo, y está sirviendo el informe de este portafolio. Por eso mi arranque falló con "puerto ocupado". No toqué ese proceso, no sé quién lo lanzó, y no lo dejé corriendo yo.

- **Qué respondió:** la portada dio 200. `/estado.json` da el informe generado el 2026-10-18 a las 01:50 UTC, con los 13 proyectos (PRY-199 a PRY-211), 9 productos y 0 peticiones abiertas. `/pmo` respondió 302 (redirección) y no seguí hacia dónde.
- **Términos:** ya estaban vigentes (versión 1.1, aceptada por José Francisco Ñáñez el 2026-10-17), así que no los mostré ni registré nada nuevo.
- **Modo:** elegí "para mirarlo un rato", que es lo que pedía el argumento `rato` y el camino por defecto.
- **Si el puerto se libera:** el comando es `servidor.py --informe /home/claude/banco/ronda-9/cooperativas/espacio/reportes --estado /home/claude/banco/ronda-9/cooperativas/espacio/estado --config /home/claude/banco/ronda-9/cooperativas/espacio/.criterio/portafolio/config.json`, con `--puerto 8788` si 8787 sigue ocupado.
- **A quién pasarle el enlace:** a nadie. Solo funciona en este equipo, así que no sirve para un patrocinador. Para eso haría falta "que quede corriendo", que implica pedir host, puerto y control de acceso a la organización. Esa conversación queda aparte.
- **Cuándo se desactualiza el informe:** desde mañana, porque hay barrido diario. El comité del 2026-10-24 es el próximo, así que conviene regenerarlo antes con `/portfolio-report html`.
- **Corrida registrada:** `estado/corridas/salida-portfolio-server.md`, con el id `2026-10-17-portfolio-server-1`. El comando de registro imprimió además los hallazgos de todo el portafolio (52 en total), que no son de esta corrida.