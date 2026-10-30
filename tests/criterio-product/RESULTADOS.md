# Resultado de las pruebas · Alba

**el agente del gerente de producto** · plugin `criterio-product`

Corrida del 2026-10-29, sobre el commit `7b708369`, con cambios en el árbol todavía sin confirmar. **3 puertas · 107 comprobaciones · todas en verde.**

> Este archivo lo escribe `python3 scripts/resultados.py` desde una corrida real. No se edita a mano: la corrida siguiente lo reemplaza.

## Lo que se corrió

| Puerta | Qué prueba | Comprob. | Tiempo | |
|---|---|---:|---:|---|
| `criterio-product/generar.py` | Lo que hay antes del proyecto: dos productos, con un control negativo | — | 66 ms | verde |
| `criterio-product/producto.py selftest` | El registro de requerimiento: evidencia, supuestos, trazas y la cifra del negocio | 64 | 118 ms | verde |
| `criterio-product/grade.py` | Alba contra respuestas escritas leyendo la definición y las entrevistas | 43 | 390 ms | verde |

Una puerta sin comprobaciones no es una puerta vacía: **genera el material sintético** o verifica una estructura completa, y falla entera si algo no está.

## Lo que esta corrida no cubre

Va aquí y no en un anexo. Un resultado de pruebas que solo dice lo que pasó es publicidad; lo que lo vuelve auditable es lo que dice que todavía no se sabe.

- **Este corpus no corre la extracción; la corren las rondas.** El corpus siembra los registros. En las rondas de punta a punta Alba arma su ficha y su registro desde lo escrito, y se califican las alertas sobre su producto. La comparación campo por campo, `grade.py --registros`, todavía no se ha ejecutado.
- **La síntesis de descubrimiento no se puede calificar con esto.** Convertir ocho entrevistas en temas con sus citas es trabajo del modelo. Las entrevistas del corpus llevan el conteo explícito —«6 de 8»— para que el día que se califique haya contra qué.
- **El barrido normativo no se prueba en ninguna parte.** Su salida depende de conocimiento externo al repositorio, y su regla dura —*no dice si cumple*— no se puede verificar con una aserción.

## Los comandos, corridos por un agente de verdad

**11 de 11** corrieron en la ronda 12 con el plugin instalado desde cero, en 2 industrias; **11** cumplieron su contrato en todas. El detalle de cada corrida, con lo que mostró el comando, está en [`tests/evidencias/rondas/ronda-12/`](../evidencias/rondas/ronda-12/).

| Comando | Terminó | Cumplió su contrato | Tiempo |
|---|---|---|---:|
| `/criterio-product:product-business-case` | 2 de 2 | 2 de 2 | 59–62 s |
| `/criterio-product:product-charter` | 2 de 2 | 2 de 2 | 52–68 s |
| `/criterio-product:product-definition` | 2 de 2 | 2 de 2 | 56–58 s |
| `/criterio-product:product-discovery` | 2 de 2 | 2 de 2 | 30–30 s |
| `/criterio-product:product-overlap` | 2 de 2 | 2 de 2 | 15–16 s |
| `/criterio-product:product-publish` | 2 de 2 | 2 de 2 | 27–37 s |
| `/criterio-product:product-requirements` | 2 de 2 | 2 de 2 | 43–55 s |
| `/criterio-product:product-setup` | 2 de 2 | 2 de 2 | 109–123 s |
| `/criterio-product:product-spec` | 2 de 2 | 2 de 2 | 60–72 s |
| `/criterio-product:product-trace` | 2 de 2 | 2 de 2 | 42–44 s |
| `/criterio-product:product-wake` | 2 de 2 | 2 de 2 | 47–56 s |


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
| `scripts/trafico.py` | La cuenta de instalaciones: clonadores únicos de la ventana menos los pushes a main de esa misma ventana | 4 | verde |
| `tests/coherencia.py` | Que la documentación y el código digan lo mismo | 264 | verde |
| `tests/contratos.py` | Que cada comando y cada skill cumplan su contrato | 1 | verde |
| `scripts/validate_plugins.py` | Que el marketplace y cada plugin estén completos | — | verde |
| `scripts/sincronizar.py` | Que las copias compartidas no se hayan separado | — | verde |
| `scripts/manual.py` | Que el manual diga lo que dicen los README y los contratos | 1 | verde |
| `scripts/industrias.py` | Que las industrias del README salgan de su fuente y que «probada» sea cierto | — | verde |
| `scripts/carpetas.py` | Que la estructura de carpetas recomendada diga lo mismo en sus cinco copias | — | verde |
| `scripts/calidad.py` | Que laboratorio o estable salga de la evidencia con el piso del 95 %, y que cada versión siga la regla de diez por entero | 18 | verde |
| `scripts/hoja.py` | Que la hoja de ruta salga de su fuente y diga «liberada» solo de lo registrado | — | verde |
| `scripts/analisis.py` | Que el análisis estadístico diga lo que dice la evidencia de las rondas | — | verde |
| `scripts/analisis_familias.py` | Que el análisis estadístico de cada familia con rondas diga lo que dice la evidencia de sus rondas | — | verde |
| `scripts/compatibilidad.py` | Que cada script corra con el Python que trae el equipo de quien instala el plugin, desde el 3.9 | — | verde |
| `scripts/soporte.py` | Que cada rol tenga el marco que lo define, verificado, y cada familia sus cifras de costo verificadas | — | verde |
| `criterio-cfo/generar.py` | El material CFO: cuatro industrias y dos entidades de control, con su clave | — | verde |
| `criterio-clo/generar.py` | El material CLO: cuatro industrias y dos entidades de control, con su clave | — | verde |
| `criterio-cso/generar.py` | El material CSO: dos industrias y un control por país en Colombia y México, cada uno con la exportación de su CRM y su clave | — | verde |
| `scripts/familias.py` | Que el diseño de cada familia salga de sus fuentes y no se apoye en una por verificar | — | verde |
| `scripts/resultados.py` | Que la página de resultados no deje una puerta sin dueño | 16 | verde |

El conjunto de los tres agentes, en [`docs/pruebas.md`](../../docs/pruebas.md) — y con gráficas, para abrir en un navegador, en [`pruebas.html`](../../docs/pruebas.html). Todo corre con la librería estándar y sin instalar nada.
