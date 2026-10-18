# /criterio-portfolio:portfolio-server rato

Rostrum está corriendo en el modo «para mirarlo un rato», en **http://127.0.0.1:8788/**, y solo se ve desde este equipo. Lo probé: la portada y `/estado.json` responden 200 y el portal lleva el nombre «Retail».

- **Modo:** nadie podía contestar, así que tomé la respuesta sugerida. Se empieza por «para mirarlo un rato» porque se levanta en diez segundos y cambia la conversación con seguridad: ya no se pide permiso para una idea.
- **Términos:** ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-17), así que no pedí aceptarlos otra vez.
- **Puerto:** el 8787 ya lo tenía otro servidor que sirve un informe distinto, con productos de banca. Por eso usé `--puerto 8788`. La nota de la corrida registrada dice 8787, porque la registré antes de levantarlo. Lo dejé aclarado al final de `estado/corridas/salida-portfolio-server.md`, pero la nota de `corridas.json` sigue diciendo 8787.

**Qué hay en el portal**

| Ruta | Para quién |
|---|---|
| `/` | Todos: portada y formulario de peticiones |
| `/pmo` | La PMO: verdes que la evidencia no sostiene, silencios, patrocinadores con más de un proyecto |
| `/decisiones` | Comité y patrocinador: preguntas cerradas con la consecuencia de no decidir |
| `/proyectos` | Todos: los 13 proyectos, los que más piden atención primero |
| `/p/<código>` | Quien gerencia: informe de un proyecto, con enlace a su producto |
| `/productos` y `/producto/<nombre>` | Quien responde por un producto: informe del producto, con enlace a sus proyectos (7 productos) |
| `/corridas` | Evidencia de las corridas (33) |
| `/estado.json` | Mecanismo: fecha del informe y peticiones abiertas |

Rostrum no calcula, no escribe fichas (solo la petición, en `estado/peticiones/`), no autentica y no manda nada. El formulario de la portada no se contesta en el momento: la petición queda a la espera hasta que el agente despierte. Hoy hay 0 abiertas.

**El enlace.** Sirve solo mientras este servidor siga encendido y solo en este equipo, así que mañana no abre. No se lo pasaría todavía al patrocinador. Para que tenga un enlace estable hay que ir a «que quede corriendo» (`--abierto`). Eso requiere que la organización apruebe un host y un puerto dentro de la red, detrás de su control de acceso, porque el servidor no trae autenticación a propósito.

**Frescura del informe.** Es del 2026-10-17 21:35. Queda desactualizado en cuanto se haga otro barrido sin regenerarlo con `/portfolio-report html`. La portada lo muestra, pero conviene avisarlo antes de enviar el enlace.

Para pararlo hay que cerrar el proceso de fondo en el puerto 8788. En una sesión normal sería Ctrl-C.