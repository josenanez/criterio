# Resultado de las pruebas · Vera

**el agente de la PMO** · plugin `criterio-portfolio`

Corrida del 2026-10-22, sobre el commit `c8a3572`, con cambios en el árbol todavía sin confirmar. **5 puertas · 244 comprobaciones · todas en verde.**

> Este archivo lo escribe `python3 scripts/resultados.py` desde una corrida real. No se edita a mano: la corrida siguiente lo reemplaza.

## Lo que se corrió

| Puerta | Qué prueba | Comprob. | Tiempo | |
|---|---|---:|---:|---|
| `criterio-portfolio/generar.py` | El portafolio sintético: seis proyectos, con un control negativo | — | 78 ms | verde |
| `criterio-portfolio/portafolio.py selftest` | La aritmética, la cadencia, la cola y el contraste entre las dos fichas | 115 | 131 ms | verde |
| `criterio-portfolio/texto.py` | Leer .docx, .xlsx, .pptx y .eml sin dependencias | 23 | 64 ms | verde |
| `criterio-portfolio/informe.py` | El informe: concordancia, formato de cifra, y que ninguna ruta salga en crudo | 27 | 58 ms | verde |
| `criterio-portfolio/grade.py` | Vera contra respuestas escritas a mano, incluido el control negativo | 79 | 430 ms | verde |

Una puerta sin comprobaciones no es una puerta vacía: **genera el material sintético** o verifica una estructura completa, y falla entera si algo no está.

## Lo que esta corrida no cubre

Va aquí y no en un anexo. Un resultado de pruebas que solo dice lo que pasó es publicidad; lo que lo vuelve auditable es lo que dice que todavía no se sabe.

- **Este corpus no corre la extracción; la corren las rondas.** El estado se siembra copiando `expected/fichas/`. La cadena documento → modelo → ficha la ejercitan las rondas de punta a punta, donde las señales de Vera se califican contra una clave que no ve. La comparación campo por campo, `grade.py --fichas`, todavía no se ha ejecutado.
- **Nada se ha corrido sobre la documentación real de una organización.** Todo el material es sintético y construido desde cero.

## Los comandos, corridos por un agente de verdad

**16 de 16** corrieron en la ronda 10 con el plugin instalado desde cero, en 4 industrias; **16** cumplieron su contrato en todas. El detalle de cada corrida, con lo que mostró el comando, está en [`tests/evidencias/rondas/ronda-10/`](../evidencias/rondas/ronda-10/).

| Comando | Terminó | Cumplió su contrato | Tiempo |
|---|---|---|---:|
| `/criterio-portfolio:budget-tracking` | 4 de 4 | 4 de 4 | 52–57 s |
| `/criterio-portfolio:change-control` | 4 de 4 | 4 de 4 | 51–70 s |
| `/criterio-portfolio:document-index` | 4 de 4 | 4 de 4 | 29–36 s |
| `/criterio-portfolio:health-check` | 4 de 4 | 4 de 4 | 114–231 s |
| `/criterio-portfolio:portfolio-report` | 4 de 4 | 4 de 4 | 48–61 s |
| `/criterio-portfolio:portfolio-scan` | 4 de 4 | 4 de 4 | 168–289 s |
| `/criterio-portfolio:portfolio-setup` | 4 de 4 | 4 de 4 | 90–173 s |
| `/criterio-portfolio:portfolio-wake` | 4 de 4 | 4 de 4 | 38–49 s |
| `/criterio-portfolio:product-view` | 4 de 4 | 4 de 4 | 38–49 s |
| `/criterio-portfolio:project-charter` | 4 de 4 | 4 de 4 | 50–55 s |
| `/criterio-portfolio:project-closure` | 4 de 4 | 4 de 4 | 64–80 s |
| `/criterio-portfolio:project-history` | 4 de 4 | 4 de 4 | 63–116 s |
| `/criterio-portfolio:raid-log` | 4 de 4 | 4 de 4 | 110–186 s |
| `/criterio-portfolio:status-report` | 4 de 4 | 4 de 4 | 50–60 s |
| `/criterio-portfolio:steering-pack` | 4 de 4 | 4 de 4 | 115–139 s |
| `/criterio-portfolio:vendor-tracking` | 4 de 4 | 4 de 4 | 58–62 s |

### Antes de las rondas

| Comando | Días | Documentos | Tiempo | Hallazgos | De dónde sale |
|---|---|---:|---:|---:|---|
| [`/criterio-portfolio:portfolio-report`](../evidencias/dia-1/portfolio-report.md) | 1, 2 | 146 | — | 189 | medida por la corrida (1/2) |
| [`/criterio-portfolio:portfolio-scan`](../evidencias/dia-1/portfolio-scan.md) | 1, 2 | 186 | 2–2 s | 194 | medida por la corrida (1/2) |
| [`/criterio-portfolio:portfolio-setup`](../evidencias/dia-1/portfolio-setup.md) | 1 | — | — | 0 | anotada a mano |

**Las cifras que salen de la corrida las midió el agente**, no las transcribió nadie: `portafolio.py corrida` cuenta los proyectos, los hallazgos por señal, los documentos releídos y el tiempo. Una cifra tecleada mide la transcripción de quien conduce la prueba, y eso la vicia.

| Comando | Qué dejó ver |
|---|---|
| `portfolio-report` | 158 de 158 alertas, y 7 de 8 cifras exactas. El aprobado salió 1000x. De aquí salieron la regla de cifras y la señal progress_vs_plan. · Cifras no cosechadas: esta corrida es anterior a que la corrida midiera lo suyo. |
| `portfolio-scan` | Encontró por su cuenta la incompatibilidad cronograma/avance en 8 proyectos. De ahí salió la señal progress_vs_plan. · Cifras no cosechadas: esta corrida es anterior a que la corrida midiera lo suyo. |
| `portfolio-setup` | El paso destapó que los 37 comandos estaban documentados sin el prefijo del plugin: 226 referencias que no resolvían. · Cifras no cosechadas: esta corrida es anterior a que la corrida midiera lo suyo. |

**Corridas en que el agente no dijo que algo no estuviera dicho:** `portfolio-report`, `portfolio-scan`. Sobre material con huecos plantados, eso es señal de que rellenó.


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
