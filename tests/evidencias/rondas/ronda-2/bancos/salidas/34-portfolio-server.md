# /criterio-portfolio:portfolio-server rato

Rostrum está corriendo en modo «para mirarlo un rato» y la portada responde 200 en `http://127.0.0.1:8787/`.

- **Términos:** ya estaban vigentes (versión 1.1, aceptados por José Francisco Ñáñez el 2026-10-15), así que no registré nada nuevo.
- **Modo:** el argumento era `rato`, y es además la forma que recomienda el comando para empezar.
- **Qué sirve:** el informe de `reportes/`, con 13 proyectos, 9 productos y 32 corridas.
- **Registro:** guardé lo mostrado en `estado/corridas/salida-portfolio-server.md` y la corrida quedó como `2026-10-15-portfolio-server-1`.

Direcciones:
- Portada: `http://127.0.0.1:8787/`
- Cómo va el portafolio (PMO): `/pmo`
- Decisiones (comité y patrocinador): `/decisiones`
- Proyectos: `/proyectos`
- Productos: `/productos`
- Corridas: `/corridas`
- Frescura: `/estado.json`

**A quién pasarle el enlace:** a nadie todavía. Solo funciona en este equipo, así que un patrocinador no lo abriría. Para darle un enlace estable hay que pasar a «que quede corriendo». Eso es arrancar con `--abierto` y pedirle a la organización un host, un puerto y su control de acceso. El servidor no autentica.

**Cuándo se desactualiza:** el informe es el de la última corrida de `/portfolio-report`, del 2026-10-15. La portada muestra esa fecha.

El servidor sigue en segundo plano y escribe su registro en `/tmp/claude-0/rostrum.log`. Para pararlo, termina el proceso `servidor.py`.