# /criterio-portfolio:portfolio-server rato

Rostrum está corriendo en modo «para mirarlo un rato» en **http://127.0.0.1:8790/**, solo en este equipo. Lo comprobé: `/estado.json` responde con los 13 proyectos y los 7 productos de este portafolio, y no hay peticiones abiertas.

- **Modo:** elegí «rato» porque ese fue el argumento y nadie podía responder la pregunta de modo.
- **Términos:** ya estaban vigentes, porque la aceptación a nombre de José Francisco Ñáñez está registrada en la configuración para la versión 0.3.13. No hizo falta volver a aceptarlos.
- **Informe:** ya existía en `reportes/`, así que el servidor solo lo sirve.
- **Puerto:** el 8787 estaba ocupado. El 8788 también, y lo que responde ahí es otro servidor, con productos bancarios que no son de este portafolio. Por eso usé el 8790.
- **Corrida:** quedó registrada como `2026-10-17-portfolio-server-1`. La nota de esa corrida dice «puerto 8787» y es inexacta. El archivo `estado/corridas/salida-portfolio-server.md` sí lo corregí y dice 8790.

Rutas del portal:

| Ruta | Qué muestra |
|---|---|
| `/` | La portada, con el formulario de peticiones |
| `/pmo` | Cómo va el portafolio, mirando todo junto |
| `/decisiones` | Lo que necesita una decisión, para el comité y el patrocinador |
| `/proyectos` | Los proyectos, ordenados por lo que más pide atención |
| `/p/<código>` | El informe de un proyecto, con enlace a su producto |
| `/productos` | Los productos, y los proyectos que no dicen cuál construyen |
| `/producto/<nombre>` | El informe de un producto, con enlace a los proyectos que lo construyen |
| `/corridas` | Las corridas registradas |
| `/estado.json` | De cuándo es el informe y cuántas peticiones hay abiertas |

**A quién pasarle qué:** todavía a nadie. El enlace solo funciona en este equipo y deja de funcionar cuando se apague el servidor. Para el patrocinador hace falta la forma «que quede corriendo», con `--abierto`. Eso exige pedirle a la organización un host y un puerto, publicarlo detrás de su control de acceso (el servidor no autentica, a propósito) y mantener el equipo encendido.

El informe es del 2026-10-17. Quedará desactualizado en cuanto cambie un documento y no se vuelva a correr `/portfolio-report html`; la portada muestra su fecha.

Rostrum no calcula ni escribe fichas, no autentica y no manda correos. Lo único que escribe son las peticiones, en `estado/peticiones/`.