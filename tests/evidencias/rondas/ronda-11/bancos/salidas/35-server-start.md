# /criterio-server:server-start rato

Rostrum está corriendo en `http://127.0.0.1:8787/`, solo en este equipo. Para pararlo hay que matar el proceso en segundo plano. Los términos 1.2 ya estaban vigentes y registrados a nombre de José Francisco Ñáñez el 2026-10-23, así que no hubo que registrarlos de nuevo. El mapa y el disco coinciden: no hay entradas nuevas ni agentes sin estado.

**Qué hay**
- **Mapa:** tres entradas. Vera (portafolio), Samuel (proyecto PRY-206) y Alba (producto PRD-302), todas de la familia PMO.
- **Portada** (`/`): los tres agentes y el formulario de peticiones.
- **Informe de la PMO** (`/pmo`): ya estaba generado, con fecha 2026-10-23T15:13 UTC.
  - **Comité:** `/decisiones`.
  - **Proyectos:** `/proyectos`, con 13 proyectos.
  - **Productos:** `/productos`, con 9 productos.
- **Corridas** (`/corridas`): 33 corridas en la historia.
- **Frescura** (`/estado.json`): para un mecanismo, no para una persona.
- **Peticiones:** 0 abiertas.

**Un hallazgo**
- `/estado.json` muestra `ultimo: null` para los tres agentes y `proxima_corrida: null`.
- Es decir, el portal no sabe decir de cuándo es lo último de cada agente. Por eso el único dato con fecha es el del informe de la PMO.

**Qué enlace pasar a quién**
- Al patrocinador y al comité: `/` o `/decisiones`.
- La PMO usa `/pmo` y `/proyectos`.
- No hay familia CFO ni CLO en el mapa, así que `/familia/…` y `/vence` no tienen contenido para esta organización.

**Lo que no hace**
- Sirve lo que los agentes ya escribieron: no calcula ni procesa documentos.
- No escribe fichas; solo crea peticiones en la carpeta `peticiones/` del agente elegido.
- No autentica y no manda correos.

**Para que el patrocinador tenga un enlace que funcione mañana**
- Esta forma solo vive mientras el proceso esté activo y solo se ve desde este equipo.
- Para eso hay que pasar a la forma «que quede corriendo» (`--abierto`). Habría que pedirle a la organización un host con puerto dentro de la red, publicarlo detrás de su control de acceso y mantener el equipo encendido.
- No necesita base de datos, certificado ni salida a internet.