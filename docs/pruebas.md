# Qué se probó, y qué no

Esta página sale de una corrida, no de un resumen escrito a mano. Cada cifra viene de ejecutar el mismo comando que corre `scripts/verificar.py` y contar las comprobaciones que ese comando imprimió. Con la librería estándar y sin instalar nada.

Corrida del 2026-10-22, sobre el commit `82d7199`, con cambios en el árbol todavía sin confirmar.

**49 de 49 puertas en verde · 1015 comprobaciones · 20 corpus, cada uno con su control negativo · 41.5 s la corrida entera.**

> La versión con gráficas, para abrir en un navegador, está en [`pruebas.html`](pruebas.html). Esta es la misma corrida, legible en GitHub.

## En conjunto

Comprobaciones por dueño. Los tamaños no son comparables entre sí y no pretenden serlo: lo que dice esta gráfica es dónde está puesta la verificación.

| Dueño | | Comprob. |
|---|---|---:|
| **Vera** | `██████████████████████` | 244 |
| **Samuel** | `██████████████` | 157 |
| **Alba** | `██████████` | 107 |
| **Rostrum** | `███████████` | 125 |
| **Clara** | `███` | 36 |
| **Tomás** | `█` | 7 |
| **Fidel** | `██` | 23 |
| **Constanza** | `█` | 7 |
| **La familia** | `████████████████████████████` | 309 |

## Vera · Agente PMO

Del latín *verus*: lo verdadero. Dice lo que los documentos dicen, no lo que se reporta.

| Puerta | Qué prueba | Comprob. | Tiempo | |
|---|---|---:|---:|---|
| `criterio-portfolio/generar.py` | El portafolio sintético: seis proyectos, con un control negativo | — | 100 ms | verde |
| `criterio-portfolio/portafolio.py selftest` | La aritmética, la cadencia, la cola y el contraste entre las dos fichas | 115 | 131 ms | verde |
| `criterio-portfolio/texto.py` | Leer .docx, .xlsx, .pptx y .eml sin dependencias | 23 | 62 ms | verde |
| `criterio-portfolio/informe.py` | El informe: concordancia, formato de cifra, y que ninguna ruta salga en crudo | 27 | 58 ms | verde |
| `criterio-portfolio/grade.py` | Vera contra respuestas escritas a mano, incluido el control negativo | 79 | 661 ms | verde |

Su análisis propio, con qué material se usó y qué no cubre, en [`tests/criterio-portfolio/RESULTADOS.md`](../tests/criterio-portfolio/RESULTADOS.md).

## Samuel · Agente de proyecto

«El que escuchó». Su función central es el compromiso dicho y no cumplido.

| Puerta | Qué prueba | Comprob. | Tiempo | |
|---|---|---:|---:|---|
| `criterio-project/generar.py` | Un proyecto visto desde adentro: dos proyectos, siete minutas | — | 85 ms | verde |
| `criterio-project/portafolio.py selftest` | La copia de la aritmética corre sola, sin tocar el otro plugin | 115 | 199 ms | verde |
| `criterio-project/texto.py` | La copia de la conversión, igual | 23 | 114 ms | verde |
| `criterio-project/grade.py` | Samuel contra respuestas escritas leyendo las minutas | 19 | 178 ms | verde |

Su análisis propio, con qué material se usó y qué no cubre, en [`tests/criterio-project/RESULTADOS.md`](../tests/criterio-project/RESULTADOS.md).

## Alba · Agente de producto

El amanecer: la luz que hay antes de que se vea nada. Trabaja antes de que exista el proyecto.

| Puerta | Qué prueba | Comprob. | Tiempo | |
|---|---|---:|---:|---|
| `criterio-product/generar.py` | Lo que hay antes del proyecto: dos productos, con un control negativo | — | 50 ms | verde |
| `criterio-product/producto.py selftest` | El registro de requerimiento: evidencia, supuestos, trazas y la cifra del negocio | 64 | 141 ms | verde |
| `criterio-product/grade.py` | Alba contra respuestas escritas leyendo la definición y las entrevistas | 43 | 330 ms | verde |

Su análisis propio, con qué material se usó y qué no cubre, en [`tests/criterio-product/RESULTADOS.md`](../tests/criterio-product/RESULTADOS.md).

## Rostrum · El portal

Una tribuna. Sostiene lo que todos los agentes ya escribieron, donde el equipo puede leerlo. No decide nada, y por eso no lleva nombre de persona.

