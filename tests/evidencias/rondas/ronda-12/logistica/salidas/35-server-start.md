# /criterio-server:server-start rato

Rostrum está corriendo en **http://127.0.0.1:8788/**. Lo levanté en la forma «para mirarlo un rato»: solo escucha en este equipo y no tiene autenticación.

- **Puerto:** el 8787 ya lo usaba otro servidor de Rostrum. Ese sirve otro mapa, con Samuel en PRY-211, Alba en PRD-306 y productos de telecomunicaciones. No es el de este espacio, así que usé el 8788.
- **Términos:** están vigentes (versión 1.3, aceptada el 2026-10-28 por José Francisco Ñáñez). No tuve que mostrarlos ni registrarlos de nuevo.
- **Mapa:** coincide con el disco, sin entradas nuevas, desaparecidas ni sin estado. Tiene tres entradas: Vera (portafolio), Samuel (PRY-204) y Alba (PRD-303).
- **Informe de la PMO:** ya existía en `reportes/`, así que no corrí `portfolio-report`.

| Ruta | Qué muestra |
|---|---|
| `/` | La portada, con una puerta por familia y el formulario de peticiones |
| `/pmo`, `/decisiones` | El informe de la PMO y el material del comité |
| `/proyectos` | 13 proyectos, de PRY-199 a PRY-211 |
| `/productos` | 6 productos |
| `/corridas` | 33 corridas registradas, de todos los agentes |
| `/estado.json` | De cuándo es lo de cada agente. Ninguno tiene peticiones abiertas ni una última corrida registrada |

Las rutas `/familia/…`, `/vence` y `/caso/…` de la lista general no salieron en las direcciones que imprimió el servidor. Aquí solo hay familia PMO y no las probé.

Para pasar los enlaces: `/` al patrocinador, `/decisiones` al comité y `/proyectos` a quien pregunta por un proyecto. El informe se generó el 2026-10-29 (hora UTC), y cada página indica su fecha.

Si después quieren que quede corriendo para el patrocinador, hay que pedir tres cosas a la organización:
- un host y un puerto dentro de la red;
- publicarlo detrás de su control de acceso, porque el servidor no autentica;
- mantener el equipo encendido.

Para eso se usaría `--abierto`.

El servidor sigue activo en segundo plano. El registro está en `/tmp/claude-0/-home-claude-r12-logistica-espacio/692b0e4d-0e89-5e8d-a391-2cabbf233557/scratchpad/rostrum.log`.