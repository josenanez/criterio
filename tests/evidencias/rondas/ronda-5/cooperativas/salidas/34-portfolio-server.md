# /criterio-portfolio:portfolio-server rato

Rostrum arrancó bien en `http://127.0.0.1:8787/`, pero lo corté a los 15 segundos porque lo lancé en primer plano. Ahora mismo no está corriendo.

- **Términos:** ya estaban vigentes (v1.1), aceptados por José Francisco Ñáñez el 2026-10-16. No hubo que pedir nada.
- **Forma elegida:** «para mirarlo un rato», como indicaba el argumento `rato`. Escucha solo en este equipo.
- **Informe servido:** `reportes/`, con 13 proyectos, 8 productos, `decisiones.html` y el listado de proyectos.
- **Falta `pmo.html`:** no está en `reportes/`, así que `/pmo` puede salir vacío hasta que corras `/portfolio-report html`. Rostrum no lo genera.
- **Corrida registrada:** `2026-10-16-portfolio-server-1`, con lo que te mostré en `estado/corridas/salida-portfolio-server.md`.

Para levantarlo y dejarlo corriendo (se apaga con Ctrl-C, o con `--puerto 8788` si el 8787 está ocupado), usa este comando:
```
python3 "/home/claude/banco/criterio/plugins/criterio-portfolio/scripts/servidor.py" --informe /home/claude/banco/ronda-5/cooperativas/espacio/reportes --estado /home/claude/banco/ronda-5/cooperativas/espacio/estado --config /home/claude/banco/ronda-5/cooperativas/espacio/.criterio/portafolio/config.json
```

**Qué enlace pasar a quién:** `http://127.0.0.1:8787/` solo lo abre quien esté en este equipo. El patrocinador no puede entrar con él, y para que tenga un enlace estable hay que elegir «que quede corriendo» (`--abierto`, detrás del control de acceso de la organización, porque Rostrum no autentica).

**Cuándo queda desactualizado:** el informe es del 2026-10-16. Deja de estar al día cuando cambie un documento o corra otro barrido; la portada muestra su fecha.