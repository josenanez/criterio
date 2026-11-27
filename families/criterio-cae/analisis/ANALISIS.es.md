# Análisis estadístico de las pruebas · familia CAE

Generado por `scripts/analisis_familias.py` desde `tests/evidencias/familias/cae/` · ronda completa más reciente: 2 · [English](ANALISIS.md)

No se edita a mano: cada cifra sale de la evidencia y el análisis se regenera con cada ronda.

## En una mirada

La ronda completa más reciente, la 2, sobre las 5 entidades del material: 76 de 76 señales sembradas encontradas (margen del 95 %: 95,1–100 %) y 0 de más; 352 de 352 datos extraídos bien (100 %, margen del 95 %: 98,9–100 %); y 2 de 2 entidades de control sin ninguna señal.

Sumando las rondas 1–2, 124 de 127 señales encontradas, 2 de más y 662 de 700 datos bien. Las rondas repiten el mismo material: no son muestras independientes, y el margen se calcula sobre los casos de cada una.

## Qué se probó y cómo

En cada entidad corren el setup y el procesamiento de Prudencia, Justo y Remedios —los comandos que procesan los documentos y escriben las fichas—, con un tope de tokens fijado antes de empezar, sobre un material que trae su clave aparte, que nadie ve. Los demás comandos calculan sobre esas fichas con el motor, que se prueba con cada cambio del repositorio. Las señales se comparan por su nombre y su clave; la extracción, campo por campo, contra lo que traen los documentos escritos. Las entidades de control no tienen ningún defecto sembrado: cualquier señal en ellas es una falla.

Cobertura: de las señales sembradas, cuántas encontró. Precisión: de las que levantó, cuántas eran correctas. Margen del 95 %: intervalo de confianza de Wilson sobre los casos.

|   |   |
|---|---|
| Rondas | 2; la completa más reciente es la 2 |
| Material | Banca · Colombia, Cooperativas · Perú, Seguros · Brasil |
| Entidades de control | Control · Colombia, Control · Perú |
| Corridas de una entidad | 10 |
| Señales sembradas | 127 |
| Datos calificados | 700 |

## Resultados acumulados · rondas 1–2

| Métrica | Casos | Resultado | Margen del 95 % |
|---|---|---|---|
| Señales · cobertura | 124 de 127 | 97,6 % | 93,2–99,2 % |
| Señales · precisión | 124 de 126 | 98,4 % | 94,3–99,6 % |
| Extracción · datos correctos | 662 de 700 | 94,6 % | 92,6–96,1 % |
| Control · sin ninguna señal | 4 de 4 | 100 % | 51–100 % |

## Evolución por ronda

![Evolución por ronda](evolucion-es.svg)

| Ronda | Entidades | Señales · cobertura | Señales · precisión | Extracción | Control sin señales | Tokens | Defectos |
|---|---|---|---|---|---|---|---|
| 1 | 5 | 94,1 % | 96 % | 89,1 % | 2 de 2 | 55,2 M | 5 |
| 2 | 5 | 100 % | 100 % | 100 % | 2 de 2 | 53,6 M | 0 |

## La ronda completa más reciente · ronda 2

| Métrica | Casos | Resultado | Margen del 95 % |
|---|---|---|---|
| Señales · cobertura | 76 de 76 | 100 % | 95,1–100 % |
| Señales · precisión | 76 de 76 | 100 % | 95,1–100 % |
| Extracción · datos correctos | 352 de 352 | 100 % | 98,9–100 % |
| Control · sin ninguna señal | 2 de 2 | 100 % | 34,2–100 % |

## Por industria y país · ronda 2

| Material | Agentes | Señales | De más | Extracción | Tokens |
|---|---|---|---|---|---|
| Banca · Colombia | Justo, Prudencia, Remedios | 25 de 25 | 0 | 72 de 72 | 10,7 M |
| Cooperativas · Perú | Justo, Prudencia, Remedios | 26 de 26 | 0 | 72 de 72 | 10,4 M |
| Seguros · Brasil | Justo, Prudencia, Remedios | 25 de 25 | 0 | 72 de 72 | 10,8 M |
| Control · Colombia | Justo, Prudencia, Remedios | 0 de 0 | 0 | 68 de 68 | 11,1 M |
| Control · Perú | Justo, Prudencia, Remedios | 0 de 0 | 0 | 68 de 68 | 10,6 M |

## Lo que falló, uno por uno · rondas 1–2

43 fallas en 10 corridas, cada una con el defecto que la explica: su origen dice si falló el agente o la prueba. Las cifras son las de la calificación original: 1 de esas fallas vino de la prueba —el arnés o la clave—, no del agente, y con la prueba corregida se califican como correctas.

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
| 1 | Seguros · Brasil | Dato calificado como mal | plan · reviewed | CAE-5 | Instrucciones del agente |

## Defectos

![Defectos](defectos-es.svg)

5 defectos registrados, cada uno con su origen, su corrección y la corrida que la verificó: 5 verificados y 0 por verificar. 3 vinieron del material, la clave o el arnés de pruebas, no de los agentes.

| Origen | Defectos |
|---|---|
| Material de prueba | 2 |
| Instrucciones del agente | 2 |
| Clave de calificación | 1 |

| Agente | Defectos |
|---|---|
| Remedios | 3 |
| Justo | 2 |
| Prudencia | 1 |

## Consumo y próximo paso

Las 2 rondas usaron 108,8 millones de tokens: 108,8 millones en las corridas calificadas y 0 en las que se repitieron después de corregir un defecto. En promedio, 10,9 millones por entidad.

El material es sintético. Si una versión es estable o de laboratorio lo dice esta evidencia, no su número: estable, con el piso del margen del 95 % en 95 % o más en señales y en datos sobre la corrida más reciente de cada entidad, y ninguna señal en los controles (decisión 0020).

---

La evidencia completa de cada ronda: [`tests/evidencias/familias/cae/`](https://github.com/josenanez/criterio/tree/main/tests/evidencias/familias/cae).
