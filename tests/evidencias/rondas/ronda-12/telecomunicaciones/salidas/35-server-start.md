# /criterio-server:server-start rato

Rostrum está corriendo en `http://127.0.0.1:8787/`, y solo se llega desde este equipo. Se para con Ctrl-C, o matando el proceso si sigue en segundo plano. El registro del arranque está en `/tmp/claude-0/-home-claude-r12-telecomunicaciones-espacio/692b0e4d-0e89-5e8d-a391-2cabbf233557/scratchpad/rostrum.log`.

**Términos.** Ya estaban vigentes (v1.3, aceptada por José Francisco Ñáñez el 2026-10-28), así que no hubo que mostrarlos ni registrar nada.

**El mapa.** Coincide con el disco: no hay entradas nuevas, desaparecidas ni sin estado. Tiene tres entradas, todas de la familia PMO: Vera (portafolio), Samuel (PRY-211) y Alba (PRD-306). El informe de la PMO ya existía en `reportes/`, con fecha 2026-10-29 02:08 UTC, y el servidor lo sirve tal cual.

**Qué hay y para quién:**

| Ruta | Qué es | Para quién |
|---|---|---|
| `/` | Portada: los tres agentes y el formulario de peticiones | Todos |
| `/pmo`, `/decisiones` | Informe de la PMO y paquete de comité | PMO, comité, patrocinador |
| `/proyectos` | 13 proyectos, de PRY-199 a PRY-211 | PMO y patrocinador |
| `/productos` | 6 productos | PMO y patrocinador |
| `/corridas` | Historia de 33 corridas | Quien audita |
| `/estado.json` | Frescura de cada agente y peticiones abiertas | Un mecanismo, no una persona |

**Lo que se ve por ahora:**
- **Sin fecha de última corrida.** `/estado.json` muestra `ultimo: null` para los tres agentes. Esas entradas aparecerán sin fecha de corrida hasta que cada agente corra.
- **Sin próxima corrida programada.** `proxima_corrida` está en null.
- **Sin peticiones abiertas.** Hay 0.
- **Sin otras familias.** Como el mapa solo tiene la PMO, no hay rutas `/familia/cfo` ni `/familia/clo`. `/vence` y `/caso/<código>` no se probaron.

**Qué enlace pasarle a quién:**
- **Patrocinador:** `/`, para entrar al informe y a los proyectos. El informe es del 2026-10-29 02:08 UTC.
- **Comité:** `/decisiones`, con la misma fecha.
- **Auditoría:** `/corridas`.

Este enlace funciona solo mientras el equipo siga encendido. Para que el patrocinador tenga uno estable hay que pasar a «que quede corriendo» con `--abierto`. Eso exige pedirle a la organización un host y un puerto, y publicarlo detrás de su control de acceso. El servidor no trae autenticación. No necesita base de datos, certificado propio ni salida a internet.

**Lo que no hace.** No calcula, no escribe fichas, no autentica y no manda correos. Las peticiones del formulario quedan en la carpeta `peticiones/` del agente elegido. Cada agente las toma cuando despierte, porque el servidor no puede correrlo.