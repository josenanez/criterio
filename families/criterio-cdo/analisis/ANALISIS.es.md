# Análisis estadístico de las pruebas · familia CDO

Generado por `scripts/analisis_familias.py` desde `tests/evidencias/familias/cdo/` · ronda más reciente: 3 · [English](ANALISIS.md)

No se edita a mano: cada cifra sale de la evidencia y el análisis se regenera con cada ronda.

## En una mirada

La ronda más reciente, la 3, parcial, sobre 1 de las 7 entidades del material: 27 de 27 señales sembradas encontradas (margen del 95 %: 87,5–100 %) y 0 de más; 76 de 76 datos extraídos bien (100 %, margen del 95 %: 95,1–100 %); y 0 de 0 entidades de control sin ninguna señal.

Sumando las rondas 1–3, 149 de 149 señales encontradas, 0 de más y 454 de 454 datos bien. Las rondas repiten el mismo material: no son muestras independientes, y el margen se calcula sobre los casos de cada una.

## Qué se probó y cómo

En cada entidad corren el setup y el procesamiento de Custodia y Ariadna —los comandos que procesan los documentos y escriben las fichas—, con un tope de tokens fijado antes de empezar, sobre un material que trae su clave aparte, que nadie ve. Los demás comandos calculan sobre esas fichas con el motor, que se prueba con cada cambio del repositorio. Las señales se comparan por su nombre y su clave; la extracción, campo por campo, contra lo que traen los documentos escritos. Las entidades de control no tienen ningún defecto sembrado: cualquier señal en ellas es una falla.

Cobertura: de las señales sembradas, cuántas encontró. Precisión: de las que levantó, cuántas eran correctas. Margen del 95 %: intervalo de confianza de Wilson sobre los casos.

|   |   |
|---|---|
| Rondas | 3; la más reciente, la 3, es parcial |
| Material | Banca · Chile |
| Entidades de control |  |
| Corridas de una entidad | 11 |
| Señales sembradas | 149 |
| Datos calificados | 454 |

## Resultados acumulados · rondas 1–3

| Métrica | Casos | Resultado | Margen del 95 % |
|---|---|---|---|
| Señales · cobertura | 149 de 149 | 100 % | 97,4–100 % |
| Señales · precisión | 149 de 149 | 100 % | 97,4–100 % |
| Extracción · datos correctos | 454 de 454 | 100 % | 99,1–100 % |
| Control · sin ninguna señal | 4 de 4 | 100 % | 51–100 % |

## Evolución por ronda

![Evolución por ronda](evolucion-es.svg)

Una ronda que no corre todas las entidades es parcial: la primera, pequeña, antes de la completa, o una de verificación, que repite las corridas que un defecto corregido dejó pendientes.

| Ronda | Entidades | Señales · cobertura | Señales · precisión | Extracción | Control sin señales | Tokens | Defectos |
|---|---|---|---|---|---|---|---|
| 1 | 5 | 100 % | 100 % | 100 % | 2 de 2 | 31,5 M | 0 |
| 2 | 5 | 100 % | 100 % | 100 % | 2 de 2 | 33,5 M | 0 |
| 3 | 1 | 100 % | 100 % | 100 % | 0 de 0 | 6,5 M | 0 |

## La ronda más reciente · ronda 3

| Métrica | Casos | Resultado | Margen del 95 % |
|---|---|---|---|
| Señales · cobertura | 27 de 27 | 100 % | 87,5–100 % |
| Señales · precisión | 27 de 27 | 100 % | 87,5–100 % |
| Extracción · datos correctos | 76 de 76 | 100 % | 95,1–100 % |
| Control · sin ninguna señal | 0 de 0 | — | — |

## Por industria y país · ronda 3

| Material | Agentes | Señales | De más | Extracción | Tokens |
|---|---|---|---|---|---|
| Banca · Chile | Ariadna, Custodia | 27 de 27 | 0 | 76 de 76 | 6,5 M |

## Lo que falló, uno por uno · rondas 1–3

Ninguna falla.

| Ronda | Material | Qué | Dónde | Defecto | Origen |
|---|---|---|---|---|---|

## Defectos

![Defectos](defectos-es.svg)

0 defectos registrados, cada uno con su origen, su corrección y la corrida que la verificó: 0 verificados y 0 por verificar. 0 vinieron del material, la clave o el arnés de pruebas, no de los agentes.

| Origen | Defectos |
|---|---|

| Agente | Defectos |
|---|---|

## Consumo y próximo paso

Las 3 rondas usaron 71,6 millones de tokens: 71,6 millones en las corridas calificadas y 0 en las que se repitieron después de corregir un defecto. En promedio, 6,5 millones por entidad.

El material es sintético. Si una versión es estable o de laboratorio lo dice esta evidencia, no su número: estable, con el piso del margen del 95 % en 95 % o más en señales y en datos sobre la corrida más reciente de cada entidad, y ninguna señal en los controles (decisión 0020).

---

La evidencia completa de cada ronda: [`tests/evidencias/familias/cdo/`](https://github.com/josenanez/criterio/tree/main/tests/evidencias/familias/cdo).
