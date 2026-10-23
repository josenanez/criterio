# /criterio-server:server-start rato

Rostrum está corriendo en **http://127.0.0.1:8788/** y responde 200. Lo levanté en la forma «para mirarlo un rato». El 8787 ya estaba ocupado, así que usé el 8788.

**Términos:** están vigentes (versión 1.2). José Francisco Ñáñez los aceptó para esta prueba el 2026-10-23, y el registro y su comprobante ya estaban en el mapa. Lo que Criterio le dice a quien lo usa:
- Produce borradores de trabajo, no decisiones ni asesoría.
- Solo lee los documentos que usted le indique, y puede equivocarse. Cada dato lleva su cita, y la verificación es suya.
- Los documentos se procesan en la infraestructura de la plataforma de IA, no solo en su equipo.
- Garantía y responsabilidad: licencia Apache 2.0.
- Nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

**Mapa:** el mapa revisado contra el disco no tiene entradas nuevas, desaparecidas ni sin estado. Tiene tres: el portafolio (Vera), el proyecto PRY-206 (Samuel) y el producto PRD-306 (Alba). Todos son de la familia PMO. El informe de la PMO ya existía en `reportes/`, así que no hizo falta correr `portfolio-report`.

**Qué hay y para quién:**

| Ruta | Para quién |
|---|---|
| `/` (portada y formulario de peticiones) | Todos |
| `/pmo` y `/decisiones` (informes PMO y comité) | La PMO, el comité y el patrocinador |
| `/proyectos` (13) y `/productos` (8) | Quien responde por cada proyecto o producto |
| `/corridas` (33 corridas) | Quien audita |
| `/estado.json` | Un mecanismo, no una persona |

No aparecen `/familia/cfo`, `/familia/clo` ni `/vence`, porque el mapa solo trae la familia PMO.

**Qué enlace pasar a quién:**
- **Patrocinador:** `/`, y `/decisiones` si necesita el material del comité.
- **PMO:** `/pmo`.
- **Gerencia:** `/proyectos` y `/productos`.

Hoy esos enlaces solo abren en este equipo (`127.0.0.1`) y dejan de funcionar cuando se apague el servidor. Cada página dice de cuándo es lo que muestra, y conviene avisar a quien reciba el enlace.

**Lo que Rostrum no hace:**
- No calcula; solo sirve lo que los agentes ya escribieron.
- No escribe ninguna ficha. Lo único que crea son las peticiones, en la carpeta `peticiones/` del agente elegido, donde esperan a que ese agente despierte.
- No autentica.
- No manda correos ni notificaciones.

**Para que quede corriendo:** hay que pedirle a la organización un host y un puerto dentro de la red, y publicarlo detrás de su control de acceso (`--abierto`). Con eso basta: no necesita base de datos, certificado ni salida a internet. Cuando haya un host, puedo dar la unidad de `systemd` con las rutas reales del mapa.