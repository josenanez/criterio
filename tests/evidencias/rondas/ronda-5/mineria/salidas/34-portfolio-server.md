# /criterio-portfolio:portfolio-server rato

Rostrum está corriendo en modo «para mirarlo un rato» en `http://127.0.0.1:8787`, y responde. Solo se ve desde este equipo.

- **Términos:** ya estaban vigentes, aceptados por José Francisco Ñáñez el 2026-10-16 (versión 0.3.11), así que no hubo que pedirlos otra vez.
- **Qué sirve:** el informe de `reportes/`, que cubre 13 proyectos (PRY-199 a PRY-211) y 6 productos. `/estado.json` lo fecha el 2026-10-16 a las 17:45 UTC y marca 0 peticiones abiertas.
- **Rutas:**
  - `/` es la portada.
  - `/pmo` es para la PMO.
  - `/decisiones` es para el comité.
  - `/proyectos` y `/productos` son los listados.
  - `/corridas` muestra las 31 corridas registradas (31 es el número que imprime el servidor al arrancar).
- **Qué no hace:** no calcula, no escribe fichas, no autentica y no manda correos. Lo único que escribe es la petición del formulario, en `estado/peticiones/`.
- **A quién pasarle el enlace:** a nadie todavía. Un patrocinador no puede abrirlo. Para que quede corriendo hay que arrancarlo con `--abierto` y pedirle a la organización un host con puerto y publicarlo detrás de su control de acceso. Hay que decirles que el servidor no autentica.
- **Cuándo se desactualiza:** cualquier documento que cambie después del 2026-10-16 12:45 deja el informe atrasado. La portada muestra su fecha.
- **Registro:** dejé la salida en `estado/corridas/salida-portfolio-server.md` y la corrida quedó registrada como `2026-10-16-portfolio-server-1`.
- **Para pararlo:** lo lancé en segundo plano y su log está en `/tmp/claude-0/rostrum.log`. No hay Ctrl-C aquí; se detiene terminando el proceso `servidor.py`.