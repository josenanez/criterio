# Análisis estadístico de las pruebas · familia CFO

Generado por `scripts/analisis_familias.py` desde `tests/evidencias/familias/cfo/` · ronda más reciente: 11 · [English](ANALISIS.md)

No se edita a mano: cada cifra sale de la evidencia y el análisis se regenera con cada ronda.

## En una mirada

La ronda más reciente, la 11, parcial, sobre 3 de las 33 entidades del material: 25 de 25 señales sembradas encontradas (margen del 95 %: 86,6–100 %) y 0 de más; 25 de 25 datos extraídos bien (100 %, margen del 95 %: 86,6–100 %); y 1 de 1 entidades de control sin ninguna señal.

Sumando las rondas 1–11, 355 de 355 señales encontradas, 0 de más y 342 de 344 datos bien. Las rondas repiten el mismo material: no son muestras independientes, y el margen se calcula sobre los casos de cada una.

## Qué se probó y cómo

En cada entidad corren el setup y el procesamiento de Clara, Tomás y Áurea —los comandos que procesan los documentos y escriben las fichas—, con un tope de tokens fijado antes de empezar, sobre un material que trae su clave aparte, que nadie ve. Los demás comandos calculan sobre esas fichas con el motor, que se prueba con cada cambio del repositorio. Las señales se comparan por su nombre y su clave; la extracción, campo por campo, contra lo que traen los documentos escritos. Las entidades de control no tienen ningún defecto sembrado: cualquier señal en ellas es una falla.

Cobertura: de las señales sembradas, cuántas encontró. Precisión: de las que levantó, cuántas eran correctas. Margen del 95 %: intervalo de confianza de Wilson sobre los casos.

|   |   |
|---|---|
| Rondas | 11; la más reciente, la 11, es parcial |
| Material | Banca · Costa Rica, Retail · Costa Rica |
| Entidades de control | Control · Costa Rica |
| Corridas de una entidad | 42 |
| Señales sembradas | 355 |
| Datos calificados | 344 |

## Resultados acumulados · rondas 1–11

| Métrica | Casos | Resultado | Margen del 95 % |
|---|---|---|---|
| Señales · cobertura | 355 de 355 | 100 % | 98,9–100 % |
| Señales · precisión | 355 de 355 | 100 % | 98,9–100 % |
| Extracción · datos correctos | 342 de 344 | 99,4 % | 97,9–99,9 % |
| Control · sin ninguna señal | 14 de 14 | 100 % | 78,4–100 % |

## Evolución por ronda

![Evolución por ronda](evolucion-es.svg)

Una ronda que no corre todas las entidades es parcial: la primera, pequeña, antes de la completa, o una de verificación, que repite las corridas que un defecto corregido dejó pendientes.

| Ronda | Entidades | Señales · cobertura | Señales · precisión | Extracción | Control sin señales | Tokens | Defectos |
|---|---|---|---|---|---|---|---|
| 1 | 2 | 100 % | 100 % | 100 % | 1 de 1 | 17,3 M | 3 |
| 2 | 6 | 100 % | 100 % | 98 % | 2 de 2 | 53 M | 1 |
| 3 | 4 | 100 % | 100 % | 100 % | 1 de 1 | 17,2 M | 3 |
| 4 | 9 | 100 % | 100 % | 100 % | 3 de 3 | 38 M | 3 |
| 5 | 3 | 100 % | 100 % | 100 % | 1 de 1 | 12,7 M | 0 |
| 6 | 3 | 100 % | 100 % | 100 % | 1 de 1 | 13,2 M | 0 |
| 7 | 3 | 100 % | 100 % | 96 % | 1 de 1 | 12,1 M | 1 |
| 8 | 3 | 100 % | 100 % | 100 % | 1 de 1 | 12,3 M | 0 |
| 9 | 3 | 100 % | 100 % | 100 % | 1 de 1 | 12,8 M | 0 |
| 10 | 3 | 100 % | 100 % | 100 % | 1 de 1 | 12,7 M | 0 |
| 11 | 3 | 100 % | 100 % | 100 % | 1 de 1 | 11,9 M | 0 |

## La ronda más reciente · ronda 11

| Métrica | Casos | Resultado | Margen del 95 % |
|---|---|---|---|
| Señales · cobertura | 25 de 25 | 100 % | 86,6–100 % |
| Señales · precisión | 25 de 25 | 100 % | 86,6–100 % |
| Extracción · datos correctos | 25 de 25 | 100 % | 86,6–100 % |
| Control · sin ninguna señal | 1 de 1 | 100 % | 20,6–100 % |

## Por industria y país · ronda 11

| Material | Agentes | Señales | De más | Extracción | Tokens |
|---|---|---|---|---|---|
| Banca · Costa Rica | Áurea, Clara, Tomás | 13 de 13 | 0 | 9 de 9 | 4 M |
| Retail · Costa Rica | Áurea, Clara, Tomás | 12 de 12 | 0 | 8 de 8 | 3,9 M |
| Control · Costa Rica | Áurea, Clara, Tomás | 0 de 0 | 0 | 8 de 8 | 3,9 M |

## Lo que falló, uno por uno · rondas 1–11

2 fallas en 42 corridas, cada una con el defecto que la explica: su origen dice si falló el agente o la prueba. Las cifras son las de la calificación original: 1 de esas fallas vino de la prueba —el arnés o la clave—, no del agente, y con la prueba corregida se califican como correctas.

| Ronda | Material | Qué | Dónde | Defecto | Origen |
|---|---|---|---|---|---|
| 2 | Minería · Ecuador | Dato calificado como mal | presupuesto · committee_commitments | CFO-4 | Arnés de pruebas |
| 7 | Control · Brasil | Dato calificado como mal | cierre · declared.status | — | — |

## Defectos

![Defectos](defectos-es.svg)

11 defectos registrados, cada uno con su origen, su corrección y la corrida que la verificó: 11 verificados y 0 por verificar. 6 vinieron del material, la clave o el arnés de pruebas, no de los agentes.

| Origen | Defectos |
|---|---|
| Instrucciones del agente | 4 |
| Material de prueba | 3 |
| Arnés de pruebas | 2 |
| Código | 1 |
| Clave de calificación | 1 |

| Agente | Defectos |
|---|---|
| Tomás | 6 |
| Clara | 4 |
| Áurea | 2 |
| Ninguno | 1 |

## Consumo y próximo paso

Las 11 rondas usaron 223,8 millones de tokens: 213,1 millones en las corridas calificadas y 10,7 en las que se repitieron después de corregir un defecto. En promedio, 5,1 millones por entidad.

El material es sintético. Si una versión es estable o de laboratorio lo dice esta evidencia, no su número: estable, con el piso del margen del 95 % en 95 % o más en señales y en datos sobre la corrida más reciente de cada entidad, y ninguna señal en los controles (decisión 0020).

---

La evidencia completa de cada ronda: [`tests/evidencias/familias/cfo/`](https://github.com/josenanez/criterio/tree/main/tests/evidencias/familias/cfo).
