# Análisis estadístico de las pruebas · familia CTO

Generado por `scripts/analisis_familias.py` desde `tests/evidencias/familias/cto/` · ronda completa más reciente: 1 · [English](ANALISIS.md)

No se edita a mano: cada cifra sale de la evidencia y el análisis se regenera con cada ronda.

## En una mirada

La ronda completa más reciente, la 1, sobre las 5 entidades del material: 96 de 96 señales sembradas encontradas (margen del 95 %: 96,1–100 %) y 0 de más; 267 de 267 datos extraídos bien (100 %, margen del 95 %: 98,5–100 %); y 2 de 2 entidades de control sin ninguna señal.

Sumando las rondas 1–1, 96 de 96 señales encontradas, 0 de más y 267 de 267 datos bien. Las rondas repiten el mismo material: no son muestras independientes, y el margen se calcula sobre los casos de cada una.

## Qué se probó y cómo

En cada entidad corren el setup y el procesamiento de Fausto y Domingo —los comandos que procesan los documentos y escriben las fichas—, con un tope de tokens fijado antes de empezar, sobre un material que trae su clave aparte, que nadie ve. Los demás comandos calculan sobre esas fichas con el motor, que se prueba con cada cambio del repositorio. Las señales se comparan por su nombre y su clave; la extracción, campo por campo, contra lo que traen los documentos escritos. Las entidades de control no tienen ningún defecto sembrado: cualquier señal en ellas es una falla.

Cobertura: de las señales sembradas, cuántas encontró. Precisión: de las que levantó, cuántas eran correctas. Margen del 95 %: intervalo de confianza de Wilson sobre los casos.

|   |   |
|---|---|
| Rondas | 1; la completa más reciente es la 1 |
| Material | Banca · Colombia, Retail · México, Tecnología · Chile |
| Entidades de control | Control · Colombia, Control · México |
| Corridas de una entidad | 5 |
| Señales sembradas | 96 |
| Datos calificados | 267 |

## Resultados acumulados · rondas 1–1

| Métrica | Casos | Resultado | Margen del 95 % |
|---|---|---|---|
| Señales · cobertura | 96 de 96 | 100 % | 96,1–100 % |
| Señales · precisión | 96 de 96 | 100 % | 96,1–100 % |
| Extracción · datos correctos | 267 de 267 | 100 % | 98,5–100 % |
| Control · sin ninguna señal | 2 de 2 | 100 % | 34,2–100 % |

## Evolución por ronda

![Evolución por ronda](evolucion-es.svg)

| Ronda | Entidades | Señales · cobertura | Señales · precisión | Extracción | Control sin señales | Tokens | Defectos |
|---|---|---|---|---|---|---|---|
| 1 | 5 | 100 % | 100 % | 100 % | 2 de 2 | 34,5 M | 1 |

## La ronda completa más reciente · ronda 1

| Métrica | Casos | Resultado | Margen del 95 % |
|---|---|---|---|
| Señales · cobertura | 96 de 96 | 100 % | 96,1–100 % |
| Señales · precisión | 96 de 96 | 100 % | 96,1–100 % |
| Extracción · datos correctos | 267 de 267 | 100 % | 98,5–100 % |
| Control · sin ninguna señal | 2 de 2 | 100 % | 34,2–100 % |

## Por industria y país · ronda 1

| Material | Agentes | Señales | De más | Extracción | Tokens |
|---|---|---|---|---|---|
| Banca · Colombia | Domingo, Fausto | 36 de 36 | 0 | 70 de 70 | 7 M |
| Retail · México | Domingo, Fausto | 36 de 36 | 0 | 70 de 70 | 7,3 M |
| Tecnología · Chile | Domingo, Fausto | 24 de 24 | 0 | 61 de 61 | 7,2 M |
| Control · Colombia | Domingo, Fausto | 0 de 0 | 0 | 33 de 33 | 6,4 M |
| Control · México | Domingo, Fausto | 0 de 0 | 0 | 33 de 33 | 6,5 M |

## Lo que falló, uno por uno · rondas 1–1

Ninguna falla.

| Ronda | Material | Qué | Dónde | Defecto | Origen |
|---|---|---|---|---|---|

## Defectos

![Defectos](defectos-es.svg)

1 defectos registrados, cada uno con su origen, su corrección y la corrida que la verificó: 1 verificados y 0 por verificar. 0 vinieron del material, la clave o el arnés de pruebas, no de los agentes.

| Origen | Defectos |
|---|---|
| Instrucciones del agente | 1 |

| Agente | Defectos |
|---|---|
| Fausto | 1 |

## Consumo y próximo paso

Las 1 rondas usaron 34,5 millones de tokens: 34,5 millones en las corridas calificadas y 0 en las que se repitieron después de corregir un defecto. En promedio, 6,9 millones por entidad.

El material es sintético. Si una versión es estable o de laboratorio lo dice esta evidencia, no su número: estable, con el piso del margen del 95 % en 95 % o más en señales y en datos sobre la corrida más reciente de cada entidad, y ninguna señal en los controles (decisión 0020).

---

La evidencia completa de cada ronda: [`tests/evidencias/familias/cto/`](https://github.com/josenanez/criterio/tree/main/tests/evidencias/familias/cto).
