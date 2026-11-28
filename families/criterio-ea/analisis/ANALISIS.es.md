# Análisis estadístico de las pruebas · familia EA

Generado por `scripts/analisis_familias.py` desde `tests/evidencias/familias/ea/` · ronda más reciente: 5 · [English](ANALISIS.md)

No se edita a mano: cada cifra sale de la evidencia y el análisis se regenera con cada ronda.

## En una mirada

La ronda más reciente, la 5, parcial, sobre 1 de las 9 entidades del material: 40 de 40 señales sembradas encontradas (margen del 95 %: 91,2–100 %) y 0 de más; 41 de 41 datos extraídos bien (100 %, margen del 95 %: 91,4–100 %); y 0 de 0 entidades de control sin ninguna señal.

Sumando las rondas 1–5, 396 de 396 señales encontradas, 1 de más y 616 de 621 datos bien. Las rondas repiten el mismo material: no son muestras independientes, y el margen se calcula sobre los casos de cada una.

## Qué se probó y cómo

En cada entidad corren el setup y el procesamiento de Ofelia —los comandos que procesan los documentos y escriben las fichas—, con un tope de tokens fijado antes de empezar, sobre un material que trae su clave aparte, que nadie ve. Los demás comandos calculan sobre esas fichas con el motor, que se prueba con cada cambio del repositorio. Las señales se comparan por su nombre y su clave; la extracción, campo por campo, contra lo que traen los documentos escritos. Las entidades de control no tienen ningún defecto sembrado: cualquier señal en ellas es una falla.

Cobertura: de las señales sembradas, cuántas encontró. Precisión: de las que levantó, cuántas eran correctas. Margen del 95 %: intervalo de confianza de Wilson sobre los casos.

|   |   |
|---|---|
| Rondas | 5; la más reciente, la 5, es parcial |
| Material | Banca · Panamá |
| Entidades de control |  |
| Corridas de una entidad | 19 |
| Señales sembradas | 396 |
| Datos calificados | 621 |

## Resultados acumulados · rondas 1–5

| Métrica | Casos | Resultado | Margen del 95 % |
|---|---|---|---|
| Señales · cobertura | 396 de 396 | 100 % | 99–100 % |
| Señales · precisión | 396 de 397 | 99,7 % | 98,5–100 % |
| Extracción · datos correctos | 616 de 621 | 99,2 % | 98,1–99,7 % |
| Control · sin ninguna señal | 6 de 7 | 85,7 % | 48,6–97,5 % |

## Evolución por ronda

![Evolución por ronda](evolucion-es.svg)

Una ronda que no corre todas las entidades es parcial: la primera, pequeña, antes de la completa, o una de verificación, que repite las corridas que un defecto corregido dejó pendientes.

| Ronda | Entidades | Señales · cobertura | Señales · precisión | Extracción | Control sin señales | Tokens | Defectos |
|---|---|---|---|---|---|---|---|
| 1 | 7 | 100 % | 94,7 % | 97,8 % | 3 de 4 | 11,3 M | 8 |
| 2 | 6 | 100 % | 100 % | 99,2 % | 2 de 2 | 9,9 M | 1 |
| 3 | 1 | 100 % | 100 % | 100 % | 0 de 0 | 5,6 M | 0 |
| 4 | 4 | 100 % | 100 % | 100 % | 1 de 1 | 22,4 M | 0 |
| 5 | 1 | 100 % | 100 % | 100 % | 0 de 0 | 5,6 M | 0 |

## La ronda más reciente · ronda 5

| Métrica | Casos | Resultado | Margen del 95 % |
|---|---|---|---|
| Señales · cobertura | 40 de 40 | 100 % | 91,2–100 % |
| Señales · precisión | 40 de 40 | 100 % | 91,2–100 % |
| Extracción · datos correctos | 41 de 41 | 100 % | 91,4–100 % |
| Control · sin ninguna señal | 0 de 0 | — | — |

## Por industria y país · ronda 5

| Material | Agentes | Señales | De más | Extracción | Tokens |
|---|---|---|---|---|---|
| Banca · Panamá | Ofelia | 40 de 40 | 0 | 41 de 41 | 5,6 M |

## Lo que falló, uno por uno · rondas 1–5

6 fallas en 19 corridas, cada una con el defecto que la explica: su origen dice si falló el agente o la prueba. Las cifras son las de la calificación original: 2 de esas fallas vinieron de la prueba —el arnés o la clave—, no del agente, y con la prueba corregida se califican como correctas.

| Ronda | Material | Qué | Dónde | Defecto | Origen |
|---|---|---|---|---|---|
| 1 | Control · Colombia | Señal de más | ["commitment_overdue", "compromiso:junta-directiva:2026-09-24:C-1"] | — | — |
| 1 | Control · Colombia | Dato calificado como mal | reuniones/junta-directiva-2026-09-24 · commitments | EA-7 | Instrucciones del agente |
| 1 | Control · Colombia | Dato calificado como mal | reuniones/junta-directiva-2026-09-24 · decisions | EA-8 | Instrucciones del agente |
| 1 | Cooperativas · Ecuador | Dato calificado como mal | reuniones/consejo-de-administracion-2026-09-24 · agreements | EA-6 | Instrucciones del agente |
| 2 | Banca · Colombia | Dato calificado como mal | reuniones/comite-de-presidencia-2026-10-05 · decisions | EA-9 | Material de prueba |
| 2 | Cooperativas · Ecuador | Dato calificado como mal | reuniones/comite-de-gerencia-2026-10-05 · decisions | EA-9 | Material de prueba |

## Defectos

![Defectos](defectos-es.svg)

9 defectos registrados, cada uno con su origen, su corrección y la corrida que la verificó: 9 verificados y 0 por verificar. 3 vinieron del material, la clave o el arnés de pruebas, no de los agentes.

| Origen | Defectos |
|---|---|
| Instrucciones del agente | 4 |
| Código | 2 |
| Clave de calificación | 1 |
| Arnés de pruebas | 1 |
| Material de prueba | 1 |

| Agente | Defectos |
|---|---|
| Ofelia | 9 |

## Consumo y próximo paso

Las 5 rondas usaron 56 millones de tokens: 54,7 millones en las corridas calificadas y 1,2 en las que se repitieron después de corregir un defecto. En promedio, 2,9 millones por entidad.

El material es sintético. Si una versión es estable o de laboratorio lo dice esta evidencia, no su número: estable, con el piso del margen del 95 % en 95 % o más en señales y en datos sobre la corrida más reciente de cada entidad, y ninguna señal en los controles (decisión 0020).

---

La evidencia completa de cada ronda: [`tests/evidencias/familias/ea/`](https://github.com/josenanez/criterio/tree/main/tests/evidencias/familias/ea).
