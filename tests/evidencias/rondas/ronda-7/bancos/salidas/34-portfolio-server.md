# /criterio-portfolio:portfolio-server rato

Rostrum quedó probado en modo «para mirarlo un rato». El servidor arrancó y respondió en `127.0.0.1:8787`, con 200 en la portada y en `/estado.json`. Lo dejé corriendo solo 20 segundos de prueba; ya está apagado, así que ahora no hay ningún servidor activo. Una prueba aparte (el servidor apagado) no confirmó el enlace de ese informe.

Lo que hice, en orden:
- **Configuración:** existe en `.criterio/portafolio/config.json`.
- **Términos:** ya estaban vigentes para la versión 0.3.13, aceptados por José Francisco Ñáñez el 2026-10-17. No hubo que volver a registrar nada.
- **Informe:** ya existe en `reportes/` (13 proyectos, 9 productos), así que no hizo falta correr `/portfolio-report`.
- **Modo:** como nadie podía responder, tomé la respuesta sugerida, que es empezar por «para mirarlo un rato».
- **Corrida registrada:** la salida está en `estado/corridas/salida-portfolio-server.md` y la corrida quedó como `2026-10-17-portfolio-server-1`.

`/pmo`, `/decisiones`, `/proyectos` y `/productos` respondieron 302 (redirección) en lugar de 200. No seguí las redirecciones, así que no sé a dónde llevan ni si las páginas se ven bien.

Para que alguien lo mire, el comando es:

```
python3 "/home/claude/banco/criterio/plugins/criterio-portfolio/scripts/servidor.py" --informe reportes --estado estado --config .criterio/portafolio/config.json
```

Lo corre desde `/home/claude/banco/ronda-7/bancos/espacio` y se para con Ctrl-C. Si el puerto está ocupado, se añade `--puerto 8788`.

- **Enlace:** `http://127.0.0.1:8787/` solo lo ve quien esté en este equipo, así que no se le puede mandar a un patrocinador.
- **Qué tan al día está:** el informe es del 2026-10-17. Queda desactualizado en cuanto cambien las fichas, y el comité es el 2026-10-24, así que conviene regenerarlo antes. La portada muestra su fecha.
- **Qué no hace:** no autentica, no calcula, no manda correos y no escribe fichas. Solo crea las peticiones del formulario en `estado/peticiones/`, que esperan hasta que el agente las vea con `due`.
- **Para un enlace estable:** hay que pedirle a la organización un host con puerto y publicarlo detrás de su control de acceso. Se levanta con `--abierto`.