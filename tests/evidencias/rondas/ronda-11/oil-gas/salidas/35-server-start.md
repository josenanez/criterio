# /criterio-server:server-start rato

Arrancó bien y la prueba de 8 segundos lo cortó, como se esperaba. Era una verificación y no queda nada corriendo.

## Rostrum, para mirarlo un rato

Levantó sin problemas. El mapa y el disco coinciden: no hay entradas nuevas ni sin estado. Los términos (v1.2) estaban vigentes, así que no hubo que registrar aceptación.

El mapa tiene 3 entradas: el portafolio (Vera), PRY-200 (Samuel) y PRD-302 (Alba), todas de la familia PMO.

Para volver a levantarlo y dejarlo abierto:

```
python3 "/home/claude/banco/plugins/criterio-server/scripts/servidor.py" --mapa /tmp/claude-0/-home-claude/692b0e4d-0e89-5e8d-a391-2cabbf233557/scratchpad/r11/oil-gas/espacio/.criterio/rostrum/config.json
```

Escucha en `127.0.0.1:8787`, solo en ese equipo. Si el puerto está ocupado, agrega `--puerto 8788`. Se detiene con Ctrl-C.

| Ruta | Qué es | Para quién |
|---|---|---|
| `/` | Portada con los agentes, una puerta por familia y el formulario de peticiones | Todos |
| `/pmo` | Informes de la PMO | La PMO y el patrocinador |
| `/decisiones` | Material del comité | El comité |
| `/proyectos` | 13 proyectos | La PMO |
| `/productos` | 4 productos | Producto y la PMO |
| `/corridas` | 33 corridas de los agentes | Quien audita |
| `/estado.json` | De cuándo es cada cosa y cuántas peticiones hay abiertas | Un mecanismo, no una persona |

Rutas como `/caso/<código>`, `/vence` o `/familia/…` solo aparecen si el mapa tiene esas familias. Aquí solo hay PMO.

**Qué enlace pasarle a quién:**
- Al patrocinador: `/`.
- Al comité: `/decisiones`.
- A quien audita: `/corridas`.

Cada página dice de cuándo es lo que muestra. Los informes en `reportes/` son del 2026-10-23, 06:52. Conviene decírselo a quien reciba el enlace.

**Límites:**
- Rostrum sirve lo que los agentes ya escribieron. No calcula, no autentica y no manda correos.
- El único archivo que crea es la petición, en `peticiones/` del agente elegido en el formulario. Esa petición espera hasta que ese agente despierte.
- Un enlace que funcione mañana requiere la otra forma, «que quede corriendo». Esa forma necesita un host y puerto internos, y que lo publiquen detrás de su control de acceso. Esa pregunta no se hizo en esta sesión.