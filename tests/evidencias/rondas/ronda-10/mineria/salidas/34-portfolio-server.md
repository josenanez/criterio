# /criterio-portfolio:portfolio-server rato

Rostrum funciona con el informe de este portafolio, pero en el puerto 8788, no en el 8787. El 8787 ya lo ocupaba otro servidor que sirve un informe distinto. Sus productos son ahorro-a-la-vista, microcredito y otros, y no coinciden con los de esta carpeta. No lo toqué.

- **Términos:** ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-18). No registré nada nuevo.
- **Modo:** «para mirarlo un rato», como pedía el argumento. Escucha solo en `127.0.0.1`, sin autenticación, y no hubo nada que pedirle a seguridad.
- **Informe servido:** `reportes/`, con 13 proyectos (PRY-199 a PRY-211) y 6 productos. Es del 2026-10-18 y tiene 0 peticiones abiertas.
- **Corrida:** quedó registrada como `2026-10-18-portfolio-server-1`, y lo que le mostré a la persona está en `estado/corridas/salida-portfolio-server.md`.
- **Estado ahora:** la prueba la levanté con un límite de 30 segundos, así que ya se apagó. Para dejarlo corriendo, ejecuta esto en `/home/claude/banco/ronda-10/mineria/espacio` y para con Ctrl-C:

```
python3 "/home/claude/banco/criterio/plugins/criterio-portfolio/scripts/servidor.py" --informe reportes --estado estado --config .criterio/portafolio/config.json --puerto 8788
```

**Qué enlace pasarle a quién:**
- `http://127.0.0.1:8788/` y `/pmo` son para la PMO.
- `/decisiones` es para el comité y el patrocinador, pero solo se abre desde esta máquina. El patrocinador no puede usar estos enlaces.
- Para darle un enlace que funcione mañana hay que pasar a «que quede corriendo» (`--abierto`). Eso pide un host y puerto internos, y publicarlo detrás del control de acceso de la organización.

El informe es del 2026-10-18 y se desactualiza cuando se corra de nuevo `/portfolio-report html`. La portada muestra su fecha.