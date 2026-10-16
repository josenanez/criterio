# /criterio-portfolio:portfolio-server rato

Rostrum arrancó en `http://127.0.0.1:8787/` y lo paré a los 8 segundos, porque lo corrí con tiempo límite. Para tenerlo en marcha, lanza esta línea en tu terminal:

```
python3 "/home/claude/banco/criterio/plugins/criterio-portfolio/scripts/servidor.py" --informe /home/claude/banco/ronda-4/mineria/espacio/reportes --estado /home/claude/banco/ronda-4/mineria/espacio/estado --config /home/claude/banco/ronda-4/mineria/espacio/.criterio/portafolio/config.json
```

- **Términos:** ya estaban vigentes (versión 1.1, aceptados por José Francisco Ñáñez el 2026-10-15), así que no hubo que registrar nada nuevo.
- **Modo:** elegí «para mirarlo un rato», la respuesta sugerida. Escucha solo en este equipo y se apaga con Ctrl-C. Si el puerto 8787 está ocupado, agrega `--puerto 8788`.
- **Qué se ve:** el arranque listó la portada, `/pmo`, `/decisiones`, `/proyectos` (13), `/productos` (6), `/corridas` (32) y `/estado.json`. Los informes de proyecto y de producto cuelgan de `/p/<código>` y `/producto/<nombre>`.
- **Lo que no hace:** no calcula, no escribe fichas, no autentica y no manda correos. Lo único que crea son las peticiones del formulario, en `estado/peticiones/`.
- **A quién le sirve el enlace:** `127.0.0.1` solo funciona en este equipo. Para que el patrocinador tenga un enlace estable hace falta «que quede corriendo» (`--abierto`). Eso exige pedirle a la organización un host y un puerto dentro de la red, publicados detrás de su control de acceso, porque el servidor no autentica. Antes de mandarle el enlace a nadie, conviene que sepa que el informe vale hasta la fecha en que se generó, y la portada la muestra.
- **Registro:** la salida quedó en `estado/corridas/salida-portfolio-server.md` y la corrida en `2026-10-15-portfolio-server-1`.