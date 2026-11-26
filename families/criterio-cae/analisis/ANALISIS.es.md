# Análisis estadístico de las pruebas · familia CAE

Generado por `scripts/analisis_familias.py` desde `tests/evidencias/familias/cae/` · ronda completa más reciente: 1 · [English](ANALISIS.md)

No se edita a mano: cada cifra sale de la evidencia y el análisis se regenera con cada ronda.

## En una mirada

La ronda completa más reciente, la 1, sobre las 5 entidades del material: 48 de 51 señales sembradas encontradas (margen del 95 %: 84–98 %) y 2 de más; 310 de 348 datos extraídos bien (89,1 %, margen del 95 %: 85,3–92 %); y 2 de 2 entidades de control sin ninguna señal.

Sumando las rondas 1–1, 48 de 51 señales encontradas, 2 de más y 310 de 348 datos bien. Las rondas repiten el mismo material: no son muestras independientes, y el margen se calcula sobre los casos de cada una.

## Qué se probó y cómo

En cada entidad corren el setup y el procesamiento de Prudencia, Justo y Remedios —los comandos que procesan los documentos y escriben las fichas—, con un tope de tokens fijado antes de empezar, sobre un material que trae su clave aparte, que nadie ve. Los demás comandos calculan sobre esas fichas con el motor, que se prueba con cada cambio del repositorio. Las señales se comparan por su nombre y su clave; la extracción, campo por campo, contra lo que traen los documentos escritos. Las entidades de control no tienen ningún defecto sembrado: cualquier señal en ellas es una falla.

Cobertura: de las señales sembradas, cuántas encontró. Precisión: de las que levantó, cuántas eran correctas. Margen del 95 %: intervalo de confianza de Wilson sobre los casos.

|   |   |
|---|---|
| Rondas | 1; la completa más reciente es la 1 |
| Material | Banca · Colombia, Cooperativas · Perú, Seguros · Brasil |
| Entidades de control | Control · Colombia, Control · Perú |
| Corridas de una entidad | 5 |
| Señales sembradas | 51 |
| Datos calificados | 348 |

## Resultados acumulados · rondas 1–1

| Métrica | Casos | Resultado | Margen del 95 % |
|---|---|---|---|
| Señales · cobertura | 48 de 51 | 94,1 % | 84–98 % |
| Señales · precisión | 48 de 50 | 96 % | 86,5–98,9 % |
| Extracción · datos correctos | 310 de 348 | 89,1 % | 85,3–92 % |
| Control · sin ninguna señal | 2 de 2 | 100 % | 34,2–100 % |

## Evolución por ronda

![Evolución por ronda](evolucion-es.svg)

| Ronda | Entidades | Señales · cobertura | Señales · precisión | Extracción | Control sin señales | Tokens | Defectos |
|---|---|---|---|---|---|---|---|
| 1 | 5 | 94,1 % | 96 % | 89,1 % | 2 de 2 | 55,2 M | 5 |

## La ronda completa más reciente · ronda 1

| Métrica | Casos | Resultado | Margen del 95 % |
|---|---|---|---|
| Señales · cobertura | 48 de 51 | 94,1 % | 84–98 % |
| Señales · precisión | 48 de 50 | 96 % | 86,5–98,9 % |
| Extracción · datos correctos | 310 de 348 | 89,1 % | 85,3–92 % |
| Control · sin ninguna señal | 2 de 2 | 100 % | 34,2–100 % |

## Por industria y país · ronda 1

| Material | Agentes | Señales | De más | Extracción | Tokens |
|---|---|---|---|---|---|
| Banca · Colombia | Justo, Prudencia, Remedios | 22 de 25 | 2 | 35 de 72 | 11,3 M |
| Cooperativas · Perú | Justo, Prudencia, Remedios | 14 de 14 | 0 | 72 de 72 | 11,5 M |
| Seguros · Brasil | Justo, Prudencia, Remedios | 12 de 12 | 0 | 67 de 68 | 11,1 M |
| Control · Colombia | Justo, Prudencia, Remedios | 0 de 0 | 0 | 68 de 68 | 10,4 M |
| Control · Perú | Justo, Prudencia, Remedios | 0 de 0 | 0 | 68 de 68 | 10,9 M |

## Lo que falló, uno por uno · rondas 1–1

43 fallas en 5 corridas, cada una con el defecto que la explica: su origen dice si falló el agente o la prueba. Las cifras son las de la calificación original: 1 de esas fallas vino de la prueba —el arnés o la clave—, no del agente, y con la prueba corregida se califican como correctas.

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

Las 1 rondas usaron 55,2 millones de tokens: 55,2 millones en las corridas calificadas y 0 en las que se repitieron después de corregir un defecto. En promedio, 11 millones por entidad.

El material es sintético. Si una versión es estable o de laboratorio lo dice esta evidencia, no su número: estable, con el piso del margen del 95 % en 95 % o más en señales y en datos sobre la corrida más reciente de cada entidad, y ninguna señal en los controles (decisión 0020).

---

La evidencia completa de cada ronda: [`tests/evidencias/familias/cae/`](https://github.com/josenanez/criterio/tree/main/tests/evidencias/familias/cae).
