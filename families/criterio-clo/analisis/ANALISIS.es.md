# Análisis estadístico de las pruebas · familia CLO

Generado por `scripts/analisis_familias.py` desde `tests/evidencias/familias/clo/` · ronda más reciente: 6 · [English](ANALISIS.md)

No se edita a mano: cada cifra sale de la evidencia y el análisis se regenera con cada ronda.

## En una mirada

La ronda más reciente, la 6, parcial, sobre 3 de las 18 entidades del material: 20 de 20 señales sembradas encontradas (margen del 95 %: 83,8–100 %) y 0 de más; 396 de 396 datos extraídos bien (100 %, margen del 95 %: 99–100 %); y 1 de 1 entidades de control sin ninguna señal.

Sumando las rondas 1–6, 128 de 128 señales encontradas, 0 de más y 3312 de 3328 datos bien. Las rondas repiten el mismo material: no son muestras independientes, y el margen se calcula sobre los casos de cada una.

## Qué se probó y cómo

En cada entidad corren el setup y el procesamiento de Fidel y Constanza —los comandos que procesan los documentos y escriben las fichas—, con un tope de tokens fijado antes de empezar, sobre un material que trae su clave aparte, que nadie ve. Los demás comandos calculan sobre esas fichas con el motor, que se prueba con cada cambio del repositorio. Las señales se comparan por su nombre y su clave; la extracción, campo por campo, contra lo que traen los documentos escritos. Las entidades de control no tienen ningún defecto sembrado: cualquier señal en ellas es una falla.

Cobertura: de las señales sembradas, cuántas encontró. Precisión: de las que levantó, cuántas eran correctas. Margen del 95 %: intervalo de confianza de Wilson sobre los casos.

|   |   |
|---|---|
| Rondas | 6; la más reciente, la 6, es parcial |
| Material | Banca · Brasil, Retail · Brasil |
| Entidades de control | Control · Brasil |
| Corridas de una entidad | 25 |
| Señales sembradas | 128 |
| Datos calificados | 3328 |

## Resultados acumulados · rondas 1–6

| Métrica | Casos | Resultado | Margen del 95 % |
|---|---|---|---|
| Señales · cobertura | 128 de 128 | 100 % | 97–100 % |
| Señales · precisión | 128 de 128 | 100 % | 97–100 % |
| Extracción · datos correctos | 3312 de 3328 | 99,5 % | 99,2–99,8 % |
| Control · sin ninguna señal | 11 de 11 | 100 % | 74,1–100 % |

## Evolución por ronda

![Evolución por ronda](evolucion-es.svg)

Una ronda que no corre todas las entidades es parcial: la primera, pequeña, antes de la completa, o una de verificación, que repite las corridas que un defecto corregido dejó pendientes.

| Ronda | Entidades | Señales · cobertura | Señales · precisión | Extracción | Control sin señales | Tokens | Defectos |
|---|---|---|---|---|---|---|---|
| 1 | 3 | 100 % | 100 % | 98,5 % | 2 de 2 | 19,1 M | 5 |
| 2 | 6 | 100 % | 100 % | 99,1 % | 2 de 2 | 43,7 M | 4 |
| 3 | 2 | 100 % | 100 % | 99,6 % | 1 de 1 | 11 M | 0 |
| 4 | 7 | 100 % | 100 % | 99,9 % | 3 de 3 | 21,6 M | 1 |
| 5 | 4 | 100 % | 100 % | 99,8 % | 2 de 2 | 12,1 M | 1 |
| 6 | 3 | 100 % | 100 % | 100 % | 1 de 1 | 9,3 M | 1 |

## La ronda más reciente · ronda 6

| Métrica | Casos | Resultado | Margen del 95 % |
|---|---|---|---|
| Señales · cobertura | 20 de 20 | 100 % | 83,8–100 % |
| Señales · precisión | 20 de 20 | 100 % | 83,8–100 % |
| Extracción · datos correctos | 396 de 396 | 100 % | 99–100 % |
| Control · sin ninguna señal | 1 de 1 | 100 % | 20,6–100 % |

## Por industria y país · ronda 6

