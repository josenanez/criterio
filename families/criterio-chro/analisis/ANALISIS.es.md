# Análisis estadístico de las pruebas · familia CHRO

Generado por `scripts/analisis_familias.py` desde `tests/evidencias/familias/chro/` · ronda más reciente: 3 · [English](ANALISIS.md)

No se edita a mano: cada cifra sale de la evidencia y el análisis se regenera con cada ronda.

## En una mirada

La ronda más reciente, la 3, parcial, sobre 3 de las 5 entidades del material: 43 de 43 señales sembradas encontradas (margen del 95 %: 91,7–100 %) y 4 de más; 6 de 6 datos extraídos bien (100 %, margen del 95 %: 60,9–100 %); y 1 de 1 entidades de control sin ninguna señal.

Sumando las rondas 1–3, 103 de 104 señales encontradas, 6 de más y 11 de 16 datos bien. Las rondas repiten el mismo material: no son muestras independientes, y el margen se calcula sobre los casos de cada una.

## Qué se probó y cómo

En cada entidad corren el setup y el procesamiento de Norma y Cándido —los comandos que procesan los documentos y escriben las fichas—, con un tope de tokens fijado antes de empezar, sobre un material que trae su clave aparte, que nadie ve. Los demás comandos calculan sobre esas fichas con el motor, que se prueba con cada cambio del repositorio. Las señales se comparan por su nombre y su clave; la extracción, campo por campo, contra lo que traen los documentos escritos. Las entidades de control no tienen ningún defecto sembrado: cualquier señal en ellas es una falla.

Cobertura: de las señales sembradas, cuántas encontró. Precisión: de las que levantó, cuántas eran correctas. Margen del 95 %: intervalo de confianza de Wilson sobre los casos.

|   |   |
|---|---|
| Rondas | 3; la más reciente, la 3, es parcial |
| Material | Retail · México, Tecnología · Chile |
| Entidades de control | Control · Perú |
| Corridas de una entidad | 8 |
| Señales sembradas | 104 |
| Datos calificados | 16 |

## Resultados acumulados · rondas 1–3

| Métrica | Casos | Resultado | Margen del 95 % |
|---|---|---|---|
| Señales · cobertura | 103 de 104 | 99 % | 94,7–99,9 % |
| Señales · precisión | 103 de 109 | 94,5 % | 88,5–97,5 % |
| Extracción · datos correctos | 11 de 16 | 68,8 % | 44,4–85,9 % |
| Control · sin ninguna señal | 3 de 4 | 75 % | 30–95,5 % |

## Evolución por ronda

![Evolución por ronda](evolucion-es.svg)

Una ronda que no corre todas las entidades es parcial: la primera, pequeña, antes de la completa, o una de verificación, que repite las corridas que un defecto corregido dejó pendientes.

| Ronda | Entidades | Señales · cobertura | Señales · precisión | Extracción | Control sin señales | Tokens | Defectos |
|---|---|---|---|---|---|---|---|
| 1 | 2 | 96,7 % | 93,5 % | 0 % | 0 de 1 | 16,5 M | 5 |
| 2 | 2 | 100 % | 100 % | 100 % | 1 de 1 | 16,7 M | 2 |
| 3 | 4 | 100 % | 91,7 % | 87,5 % | 2 de 2 | 20,5 M | 2 |

## La ronda más reciente · ronda 3

| Métrica | Casos | Resultado | Margen del 95 % |
|---|---|---|---|
| Señales · cobertura | 43 de 43 | 100 % | 91,7–100 % |
| Señales · precisión | 43 de 47 | 91,5 % | 80–96,7 % |
| Extracción · datos correctos | 6 de 6 | 100 % | 60,9–100 % |
| Control · sin ninguna señal | 1 de 1 | 100 % | 20,6–100 % |

## Por industria y país · ronda 3

