# /criterio-portfolio:portfolio-server rato

Rostrum arrancó en el puerto 8790. Lo paré a los 5 segundos, porque esta sesión no tiene a nadie mirando; el código 124 es ese corte, no un fallo.

Los puertos 8787 y 8788 ya estaban ocupados, así que usé el 8790. El 8789 no lo probé.

**Para levantarlo de nuevo y dejarlo abierto:**
```
python3 "/home/claude/banco/criterio/plugins/criterio-portfolio/scripts/servidor.py" --informe reportes --estado estado --config .criterio/portafolio/config.json --puerto 8790
```
Escucha solo en este equipo (127.0.0.1) y se para con Ctrl-C.

**Qué hay y a quién le sirve:**
- **`/`:** portada con las tres secciones y el formulario de peticiones.
- **`/pmo`:** cómo va el portafolio, para la PMO.
- **`/decisiones`:** lo que necesita decisión, para el comité y el patrocinador.
- **`/proyectos` (13), `/productos` (6) y `/corridas` (31):** los listados.
- **`/estado.json`:** de cuándo es el informe y cuántas peticiones hay abiertas.

**Lo que Rostrum no hace:** no calcula, no escribe fichas, no autentica y no manda correos. Solo crea las peticiones en `estado/peticiones/`.

**Qué enlace pasar a quién:** en este modo el enlace solo funciona en este equipo, así que no se le puede pasar al patrocinador. Para eso haría falta «que quede corriendo» con `--abierto`. Eso exige pedirle a la organización un host y puerto internos, publicarlo detrás de su control de acceso y mantener el equipo encendido; nada más. El informe es del 2026-10-17 y queda desactualizado en cuanto cambie un documento o se corra otro barrido. La portada muestra su fecha.

Los términos ya estaban vigentes (versión 1.1, aceptados por José Francisco Ñáñez el 2026-10-17), así que no hubo que registrar nada. Dejé la corrida registrada como `2026-10-17-portfolio-server-1`, con la salida en `estado/corridas/salida-portfolio-server.md`. Esa salida dice 8787, que el puerto ocupado me obligó a cambiar. No la reescribí, y la nota de la corrida también dice 8787.