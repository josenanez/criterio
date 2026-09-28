# Resultado de las pruebas · Vera y Rostrum

**el agente de la PMO y el servidor que publica su informe** · plugin `criterio-portfolio`

Corrida del 2026-09-28, sobre el commit `9480ae0`, con cambios en el árbol todavía sin confirmar. **6 puertas · 215 comprobaciones · todas en verde.**

> Este archivo lo escribe `python3 scripts/resultados.py` desde una corrida real. No se edita a mano: la corrida siguiente lo reemplaza.

## Lo que se corrió

| Puerta | Qué prueba | Comprob. | Tiempo | |
|---|---|---:|---:|---|
| `criterio-portfolio/generar.py` | El portafolio sintético: seis proyectos, con un control negativo | — | 59 ms | verde |
| `criterio-portfolio/portafolio.py selftest` | La aritmética, la cadencia, la cola y el contraste entre las dos fichas | 79 | 24 ms | verde |
| `criterio-portfolio/texto.py` | Leer .docx, .xlsx, .pptx y .eml sin dependencias | 12 | 19 ms | verde |
| `criterio-portfolio/informe.py` | El informe: concordancia, formato de cifra, y que ninguna ruta salga en crudo | 15 | 17 ms | verde |
| `criterio-portfolio/servidor.py` | Rostrum: rutas, que no se salga de la carpeta, y que no escriba la ficha | 30 | 554 ms | verde |
| `criterio-portfolio/grade.py` | Vera contra respuestas escritas a mano, incluido el control negativo | 79 | 191 ms | verde |

Una puerta sin comprobaciones no es una puerta vacía: **genera el material sintético** o verifica una estructura completa, y falla entera si algo no está.

## Lo que esta corrida no cubre

Va aquí y no en un anexo. Un resultado de pruebas que solo dice lo que pasó es publicidad; lo que lo vuelve auditable es lo que dice que todavía no se sabe.

- **La extracción nunca se ha corrido.** El estado se siembra copiando `expected/fichas/`, así que la cadena documento → modelo → ficha no se ha ejercitado. `grade.py --fichas` existe para eso.
- **Nada se ha corrido sobre la documentación real de una organización.** Todo el material es sintético y construido desde cero.

## Los comandos, corridos por un agente de verdad

**3 de 17.** Un comando sin evidencia registrada no se probó: no se cuenta como aprobado y no se redondea. Los verificados como estructura —existen, declaran, y no invocan un skill que no esté— son otra cosa.

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

**Sin evidencia todavía, y por eso sin probar:** `budget-tracking`, `change-control`, `document-index`, `health-check`, `portfolio-server`, `portfolio-wake`, `product-view`, `project-charter`, `project-closure`, `project-history`, `raid-log`, `status-report`, `steering-pack`, `vendor-tracking`

**Corridas en que el agente no dijo que algo no estuviera dicho:** `portfolio-report`, `portfolio-scan`. Sobre material con huecos plantados, eso es señal de que rellenó.


## Qué material se usó, y qué prueba cada pieza

El detalle del corpus —qué planta cada proyecto o producto, por qué, y cuál es su control negativo— está en [`EVIDENCIA.md`](EVIDENCIA.md), que se escribe a mano y no se genera.

**El control negativo es la mitad del valor de estas pruebas.** Un agente que encuentra hallazgos donde no los hay es un generador de ruido, y eso no se detecta mirando solo los casos que sí fallan.

## Y lo que se verifica para toda la familia

| Puerta | Qué prueba | Comprob. | |
|---|---|---:|---|
| `sintetico/corpus.py` | El motor del material: la estructura de referencia y las cuatro disposiciones | 31 | verde |
| `sintetico/disposiciones.py` | Que el recorrido encuentre los mismos documentos sin importar cómo estén | 16 | verde |
| `sintetico/cobertura.py` | Que ninguna señal se quede sin disparar sin que esté declarado por qué | 3 | verde |
| `sintetico/resumen.py` | El resumen de las corridas diarias: precisión, cobertura y qué se movió | — | verde |
| `sintetico/evidencia.py verificar` | Que el registro de comandos no prometa una evidencia que no está | 1 | verde |
| `tests/coherencia.py` | Que la documentación y el código digan lo mismo | 69 | verde |
| `scripts/validate_plugins.py` | Que el marketplace y cada plugin estén completos | — | verde |
| `scripts/sincronizar.py` | Que las copias compartidas no se hayan separado | — | verde |
| `scripts/resultados.py` | Que la página de resultados no deje una puerta sin dueño | 16 | verde |

El conjunto de los tres agentes, en [`docs/pruebas.md`](../../docs/pruebas.md) — y con gráficas, para abrir en un navegador, en [`pruebas.html`](../../docs/pruebas.html). Todo corre con la librería estándar y sin instalar nada.
