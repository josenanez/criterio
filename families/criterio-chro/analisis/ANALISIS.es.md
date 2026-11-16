# Análisis estadístico de las pruebas · familia CHRO

Generado por `scripts/analisis_familias.py` desde `tests/evidencias/familias/chro/` · ronda más reciente: 2 · [English](ANALISIS.md)

No se edita a mano: cada cifra sale de la evidencia y el análisis se regenera con cada ronda.

## En una mirada

La ronda más reciente, la 2, parcial, sobre 2 de las 5 entidades del material: 30 de 30 señales sembradas encontradas (margen del 95 %: 88,6–100 %) y 0 de más; 4 de 4 datos extraídos bien (100 %, margen del 95 %: 51–100 %); y 1 de 1 entidades de control sin ninguna señal.

Sumando las rondas 1–2, 59 de 60 señales encontradas, 2 de más y 4 de 8 datos bien. Las rondas repiten el mismo material: no son muestras independientes, y el margen se calcula sobre los casos de cada una.

## Qué se probó y cómo

En cada entidad corren el setup y el procesamiento de Norma y Cándido —los comandos que procesan los documentos y escriben las fichas—, con un tope de tokens fijado antes de empezar, sobre un material que trae su clave aparte, que nadie ve. Los demás comandos calculan sobre esas fichas con el motor, que se prueba con cada cambio del repositorio. Las señales se comparan por su nombre y su clave; la extracción, campo por campo, contra lo que traen los documentos escritos. Las entidades de control no tienen ningún defecto sembrado: cualquier señal en ellas es una falla.

Cobertura: de las señales sembradas, cuántas encontró. Precisión: de las que levantó, cuántas eran correctas. Margen del 95 %: intervalo de confianza de Wilson sobre los casos.

|   |   |
|---|---|
| Rondas | 2; la más reciente, la 2, es parcial |
| Material | Banca · Colombia |
| Entidades de control | Control · Colombia |
| Corridas de una entidad | 4 |
| Señales sembradas | 60 |
| Datos calificados | 8 |

## Resultados acumulados · rondas 1–2

| Métrica | Casos | Resultado | Margen del 95 % |
|---|---|---|---|
| Señales · cobertura | 59 de 60 | 98,3 % | 91,1–99,8 % |
| Señales · precisión | 59 de 61 | 96,7 % | 88,8–99,1 % |
| Extracción · datos correctos | 4 de 8 | 50 % | 21,5–78,5 % |
| Control · sin ninguna señal | 1 de 2 | 50 % | 9,4–90,6 % |

## Evolución por ronda

![Evolución por ronda](evolucion-es.svg)

Una ronda que no corre todas las entidades es parcial: la primera, pequeña, antes de la completa, o una de verificación, que repite las corridas que un defecto corregido dejó pendientes.

| Ronda | Entidades | Señales · cobertura | Señales · precisión | Extracción | Control sin señales | Tokens | Defectos |
|---|---|---|---|---|---|---|---|
| 1 | 2 | 96,7 % | 93,5 % | 0 % | 0 de 1 | 16,5 M | 5 |
| 2 | 2 | 100 % | 100 % | 100 % | 1 de 1 | 16,7 M | 2 |

## La ronda más reciente · ronda 2

| Métrica | Casos | Resultado | Margen del 95 % |
|---|---|---|---|
| Señales · cobertura | 30 de 30 | 100 % | 88,6–100 % |
| Señales · precisión | 30 de 30 | 100 % | 88,6–100 % |
| Extracción · datos correctos | 4 de 4 | 100 % | 51–100 % |
| Control · sin ninguna señal | 1 de 1 | 100 % | 20,6–100 % |

## Por industria y país · ronda 2

| Material | Agentes | Señales | De más | Extracción | Tokens |
|---|---|---|---|---|---|
| Banca · Colombia | Cándido, Norma | 29 de 29 | 0 | 2 de 2 | 8,8 M |
| Control · Colombia | Cándido, Norma | 1 de 1 | 0 | 2 de 2 | 7,9 M |

## Lo que falló, uno por uno · rondas 1–2

7 fallas en 4 corridas, cada una con el defecto que la explica: su origen dice si falló el agente o la prueba. Las cifras son las de la calificación original: 3 de esas fallas vinieron de la prueba —el arnés o la clave—, no del agente, y con la prueba corregida se califican como correctas.

| Ronda | Material | Qué | Dónde | Defecto | Origen |
|---|---|---|---|---|---|
| 1 | Banca · Colombia | Señal no encontrada | ["profile_review_overdue", "revision:PC-01"] | CHRO-3 | Material de prueba |
| 1 | Banca · Colombia | Dato calificado como mal | perfiles · profiles | CHRO-1 | Clave de calificación |
| 1 | Banca · Colombia | Dato calificado como mal | seleccion · candidates | CHRO-2 | Clave de calificación |
| 1 | Control · Colombia | Señal de más | ["claim_without_support", "soporte:CAN-406:K1"] | CHRO-4 | Instrucciones del agente |
| 1 | Control · Colombia | Señal de más | ["protected_data_received", "protegido:CAN-406:fotografia"] | CHRO-4 | Instrucciones del agente |
| 1 | Control · Colombia | Dato calificado como mal | perfiles · profiles | — | — |
| 1 | Control · Colombia | Dato calificado como mal | seleccion · candidates | CHRO-5 | Instrucciones del agente |

## Defectos

![Defectos](defectos-es.svg)

7 defectos registrados, cada uno con su origen, su corrección y la corrida que la verificó: 6 verificados y 1 por verificar. 4 vinieron del material, la clave o el arnés de pruebas, no de los agentes.

| Origen | Defectos |
|---|---|
| Instrucciones del agente | 3 |
| Clave de calificación | 2 |
| Material de prueba | 1 |
| Arnés de pruebas | 1 |

| Agente | Defectos |
|---|---|
| Cándido | 4 |
| Norma | 3 |

## Consumo y próximo paso

Las 2 rondas usaron 33,2 millones de tokens: 33,2 millones en las corridas calificadas y 0 en las que se repitieron después de corregir un defecto. En promedio, 8,3 millones por entidad.

El material es sintético. Si una versión es estable o de laboratorio lo dice esta evidencia, no su número: estable, con el piso del margen del 95 % en 95 % o más en señales y en datos sobre la corrida más reciente de cada entidad, y ninguna señal en los controles (decisión 0020).

---

La evidencia completa de cada ronda: [`tests/evidencias/familias/chro/`](https://github.com/josenanez/criterio/tree/main/tests/evidencias/familias/chro).
