# /criterio-portfolio:portfolio-server rato

Rostrum funciona en modo «para mirarlo un rato». Lo probé 20 segundos en segundo plano y ya está apagado.

Como no se eligió forma, tomé la sugerida: la de mirarlo un rato. Los términos están aceptados (versión 1.0, 2026-10-14). El informe existe en `reportes/` (13 proyectos, 7 productos), generado el 2026-10-14.

**Para levantarlo de nuevo:**
```
python3 "/home/claude/banco/criterio/plugins/criterio-portfolio/scripts/servidor.py" --informe reportes --estado estado/portafolio --config .criterio/portafolio/config.json
```
- **Dirección:** escucha en `http://127.0.0.1:8787/`, solo en este equipo. Se para con Ctrl-C. Si el puerto está ocupado, añade `--puerto 8788`.
- **Qué respondió en la prueba:** la portada respondió 200 y `/estado.json` mostró 0 peticiones abiertas. `/pmo` respondió con una redirección (302) y no comprobé a dónde lleva.
- **Qué se ve:** `/decisiones`, `/proyectos`, `/p/<código>`, `/productos` y `/producto/<nombre>`. El servidor también anuncia `/corridas`, con 27 corridas. El portal lleva el nombre «Portafolio de proyectos mineros».
- **Lo que no hace:** no calcula, no escribe fichas, no autentica y no manda correos. Solo guarda las peticiones del formulario en `estado/portafolio/peticiones/`.

**Cierre:**
- **Enlace:** `http://127.0.0.1:8787/` solo sirve en este equipo y mientras el proceso esté vivo. No sirve para pasárselo al patrocinador.
- **Para el patrocinador:** hace falta la forma «que quede corriendo» (`--abierto`). Eso exige pedir un host y un puerto dentro de la red, publicarlo detrás del control de acceso de la organización y mantener el equipo encendido. El servidor no trae autenticación.
- **Cuándo queda viejo:** el informe quedará desactualizado en cuanto cambien los documentos o corra de nuevo `/portfolio-report`. El próximo comité es el 2026-10-28.

**Corrida registrada:** `2026-10-14-portfolio-server-1`. Lo que le muestro a la persona está en `estado/portafolio/corridas/salida-portfolio-server.md`.