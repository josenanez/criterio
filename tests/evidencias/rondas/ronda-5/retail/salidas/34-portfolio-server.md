# /criterio-portfolio:portfolio-server rato

Rostrum arrancó bien en `http://127.0.0.1:8787/`, pero el comando que lo lanzó venció a los 8 segundos y el servidor ya no está corriendo. Para volver a levantarlo, corre esto en una terminal y déjala abierta:

```
python3 "/home/claude/banco/criterio/plugins/criterio-portfolio/scripts/servidor.py" --informe reportes --estado estado --config .criterio/portafolio/config.json
```

- **Términos:** ya estaban vigentes (versión 1.1, aceptados por José Francisco Ñáñez el 2026-10-16), así que no volví a pedirlos.
- **Modo:** «para mirarlo un rato», que es la respuesta sugerida. El servidor escucha solo en este equipo y se para con Ctrl-C. Si el puerto está ocupado, añade `--puerto 8788`.
- **Qué sirve:** el informe de `reportes/` (13 proyectos, 7 productos, 32 corridas), con el nombre «Portafolio retail».
  - `/pmo`: cómo va el portafolio.
  - `/decisiones`: lo que necesita una decisión.
  - `/proyectos` y `/p/<código>`: el listado y el informe de cada proyecto.
  - `/productos` y `/producto/<nombre>`: el listado y el informe de cada producto.
  - `/corridas`: las corridas registradas.
  - `/estado.json`: de cuándo es el informe y cuántas peticiones hay abiertas.
- **Qué no hace:**
  - No calcula nada: sirve lo que el informe ya escribió.
  - No escribe fichas: solo crea las peticiones del formulario, en `estado/peticiones/`.
  - No autentica.
  - No manda nada.
- **Qué enlace pasar a quién:** ninguno todavía. Este enlace solo funciona en este equipo y mientras el proceso esté vivo, así que sirve para mirar, no para mandárselo al patrocinador. Para un enlace estable hace falta el modo «que quede corriendo» (`--abierto`, detrás del control de acceso de la organización).
- **Cuándo se desactualiza:** el informe es del 2026-10-16 (generado a las 11:49). Queda viejo en cuanto cambie un documento o corra otro barrido, y la portada muestra su fecha.
- **Corrida:** quedó registrada como `2026-10-16-portfolio-server-1`, con su salida en `estado/corridas/salida-portfolio-server.md`.