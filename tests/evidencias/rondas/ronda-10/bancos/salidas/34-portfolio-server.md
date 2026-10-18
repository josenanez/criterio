# /criterio-portfolio:portfolio-server rato

Rostrum arrancó bien en el puerto 8788. Lo paré a los 4 segundos, porque el servidor no termina solo y esta sesión no tiene interfaz. Para dejarlo levantado, lanza el mismo comando sin `timeout`.

- **Configuración y términos:** la configuración existe. Los términos ya estaban vigentes (versión 1.1, aceptados por José Francisco Ñáñez el 2026-10-18, con comprobante en `.criterio/terminos/`), así que no hizo falta registrarlos otra vez.
- **Modo:** elegí «para mirarlo un rato», que es la respuesta sugerida.
- **Puerto:** el 8787 estaba ocupado (`Address already in use`), así que usé `--puerto 8788`.
- **Informe:** el servidor sirve `reportes/`, que ya tenía el informe.
- **Corrida registrada:** quedó como `2026-10-18-portfolio-server-1`. La salida está en `estado/corridas/salida-portfolio-server.md`. Esa salida dice que el puerto es el 8787 y la nota de la corrida también, y ambos son erróneos: se escribieron antes de saber que estaba ocupado. No los corregí.

Comando para dejarlo levantado:

```
python3 "/home/claude/banco/criterio/plugins/criterio-portfolio/scripts/servidor.py" --informe /home/claude/banco/ronda-10/bancos/espacio/reportes --estado /home/claude/banco/ronda-10/bancos/espacio/estado --config /home/claude/banco/ronda-10/bancos/espacio/.criterio/portafolio/config.json --puerto 8788
```

Escucha solo en este equipo y se para con Ctrl-C. Estas son las páginas, con Banco Ejemplo en todas:

| Ruta | Qué muestra | Para quién |
|---|---|---|
| `http://127.0.0.1:8788/` | Portada con el formulario de peticiones | Todos |
| `/pmo` | Cómo va el portafolio mirando todo junto | La PMO |
| `/decisiones` | Lo que necesita una decisión, con la consecuencia de no decidir | Comité y patrocinador |
| `/proyectos` | 13 proyectos, por lo que más pide atención | Todos |
| `/productos` | 9 entradas, con los proyectos que construyen cada producto | Quien responde por un producto |
| `/corridas` | 32 corridas | Quien quiera ver la evidencia |
| `/estado.json` | Fecha del informe y peticiones abiertas | Un mecanismo |

**Qué hace y qué no:**
- Sirve lo que `informe.py` ya escribió.
- No calcula, no escribe fichas, no autentica y no manda correos.
- Lo único que crea son las peticiones, en `estado/peticiones/`.

**Enlace:** `http://127.0.0.1:8788/` solo funciona en este equipo, así que no se lo pases a nadie. Para que el patrocinador tenga un enlace estable hay que pasar a «que quede corriendo». Eso requiere pedir a la organización un host y un puerto, y publicarlo detrás de su control de acceso, porque el servidor no autentica.

**Cuándo se desactualiza:** el informe es del 2026-10-18. Queda viejo en cuanto cambie un documento de los proyectos o se haga un nuevo barrido. La portada muestra esa fecha.