| Puerta | Qué prueba | Comprob. | Tiempo | |
|---|---|---:|---:|---|
| `criterio-server/servidor.py` | Rostrum: rutas, que no se salga de lo que sirve, que no escriba la ficha, y las tres familias en un portal | 97 | 1275 ms | verde |
| `criterio-server/mapa.py` | El mapa: cada agente por la carpeta de su configuración, y nada que no se haya confirmado | 13 | 115 ms | verde |
| `criterio-server/robots.py` | Los robots: cada uno con el gesto de su oficio, el mismo en el navegador y en el GIF, y quieto si se pide | 15 | 46 ms | verde |

Su análisis propio, con qué material se usó y qué no cubre, en [`tests/criterio-server/RESULTADOS.md`](../tests/criterio-server/RESULTADOS.md).

## Clara · Agente contralor

De *clarus*: que los libros digan lo mismo que los soportes. Cierra el mes contra su evidencia.

| Puerta | Qué prueba | Comprob. | Tiempo | |
|---|---|---:|---:|---|
| `criterio-finance/finanzas.py selftest` | El motor de Clara y Tomás: números, fechas, lectores de la DIAN y del SRI, y una entidad mínima | 29 | 161 ms | verde |
| `criterio-cfo/evaluar.py` | Que Clara levante cada señal sembrada en el cierre, y ninguna en los controles | 7 | 261 ms | verde |

Su análisis propio, con qué material se usó y qué no cubre, en [`tests/criterio-finance/RESULTADOS.md`](../tests/criterio-finance/RESULTADOS.md).

## Tomás · Agente de FP&A

«El gemelo»: pone el presupuesto al lado de su gemelo, la ejecución.

| Puerta | Qué prueba | Comprob. | Tiempo | |
|---|---|---:|---:|---|
| `criterio-cfo/evaluar.py` | Que Tomás levante cada señal sembrada en el presupuesto, y ninguna en los controles | 7 | 267 ms | verde |

Su análisis propio, con qué material se usó y qué no cubre, en [`tests/criterio-budget/RESULTADOS.md`](../tests/criterio-budget/RESULTADOS.md).

## Fidel · Agente de contratos

De *fides*: la palabra dada. Pone lo firmado al lado de lo que está pasando.

| Puerta | Qué prueba | Comprob. | Tiempo | |
|---|---|---:|---:|---|
| `criterio-legal/legal.py selftest` | El motor de Fidel y Constanza: fechas, prórrogas, plazos y una entidad mínima con todo mal | 16 | 89 ms | verde |
| `criterio-clo/evaluar.py` | Que Fidel levante cada señal sembrada en los contratos, y ninguna en los controles | 7 | 255 ms | verde |

Su análisis propio, con qué material se usó y qué no cubre, en [`tests/criterio-legal/RESULTADOS.md`](../tests/criterio-legal/RESULTADOS.md).

## Constanza · Agente de cumplimiento

De *constantia*: cada obligación con su evidencia, todos los días y no solo el de la auditoría.

| Puerta | Qué prueba | Comprob. | Tiempo | |
|---|---|---:|---:|---|
| `criterio-clo/evaluar.py` | Que Constanza levante cada señal sembrada en el cumplimiento, y ninguna en los controles | 7 | 206 ms | verde |

Su análisis propio, con qué material se usó y qué no cubre, en [`tests/criterio-compliance/RESULTADOS.md`](../tests/criterio-compliance/RESULTADOS.md).

## La familia · Lo que los tres comparten

Que la documentación y el código digan lo mismo, que el marketplace esté completo, que las copias compartidas no se hayan separado, y que el recorrido encuentre los documentos sin importar cómo estén organizados.

