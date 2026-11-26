# Análisis estadístico de las pruebas · familia CDO

Generado por `scripts/analisis_familias.py` desde `tests/evidencias/familias/cdo/` · ronda completa más reciente: 2 · [English](ANALISIS.md)

No se edita a mano: cada cifra sale de la evidencia y el análisis se regenera con cada ronda.

## En una mirada

La ronda completa más reciente, la 2, sobre las 5 entidades del material: 94 de 94 señales sembradas encontradas (margen del 95 %: 96–100 %) y 0 de más; 348 de 348 datos extraídos bien (100 %, margen del 95 %: 98,9–100 %); y 2 de 2 entidades de control sin ninguna señal.

Sumando las rondas 1–2, 122 de 122 señales encontradas, 0 de más y 378 de 378 datos bien. Las rondas repiten el mismo material: no son muestras independientes, y el margen se calcula sobre los casos de cada una.

## Qué se probó y cómo

En cada entidad corren el setup y el procesamiento de Custodia y Ariadna —los comandos que procesan los documentos y escriben las fichas—, con un tope de tokens fijado antes de empezar, sobre un material que trae su clave aparte, que nadie ve. Los demás comandos calculan sobre esas fichas con el motor, que se prueba con cada cambio del repositorio. Las señales se comparan por su nombre y su clave; la extracción, campo por campo, contra lo que traen los documentos escritos. Las entidades de control no tienen ningún defecto sembrado: cualquier señal en ellas es una falla.

Cobertura: de las señales sembradas, cuántas encontró. Precisión: de las que levantó, cuántas eran correctas. Margen del 95 %: intervalo de confianza de Wilson sobre los casos.

|   |   |
|---|---|
| Rondas | 2; la completa más reciente es la 2 |
| Material | Banca · Colombia, Retail · México, Seguros · Perú |
| Entidades de control | Control · Colombia, Control · México |
| Corridas de una entidad | 10 |
| Señales sembradas | 122 |
| Datos calificados | 378 |

## Resultados acumulados · rondas 1–2

| Métrica | Casos | Resultado | Margen del 95 % |
|---|---|---|---|
| Señales · cobertura | 122 de 122 | 100 % | 96,9–100 % |
| Señales · precisión | 122 de 122 | 100 % | 96,9–100 % |
| Extracción · datos correctos | 378 de 378 | 100 % | 98,9–100 % |
| Control · sin ninguna señal | 4 de 4 | 100 % | 51–100 % |

## Evolución por ronda

![Evolución por ronda](evolucion-es.svg)

| Ronda | Entidades | Señales · cobertura | Señales · precisión | Extracción | Control sin señales | Tokens | Defectos |
|---|---|---|---|---|---|---|---|
| 1 | 5 | 100 % | 100 % | 100 % | 2 de 2 | 31,5 M | 0 |
| 2 | 5 | 100 % | 100 % | 100 % | 2 de 2 | 33,5 M | 0 |

## La ronda completa más reciente · ronda 2

| Métrica | Casos | Resultado | Margen del 95 % |
|---|---|---|---|
| Señales · cobertura | 94 de 94 | 100 % | 96–100 % |
| Señales · precisión | 94 de 94 | 100 % | 96–100 % |
| Extracción · datos correctos | 348 de 348 | 100 % | 98,9–100 % |
| Control · sin ninguna señal | 2 de 2 | 100 % | 34,2–100 % |

## Por industria y país · ronda 2

| Material | Agentes | Señales | De más | Extracción | Tokens |
|---|---|---|---|---|---|
| Banca · Colombia | Ariadna, Custodia | 40 de 40 | 0 | 104 de 104 | 6,7 M |
| Retail · México | Ariadna, Custodia | 27 de 27 | 0 | 76 de 76 | 6,4 M |
| Seguros · Perú | Ariadna, Custodia | 27 de 27 | 0 | 76 de 76 | 6,8 M |
| Control · Colombia | Ariadna, Custodia | 0 de 0 | 0 | 46 de 46 | 6,6 M |
| Control · México | Ariadna, Custodia | 0 de 0 | 0 | 46 de 46 | 7 M |

## Lo que falló, uno por uno · rondas 1–2

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

Las 2 rondas usaron 65 millones de tokens: 65 millones en las corridas calificadas y 0 en las que se repitieron después de corregir un defecto. En promedio, 6,5 millones por entidad.

El material es sintético. Si una versión es estable o de laboratorio lo dice esta evidencia, no su número: estable, con el piso del margen del 95 % en 95 % o más en señales y en datos sobre la corrida más reciente de cada entidad, y ninguna señal en los controles (decisión 0020).

---

La evidencia completa de cada ronda: [`tests/evidencias/familias/cdo/`](https://github.com/josenanez/criterio/tree/main/tests/evidencias/familias/cdo).
