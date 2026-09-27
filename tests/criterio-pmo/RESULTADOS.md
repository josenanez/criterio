# Resultado de las pruebas · Vera y Rostrum

**el agente de la PMO y el servidor que publica su informe** · plugin `criterio-pmo`

Corrida del 2026-09-27, sobre el commit `a0996a0`, con cambios en el árbol todavía sin confirmar. **6 puertas · 202 comprobaciones · todas en verde.**

> Este archivo lo escribe `python3 scripts/resultados.py` desde una corrida real. No se edita a mano: la corrida siguiente lo reemplaza.

## Lo que se corrió

| Puerta | Qué prueba | Comprob. | Tiempo | |
|---|---|---:|---:|---|
| `criterio-pmo/generar.py` | El portafolio sintético: seis proyectos, con un control negativo | — | 54 ms | verde |
| `criterio-pmo/pmo.py selftest` | La aritmética, la cadencia, la cola y el contraste entre las dos fichas | 66 | 22 ms | verde |
| `criterio-pmo/texto.py` | Leer .docx, .xlsx, .pptx y .eml sin dependencias | 12 | 19 ms | verde |
| `criterio-pmo/informe.py` | El informe: concordancia, formato de cifra, y que ninguna ruta salga en crudo | 15 | 16 ms | verde |
| `criterio-pmo/servidor.py` | Rostrum: rutas, que no se salga de la carpeta, y que no escriba la ficha | 30 | 36 ms | verde |
| `criterio-pmo/grade.py` | Vera contra respuestas escritas a mano, incluido el control negativo | 79 | 189 ms | verde |

Una puerta sin comprobaciones no es una puerta vacía: **genera el material sintético** o verifica una estructura completa, y falla entera si algo no está.

## Lo que esta corrida no cubre

Va aquí y no en un anexo. Un resultado de pruebas que solo dice lo que pasó es publicidad; lo que lo vuelve auditable es lo que dice que todavía no se sabe.

- **La extracción nunca se ha corrido.** El estado se siembra copiando `expected/fichas/`, así que la cadena documento → modelo → ficha no se ha ejercitado. `grade.py --fichas` existe para eso.
- **Los diecisiete comandos no se han corrido con un agente de verdad.** Están verificados como estructura —existen, declaran, y no invocan un skill que no esté—, y eso no es lo mismo que haberlos ejercitado.
- **Nada se ha corrido sobre la documentación real de una organización.** Todo el material es sintético y construido desde cero.

## Qué material se usó, y qué prueba cada pieza

El detalle del corpus —qué planta cada proyecto o producto, por qué, y cuál es su control negativo— está en [`EVIDENCIA.md`](EVIDENCIA.md), que se escribe a mano y no se genera.

**El control negativo es la mitad del valor de estas pruebas.** Un agente que encuentra hallazgos donde no los hay es un generador de ruido, y eso no se detecta mirando solo los casos que sí fallan.

## Y lo que se verifica para toda la familia

| Puerta | Qué prueba | Comprob. | |
|---|---|---:|---|
| `tests/coherencia.py` | Que la documentación y el código digan lo mismo | 57 | verde |
| `scripts/validate_plugins.py` | Que el marketplace y cada plugin estén completos | — | verde |
| `scripts/sincronizar.py` | Que las copias compartidas no se hayan separado | — | verde |
| `scripts/resultados.py` | Que la página de resultados no deje una puerta sin dueño | 14 | verde |

El conjunto de los tres agentes, con gráficas, en [`docs/pruebas.html`](../../docs/pruebas.html). Todo corre con la librería estándar y sin instalar nada.