| Puerta | Qué prueba | Comprob. | Tiempo | |
|---|---|---:|---:|---|
| `sintetico/corpus.py` | El motor del material: la estructura de referencia y las cuatro disposiciones | 31 | 39 ms | verde |
| `sintetico/sectores.py` | Tres industrias con el mismo motor de hechos: finanzas, retail y minería | — | 17 ms | verde |
| `sintetico/formatos.py` | El material en Word, Excel y PDF, y que el plugin lo lea | — | 98 ms | verde |
| `sintetico/disposiciones.py` | Que el recorrido encuentre los mismos documentos sin importar cómo estén | 16 | 141 ms | verde |
| `sintetico/cobertura.py` | Que ninguna señal se quede sin disparar sin que esté declarado por qué | 3 | 400 ms | verde |
| `sintetico/resumen.py` | El resumen de las corridas diarias: precisión, cobertura y qué se movió | — | 35 ms | verde |
| `sintetico/regresion.py verificar` | La regresión del motor: cinco semanas de una organización, en cada cambio | 1 | 33766 ms | verde |
| `sintetico/evidencia.py verificar` | Que el registro de comandos no prometa una evidencia que no está | 1 | 36 ms | verde |
| `tests/ronda.py verificar` | Que cada defecto registrado diga su origen, su corrección y dónde se verificó | 1 | 86 ms | verde |
| `tests/banco.py verificar` | Que cada calificación del agente salga de sus conteos, con intervalo y origen | 1 | 47 ms | verde |
| `sintetico/funcionalidades.py` | Que cada comando declare qué produce y qué deja escrito | 1 | 35 ms | verde |
| `criterio-portfolio/rastro.py` | Que el arnés deje la página de cada corrida, con lo que el agente mostró y sus cifras | 20 | 124 ms | verde |
| `criterio-portfolio/terminos.py` | Los términos: una aceptación por versión, con comprobante en Markdown y PDF y su huella SHA-256 | 14 | 103 ms | verde |
| `criterio-portfolio/raiz.py` | La carpeta raíz: encontrarla por su estructura y su marca, y marcarla solo con permiso | 11 | 109 ms | verde |
| `scripts/registro.py verificar` | El registro de versiones: cada entrada con su huella y la de la anterior, sin huecos | 1 | 124 ms | verde |
| `tests/coherencia.py` | Que la documentación y el código digan lo mismo | 190 | 388 ms | verde |
| `tests/contratos.py` | Que cada comando y cada skill cumplan su contrato | 1 | 79 ms | verde |
| `scripts/validate_plugins.py` | Que el marketplace y cada plugin estén completos | — | 59 ms | verde |
| `scripts/sincronizar.py` | Que las copias compartidas no se hayan separado | — | 62 ms | verde |
| `scripts/manual.py` | Que el manual diga lo que dicen los README y los contratos | 1 | 44 ms | verde |
| `scripts/industrias.py` | Que las industrias del README salgan de su fuente y que «probada» sea cierto | — | 38 ms | verde |
| `scripts/carpetas.py` | Que la estructura de carpetas recomendada diga lo mismo en sus cinco copias | — | 37 ms | verde |
| `scripts/hoja.py` | Que la hoja de ruta salga de su fuente y diga «liberada» solo de lo registrado | — | 47 ms | verde |
| `scripts/analisis.py` | Que el análisis estadístico diga lo que dice la evidencia de las rondas | — | 51 ms | verde |
| `criterio-cfo/generar.py` | El material CFO: cuatro industrias y dos entidades de control, con su clave | — | 225 ms | verde |
| `criterio-clo/generar.py` | El material CLO: cuatro industrias y dos entidades de control, con su clave | — | 278 ms | verde |
| `scripts/familias.py` | Que el diseño de las familias CFO y CLO salga de sus fuentes y no se apoye en una por verificar | — | 130 ms | verde |
| `scripts/resultados.py` | Que la página de resultados no deje una puerta sin dueño | 16 | 124 ms | verde |

## Lo que esta corrida no cubre

Va aquí y no en un anexo. Una página de resultados que solo dice lo que pasó es publicidad; lo que la vuelve auditable es lo que dice que todavía no se sabe.

- **Estos corpus no corren la extracción; la corren las rondas.** Los tres corpus de esta página siembran el estado desde sus respuestas de referencia: lo que prueban es el cálculo. La cadena documento → modelo → ficha la ejercitan las rondas de punta a punta de `tests/evidencias/rondas/`, con los 68 comandos corridos por un agente de verdad y sus señales calificadas contra una clave que no ve. Lo que todavía no se ha ejecutado es la comparación campo por campo, `grade.py --fichas` y `grade.py --registros`.
- **Nada se ha corrido sobre la documentación real de una organización.** Todo el material es sintético y construido desde cero. Es la diferencia que protege a quien instale esto: **construido y verificado sobre corpus, no probado sobre documentación real.**
- **Lo que produce el modelo no lo mide un calificador determinista.** Convertir ocho entrevistas en temas con sus citas, redactar un acta o un informe es trabajo del modelo. Lo que se verifica aquí es la aritmética de la que salen sus cifras, y la estructura de lo que se le pide.

---

Reproducirlo: `python3 scripts/resultados.py`. El detalle de qué prueba cada corpus y qué no, en las tres páginas de evidencia bajo `tests/`.
