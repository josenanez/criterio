# /criterio-portfolio:portfolio-server rato

Rostrum está listo para levantar en modo «para mirarlo un rato», pero no lo arranqué. El servidor no termina y esta sesión no tiene interfaz, así que no pude comprobar que responde.

- **Términos:** ya estaban vigentes (versión 1.1, aceptada el 2026-10-17 por José Francisco Ñáñez), así que no pedí nada de nuevo.
- **Informe:** `reportes/` tiene 23 páginas ya generadas: `index.html`, `decisiones.html`, una por proyecto y una por producto.
- **Modo:** «rato», porque ese fue el argumento. Escucha solo en `127.0.0.1:8787`.
- **Registro:** guardé lo que le mostraría a la persona en `estado/corridas/salida-portfolio-server.md` y registré la corrida como `2026-10-17-portfolio-server-1`.

Para levantarlo, corra esto en una terminal y páralo con Ctrl-C:

```
python3 "/home/claude/banco/criterio/plugins/criterio-portfolio/scripts/servidor.py" --informe /home/claude/banco/ronda-7/mineria/espacio/reportes --estado /home/claude/banco/ronda-7/mineria/espacio/estado --config /home/claude/banco/ronda-7/mineria/espacio/.criterio/portafolio/config.json
```

Si el puerto está ocupado, añada `--puerto 8788`.

- **Rutas:**
  - `/`: portada con las tres secciones y el formulario de peticiones.
  - `/pmo`: cómo va el portafolio.
  - `/decisiones`: lo que necesita una decisión.
  - `/proyectos` y `/p/<código>`: el listado de proyectos y el informe de cada uno.
  - `/productos` y `/producto/<nombre>`: lo mismo para productos.
  - `/estado.json`: de cuándo es el informe y cuántas peticiones hay abiertas.
- **Enlace:** `http://127.0.0.1:8787/` solo sirve en este equipo. No se lo pase a un patrocinador.
- **Para el patrocinador:** hace falta pasar a «que quede corriendo» (`--abierto`). Eso pide un host y un puerto dentro de la red, publicarlo detrás del control de acceso que ya usan y mantener el equipo encendido. El servidor no autentica, y eso es a propósito.
- **Desactualización:** el informe es del 2026-10-17 y el comité es el 2026-10-23. Conviene regenerarlo con `/portfolio-report html` antes de esa fecha.
- **Qué no hace Rostrum:** no calcula nada, no escribe fichas (solo crea las peticiones en `estado/peticiones/`) y no envía correos ni notificaciones.