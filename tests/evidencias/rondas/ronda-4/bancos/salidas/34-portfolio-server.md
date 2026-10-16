# /criterio-portfolio:portfolio-server rato

Rostrum está corriendo para mirarlo un rato, en **http://127.0.0.1:8801/**, solo en este equipo. Lo probé con `/estado.json` y respondió.

- **Puerto:** el 8787 y el 8788 ya estaban ocupados por otros servidores que no son este. Servían informes de otros portafolios, con otros productos. Usé el 8801 y no toqué esos procesos.
- **Términos:** ya estaban vigentes (versión 1.1, aceptada por José Francisco Ñáñez el 2026-10-15), así que no volví a registrarlos.
- **Informe:** existe en `reportes/` y lo sirvo desde ahí. Trae 13 proyectos, 9 productos y 0 peticiones abiertas.
- **Corrida registrada:** la salida está en `estado/corridas/salida-portfolio-server.md`. La nota de la corrida dice puerto 8787, pero el servidor quedó en el 8801. La corrida se registró antes de levantarlo y no la corregí.

Las páginas están en estas rutas:

| Ruta | Qué muestra |
|---|---|
| `/` | La portada |
| `/pmo` | Cómo va el portafolio |
| `/decisiones` | Lo que necesita decisión del comité |
| `/proyectos` | Los 13 proyectos |
| `/productos` | Los productos |
| `/corridas` | Las corridas registradas (31) |
| `/estado.json` | La fecha del informe y las peticiones abiertas |

**A quién pasarle el enlace:** a nadie todavía. `127.0.0.1` solo abre desde este equipo y solo mientras el proceso siga vivo. Para un patrocinador hace falta el modo «que quede corriendo» con `--abierto`. Eso exige pedirle a la organización un host y un puerto, y publicarlo detrás de su control de acceso, porque el servidor no autentica.

**Cuándo queda desactualizado:** el informe es del 2026-10-15. Deja de ser fiel en cuanto cambie un documento o corra otro barrido. La portada muestra su fecha.

El servidor corre en segundo plano y sigue activo; se detiene terminando el proceso.