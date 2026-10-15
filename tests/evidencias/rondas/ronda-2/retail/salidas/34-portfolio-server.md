# /criterio-portfolio:portfolio-server rato

Rostrum está corriendo en **http://127.0.0.1:8799/**, solo en este equipo. Eso es la forma «para mirarlo un rato», así que no hay nada que pedirle a seguridad. Lo paras con Ctrl-C si lo lanzas tú, o matando el proceso que dejé en segundo plano.

- **Términos:** ya estaban vigentes (versión 1.1, aceptados por José Francisco Ñáñez el 2026-10-15), así que no los volví a registrar.
- **Puerto:** el 8787 y el 8788 ya los ocupaban otros servidores, así que usé el 8799. Esos dos sirven informes distintos al de esta carpeta: el del 8787 lista productos que no están en `reportes/`.
- **Informe servido:** `reportes/` tiene 13 proyectos (PRY-199 a PRY-211).
- **Corrida registrada:** `estado/corridas/salida-portfolio-server.md` y `2026-10-15-portfolio-server-1`. La corrida registra 60 hallazgos sobre los 13 proyectos; la mayoría son hitos dados por cumplidos sin evidencia.
- **Rutas principales:**
  - `/`: portada.
  - `/pmo`: cómo va el portafolio.
  - `/decisiones`: lo que necesita decisión.
  - `/proyectos`: listado de proyectos.
  - `/productos`: listado de productos.
  - `/estado.json`: fecha del informe y peticiones abiertas.
  - Cada proyecto y cada producto tiene además su propia página.
- **Qué no hace:** no calcula, no escribe fichas (solo crea peticiones en `estado/peticiones/`), no autentica y no manda correos.

**Qué enlace pasar:** ninguno al patrocinador todavía. `127.0.0.1` solo funciona en este equipo y el servidor se apaga cuando lo detengas, así que el enlace no sirve mañana. Para un enlace estable hay que volver a correrlo con `--abierto` y pedirle a la organización un host, un puerto y que lo publique detrás del control de acceso que ya usa.

**Cuándo se desactualiza:** el informe es del 2026-10-15. Queda viejo cuando cambie la documentación o corra otro barrido, y la portada muestra su fecha.