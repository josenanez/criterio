# /criterio-portfolio:portfolio-server rato

Rostrum está corriendo en `http://127.0.0.1:8788/`, en modo «para mirarlo un rato». Solo es accesible desde esta máquina.

**Qué pasó:**
- **Puerto:** el 8787 ya lo ocupaba otro proceso. Sus datos no coinciden con este informe (otra lista de productos), así que no lo toqué y usé 8788.
- **Términos:** ya estaban vigentes (v0.3.13, aceptados por José Francisco Ñáñez el 2026-10-17). No hizo falta volver a registrarlos.
- **Modo:** nadie podía responder, así que tomé la respuesta sugerida, que es empezar por «para mirarlo un rato».
- **Informe servido:** `estado/reportes`, con 13 proyectos (PRY-199 a PRY-211) y 9 productos. Es del 2026-10-17 17:20.
- **Pruebas:** la portada y `/estado.json` responden con 200. Las demás rutas (`/pmo`, `/decisiones`, `/proyectos`, `/productos`, `/p/PRY-202`) responden con 302, es decir, redirigen a su página, y no seguí ninguna redirección.
- **Registro:** la corrida quedó como `2026-10-17-portfolio-server-1`, con la salida en `estado/corridas/salida-portfolio-server.md`. Esa salida ya dice 8788; la corrida se registró antes de que supiera que el 8787 estaba ocupado.

**Qué hay en el portal:**
- **Portada:** `/`, con el formulario de peticiones.
- **PMO:** `/pmo` es el estado del portafolio visto en conjunto.
- **Decisiones:** `/decisiones` es lo que el comité tiene que decidir.
- **Proyectos y productos:** `/proyectos` y `/productos` son los listados. `/p/<código>` y `/producto/<nombre>` enlazan entre sí en los dos sentidos.
- **Corridas y frescura:** `/corridas` muestra las 33 corridas registradas, y `/estado.json` dice de cuándo es el informe.

**Qué enlace pasarle a quién:** ninguno todavía. Este enlace solo funciona en esta máquina y mientras el proceso siga vivo, así que no sirve para el patrocinador. Para eso hace falta el modo «que quede corriendo». Habría que pedir a la organización un host y un puerto internos, y publicarlo detrás de su control de acceso, porque el servidor no autentica.

**Cuándo queda desactualizado:** en cuanto cambie una ficha o un documento. El próximo comité es el 2026-10-20, y conviene regenerar el informe con `/portfolio-report html` antes. La portada muestra la fecha del informe.

El servidor sigue en segundo plano; su log está en `/tmp/claude-0/-home-claude-banco-ronda-8-bancos-espacio/692b0e4d-0e89-5e8d-a391-2cabbf233557/scratchpad/rostrum.log`.