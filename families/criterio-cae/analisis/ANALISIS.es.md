# Análisis estadístico de las pruebas · familia CAE

Generado por `scripts/analisis_familias.py` desde `tests/evidencias/familias/cae/` · ronda más reciente: 1 · [English](ANALISIS.md)

No se edita a mano: cada cifra sale de la evidencia y el análisis se regenera con cada ronda.

## En una mirada

La ronda más reciente, la 1, parcial, sobre 1 de las 5 entidades del material: 22 de 25 señales sembradas encontradas (margen del 95 %: 70–95,9 %) y 2 de más; 35 de 72 datos extraídos bien (48,6 %, margen del 95 %: 37,4–60 %); y 0 de 0 entidades de control sin ninguna señal.

Sumando las rondas 1–1, 22 de 25 señales encontradas, 2 de más y 35 de 72 datos bien. Las rondas repiten el mismo material: no son muestras independientes, y el margen se calcula sobre los casos de cada una.

## Qué se probó y cómo

En cada entidad corren el setup y el procesamiento de Prudencia, Justo y Remedios —los comandos que procesan los documentos y escriben las fichas—, con un tope de tokens fijado antes de empezar, sobre un material que trae su clave aparte, que nadie ve. Los demás comandos calculan sobre esas fichas con el motor, que se prueba con cada cambio del repositorio. Las señales se comparan por su nombre y su clave; la extracción, campo por campo, contra lo que traen los documentos escritos. Las entidades de control no tienen ningún defecto sembrado: cualquier señal en ellas es una falla.

Cobertura: de las señales sembradas, cuántas encontró. Precisión: de las que levantó, cuántas eran correctas. Margen del 95 %: intervalo de confianza de Wilson sobre los casos.

|   |   |
|---|---|
| Rondas | 1; la más reciente, la 1, es parcial |
| Material | Banca · Colombia |
| Entidades de control |  |
| Corridas de una entidad | 1 |
| Señales sembradas | 25 |
| Datos calificados | 72 |

## Resultados acumulados · rondas 1–1

| Métrica | Casos | Resultado | Margen del 95 % |
|---|---|---|---|
| Señales · cobertura | 22 de 25 | 88 % | 70–95,9 % |
| Señales · precisión | 22 de 24 | 91,7 % | 74,1–97,7 % |
| Extracción · datos correctos | 35 de 72 | 48,6 % | 37,4–60 % |
| Control · sin ninguna señal | 0 de 0 | — | — |

## Evolución por ronda

![Evolución por ronda](evolucion-es.svg)

Una ronda que no corre todas las entidades es parcial: la primera, pequeña, antes de la completa, o una de verificación, que repite las corridas que un defecto corregido dejó pendientes.

| Ronda | Entidades | Señales · cobertura | Señales · precisión | Extracción | Control sin señales | Tokens | Defectos |
|---|---|---|---|---|---|---|---|
| 1 | 1 | 88 % | 91,7 % | 48,6 % | 0 de 0 | 11,3 M | 4 |

## La ronda más reciente · ronda 1

| Métrica | Casos | Resultado | Margen del 95 % |
|---|---|---|---|
| Señales · cobertura | 22 de 25 | 88 % | 70–95,9 % |
| Señales · precisión | 22 de 24 | 91,7 % | 74,1–97,7 % |
| Extracción · datos correctos | 35 de 72 | 48,6 % | 37,4–60 % |
| Control · sin ninguna señal | 0 de 0 | — | — |

## Por industria y país · ronda 1

| Material | Agentes | Señales | De más | Extracción | Tokens |
|---|---|---|---|---|---|
| Banca · Colombia | Justo, Prudencia, Remedios | 22 de 25 | 2 | 35 de 72 | 11,3 M |

## Lo que falló, uno por uno · rondas 1–1

42 fallas en 1 corridas, cada una con el defecto que la explica: su origen dice si falló el agente o la prueba. Las cifras son las de la calificación original: 1 de esas fallas vino de la prueba —el arnés o la clave—, no del agente, y con la prueba corregida se califican como correctas.

