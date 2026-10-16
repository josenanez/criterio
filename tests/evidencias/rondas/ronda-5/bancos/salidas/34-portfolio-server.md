# /criterio-portfolio:portfolio-server rato

Rostrum arrancó y escuchó en `http://127.0.0.1:8787`. Mi comando de prueba lo cortó a los 15 segundos, así que ahora **no está corriendo**.

Para mirarlo un rato, ejecuta esto en tu terminal. Se para con Ctrl-C:

```
python3 "/home/claude/banco/criterio/plugins/criterio-portfolio/scripts/servidor.py" --informe /home/claude/banco/ronda-5/bancos/espacio/reportes --estado /home/claude/banco/ronda-5/bancos/espacio/estado --config /home/claude/banco/ronda-5/bancos/espacio/.criterio/portafolio/config.json
```

- **Términos:** ya estaban vigentes (versión 1.1, aceptados el 2026-10-16 por José Francisco Ñáñez), así que no registré una aceptación nueva.
- **Modo:** «para mirarlo un rato», como venía en el argumento. No pregunté nada más.
- **Informe:** encontré `reportes/` con 13 proyectos y 9 productos.
- **Rutas:**
  - `/` es la portada.
  - `/pmo` y `/decisiones` son el resumen para la PMO y las decisiones del comité.
  - `/proyectos` y `/productos` son los listados.
  - `/corridas` muestra las corridas registradas.
  - `/estado.json` dice de cuándo es el informe.
- **Alcance:** escucha solo en este equipo y no trae autenticación. No escribe fichas ni manda nada; lo único que crea son las peticiones del formulario, en `estado/peticiones/`.
- **Corrida registrada:** es la `2026-10-16-portfolio-server-1`, y lo que te mostré quedó en `estado/corridas/salida-portfolio-server.md`.
- **A quién pasar el enlace:** a nadie todavía, porque `127.0.0.1` solo abre en este equipo. El informe es del 2026-10-16 y se desactualiza con el próximo barrido. El comité es el 2026-10-21.
- **Si quieres que quede corriendo:** hay que pedir a la organización un host y un puerto, y publicarlo detrás de su control de acceso con `--abierto`.