# /criterio-portfolio:portfolio-server rato

Rostrum quedó levantado en **http://127.0.0.1:8817/**, no en el 8787 que sugiere el comando. Lo comprobé con `/estado.json`: lista los 13 proyectos y los 6 productos de `reportes/`.

- **Puertos:** el 8787 y el 8788 ya los tenían otros servidores. Sirven informes distintos al de `reportes/` (otros productos y otra hora de generación), así que no abra esos dos.
- **Términos:** ya estaban vigentes (versión 0.3.8, aceptados por José Francisco Ñáñez el 2026-10-15), y no hizo falta registrarlos otra vez.
- **Modo:** «para mirarlo un rato», como pidió el argumento. Escucha solo en este equipo, no autentica y no manda nada. Para pararlo hay que matar su proceso, porque corre en segundo plano y no tiene Ctrl-C.
- **Rutas:** `/` portada y formulario de peticiones, `/pmo`, `/decisiones`, `/proyectos`, `/productos`, `/p/<código>`, `/producto/<nombre>`, `/corridas` y `/estado.json`.
- **Enlace:** solo lo abre quien esté en este equipo, así que no se le pasa a nadie. Un patrocinador necesita la segunda forma, «que quede corriendo». Para eso hay que pedir a la organización un host y un puerto en la red, publicarlo detrás de su control de acceso y que el equipo siga encendido.
- **Informe:** es del 2026-10-15 y queda desactualizado cuando cambie un documento o corra otro barrido. Antes de mandarle algo al patrocinador, regenérelo con `/portfolio-report html`.
- **Registro:** dejé lo mostrado en `estado/corridas/salida-portfolio-server.md` y registré la corrida `2026-10-15-portfolio-server-1`. Esos archivos dicen 8787, que fue el puerto previsto, no el que quedó.