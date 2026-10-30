# Análisis estadístico de las pruebas · familia CCO

Generado por `scripts/analisis_familias.py` desde `tests/evidencias/familias/cco/` · ronda más reciente: 2 · [English](ANALISIS.md)

No se edita a mano: cada cifra sale de la evidencia y el análisis se regenera con cada ronda.

## En una mirada

La ronda más reciente, la 2, parcial, sobre 9 de las 15 entidades del material: 117 de 117 señales sembradas encontradas (margen del 95 %: 96,8–100 %) y 0 de más; 45 de 45 datos extraídos bien (100 %, margen del 95 %: 92,1–100 %); y 3 de 3 entidades de control sin ninguna señal.

Sumando las rondas 1–2, 228 de 236 señales encontradas, 3 de más y 100 de 100 datos bien. Las rondas repiten el mismo material: no son muestras independientes, y el margen se calcula sobre los casos de cada una.

## Qué se probó y cómo

En cada entidad corren el setup y el procesamiento de Augusto y Valeria —los comandos que procesan los documentos y escriben las fichas—, con un tope de tokens fijado antes de empezar, sobre un material que trae su clave aparte, que nadie ve. Los demás comandos calculan sobre esas fichas con el motor, que se prueba con cada cambio del repositorio. Las señales se comparan por su nombre y su clave; la extracción, campo por campo, contra lo que traen los documentos escritos. Las entidades de control no tienen ningún defecto sembrado: cualquier señal en ellas es una falla.

Cobertura: de las señales sembradas, cuántas encontró. Precisión: de las que levantó, cuántas eran correctas. Margen del 95 %: intervalo de confianza de Wilson sobre los casos.

|   |   |
|---|---|
| Rondas | 2; la más reciente, la 2, es parcial |
| Material | Retail · Chile, Retail · Ecuador, manufactura · Perú, servicios · Perú, tecnologia · Chile, tecnologia · Ecuador |
| Entidades de control | Control · Chile, Control · Ecuador, Control · Perú |
| Corridas de una entidad | 20 |
| Señales sembradas | 236 |
| Datos calificados | 100 |

## Resultados acumulados · rondas 1–2

| Métrica | Casos | Resultado | Margen del 95 % |
|---|---|---|---|
| Señales · cobertura | 228 de 236 | 96,6 % | 93,4–98,3 % |
| Señales · precisión | 228 de 231 | 98,7 % | 96,2–99,6 % |
| Extracción · datos correctos | 100 de 100 | 100 % | 96,3–100 % |
| Control · sin ninguna señal | 6 de 8 | 75 % | 40,9–92,9 % |

## Evolución por ronda

![Evolución por ronda](evolucion-es.svg)

Una ronda que no corre todas las entidades es parcial: la primera, pequeña, antes de la completa, o una de verificación, que repite las corridas que un defecto corregido dejó pendientes.

| Ronda | Entidades | Señales · cobertura | Señales · precisión | Extracción | Control sin señales | Tokens | Defectos |
|---|---|---|---|---|---|---|---|
| 1 | 10 | 93,3 % | 98,2 % | 100 % | 3 de 4 | 30,9 M | 3 |
| 2 | 10 | 100 % | 99,2 % | 100 % | 3 de 4 | 30,4 M | 1 |

## La ronda más reciente · ronda 2

| Métrica | Casos | Resultado | Margen del 95 % |
|---|---|---|---|
| Señales · cobertura | 117 de 117 | 100 % | 96,8–100 % |
| Señales · precisión | 117 de 117 | 100 % | 96,8–100 % |
| Extracción · datos correctos | 45 de 45 | 100 % | 92,1–100 % |
| Control · sin ninguna señal | 3 de 3 | 100 % | 43,8–100 % |

## Por industria y país · ronda 2

| Material | Agentes | Señales | De más | Extracción | Tokens |
|---|---|---|---|---|---|
| Retail · Chile | Augusto, Valeria | 19 de 19 | 0 | 5 de 5 | 3,2 M |
| Retail · Ecuador | Augusto, Valeria | 18 de 18 | 0 | 5 de 5 | 3,2 M |
| manufactura · Perú | Augusto, Valeria | 20 de 20 | 0 | 5 de 5 | 3,2 M |
| servicios · Perú | Augusto, Valeria | 20 de 20 | 0 | 5 de 5 | 3,1 M |
| tecnologia · Chile | Augusto, Valeria | 20 de 20 | 0 | 5 de 5 | 3 M |
| tecnologia · Ecuador | Augusto, Valeria | 20 de 20 | 0 | 5 de 5 | 3,1 M |
| Control · Chile | Augusto, Valeria | 0 de 0 | 0 | 5 de 5 | 2,6 M |
| Control · Ecuador | Augusto, Valeria | 0 de 0 | 0 | 5 de 5 | 3,1 M |
| Control · Perú | Augusto, Valeria | 0 de 0 | 1 | 5 de 5 | 2,9 M |
| Control · Perú | Augusto, Valeria | 0 de 0 | 0 | 5 de 5 | 2,9 M |

## Lo que falló, uno por uno · rondas 1–2

11 fallas en 20 corridas, cada una con el defecto que la explica: su origen dice si falló el agente o la prueba. Las cifras son las de la calificación original: 0 de esas fallas vinieron de la prueba —el arnés o la clave—, no del agente, y con la prueba corregida se califican como correctas.

| Ronda | Material | Qué | Dónde | Defecto | Origen |
|---|---|---|---|---|---|
| 1 | Control · México | Señal de más | ["commission_differs_from_plan", "comision:2026-10:isabel_mendez"] | — | — |
| 1 | Control · México | Señal de más | ["commission_differs_from_plan", "comision:2026-10:oscar_delgado"] | — | — |
| 1 | servicios · México | Señal no encontrada | ["close_date_slipped", "corre:OPP-1504"] | — | — |
| 1 | servicios · México | Señal no encontrada | ["close_date_slipped", "corre:OPP-1526"] | — | — |
| 1 | servicios · México | Señal no encontrada | ["close_date_slipped", "corre:OPP-1527"] | — | — |
| 1 | servicios · México | Señal no encontrada | ["close_date_slipped", "corre:OPP-1528"] | — | — |
| 1 | tecnologia · Colombia | Señal no encontrada | ["close_date_slipped", "corre:OPP-1204"] | — | — |
| 1 | tecnologia · Colombia | Señal no encontrada | ["close_date_slipped", "corre:OPP-1226"] | — | — |
| 1 | tecnologia · Colombia | Señal no encontrada | ["close_date_slipped", "corre:OPP-1227"] | — | — |
| 1 | tecnologia · Colombia | Señal no encontrada | ["close_date_slipped", "corre:OPP-1228"] | — | — |
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

Las 2 rondas usaron 61,3 millones de tokens: 61,3 millones en las corridas calificadas y 0 en las que se repitieron después de corregir un defecto. En promedio, 3,1 millones por entidad.

El material es sintético. Si una versión es estable o de laboratorio lo dice esta evidencia, no su número: estable, con el piso del margen del 95 % en 95 % o más en señales y en datos sobre la corrida más reciente de cada entidad, y ninguna señal en los controles (decisión 0020).

---

La evidencia completa de cada ronda: [`tests/evidencias/familias/cco/`](https://github.com/josenanez/criterio/tree/main/tests/evidencias/familias/cco).
