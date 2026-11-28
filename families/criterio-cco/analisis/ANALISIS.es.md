# Análisis estadístico de las pruebas · familia CCO

Generado por `scripts/analisis_familias.py` desde `tests/evidencias/familias/cco/` · ronda más reciente: 3 · [English](ANALISIS.md)

No se edita a mano: cada cifra sale de la evidencia y el análisis se regenera con cada ronda.

## En una mirada

La ronda más reciente, la 3, parcial, sobre 1 de las 16 entidades del material: 20 de 20 señales sembradas encontradas (margen del 95 %: 83,8–100 %) y 0 de más; 5 de 5 datos extraídos bien (100 %, margen del 95 %: 56,5–100 %); y 0 de 0 entidades de control sin ninguna señal.

Sumando las rondas 1–3, 248 de 256 señales encontradas, 3 de más y 105 de 105 datos bien. Las rondas repiten el mismo material: no son muestras independientes, y el margen se calcula sobre los casos de cada una.

## Qué se probó y cómo

En cada entidad corren el setup y el procesamiento de Augusto y Valeria —los comandos que procesan los documentos y escriben las fichas—, con un tope de tokens fijado antes de empezar, sobre un material que trae su clave aparte, que nadie ve. Los demás comandos calculan sobre esas fichas con el motor, que se prueba con cada cambio del repositorio. Las señales se comparan por su nombre y su clave; la extracción, campo por campo, contra lo que traen los documentos escritos. Las entidades de control no tienen ningún defecto sembrado: cualquier señal en ellas es una falla.

Cobertura: de las señales sembradas, cuántas encontró. Precisión: de las que levantó, cuántas eran correctas. Margen del 95 %: intervalo de confianza de Wilson sobre los casos.

|   |   |
|---|---|
| Rondas | 3; la más reciente, la 3, es parcial |
| Material | Manufactura · México |
| Entidades de control |  |
| Corridas de una entidad | 21 |
| Señales sembradas | 256 |
| Datos calificados | 105 |

## Resultados acumulados · rondas 1–3

| Métrica | Casos | Resultado | Margen del 95 % |
|---|---|---|---|
| Señales · cobertura | 248 de 256 | 96,9 % | 93,9–98,5 % |
| Señales · precisión | 248 de 251 | 98,8 % | 96,5–99,6 % |
| Extracción · datos correctos | 105 de 105 | 100 % | 96,4–100 % |
| Control · sin ninguna señal | 6 de 8 | 75 % | 40,9–92,9 % |

## Evolución por ronda

![Evolución por ronda](evolucion-es.svg)

Una ronda que no corre todas las entidades es parcial: la primera, pequeña, antes de la completa, o una de verificación, que repite las corridas que un defecto corregido dejó pendientes.

| Ronda | Entidades | Señales · cobertura | Señales · precisión | Extracción | Control sin señales | Tokens | Defectos |
|---|---|---|---|---|---|---|---|
| 1 | 10 | 93,3 % | 98,2 % | 100 % | 3 de 4 | 30,9 M | 3 |
| 2 | 10 | 100 % | 99,2 % | 100 % | 3 de 4 | 30,4 M | 1 |
| 3 | 1 | 100 % | 100 % | 100 % | 0 de 0 | 7 M | 0 |

## La ronda más reciente · ronda 3

| Métrica | Casos | Resultado | Margen del 95 % |
|---|---|---|---|
| Señales · cobertura | 20 de 20 | 100 % | 83,8–100 % |
| Señales · precisión | 20 de 20 | 100 % | 83,8–100 % |
| Extracción · datos correctos | 5 de 5 | 100 % | 56,5–100 % |
| Control · sin ninguna señal | 0 de 0 | — | — |

## Por industria y país · ronda 3

| Material | Agentes | Señales | De más | Extracción | Tokens |
|---|---|---|---|---|---|
| Manufactura · México | Augusto, Valeria | 20 de 20 | 0 | 5 de 5 | 7 M |

## Lo que falló, uno por uno · rondas 1–3

11 fallas en 21 corridas, cada una con el defecto que la explica: su origen dice si falló el agente o la prueba. Las cifras son las de la calificación original: 0 de esas fallas vinieron de la prueba —el arnés o la clave—, no del agente, y con la prueba corregida se califican como correctas.

| Ronda | Material | Qué | Dónde | Defecto | Origen |
|---|---|---|---|---|---|
| 1 | Control · México | Señal de más | ["commission_differs_from_plan", "comision:2026-10:isabel_mendez"] | — | — |
| 1 | Control · México | Señal de más | ["commission_differs_from_plan", "comision:2026-10:oscar_delgado"] | — | — |
| 1 | Servicios · México | Señal no encontrada | ["close_date_slipped", "corre:OPP-1504"] | — | — |
| 1 | Servicios · México | Señal no encontrada | ["close_date_slipped", "corre:OPP-1526"] | — | — |
| 1 | Servicios · México | Señal no encontrada | ["close_date_slipped", "corre:OPP-1527"] | — | — |
| 1 | Servicios · México | Señal no encontrada | ["close_date_slipped", "corre:OPP-1528"] | — | — |
| 1 | Tecnología · Colombia | Señal no encontrada | ["close_date_slipped", "corre:OPP-1204"] | — | — |
| 1 | Tecnología · Colombia | Señal no encontrada | ["close_date_slipped", "corre:OPP-1226"] | — | — |
| 1 | Tecnología · Colombia | Señal no encontrada | ["close_date_slipped", "corre:OPP-1227"] | — | — |
| 1 | Tecnología · Colombia | Señal no encontrada | ["close_date_slipped", "corre:OPP-1228"] | — | — |
| 2 | Control · Perú | Señal de más | ["stalled_opportunity", "detenida:OPP-2205"] | CCO-4 | Instrucciones del agente |

## Defectos

![Defectos](defectos-es.svg)

4 defectos registrados, cada uno con su origen, su corrección y la corrida que la verificó: 4 verificados y 0 por verificar. 2 vinieron del material, la clave o el arnés de pruebas, no de los agentes.

| Origen | Defectos |
|---|---|
| Arnés de pruebas | 1 |
| Material de prueba | 1 |
| Código | 1 |
| Instrucciones del agente | 1 |

| Agente | Defectos |
|---|---|
| Augusto | 3 |
| Valeria | 1 |

## Consumo y próximo paso

Las 3 rondas usaron 68,3 millones de tokens: 68,3 millones en las corridas calificadas y 0 en las que se repitieron después de corregir un defecto. En promedio, 3,3 millones por entidad.

El material es sintético. Si una versión es estable o de laboratorio lo dice esta evidencia, no su número: estable, con el piso del margen del 95 % en 95 % o más en señales y en datos sobre la corrida más reciente de cada entidad, y ninguna señal en los controles (decisión 0020).

---

La evidencia completa de cada ronda: [`tests/evidencias/familias/cco/`](https://github.com/josenanez/criterio/tree/main/tests/evidencias/familias/cco).
