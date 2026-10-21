# Qué se probó, y qué no

Esta página sale de una corrida, no de un resumen escrito a mano. Cada cifra viene de ejecutar el mismo comando que corre `scripts/verificar.py` y contar las comprobaciones que ese comando imprimió. Con la librería estándar y sin instalar nada.

Corrida del 2026-10-20, sobre el commit `0fa2601`, con cambios en el árbol todavía sin confirmar.

**46 de 46 puertas en verde · 872 comprobaciones · 20 corpus, cada uno con su control negativo · 30.1 s la corrida entera.**

> La versión con gráficas, para abrir en un navegador, está en [`pruebas.html`](pruebas.html). Esta es la misma corrida, legible en GitHub.

## En conjunto

Comprobaciones por dueño. Los tamaños no son comparables entre sí y no pretenden serlo: lo que dice esta gráfica es dónde está puesta la verificación.

| Dueño | | Comprob. |
|---|---|---:|
| **Vera** | `████████████████████████████` | 237 |
| **Samuel** | `███████████████████` | 157 |
| **Alba** | `█████████████` | 107 |
| **Rostrum** | `████████` | 67 |
| **Clara** | `████` | 35 |
| **Tomás** | `█` | 7 |
| **Fidel** | `██` | 18 |
| **Constanza** | `█` | 7 |
| **La familia** | `██████████████████████████` | 219 |

## Vera · Agente PMO

Del latín *verus*: lo verdadero. Dice lo que los documentos dicen, no lo que se reporta.

| Puerta | Qué prueba | Comprob. | Tiempo | |
|---|---|---:|---:|---|
| `criterio-portfolio/generar.py` | El portafolio sintético: seis proyectos, con un control negativo | — | 59 ms | verde |
| `criterio-portfolio/portafolio.py selftest` | La aritmética, la cadencia, la cola y el contraste entre las dos fichas | 115 | 117 ms | verde |
| `criterio-portfolio/texto.py` | Leer .docx, .xlsx, .pptx y .eml sin dependencias | 23 | 63 ms | verde |
| `criterio-portfolio/informe.py` | El informe: concordancia, formato de cifra, y que ninguna ruta salga en crudo | 20 | 57 ms | verde |
| `criterio-portfolio/grade.py` | Vera contra respuestas escritas a mano, incluido el control negativo | 79 | 467 ms | verde |

Su análisis propio, con qué material se usó y qué no cubre, en [`tests/criterio-portfolio/RESULTADOS.md`](../tests/criterio-portfolio/RESULTADOS.md).

## Samuel · Agente de proyecto

«El que escuchó». Su función central es el compromiso dicho y no cumplido.

| Puerta | Qué prueba | Comprob. | Tiempo | |
|---|---|---:|---:|---|
| `criterio-project/generar.py` | Un proyecto visto desde adentro: dos proyectos, siete minutas | — | 46 ms | verde |
| `criterio-project/portafolio.py selftest` | La copia de la aritmética corre sola, sin tocar el otro plugin | 115 | 122 ms | verde |
| `criterio-project/texto.py` | La copia de la conversión, igual | 23 | 58 ms | verde |
| `criterio-project/grade.py` | Samuel contra respuestas escritas leyendo las minutas | 19 | 121 ms | verde |

Su análisis propio, con qué material se usó y qué no cubre, en [`tests/criterio-project/RESULTADOS.md`](../tests/criterio-project/RESULTADOS.md).

## Alba · Agente de producto

El amanecer: la luz que hay antes de que se vea nada. Trabaja antes de que exista el proyecto.

| Puerta | Qué prueba | Comprob. | Tiempo | |
|---|---|---:|---:|---|
| `criterio-product/generar.py` | Lo que hay antes del proyecto: dos productos, con un control negativo | — | 31 ms | verde |
| `criterio-product/producto.py selftest` | El registro de requerimiento: evidencia, supuestos, trazas y la cifra del negocio | 64 | 85 ms | verde |
| `criterio-product/grade.py` | Alba contra respuestas escritas leyendo la definición y las entrevistas | 43 | 297 ms | verde |

Su análisis propio, con qué material se usó y qué no cubre, en [`tests/criterio-product/RESULTADOS.md`](../tests/criterio-product/RESULTADOS.md).

