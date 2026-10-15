# /criterio-portfolio:portfolio-server rato

Rostrum está corriendo en modo «para mirarlo un rato». Lo levanté yo, así que se queda encendido hasta que se pare el proceso; no hay Ctrl-C porque corre en segundo plano.

No hubo nadie a quien preguntarle «¿rato o que quede corriendo?». Tomé `rato`, que es lo que pediste en el argumento y lo que se recomienda cuando no se sabe cuál se quiere. Los términos ya estaban vigentes (versión 0.3.9, aceptados por José Francisco Ñáñez el 2026-10-15), así que no los registré otra vez.

**Dirección:** http://127.0.0.1:8787/. Escucha solo en este equipo. Sirve el informe de `reportes/2026-10-15-portafolio` con el nombre «Retail (prueba)». Respondió bien a una consulta de prueba: 13 proyectos, 7 productos y 0 peticiones abiertas.

| Ruta | Qué es | Para quién |
|---|---|---|
| `/` | Portada con las tres secciones y el formulario de peticiones | Todos |
| `/pmo` | Cómo va el portafolio: verdes sin sustento, silencios, patrocinadores repetidos | La PMO |
| `/decisiones` | Lo que necesita una decisión, con la consecuencia de no decidirla | Comité y patrocinador |
| `/proyectos` | Listado de 13 proyectos, ordenado por lo que más pide atención | Todos |
| `/p/<código>` | Informe de un proyecto, con enlace a su producto | Quien gerencia |
| `/productos` y `/producto/<nombre>` | Los productos y los proyectos que los construyen, en los dos sentidos | Quien responde por un producto |
| `/estado.json` | Fecha del informe y peticiones abiertas | Un mecanismo |

También aparece `/corridas`, con 32 corridas registradas.

**Lo que no hace:**
- **Calcular:** sirve lo que ya escribió el informe.
- **Escribir fichas:** solo crea la petición del formulario, en `estado/peticiones/`.
- **Autenticar:** quien autentica es la organización.
- **Mandar nada:** ni correo ni notificaciones.

Las peticiones esperan al agente: `due` las cuenta y rompen el silencio de `/portfolio-wake`.

**Qué enlace a quién:** por ahora a nadie. Esta dirección solo abre en este equipo, así que el patrocinador no tiene un enlace que le funcione mañana. Para eso está «que quede corriendo», con `--abierto`. Hay que pedirle a la organización:
- un host y un puerto dentro de la red;
- publicarlo detrás de su control de acceso;
- que el equipo siga encendido.

Con el portal ya visto funcionando, esa conversación con seguridad es más fácil.

**Cuándo se desactualiza:** el informe es del 2026-10-15. Queda viejo en cuanto cambien los documentos o se corra otro barrido, y conviene regenerarlo antes del comité del 2026-10-22. La portada muestra su fecha.

**Registro de la corrida:**
- `estado/corridas/salida-portfolio-server.md`
- `estado/corridas/2026-10-15-portfolio-server-1.md`

La salida del servidor está en `/tmp/claude-0/rostrum.log`.