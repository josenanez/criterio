# /criterio-portfolio:portfolio-server rato

Rostrum está corriendo en **http://127.0.0.1:8788/**. Es solo para este equipo y se apaga con Ctrl-C.

- **Términos:** ya estaban vigentes para la versión 0.5.0. Los aceptó José Francisco Ñáñez el 2026-10-18, así que no los volví a pedir ni los registré de nuevo.
- **Modo:** no había quién contestara, así que tomé la opción sugerida, «para mirarlo un rato». No hay nada que pedirle a seguridad.
- **Puerto:** el 8787 estaba ocupado, así que usé el 8788, como sugería el propio programa.
- **Qué sirve:** el informe que ya estaba en `reportes/` (13 proyectos, 7 productos), con `estado/` como carpeta de estado. No hay peticiones abiertas.
- **Registro de la corrida:** `estado/corridas/salida-portfolio-server.md` lleva lo mostrado, y la corrida quedó como `2026-10-18-portfolio-server-1`. Dejé escrito allí el puerto 8787, y el servidor quedó en el 8788.

Las rutas son:

| Ruta | Qué es |
|---|---|
| `/` | Portada y formulario de peticiones |
| `/pmo` | Cómo va el portafolio: verdes sin sustento, silencios, patrocinadores repetidos |
| `/decisiones` | Lo que necesita una decisión, con la consecuencia de no decidir |
| `/proyectos`, `/p/<código>` | Listado y cada proyecto, con enlace a su producto |
| `/productos`, `/producto/<nombre>` | Listado y cada producto, con enlace a los proyectos que lo construyen |
| `/corridas` | Evidencia de las corridas (33) |
| `/estado.json` | Fecha del informe y peticiones abiertas |

Rostrum no calcula, no escribe fichas, no autentica y no manda correos. Solo crea las peticiones del formulario, en `estado/peticiones/`, y ahí esperan hasta que el agente despierte.

**A quién pasarle el enlace:** a nadie. `127.0.0.1` solo se ve desde esta máquina. Para que el patrocinador tenga un enlace estable hay que repetir con «que quede corriendo» (`--abierto`) y publicarlo detrás del control de acceso de la organización.

El informe es del 2026-10-18 a las 14:13 UTC. Queda desactualizado en cuanto cambie un documento, hasta que se regenere con `/portfolio-report html`.