## Rostrum · El servidor

Una tribuna. Sostiene lo que ya está escrito, donde el equipo puede leerlo. No decide nada, y por eso no lleva nombre de persona.

| Puerta | Qué prueba | Comprob. | Tiempo | |
|---|---|---:|---:|---|
| `criterio-portfolio/servidor.py` | Rostrum: rutas, que no se salga de la carpeta, y que no escriba la ficha | 67 | 697 ms | verde |

Su análisis propio, con qué material se usó y qué no cubre, en [`tests/criterio-portfolio/RESULTADOS.md`](../tests/criterio-portfolio/RESULTADOS.md).

## Clara · Agente contralor

De *clarus*: que los libros digan lo mismo que los soportes. Cierra el mes contra su evidencia.

| Puerta | Qué prueba | Comprob. | Tiempo | |
|---|---|---:|---:|---|
| `criterio-finance/finanzas.py selftest` | El motor de Clara y Tomás: números, fechas, lectores de la DIAN y del SRI, y una entidad mínima | 28 | 92 ms | verde |
| `criterio-cfo/evaluar.py` | Que Clara levante cada señal sembrada en el cierre, y ninguna en los controles | 7 | 221 ms | verde |

Su análisis propio, con qué material se usó y qué no cubre, en [`tests/criterio-finance/RESULTADOS.md`](../tests/criterio-finance/RESULTADOS.md).

## Tomás · Agente de FP&A

«El gemelo»: pone el presupuesto al lado de su gemelo, la ejecución.

| Puerta | Qué prueba | Comprob. | Tiempo | |
|---|---|---:|---:|---|
| `criterio-cfo/evaluar.py` | Que Tomás levante cada señal sembrada en el presupuesto, y ninguna en los controles | 7 | 220 ms | verde |

Su análisis propio, con qué material se usó y qué no cubre, en [`tests/criterio-budget/RESULTADOS.md`](../tests/criterio-budget/RESULTADOS.md).

## Fidel · Agente de contratos

De *fides*: la palabra dada. Pone lo firmado al lado de lo que está pasando.

| Puerta | Qué prueba | Comprob. | Tiempo | |
|---|---|---:|---:|---|
| `criterio-legal/legal.py selftest` | El motor de Fidel y Constanza: fechas, prórrogas, plazos y una entidad mínima con todo mal | 11 | 68 ms | verde |
| `criterio-clo/evaluar.py` | Que Fidel levante cada señal sembrada en los contratos, y ninguna en los controles | 7 | 185 ms | verde |

Su análisis propio, con qué material se usó y qué no cubre, en [`tests/criterio-legal/RESULTADOS.md`](../tests/criterio-legal/RESULTADOS.md).

## Constanza · Agente de cumplimiento

De *constantia*: cada obligación con su evidencia, todos los días y no solo el de la auditoría.

| Puerta | Qué prueba | Comprob. | Tiempo | |
|---|---|---:|---:|---|
| `criterio-clo/evaluar.py` | Que Constanza levante cada señal sembrada en el cumplimiento, y ninguna en los controles | 7 | 166 ms | verde |

Su análisis propio, con qué material se usó y qué no cubre, en [`tests/criterio-compliance/RESULTADOS.md`](../tests/criterio-compliance/RESULTADOS.md).

## La familia · Lo que los tres comparten

Que la documentación y el código digan lo mismo, que el marketplace esté completo, que las copias compartidas no se hayan separado, y que el recorrido encuentre los documentos sin importar cómo estén organizados.