| Material | Agentes | Señales | De más | Extracción | Tokens |
|---|---|---|---|---|---|
| Banca · Brasil | Constanza, Fidel | 10 de 10 | 0 | 132 de 132 | 3,3 M |
| Retail · Brasil | Constanza, Fidel | 10 de 10 | 0 | 132 de 132 | 2,9 M |
| Control · Brasil | Constanza, Fidel | 0 de 0 | 0 | 132 de 132 | 3,1 M |

## Lo que falló, uno por uno · rondas 1–6

16 fallas en 25 corridas, cada una con el defecto que la explica: su origen dice si falló el agente o la prueba. Las cifras son las de la calificación original: 4 de esas fallas vinieron de la prueba —el arnés o la clave—, no del agente, y con la prueba corregida se califican como correctas.

| Ronda | Material | Qué | Dónde | Defecto | Origen |
|---|---|---|---|---|---|
| 1 | Control · Colombia | Dato calificado como mal | contratos/CTR-501 · obligations | CLO-4 | Instrucciones del agente |
| 1 | Control · Colombia | Dato calificado como mal | contratos/CTR-502 · obligations | CLO-4 | Instrucciones del agente |
| 1 | Control · Colombia | Dato calificado como mal | contratos/CTR-503 · obligations | CLO-4 | Instrucciones del agente |
| 1 | Control · Colombia | Dato calificado como mal | contratos/CTR-504 · obligations | CLO-4 | Instrucciones del agente |
| 1 | Control · Colombia | Dato calificado como mal | contratos/CTR-505 · obligations | CLO-4 | Instrucciones del agente |
| 1 | Control · Colombia | Dato calificado como mal | cumplimiento · new_rules | CLO-5 | Arnés de pruebas |
| 2 | Banca · Colombia | Dato calificado como mal | contratos/CTR-101 · obligations | CLO-9 | Arnés de pruebas |
| 2 | Control · Colombia | Dato calificado como mal | cumplimiento · declared.status | CLO-6 | Instrucciones del agente |
| 2 | Control · Colombia | Dato calificado como mal | cumplimiento · declared.date | CLO-6 | Instrucciones del agente |
| 2 | Control · Colombia | Dato calificado como mal | cumplimiento · declared.source | CLO-6 | Instrucciones del agente |
| 2 | Control · Colombia | Dato calificado como mal | cumplimiento · new_rules | CLO-6 | Instrucciones del agente |
| 2 | Minería · Ecuador | Dato calificado como mal | contratos/CTR-405 · signed_on | CLO-8 | Instrucciones del agente |
| 2 | Minería · Ecuador | Dato calificado como mal | contratos/CTR-405 · signatories | CLO-7 | Clave de calificación |
| 3 | Control · Colombia | Dato calificado como mal | contratos/CTR-501 · obligations | CLO-9 | Arnés de pruebas |
| 4 | Control · Perú | Dato calificado como mal | contratos/CTR-902 · obligations | CLO-10 | Instrucciones del agente |
| 5 | Control · México | Dato calificado como mal | contratos/CTR-1502 · obligations | CLO-11 | Instrucciones del agente |

## Defectos

![Defectos](defectos-es.svg)

12 defectos registrados, cada uno con su origen, su corrección y la corrida que la verificó: 12 verificados y 0 por verificar. 5 vinieron del material, la clave o el arnés de pruebas, no de los agentes.

| Origen | Defectos |
|---|---|
| Instrucciones del agente | 5 |
| Arnés de pruebas | 4 |
| Código | 2 |
| Clave de calificación | 1 |

| Agente | Defectos |
|---|---|
| Fidel | 6 |
| Constanza | 5 |
| Ninguno | 1 |

## Consumo y próximo paso

Las 6 rondas usaron 119,3 millones de tokens: 116,8 millones en las corridas calificadas y 2,4 en las que se repitieron después de corregir un defecto. En promedio, 4,7 millones por entidad.

El material es sintético. Si una versión es estable o de laboratorio lo dice esta evidencia, no su número: estable, con el piso del margen del 95 % en 95 % o más en señales y en datos sobre la corrida más reciente de cada entidad, y ninguna señal en los controles (decisión 0020).

---

La evidencia completa de cada ronda: [`tests/evidencias/familias/clo/`](https://github.com/josenanez/criterio/tree/main/tests/evidencias/familias/clo).
