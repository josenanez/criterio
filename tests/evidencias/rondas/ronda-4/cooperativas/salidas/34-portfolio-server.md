# /criterio-portfolio:portfolio-server rato

Rostrum no quedó corriendo: los tres puertos que probé (8787, 8788 y 8801) ya los ocupan servidores de otros portafolios. Les consulté `/estado.json` y respondieron con productos que no son los de esta Cooperativa. No toqué ninguno y no quise seguir probando puertos a ciegas.

**Lo que dejé hecho**
- **Términos:** ya estaban vigentes (versión 1.1, aceptados por José Francisco Ñáñez el 2026-10-15), así que no hizo falta registrarlos otra vez.
- **Forma:** «para mirarlo un rato», como indicaba el argumento `rato`.
- **Informe:** existe en `reportes/` (13 proyectos, 7 productos, portada, listados y decisiones). No hay `pmo.html`, así que `/pmo` puede no responder hasta que `/portfolio-report html` lo genere.
- **Registro de la corrida:** `estado/corridas/salida-portfolio-server.md` y `2026-10-15-portfolio-server-1`. Quedó registrada antes de intentar levantar el servidor.

**Para levantarlo** (elige un puerto libre; no se paró ninguno de los servidores que ocupan los tres puertos):
```
python3 "/home/claude/banco/criterio/plugins/criterio-portfolio/scripts/servidor.py" --informe /home/claude/banco/ronda-4/cooperativas/espacio/reportes --estado /home/claude/banco/ronda-4/cooperativas/espacio/estado --config /home/claude/banco/ronda-4/cooperativas/espacio/.criterio/portafolio/config.json --puerto <libre>
```
Escucha solo en este equipo y se apaga con Ctrl-C.

**Qué enlace pasar:** en este modo no hay enlace para el patrocinador, porque solo se ve desde el mismo equipo. El informe es del 2026-10-15 y la portada muestra esa fecha. Para un enlace estable hay que pedir a la organización un host y un puerto internos, publicados detrás de su control de acceso. El servidor no autentica.

La nota de la corrida dice «puerto 8787», que no es lo que pasó. No la corregí porque la corrida ya está registrada.