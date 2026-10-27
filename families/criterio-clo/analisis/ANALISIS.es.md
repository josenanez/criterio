# Análisis estadístico de las pruebas · familia CLO

Generado por `scripts/analisis_familias.py` desde `tests/evidencias/familias/clo/` · ronda más reciente: 4 · [English](ANALISIS.md)

No se edita a mano: cada cifra sale de la evidencia y el análisis se regenera con cada ronda.

## En una mirada

La ronda más reciente, la 4, parcial, sobre 7 de las 12 entidades del material: 37 de 37 señales sembradas encontradas (margen del 95 %: 90,5–100 %) y 0 de más; 940 de 941 datos extraídos bien (99,9 %, margen del 95 %: 99,4–100 %); y 3 de 3 entidades de control sin ninguna señal.

Sumando las rondas 1–4, 88 de 88 señales encontradas, 0 de más y 2393 de 2408 datos bien. Las rondas repiten el mismo material: no son muestras independientes, y el margen se calcula sobre los casos de cada una.

## Qué se probó y cómo

Cada entidad corre todos los comandos de los dos agentes, con un tope de tokens fijado antes de empezar, sobre un material que trae su clave aparte: el agente nunca la ve. Las señales se comparan por su nombre y su clave; la extracción, campo por campo, contra lo que traen los documentos escritos. Las entidades de control no tienen ningún defecto sembrado: cualquier señal en ellas es una falla.

Cobertura: de las señales sembradas, cuántas encontró. Precisión: de las que levantó, cuántas eran correctas. Margen del 95 %: intervalo de confianza de Wilson sobre los casos.

|   |   |
|---|---|
| Rondas | 4; la más reciente, la 4, es parcial |
| Material | Banca · Perú, Minería · Chile, Minería · Perú, Retail · Chile |
| Entidades de control | Control · Chile, Control · Perú |
| Corridas de una entidad | 18 |
| Señales sembradas | 88 |
| Datos calificados | 2408 |

## Resultados acumulados · rondas 1–4

| Métrica | Casos | Resultado | Margen del 95 % |
|---|---|---|---|
| Señales · cobertura | 88 de 88 | 100 % | 95,8–100 % |
| Señales · precisión | 88 de 88 | 100 % | 95,8–100 % |
| Extracción · datos correctos | 2393 de 2408 | 99,4 % | 98,9–99,7 % |
| Control · sin ninguna señal | 8 de 8 | 100 % | 67,5–100 % |

## Evolución por ronda

![Evolución por ronda](evolucion-es.svg)

Una ronda que no corre todas las entidades es parcial: la primera, pequeña, antes de la completa, o una de verificación, que repite las corridas que un defecto corregido dejó pendientes.

| Ronda | Entidades | Señales · cobertura | Señales · precisión | Extracción | Control sin señales | Tokens | Defectos |
|---|---|---|---|---|---|---|---|
| 1 | 3 | 100 % | 100 % | 98,5 % | 2 de 2 | 19,1 M | 5 |
| 2 | 6 | 100 % | 100 % | 99,1 % | 2 de 2 | 43,7 M | 4 |
| 3 | 2 | 100 % | 100 % | 99,6 % | 1 de 1 | 11 M | 0 |
| 4 | 7 | 100 % | 100 % | 99,9 % | 3 de 3 | 21,6 M | 1 |

## La ronda más reciente · ronda 4

| Métrica | Casos | Resultado | Margen del 95 % |
|---|---|---|---|
| Señales · cobertura | 37 de 37 | 100 % | 90,5–100 % |
| Señales · precisión | 37 de 37 | 100 % | 90,5–100 % |
| Extracción · datos correctos | 940 de 941 | 99,9 % | 99,4–100 % |
| Control · sin ninguna señal | 3 de 3 | 100 % | 43,8–100 % |

## Por industria y país · ronda 4

| Material | Agentes | Señales | De más | Extracción | Tokens |
|---|---|---|---|---|---|
| Banca · Perú | Constanza, Fidel | 10 de 10 | 0 | 132 de 132 | 3,2 M |
| Minería · Chile | Constanza, Fidel | 9 de 9 | 0 | 132 de 132 | 3,1 M |
| Minería · Perú | Constanza, Fidel | 9 de 9 | 0 | 153 de 153 | 3,6 M |
| Retail · Chile | Constanza, Fidel | 9 de 9 | 0 | 132 de 132 | 3,5 M |
| Control · Chile | Constanza, Fidel | 0 de 0 | 0 | 132 de 132 | 3,3 M |
| Control · Perú | Constanza, Fidel | 0 de 0 | 0 | 131 de 132 | 3,2 M |
| Control · Perú | Fidel | 0 de 0 | 0 | 128 de 128 | 1,8 M |

## Lo que falló, uno por uno · rondas 1–4

15 fallas en 18 corridas, cada una con el defecto que la explica: su origen dice si falló el agente o la prueba. Las cifras son las de la calificación original: 4 de esas fallas vinieron de la prueba —el arnés o la clave—, no del agente, y con la prueba corregida se califican como correctas.

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

## Defectos

![Defectos](defectos-es.svg)

10 defectos registrados, cada uno con su origen, su corrección y la corrida que la verificó: 10 verificados y 0 por verificar. 4 vinieron del material, la clave o el arnés de pruebas, no de los agentes.

| Origen | Defectos |
|---|---|
| Instrucciones del agente | 4 |
| Arnés de pruebas | 3 |
| Código | 2 |
| Clave de calificación | 1 |

| Agente | Defectos |
|---|---|
| Fidel | 5 |
| Constanza | 4 |
| Ninguno | 1 |

## Consumo y próximo paso

Las 4 rondas usaron 97,9 millones de tokens: 95,4 millones en las corridas calificadas y 2,4 en las que se repitieron después de corregir un defecto. En promedio, 5,3 millones por entidad.

El material es sintético. El próximo paso es el despliegue en una organización, con su propia documentación.

---

La evidencia completa de cada ronda: [`tests/evidencias/familias/clo/`](https://github.com/josenanez/criterio/tree/main/tests/evidencias/familias/clo).
