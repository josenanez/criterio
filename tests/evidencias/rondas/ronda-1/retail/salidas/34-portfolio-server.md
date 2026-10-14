# /criterio-portfolio:portfolio-server rato

Rostrum arrancó bien en modo «para mirarlo un rato». El comando de prueba lo paró a los 8 segundos, así que ahora no está corriendo. Para mirarlo, relanza el mismo comando en una terminal propia.

- **Modo:** «para mirarlo un rato». Nadie podía responder, así que tomé la respuesta sugerida. No hay nada que pedirle a seguridad.
- **Términos:** `TERMS.md` es la versión 1.0 y la configuración ya la tiene aceptada (José Francisco Ñáñez, 2026-10-14).
- **Qué sirve:** el informe que ya está en `reportes/`: 13 proyectos, 7 productos y 28 corridas. El estado sale de `estado-portafolio/`.
- **Dónde escucha:** `http://127.0.0.1:8787/`, solo en este equipo. Si el puerto está ocupado, usa `--puerto 8788`.

Para relanzarlo, pega este comando:
```
python3 "/home/claude/banco/criterio/plugins/criterio-portfolio/scripts/servidor.py" --informe /home/claude/banco/ronda-1/retail/espacio/reportes --estado /home/claude/banco/ronda-1/retail/espacio/estado-portafolio --config /home/claude/banco/ronda-1/retail/espacio/.criterio/portafolio/config.json
```

| Ruta | Para quién |
|---|---|
| `/` | Todos: portada con las tres secciones y el formulario de peticiones |
| `/pmo` | La PMO: los verdes que la evidencia no sostiene, los silencios y los patrocinadores repetidos |
| `/decisiones` | El comité y el patrocinador: preguntas cerradas con la consecuencia de no decidir |
| `/proyectos`, `/p/<código>` | Todos y quien gerencia: listado por urgencia e informe de cada proyecto, con enlace a su producto |
| `/productos`, `/producto/<nombre>` | Quien responde por un producto: informe con enlace a los proyectos que lo construyen |
| `/estado.json` | Un mecanismo, no una persona: fecha del informe y peticiones abiertas |

**Lo que no hace:**
- No calcula: sirve lo que el informe ya tiene escrito.
- No escribe fichas. Lo único que crea es la petición, en `estado-portafolio/peticiones/`.
- No autentica.
- No manda correos ni avisos.

**Enlace y vigencia:** `http://127.0.0.1:8787/` solo lo ve quien esté en este equipo, así que el patrocinador no puede abrirlo. Si necesita un enlace estable, el siguiente paso es «que quede corriendo» con `--abierto`. Eso exige pedir a la organización un host y puerto internos y publicarlo detrás de su control de acceso. El informe vale hasta su última generación y la portada muestra la fecha. Si cambian los documentos, corre `/portfolio-report html` otra vez.

**Corrida registrada:** `2026-10-14-portfolio-server-1`, con la salida en `estado-portafolio/corridas/salida-portfolio-server.md`. No se midieron segundos ni documentos, porque este comando no usa `corrida-inicio`.