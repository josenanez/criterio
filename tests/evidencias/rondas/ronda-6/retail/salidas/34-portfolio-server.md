# /criterio-portfolio:portfolio-server rato

Rostrum arrancó bien en el puerto 8789, con el informe de esta carpeta (13 proyectos, 7 productos). El proceso lo paró el tiempo límite de la herramienta, así que ya no está corriendo. Para mirarlo, ejecuta tú el comando abajo y apágalo con Ctrl-C.

- **Términos:** ya estaban vigentes (versión 1.1, aceptados por José Francisco Ñáñez el 2026-10-16). No registré nada nuevo.
- **Forma:** «para mirarlo un rato», la respuesta sugerida. Escucha solo en este equipo (`127.0.0.1`), sin autenticación y sin enlace estable para el patrocinador.
- **Puertos:** el 8787 y el 8788 estaban ocupados por otros servidores, con informes distintos al de esta carpeta. No los toqué y usé el 8789.

```
python3 "/home/claude/banco/criterio/plugins/criterio-portfolio/scripts/servidor.py" --informe /home/claude/banco/ronda-6/retail/espacio/reportes --estado /home/claude/banco/ronda-6/retail/espacio/estado --config /home/claude/banco/ronda-6/retail/espacio/.criterio/portafolio/config.json --puerto 8789
```

| Ruta | Qué es | Para quién |
|---|---|---|
| `/` | Portada y formulario de peticiones | Todos |
| `/pmo` | Cómo va el portafolio | La PMO |
| `/decisiones` | Lo que necesita una decisión | Comité y patrocinador |
| `/proyectos` | Listado por atención | Todos |
| `/productos` | Productos y los proyectos que los construyen | Quien responde por un producto |
| `/corridas` | Corridas registradas (32) | La PMO |
| `/estado.json` | Fecha del informe y peticiones abiertas | Un mecanismo |

- **Qué no hace:** no calcula, no escribe fichas (solo crea peticiones en `estado/peticiones/`), no autentica y no manda correos.
- **A quién se lo pasas:** `http://127.0.0.1:8789/` solo funciona en este equipo, para quien esté sentado aquí. No se lo mandes a nadie.
- **Cuándo se desactualiza:** el informe es del 2026-10-16 y queda viejo con el siguiente barrido o cuando cambien los documentos. La portada muestra su fecha.
- **Para el patrocinador:** hay que pasar a «que quede corriendo». Eso exige pedir a la organización un host y un puerto, publicarlo detrás de su control de acceso, y que el equipo siga encendido.

La corrida quedó registrada como `2026-10-16-portfolio-server-1`, con lo mostrado en `estado/corridas/salida-portfolio-server.md`. La nota de esa corrida dice «puerto 8787», pero lo que se usó fue el 8789.