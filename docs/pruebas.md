# Qué se probó, y qué no

Esta página sale de una corrida, no de un resumen escrito a mano. Cada cifra viene de ejecutar el mismo comando que corre `scripts/verificar.py` y contar las comprobaciones que ese comando imprimió. Con la librería estándar y sin instalar nada.

Corrida del 2026-09-27, sobre el commit `d8dc751`, con cambios en el árbol todavía sin confirmar.

**17 de 17 puertas en verde · 483 comprobaciones · 3 corpus, cada uno con su control negativo · 1.6 s la corrida entera.**

> La versión con gráficas, para abrir en un navegador, está en [`pruebas.html`](pruebas.html). Esta es la misma corrida, legible en GitHub.

## En conjunto

Comprobaciones por dueño. Los tamaños no son comparables entre sí y no pretenden serlo: lo que dice esta gráfica es dónde está puesta la verificación.

| Dueño | | Comprob. |
|---|---|---:|
| **Vera** | `████████████████████████████` | 172 |
| **Samuel** | `████████████████` | 97 |
| **Alba** | `█████████████████` | 105 |
| **Rostrum** | `█████` | 30 |
| **La familia** | `█████████████` | 79 |

## Vera · Agente PMO

Del latín *verus*: lo verdadero. Dice lo que los documentos dicen, no lo que se reporta.

| Puerta | Qué prueba | Comprob. | Tiempo | |
|---|---|---:|---:|---|
| `criterio-pmo/generar.py` | El portafolio sintético: seis proyectos, con un control negativo | — | 58 ms | verde |
| `criterio-pmo/pmo.py selftest` | La aritmética, la cadencia, la cola y el contraste entre las dos fichas | 66 | 21 ms | verde |
| `criterio-pmo/texto.py` | Leer .docx, .xlsx, .pptx y .eml sin dependencias | 12 | 21 ms | verde |
| `criterio-pmo/informe.py` | El informe: concordancia, formato de cifra, y que ninguna ruta salga en crudo | 15 | 18 ms | verde |
| `criterio-pmo/grade.py` | Vera contra respuestas escritas a mano, incluido el control negativo | 79 | 210 ms | verde |

Su análisis propio, con qué material se usó y qué no cubre, en [`tests/criterio-pmo/RESULTADOS.md`](../tests/criterio-pmo/RESULTADOS.md).

## Samuel · Agente de proyecto

«El que escuchó». Su función central es el compromiso dicho y no cumplido.

| Puerta | Qué prueba | Comprob. | Tiempo | |
|---|---|---:|---:|---|
| `criterio-pm/generar.py` | Un proyecto visto desde adentro: dos proyectos, siete minutas | — | 40 ms | verde |
| `criterio-pm/pmo.py selftest` | La copia de la aritmética corre sola, sin tocar el otro plugin | 66 | 34 ms | verde |
| `criterio-pm/texto.py` | La copia de la conversión, igual | 12 | 24 ms | verde |
| `criterio-pm/grade.py` | Samuel contra respuestas escritas leyendo las minutas | 19 | 40 ms | verde |

Su análisis propio, con qué material se usó y qué no cubre, en [`tests/criterio-pm/RESULTADOS.md`](../tests/criterio-pm/RESULTADOS.md).

## Alba · Agente de producto

El amanecer: la luz que hay antes de que se vea nada. Trabaja antes de que exista el proyecto.

| Puerta | Qué prueba | Comprob. | Tiempo | |
|---|---|---:|---:|---|
| `criterio-product/generar.py` | Lo que hay antes del proyecto: dos productos, con un control negativo | — | 35 ms | verde |
| `criterio-product/producto.py selftest` | El registro de requerimiento: evidencia, supuestos, trazas y la cifra del negocio | 62 | 27 ms | verde |
| `criterio-product/grade.py` | Alba contra respuestas escritas leyendo la definición y las entrevistas | 43 | 116 ms | verde |

Su análisis propio, con qué material se usó y qué no cubre, en [`tests/criterio-product/RESULTADOS.md`](../tests/criterio-product/RESULTADOS.md).

## Rostrum · El servidor

Una tribuna. Sostiene lo que ya está escrito, donde el equipo puede leerlo. No decide nada, y por eso no lleva nombre de persona.

| Puerta | Qué prueba | Comprob. | Tiempo | |
|---|---|---:|---:|---|
| `criterio-pmo/servidor.py` | Rostrum: rutas, que no se salga de la carpeta, y que no escriba la ficha | 30 | 550 ms | verde |

Su análisis propio, con qué material se usó y qué no cubre, en [`tests/criterio-pmo/RESULTADOS.md`](../tests/criterio-pmo/RESULTADOS.md).

## La familia · Lo que los tres comparten

Que la documentación y el código digan lo mismo, que el marketplace esté completo, y que las copias compartidas no se hayan separado.

| Puerta | Qué prueba | Comprob. | Tiempo | |
|---|---|---:|---:|---|
| `tests/coherencia.py` | Que la documentación y el código digan lo mismo | 63 | 146 ms | verde |
| `scripts/validate_plugins.py` | Que el marketplace y cada plugin estén completos | — | 45 ms | verde |
| `scripts/sincronizar.py` | Que las copias compartidas no se hayan separado | — | 35 ms | verde |
| `scripts/resultados.py` | Que la página de resultados no deje una puerta sin dueño | 16 | 181 ms | verde |

## Lo que esta corrida no cubre

Va aquí y no en un anexo. Una página de resultados que solo dice lo que pasó es publicidad; lo que la vuelve auditable es lo que dice que todavía no se sabe.

- **La extracción nunca se ha corrido.** Los tres corpus siembran el estado desde sus respuestas de referencia, así que la cadena documento → modelo → ficha no se ha ejercitado. `grade.py --fichas` y `grade.py --registros` existen para eso y no se han ejecutado.
- **Ningún comando se ha corrido con un agente de verdad.** Los 37 comandos están verificados como estructura —existen, declaran, y no invocan un skill que no esté—, y eso no es lo mismo que haberlos ejercitado.
- **Nada se ha corrido sobre la documentación real de una organización.** Todo el material es sintético y construido desde cero. Es la diferencia que protege a quien instale esto: **construido y verificado sobre corpus, no probado sobre documentación real.**
- **Lo que produce el modelo no lo mide un calificador determinista.** Convertir ocho entrevistas en temas con sus citas, redactar un acta o un informe es trabajo del modelo. Lo que se verifica aquí es la aritmética de la que salen sus cifras, y la estructura de lo que se le pide.

---

Reproducirlo: `python3 scripts/resultados.py`. El detalle de qué prueba cada corpus y qué no, en las tres páginas de evidencia bajo `tests/`.
