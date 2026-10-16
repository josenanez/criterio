# /criterio-portfolio:portfolio-server rato

Rostrum está corriendo en **http://127.0.0.1:8791/**, solo en este equipo. Lo levanté en modo «para mirarlo un rato», que es lo que pedía el argumento `rato`.

- **Términos:** ya estaban vigentes (versión 1.1, aceptada por José Francisco Ñáñez el 2026-10-16). No pedí un nuevo sí ni escribí otro comprobante.
- **Puerto:** el 8787 y el 8788 estaban ocupados por otros servidores. Sus listas de productos no coinciden con esta carpeta, así que no eran el nuestro. Usé el 8791 y comprobé que `/estado.json` muestra los 13 proyectos y los 6 productos de `reportes/`.
- **Qué muestra:** la portada con sus secciones, `/pmo`, `/decisiones`, `/proyectos`, `/productos` y `/corridas`. El nombre de la organización sale como «Portafolio de proyectos». No hay peticiones abiertas.
- **Qué no hace:** no calcula, no escribe fichas, no autentica y no manda correos. El formulario solo deja peticiones en `estado/peticiones/`.
- **Registro:** guardé lo mostrado en `estado/corridas/salida-portfolio-server.md` y registré la corrida como `2026-10-16-portfolio-server-1`. La nota de la corrida dice «puerto 8787»; el puerto real fue el 8791. Corrí el registro antes de saber qué puerto quedaría libre, y la nota quedó así.
- **Enlace:** `127.0.0.1` solo sirve en este equipo, así que no se lo puedes pasar al patrocinador. El informe es de hoy y queda desactualizado si cambia algún documento. Entonces hay que volver a correr `/portfolio-report html`.
- **Para un enlace estable:** el paso siguiente es «que quede corriendo» con `--abierto`. Eso exige pedirle a la organización un host, un puerto y su control de acceso, porque el servidor no autentica.

El servidor sigue en segundo plano. Se apaga terminando el proceso `servidor.py` del puerto 8791; el registro está en `/tmp/claude-0/rostrum.log`.