| Ronda | Material | Qué | Dónde | Defecto | Origen |
|---|---|---|---|---|---|
| 1 | Banca · Colombia | Señal no encontrada | ["finding_element_missing", "elementos:TR-01:H-01"] | — | — |
| 1 | Banca · Colombia | Señal no encontrada | ["finding_without_workpaper", "papel:TR-01:H-02"] | — | — |
| 1 | Banca · Colombia | Señal no encontrada | ["rating_inconsistent", "prioridad:TR-01:H-01"] | — | — |
| 1 | Banca · Colombia | Señal de más | ["report_differs_from_workpapers", "informe:TR-01:H-01"] | — | — |
| 1 | Banca · Colombia | Señal de más | ["report_differs_from_workpapers", "informe:TR-02:H-03"] | — | — |
| 1 | Banca · Colombia | Dato calificado como mal | trabajos · engagements[TR-01].findings[H-01].id | — | — |
| 1 | Banca · Colombia | Dato calificado como mal | trabajos · engagements[TR-01].findings[H-01].criteria | — | — |
| 1 | Banca · Colombia | Dato calificado como mal | trabajos · engagements[TR-01].findings[H-01].condition | — | — |
| 1 | Banca · Colombia | Dato calificado como mal | trabajos · engagements[TR-01].findings[H-01].effect | — | — |
| 1 | Banca · Colombia | Dato calificado como mal | trabajos · engagements[TR-01].findings[H-01].impact | — | — |
| 1 | Banca · Colombia | Dato calificado como mal | trabajos · engagements[TR-01].findings[H-01].likelihood | — | — |
| 1 | Banca · Colombia | Dato calificado como mal | trabajos · engagements[TR-01].findings[H-01].priority | — | — |
| 1 | Banca · Colombia | Dato calificado como mal | trabajos · engagements[TR-01].findings[H-01].workpapers | — | — |
| 1 | Banca · Colombia | Dato calificado como mal | trabajos · engagements[TR-01].findings[H-01].figures | — | — |
| 1 | Banca · Colombia | Dato calificado como mal | trabajos · engagements[TR-01].findings[H-01].source | — | — |
| 1 | Banca · Colombia | Dato calificado como mal | trabajos · engagements[TR-01].findings[H-02].id | — | — |
| 1 | Banca · Colombia | Dato calificado como mal | trabajos · engagements[TR-01].findings[H-02].criteria | — | — |
| 1 | Banca · Colombia | Dato calificado como mal | trabajos · engagements[TR-01].findings[H-02].condition | — | — |
| 1 | Banca · Colombia | Dato calificado como mal | trabajos · engagements[TR-01].findings[H-02].cause | — | — |
| 1 | Banca · Colombia | Dato calificado como mal | trabajos · engagements[TR-01].findings[H-02].effect | — | — |
| 1 | Banca · Colombia | Dato calificado como mal | trabajos · engagements[TR-01].findings[H-02].impact | — | — |
| 1 | Banca · Colombia | Dato calificado como mal | trabajos · engagements[TR-01].findings[H-02].likelihood | — | — |
| 1 | Banca · Colombia | Dato calificado como mal | trabajos · engagements[TR-01].findings[H-02].priority | — | — |
| 1 | Banca · Colombia | Dato calificado como mal | trabajos · engagements[TR-01].findings[H-02].workpapers | — | — |
| 1 | Banca · Colombia | Dato calificado como mal | trabajos · engagements[TR-01].findings[H-02].figures | — | — |
| 1 | Banca · Colombia | Dato calificado como mal | trabajos · engagements[TR-01].findings[H-02].source | — | — |
| 1 | Banca · Colombia | Dato calificado como mal | trabajos · engagements[TR-01].report_findings[H-01].figures | — | — |
| 1 | Banca · Colombia | Dato calificado como mal | trabajos · engagements[TR-01].report_findings[H-02].figures | — | — |
| 1 | Banca · Colombia | Dato calificado como mal | trabajos · engagements[TR-02].findings[H-03].id | — | — |
| 1 | Banca · Colombia | Dato calificado como mal | trabajos · engagements[TR-02].findings[H-03].criteria | — | — |
| 1 | Banca · Colombia | Dato calificado como mal | trabajos · engagements[TR-02].findings[H-03].condition | — | — |
| 1 | Banca · Colombia | Dato calificado como mal | trabajos · engagements[TR-02].findings[H-03].cause | — | — |
| 1 | Banca · Colombia | Dato calificado como mal | trabajos · engagements[TR-02].findings[H-03].effect | — | — |
| 1 | Banca · Colombia | Dato calificado como mal | trabajos · engagements[TR-02].findings[H-03].impact | — | — |
| 1 | Banca · Colombia | Dato calificado como mal | trabajos · engagements[TR-02].findings[H-03].likelihood | — | — |
| 1 | Banca · Colombia | Dato calificado como mal | trabajos · engagements[TR-02].findings[H-03].priority | — | — |
| 1 | Banca · Colombia | Dato calificado como mal | trabajos · engagements[TR-02].findings[H-03].workpapers | — | — |
| 1 | Banca · Colombia | Dato calificado como mal | trabajos · engagements[TR-02].findings[H-03].source | — | — |
| 1 | Banca · Colombia | Dato calificado como mal | trabajos · reviewed | CAE-4 | Instrucciones del agente |
| 1 | Banca · Colombia | Dato calificado como mal | seguimiento · evidence | CAE-2 | Material de prueba |
| 1 | Banca · Colombia | Dato calificado como mal | seguimiento · external_findings[RF-01].title | — | — |
| 1 | Banca · Colombia | Dato calificado como mal | seguimiento · reviewed | CAE-4 | Instrucciones del agente |

## Defectos

![Defectos](defectos-es.svg)

4 defectos registrados, cada uno con su origen, su corrección y la corrida que la verificó: 0 verificados y 4 por verificar. 3 vinieron del material, la clave o el arnés de pruebas, no de los agentes.

| Origen | Defectos |
|---|---|
| Material de prueba | 2 |
| Clave de calificación | 1 |
| Instrucciones del agente | 1 |

| Agente | Defectos |
|---|---|
| Remedios | 3 |
| Justo | 2 |

## Consumo y próximo paso

Las 1 rondas usaron 11,3 millones de tokens: 11,3 millones en las corridas calificadas y 0 en las que se repitieron después de corregir un defecto. En promedio, 11,3 millones por entidad.

El material es sintético. Si una versión es estable o de laboratorio lo dice esta evidencia, no su número: estable, con el piso del margen del 95 % en 95 % o más en señales y en datos sobre la corrida más reciente de cada entidad, y ninguna señal en los controles (decisión 0020).

---

La evidencia completa de cada ronda: [`tests/evidencias/familias/cae/`](https://github.com/josenanez/criterio/tree/main/tests/evidencias/familias/cae).
