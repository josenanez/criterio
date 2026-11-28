# Análisis estadístico de las pruebas · familia CAE

Generado por `scripts/analisis_familias.py` desde `tests/evidencias/familias/cae/` · ronda más reciente: 3 · [English](ANALISIS.md)

No se edita a mano: cada cifra sale de la evidencia y el análisis se regenera con cada ronda.

## En una mirada

La ronda más reciente, la 3, parcial, sobre 1 de las 7 entidades del material: 26 de 26 señales sembradas encontradas (margen del 95 %: 87,1–100 %) y 0 de más; 72 de 72 datos extraídos bien (100 %, margen del 95 %: 94,9–100 %); y 0 de 0 entidades de control sin ninguna señal.

Sumando las rondas 1–3, 150 de 153 señales encontradas, 2 de más y 734 de 772 datos bien. Las rondas repiten el mismo material: no son muestras independientes, y el margen se calcula sobre los casos de cada una.

## Qué se probó y cómo

En cada entidad corren el setup y el procesamiento de Prudencia, Justo y Remedios —los comandos que procesan los documentos y escriben las fichas—, con un tope de tokens fijado antes de empezar, sobre un material que trae su clave aparte, que nadie ve. Los demás comandos calculan sobre esas fichas con el motor, que se prueba con cada cambio del repositorio. Las señales se comparan por su nombre y su clave; la extracción, campo por campo, contra lo que traen los documentos escritos. Las entidades de control no tienen ningún defecto sembrado: cualquier señal en ellas es una falla.

Cobertura: de las señales sembradas, cuántas encontró. Precisión: de las que levantó, cuántas eran correctas. Margen del 95 %: intervalo de confianza de Wilson sobre los casos.

|   |   |
|---|---|
| Rondas | 3; la más reciente, la 3, es parcial |
| Material | Banca · México |
| Entidades de control |  |
| Corridas de una entidad | 11 |
| Señales sembradas | 153 |
| Datos calificados | 772 |

## Resultados acumulados · rondas 1–3

| Métrica | Casos | Resultado | Margen del 95 % |
|---|---|---|---|
| Señales · cobertura | 150 de 153 | 98 % | 94,3–99,4 % |
| Señales · precisión | 150 de 152 | 98,7 % | 95,3–99,7 % |
| Extracción · datos correctos | 734 de 772 | 95,1 % | 93,3–96,4 % |
| Control · sin ninguna señal | 4 de 4 | 100 % | 51–100 % |

## Evolución por ronda

![Evolución por ronda](evolucion-es.svg)

Una ronda que no corre todas las entidades es parcial: la primera, pequeña, antes de la completa, o una de verificación, que repite las corridas que un defecto corregido dejó pendientes.

| Ronda | Entidades | Señales · cobertura | Señales · precisión | Extracción | Control sin señales | Tokens | Defectos |
|---|---|---|---|---|---|---|---|
| 1 | 5 | 94,1 % | 96 % | 89,1 % | 2 de 2 | 55,2 M | 5 |
| 2 | 5 | 100 % | 100 % | 100 % | 2 de 2 | 53,6 M | 0 |
| 3 | 1 | 100 % | 100 % | 100 % | 0 de 0 | 11 M | 0 |

## La ronda más reciente · ronda 3

| Métrica | Casos | Resultado | Margen del 95 % |
|---|---|---|---|
| Señales · cobertura | 26 de 26 | 100 % | 87,1–100 % |
| Señales · precisión | 26 de 26 | 100 % | 87,1–100 % |
| Extracción · datos correctos | 72 de 72 | 100 % | 94,9–100 % |
| Control · sin ninguna señal | 0 de 0 | — | — |

## Por industria y país · ronda 3

| Material | Agentes | Señales | De más | Extracción | Tokens |
|---|---|---|---|---|---|
| Banca · México | Justo, Prudencia, Remedios | 26 de 26 | 0 | 72 de 72 | 11 M |

## Lo que falló, uno por uno · rondas 1–3

43 fallas en 11 corridas, cada una con el defecto que la explica: su origen dice si falló el agente o la prueba. Las cifras son las de la calificación original: 1 de esas fallas vino de la prueba —el arnés o la clave—, no del agente, y con la prueba corregida se califican como correctas.

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

Las 3 rondas usaron 119,7 millones de tokens: 119,7 millones en las corridas calificadas y 0 en las que se repitieron después de corregir un defecto. En promedio, 10,9 millones por entidad.

El material es sintético. Si una versión es estable o de laboratorio lo dice esta evidencia, no su número: estable, con el piso del margen del 95 % en 95 % o más en señales y en datos sobre la corrida más reciente de cada entidad, y ninguna señal en los controles (decisión 0020).

---

La evidencia completa de cada ronda: [`tests/evidencias/familias/cae/`](https://github.com/josenanez/criterio/tree/main/tests/evidencias/familias/cae).