| Puerta | Qué prueba | Comprob. | Tiempo | |
|---|---|---:|---:|---|
| `sintetico/corpus.py` | El motor del material: la estructura de referencia y las cuatro disposiciones | 31 | 29 ms | verde |
| `sintetico/sectores.py` | Tres industrias con el mismo motor de hechos: finanzas, retail y minería | — | 12 ms | verde |
| `sintetico/formatos.py` | El material en Word, Excel y PDF, y que el plugin lo lea | — | 78 ms | verde |
| `sintetico/disposiciones.py` | Que el recorrido encuentre los mismos documentos sin importar cómo estén | 16 | 120 ms | verde |
| `sintetico/cobertura.py` | Que ninguna señal se quede sin disparar sin que esté declarado por qué | 3 | 294 ms | verde |
| `sintetico/resumen.py` | El resumen de las corridas diarias: precisión, cobertura y qué se movió | — | 31 ms | verde |
| `sintetico/regresion.py verificar` | La regresión del motor: cinco semanas de una organización, en cada cambio | 1 | 24661 ms | verde |
| `sintetico/evidencia.py verificar` | Que el registro de comandos no prometa una evidencia que no está | 1 | 40 ms | verde |
| `tests/ronda.py verificar` | Que cada defecto registrado diga su origen, su corrección y dónde se verificó | 1 | 94 ms | verde |
| `tests/banco.py verificar` | Que cada calificación del agente salga de sus conteos, con intervalo y origen | 1 | 43 ms | verde |
| `sintetico/funcionalidades.py` | Que cada comando declare qué produce y qué deja escrito | 1 | 30 ms | verde |
| `criterio-portfolio/terminos.py` | Los términos: una aceptación por versión, con comprobante en Markdown y PDF y su huella SHA-256 | 14 | 60 ms | verde |
| `scripts/registro.py verificar` | El registro de versiones: cada entrada con su huella y la de la anterior, sin huecos | 1 | 105 ms | verde |
| `tests/coherencia.py` | Que la documentación y el código digan lo mismo | 131 | 285 ms | verde |
| `tests/contratos.py` | Que cada comando y cada skill cumplan su contrato | 1 | 93 ms | verde |
| `scripts/validate_plugins.py` | Que el marketplace y cada plugin estén completos | — | 60 ms | verde |
| `scripts/sincronizar.py` | Que las copias compartidas no se hayan separado | — | 56 ms | verde |
| `scripts/manual.py` | Que el manual diga lo que dicen los README y los contratos | 1 | 48 ms | verde |
| `scripts/industrias.py` | Que las industrias del README salgan de su fuente y que «probada» sea cierto | — | 45 ms | verde |
| `scripts/carpetas.py` | Que la estructura de carpetas recomendada diga lo mismo en sus cinco copias | — | 31 ms | verde |
| `scripts/hoja.py` | Que la hoja de ruta salga de su fuente y diga «liberada» solo de lo registrado | — | 32 ms | verde |
| `scripts/analisis.py` | Que el análisis estadístico diga lo que dice la evidencia de las rondas | — | 43 ms | verde |
| `criterio-cfo/generar.py` | El material CFO: cuatro industrias y dos entidades de control, con su clave | — | 145 ms | verde |
| `criterio-clo/generar.py` | El material CLO: cuatro industrias y dos entidades de control, con su clave | — | 229 ms | verde |
| `scripts/familias.py` | Que el diseño de las familias CFO y CLO salga de sus fuentes y no se apoye en una por verificar | — | 59 ms | verde |
| `scripts/resultados.py` | Que la página de resultados no deje una puerta sin dueño | 16 | 129 ms | verde |

## Lo que esta corrida no cubre

Va aquí y no en un anexo. Una página de resultados que solo dice lo que pasó es publicidad; lo que la vuelve auditable es lo que dice que todavía no se sabe.

- **Estos corpus no corren la extracción; la corren las rondas.** Los tres corpus de esta página siembran el estado desde sus respuestas de referencia: lo que prueban es el cálculo. La cadena documento → modelo → ficha la ejercitan las rondas de punta a punta de `tests/evidencias/rondas/`, con los 67 comandos corridos por un agente de verdad y sus señales calificadas contra una clave que no ve. Lo que todavía no se ha ejecutado es la comparación campo por campo, `grade.py --fichas` y `grade.py --registros`.
- **Nada se ha corrido sobre la documentación real de una organización.** Todo el material es sintético y construido desde cero. Es la diferencia que protege a quien instale esto: **construido y verificado sobre corpus, no probado sobre documentación real.**
- **Lo que produce el modelo no lo mide un calificador determinista.** Convertir ocho entrevistas en temas con sus citas, redactar un acta o un informe es trabajo del modelo. Lo que se verifica aquí es la aritmética de la que salen sus cifras, y la estructura de lo que se le pide.

---

Reproducirlo: `python3 scripts/resultados.py`. El detalle de qué prueba cada corpus y qué no, en las tres páginas de evidencia bajo `tests/`.
