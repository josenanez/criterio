# /criterio-portfolio:portfolio-server rato

Rostrum arrancó bien en modo «para mirarlo un rato». No hice ninguna petición al servidor; el 15 s de espera fue un arranque de prueba y el proceso se cortó solo.

- **Términos:** ya estaban vigentes (versión 1.1, aceptados por José Francisco Ñáñez el 2026-10-15), así que no los volví a registrar.
- **Informe:** existe en `reportes/`, con 13 proyectos. El servidor lista 8 productos, pero en `reportes/` hay 7 archivos de producto. Esa diferencia no la revisé.
- **Registro:** dejé lo que te mostré en `estado/corridas/salida-portfolio-server.md`. La corrida quedó registrada como `2026-10-15-portfolio-server-1`.
- **Dónde corre:** `http://127.0.0.1:8787/`, solo en este equipo. Las rutas son `/pmo`, `/decisiones`, `/proyectos`, `/productos`, `/corridas` y `/estado.json`.
- **Aviso sobre `/pmo`:** en `reportes/` no hay un `pmo.html`. Si esa ruta no responde, hay que correr `/portfolio-report html` otra vez.
- **Si lo vuelves a levantar:** este comando termina al detener el proceso. Para dejarlo corriendo hay que ejecutarlo en una terminal propia, con Ctrl-C para pararlo. Si el 8787 está ocupado, usa `--puerto 8788`.
- **A quién pasarle el enlace:** a nadie todavía. `127.0.0.1` solo abre en este equipo, así que el patrocinador no puede verlo. Para eso hace falta «que quede corriendo» con `--abierto`, detrás del control de acceso de la organización. El servidor no autentica.
- **Cuándo se desactualiza:** el informe es de 2026-10-15. Queda viejo cuando cambie algún documento o se corra un nuevo barrido. La portada muestra su fecha.