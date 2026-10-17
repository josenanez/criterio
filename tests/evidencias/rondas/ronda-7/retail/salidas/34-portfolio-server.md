# /criterio-portfolio:portfolio-server rato

Rostrum está corriendo en **http://127.0.0.1:8788/**, en modo «rato». Solo se ve desde este equipo.

- **Puerto:** el 8787 ya lo ocupaba otro servidor. Ese otro servidor sirve un portafolio distinto, con productos como ahorro a la vista y microcrédito. El de este portafolio usa el 8788, y lo comprobé con `/estado.json`. Registré la corrida antes de esta corrección, así que su nota dice 8787. El archivo de salida ya dice 8788.
- **Términos:** ya estaban vigentes. Los aceptó José Francisco Ñáñez el 2026-10-17, así que no hubo que registrar nada.
- **Modo:** nadie pudo contestar la pregunta de las dos formas. Tomé la sugerida, que es empezar por «para mirarlo un rato».
- **Qué hay:**
  - La portada y `/pmo`.
  - `/decisiones`.
  - `/proyectos`, con 13 proyectos (PRY-199 a PRY-211).
  - `/productos`, con 7 productos.
  - `/corridas`, con 32 corridas.
  - Hay 0 peticiones abiertas.
- **Qué no hace:** no calcula nada, solo sirve el informe ya generado. Tampoco escribe fichas, no autentica y no manda correos.
- **A quién pasarle el enlace:** a nadie. Un patrocinador no puede abrir 127.0.0.1. Para darle un enlace estable hay que pasar a «que quede corriendo», con `--abierto` y un host y puerto dentro de la red. La organización debe publicarlo detrás de su control de acceso, porque el servidor no autentica.
- **Cuándo se desactualiza:** el informe es del 2026-10-17. Se desactualiza cuando cambien las fichas o se vuelva a correr `/portfolio-report html`. La portada muestra su fecha.
- **Cómo pararlo:** al estar en segundo plano no hay Ctrl-C. Se para terminando su proceso, por ejemplo con `pkill -f "servidor.py"`. Ese comando mataría también cualquier otro servidor.py que esté corriendo.

La salida completa quedó en `estado/corridas/salida-portfolio-server.md`.