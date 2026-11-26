# Análisis estadístico de las pruebas · familia CDO

Generado por `scripts/analisis_familias.py` desde `tests/evidencias/familias/cdo/` · ronda completa más reciente: 1 · [English](ANALISIS.md)

No se edita a mano: cada cifra sale de la evidencia y el análisis se regenera con cada ronda.

## En una mirada

La ronda completa más reciente, la 1, sobre las 5 entidades del material: 28 de 28 señales sembradas encontradas (margen del 95 %: 87,9–100 %) y 0 de más; 30 de 30 datos extraídos bien (100 %, margen del 95 %: 88,6–100 %); y 2 de 2 entidades de control sin ninguna señal.

Sumando las rondas 1–1, 28 de 28 señales encontradas, 0 de más y 30 de 30 datos bien. Las rondas repiten el mismo material: no son muestras independientes, y el margen se calcula sobre los casos de cada una.

## Qué se probó y cómo

En cada entidad corren el setup y el procesamiento de Custodia y Ariadna —los comandos que procesan los documentos y escriben las fichas—, con un tope de tokens fijado antes de empezar, sobre un material que trae su clave aparte, que nadie ve. Los demás comandos calculan sobre esas fichas con el motor, que se prueba con cada cambio del repositorio. Las señales se comparan por su nombre y su clave; la extracción, campo por campo, contra lo que traen los documentos escritos. Las entidades de control no tienen ningún defecto sembrado: cualquier señal en ellas es una falla.

Cobertura: de las señales sembradas, cuántas encontró. Precisión: de las que levantó, cuántas eran correctas. Margen del 95 %: intervalo de confianza de Wilson sobre los casos.

|   |   |
|---|---|
| Rondas | 1; la completa más reciente es la 1 |
| Material | Banca · Colombia, Retail · México, Seguros · Perú |
| Entidades de control | Control · Colombia, Control · México |
| Corridas de una entidad | 5 |
| Señales sembradas | 28 |
| Datos calificados | 30 |

## Resultados acumulados · rondas 1–1

| Métrica | Casos | Resultado | Margen del 95 % |
|---|---|---|---|
| Señales · cobertura | 28 de 28 | 100 % | 87,9–100 % |
| Señales · precisión | 28 de 28 | 100 % | 87,9–100 % |
| Extracción · datos correctos | 30 de 30 | 100 % | 88,6–100 % |
| Control · sin ninguna señal | 2 de 2 | 100 % | 34,2–100 % |

## Evolución por ronda

![Evolución por ronda](evolucion-es.svg)

| Ronda | Entidades | Señales · cobertura | Señales · precisión | Extracción | Control sin señales | Tokens | Defectos |
|---|---|---|---|---|---|---|---|
| 1 | 5 | 100 % | 100 % | 100 % | 2 de 2 | 31,5 M | 0 |

## La ronda completa más reciente · ronda 1

| Métrica | Casos | Resultado | Margen del 95 % |
|---|---|---|---|
| Señales · cobertura | 28 de 28 | 100 % | 87,9–100 % |
| Señales · precisión | 28 de 28 | 100 % | 87,9–100 % |
| Extracción · datos correctos | 30 de 30 | 100 % | 88,6–100 % |
| Control · sin ninguna señal | 2 de 2 | 100 % | 34,2–100 % |

## Por industria y país · ronda 1

| Material | Agentes | Señales | De más | Extracción | Tokens |
|---|---|---|---|---|---|
| Banca · Colombia | Ariadna, Custodia | 14 de 14 | 0 | 6 de 6 | 6,4 M |
| Retail · México | Ariadna, Custodia | 8 de 8 | 0 | 6 de 6 | 6,3 M |
| Seguros · Perú | Ariadna, Custodia | 6 de 6 | 0 | 6 de 6 | 6,7 M |
| Control · Colombia | Ariadna, Custodia | 0 de 0 | 0 | 6 de 6 | 5,9 M |
| Control · México | Ariadna, Custodia | 0 de 0 | 0 | 6 de 6 | 6,3 M |

## Lo que falló, uno por uno · rondas 1–1

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

Las 1 rondas usaron 31,5 millones de tokens: 31,5 millones en las corridas calificadas y 0 en las que se repitieron después de corregir un defecto. En promedio, 6,3 millones por entidad.

El material es sintético. Si una versión es estable o de laboratorio lo dice esta evidencia, no su número: estable, con el piso del margen del 95 % en 95 % o más en señales y en datos sobre la corrida más reciente de cada entidad, y ninguna señal en los controles (decisión 0020).

---

La evidencia completa de cada ronda: [`tests/evidencias/familias/cdo/`](https://github.com/josenanez/criterio/tree/main/tests/evidencias/familias/cdo).
