# Análisis estadístico de las pruebas · familia EA

Generado por `scripts/analisis_familias.py` desde `tests/evidencias/familias/ea/` · ronda completa más reciente: 2 · [English](ANALISIS.md)

No se edita a mano: cada cifra sale de la evidencia y el análisis se regenera con cada ronda.

## En una mirada

La ronda completa más reciente, la 2, sobre las 4 entidades del material: 85 de 85 señales sembradas encontradas (margen del 95 %: 95,6–100 %) y 0 de más; 144 de 146 datos extraídos bien (98,6 %, margen del 95 %: 95,1–99,7 %); y 2 de 2 entidades de control sin ninguna señal.

Sumando las rondas 1–2, 103 de 103 señales encontradas, 1 de más y 280 de 285 datos bien. Las rondas repiten el mismo material: no son muestras independientes, y el margen se calcula sobre los casos de cada una.

## Qué se probó y cómo

En cada entidad corren el setup y el procesamiento de Ofelia —los comandos que procesan los documentos y escriben las fichas—, con un tope de tokens fijado antes de empezar, sobre un material que trae su clave aparte, que nadie ve. Los demás comandos calculan sobre esas fichas con el motor, que se prueba con cada cambio del repositorio. Las señales se comparan por su nombre y su clave; la extracción, campo por campo, contra lo que traen los documentos escritos. Las entidades de control no tienen ningún defecto sembrado: cualquier señal en ellas es una falla.

Cobertura: de las señales sembradas, cuántas encontró. Precisión: de las que levantó, cuántas eran correctas. Margen del 95 %: intervalo de confianza de Wilson sobre los casos.

|   |   |
|---|---|
| Rondas | 2; la completa más reciente es la 2 |
| Material | Banca · Colombia, Cooperativas · Ecuador |
| Entidades de control | Control · Colombia, Control · Ecuador |
| Corridas de una entidad | 11 |
| Señales sembradas | 103 |
| Datos calificados | 285 |

## Resultados acumulados · rondas 1–2

| Métrica | Casos | Resultado | Margen del 95 % |
|---|---|---|---|
| Señales · cobertura | 103 de 103 | 100 % | 96,4–100 % |
| Señales · precisión | 103 de 104 | 99 % | 94,7–99,9 % |
| Extracción · datos correctos | 280 de 285 | 98,2 % | 95,9–99,3 % |
| Control · sin ninguna señal | 5 de 6 | 83,3 % | 43,6–97 % |

## Evolución por ronda

![Evolución por ronda](evolucion-es.svg)

| Ronda | Entidades | Señales · cobertura | Señales · precisión | Extracción | Control sin señales | Tokens | Defectos |
|---|---|---|---|---|---|---|---|
| 1 | 7 | 100 % | 94,7 % | 97,8 % | 3 de 4 | 11,3 M | 8 |
| 2 | 4 | 100 % | 100 % | 98,6 % | 2 de 2 | 6,4 M | 0 |

## La ronda completa más reciente · ronda 2

| Métrica | Casos | Resultado | Margen del 95 % |
|---|---|---|---|
| Señales · cobertura | 85 de 85 | 100 % | 95,6–100 % |
| Señales · precisión | 85 de 85 | 100 % | 95,6–100 % |
| Extracción · datos correctos | 144 de 146 | 98,6 % | 95,1–99,7 % |
| Control · sin ninguna señal | 2 de 2 | 100 % | 34,2–100 % |

## Por industria y país · ronda 2

| Material | Agentes | Señales | De más | Extracción | Tokens |
|---|---|---|---|---|---|
| Banca · Colombia | Ofelia | 50 de 50 | 0 | 50 de 51 | 1,6 M |
| Cooperativas · Ecuador | Ofelia | 35 de 35 | 0 | 44 de 45 | 1,6 M |
| Control · Colombia | Ofelia | 0 de 0 | 0 | 25 de 25 | 1,9 M |
| Control · Ecuador | Ofelia | 0 de 0 | 0 | 25 de 25 | 1,2 M |

## Lo que falló, uno por uno · rondas 1–2

6 fallas en 11 corridas, cada una con el defecto que la explica: su origen dice si falló el agente o la prueba. Las cifras son las de la calificación original: 0 de esas fallas vinieron de la prueba —el arnés o la clave—, no del agente, y con la prueba corregida se califican como correctas.

| Ronda | Material | Qué | Dónde | Defecto | Origen |
|---|---|---|---|---|---|
| 1 | Control · Colombia | Señal de más | ["commitment_overdue", "compromiso:junta-directiva:2026-09-24:C-1"] | — | — |
| 1 | Control · Colombia | Dato calificado como mal | reuniones/junta-directiva-2026-09-24 · commitments | EA-7 | Instrucciones del agente |
| 1 | Control · Colombia | Dato calificado como mal | reuniones/junta-directiva-2026-09-24 · decisions | EA-8 | Instrucciones del agente |
| 1 | Cooperativas · Ecuador | Dato calificado como mal | reuniones/consejo-de-administracion-2026-09-24 · agreements | EA-6 | Instrucciones del agente |
| 2 | Banca · Colombia | Dato calificado como mal | reuniones/comite-de-presidencia-2026-10-05 · decisions | — | — |
| 2 | Cooperativas · Ecuador | Dato calificado como mal | reuniones/comite-de-gerencia-2026-10-05 · decisions | — | — |

## Defectos

![Defectos](defectos-es.svg)

8 defectos registrados, cada uno con su origen, su corrección y la corrida que la verificó: 8 verificados y 0 por verificar. 2 vinieron del material, la clave o el arnés de pruebas, no de los agentes.

| Origen | Defectos |
|---|---|
| Instrucciones del agente | 4 |
| Código | 2 |
| Clave de calificación | 1 |
| Arnés de pruebas | 1 |

| Agente | Defectos |
|---|---|
| Ofelia | 8 |

## Consumo y próximo paso

Las 2 rondas usaron 18,9 millones de tokens: 17,7 millones en las corridas calificadas y 1,2 en las que se repitieron después de corregir un defecto. En promedio, 1,6 millones por entidad.

El material es sintético. Si una versión es estable o de laboratorio lo dice esta evidencia, no su número: estable, con el piso del margen del 95 % en 95 % o más en señales y en datos sobre la corrida más reciente de cada entidad, y ninguna señal en los controles (decisión 0020).

---

La evidencia completa de cada ronda: [`tests/evidencias/familias/ea/`](https://github.com/josenanez/criterio/tree/main/tests/evidencias/familias/ea).
