# Análisis estadístico de las pruebas · familia EA

Generado por `scripts/analisis_familias.py` desde `tests/evidencias/familias/ea/` · ronda completa más reciente: 1 · [English](ANALISIS.md)

No se edita a mano: cada cifra sale de la evidencia y el análisis se regenera con cada ronda.

## En una mirada

La ronda completa más reciente, la 1, sobre las 7 entidades del material: 18 de 18 señales sembradas encontradas (margen del 95 %: 82,4–100 %) y 1 de más; 136 de 139 datos extraídos bien (97,8 %, margen del 95 %: 93,8–99,3 %); y 3 de 4 entidades de control sin ninguna señal.

Sumando las rondas 1–1, 18 de 18 señales encontradas, 1 de más y 136 de 139 datos bien. Las rondas repiten el mismo material: no son muestras independientes, y el margen se calcula sobre los casos de cada una.

## Qué se probó y cómo

En cada entidad corren el setup y el procesamiento de Ofelia —los comandos que procesan los documentos y escriben las fichas—, con un tope de tokens fijado antes de empezar, sobre un material que trae su clave aparte, que nadie ve. Los demás comandos calculan sobre esas fichas con el motor, que se prueba con cada cambio del repositorio. Las señales se comparan por su nombre y su clave; la extracción, campo por campo, contra lo que traen los documentos escritos. Las entidades de control no tienen ningún defecto sembrado: cualquier señal en ellas es una falla.

Cobertura: de las señales sembradas, cuántas encontró. Precisión: de las que levantó, cuántas eran correctas. Margen del 95 %: intervalo de confianza de Wilson sobre los casos.

|   |   |
|---|---|
| Rondas | 1; la completa más reciente es la 1 |
| Material | Banca · Colombia, Cooperativas · Ecuador |
| Entidades de control | Control · Colombia, Control · Ecuador |
| Corridas de una entidad | 7 |
| Señales sembradas | 18 |
| Datos calificados | 139 |

## Resultados acumulados · rondas 1–1

| Métrica | Casos | Resultado | Margen del 95 % |
|---|---|---|---|
| Señales · cobertura | 18 de 18 | 100 % | 82,4–100 % |
| Señales · precisión | 18 de 19 | 94,7 % | 75,3–99,1 % |
| Extracción · datos correctos | 136 de 139 | 97,8 % | 93,8–99,3 % |
| Control · sin ninguna señal | 3 de 4 | 75 % | 30–95,5 % |

## Evolución por ronda

![Evolución por ronda](evolucion-es.svg)

| Ronda | Entidades | Señales · cobertura | Señales · precisión | Extracción | Control sin señales | Tokens | Defectos |
|---|---|---|---|---|---|---|---|
| 1 | 7 | 100 % | 94,7 % | 97,8 % | 3 de 4 | 11,3 M | 8 |

## La ronda completa más reciente · ronda 1

| Métrica | Casos | Resultado | Margen del 95 % |
|---|---|---|---|
| Señales · cobertura | 18 de 18 | 100 % | 82,4–100 % |
| Señales · precisión | 18 de 19 | 94,7 % | 75,3–99,1 % |
| Extracción · datos correctos | 136 de 139 | 97,8 % | 93,8–99,3 % |
| Control · sin ninguna señal | 3 de 4 | 75 % | 30–95,5 % |

## Por industria y país · ronda 1

| Material | Agentes | Señales | De más | Extracción | Tokens |
|---|---|---|---|---|---|
| Banca · Colombia | Ofelia | 10 de 10 | 0 | 17 de 17 | 1,4 M |
| Cooperativas · Ecuador | Ofelia | 4 de 4 | 0 | 16 de 17 | 1,7 M |
| Cooperativas · Ecuador | Ofelia | 4 de 4 | 0 | 17 de 17 | 1,8 M |
| Control · Colombia | Ofelia | 0 de 0 | 1 | 21 de 22 | 1,3 M |
| Control · Colombia | Ofelia | 0 de 0 | 0 | 21 de 22 | 1,5 M |
| Control · Colombia | Ofelia | 0 de 0 | 0 | 22 de 22 | 2,1 M |
| Control · Ecuador | Ofelia | 0 de 0 | 0 | 22 de 22 | 1,5 M |

## Lo que falló, uno por uno · rondas 1–1

4 fallas en 7 corridas, cada una con el defecto que la explica: su origen dice si falló el agente o la prueba. Las cifras son las de la calificación original: 0 de esas fallas vinieron de la prueba —el arnés o la clave—, no del agente, y con la prueba corregida se califican como correctas.

| Ronda | Material | Qué | Dónde | Defecto | Origen |
|---|---|---|---|---|---|
| 1 | Control · Colombia | Señal de más | ["commitment_overdue", "compromiso:junta-directiva:2026-09-24:C-1"] | — | — |
| 1 | Control · Colombia | Dato calificado como mal | reuniones/junta-directiva-2026-09-24 · commitments | EA-7 | Instrucciones del agente |
| 1 | Control · Colombia | Dato calificado como mal | reuniones/junta-directiva-2026-09-24 · decisions | EA-8 | Instrucciones del agente |
| 1 | Cooperativas · Ecuador | Dato calificado como mal | reuniones/consejo-de-administracion-2026-09-24 · agreements | EA-6 | Instrucciones del agente |

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

Las 1 rondas usaron 12,5 millones de tokens: 11,3 millones en las corridas calificadas y 1,2 en las que se repitieron después de corregir un defecto. En promedio, 1,6 millones por entidad.

El material es sintético. Si una versión es estable o de laboratorio lo dice esta evidencia, no su número: estable, con el piso del margen del 95 % en 95 % o más en señales y en datos sobre la corrida más reciente de cada entidad, y ninguna señal en los controles (decisión 0020).

---

La evidencia completa de cada ronda: [`tests/evidencias/familias/ea/`](https://github.com/josenanez/criterio/tree/main/tests/evidencias/familias/ea).
