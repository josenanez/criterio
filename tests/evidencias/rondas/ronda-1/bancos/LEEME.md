# Ronda 1 · bancos

Los 37 comandos de Vera, Samuel y Alba, en orden, sobre datos de prueba de entidades
financieras de Suramérica (bancos), con la versión 0.3.6 y el modelo `claude-sonnet-5-5`.

- `salidas/NN-comando.md` — lo que el comando le mostró a la persona, tal cual.
- `salidas/NN-comando.json` — cuánto tardó, cuántos tokens usó y qué archivos cambió.
- `revision.json` — el contrato de cada comando y la auditoría de que ningún agente leyó la clave.
- `calificacion-samuel-alba.json` — los compromisos de Samuel y las alertas del producto de Alba contra la clave.
- `clave/` — lo que el agente nunca vio: la clave de la ronda y los objetivos de cada comando.
- `documentos.tgz` — la carpeta que leyó el agente. `estado-del-agente.tgz` — lo que escribió.

La calificación de Vera está en `tests/evidencias/calificaciones.json` y los defectos en
`tests/evidencias/defectos.json`. Se reconstruye con `python3 tests/ronda.py armar bancos <carpeta> --ronda 1`
el mismo día del corte (2026-10-14): las fechas del material son relativas al día en que se arma.
