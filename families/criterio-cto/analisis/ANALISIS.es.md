# Análisis estadístico de las pruebas · familia CTO

Generado por `scripts/analisis_familias.py` desde `tests/evidencias/familias/cto/` · ronda más reciente: 2 · [English](ANALISIS.md)

No se edita a mano: cada cifra sale de la evidencia y el análisis se regenera con cada ronda.

## En una mirada

La ronda más reciente, la 2, parcial, sobre 1 de las 6 entidades del material: 24 de 24 señales sembradas encontradas (margen del 95 %: 86,2–100 %) y 0 de más; 61 de 61 datos extraídos bien (100 %, margen del 95 %: 94–100 %); y 0 de 0 entidades de control sin ninguna señal.

Sumando las rondas 1–2, 120 de 120 señales encontradas, 0 de más y 328 de 328 datos bien. Las rondas repiten el mismo material: no son muestras independientes, y el margen se calcula sobre los casos de cada una.

## Qué se probó y cómo

En cada entidad corren el setup y el procesamiento de Fausto y Domingo —los comandos que procesan los documentos y escriben las fichas—, con un tope de tokens fijado antes de empezar, sobre un material que trae su clave aparte, que nadie ve. Los demás comandos calculan sobre esas fichas con el motor, que se prueba con cada cambio del repositorio. Las señales se comparan por su nombre y su clave; la extracción, campo por campo, contra lo que traen los documentos escritos. Las entidades de control no tienen ningún defecto sembrado: cualquier señal en ellas es una falla.

Cobertura: de las señales sembradas, cuántas encontró. Precisión: de las que levantó, cuántas eran correctas. Margen del 95 %: intervalo de confianza de Wilson sobre los casos.

|   |   |
|---|---|
| Rondas | 2; la más reciente, la 2, es parcial |
| Material | Banca · Panamá |
| Entidades de control |  |
| Corridas de una entidad | 6 |
| Señales sembradas | 120 |
| Datos calificados | 328 |

## Resultados acumulados · rondas 1–2

| Métrica | Casos | Resultado | Margen del 95 % |
|---|---|---|---|
| Señales · cobertura | 120 de 120 | 100 % | 96,8–100 % |
| Señales · precisión | 120 de 120 | 100 % | 96,8–100 % |
| Extracción · datos correctos | 328 de 328 | 100 % | 98,8–100 % |
| Control · sin ninguna señal | 2 de 2 | 100 % | 34,2–100 % |

## Evolución por ronda

![Evolución por ronda](evolucion-es.svg)

Una ronda que no corre todas las entidades es parcial: la primera, pequeña, antes de la completa, o una de verificación, que repite las corridas que un defecto corregido dejó pendientes.

| Ronda | Entidades | Señales · cobertura | Señales · precisión | Extracción | Control sin señales | Tokens | Defectos |
|---|---|---|---|---|---|---|---|
| 1 | 5 | 100 % | 100 % | 100 % | 2 de 2 | 34,5 M | 1 |
| 2 | 1 | 100 % | 100 % | 100 % | 0 de 0 | 6,6 M | 0 |

## La ronda más reciente · ronda 2

| Métrica | Casos | Resultado | Margen del 95 % |
|---|---|---|---|
| Señales · cobertura | 24 de 24 | 100 % | 86,2–100 % |
| Señales · precisión | 24 de 24 | 100 % | 86,2–100 % |
| Extracción · datos correctos | 61 de 61 | 100 % | 94–100 % |
| Control · sin ninguna señal | 0 de 0 | — | — |

## Por industria y país · ronda 2

| Material | Agentes | Señales | De más | Extracción | Tokens |
|---|---|---|---|---|---|
| Banca · Panamá | Domingo, Fausto | 24 de 24 | 0 | 61 de 61 | 6,6 M |

## Lo que falló, uno por uno · rondas 1–2

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

Las 2 rondas usaron 41,2 millones de tokens: 41,2 millones en las corridas calificadas y 0 en las que se repitieron después de corregir un defecto. En promedio, 6,9 millones por entidad.

El material es sintético. Si una versión es estable o de laboratorio lo dice esta evidencia, no su número: estable, con el piso del margen del 95 % en 95 % o más en señales y en datos sobre la corrida más reciente de cada entidad, y ninguna señal en los controles (decisión 0020).

---

La evidencia completa de cada ronda: [`tests/evidencias/familias/cto/`](https://github.com/josenanez/criterio/tree/main/tests/evidencias/familias/cto).
