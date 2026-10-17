# /criterio-portfolio:portfolio-server rato

Rostrum está corriendo, en modo «para mirarlo un rato», en **http://127.0.0.1:8789/**. Solo se ve desde este equipo.

- **Puerto:** el 8787 y el 8788 ya estaban ocupados. En el 8788 responde otro servidor con otro informe (productos `pagos-qr`, `recaudos`…). Tomé la sugerencia de probar otro puerto y usé el 8789.
- **Términos:** ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-17). No hizo falta pedirlos de nuevo.
- **Informe:** sirve lo que ya había en `reportes/`: 13 proyectos y 6 productos. El informe es del 2026-10-17 23:02 UTC. Si cambia algo, hay que correr `/portfolio-report html` antes de que el servidor lo muestre.

**Qué hay en cada ruta**
- `/` es la portada, con el formulario de peticiones.
- `/pmo` muestra cómo va el portafolio. Responde con una redirección (302), así que se abre bien en el navegador.
- `/decisiones` es lo que necesita decisión del comité.
- `/proyectos` y `/p/<código>` son el listado y el informe de cada proyecto, con enlace a su producto.
- `/productos` y `/producto/<nombre>` son lo mismo por producto, con enlace a los proyectos que lo construyen.
- `/corridas` son las 32 corridas registradas. Es la evidencia que muestra el portal.
- `/estado.json` dice de cuándo es el informe y cuántas peticiones hay abiertas (hoy, 0).

**Lo que no hace:** no calcula, no escribe fichas, no autentica y no manda correos. Lo único que crea son las peticiones del formulario, en `estado/peticiones/`.

**A quién pasarle el enlace:** a nadie todavía. `127.0.0.1` solo lo abre quien esté sentado en este equipo, y el servidor se apaga con la sesión. Para que un patrocinador tenga un enlace estable hay que pasar a «que quede corriendo». Eso significa pedirle a la organización un host, un puerto y que lo publique detrás de su control de acceso, porque el servidor no autentica. Cuando eso exista, el enlace mostrará un informe tan viejo como la última vez que se regeneró.

**Registro:** lo mostrado quedó en `estado/corridas/salida-portfolio-server.md`. La corrida quedó registrada como `2026-10-17-portfolio-server-1`, con la nota «puerto 8787, informe en reportes/, modo rato». La nota dice 8787 y el servidor quedó en el 8789, porque registré la corrida antes de levantarlo y no la corregí. El registro del servidor está en `/tmp/claude-0/-home-claude-banco-ronda-8-mineria-espacio/692b0e4d-0e89-5e8d-a391-2cabbf233557/scratchpad/rostrum.log`.