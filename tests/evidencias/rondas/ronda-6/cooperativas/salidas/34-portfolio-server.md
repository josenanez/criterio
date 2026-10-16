# /criterio-portfolio:portfolio-server rato

Rostrum está corriendo en modo «para mirarlo un rato». Lo probé con `curl http://127.0.0.1:8787/estado.json` y responde.

- **Términos:** ya estaban vigentes para la versión 0.3.12. José Francisco Ñáñez los aceptó el 2026-10-16 y el comprobante está en `.criterio/terminos/`. No los registré de nuevo.
- **Forma elegida:** «para mirarlo un rato». No había quién respondiera, así que tomé la sugerida: empezar por esta y dejar «que quede corriendo» para cuando haya que hablar con seguridad.
- **Informe:** ya existía en `reportes/`. Tiene 13 proyectos (PRY-199 a PRY-211), 8 productos, la página de decisiones y 34 corridas. No hay peticiones abiertas.
- **Dónde mirarlo:** `http://127.0.0.1:8787/`, solo en este equipo.

| Ruta | Qué muestra |
|---|---|
| `/` | La portada, con el formulario de peticiones |
| `/pmo` | Cómo va el portafolio |
| `/decisiones` | Lo que necesita una decisión del comité |
| `/proyectos` y `/p/<código>` | El listado y el informe de cada proyecto |
| `/productos` y `/producto/<nombre>` | El listado y el informe de cada producto |
| `/corridas` | Las corridas registradas |
| `/estado.json` | De cuándo es el informe |

- **Qué no hace Rostrum:** no calcula (sirve lo que ya escribió el informe), no escribe fichas, no autentica y no manda correos. Una petición del formulario queda en `estado/peticiones/` hasta que el agente despierte.
- **Enlace para el patrocinador:** este enlace solo funciona en este equipo, así que no se lo pases a nadie. El informe es del 2026-10-16 15:13 y se desactualiza en cuanto cambie un documento. Para que el patrocinador tenga un enlace propio hay que pasar a «que quede corriendo». Para eso hay que pedirle a la organización un host con puerto, publicarlo detrás de su control de acceso y mantener el equipo encendido.
- **Registro:** guardé lo mostrado en `estado/corridas/salida-portfolio-server.md` y la corrida quedó como `2026-10-16-portfolio-server-1`. El registro de la corrida dice 52 hallazgos en los 13 proyectos.
- **Apagarlo:** el servidor sigue en segundo plano y su log está en `/tmp/claude-0/-home-claude-banco-ronda-6-cooperativas-espacio/692b0e4d-0e89-5e8d-a391-2cabbf233557/scratchpad/rostrum.log`. Se detiene terminando el proceso `servidor.py`.