# /criterio-portfolio:portfolio-server rato

Rostrum arrancó y escuchó en `http://127.0.0.1:8787/`, solo en este equipo. El comando se cortó a los 8 segundos que le puse de límite, así que ya no está corriendo. Lo probé solo hasta ver las direcciones que imprimió; no abrí ninguna página.

Elegí el modo «rato», que es el que pedías. Los términos 1.0 que acepta José Francisco Ñáñez (2026-10-14) coinciden con la versión de `TERMS.md`. El informe ya existía en `reportes/`, con 13 proyectos y 10 productos, así que no corrí `/portfolio-report`.

**A quién pasarle qué:**
- **Quien lo mira ahora, en este equipo:** `/` es la portada, `/pmo` es para la PMO y `/decisiones` para el comité o el patrocinador. Los listados están en `/proyectos` y `/productos`.
- **El patrocinador:** hoy no tiene un enlace que le sirva, porque la dirección solo abre en este equipo y no funciona mañana. Para eso hace falta el modo «que quede corriendo»: un host y un puerto dentro de la red, y publicarlo detrás del control de acceso que ya usa la organización. El servidor no autentica por sí mismo.

**Cuándo se desactualiza:** el informe es del 2026-10-14. Deja de reflejar la realidad en cuanto cambie un documento o pase el próximo barrido. La portada muestra su fecha.

**Registro de la corrida:** guardé lo que te mostré en `estado/corridas/salida-portfolio-server.md` y registré la corrida como `2026-10-14-portfolio-server-1`.

Para volver a levantarlo a mano, con Ctrl-C para pararlo:

```
python3 "/home/claude/banco/criterio/plugins/criterio-portfolio/scripts/servidor.py" --informe /home/claude/banco/ronda-1/bancos/espacio/reportes --estado /home/claude/banco/ronda-1/bancos/espacio/estado --config /home/claude/banco/ronda-1/bancos/espacio/.criterio/portafolio/config.json
```

Si el puerto 8787 está ocupado, agrega `--puerto 8788`.