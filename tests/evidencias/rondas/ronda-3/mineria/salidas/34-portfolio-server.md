# /criterio-portfolio:portfolio-server rato

Rostrum está corriendo en modo «para mirarlo un rato», en `http://127.0.0.1:8788/`. El puerto 8787 ya estaba ocupado, así que usé el 8788.

- **Términos:** ya estaban vigentes (versión 1.1, aceptados por José Francisco Ñáñez el 2026-10-15). No hizo falta registrarlos otra vez.
- **Qué sirve:** el informe de `reportes/`, que cubre 13 proyectos (PRY-199 a PRY-211) y 6 productos. No hay peticiones abiertas.
- **Rutas:**
  - `/` es la portada.
  - `/pmo` es el informe de la PMO.
  - `/decisiones` es para el comité.
  - `/proyectos` y `/productos` son los listados.
  - `/corridas` muestra las corridas registradas.
  - `/estado.json` da la fecha del informe.
- **`/pmo`:** en `reportes/` no hay `pmo.html`. Puede que esa ruta salga vacía hasta que se corra `/portfolio-report html`. No la abrí para comprobarlo.
- **Solo en este equipo:** el enlace no sirve para el patrocinador. Para darle uno estable hay que pasar a «que quede corriendo» (`--abierto`). Eso exige pedir a la organización un host, un puerto y su control de acceso, porque el servidor no autentica.
- **Cuándo se desactualiza:** el informe es del 2026-10-15 y queda viejo en cuanto cambie la documentación.
- **Para pararlo:** el servidor está en segundo plano. Se detiene matando su proceso, y el registro está en `/tmp/claude-0/rostrum.log`.
- **Corrida registrada:** la salida está en `estado/corridas/salida-portfolio-server.md` y la corrida quedó como `2026-10-15-portfolio-server-1`.