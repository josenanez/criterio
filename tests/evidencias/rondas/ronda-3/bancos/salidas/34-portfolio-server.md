# /criterio-portfolio:portfolio-server rato

Rostrum arranca bien en modo «rato». No lo dejé corriendo, porque esta sesión no tiene interfaz y el proceso no termina por sí solo. Lo comprobé con un arranque de 4 segundos, que salió con código 124, el que da `timeout` al cortarlo.

**Términos:** ya estaban vigentes, versión 1.1, aceptados por José Francisco Ñáñez el 2026-10-15. El comprobante está en `.criterio/terminos/`, así que no registré nada nuevo.

**Forma elegida:** «para mirarlo un rato». Al no haber nadie que respondiera, tomé la respuesta sugerida: empezar por esta forma, que no necesita infraestructura ni hablar con seguridad.

**Para levantarlo** (desde `/home/claude/banco/ronda-3/bancos/espacio`):
```
python3 "/home/claude/banco/criterio/plugins/criterio-portfolio/scripts/servidor.py" --informe reportes --estado estado --config .criterio/portafolio/config.json
```
Escucha en `127.0.0.1:8787`, solo en este equipo, y se para con Ctrl-C. Si el puerto está ocupado, añade `--puerto 8788`.

Rutas disponibles:
- `/`: la portada, con el formulario de peticiones.
- `/pmo`: cómo va el portafolio.
- `/decisiones`: lo que necesita una decisión del comité.
- `/proyectos`: 13 proyectos.
- `/productos`: 9 entradas.
- `/corridas`: 32 corridas.
- `/estado.json`: la frescura del informe y las peticiones abiertas.

**Lo que no hace:**
- No calcula nada: sirve lo que el informe ya escribió.
- No escribe fichas; solo crea peticiones en `estado/peticiones/`.
- No autentica ni manda correos.
- No puede correr el agente: las peticiones esperan a `/portfolio-wake`.

**Corrida registrada:** `2026-10-15-portfolio-server-1`, con el texto mostrado en `estado/corridas/salida-portfolio-server.md`.

**Qué enlace pasar:** ninguno todavía. `http://127.0.0.1:8787/` solo funciona en este equipo y mientras el proceso esté vivo, así que no sirve para un patrocinador. Para un enlace estable mañana hace falta la forma «que quede corriendo», con `--abierto`, un host y puerto internos, y el control de acceso de la organización.

Sobre la fecha del informe: la portada muestra de cuándo es. Las peticiones que lleguen por el formulario no se contestan solas.