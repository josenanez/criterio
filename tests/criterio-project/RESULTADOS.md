# Resultado de las pruebas · Samuel

**el agente del gerente de proyecto** · plugin `criterio-project`

Corrida del 2026-10-22, sobre el commit `bcd931b`, con cambios en el árbol todavía sin confirmar. **4 puertas · 157 comprobaciones · todas en verde.**

> Este archivo lo escribe `python3 scripts/resultados.py` desde una corrida real. No se edita a mano: la corrida siguiente lo reemplaza.

## Lo que se corrió

| Puerta | Qué prueba | Comprob. | Tiempo | |
|---|---|---:|---:|---|
| `criterio-project/generar.py` | Un proyecto visto desde adentro: dos proyectos, siete minutas | — | 68 ms | verde |
| `criterio-project/portafolio.py selftest` | La copia de la aritmética corre sola, sin tocar el otro plugin | 115 | 159 ms | verde |
| `criterio-project/texto.py` | La copia de la conversión, igual | 23 | 80 ms | verde |
| `criterio-project/grade.py` | Samuel contra respuestas escritas leyendo las minutas | 19 | 117 ms | verde |

Una puerta sin comprobaciones no es una puerta vacía: **genera el material sintético** o verifica una estructura completa, y falla entera si algo no está.

## Lo que esta corrida no cubre

Va aquí y no en un anexo. Un resultado de pruebas que solo dice lo que pasó es publicidad; lo que lo vuelve auditable es lo que dice que todavía no se sabe.

- **Este corpus no corre la extracción; la corren las rondas.** El corpus siembra las fichas. En las rondas de punta a punta Samuel lee seis comités y las notas del día, y se califican sus compromisos y su fecha de cierre. La comparación campo por campo, `grade.py --fichas`, todavía no se ha ejecutado.
- **La agenda, el acta y el informe no se califican con esto.** Lo que producen es redacción sobre la minuta, y un calificador determinista no la mide. Lo que sí se verifica es la aritmética de la que salen sus cifras.
- **La ficha publicada y su contraste corren de punta a punta en cada ronda.** Samuel publica con `/criterio-project:pm-publish` y Vera la lee en su barrido; desde la ronda 6 la clave calcula el contraste esperado desde la ficha publicada.

## Los comandos, corridos por un agente de verdad

**9 de 9** corrieron en la ronda 10 con el plugin instalado desde cero, en 4 industrias; **9** cumplieron su contrato en todas. El detalle de cada corrida, con lo que mostró el comando, está en [`tests/evidencias/rondas/ronda-10/`](../evidencias/rondas/ronda-10/).

| Comando | Terminó | Cumplió su contrato | Tiempo |
|---|---|---|---:|
| `/criterio-project:pm-agenda` | 4 de 4 | 4 de 4 | 67–112 s |
| `/criterio-project:pm-commitments` | 4 de 4 | 4 de 4 | 47–59 s |
| `/criterio-project:pm-escalate` | 4 de 4 | 4 de 4 | 58–73 s |
| `/criterio-project:pm-minutes` | 4 de 4 | 4 de 4 | 56–68 s |
| `/criterio-project:pm-plan` | 4 de 4 | 4 de 4 | 60–86 s |
| `/criterio-project:pm-publish` | 4 de 4 | 4 de 4 | 46–58 s |
| `/criterio-project:pm-report` | 4 de 4 | 4 de 4 | 46–111 s |
| `/criterio-project:pm-setup` | 4 de 4 | 4 de 4 | 144–174 s |
| `/criterio-project:pm-wake` | 4 de 4 | 4 de 4 | 34–65 s |


## Qué material se usó, y qué prueba cada pieza

El detalle del corpus —qué planta cada proyecto o producto, por qué, y cuál es su control negativo— está en [`EVIDENCIA.md`](EVIDENCIA.md), que se escribe a mano y no se genera.