| Material | Agentes | Señales | De más | Extracción | Tokens |
|---|---|---|---|---|---|
| Retail · México | Cándido, Norma | 22 de 22 | 4 | 2 de 2 | 5,4 M |
| Tecnología · Chile | Cándido, Norma | 20 de 20 | 0 | 2 de 2 | 5,5 M |
| Control · Perú | Cándido, Norma | 1 de 1 | 0 | 1 de 2 | 4,7 M |
| Control · Perú | Cándido, Norma | 1 de 1 | 0 | 2 de 2 | 4,8 M |

## Lo que falló, uno por uno · rondas 1–3

12 fallas en 8 corridas, cada una con el defecto que la explica: su origen dice si falló el agente o la prueba. Las cifras son las de la calificación original: 8 de esas fallas vinieron de la prueba —el arnés o la clave—, no del agente, y con la prueba corregida se califican como correctas.

| Ronda | Material | Qué | Dónde | Defecto | Origen |
|---|---|---|---|---|---|
| 1 | Banca · Colombia | Señal no encontrada | ["profile_review_overdue", "revision:PC-01"] | CHRO-3 | Material de prueba |
| 1 | Banca · Colombia | Dato calificado como mal | perfiles · profiles | CHRO-1 | Clave de calificación |
| 1 | Banca · Colombia | Dato calificado como mal | seleccion · candidates | CHRO-2 | Clave de calificación |
| 1 | Control · Colombia | Señal de más | ["claim_without_support", "soporte:CAN-406:K1"] | CHRO-4 | Instrucciones del agente |
| 1 | Control · Colombia | Señal de más | ["protected_data_received", "protegido:CAN-406:fotografia"] | CHRO-4 | Instrucciones del agente |
| 1 | Control · Colombia | Dato calificado como mal | perfiles · profiles | — | — |
| 1 | Control · Colombia | Dato calificado como mal | seleccion · candidates | CHRO-5 | Instrucciones del agente |
| 3 | Control · Perú | Dato calificado como mal | perfiles · profiles | CHRO-8 | Material de prueba |
| 3 | Retail · México | Señal de más | ["essential_skill_missing", "elemento:PT-01:2_a_1_d"] | CHRO-8 | Material de prueba |
| 3 | Retail · México | Señal de más | ["essential_skill_missing", "elemento:PT-01:2_c_4_a"] | CHRO-8 | Material de prueba |
| 3 | Retail · México | Señal de más | ["essential_skill_missing", "elemento:PT-02:2_a_1_d"] | CHRO-8 | Material de prueba |
| 3 | Retail · México | Señal de más | ["essential_skill_missing", "elemento:PT-02:2_c_4_a"] | CHRO-8 | Material de prueba |

## Defectos

![Defectos](defectos-es.svg)

9 defectos registrados, cada uno con su origen, su corrección y la corrida que la verificó: 8 verificados y 1 por verificar. 6 vinieron del material, la clave o el arnés de pruebas, no de los agentes.

| Origen | Defectos |
|---|---|
| Instrucciones del agente | 3 |
| Clave de calificación | 2 |
| Material de prueba | 2 |
| Arnés de pruebas | 2 |

| Agente | Defectos |
|---|---|
| Cándido | 5 |
| Norma | 4 |

## Consumo y próximo paso

Las 3 rondas usaron 53,7 millones de tokens: 53,7 millones en las corridas calificadas y 0 en las que se repitieron después de corregir un defecto. En promedio, 6,7 millones por entidad.

El material es sintético. Si una versión es estable o de laboratorio lo dice esta evidencia, no su número: estable, con el piso del margen del 95 % en 95 % o más en señales y en datos sobre la corrida más reciente de cada entidad, y ninguna señal en los controles (decisión 0020).

---

La evidencia completa de cada ronda: [`tests/evidencias/familias/chro/`](https://github.com/josenanez/criterio/tree/main/tests/evidencias/familias/chro).
