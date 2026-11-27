# Análisis estadístico de las pruebas · familia CMO

Generado por `scripts/analisis_familias.py` desde `tests/evidencias/familias/cmo/` · ronda completa más reciente: 2 · [English](ANALISIS.md)

No se edita a mano: cada cifra sale de la evidencia y el análisis se regenera con cada ronda.

## En una mirada

La ronda completa más reciente, la 2, sobre las 5 entidades del material: 88 de 88 señales sembradas encontradas (margen del 95 %: 95,8–100 %) y 0 de más; 380 de 380 datos extraídos bien (100 %, margen del 95 %: 98,9–100 %); y 2 de 2 entidades de control sin ninguna señal.

Sumando las rondas 1–2, 110 de 110 señales encontradas, 0 de más y 405 de 405 datos bien. Las rondas repiten el mismo material: no son muestras independientes, y el margen se calcula sobre los casos de cada una.

## Qué se probó y cómo

En cada entidad corren el setup y el procesamiento de Lucía y Próspero —los comandos que procesan los documentos y escriben las fichas—, con un tope de tokens fijado antes de empezar, sobre un material que trae su clave aparte, que nadie ve. Los demás comandos calculan sobre esas fichas con el motor, que se prueba con cada cambio del repositorio. Las señales se comparan por su nombre y su clave; la extracción, campo por campo, contra lo que traen los documentos escritos. Las entidades de control no tienen ningún defecto sembrado: cualquier señal en ellas es una falla.

Cobertura: de las señales sembradas, cuántas encontró. Precisión: de las que levantó, cuántas eran correctas. Margen del 95 %: intervalo de confianza de Wilson sobre los casos.

|   |   |
|---|---|
| Rondas | 2; la completa más reciente es la 2 |
| Material | Banca · Perú, Manufactura · México, Retail · Colombia |
| Entidades de control | Control · Colombia, Control · México |
| Corridas de una entidad | 10 |
| Señales sembradas | 110 |
| Datos calificados | 405 |

## Resultados acumulados · rondas 1–2

| Métrica | Casos | Resultado | Margen del 95 % |
|---|---|---|---|
| Señales · cobertura | 110 de 110 | 100 % | 96,6–100 % |
| Señales · precisión | 110 de 110 | 100 % | 96,6–100 % |
| Extracción · datos correctos | 405 de 405 | 100 % | 99–100 % |
| Control · sin ninguna señal | 4 de 4 | 100 % | 51–100 % |

## Evolución por ronda

![Evolución por ronda](evolucion-es.svg)

| Ronda | Entidades | Señales · cobertura | Señales · precisión | Extracción | Control sin señales | Tokens | Defectos |
|---|---|---|---|---|---|---|---|
| 1 | 5 | 100 % | 100 % | 100 % | 2 de 2 | 32,9 M | 2 |
| 2 | 5 | 100 % | 100 % | 100 % | 2 de 2 | 34,6 M | 0 |

## La ronda completa más reciente · ronda 2

| Métrica | Casos | Resultado | Margen del 95 % |
|---|---|---|---|
| Señales · cobertura | 88 de 88 | 100 % | 95,8–100 % |
| Señales · precisión | 88 de 88 | 100 % | 95,8–100 % |
| Extracción · datos correctos | 380 de 380 | 100 % | 98,9–100 % |
| Control · sin ninguna señal | 2 de 2 | 100 % | 34,2–100 % |

## Por industria y país · ronda 2

| Material | Agentes | Señales | De más | Extracción | Tokens |
|---|---|---|---|---|---|
| Banca · Perú | Lucía, Próspero | 33 de 33 | 0 | 99 de 99 | 6,7 M |
| Manufactura · México | Lucía, Próspero | 22 de 22 | 0 | 76 de 76 | 7 M |
| Retail · Colombia | Lucía, Próspero | 33 de 33 | 0 | 99 de 99 | 7,2 M |
| Control · Colombia | Lucía, Próspero | 0 de 0 | 0 | 53 de 53 | 6,6 M |
| Control · México | Lucía, Próspero | 0 de 0 | 0 | 53 de 53 | 7,2 M |

## Lo que falló, uno por uno · rondas 1–2

Ninguna falla.

| Ronda | Material | Qué | Dónde | Defecto | Origen |
|---|---|---|---|---|---|

## Defectos

![Defectos](defectos-es.svg)

2 defectos registrados, cada uno con su origen, su corrección y la corrida que la verificó: 2 verificados y 0 por verificar. 1 vinieron del material, la clave o el arnés de pruebas, no de los agentes.

| Origen | Defectos |
|---|---|
| Clave de calificación | 1 |
| Instrucciones del agente | 1 |

| Agente | Defectos |
|---|---|
| Lucía | 2 |

## Consumo y próximo paso

Las 2 rondas usaron 74,5 millones de tokens: 67,5 millones en las corridas calificadas y 7 en las que se repitieron después de corregir un defecto. En promedio, 6,8 millones por entidad.

El material es sintético. Si una versión es estable o de laboratorio lo dice esta evidencia, no su número: estable, con el piso del margen del 95 % en 95 % o más en señales y en datos sobre la corrida más reciente de cada entidad, y ninguna señal en los controles (decisión 0020).

---

La evidencia completa de cada ronda: [`tests/evidencias/familias/cmo/`](https://github.com/josenanez/criterio/tree/main/tests/evidencias/familias/cmo).
