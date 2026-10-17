# Qué se probó, y qué no

Esta página sale de una corrida, no de un resumen escrito a mano. Cada cifra viene de ejecutar el mismo comando que corre `scripts/verificar.py` y contar las comprobaciones que ese comando imprimió. Con la librería estándar y sin instalar nada.

Corrida del 2026-10-17, sobre el commit `eeef25fa`, con cambios en el árbol todavía sin confirmar.

**33 de 33 puertas en verde · 732 comprobaciones · 14 corpus, cada uno con su control negativo · 28.9 s la corrida entera.**

> La versión con gráficas, para abrir en un navegador, está en [`pruebas.html`](pruebas.html). Esta es la misma corrida, legible en GitHub.

## En conjunto

Comprobaciones por dueño. Los tamaños no son comparables entre sí y no pretenden serlo: lo que dice esta gráfica es dónde está puesta la verificación.

| Dueño | | Comprob. |
|---|---|---:|
| **Vera** | `████████████████████████████` | 223 |
| **Samuel** | `██████████████████` | 145 |
| **Alba** | `█████████████` | 107 |
| **Rostrum** | `████████` | 67 |
| **La familia** | `██████████████████████` | 172 |

## Vera · Agente PMO

Del latín *verus*: lo verdadero. Dice lo que los documentos dicen, no lo que se reporta.

| Puerta | Qué prueba | Comprob. | Tiempo | |
|---|---|---:|---:|---|
| `criterio-portfolio/generar.py` | El portafolio sintético: seis proyectos, con un control negativo | — | 68 ms | verde |
| `criterio-portfolio/portafolio.py selftest` | La aritmética, la cadencia, la cola y el contraste entre las dos fichas | 112 | 151 ms | verde |
| `criterio-portfolio/texto.py` | Leer .docx, .xlsx, .pptx y .eml sin dependencias | 14 | 64 ms | verde |
| `criterio-portfolio/informe.py` | El informe: concordancia, formato de cifra, y que ninguna ruta salga en crudo | 18 | 41 ms | verde |
| `criterio-portfolio/grade.py` | Vera contra respuestas escritas a mano, incluido el control negativo | 79 | 445 ms | verde |

Su análisis propio, con qué material se usó y qué no cubre, en [`tests/criterio-portfolio/RESULTADOS.md`](../tests/criterio-portfolio/RESULTADOS.md).

## Samuel · Agente de proyecto

«El que escuchó». Su función central es el compromiso dicho y no cumplido.

| Puerta | Qué prueba | Comprob. | Tiempo | |
|---|---|---:|---:|---|
| `criterio-project/generar.py` | Un proyecto visto desde adentro: dos proyectos, siete minutas | — | 65 ms | verde |
| `criterio-project/portafolio.py selftest` | La copia de la aritmética corre sola, sin tocar el otro plugin | 112 | 120 ms | verde |
| `criterio-project/texto.py` | La copia de la conversión, igual | 14 | 51 ms | verde |
| `criterio-project/grade.py` | Samuel contra respuestas escritas leyendo las minutas | 19 | 102 ms | verde |

Su análisis propio, con qué material se usó y qué no cubre, en [`tests/criterio-project/RESULTADOS.md`](../tests/criterio-project/RESULTADOS.md).

## Alba · Agente de producto

El amanecer: la luz que hay antes de que se vea nada. Trabaja antes de que exista el proyecto.

| Puerta | Qué prueba | Comprob. | Tiempo | |
|---|---|---:|---:|---|
| `criterio-product/generar.py` | Lo que hay antes del proyecto: dos productos, con un control negativo | — | 46 ms | verde |
| `criterio-product/producto.py selftest` | El registro de requerimiento: evidencia, supuestos, trazas y la cifra del negocio | 64 | 92 ms | verde |
| `criterio-product/grade.py` | Alba contra respuestas escritas leyendo la definición y las entrevistas | 43 | 300 ms | verde |

Su análisis propio, con qué material se usó y qué no cubre, en [`tests/criterio-product/RESULTADOS.md`](../tests/criterio-product/RESULTADOS.md).

## Rostrum · El servidor

Una tribuna. Sostiene lo que ya está escrito, donde el equipo puede leerlo. No decide nada, y por eso no lleva nombre de persona.

| Puerta | Qué prueba | Comprob. | Tiempo | |
|---|---|---:|---:|---|
| `criterio-portfolio/servidor.py` | Rostrum: rutas, que no se salga de la carpeta, y que no escriba la ficha | 67 | 720 ms | verde |

