# /criterio-portfolio:portfolio-server rato

Rostrum arrancó bien en `127.0.0.1:8787`, pero no sigue corriendo. Esta sesión no tiene interfaz y el comando de arranque se cortó a los 15 segundos. Para mirarlo, ejecuta tú el comando de más abajo en tu máquina.

- **Modo:** «para mirarlo un rato», como indicaste. Escucha solo en el equipo donde corre, sin autenticación ni acceso desde fuera.
- **Términos:** la configuración ya tenía la aceptación de José Francisco Ñáñez (versión 1.0, 2026-10-14), igual que `TERMS.es.md`. No hizo falta pedirla.
- **Informe:** ya existía en `reportes/`, así que no hubo que correr `/portfolio-report`.
- **Corrida:** quedó registrada como `2026-10-14-portfolio-server-1`. El texto mostrado está en `estado/corridas/salida-portfolio-server.md`. Lo guardé antes de arrancar el servidor, como pide el comando.
- **Cifra de productos:** mi texto guardado dice 3 productos, pero el servidor cuenta 8. El 3 salió de los archivos `producto-*.html` que vi en un listado cortado. Vale la cifra del servidor.

Páginas que sirve el portal:
- `/` es la portada, con el formulario de peticiones.
- `/pmo` muestra cómo va el portafolio.
- `/decisiones` reúne lo que necesita decisión del comité.
- `/proyectos` lista 13 proyectos.
- `/productos` lista 8 productos.
- `/corridas` lista 34 corridas.
- `/estado.json` dice de cuándo es el informe.

Para levantarlo otra vez:
```
python3 "/home/claude/banco/criterio/plugins/criterio-portfolio/scripts/servidor.py" --informe /home/claude/banco/ronda-1/cooperativas/espacio/reportes --estado /home/claude/banco/ronda-1/cooperativas/espacio/estado --config /home/claude/banco/ronda-1/cooperativas/espacio/.criterio/portafolio/config.json
```
Si el puerto 8787 está ocupado, añade `--puerto 8788`.

**A quién pasarle el enlace:** `http://127.0.0.1:8787/` solo abre en el equipo donde corre. Sirve para enseñárselo a alguien delante de la pantalla, no para mandárselo a un patrocinador. Para eso hay que dejarlo corriendo con `--abierto`. Eso requiere un host y un puerto dentro de la red, publicados detrás del control de acceso que la organización ya usa, y que el equipo siga encendido.

**Cuándo se desactualiza:** el informe está al día hasta la última vez que se corrió `/portfolio-report`. La portada muestra esa fecha.