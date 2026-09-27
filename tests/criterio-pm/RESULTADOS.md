# Resultado de las pruebas · Samuel

**el agente del gerente de proyecto** · plugin `criterio-pm`

Corrida del 2026-09-27, sobre el commit `a8abd51`, con cambios en el árbol todavía sin confirmar. **4 puertas · 97 comprobaciones · todas en verde.**

> Este archivo lo escribe `python3 scripts/resultados.py` desde una corrida real. No se edita a mano: la corrida siguiente lo reemplaza.

## Lo que se corrió

| Puerta | Qué prueba | Comprob. | Tiempo | |
|---|---|---:|---:|---|
| `criterio-pm/generar.py` | Un proyecto visto desde adentro: dos proyectos, siete minutas | — | 38 ms | verde |
| `criterio-pm/pmo.py selftest` | La copia de la aritmética corre sola, sin tocar el otro plugin | 66 | 36 ms | verde |
| `criterio-pm/texto.py` | La copia de la conversión, igual | 12 | 23 ms | verde |
| `criterio-pm/grade.py` | Samuel contra respuestas escritas leyendo las minutas | 19 | 36 ms | verde |

Una puerta sin comprobaciones no es una puerta vacía: **genera el material sintético** o verifica una estructura completa, y falla entera si algo no está.

## Lo que esta corrida no cubre

Va aquí y no en un anexo. Un resultado de pruebas que solo dice lo que pasó es publicidad; lo que lo vuelve auditable es lo que dice que todavía no se sabe.

- **La extracción nunca se ha corrido.** El corpus siembra las fichas, así que la cadena documento → modelo → ficha no se ha ejercitado. `grade.py --fichas` existe para eso.
- **La agenda, el acta y el informe no se califican con esto.** Lo que producen es redacción sobre la minuta, y un calificador determinista no la mide. Lo que sí se verifica es la aritmética de la que salen sus cifras.
- **La ficha publicada y su contraste no se han corrido de punta a punta.** `/pm-publish` escribe y `contrastar()` emite la señal con sus dos citas, verificado sobre fichas sintéticas. Falta que un agente de verdad publique y otro de verdad lea.

## Qué material se usó, y qué prueba cada pieza

El detalle del corpus —qué planta cada proyecto o producto, por qué, y cuál es su control negativo— está en [`EVIDENCIA.md`](EVIDENCIA.md), que se escribe a mano y no se genera.

**El control negativo es la mitad del valor de estas pruebas.** Un agente que encuentra hallazgos donde no los hay es un generador de ruido, y eso no se detecta mirando solo los casos que sí fallan.

## Y lo que se verifica para toda la familia

| Puerta | Qué prueba | Comprob. | |
|---|---|---:|---|
| `tests/coherencia.py` | Que la documentación y el código digan lo mismo | 53 | verde |
| `scripts/validate_plugins.py` | Que el marketplace y cada plugin estén completos | — | verde |
| `scripts/sincronizar.py` | Que las copias compartidas no se hayan separado | — | verde |
| `scripts/resultados.py` | Que la página de resultados no deje una puerta sin dueño | 14 | verde |

El conjunto de los tres agentes, con gráficas, en [`docs/pruebas.html`](../../docs/pruebas.html). Todo corre con la librería estándar y sin instalar nada.
