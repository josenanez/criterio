# /criterio-server:server-start rato

Rostrum arrancó bien, pero lo paró el límite de 15 s de esta sesión. Mientras estuvo arriba imprimió sus direcciones, y ahora no está corriendo. No pude dejarlo en segundo plano, porque la herramienta de comandos de esta sesión no lo permite.

**Lo que sirve el mapa** (3 entradas: Vera/portafolio, Samuel/PRY-201, Alba/PRD-305; el mapa está al día, sin entradas nuevas, desaparecidas ni sin estado):

| Ruta | Qué hay |
|---|---|
| `/` | Portada con las tres puertas y el formulario de peticiones |
| `/pmo` | Informes de la PMO |
| `/decisiones` | Material para el comité |
| `/proyectos` | 13 proyectos (PRY-199 a PRY-211) |
| `/productos` | 5 productos |
| `/corridas` | 33 corridas |
| `/estado.json` | De cuándo es lo de cada agente (para un mecanismo, no una persona) |

**Para levantarlo a mano**, en una terminal propia:

```
python3 "/home/claude/banco/plugins/criterio-server/scripts/servidor.py" --mapa .criterio/rostrum/config.json
```

Escucha solo en `127.0.0.1:8787` y se para con Ctrl-C. Si el puerto está ocupado, agrega `--puerto 8788`.

**Qué enlace pasar a quién**, cuando lo dejen corriendo:
- **Patrocinador:** `/`.
- **Comité:** `/decisiones`.
- **Gerencia:** `/pmo` y `/proyectos`. `/vence` y `/familia/…` no aparecieron en las direcciones que imprimió, porque el mapa solo tiene la familia PMO.

Cada página dice de cuándo es lo que muestra. Los informes de `reportes/` son del 2026-10-22. Conviene decírselo a quien reciba el enlace.

**Qué no hace.** No calcula, no autentica, no manda correos y no escribe fichas. Lo único que crea son las peticiones, en la carpeta `peticiones/` de cada agente.

**Para dejarlo corriendo** (`--abierto`), la organización tendría que dar un host y un puerto internos y publicarlo detrás de su control de acceso, porque el servidor no autentica. No necesita nada más. Por ahora, como pidió `rato`, no hace falta.