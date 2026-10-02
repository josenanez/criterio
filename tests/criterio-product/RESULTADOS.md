# Resultado de las pruebas · Alba

**el agente del gerente de producto** · plugin `criterio-product`

Corrida del 2026-10-02, sobre el commit `0f619b1`, con cambios en el árbol todavía sin confirmar (sin regenerar el material sintético). **2 puertas · 105 comprobaciones · todas en verde.**

> Este archivo lo escribe `python3 scripts/resultados.py` desde una corrida real. No se edita a mano: la corrida siguiente lo reemplaza.

## Lo que se corrió

| Puerta | Qué prueba | Comprob. | Tiempo | |
|---|---|---:|---:|---|
| `criterio-product/producto.py selftest` | El registro de requerimiento: evidencia, supuestos, trazas y la cifra del negocio | 62 | 29 ms | verde |
| `criterio-product/grade.py` | Alba contra respuestas escritas leyendo la definición y las entrevistas | 43 | 127 ms | verde |

Una puerta sin comprobaciones no es una puerta vacía: **genera el material sintético** o verifica una estructura completa, y falla entera si algo no está.

## Lo que esta corrida no cubre

Va aquí y no en un anexo. Un resultado de pruebas que solo dice lo que pasó es publicidad; lo que lo vuelve auditable es lo que dice que todavía no se sabe.

- **La extracción nunca se ha corrido.** El corpus siembra los registros, así que la cadena documento → modelo → registro no se ha ejercitado. `grade.py --registros` existe para eso.
- **La síntesis de descubrimiento no se puede calificar con esto.** Convertir ocho entrevistas en temas con sus citas es trabajo del modelo. Las entrevistas del corpus llevan el conteo explícito —«6 de 8»— para que el día que se califique haya contra qué.
- **El barrido normativo no se prueba en ninguna parte.** Su salida depende de conocimiento externo al repositorio, y su regla dura —*no dice si cumple*— no se puede verificar con una aserción.

## Los comandos, corridos por un agente de verdad

**0 de 11.** Un comando sin evidencia registrada no se probó: no se cuenta como aprobado y no se redondea. Los verificados como estructura —existen, declaran, y no invocan un skill que no esté— son otra cosa.

Ninguno todavía. La evidencia se registra con `tests/sintetico/evidencia.py`.


## Qué material se usó, y qué prueba cada pieza

El detalle del corpus —qué planta cada proyecto o producto, por qué, y cuál es su control negativo— está en [`EVIDENCIA.md`](EVIDENCIA.md), que se escribe a mano y no se genera.

**El control negativo es la mitad del valor de estas pruebas.** Un agente que encuentra hallazgos donde no los hay es un generador de ruido, y eso no se detecta mirando solo los casos que sí fallan.

## Y lo que se verifica para toda la familia

| Puerta | Qué prueba | Comprob. | |
|---|---|---:|---|
| `tests/coherencia.py` | Que la documentación y el código digan lo mismo | 73 | verde |
| `tests/contratos.py` | Que cada comando y cada skill cumplan su contrato | 1 | verde |
| `scripts/validate_plugins.py` | Que el marketplace y cada plugin estén completos | — | verde |
| `scripts/sincronizar.py` | Que las copias compartidas no se hayan separado | — | verde |
| `scripts/resultados.py` | Que la página de resultados no deje una puerta sin dueño | 16 | verde |

El conjunto de los tres agentes, en [`docs/pruebas.md`](../../docs/pruebas.md) — y con gráficas, para abrir en un navegador, en [`pruebas.html`](../../docs/pruebas.html). Todo corre con la librería estándar y sin instalar nada.