**El control negativo es la mitad del valor de estas pruebas.** Un agente que encuentra hallazgos donde no los hay es un generador de ruido, y eso no se detecta mirando solo los casos que sí fallan.

## Y lo que se verifica para toda la familia

| Puerta | Qué prueba | Comprob. | |
|---|---|---:|---|
| `sintetico/corpus.py` | El motor del material: la estructura de referencia y las cuatro disposiciones | 31 | verde |
| `sintetico/sectores.py` | Tres industrias con el mismo motor de hechos: finanzas, retail y minería | — | verde |
| `sintetico/formatos.py` | El material en Word, Excel y PDF, y que el plugin lo lea | — | verde |
| `sintetico/disposiciones.py` | Que el recorrido encuentre los mismos documentos sin importar cómo estén | 16 | verde |
| `sintetico/cobertura.py` | Que ninguna señal se quede sin disparar sin que esté declarado por qué | 3 | verde |
| `sintetico/resumen.py` | El resumen de las corridas diarias: precisión, cobertura y qué se movió | — | verde |
| `sintetico/regresion.py verificar` | La regresión del motor: cinco semanas de una organización, en cada cambio | 1 | verde |
| `sintetico/evidencia.py verificar` | Que el registro de comandos no prometa una evidencia que no está | 1 | verde |
| `tests/ronda.py verificar` | Que cada defecto registrado diga su origen, su corrección y dónde se verificó | 1 | verde |
| `tests/banco.py verificar` | Que cada calificación del agente salga de sus conteos, con intervalo y origen | 1 | verde |
| `sintetico/funcionalidades.py` | Que cada comando declare qué produce y qué deja escrito | 1 | verde |
| `criterio-portfolio/rastro.py` | Que el arnés deje la página de cada corrida, con lo que el agente mostró y sus cifras | 20 | verde |
| `criterio-portfolio/terminos.py` | Los términos: una aceptación por versión, con comprobante en Markdown y PDF y su huella SHA-256 | 14 | verde |
| `criterio-portfolio/raiz.py` | La carpeta raíz: encontrarla por su estructura y su marca, y marcarla solo con permiso | 11 | verde |
| `scripts/registro.py verificar` | El registro de versiones: cada entrada con su huella y la de la anterior, sin huecos | 1 | verde |
| `tests/coherencia.py` | Que la documentación y el código digan lo mismo | 190 | verde |
| `tests/contratos.py` | Que cada comando y cada skill cumplan su contrato | 1 | verde |
| `scripts/validate_plugins.py` | Que el marketplace y cada plugin estén completos | — | verde |
| `scripts/sincronizar.py` | Que las copias compartidas no se hayan separado | — | verde |
| `scripts/manual.py` | Que el manual diga lo que dicen los README y los contratos | 1 | verde |
| `scripts/industrias.py` | Que las industrias del README salgan de su fuente y que «probada» sea cierto | — | verde |
| `scripts/carpetas.py` | Que la estructura de carpetas recomendada diga lo mismo en sus cinco copias | — | verde |
| `scripts/hoja.py` | Que la hoja de ruta salga de su fuente y diga «liberada» solo de lo registrado | — | verde |
| `scripts/analisis.py` | Que el análisis estadístico diga lo que dice la evidencia de las rondas | — | verde |
| `criterio-cfo/generar.py` | El material CFO: cuatro industrias y dos entidades de control, con su clave | — | verde |
| `criterio-clo/generar.py` | El material CLO: cuatro industrias y dos entidades de control, con su clave | — | verde |
| `scripts/familias.py` | Que el diseño de las familias CFO y CLO salga de sus fuentes y no se apoye en una por verificar | — | verde |
| `scripts/resultados.py` | Que la página de resultados no deje una puerta sin dueño | 16 | verde |

El conjunto de los tres agentes, en [`docs/pruebas.md`](../../docs/pruebas.md) — y con gráficas, para abrir en un navegador, en [`pruebas.html`](../../docs/pruebas.html). Todo corre con la librería estándar y sin instalar nada.
