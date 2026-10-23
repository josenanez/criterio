# /criterio-server:server-start rato

Rostrum está corriendo en **http://127.0.0.1:8789/**. Escucha solo en este equipo y no tiene autenticación.

Los puertos 8787 y 8788 ya los usan otros servidores. Esos tienen mapas distintos (otros productos, PRD-302 y PRD-306), así que no son este espacio. Levanté el mío en el 8789 y el `/estado.json` de ese puerto muestra los agentes de este mapa: Vera, Samuel (PRY-202) y Alba (PRD-301). El servidor sigue en segundo plano. Para pararlo, mata el proceso del puerto 8789.

**Términos:** están vigentes (versión 1.2, aceptada en 0.8.0). Quedó registrado a nombre de José Francisco Ñáñez, con fecha 2026-10-23. El recibo está en `.criterio/terminos/aceptacion-criterio-server-0.8.0-2026-10-23.md` y en PDF.

**Forma elegida:** «para mirarlo un rato», que es lo que indicó el argumento `rato`. No pedí ninguna infraestructura.

**Mapa contra el disco:** no hay entradas nuevas, desaparecidas ni sin estado. El informe de la PMO ya existe en `reportes/`, así que no hizo falta correr `portfolio-report`.

**Qué hay en cada ruta:**
| Ruta | Para quién |
|---|---|
| `/` | Todos: los 3 agentes del mapa y el formulario de peticiones |
| `/pmo`, `/decisiones` | PMO, comité y patrocinador |
| `/proyectos` (13), `/productos` (7) | Quien pregunta por un proyecto o un producto |
| `/caso/<código>` | Todo lo que los agentes hicieron sobre un caso, juntando familias |
| `/corridas` (33) | Quien audita |
| `/estado.json` | Un mecanismo, no una persona |

No aparecen `/familia/cfo`, `/familia/clo` ni `/vence`, porque este mapa solo tiene la familia PMO.

**Qué enlace pasarle a quién:**
- **Patrocinador:** `/` y `/decisiones`.
- **Gerencia:** `/proyectos`.

Esos enlaces solo funcionan mientras este equipo siga encendido y el servidor corriendo. Cada página dice de cuándo es lo que muestra. El informe se generó hoy, 2026-10-23, y ningún agente tiene todavía una corrida registrada, porque `ultimo` sale en `null` para los tres.

**Lo que Rostrum no hace:** no calcula, no escribe fichas, no autentica y no manda correos. Lo único que crea son las peticiones, en `peticiones/` del agente elegido, y no puede correr al agente.

**Para dejarlo corriendo:** hay que pedirle a la organización un host con puerto dentro de la red, publicarlo detrás de su control de acceso (`--abierto`) y que el equipo siga encendido. No necesita base de datos, certificado ni salida a internet.