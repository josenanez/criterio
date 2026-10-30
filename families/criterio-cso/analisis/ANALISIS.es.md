# Análisis estadístico de las pruebas · familia CSO

Generado por `scripts/analisis_familias.py` desde `tests/evidencias/familias/cso/` · ronda más reciente: 1 · [English](ANALISIS.md)

No se edita a mano: cada cifra sale de la evidencia y el análisis se regenera con cada ronda.

## En una mirada

La ronda más reciente, la 1, parcial, sobre 6 de las 15 entidades del material: 80 de 80 señales sembradas encontradas (margen del 95 %: 95,4–100 %) y 0 de más; 30 de 30 datos extraídos bien (100 %, margen del 95 %: 88,6–100 %); y 2 de 2 entidades de control sin ninguna señal.

Sumando las rondas 1–1, 111 de 119 señales encontradas, 2 de más y 50 de 50 datos bien. Las rondas repiten el mismo material: no son muestras independientes, y el margen se calcula sobre los casos de cada una.

## Qué se probó y cómo

En cada entidad corren el setup y el procesamiento de Augusto y Valeria —los comandos que procesan los documentos y escriben las fichas—, con un tope de tokens fijado antes de empezar, sobre un material que trae su clave aparte, que nadie ve. Los demás comandos calculan sobre esas fichas con el motor, que se prueba con cada cambio del repositorio. Las señales se comparan por su nombre y su clave; la extracción, campo por campo, contra lo que traen los documentos escritos. Las entidades de control no tienen ningún defecto sembrado: cualquier señal en ellas es una falla.

Cobertura: de las señales sembradas, cuántas encontró. Precisión: de las que levantó, cuántas eran correctas. Margen del 95 %: intervalo de confianza de Wilson sobre los casos.

|   |   |
|---|---|
| Rondas | 1; la más reciente, la 1, es parcial |
| Material | Retail · Colombia, manufactura · México, servicios · México, tecnologia · Colombia |
| Entidades de control | Control · Colombia, Control · México |
| Corridas de una entidad | 10 |
| Señales sembradas | 119 |
| Datos calificados | 50 |

## Resultados acumulados · rondas 1–1

| Métrica | Casos | Resultado | Margen del 95 % |
|---|---|---|---|
| Señales · cobertura | 111 de 119 | 93,3 % | 87,2–96,6 % |
| Señales · precisión | 111 de 113 | 98,2 % | 93,7–99,6 % |
| Extracción · datos correctos | 50 de 50 | 100 % | 92,8–100 % |
| Control · sin ninguna señal | 3 de 4 | 75 % | 30–95,5 % |

## Evolución por ronda

![Evolución por ronda](evolucion-es.svg)

Una ronda que no corre todas las entidades es parcial: la primera, pequeña, antes de la completa, o una de verificación, que repite las corridas que un defecto corregido dejó pendientes.

| Ronda | Entidades | Señales · cobertura | Señales · precisión | Extracción | Control sin señales | Tokens | Defectos |
|---|---|---|---|---|---|---|---|
| 1 | 10 | 93,3 % | 98,2 % | 100 % | 3 de 4 | 30,9 M | 3 |

## La ronda más reciente · ronda 1

| Métrica | Casos | Resultado | Margen del 95 % |
|---|---|---|---|
| Señales · cobertura | 80 de 80 | 100 % | 95,4–100 % |
| Señales · precisión | 80 de 80 | 100 % | 95,4–100 % |
| Extracción · datos correctos | 30 de 30 | 100 % | 88,6–100 % |
| Control · sin ninguna señal | 2 de 2 | 100 % | 34,2–100 % |

## Por industria y país · ronda 1

| Material | Agentes | Señales | De más | Extracción | Tokens |
|---|---|---|---|---|---|
| Retail · Colombia | Augusto, Valeria | 21 de 21 | 0 | 5 de 5 | 2,8 M |
| manufactura · México | Augusto, Valeria | 20 de 20 | 0 | 5 de 5 | 3,1 M |
| servicios · México | Augusto, Valeria | 15 de 19 | 0 | 5 de 5 | 3,2 M |
| servicios · México | Augusto, Valeria | 19 de 19 | 0 | 5 de 5 | 3,3 M |
| tecnologia · Colombia | Augusto, Valeria | 16 de 20 | 0 | 5 de 5 | 3,5 M |
| tecnologia · Colombia | Augusto, Valeria | 20 de 20 | 0 | 5 de 5 | 3,2 M |
| Control · Colombia | Augusto, Valeria | 0 de 0 | 0 | 5 de 5 | 3,2 M |
| Control · México | Augusto, Valeria | 0 de 0 | 2 | 5 de 5 | 2,9 M |
| Control · México | Augusto, Valeria | 0 de 0 | 0 | 5 de 5 | 2,9 M |
| Control · México | Augusto, Valeria | 0 de 0 | 0 | 5 de 5 | 2,9 M |

## Lo que falló, uno por uno · rondas 1–1

10 fallas en 10 corridas, cada una con el defecto que la explica: su origen dice si falló el agente o la prueba. Las cifras son las de la calificación original: 0 de esas fallas vinieron de la prueba —el arnés o la clave—, no del agente, y con la prueba corregida se califican como correctas.

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

## Defectos

![Defectos](defectos-es.svg)

3 defectos registrados, cada uno con su origen, su corrección y la corrida que la verificó: 3 verificados y 0 por verificar. 2 vinieron del material, la clave o el arnés de pruebas, no de los agentes.

| Origen | Defectos |
|---|---|
| Arnés de pruebas | 1 |
| Material de prueba | 1 |
| Código | 1 |

| Agente | Defectos |
|---|---|
| Augusto | 2 |
| Valeria | 1 |

## Consumo y próximo paso

Las 1 rondas usaron 30,9 millones de tokens: 30,9 millones en las corridas calificadas y 0 en las que se repitieron después de corregir un defecto. En promedio, 3,1 millones por entidad.

El material es sintético. Si una versión es estable o de laboratorio lo dice esta evidencia, no su número: estable, con el piso del margen del 95 % en 95 % o más en señales y en datos sobre la corrida más reciente de cada entidad, y ninguna señal en los controles (decisión 0020).

---

La evidencia completa de cada ronda: [`tests/evidencias/familias/cso/`](https://github.com/josenanez/criterio/tree/main/tests/evidencias/familias/cso).
