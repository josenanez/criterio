# Análisis estadístico de las pruebas · familia CISO

Generado por `scripts/analisis_familias.py` desde `tests/evidencias/familias/ciso/` · ronda más reciente: 1 · [English](ANALISIS.md)

No se edita a mano: cada cifra sale de la evidencia y el análisis se regenera con cada ronda.

## En una mirada

La ronda más reciente, la 1, parcial, sobre 4 de las 6 entidades del material: 100 de 100 señales sembradas encontradas (margen del 95 %: 96,3–100 %) y 0 de más; 32 de 32 datos extraídos bien (100 %, margen del 95 %: 89,2–100 %); y 0 de 0 entidades de control sin ninguna señal.

Sumando las rondas 1–1, 100 de 100 señales encontradas, 0 de más y 32 de 32 datos bien. Las rondas repiten el mismo material: no son muestras independientes, y el margen se calcula sobre los casos de cada una.

## Qué se probó y cómo

En cada entidad corren el setup y el procesamiento de Alexis, Guillermo y Amparo —los comandos que procesan los documentos y escriben las fichas—, con un tope de tokens fijado antes de empezar, sobre un material que trae su clave aparte, que nadie ve. Los demás comandos calculan sobre esas fichas con el motor, que se prueba con cada cambio del repositorio. Las señales se comparan por su nombre y su clave; la extracción, campo por campo, contra lo que traen los documentos escritos. Las entidades de control no tienen ningún defecto sembrado: cualquier señal en ellas es una falla.

Cobertura: de las señales sembradas, cuántas encontró. Precisión: de las que levantó, cuántas eran correctas. Margen del 95 %: intervalo de confianza de Wilson sobre los casos.

|   |   |
|---|---|
| Rondas | 1; la más reciente, la 1, es parcial |
| Material | Banca · Colombia, Retail · México, Tecnología · Chile, salud · Perú |
| Entidades de control |  |
| Corridas de una entidad | 4 |
| Señales sembradas | 100 |
| Datos calificados | 32 |

## Resultados acumulados · rondas 1–1

| Métrica | Casos | Resultado | Margen del 95 % |
|---|---|---|---|
| Señales · cobertura | 100 de 100 | 100 % | 96,3–100 % |
| Señales · precisión | 100 de 100 | 100 % | 96,3–100 % |
| Extracción · datos correctos | 32 de 32 | 100 % | 89,2–100 % |
| Control · sin ninguna señal | 0 de 0 | — | — |

## Evolución por ronda

![Evolución por ronda](evolucion-es.svg)

Una ronda que no corre todas las entidades es parcial: la primera, pequeña, antes de la completa, o una de verificación, que repite las corridas que un defecto corregido dejó pendientes.

| Ronda | Entidades | Señales · cobertura | Señales · precisión | Extracción | Control sin señales | Tokens | Defectos |
|---|---|---|---|---|---|---|---|
| 1 | 4 | 100 % | 100 % | 100 % | 0 de 0 | 21,4 M | 3 |

## La ronda más reciente · ronda 1

| Métrica | Casos | Resultado | Margen del 95 % |
|---|---|---|---|
| Señales · cobertura | 100 de 100 | 100 % | 96,3–100 % |
| Señales · precisión | 100 de 100 | 100 % | 96,3–100 % |
| Extracción · datos correctos | 32 de 32 | 100 % | 89,2–100 % |
| Control · sin ninguna señal | 0 de 0 | — | — |

## Por industria y país · ronda 1

| Material | Agentes | Señales | De más | Extracción | Tokens |
|---|---|---|---|---|---|
| Banca · Colombia | Alexis, Amparo, Guillermo | 25 de 25 | 0 | 8 de 8 | 5,3 M |
| Retail · México | Alexis, Amparo, Guillermo | 25 de 25 | 0 | 8 de 8 | 5,1 M |
| Tecnología · Chile | Alexis, Amparo, Guillermo | 25 de 25 | 0 | 8 de 8 | 5 M |
| salud · Perú | Alexis, Amparo, Guillermo | 25 de 25 | 0 | 8 de 8 | 6 M |

## Lo que falló, uno por uno · rondas 1–1

Ninguna falla.

| Ronda | Material | Qué | Dónde | Defecto | Origen |
|---|---|---|---|---|---|

## Defectos

![Defectos](defectos-es.svg)

3 defectos registrados, cada uno con su origen, su corrección y la corrida que la verificó: 2 verificados y 1 por verificar. 1 vinieron del material, la clave o el arnés de pruebas, no de los agentes.

| Origen | Defectos |
|---|---|
| Arnés de pruebas | 1 |
| Código | 1 |
| Instrucciones del agente | 1 |

| Agente | Defectos |
|---|---|
| Amparo | 2 |
| Alexis | 2 |
| Guillermo | 1 |

## Consumo y próximo paso

Las 1 rondas usaron 21,4 millones de tokens: 21,4 millones en las corridas calificadas y 0 en las que se repitieron después de corregir un defecto. En promedio, 5,4 millones por entidad.

El material es sintético. Si una versión es estable o de laboratorio lo dice esta evidencia, no su número: estable, con el piso del margen del 95 % en 95 % o más en señales y en datos sobre la corrida más reciente de cada entidad, y ninguna señal en los controles (decisión 0020).

---

La evidencia completa de cada ronda: [`tests/evidencias/familias/ciso/`](https://github.com/josenanez/criterio/tree/main/tests/evidencias/familias/ciso).