Su análisis propio, con qué material se usó y qué no cubre, en [`tests/criterio-portfolio/RESULTADOS.md`](../tests/criterio-portfolio/RESULTADOS.md).

## La familia · Lo que los tres comparten

Que la documentación y el código digan lo mismo, que el marketplace esté completo, que las copias compartidas no se hayan separado, y que el recorrido encuentre los documentos sin importar cómo estén organizados.

| Puerta | Qué prueba | Comprob. | Tiempo | |
|---|---|---:|---:|---|
| `sintetico/corpus.py` | El motor del material: la estructura de referencia y las cuatro disposiciones | 31 | 30 ms | verde |
| `sintetico/sectores.py` | Tres industrias con el mismo motor de hechos: finanzas, retail y minería | — | 13 ms | verde |
| `sintetico/formatos.py` | El material en Word, Excel y PDF, y que el plugin lo lea | — | 80 ms | verde |
| `sintetico/disposiciones.py` | Que el recorrido encuentre los mismos documentos sin importar cómo estén | 16 | 120 ms | verde |
| `sintetico/cobertura.py` | Que ninguna señal se quede sin disparar sin que esté declarado por qué | 3 | 325 ms | verde |
| `sintetico/resumen.py` | El resumen de las corridas diarias: precisión, cobertura y qué se movió | — | 31 ms | verde |
| `sintetico/regresion.py verificar` | La regresión del motor: cinco semanas de una organización, en cada cambio | 1 | 25259 ms | verde |
| `sintetico/evidencia.py verificar` | Que el registro de comandos no prometa una evidencia que no está | 1 | 32 ms | verde |
| `tests/ronda.py verificar` | Que cada defecto registrado diga su origen, su corrección y dónde se verificó | 1 | 87 ms | verde |
| `tests/banco.py verificar` | Que cada calificación del agente salga de sus conteos, con intervalo y origen | 1 | 52 ms | verde |
| `sintetico/funcionalidades.py` | Que cada comando declare qué produce y qué deja escrito | 1 | 38 ms | verde |
| `criterio-portfolio/terminos.py` | Los términos: una aceptación por versión, con comprobante en Markdown y PDF y su huella SHA-256 | 14 | 53 ms | verde |
| `scripts/registro.py verificar` | El registro de versiones: cada entrada con su huella y la de la anterior, sin huecos | 1 | 51 ms | verde |
| `tests/coherencia.py` | Que la documentación y el código digan lo mismo | 84 | 175 ms | verde |
| `tests/contratos.py` | Que cada comando y cada skill cumplan su contrato | 1 | 47 ms | verde |
| `scripts/validate_plugins.py` | Que el marketplace y cada plugin estén completos | — | 33 ms | verde |
| `scripts/sincronizar.py` | Que las copias compartidas no se hayan separado | — | 42 ms | verde |
| `scripts/manual.py` | Que el manual diga lo que dicen los README y los contratos | 1 | 43 ms | verde |
| `scripts/resultados.py` | Que la página de resultados no deje una puerta sin dueño | 16 | 61 ms | verde |

## Lo que esta corrida no cubre

Va aquí y no en un anexo. Una página de resultados que solo dice lo que pasó es publicidad; lo que la vuelve auditable es lo que dice que todavía no se sabe.

- **La extracción nunca se ha corrido.** Los tres corpus siembran el estado desde sus respuestas de referencia, así que la cadena documento → modelo → ficha no se ha ejercitado. `grade.py --fichas` y `grade.py --registros` existen para eso y no se han ejecutado.
- **Ningún comando se ha corrido con un agente de verdad.** Los 37 comandos están verificados como estructura —existen, declaran, y no invocan un skill que no esté—, y eso no es lo mismo que haberlos ejercitado.
- **Nada se ha corrido sobre la documentación real de una organización.** Todo el material es sintético y construido desde cero. Es la diferencia que protege a quien instale esto: **construido y verificado sobre corpus, no probado sobre documentación real.**
- **Lo que produce el modelo no lo mide un calificador determinista.** Convertir ocho entrevistas en temas con sus citas, redactar un acta o un informe es trabajo del modelo. Lo que se verifica aquí es la aritmética de la que salen sus cifras, y la estructura de lo que se le pide.

---

Reproducirlo: `python3 scripts/resultados.py`. El detalle de qué prueba cada corpus y qué no, en las tres páginas de evidencia bajo `tests/`.
