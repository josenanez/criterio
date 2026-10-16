# /criterio-portfolio:portfolio-server rato

Rostrum arrancó sin errores y escuchaba en `127.0.0.1:8787`, pero ya no está corriendo. Lo corté a los 8 segundos para comprobar que arrancaba, y en esta sesión no puede quedar vivo. Para usarlo, lanza tú este comando en una terminal:

```
python3 "/home/claude/banco/criterio/plugins/criterio-portfolio/scripts/servidor.py" --informe /home/claude/banco/ronda-4/retail/espacio/reportes --estado /home/claude/banco/ronda-4/retail/espacio/estado --config /home/claude/banco/ronda-4/retail/espacio/.criterio/portafolio/config.json
```

Se para con Ctrl-C. Si el puerto está ocupado, añade `--puerto 8788`.

- **Términos:** ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-15). No registré una aceptación nueva.
- **Forma elegida:** «para mirarlo un rato», como indicaba el argumento `rato`.
- **Qué sirve:**
  - La portada con las tres secciones y el formulario de peticiones.
  - `/pmo`, con cómo va el portafolio.
  - `/decisiones`, para el comité.
  - 13 proyectos y 7 productos, cada uno con su enlace cruzado.
  - `/corridas`, con 32 corridas.
  - `/estado.json`, con la frescura del informe.
- **A quién se lo pasas:** a nadie todavía. El enlace solo funciona en este equipo y mientras el servidor esté encendido, así que un patrocinador no puede abrirlo.
- **Para que un patrocinador lo abra:** hay que pasar a «que quede corriendo». Eso significa pedir un host y un puerto dentro de la red y publicarlo detrás del control de acceso que la organización ya usa, porque el servidor no autentica.
- **Qué tan reciente es:** el informe es el de la última corrida, y la portada dice de cuándo es. Mírala antes de reenviar nada.
- **Registro:** dejé lo que te mostré en `estado/corridas/salida-portfolio-server.md` y registré la corrida como `2026-10-15-portfolio-server-1`.